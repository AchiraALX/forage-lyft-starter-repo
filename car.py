#!/usr/bin/env python3

"""The car module
"""

from car_parts.engines import Engine
from car_parts.batteries import Battery


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
