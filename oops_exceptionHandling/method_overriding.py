#method overriding

class bird:
    def intro(self):
        print("There many types of birds")
        self.bird()
    def flight(self):
        print("some birds may fly and some may not")
        self.bird()
        
class sparrow(bird):
    def flight(self):
        print("all birds can fly")
        self.sparrow()


class Ostrich(bird):
    def flight(self):
        print("they cannot fly")
        self.ostrich()

obj=sparrow()

sparrow.flight()
    
