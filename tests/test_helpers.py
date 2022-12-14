# -*- coding: utf-8 -*-

from helpers import add

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_add(self):
        self.assertTrue(add(10, 20) == 30)


if __name__ == '__main__':
    unittest.main()
