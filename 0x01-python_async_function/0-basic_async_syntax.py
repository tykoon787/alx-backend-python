#!/usr/bin/env python3
""""
The basics of async
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This function just takes in a max delay and waits for 'delay'
    seconds before returning the delay time

    Args:
        max_delay (int, optional): _Delay from '0' seconds to max-delay
        seconds. Defaults to 10.

    Returns:
        float: delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main():
    """
    Main Function
    """
    asyncio.run(wait_random())

if __name__ == '__main__':
    main()
