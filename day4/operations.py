def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
        
    except ZeroDivisionError:
    
        print("Can`t devide by 0")
        return "Can`t devide by 0"