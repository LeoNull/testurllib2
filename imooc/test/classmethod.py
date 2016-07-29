class Person(object):
    __count = 0
    @classmethod
    def how_count(cls):
        return cls.__count
    
    
    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1

print Person.how_count()

p1 = Person("Bob")

print Person.how_count()


