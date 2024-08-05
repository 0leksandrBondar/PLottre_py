class DataRange:
    def __init__(self, min, max):
        self.min = min
        self.max = max


class Graph:
    def __init__(self, graph_data, data_range: DataRange, graph_name: str, visible=False):
        self.graph_data = graph_data
        self.data_range = data_range
        self.graph_name = graph_name
        self.visible = visible

    def __iter__(self):
        return iter(self.graph_data)


class GraphController:
    graph_list = []
    change_callback = None

    def add(self, graph: Graph):
        self.graph_list.append(graph)

    def get_data_graph(self, graph_name: str):
        graph = self.get_graph(graph_name)
        if graph:
            return graph.graph_data
        return None

    def exists(self, graph_name: str):
        return self.get_graph(graph_name) is not None

    def set_visible(self, visible: bool, graph_name: str):
        graph = self.get_graph(graph_name)
        if graph is not None:
            graph.visible = visible
            self.update()

    def get_visible_graphs(self):
        visible_graphs = []
        for graph in self.graph_list:
            if graph.visible:
                visible_graphs.append(graph)
        return visible_graphs


    def get_graph(self, graph_name: str):
        for graph in self.graph_list:
            if graph.graph_name == graph_name:
                return graph

        return None

    def on_change(self, callback):
        self.change_callback = callback

    def update(self):
        self.change_callback()


graphController = GraphController()
