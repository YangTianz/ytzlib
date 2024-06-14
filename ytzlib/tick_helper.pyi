from typing import Callable

class TickHelper:
    def __init__(self) -> None: ...
    async def start(self) -> None: ...
    def delay_call(self, callback: Callable[..., None], delay: float) -> None: ...
    def repeat_call(self, callback: Callable[..., None], interval: float) -> int: ...
    def cancel_call(self, timer_id: int) -> None: ...
    def destroy(self) -> None: ...

ticker: TickHelper

async def main(): ...
