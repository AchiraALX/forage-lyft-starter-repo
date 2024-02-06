#!/usr/bin/env python3


"""The engine
"""


from interface import Serviceable


class Engine(Serviceable):
    """Engine Base
    """

    def needs_service(self) -> bool:
        """Check if engine needs service"""
