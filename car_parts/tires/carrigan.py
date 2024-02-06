#!/usr/bin/env python3


"""The carrigan tires
"""

from typing import List
from . import Tires


class Carrigan(Tires):
    """Carrigan tires implementation"""

    def __init__(self, tire_states: List):
        self.tire_states = tire_states

    def needs_service(self) -> bool:
        """Check if carrigan tires needs service
        """

        for state in self.tire_states:
            if state >= 0.9:
                return True

        return False
