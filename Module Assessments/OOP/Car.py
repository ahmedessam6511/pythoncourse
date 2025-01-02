class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def description(self):
        print(f"This is a {self.make} {self.model}.")

    def __del__(self): 
            print(f"{self.make} {self.model} 'Car' object has been deleted.") 


class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)

        self.battery_capacity = battery_capacity

    def display_battery(self):
        print(f"This electric car has a {self.battery_capacity} kWh battery.") 
         


