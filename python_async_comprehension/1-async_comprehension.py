#!/usr/bin/env python3
"""Task 1"""
from typing import List
import asyncio
task0 = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Func 1
    """
    return [i async for i in task0()]
