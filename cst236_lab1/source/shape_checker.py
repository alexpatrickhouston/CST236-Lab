"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or iscoceles
"""


def get_triangle_type(a=0, b=0, c=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 3:
        c = a[2]
        b = b[1]
        a = a[1]

    if isinstance(a, dict) and len(a.keys()) == 3:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"

    if a == b and b == c:
        return "equilateral"

    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"


def get_rectangle_type(a=0, b=0, c=0, d=0):
    """
    Determine if the given rectangle is a rectangle or square

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :param d: line d
    :type d: float

    :return: "square", "rectangle" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 4:
        d = a[3]
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 4:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]
        d = values[3]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(
            d, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "invalid"

    if a == b and b == c and c == d:
        return "square"
    else:
        return "rectangle"


def get_4sided_type(a=0, b=0, c=0, d=0, ab=0, bc=0, cd=0, da=0):
    """
    Determine if the given 4-sided object is a square, rectangle, rhombus or disconnect

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :param d: line d
    :type d: float

    :param d: corner ab
    :type ab: float

    :param d: corner bc
    :type bc: float

    :param d: corner cd
    :type cd: float

    :param d: corner da
    :type da: float

    :return: "square", "rhombus", "disconnect", "rectangle" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 8:
        da = a[7]
        cd = a[6]
        bc = a[5]
        ab = a[4]
        d = a[3]
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 8:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]
        d = values[3]
        ab = values[4]
        bc = values[5]
        cd = values[6]
        da = values[7]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and
            isinstance(d, (int, float)) and isinstance(ab, (int, float)) and isinstance(bc, (
            int, float)) and isinstance(cd, (int, float)) and isinstance(
            da, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0 or ab <= 0 or bc <= 0 or cd <= 0 or da <= 0:
        return "invalid"

    if ab + bc + cd + da > 360:
        return "disconnect"
    if a == b and b == c and c == d:
        if ab == bc == cd == da:
            return "square"
        else:
            return "rhombus"

    else:
        return "rectangle"
