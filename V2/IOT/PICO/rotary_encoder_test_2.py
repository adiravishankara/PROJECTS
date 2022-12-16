# Write your code here :-)
from board import *
import _asyncio as asyncio
import rotaryio as rio
import countio as cio


class encoder:
    def __init__(self, pinA, pinB, name):
        self.name = name
        self.enc = rio.IncrementalEncoder(pinA, pinB)
        self.last_position = None

    async def rotary_interrupt(self):
        while True:
            self.position = self.enc.position
            if self.last_position == None or self.position != self.last_position:
                print("{} encoder at {}".format(self.name, self.position))
            self.last_position = self.position
            await asyncio.sleep(0)


class multi_input_handler:
    def __init__(self):
        left_encoder = encoder('GP18', 'GP19', "left")
        right_encoder = encoder('GP12', 'GP13', "right")
        asyncio.run(self.run_async())

    def run_async(self):
        self.interrupt_task_left = asyncio.create_task(left_encoder.rotary_interrupt())
        self.interrupt_task_right = asyncio.create_task(right_encoder.rotary_interrupt())
        await asyncio.gather(self.interrupt_task_left, self.interrupt_task_right)

if __name__ == "__main__":
    multi_input_handler()






