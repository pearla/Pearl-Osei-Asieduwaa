__author__ = 'pearl'

from numbers import Number
import math


def cylinder_surface_area(height: int, radius: int) -> Number:

    """
    calculate the area of cylinder
    :param height: the height of the cylinder
    :param radius: the radius of the cylinder
    :return: surface_area (unit^2 from height, radius)
    >>> cylinder_surface_area(8, 4)
    301.7142857142857
    """
    return 2*(22/7)*height*radius+2*(22/7)*radius**2


if __name__ == "__main__":
    print(cylinder_surface_area(8, 4))


def cone_volume(height: int, radius: int) -> Number:

    """
    calculate the volume of a cone from height and radius
    :param height: height of the cone
    :param radius: radius of the cone
    :return: volume (unit^3 from height, radius)
    >>>cone_volume(10, 5)
    261.90476190476187
    """
    return ((22/7)*radius**2*height)/3

if __name__ == "__main__":
    print(cone_volume(10, 5))


def cuboid_surface_area(length: int, width: int, height: int) -> Number:
    """
    calculate the area of a cuboid from length width and height
    :param length: length of the cuboid
    :param width: width of the cuboid
    :param height: height of the cuboid
    :return:surface_area (unit^2 from length, width, height)
    >>>cuboid_surface_area(8, 4, 5)
    184
    """
    return 2*(length*width + width*height + length*height)

if __name__ == "__main__":
    print(cuboid_surface_area(8, 4, 5))


def cube_volume(edge: Number) -> Number:
    """
    calculate the volume of a cube with side
    :param edge:side of the cube
    :return:volume(unity^3 from side)
    >>>cube_volume(6)
    216
    """
    return edge*edge*edge

if __name__ == "__main__":
    print(cube_volume(6))


def sphere_surface_area(radius: int) -> Number:
    """
    calculate the area of a sphere with radius
    :param radius: radius of the sphere
    :return:surface_area(unit^2 from radius)
    >>>sphere_surface_area(4)
    201.14285714285714
    """
    return 4*(22/7)*radius*radius

if __name__ == "__main__":
    print(sphere_surface_area(4))


def rectangle_area(width: int, length: int)-> Number:
    """
    calculate the area of a rectangle
    :param width:the width of the rectangle
    :param Length:the length of the rectangle
    :return:area(unit^2 from width, length)
    >>> rectangle_area(5, 6)
    30
    """
    return width*length

if __name__ == "__main__":
    print(rectangle_area(5, 6))


def triangle_area(width: int, length: int) -> Number:
    """
    calculate the area of a triangle with width and length
    :param width: width of the triangle
    :param length:length of the triangle
    :return:area(unit^2 from width, length)
    >>>triangle_area(4, 7)
    14
    """
    return (1/2)*(width*length)

if __name__ == "__main__":
    print(triangle_area(4, 7))


def pentagon_perimeter(side: Number) -> Number:
    """
    calculate the perimeter of a pentagon with equal side
    :param side: side of the pentagon
    :return:perimeter(same unit as side length)
    >>>pentagon_perimeter(5)
    25
    """
    return 5*side

if __name__ == "__main__":
    print(pentagon_perimeter(5))


def heptagon_perimeter(side: Number) -> Number:
    """
     calculate the perimeter of the a heptagon with equal side
    :param side:side of the heptagon
    :return:perimeter(same unit as side length)
    >>>heptagon_perimeter(7)
    49
    """
    return 7*side

if __name__ == "__main__":
    print(heptagon_perimeter(7))


def octagon_area(side:  Number) -> Number:
    """
    calculate the area of an octagon with equal side
    :param side:side of an octagon
    :return:area(unit^2 from side)
    >>>octagon_area(6)
    173.82337649086284
    """
    return 2*side*side*(1+math.sqrt(2))

if __name__ == "__main__":
    print(octagon_area(6))