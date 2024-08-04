import tkinter as tk

from matplotlib import pyplot as plt
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from model.graph import graphController


def configure_grid_weights(root, plot_frame):
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    plot_frame.grid_rowconfigure(1, weight=1)
    plot_frame.grid_columnconfigure(0, weight=1)


def create_plot_frame(root):
    plot_frame = tk.Frame(root)
    plot_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')
    return plot_frame


def create_bottom_frame(root):
    bottom_frame = tk.Frame(root)
    bottom_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='ew')
    bottom_frame.grid_columnconfigure(0, weight=1)
    bottom_frame.grid_columnconfigure(1, weight=1)
    return bottom_frame


def create_check_frame(bottom_frame):
    check_frame = tk.Frame(bottom_frame)
    check_frame.grid(row=0, column=0, sticky='w', padx=5, pady=5)
    return check_frame


def create_list_widgets_frame(bottom_frame):
    list_widgets_frame = tk.Frame(bottom_frame)
    list_widgets_frame.grid(row=0, column=1, sticky='e', padx=5, pady=5)
    return list_widgets_frame


def create_loaded_files_list_widget(time_frame):
    listbox = tk.Listbox(time_frame, exportselection=False, selectmode=tk.MULTIPLE, width=80, height=10)
    listbox.user_data = []
    listbox.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    return listbox


def create_load_button(time_frame, listbox, plot_frame):
    btn_open = tk.Button(
        time_frame,
        text="Load files",
        # command=lambda: open_file_dialog(listbox, plot_frame)
    )
    btn_open.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    return btn_open


def create_displayed_graph_list_widget(bottom_frame):
    displayed_graph_list_widget = tk.Listbox(bottom_frame, exportselection=False, selectmode=tk.MULTIPLE, width=80,
                                             height=10)
    displayed_graph_list_widget.user_data = []
    displayed_graph_list_widget.grid(row=0, column=2, columnspan=2, padx=5, pady=5)
    return displayed_graph_list_widget


def add_to_displayed_list(loaded_list, displayed_list):
    selected_labels = {loaded_list.get(i) for i in loaded_list.curselection()}
    current_labels = set(displayed_list.get(0, tk.END))

    labels_to_add = selected_labels - current_labels
    labels_to_remove = current_labels - selected_labels

    for label in labels_to_add:
        displayed_list.insert(tk.END, label)
        graphController.set_visible(True, label)

    for label in labels_to_remove:
        index = displayed_list.get(0, tk.END).index(label)
        displayed_list.delete(index)
        graphController.set_visible(False, label)


def create_plot_widget(parent_frame):
    fig, ax = plt.subplots(figsize=(12, 8))

    ax.set_xlabel('Расстояние до точки дома (м)')
    ax.set_ylabel('Значение')
    ax.set_title('График данных DEBUG_VECT по расстоянию до точки дома')
    ax.legend()
    ax.grid(True)

    plot_widget = FigureCanvasTkAgg(fig, master=parent_frame)
    plot_widget.draw()
    plot_widget.get_tk_widget().grid(row=1, column=0, columnspan=2, sticky='nsew')

    return fig, ax


def create_plot_toolbar(parent_frame, fig):
    plot_widget = FigureCanvasTkAgg(fig, master=parent_frame)
    plot_widget.get_tk_widget().grid(row=1, column=0, columnspan=2, sticky='nsew')

    toolbar_frame = tk.Frame(parent_frame)
    toolbar_frame.grid(row=0, column=0, columnspan=2, sticky='ew')

    toolbar = NavigationToolbar2Tk(plot_widget, toolbar_frame)
    toolbar.update()
    toolbar.pack(side=tk.TOP, fill=tk.X)
