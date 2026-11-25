class Personagem:
    #constrututor
    def __init__( self, name, mass, height, gender, eye_color, homeworld ):
        self.name = name
        self.height = height
        self.mass = mass
        self.eye_color = eye_color
        self.gender = gender
        self.homeworld = homeworld

    def __str__( self ):
        return (
            f"\nName: { self.name }\n" 
            f"Mass: { self.mass }\n" 
            f"Height: { self.height }\n" 
            f"Gender: { self.gender }\n"
            f"Eye color: { self.eye_color }\n"
            f"Home world: { self.homeworld }"
        )