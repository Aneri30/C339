# Decorator

# i am passing a parameter which can be a variable or function but these time its a function
# what is the use :- 
# deposit money or withdraw money you can have a function call audit

import datetime
def my_decorator(my_function):
    def inner_decorator():
        print("this happend before",datetime.datetime.utcnow())     # you add the balance
        my_function()    # when you call my function the my_decorated function get executed   # here you do the audit function call
        print("this happened after",datetime.datetime.utcnow())   # ensure database is updated
        print("This happend at end!!!!",datetime.datetime.utcnow())  # drop a message on console
    return inner_decorator

@my_decorator
def my_decorated():
    print("welcome to first lecture of class",datetime.datetime.utcnow())

# whenever you write a python file first function which get invoked is main function
if __name__ == "__main__":    # these code check name of the function is it main
    print("first line of main",datetime.datetime.utcnow())
    my_decorated()
    print("after decorator",datetime.datetime.utcnow())