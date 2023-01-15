import unittest

from tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def tires_need_service_true(self):
        tires_damage = [0, 0.9, 0.7, 0.44]
        tire = CarriganTire(tires_damage)

        self.assertTrue(tire.needs_service())

    def tires_need_service_false(self):
        tires_damage = [0, 0.89, 0.7, 0.44]
        tire = CarriganTire(tires_damage)

        self.assertFalse(tire.needs_service())
