class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.system = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.system[carType] < 1:
            return False
        self.system[carType] -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
if __name__ == "__main__":
    parking = ParkingSystem(1, 1, 0)
    print(
        [
            parking.addCar(1),
            parking.addCar(2),
            parking.addCar(3),
            parking.addCar(1),
        ]
    )
