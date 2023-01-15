from car import Car

import engine
import battery


class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            engine.CapuletEngine(current_mileage, last_service_mileage),
            battery.SpindlerBattery(last_service_date, current_date)
        )

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            engine.WilloughbyEngine(current_mileage, last_service_mileage),
            battery.SpindlerBattery(last_service_date, current_date)
        )

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            engine.WilloughbyEngine(current_mileage, last_service_mileage),
            battery.NubbinBattery(last_service_date, current_date)
        )

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            engine.CapuletEngine(current_mileage, last_service_mileage),
            battery.NubbinBattery(last_service_date, current_date)
        )

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        return Car(
            engine.SternmanEngine(warning_light_on),
            battery.SpindlerBattery(last_service_date, current_date)
        )
