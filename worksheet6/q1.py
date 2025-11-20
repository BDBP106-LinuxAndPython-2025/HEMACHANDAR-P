#!/usr/bin/python3

class Car:
    def __init__(self, make, model, year, color, started=False, speed=0, max_speed=200):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = started
        self.speed = speed
        self.max_speed = max_speed

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) - {self.color}"

    @staticmethod
    def show_intro_message():
        print("This class represents a car object.")

    showroom = "City Showroom"

    @classmethod
    def change_showroom(cls, new_name):
        cls.showroom = new_name


# (a)
print("question a")
car1 = Car('Hyundai', 'i20', 2023, 'Red')
print(vars(car1))
print()

# (b)
print("question b")
car2 = Car('Suzuki', 'Baleno', 2024, 'Blue')
print(vars(car2))
print()

# (c)
print("question c")
#print(Car.make)  # giving an error
print(car1.make)   # correct way
print()

# (d)
print("question d")
print(car1.model)
print(Car.__dict__)
print()

# (e)
print("question e")
Car.change_showroom("Dream Motors")
print(Car.showroom)
print()

# (f)
print("question f")
print(car1.__dict__)
print()

# (g)
print("question g")
print(car1)
print()

# (h)
print("question h")
Car.show_intro_message()
print()

