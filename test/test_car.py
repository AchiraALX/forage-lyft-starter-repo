#!/usr/bin/env python3


"""Test cars
"""

from datetime import date
import unittest
from car_factory import CarFactory


factory = CarFactory()


class TestCars(unittest.TestCase):
    """ Test the calliope
    """

    def test_calliope_battery_should_be_serviced(self):
        """Test the calliope battery"""
        last_service_date = date.today().replace(year=date.today().year - 3)
        current_date = date.today()
        current_mileage = 0
        last_service_mileage = 0
        car = factory.create_calliope(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_calliope_battery_should_not_be_serviced(self):
        """Test the calliope battery should not be serviced"""
        last_service_date = date.today().replace(year=date.today().year - 1)
        current_date = date.today()
        current_mileage = 0
        last_service_mileage = 0
        car = factory.create_calliope(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_calliope_engine_should_be_serviced(self):
        """Test calliope engine should be serviced"""
        last_service_date = date.today()
        current_date = date.today()
        current_mileage = 30002
        last_service_mileage = 0
        car = factory.create_calliope(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_calliope_engine_should_not_be_serviced(self):
        """ Calliope engine should not be serviced"""
        last_service_date = date.today()
        current_date = date.today()
        current_mileage = 30000
        last_service_mileage = 0
        car = factory.create_calliope(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_glissade_battery_should_be_serviced(self):
        """Test the glissade battery"""
        last_service_date = date.today().replace(year=date.today().year - 3)
        current_date = date.today()
        current_mileage = 0
        last_service_mileage = 0
        car = factory.create_glissade(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_glissade_battery_should_not_be_serviced(self):
        """Test the glissade battery should not be serviced"""
        last_service_date = date.today().replace(year=date.today().year - 1)
        current_date = date.today()
        current_mileage = 0
        last_service_mileage = 0
        car = factory.create_glissade(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_glissade_engine_should_be_serviced(self):
        """Test glissade engine should be serviced"""
        last_service_date = date.today()
        current_date = date.today()
        current_mileage = 60001
        last_service_mileage = 0
        car = factory.create_glissade(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_glissade_engine_should_not_be_serviced(self):
        """ Glissade engine should not be serviced"""
        last_service_date = date.today()
        current_date = date.today()
        current_mileage = 60000
        last_service_mileage = 0
        car = factory.create_glissade(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_palindrome_battery_should_be_serviced(self):
        """Test the palindrome battery"""
        last_service_date = date.today().replace(year=date.today().year - 3)
        current_date = date.today()
        car = factory.create_palindrome(
            current_date=current_date,
            last_service_date=last_service_date,
            warning_light_on=False
        )
        self.assertTrue(car.needs_service())

    def test_palindrome_battery_should_not_be_serviced(self):
        """Test the palindrome battery should not be serviced"""
        last_service_date = date.today().replace(year=date.today().year - 1)
        current_date = date.today()
        car = factory.create_palindrome(
            current_date=current_date,
            last_service_date=last_service_date,
            warning_light_on=False)
        self.assertFalse(car.needs_service())

    def test_palindrome_engine_should_be_serviced(self):
        """Test palindrome engine should be serviced"""
        last_service_date = date.today()
        current_date = date.today()
        car = factory.create_palindrome(
            current_date=current_date,
            last_service_date=last_service_date,
            warning_light_on=True)
        self.assertTrue(car.needs_service())

    def test_palindrome_engine_should_not_be_serviced(self):
        """ Glissade engine should not be serviced"""
        last_service_date = date.today()
        current_date = date.today()
        car = factory.create_palindrome(
            current_date=current_date,
            last_service_date=last_service_date,
            warning_light_on=False)
        self.assertFalse(car.needs_service())

    def test_rorschach_battery_should_be_serviced(self):
        """Test the rorschach battery"""
        last_service_date = date.today().replace(year=date.today().year - 4)
        current_date = date.today()
        last_service_mileage = 0
        current_mileage = 0
        car = factory.create_rorschach(
            current_date=current_date,
            last_service_date=last_service_date,
            last_service_mileage=last_service_mileage,
            current_mileage=current_mileage
        )
        self.assertTrue(car.needs_service())

    def test_rorschach_battery_should_not_be_serviced(self):
        """Test the rorschach battery should not be serviced"""
        last_service_date = date.today().replace(year=date.today().year - 1)
        current_date = date.today()
        last_service_mileage = 0
        current_mileage = 0
        car = factory.create_rorschach(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage
        )
        self.assertFalse(car.needs_service())

    def test_rorschach_engine_should_be_serviced(self):
        """Test rorschach engine should be serviced"""
        last_service_date = date.today()
        current_date = date.today()
        last_service_mileage = 0
        current_mileage = 60001
        car = factory.create_rorschach(
            current_date=current_date,
            last_service_date=last_service_date,
            last_service_mileage=last_service_mileage,
            current_mileage=current_mileage
        )
        self.assertTrue(car.needs_service())

    def test_rorschach_engine_should_not_be_serviced(self):
        """ Rorschach engine should not be serviced"""
        last_service_date = date.today()
        current_date = date.today()
        last_service_mileage = 0
        current_mileage = 60000
        car = factory.create_rorschach(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_thovex_battery_should_be_serviced(self):
        """Test the thovex battery"""
        last_service_date = date.today().replace(year=date.today().year - 4)
        current_date = date.today()
        current_mileage = 0
        last_service_mileage = 0
        car = factory.create_thovex(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_thovex_battery_should_not_be_serviced(self):
        """Test the thovex battery should not be serviced"""
        last_service_date = date.today().replace(year=date.today().year - 1)
        current_date = date.today()
        current_mileage = 0
        last_service_mileage = 0
        car = factory.create_thovex(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_thovex_engine_should_be_serviced(self):
        """Test thovex engine should be serviced"""
        last_service_date = date.today()
        current_date = date.today()
        current_mileage = 30002
        last_service_mileage = 0
        car = factory.create_calliope(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_thovex_engine_should_not_be_serviced(self):
        """ Calliope thovex should not be serviced"""
        last_service_date = date.today()
        current_date = date.today()
        current_mileage = 30000
        last_service_mileage = 0
        car = factory.create_calliope(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())
