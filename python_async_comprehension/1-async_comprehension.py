#!/usr/bin/env python3
"""Task 1"""
from typing import List
import asyncio
task0 = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using async comprehension.

    Returns:
        A list of 10 random float numbers between 0 and 10.
    """
    return [i async for i in async_generator()]
