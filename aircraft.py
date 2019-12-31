class AircraftHandler:
    def __init__(self, displayHandler):
        self.g13 = displayHandler

    def buttonHandleSpecificAC(self, buttonPressed):
        print(f'{self.__class__.__name__} Button: {buttonPressed}')
        return '\n'

    def updateDisplay(self):
        # clear bitmap
        self.g13.draw.rectangle((0, 0, self.g13.width, self.g13.height), 0, 0)

    def setData(self, selector, value, update=True):
        setattr(self, selector, value)
        if update:
            self.updateDisplay()
