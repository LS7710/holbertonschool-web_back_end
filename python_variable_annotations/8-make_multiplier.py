#!/usr/bin/env python3
"""i hate commenting"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """comment comment comment"""
    def multiplier_function(x: float) -> float:
        """return"""
        return x * multiplier
    return multiplier_function
