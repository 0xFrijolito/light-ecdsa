import matplotlib.pyplot as plt

INF_POINT = None

class Point:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
    
    def plot(self) -> None:
        plt.plot(self.x, self.y, "o")

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
