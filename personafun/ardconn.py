import time
import random

class ArdSimulator:
    def __init__(self, sampletime):
        self._sampletime = sampletime

    def get_data(self):
        temp_rand = random.randint(22,23) + round(random.random(),3)
        data_rand = [self._sampletime, temp_rand]
        time.sleep(self._sampletime/1000)
        return data_rand