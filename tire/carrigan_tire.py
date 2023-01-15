from tire import Tire


class CarriganTire(Tire):
    def __init__(self, tires_damage: list):
        self.tires_damage = tires_damage

    def needs_service(self):
        return any(damage >= 0.9 for damage in self.tires_damage)
