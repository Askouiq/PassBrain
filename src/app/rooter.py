#

class Rit:
    def __init__(self, name):
        self.name = name
        self.battery_level = 100

    def perform_task(self, task):
        if self.battery_level > 0:
            print(f"{self.name} is performing task: {task}")
            self.battery_level -= 10
        else:
            print(f"{self.name} is out of battery. Recharge needed.")

class Generator(Robot):
    def __init__(self, name, location):
        super().__init__(name)
        self.location = location

    def display_info(self):
        print(f"{self.name} is currently at {self.location}.")

class CookingRobot(Robot):
    def __init__(self, name, cuisine_preference):
        super().__init__(name)
        self.cuisine_preference = cuisine_preference

    def cook(self, dish):
        print(f"{self.name} is cooking {dish} with {self.cuisine_preference} flavor.")

# Example usage
