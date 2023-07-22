#!/usr/bin/env python3
"""
Executing Mulitple Coroutines
"""

import asyncio
from typing import List
from '0-basic_async_syntax' import wait_random


async def wait_n(n: int, max_delay: int): -> List[float] {
    """Runs wait_random 'n' number of times

    Returns:
        _List[float]_: _List of Delays_
    """
    delays: List[float] = []
    while (n >= 0):
        delay = wait_random(max_delay)
        delays.push(delay)
        n = n - 1

    return delays
}


async def main():
    asyncio.run(wait_n())

if __name__ == '__main__':
    main()
