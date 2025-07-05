#def greet():
#    return "welcome!"
def upperCase(func):
    def wrapper():
        orgin_message = func()

        mod_message = orgin_message.upper()
        return mod_message
    return wrapper

#greet_upper = upperCase(greet)
#print(greet_upper())




@upperCase
def greet():
    return "Welcome!" 
print(greet())

