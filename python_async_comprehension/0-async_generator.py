#!/usr/bin/env python3
"""
Task 0
"""
import asyncio
import random
from typing import AsyncGenerator

"""
Func 0
"""
async def async_generator() -> AsyncGenerator[float, None, None]:
    yield random.uniform(0, 10)
