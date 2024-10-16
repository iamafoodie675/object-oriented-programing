class Dog:
    species = "Animal" 

    def __init__(self, breed, name, age, color, weight):
        self.breed = breed          
        self.name = name            
        self.age = age       
        self.color = color       
        self.weight = weight     

    def display_details(self):
        print(f"Breed: {self.breed}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years")
        print(f"Color: {self.color}")
        print(f"Weight: {self.weight} kg")
        print(f"Species: {self.species}\n")


tommy = Dog("Labrador", "tommy", 3, "Yellow", 30)
max = Dog("German Shepherd", "Max", 5, "Black and Tan", 40)
charlie = Dog("Beagle", "Charlie", 2, "Tri-color", 10)


tommy.display_details()
max.display_details()
charlie.display_details()