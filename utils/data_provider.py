import numpy as np
import tkinter as tk
from pymavlink import mavutil
from geopy.distance import great_circle
from tkinter import filedialog
from model.graph import *


def debug_vect_from_tlog(log_file):
    mavlog = mavutil.mavlink_connection(log_file)
    positions = []
    selected_data = []
    home_coords = None

    while True:
        msg = mavlog.recv_match(blocking=False)
        if msg is None:
            break

        if msg.get_type() == 'GPS_GLOBAL_ORIGIN':
            home_coords = (msg.latitude / 1e7, msg.longitude / 1e7)

        if msg.get_type() == 'GLOBAL_POSITION_INT':
            if home_coords:
                current_coords = (msg.lat / 1e7, msg.lon / 1e7)
                distance_to_home = great_circle(current_coords, home_coords).meters
                positions.append((mavlog.timestamp, distance_to_home))

    mavlog = mavutil.mavlink_connection(log_file)

    while True:
        msg = mavlog.recv_match(blocking=False)
        if msg is None:
            break

        if msg.get_type() == 'DEBUG_VECT':
            x_ang = msg.x
            y_ang = msg.y
            RSSI = msg.z

            if positions:
                closest_time = min(positions, key=lambda p: abs(p[0] - mavlog.timestamp))
                distance_to_home = closest_time[1]
                selected_data.append((mavlog.timestamp, distance_to_home, x_ang, y_ang, RSSI))

    return np.array(selected_data)


# files_dict = {}

def get_file_name(file_path):
    return file_path.split("/")[-1]


def add_file(file: str):
    graphController.add(Graph(debug_vect_from_tlog(file), DataRange(0, 100), get_file_name(file)))


def get_dictionary(file: str):
    return graphController.get_data_graph(file)


def process_load(listbox):
    file_paths = filedialog.askopenfilenames(filetypes=[("TLOG files", "*.tlog"), ("All files", "*.*")])
    if file_paths:
        for file_path in file_paths:
            file_name = get_file_name(file_path)
            if not graphController.exists(file_name):
                listbox.insert(tk.END, file_name)
                listbox.user_data.append(file_name)
                add_file(file_path)
