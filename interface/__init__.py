#!/usr/bin/env python3


"""Serviceable interface"""

from abc import ABC, abstractmethod


class Serviceable(ABC):
    """Service Interface
    """

    @abstractmethod
    def needs_service(self) -> bool:
        """Check if car needs service
        """
