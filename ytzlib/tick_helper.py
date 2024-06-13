import asyncio
import time
from typing import Callable


class TickHelper:
    def __init__(self) -> None:
        self._id = 0
        self._time = time.time()

        self._callbacks: dict[int, Callable[..., None]] = {}
        self._intervals: dict[int, float] = {}

        self._is_running = True

    async def start(self) -> None:
        self._is_running = True
        while self._is_running:
            await asyncio.sleep(1)

    def _gen_id(self) -> int:
        self._id += 1
        return self._id

    def delay_call(self, callback: Callable[..., None], delay: float) -> None:
        async def call_later():
            await asyncio.sleep(delay)
            callback()

        asyncio.create_task(call_later())

    def repeat_call(
        self, callback: Callable[..., None], interval: float
    ) -> int:
        timer_id = self._gen_id()
        self._callbacks[timer_id] = callback
        self._intervals[timer_id] = interval

        async def handle():
            if timer_id in self._callbacks:
                self._callbacks[timer_id]()
                await asyncio.sleep(self._intervals[timer_id])
                asyncio.create_task(handle())

        asyncio.create_task(handle())
        return timer_id

    def cancel_call(self, timer_id: int) -> None:
        if timer_id in self._callbacks:
            del self._callbacks[timer_id]
            del self._intervals[timer_id]

    def destroy(self):
        self._is_running = False


ticker = TickHelper()


async def main():
    start = time.time()

    def _get_time():
        return int(round(time.time() - start))

    def hello1():
        print("hello1", _get_time())

    def hello2():
        print("hello2", _get_time())

    def hello5():
        print("hello5", _get_time())

    _ = ticker.repeat_call(hello1, 1)
    i2 = ticker.repeat_call(hello2, 2)
    _ = ticker.repeat_call(hello5, 5)
    ticker.delay_call(lambda: ticker.cancel_call(i2), 10)
    await asyncio.gather(ticker.start())


if __name__ == "__main__":
    asyncio.run(main())
