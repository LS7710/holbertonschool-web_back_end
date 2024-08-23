#!/usr/bin/env python3
"""Task 2"""
import asyncio
import time
from typing import List
t1 = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times.

    Returns:
        The total runtime in seconds.
    """
    start_time = time.perf_counter()

    await asyncio.gather(*(t1() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
