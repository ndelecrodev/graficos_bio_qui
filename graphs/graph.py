import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')   # ou 'ggplot', 'bmh', 'fivethirtyeight'

class Graph():

    @staticmethod
    def build_graph(time: list[float], cells: list[float], title: str, xlabel: str, ylabel: str, grid: bool) -> None:
        plt.figure()
        plt.plot(time, cells, marker="o")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(grid)

    @staticmethod
    def plotar() -> None:
        plt.show()

    @staticmethod
    def build_in_file(name_file: str):
        plt.savefig(name_file)
        