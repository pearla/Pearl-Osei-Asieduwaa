__author__ = 'pearl'

from numbers import Number


def square_perimeter(side: Number) -> Number:
    """
    Calculate perimeter of a square from side length .
    @param side: the side length
    @return: the perimeter (same units as side length)
    >>> square_perimeter(4)
    16
    """
    return 4*side


def square_area(side):
    """
    calculate area of a square from side length
    :param side: the side length
    :return:t the area (unit^2 from side)
    >>> square_area(4)
    16
    """
    return side*side


if __name__ == "__main__":
    print(square_area(7))
    print(square_area(4))

if __name__ == "__main__":
    sampleSide = 4
    print("area:", square_area(sampleSide), "perimeter", square_perimeter(sampleSide))


def octagon_area(side: Number) -> Number:
    """
    calculate area of an octagon from side length
    :param side: the side length
    :return:the area
    >>>octagonal_area(3)
    43.46
    """
    return 2*side*(1+(2^(1/2)))

if __name__ == "__main__":
    sampleSide = 3
    print("area:", octagonal_area(sampleSide))


if __name__ == "__main__":
    print(octagonal_area(side))