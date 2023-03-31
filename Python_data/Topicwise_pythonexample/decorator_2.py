def deco(func):
    def inner(*args, **kwargs):
        print("Doing", func.__name__)
        result = func(*args, **kwargs)
        print("Doing executed")
        return result
    return inner

@deco
def addition(a,b):
    print(a+b)

@deco
def subtraction(a,b):
    print(b-a)

if __name__ == "__main__":
    addition(2,4)
    subtraction(2,4)        


"""
def handle_addsub_exception(func):
    def inner(*args, **kwargs):
        print(f'Passing {len(args)} numbers')
        try:
            return f'\tResult is {func(*args, **kwargs)}'
        except Exception as ex:
            print('\tWe got the following exception:', ex )
        finally:
            print('\tOperation success!')
    return inner

@handle_addsub_exception
def addition(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

@handle_addsub_exception
def substraction(*args):
    sub = 0
    for num in args:
        sub -= num
    return sub

def mydec(func):
    def warrper(*args,**kwargs):
        if 'my_param' in kwargs:
            my_param =kwargs['my_param']
            print(f"my_param value is {my_param}")
        else:
            print("my_param is not found in kwargs")
    return warrper
@mydec
def my_function(*args,**kwargs):
    pass
print(addition(8, 0, 1, 2, 3, 5))
print(substraction(8, 0, 1, 2, 3, 5))

print(my_function(my_param="hello"))

"""
"""
import datetime

def my_decorator(inner):
    def inner_decorator(num_copy):
        print("this happend before",datetime.datetime.utcnow())     
        inner(int(num_copy) +1)    # when you call my function the my_decorated function get executed   # here you do the audit function call
        print("this happened after",datetime.datetime.utcnow())   # ensure database is updated
        print("This happend at end!!!!")  # drop a message on console
    return inner_decorator

@my_decorator
def decorated(number):
    print("This happened :"+str(number))   # if you dont specify str print would not work as it would say int and string cannot be combined


if __name__ == "__main__":
    decorated(9)
"""

