class Person(object):
    def __init__(self, name, sex, birth, job):
        self.name = name
        self.sex = sex
        self.birth = birth
        self.job = job

xiaoming = Person('xiaoming', 'Male', '1990-1-1', job="Student")

print xiaoming.name
print xiaoming.job
