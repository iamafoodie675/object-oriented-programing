class Student:
    grade = 7 
    print(f"i am a student of grade{grade}")
    
    def __init__(self,name,age,height):
        self.name =name
        self.age =age
        self.height =height
        
rose = Student("rose",14,5.3)
nabila = Student("nabila",13,5.5)
nusaiba = Student("nusaiba",14,5.0)

print(f"name:{rose.name}\nage:{rose.age}\nheight:{rose.height}\n\n")
print(f"name:{nabila.name}\nage:{nabila.age}\nheight:{nabila.height}\n\n")
print(f"name:{nusaiba.name}\nage:{nusaiba.age}\nheight:{nusaiba.height}\n\n")

print(f"rose grade:{rose.grade}")
print(f"nabila grade:{nabila.grade}")
print(f"nusaiba grade:{nusaiba.grade}")


        