#!/usr/bin/env python3

"""Willoughby Engine module
"""

from . import Engine


class WilloughbyEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int):
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        """Determine if Willoughby Engine needs service
        """
        return self.current_mileage - self.last_service_mileage > 60000
