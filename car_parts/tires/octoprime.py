#!/usr/bin/env python3


"""The octoprime tires
"""

from typing import List
from . import Tires


class Octoprime(Tires):
    """Carrigan tires implementation"""

    def __init__(self, tire_states: List):
        self.tire_states = tire_states

    def needs_service(self) -> bool:
        """Check if carrigan tires needs service
        """

        return sum(self.tire_states) > 3
