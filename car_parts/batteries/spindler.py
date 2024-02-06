#!/usr/bin/env python3


"""The spindler battery
"""


from abc import ABC
from datetime import date
from . import Battery


class SpindlerBattery(Battery, ABC):
    """Represent the spindler battery
    """

    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        """Check if the spindler Battery needs service"""
        serviceable = self.current_date - self.last_service_date

        if serviceable.days > 365 * 2:
            return True

        return False
