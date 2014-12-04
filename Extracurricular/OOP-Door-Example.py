"""     OOP example using doors
"""
class Door:
    color = 'brown'

    def __init__(self, number, status):
        self.number = number
        self.status = status
        
    @classmethod
    def knock(cls):
        print("Knock!")
        
    @classmethod
    def paint(cls, color):
        cls.color = color
    
    def open(self):
        self.status = 'open'
        
    def close(self):
        self.status = 'closed'

class SecurityDoor(Door):
    locked = True
    
    def __init__(self, number, status):
        self.door = Door(number, status)
    
    def open(self):
        if self.locked:
            return
        self.door.open()
    
    def __getattr__(self, attr):
        return getattr(self.door, attr)

class ComposedDoor:
    def __init__(self, number, status):
        self.door = Door(number, status)
        
    def __getattr__(self, attr):
        return getattr(self.door, attr)

class Room:
    def __init__(self, door):
        self.door = door
    
    def open(self):
        self.door.open()
    
    