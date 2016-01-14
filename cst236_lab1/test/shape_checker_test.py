"""
Test for source.shape_checker
"""
from source.shape_checker import get_triangle_type
from source.shape_checker import get_rectangle_type
from source.shape_checker import get_4sided_type
from unittest import TestCase


class TestGetTriangleType(TestCase):
    """Normal Cases"""
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(2, 1, 1)
        self.assertEqual(result, 'isosceles')

    """Range Cases"""
    def test_get_triangle_invalida_all_int(self):
        result = get_triangle_type(-1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalidb_all_int(self):
        result = get_triangle_type(1, -1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalidc_all_int(self):
        result = get_triangle_type(1, 1, -1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalida0_all_int(self):
        result = get_triangle_type(0, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalidb0_all_int(self):
        result = get_triangle_type(1, 0, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalidc0_all_int(self):
        result = get_triangle_type(1, 1, 0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_all_int(self):
        result = get_triangle_type(-1, 1, 1)
        self.assertEqual(result, 'invalid')

    """Invalid data type cases"""
    def test_get_triangle_chara_all_int(self):
        result = get_triangle_type('a', 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_charb_all_int(self):
        result = get_triangle_type(1, 'b', 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_charc_all_int(self):
        result = get_triangle_type(1, 1, 'c')
        self.assertEqual(result, 'invalid')

class TestGetRectangleType(TestCase):
    """Normal cases"""
    def test_get_rectangle_square_all_int(self):
        result = get_rectangle_type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_get_rectangle_rectangle_all_int(self):
        result = get_rectangle_type(1, 2, 2, 1)
        self.assertEqual(result, 'rectangle')

    """Range Cases"""
    def test_get_rectangle_invalida_all_int(self):
        result = get_rectangle_type(-1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_invalidb_all_int(self):
        result = get_rectangle_type(1, -1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_invalidc_all_int(self):
        result = get_rectangle_type(1, 1, -1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_invalidd_all_int(self):
        result = get_rectangle_type(1, 1, 1, -1)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_invalida0_all_int(self):
        result = get_rectangle_type(0, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_invalidb0_all_int(self):
        result = get_rectangle_type(1, 0, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_invalidc0_all_int(self):
        result = get_rectangle_type(1, 1, 0, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_invalidd0_all_int(self):
        result = get_rectangle_type(1, 1, 1, 0)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_invalid_all_int(self):
        result = get_rectangle_type(-1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    """Invalid Data type"""
    def test_get_rectangle_chara_all_int(self):
        result = get_rectangle_type('a', 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_charb_all_int(self):
        result = get_rectangle_type(1, 'a', 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_charc_all_int(self):
        result = get_rectangle_type(1, 1, 'a', 1)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_chard_all_int(self):
        result = get_rectangle_type(1, 1, 1, 'a')
        self.assertEqual(result, 'invalid')


class TestGet4sidedType(TestCase):
    """Normal Cases"""
    def test_get_4sided_square_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    def test_get_4sided_rhombus_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 120, 60, 120, 60)
        self.assertEqual(result, 'rhombus')

    def test_get_4sided_disconnect_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 121, 60, 120, 60)
        self.assertEqual(result, 'disconnect')

    def test_get_4sided_rectangle_all_int(self):
        result = get_4sided_type(1, 2, 1, 2, 30, 60, 30, 60)
        self.assertEqual(result, 'rectangle')

    """Range Cases"""
    def test_get_4sided_invalida_all_int(self):
        result = get_4sided_type(-1, 1, 1, 1, 1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidb_all_int(self):
        result = get_4sided_type(1,-1, 1, 1, 1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidc_all_int(self):
        result = get_4sided_type(1, 1, -1, 1, 1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidd_all_int(self):
        result = get_4sided_type(1, 1, 1, -1, 1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidab_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, -1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidbc_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 1, -1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidcd_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 1, 1, -1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidda_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 1, 1, 1, -1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalida0_all_int(self):
        result = get_4sided_type(0, 1, 1, 1, 1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidb0_all_int(self):
        result = get_4sided_type(1, 0, 1, 1, 1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidc0_all_int(self):
        result = get_4sided_type(1, 1, 0, 1, 1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidd0_all_int(self):
        result = get_4sided_type(1, 1, 1, 0, 1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidab0_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 0, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidbc0_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 1, 0, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidcd0_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 1, 1, 0, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_invalidda0_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 1, 1, 1, 0)
        self.assertEqual(result, 'invalid')

    """Invalid Data types"""
    def test_get_4sided_chara_all_int(self):
        result = get_4sided_type('a', 1, 1, 1, 1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_charb_all_int(self):
        result = get_4sided_type(1, 'a', 1, 1, 1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_charc_all_int(self):
        result = get_4sided_type(1, 1, 'a', 1, 1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_chard_all_int(self):
        result = get_4sided_type(1, 1, 1, 'a', 1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_charab_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 'a', 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_charbc_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 1, 'a', 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_charcd_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 1, 1, 'a', 1)
        self.assertEqual(result, 'invalid')

    def test_get_4sided_charda_all_int(self):
        result = get_4sided_type(1, 1, 1, 1, 1, 1, 1, 'a')
        self.assertEqual(result, 'invalid')