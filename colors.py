class Color():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def set(c:int):
        c = str(c)
        color = "\033[38;5;"+ c +"m"
        return color

