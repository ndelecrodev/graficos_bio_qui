from graphs.graph import Graph
from tools.tool import Tool


n0 = 1000
time_duplication = 4

time = [0, 4, 8, 12, 16, 20, 24]
cells = [n0 * 2 ** (t / time_duplication) for t in time]

Graph.build_graph(time, cells, "Graph Etapa 3", "time (h)", "cells", True)
Graph.build_in_file("Graph Etapa 3")
Graph.build_graph(time, Tool.calcular_logs(cells), "Graph Etapa 4", "time (h)", "cells em log", True)
Graph.build_in_file("Graph Etapa 4")
Graph.plotar()