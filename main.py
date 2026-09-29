from graphs.graph import Graph
from tools.tool import Tool



Graph.build_graph(time, cells, "Graph Etapa 3", "time (h)", "cells", True)
Graph.build_in_file("Graph Etapa 3")
Graph.build_graph(time, Tool.calcular_logs(cells), "Graph Etapa 4", "time (h)", "cells em log", True)
Graph.build_in_file("Graph Etapa 4")
Graph.plotar()