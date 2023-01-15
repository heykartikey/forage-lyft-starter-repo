import unittest
import datetime

from battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def battery_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)
        last_service_date = last_service_date.replace(
            day=last_service_date.day - 1)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def battery_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
