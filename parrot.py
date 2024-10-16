class parrot:
    species ="bird"
    
    def __init__(self,name,age):
        self.name =name
        self.age =age
        
        
blu =parrot("Blu",10)
woo =parrot("woo",15)


print(f"Blue is a {blu.species}")
print(f"woo is a {woo.species}")

print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")
