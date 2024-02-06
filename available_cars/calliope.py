from datetime import datetime

from car_parts.engines.capulet_engine import CapuletEngine
from car_parts.batteries.spindler import SpindlerBattery


class Calliope(CapuletEngine, SpindlerBattery):
    def needs_service(self):
        """Check if car needs service
        """
