# %%
try :
    print(1/0)

except:
    print("Error occured because you cannot divide a value by zero")

finally:
    print("abcdefghijklmnop")
    print("Hi")

# %%
try :  
    print(1/0)   # failuere codnition code can be written here
    
except Exception as ex:   # only when you get an error
    print("an error occured",ex)
finally:  # these is always getting executed
    print("hi how are ayoposadjklasndksanknd")
    print("I am god")

# %%
def handle_exception(func_name):
    def inner(a,b):
        try:
            return func_name(a,b)
        except Exception as ex:
            print('We have following exception', ex)
    return inner

@handle_exception
def divide(x,y):
    return x/y

divide(8,0)
# %%
try :  
    #print(1/0)   # failuere codnition code can be written here
    raise RuntimeError("you are wrong")
except ZeroDivisionError as error:   # only when you get an error
    print("an error occured",error)
except Exception as ex:   # only when you get an error
    print("from exception",ex)
finally:  # these is always getting executed
    print("hi how are ayoposadjklasndksanknd")
    print("I am god")

# %%
#Error can be anything insufficentfunderror or incorrectageerror
class Customerror(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self) -> str:
        return f"{type(self).__name__}: {self.message} written by Aneri"
    
print("Welcome to program")
raise Customerror("Welcome to the first python customerror")

# %%
# Error with pass
class Customerror(Exception):
    pass
    
print("Welcome to program")
raise Customerror("Welcome to your first python customerror")
# %%
