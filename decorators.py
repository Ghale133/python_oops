class Room:
    area = 50

    def __init__(self, a = 5):
        self.length = a
        self.area = 10

    def area_instance(self):
        return self.length ** 2
    
    @classmethod
    def area_class(cls):
        return cls.area
    
    @staticmethod
    def area_static(length, breadth):
        return length * breadth

room = Room(10)

# Room.area_static = staticmethod(Room.area_static)


# default arguments 
# class variables
# instance variables


create a class Burger
instance > create Burger
return Burger
