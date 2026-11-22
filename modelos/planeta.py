class Planeta:
    #constrututor
    def __init__(self, name, climate, diameter, gravity, population):
        self.name = name
        self.climate = climate
        self.diameter = diameter
        self.gravity = gravity
        self.population = population

    def __str__(self):
        return (
            f"Name: {self.name}\n" 
            f"Climate: {self.climate}\n" 
            f"Diameter: {self.diameter}\n" 
            f"Gravity: {self.gravity}\n" 
            f"Population: {self.population}"
        )