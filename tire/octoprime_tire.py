from tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tires_damage: list):
        self.tires_damage = tires_damage

    def needs_service(self):
        return sum(self.tires_damage) >= 3
