class SpaceShip():
    """Describing starship"""

    def __init__(self, max_speed, consumption, max_fuel):
        """Starship valuables"""
        self.max_speed = max_speed
        self.consumption = consumption
        self.max_fuel = max_fuel
        self.speed = 0
        self.fuel = 0

    def accelerate(self):
        """Accelerate our starship"""
        if self.fuel >= self.consumption:
            self.speed += 10
            self.fuel -= self.consumption
            if self.speed > self.max_speed:
                self.speed = self.max_speed
        else:
            print("Not enough fuel!")
            return
        if self.fuel > 0:
            print("Fuel:", self.fuel, "from", self.max_fuel, "Speed:", self.speed, "from", self.max_speed)

    def fuelUp(self):
        """Fuel our spaceship"""
        self.fuel = self.max_fuel
        print("Fuel:", self.fuel, "from", self.max_fuel, "Speed:", self.speed, "from", self.max_speed)

    def print_state(self):
        print("Your space ship fuel:", self.fuel, "from", self.max_fuel, "and", "Speed:", self.speed, "from",
              self.max_speed)


"""Max speed, consumption and max fuel of spaceship"""
space_ship1 = SpaceShip(20, 3, 9)

space_ship2 = SpaceShip(500, 1, 2)

space_ship3 = SpaceShip(42, 1, 20)

space_ship4 = SpaceShip(99, 2, 11)

print("\nCondition of your Spaceship:\n")
space_ship1.print_state()
space_ship2.print_state()
space_ship3.print_state()
space_ship4.print_state()

print("\naccelerating of your spacecraft No:1\n")
space_ship1.fuelUp()
space_ship1.accelerate()
space_ship1.accelerate()
space_ship1.accelerate()
space_ship1.fuelUp()
space_ship1.accelerate()
space_ship1.accelerate()
space_ship1.accelerate()
print("\naccelerating of your spacecraft No:2\n")
space_ship2.fuelUp()
space_ship2.accelerate()
space_ship2.accelerate()
space_ship2.accelerate()
space_ship2.fuelUp()
space_ship2.accelerate()
space_ship2.accelerate()
space_ship2.accelerate()
print("\naccelerating of your spacecraft No:3\n")
space_ship3.fuelUp()
space_ship3.accelerate()
space_ship3.accelerate()
space_ship3.accelerate()
space_ship3.fuelUp()
space_ship3.accelerate()
space_ship3.accelerate()
space_ship3.accelerate()
print("\naccelerating of your spacecraft No:4\n")
space_ship4.fuelUp()
space_ship4.accelerate()
space_ship4.accelerate()
space_ship4.accelerate()
space_ship4.fuelUp()
space_ship4.accelerate()
space_ship4.accelerate()
space_ship4.accelerate()
