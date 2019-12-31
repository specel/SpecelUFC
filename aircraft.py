from abc import abstractmethod


class AircraftHandler:
    def __init__(self, displayHandler):
        self.g13 = displayHandler

    @abstractmethod
    def buttonHandleSpecificAC(self, buttonPressed):
        pass

    def updateDisplay(self):
        # clear bitmap
        self.g13.draw.rectangle((0, 0, self.g13.width, self.g13.height), 0, 0)

    def setData(self, selector, value, update=True):
        setattr(self, selector, value)
        if update:
            self.updateDisplay()
