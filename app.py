from cal_fun import do_addition,do_subtraction

def main():
    print("welcome to the calculator App")
    print('''\n select the function from the following opition:
          1. Add
          2. Subtract''')
    user_input=input('select the function :')
    x=int(input('value of x :'))
    y=int(input('value of y :'))
    if user_input == '1':
        result=do_addition(x,y)
    elif user_input == '2':
        result=do_subtraction(x,y)
    print(result)


if __name__ == "__main__":
    main()
