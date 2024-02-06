#!/usr/bin/env python3

"""Sternman engine module
"""

from . import Engine


class SternmanEngine(Engine):
    """Sternman Engine"""
    def __init__(self, warning_light_is_on: bool):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        """Determine if sternman engine needs service
        """
        return self.warning_light_is_on
