from graphs.graph import Graph
from tools.tool import Tool

time = [4, 8, 12, 16, 20, 24]
cells = [1000, 5000, 10000, 20000, 35000, 65000]

Graph.build_graph(time, cells, "Graph Etapa 3", "time (h)", "cells", True)
Graph.build_in_file("Graph Etapa 1")
Graph.build_graph(time, Tool.calcular_logs(cells), "Graph Etapa 4", "time (h)", "cells em log", True)
Graph.build_in_file("Graph Etapa 2")
Graph.plotar()