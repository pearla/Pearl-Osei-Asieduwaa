__author__ = 'pearl'
from numbers import Number
import math
import numpy as mp


def cylinder_surface_area(height: int, radius: int) -> Number:

    """
    calculate the area of cylinder
    :param height: the height of the cylinder
    :param radius: the radius of the cylinder
    :return: surface_area (unit^2 from height, radius)
    >>> cylinder_surface_area(8, 4)
    301.59289474462014
    """
    return 2*mp.pi*height*radius+2*mp.pi*radius**2


def cone_volume(height: int, radius: int) -> Number:

    """
    calculate the volume of a cone from height and radius
    :param height: height of the cone
    :param radius: radius of the cone
    :return: volume (unit^3 from height, radius)
    >>>cone_volume(10, 5)
    261.79938779914943
    """
    return (mp.pi*radius**2*height)/3


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


def cube_volume(edge: Number) -> Number:
    """
    calculate the volume of a cube with side
    :param edge:side of the cube
    :return:volume(unity^3 from side)
    >>>cube_volume(6)
    216
    """
    return edge*edge*edge


def sphere_surface_area(radius: int) -> Number:
    """
    calculate the area of a sphere with radius
    :param radius: radius of the sphere
    :return:surface_area(unit^2 from radius)
    >>>sphere_surface_area(4)
    201.06192982974676
    """
    return 4*mp.pi*radius*radius


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


def triangle_area(base: int, height: int) -> Number:
    """
    calculate the area of a triangle with base, height and side
    :param base: base of the triangle
    :param height:height of the triangle
    :return:area(unit^2 from width, length)
    >>>triangle_area(6, 4)
    12
    """
    return (1/2)*(base*height)


def triangle_area1(base: int,  side1: int, side2: int) -> Number:
    """
    calculate the area of a triangle
    :param base: base of the triangle
    :param side1:side1 of the triangle
    :param side2: side2 of the triangle
    :return:area of a triangle(unit^2)
    >>>triangle_area(6,  5, 5)
    12
    """
    s = 1/2*(side1+side2+base)
    return math.sqrt(s*(s-side1)*(s-side2)*(s-base))


def pentagon_perimeter(side: Number) -> Number:
    """
    calculate the perimeter of a pentagon with equal side
    :param side: side of the pentagon
    :return:perimeter(same unit as side length)
    >>>pentagon_perimeter(5)
    25
    """
    return 5*side


def heptagon_perimeter(side: Number) -> Number:
    """
     calculate the perimeter of the a heptagon with equal side
    :param side:side of the heptagon
    :return:perimeter(same unit as side length)
    >>>heptagon_perimeter(7)
    49
    """
    return 7*side


def octagon_area(side:  Number) -> Number:
    """
    calculate the area of an octagon with equal side
    :param side:side of an octagon
    :return:area(unit^2 from side)
    >>>octagon_area(6)
    173.82337649086284
    """
    return 2*side*side*(1+math.sqrt(2))


def circle_area(radius: int) -> Number:
    """
    calculate the area of a circle
    :param radius: radius of the circle
    :return:circle_area(unit^2)
    >>>circle_area(7)
    153.93804002589985
    """
    return mp.pi*radius*radius


def trapezium_area(length: int, width: int, height: int) -> Number:
    """
    calculate the area of a trapezium
    :param length: length of the trapezium
    :param width: width of the trapezium
    :param height: height of the trapezium
    :return:trapezium_area(unit^2)
    >>>trapezium_area(5, 3, 6)
    45
    """
    return (length*width*height)*1/2


if __name__ == "__main__":
    print("surface_area of a cylinder:", cylinder_surface_area(8, 4))
    print("volume of a cone:", cone_volume(10, 5))
    print("surface_area of a cuboid:", cuboid_surface_area(8, 4, 5))
    print("volume of a cube:", cube_volume(6))
    print("surface_area of a sphere:", sphere_surface_area(4))
    print("area of a rectangle:", rectangle_area(5, 6))
    print("area of a triangle:", triangle_area(6, 4))
    print("area1 of a triangle:", triangle_area1(6, 5, 5))
    print("perimeter of a pentagon:", pentagon_perimeter(5))
    print("perimeter of a heptagon:", heptagon_perimeter(7))
    print("area of an octagon:", octagon_area(6))
    print("area of a circle:", circle_area(7))
    print("are of a trapezium:", trapezium_area(5, 3, 6))
