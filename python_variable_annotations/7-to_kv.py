#!/usr/bin/env python3
"""Kendrick > Drake"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return"""
    return (k, float(v ** 2))
