class Car:
    def __init__(self, name, number):
        self.name = name
        self.number = number


def groupCarName(carArray):
    c = {}
    for car in carArray:
        if car.name in c.keys():
            c[car.name].append(car.number)
        else:
            c[car.name] = [car.number]
    return c

        
    
        
        
c1 = Car("tata", "1")
c2 = Car("mahindra", "2")
c3 = Car("tata", "3")
c4 = Car("tata", "4")
c5 = Car("toyota", "6")
c6 = Car("toyota", "7")
c7 = Car("toyota", "8")
c7 = Car("mahindra", "9")
c8 = Car("tata", "10")
print(c1.name)
carArray = [c1,c2,c3,c4,c5,c6,c7,c8]

print(groupCarName(carArray))

