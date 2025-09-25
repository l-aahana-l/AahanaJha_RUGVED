from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, c):
        self.color = c
    def get_color(self):
        return self.color
    @abstractmethod
    def get_area(self):
        pass
class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side
    def get_area(self):
        return self.side * self.side
if __name__ == "__main__":
    sq = Square("red", 4.0)
    print("Color:", sq.get_color())
    print("Area:", sq.get_area())
