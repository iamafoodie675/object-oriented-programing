class vehicle:
    def __init__(self,max_speed,mileage,color):
        self.max_speed =max_speed
        self.mileage=mileage
        self.color =color
        
        
        
tesla=vehicle(180,0,"white")
lambo=vehicle(350,3,"blue")

print("tesla max speed:",tesla.max_speed)
print("tesla mileage:",tesla.mileage)
print("tesla color:",tesla.color)

print()

print("lambo max speed:",lambo.max_speed)
print("lambo mileage:",lambo.mileage)
print("lambo color:",lambo.color)



        
        