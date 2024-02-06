#!/usr/bin/env python3

"""Capulet Engine Module
"""

from . import Engine


class CapuletEngine(Engine):
    """Capulet engine"""
    def __init__(self, current_mileage: int, last_service_mileage: int):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        """Check if Capulet Engine needs to be serviceable
        """
        return int(self.current_mileage - self.last_service_mileage) > 30000
