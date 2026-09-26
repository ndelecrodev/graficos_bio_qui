from math import log10

class Tool:
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def calcular_logs(list: list) -> list:
        list_log = []
        if 0 in list:
                return 0
        for i in list:
            list_log.append(log10(i))
        return list_log