#!/usr/bin/env python3
"""Module with an async generator that yields random numbers."""

import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """Loop 10 times, wait 1 second, then yield a random number."""

    for i in range(10):
        await asyncio.sleep(1)
        n = random.uniform(0, 10)
        yield n
