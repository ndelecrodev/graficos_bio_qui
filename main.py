from graphs.graph import Graph
from tools.tool import Tool

n0 = 1000
time_duplication = 4

time = list[int](range(0,49,4))
cells = [n0 * 2 ** (t / time_duplication) for t in time]

Graph.build_graph(time, cells, "Gráfico Exponencial", "Tempo (h)", "Células", True)
Graph.build_in_file("Graph Etapa 3")
Graph.build_graph(time, Tool.calcular_logs(cells), "Gráfico Semilogarítmico", "Tempo (h)", "Células Log", True)
Graph.build_in_file("Graph Etapa 4")
Graph.plotar()