#!/usr/bin/env python3
"""function num 1"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """list retrn"""
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = await asyncio.gather(*tasks)

    """ not using sort"""
    for i in range(len(delays)):
        for j in range(0, len(delays) - i - 1):
            if delays[j] > delays[j + 1]:
                delays[j], delays[j + 1] = delays[j + 1], delays[j]

    return delays
