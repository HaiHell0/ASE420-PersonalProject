# -*- coding: utf-8 -*-

from core import Arith

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_arith(self):
        self.assertTrue(Arith().add(10, 20) == 30)


if __name__ == '__main__':
    unittest.main()
