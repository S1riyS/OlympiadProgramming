"""
5 kuy

Create a Vector object that supports addition, subtraction, dot products, and norms
"""
from functools import wraps


def check_length(func):
    @wraps
    def wrapper(*args, **kwargs):
        vector_1, vector_2 = args
        if len(vector_1.coordinates) == len(vector_2):
            return func(*args, **kwargs)
        raise Exception
    return wrapper


class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    @check_length
    def add(self, other):
        result = []
        for coord_1, coord_2 in zip(self.coordinates, other.coordinates):
            result.append(coord_1 + coord_2)
        print(result)
        return Vector(result)

    @check_length
    def subtract(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    @check_length
    def dot(self, other) -> int:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def norm(self) -> float:
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = a.add(b)
print(c.coordinates)
