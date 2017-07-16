#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import lispy
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_value(self):
        source = ''
        self.assertEqual('', lispy.s_expression(source))

        source = '100'
        self.assertEqual(100, lispy.s_expression(source))

    def test_expression(self):
        source = '()'
        self.assertEqual('nil', lispy.s_expression(source))


    def test_expression_list(self):
        source = '1 1 (+ 1 1)'
        self.assertEqual(['1', '1', '(+ 1 1)'], lispy.s_expression_list(source))


    def test_expression_calc(self):
        source = '(+ 1 (+ 1 1))'
        self.assertEqual(3, lispy.s_expression(source))

        source = '(- 1 (+ 1 1))'
        self.assertEqual(-1, lispy.s_expression(source))

        source = '(* 3 (+ 1 2))'
        self.assertEqual(9, lispy.s_expression(source))

        source = '(/ 1 (- 5 10))'
        self.assertEqual(- 0.2, lispy.s_expression(source))
        # self.assertEqual('1 / 5', lispy.s_expression(source))


    def test_calc(self):
        self.assertEqual(6, lispy.calc('+', [1, 2, 3]))
        self.assertEqual(-4, lispy.calc('-', [1, 2, 3]))
        self.assertEqual(6, lispy.calc('*', [1, 2, 3]))
        self.assertEqual(0.2, lispy.calc('/', [1, 5]))


if __name__ == '__main__':
    unittest.main()
