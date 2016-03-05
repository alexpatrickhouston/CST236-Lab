"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle
is equilateral, scalene or iscoceles
"""
#pylint: disable= no-member,too-many-boolean-expressions,too-many-arguments

def get_triangle_type(a_side=0, b_side=0, c_side=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a_side: line a
    :type a_side: float or int or tuple or list or dict

    :param b_side: line b
    :type b_side: float

    :param c_side: line c
    :type c_side: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(a_side, (tuple, list)) and len(a_side) == 3:
        c_side = a_side[2]
        b_side = a_side[1]
        a_side = a_side[0]

    if isinstance(a_side, dict) and len(a_side.keys()) == 3:
        values = []
        for value in a_side.values():
            values.append(value)
        a_side = values[0]
        b_side = values[1]
        c_side = values[2]

    if not (isinstance(a_side, (int, float)) and isinstance(b_side, (int, float))
            and isinstance(c_side, (int, float))):
        return "invalid"

    if a_side <= 0 or b_side <= 0 or c_side <= 0:
        return "invalid"

    if a_side == b_side and b_side == c_side:
        return "equilateral"

    elif a_side == b_side or a_side == c_side or b_side == c_side:
        return "isosceles"
    else:
        return "scalene"


def get_rectangle_type(a_side=0, b_side=0, c_side=0, d_side=0):
    """
    Determine if the given rectangle is a rectangle or square

    :param a_side: line a
    :type a_side: float or int or tuple or list or dict

    :param b_side: line b
    :type b_side: float

    :param c_side: line c
    :type c_side: float

    :param d_side: line d
    :type d_side: float

    :return: "square", "rectangle" or "invalid"
    :rtype: str
    """
    if isinstance(a_side, (tuple, list)) and len(a_side) == 4:
        d_side = a_side[3]
        c_side = a_side[2]
        b_side = a_side[1]
        a_side = a_side[0]

    if isinstance(a_side, dict) and len(a_side.keys()) == 4:
        values = []
        for value in a_side.values():
            values.append(value)
        a_side = values[0]
        b_side = values[1]
        c_side = values[2]
        d_side = values[3]

    if not (isinstance(a_side, (int, float)) and isinstance(b_side, (int, float))
            and isinstance(c_side, (int, float)) and isinstance(d_side, (int, float))):
        return "invalid"

    if a_side <= 0 or b_side <= 0 or c_side <= 0 or d_side <= 0:
        return "invalid"

    if a_side == b_side and b_side == c_side and c_side == d_side:
        return "square"
    else:
        return "rectangle"


def get_4sided_type(a_angle=0, b_angle=0, c_angle=0, d_angle=0,
                    ab_side=0, bc_side=0, cd_side=0, da_side=0):
    """
    Determine if the given 4-sided object is a square, rectangle, rhombus or disconnect

    :param a_angle: line a
    :type a_angle: float or int or tuple or list or dict

    :param b_angle: line b
    :type b_angle: float

    :param c_angle: line c
    :type c_angle: float

    :param d_angle: line d
    :type d_angle: float

    :param d: corner ab
    :type ab_side: float

    :param d: corner bc
    :type bc_side: float

    :param d: corner cd
    :type cd_side: float

    :param d: corner da
    :type da_side: float

    :return: "square", "rhombus", "disconnect", "rectangle" or "invalid"
    :rtype: str
    """
    if isinstance(a_angle, (tuple, list)) and len(a_angle) == 8:
        da_side = a_angle[7]
        cd_side = a_angle[6]
        bc_side = a_angle[5]
        ab_side = a_angle[4]
        d_angle = a_angle[3]
        c_angle = a_angle[2]
        b_angle = a_angle[1]
        a_angle = a_angle[0]

    if isinstance(a_angle, dict) and len(a_angle.keys()) == 8:
        values = []
        for value in a_angle.values():
            values.append(value)
        a_angle = values[0]
        b_angle = values[1]
        c_angle = values[2]
        d_angle = values[3]
        ab_side = values[4]
        bc_side = values[5]
        cd_side = values[6]
        da_side = values[7]

    if not (isinstance(a_angle, (int, float)) and isinstance(b_angle, (int, float))
            and isinstance(c_angle, (int, float)) and
            isinstance(d_angle, (int, float)) and isinstance(ab_side, (int, float)) and
            isinstance(bc_side, (int, float)) and
            isinstance(cd_side, (int, float)) and isinstance(
                da_side, (int, float))):
        return "invalid"

    if a_angle <= 0 or b_angle <= 0 or c_angle <= 0 or \
                    d_angle <= 0 or ab_side <= 0 or bc_side <= 0 or cd_side <= 0 or da_side <= 0:
        return "invalid"

    if ab_side + bc_side + cd_side + da_side > 360:
        return "disconnect"
    if a_angle == b_angle and b_angle == c_angle and c_angle == d_angle:
        if ab_side == bc_side == cd_side == da_side:
            return "square"
        else:
            return "rhombus"

    else:
        return "rectangle"
