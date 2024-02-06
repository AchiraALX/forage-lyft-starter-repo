#!/usr/bin/env python3


"""Test for Carrigan
"""

import unittest

from car_parts.tires.carrigan import Carrigan



class TestCarrigan(unittest.TestCase):
    """Test carrigan
    """

    def test_needs_service_true(self):
        tire_stats = [0, 0.9, 0, 0]
        tire = Carrigan(tire_stats)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_stats = [0, 0.8, 0, 0]
        tire = Carrigan(tire_stats)
        self.assertFalse(tire.needs_service())

