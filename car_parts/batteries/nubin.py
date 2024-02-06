#!/usr/bin/env python3


"""The nubbin battery
"""


from datetime import date
from . import Battery


class NubbinBattery(Battery):
    """The Nubbin Battery
    """

    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        """Check if Nubbin battery needs a service"""
        serviceable = self.current_date - self.last_service_date

        if serviceable.days > 365 * 4:
            return True
        return False
