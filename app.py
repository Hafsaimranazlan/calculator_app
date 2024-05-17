from cal_fun import do_addition,do_subtraction
from multiply import do_multiply
from area import cal_area_rectangle 
def main():
    print("welcome to the calculator App")
    print('''\n select the function from the following opition:
          1. Add
          2. Subtract
          3. multiply
          4. area  ''')
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
        result=cal_area_rectangle(x,y)


if __name__ == "__main__":
    main()
