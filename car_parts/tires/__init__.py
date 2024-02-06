#!/usr/bin/env python3


"""The tire module
"""

from interface import Serviceable


class Tires(Serviceable):
    """Implements tires"""

    def needs_service(self) -> bool:
        """Check if tires needs service"""