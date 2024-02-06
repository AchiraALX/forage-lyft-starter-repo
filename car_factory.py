#!/usr/bin/env python3


"""Car factory
"""

from datetime import date
from car import Car
from car_parts.batteries.nubin import NubbinBattery
from car_parts.batteries.spindler import SpindlerBattery
from car_parts.engines.capulet_engine import CapuletEngine
from car_parts.engines.sternman_engine import SternmanEngine
from car_parts.engines.willoughby_engine import WilloughbyEngine


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
        capulet_engine = CapuletEngine(
            last_service_mileage=last_service_mileage,
            current_mileage=current_mileage)
        spindler_battery = SpindlerBattery(
            last_service_date=last_service_date,
            current_date=current_date)
        return Car(capulet_engine, spindler_battery)

    @staticmethod
    def create_glissade(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int
    ) -> Car:
        """Create a glissade car"""
        willoughby_engine = WilloughbyEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        spindler_battery = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date)
        return Car(willoughby_engine, spindler_battery)

    @staticmethod
    def create_palindrome(
            current_date: date,
            last_service_date: date,
            warning_light_on: bool
    ) -> Car:
        """Create a palindrome car"""
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date)
        return Car(sternman_engine, spindler_battery)

    @staticmethod
    def create_rorschach(
            current_date: date,
            last_service_date: date,
            current_mileage: int,
            last_service_mileage: int
    ) -> Car:
        """Create a rorschach car"""
        willoughby_engine = WilloughbyEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        nubbin_battery = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date)
        return Car(willoughby_engine, nubbin_battery)

    @staticmethod
    def create_thovex(
            current_date: date,
            last_service_date: date,
            current_mileage: int,
            last_service_mileage: int
    ) -> Car:
        """Create a thovex car"""
        capulet_engine = CapuletEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        nubbin_battery = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date)
        return Car(capulet_engine, nubbin_battery)
