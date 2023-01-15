from car import Car

import engine
import battery
import tire


class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires_damage):
        return Car(
            engine.CapuletEngine(current_mileage, last_service_mileage),
            battery.SpindlerBattery(last_service_date, current_date),
            tire.CarriganTire(tires_damage)
        )

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires_damage):
        return Car(
            engine.WilloughbyEngine(current_mileage, last_service_mileage),
            battery.SpindlerBattery(last_service_date, current_date),
            tire.CarriganTire(tires_damage)
        )

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires_damage):
        return Car(
            engine.WilloughbyEngine(current_mileage, last_service_mileage),
            battery.NubbinBattery(last_service_date, current_date),
            tire.OctoprimeTire(tires_damage)
        )

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires_damage):
        return Car(
            engine.CapuletEngine(current_mileage, last_service_mileage),
            battery.NubbinBattery(last_service_date, current_date),
            tire.OctoprimeTire(tires_damage)
        )

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tires_damage):
        return Car(
            engine.SternmanEngine(warning_light_on),
            battery.SpindlerBattery(last_service_date, current_date),
            tire.CarriganTire(tires_damage)
        )
