import unittest

from tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def tires_need_service_true(self):
        tires_damage = [0, 1, 1, 1]
        tire = OctoprimeTire(tires_damage)

        self.assertTrue(tire.needs_service())

    def tires_need_service_false(self):
        tires_damage = [0, 0, 1, 1]
        tire = OctoprimeTire(tires_damage)

        self.assertFalse(tire.needs_service())
