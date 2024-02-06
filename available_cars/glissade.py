#!/usr/bin/env python3

"""Glissade car
"""

from datetime import datetime

from car_parts.engines.willoughby_engine import WilloughbyEngine
from car_parts.batteries.spindler import SpindlerBattery


class Glissade(WilloughbyEngine, SpindlerBattery):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
