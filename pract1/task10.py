import math

class Descr:
    def __init__(self,A,B,C,D):
        self.coordinates = (A,B,C,D)

    def __eq__(self, other):
        if isinstance(other, Descr):
            return (sorted(self.coordinates) == sorted(other.coordinates))
        else:
            return NotImplementedError
        
    def _get_side_lengths(self, coords):
        
        a = math.sqrt((coords[1][0] - coords[0][0]) ** 2 + (coords[1][1] - coords[0][1]) ** 2)
        b = math.sqrt((coords[2][0] - coords[1][0]) ** 2 + (coords[2][1] - coords[1][1]) ** 2)
        c = math.sqrt((coords[3][0] - coords[2][0]) ** 2 + (coords[3][1] - coords[2][1]) ** 2)
        d = math.sqrt((coords[0][0] - coords[3][0]) ** 2 + (coords[0][1] - coords[3][1]) ** 2)
        return [a, b, c, d]
    
    def _simillar_(self, other):

        if not isinstance(other,Descr):
            return NotImplementedError

        lengths_self = self._get_side_lengths(self.coordinates)
        lengths_other = self._get_side_lengths(other.coordinates)
        ratio = lengths_self[0] / lengths_other[0]

        for length_self, length_other in zip(lengths_self, lengths_other):
            if not math.isclose(length_self / length_other, ratio):
                return False
        return True

    def __str__(self):
        return f'Координаты = {self.coordinates}'

quad1 = Descr((0, 0), (2, 0), (2, 1), (0, 1))
quad2 = Descr((0, 0), (1, 0), (1, 0.5), (0, 0.5))
quad3 = Descr((0, 0), (2, 0), (2, 1), (0, 1))


print(quad1)
print(quad1 == quad3)
print(quad1._simillar_(quad2))  