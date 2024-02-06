#!/usr/bin/env python3

"""The car module
"""
from datetime import date

from car_parts.batteries.nubin import NubbinBattery
from car_parts.batteries.spindler import SpindlerBattery
from car_parts.engines import Engine
from car_parts.batteries import Battery
from car_parts.engines.capulet_engine import CapuletEngine
from car_parts.engines.sternman_engine import SternmanEngine
from car_parts.engines.willoughby_engine import WilloughbyEngine


class Car:
    """Make car
    """

    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        """Check if car needs service
        """
        return self.engine.needs_service() or self.battery.needs_service()


class CarFactory:
    """Be the engineer for the cars. Create cars"""
    @staticmethod
    def create_calliope(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int
    ) -> Car:
        """Create the calliope car"""
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(capulet_engine, spindler_battery)

    @staticmethod
    def create_glissade(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int
    ) -> Car:
        """Create a glissade car"""
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(willoughby_engine, spindler_battery)

    @staticmethod
    def create_palindrome(
            current_date: date,
            last_service_date: date,
            warning_light_on: bool
    ) -> Car:
        """Create a palindrome car"""
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(sternman_engine, spindler_battery)

    @staticmethod
    def create_rorschach(
            current_date: date,
            last_service_date: date,
            current_mileage: int,
            last_service_mileage: int
    ) -> Car:
        """Create a rorschach car"""
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        return Car(willoughby_engine, nubbin_battery)

    @staticmethod
    def create_thovex(
            current_date: date,
            last_service_date: date,
            current_mileage: int,
            last_service_mileage: int
    ) -> Car:
        """Create a thovex car"""
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        return Car(capulet_engine, nubbin_battery)
