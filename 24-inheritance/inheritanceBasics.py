class SmartDevice:
    def __init__(self, name: str):
        self.name = name

class SmartLight(SmartDevice):
    def turn_on(self) -> None:
        print(f"{self.name} is turned on")

    def turn_off(self) -> None:
        print(f"{self.name} is turned off")



device = SmartLight("Smart Light")
device.turn_on()
device.turn_off()