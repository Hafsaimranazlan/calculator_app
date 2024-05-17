from cal_fun import do_addition,do_subtraction,do_division
from multiply import do_multiply 
def main():
    print("welcome to the calculator App")
    print('''\n select the function from the following opition:
          1. Add
          2. Subtract
          3. multiply ''')
    user_input=input('select the function :')
    x=int(input('value of x :'))
    y=int(input('value of y :'))
    if user_input == '1':
        result=do_addition(x,y)
    elif user_input == '2':
        result=do_subtraction(x,y)
    elif user_input == '3':
        result=do_multiply(x,y)
    elif user_input == '4':
        result=do_division(x,y)


if __name__ == "__main__":
    main()
