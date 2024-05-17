def do_addition(x:int,y:int):
    return x+y

def do_subtraction(x:int,y:int):
    return x-y


def do_division(x:int,y:int):
    try:
        return x/y
    except ZeroDivisionError as e:
        return "cannot divide by zero"