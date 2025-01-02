from  Car import *

if __name__ == "__main__":

    car =  Car("BMW", "2024")
    car.description()

    electric_car = ElectricCar("Tesla", "Model S", 50) 
    electric_car.description()
    electric_car.display_battery()
