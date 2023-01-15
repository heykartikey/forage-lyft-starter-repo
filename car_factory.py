from car import Car

import engine
import battery


class CarFactory:
    
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            engine.CapuletEngine(current_mileage, last_service_mileage),
            battery.SpindlerBattery(last_service_date, current_date)
        )

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            engine.WilloughbyEngine(current_mileage, last_service_mileage),
            battery.SpindlerBattery(last_service_date, current_date)
        )

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            engine.WilloughbyEngine(current_mileage, last_service_mileage),
            battery.NubbinBattery(last_service_date, current_date)
        )

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            engine.CapuletEngine(current_mileage, last_service_mileage),
            battery.NubbinBattery(last_service_date, current_date)
        )

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(
            engine.SternmanEngine(warning_light_on),
            battery.SpindlerBattery(last_service_date, current_date)
        )
