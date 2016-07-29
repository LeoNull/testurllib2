# coding:utf-8


def dec(func):
    def in_dec(*arg):
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)
    return in_dec

def my_sum(*arg):
    return sum(arg)

def my_average(*arg):
    return sum / len(arg)
 
my_sum = dec(my_sum)

print (my_sum(1, 2, 3, 4, 5))
