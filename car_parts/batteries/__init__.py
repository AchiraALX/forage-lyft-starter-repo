#!/usr/bin/env python3


"""Car batteries
"""

from interface import Serviceable


class Battery(Serviceable):
    """Represent the battery
    """

    def needs_service(self) -> bool:
        """If battery needs a service"""
