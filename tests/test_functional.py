#! -*- coding: utf-8 -*-

""" Functional tests."""

import sys
import os

my_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(my_path)

# Library Imports
import unittest2
import mock
import random

# App Imports

from app import get_menu


class TestApp(unittest2.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_app_get_menu(self):
        res = get_menu()
        self.assertIn('Main Menu', res)

    def test_choose_correct_option(self):
        base = ('C', 'L', 'R', 'B', 'Q')
        selected = base[random.randint(0, len(base)-1)]
        get_option = mock.MagicMock(return_value=selected)
        option = get_option('C', 'L', 'R', 'B', 'Q', key='value')
        self.assertIn(option, base)

    def test_get_create_canvas_command(self):
        get_option = mock.MagicMock(return_value='C 3 4')
        option = get_option('C 3 4', key='value')
        self.assertIn(option, 'C 3 4')

    def test_create_canvas(self):
        base_canvas = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ]
        get_canvas = mock.MagicMock(return_value=base_canvas)
        printed = get_canvas('C 18 4')
        self.assertListEqual(printed, base_canvas)

    def test_draw_line(self):
        base_canvas = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ]

        get_canvas = mock.MagicMock(return_value=base_canvas)
        printed = get_canvas('L 1 2 6 2')
        self.assertListEqual(printed, base_canvas)

    def test_draw_rectangle(self):
        base_canvas = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ]

        get_canvas = mock.MagicMock(return_value=base_canvas)
        printed = get_canvas('R 16 1 18 3')
        self.assertListEqual(printed, base_canvas)

    def test_bucket_fill(self):
        base_canvas = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            [' ', '|', ' ', ' ', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x', 'x', 'x', 'x', 'x', '|', ' '],
            [' ', '|', 'x', 'x', 'x', 'x', 'x', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x', ' ', ' ', ' ', 'x', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x', 'x', 'x', 'x', 'x', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '|', ' '],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        ]

        get_canvas = mock.MagicMock(return_value=base_canvas)
        printed = get_canvas('B 10 3 o')
        self.assertListEqual(printed, base_canvas)


if __name__ == '__main__':
    unittest2.main()