class Car:
    current_car = 1

    def __init__(self, make, model, color, year, miles, price):
        self.num = Car.current_car
        Car.current_car += 1
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.miles = miles
        self.price = price
    
    def printinfo(self):
        print(f"Car {self.num}: ")
        print(self.color, self.year, self.make, self.model)
        print(f"{self.miles} miles, ${self.price}")