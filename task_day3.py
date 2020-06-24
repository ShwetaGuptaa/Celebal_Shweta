## Exception Handling
def exception_example_1():
    var=3
    try:
        ans=var/(var-var)
        print(var)
    except ZeroDivisionError:
        print("We can not divide a number by zero")
exception_example_1()       

## handling multiple exception
def exception_example_3():
    try :  
        var = 3
        if var < 4 : 
            ans = var/(var-3)  
    # throws NameError if var >= 4 
        print("Value of ans = ", ans)
    except(ZeroDivisionError, NameError): 
        print("\nError Occurred")
exception_example_3()


##  passing argument to an Exception
def exception_example_2():
    array=[3,2,3,6]
    try:
        print(array[6])
    except Exception as e:
        print("Error occured : ",e)
        
exception_example_2()        

## user defined exceptions
class MyError(Exception):  
     
    def __init__(self, value):  
        self.value = value   
    
try:
    var=3
    if var!=1:
        raise(MyError("Some Error has occured"))
    else:
        print(var)
    
# Value of Exception is stored in error  
except MyError as e:  
    print( e)