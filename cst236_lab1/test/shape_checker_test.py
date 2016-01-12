"""
Test for source.shape_checker
"""
from source.shape_checker import get_triangle_type
from source.shape_checker import get_rectangle_type
from source.shape_checker import get_4sided_type
from unittest import TestCase


class TestGetTriangleType(TestCase):
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_invalid_all_int(self):
        result = get_triangle_type(-1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(2, 1, 1)
        self.assertEqual(result, 'isosceles')


class TestGetRectangleType(TestCase):
    def test_get_rectangle_invalid_all_int(self):
        result = get_rectangle_type(-1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_square_all_int(self):
        result = get_rectangle_type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_get_rectangle_rectangle_all_int(self):
        result = get_rectangle_type(1, 2, 2, 1)
        self.assertEqual(result, 'rectangle')


class TestGet4sidedType(TestCase):
    def test_get_4sided_invalid_all_int(self):
        result = get_4sided_type(-1, 1, 1, 1, 1, 1, 1, 1)
        self.assertEqual(result, 'invalid')

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
