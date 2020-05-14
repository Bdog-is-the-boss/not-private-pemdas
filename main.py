num = input("enter how many numbers/operaters you want in the equation  ***NOTE*** up to 7 numbers/operaters 3,5,7 are all the numbers/opertater sets ")
if num == '3':
    num1 = int(input("first number "))
    oper = input("operator ")
    num2 = int(input("next number "))
    if oper == '*':
        print(num1 * num2)
    elif oper == '/':
        print(num1 / num2)
    elif oper == '+':
        print(num1 + num2)
    elif oper == '-':
        print(num1 - num2)

if num == '5':
    num1 = int(input("first number "))
    oper = input("operator ")
    num2 = int(input("next number "))
    oper2 = input("next number ")
    num3 = int(input("next number "))
    if oper == '*' and oper2 == '-':
        print(num1 * num2 - num3)
    elif oper == '/' and oper2 == '-':
        print(num1 / num2 - num3)
    elif oper == '+' and oper2 == '-':
        print(num1 + num2 - num3)
    elif oper == '-' and oper2 == '-':
        print(num1 - num2 - num3)
    elif oper == '*' and oper2 == '/':
        print(num1 * num2 / num3)
    elif oper == '/' and oper2 == '/':
        print(num1 / num2 / num3)
    elif oper == '+' and oper2 == '/':
        print(num1 / num2 + num3)
    elif oper == '-' and oper2 == '/':
        print(num1 - num2 / num3)
    elif oper == '*' and oper2 == '+':
        print(num1 * num2 + num3)
    elif oper == '/' and oper2 == '+':
        print(num1 / num2 + num3)
    elif oper == '+' and oper2 == '+':
        print(num1 + num2 + num3)
    elif oper == '-' and oper2 == '+':
        print(num1 - num2 + num3)
    elif oper == '*' and oper2 == '*':
        print(num1 * num2 * num3)
    elif oper == '/' and oper2 == '*':
        print(num1 / num2 * num3)
    elif oper == '+' and oper2 == '*':
        print(num1 * num2 + num3)
    elif oper == '-' and oper2 == '*':
        print(num1 * num2 - num3) 

if num == '7':
    num1 = int(input("first number "))
    oper = input("operator ")
    num2 = int(input("next number "))
    oper2 = input("next operater ")
    num3 = int(input("next number ")) 
    oper3 = input("next operater ")
    num4 = int(input("next number "))
    if oper == '+' and oper2 == '+' and oper3 == '+':
        print(num1 + num2 + num3 + num4)
    
    elif oper == '+' and oper2 == '+' and oper3 == '-':
        print(num1 + num2 + num3 - num4)
    
    elif oper == '+' and oper2 == '+' and oper3 == '*':
        print(num1 * num2 + num3 + num4)

    elif oper == '+' and oper2 == '+' and oper3 == '/':
        print(num1 / num2 + num3 + num4)
#2222222222222222222222222222222222222222222222
    elif oper == '+' and oper2 == '-' and oper3 == '+':
        print(num1 + num2 - num3 + num4)

    elif oper == '+' and oper2 == '*' and oper3 == '+':
        print(num1 * num2 + num3 + num4)

    elif oper == '+' and oper2 == '/' and oper3 == '+':
        print(num1 / num2 + num3 + num4)
#3333333333333333333333333333333333333333333333
    elif oper == '-' and oper2 == '+' and oper3 == '+':
        print(num1 - num2 + num3 + num4)

    elif oper == '*' and oper2 == '+' and oper3 == '+':
        print(num1 * num2 + num3 + num4)

    elif oper == '/' and oper2 == '+' and oper3 == '+':
        print(num1 / num2 + num3 + num4)
#32323232323232323232323233232332323322323232322323
    elif oper == '-' and oper2 == '-' and oper3 == '+':
        print(num1 - num2 - num3 + num4)

    elif oper == '*' and oper2 == '*' and oper3 == '+':
        print(num1 * num2 * num3 + num4)

    elif oper == '/' and oper2 == '/' and oper3 == '+':
        print(num1 / num2 + num3 / num4)
#switch------------------------------------------------
    elif oper == '+' and oper2 == '-' and oper3 == '-':
        print(num1 + num2 - num3 - num4)
    
    elif oper == '+' and oper2 == '*' and oper3 == '*':
        print(num1 * num2 * num3 + num4)

    elif oper == '+' and oper2 == '/' and oper3 == '/':
        print(num1 / num2 / num3 + num4)
#switch X2---------------------------------------------
    elif oper == '-' and oper2 == '+' and oper3 == '-':
        print(num1 - num2 + num3 - num4)

    elif oper == '*' and oper2 == '+' and oper3 == '*':
        print(num1 * num2 * num3 + num4)

    elif oper == '/' and oper2 == '+' and oper3 == '/':
        print(num1 / num2 / num3 + num4)
#div mult sub-------------------------------------------
    elif oper == '/' and oper2 == '*' and oper3 == '-':
        print(num1 / num2 * num3 - num4)

    elif oper == '*' and oper2 == '-' and oper3 == '/':
        print(num1 * num2 / num3 - num4)

    elif oper == '/' and oper2 == '-' and oper3 == '*':
        print(num1 / num2 * num3 - num4)

    elif oper == '*' and oper2 == '/' and oper3 == '-':
        print(num1 * num2 / num3 - num4)

    elif oper == '-' and oper2 == '*' and oper3 == '/':
        print(num1 * num2 / num3 - num4)

    elif oper == '-' and oper2 == '/' and oper3 == '*':
        print(num1 / num2 * num3 - num4)
#something---------------------------------------------
    elif oper == '/' and oper2 == '+' and oper3 == '/':
        print(num1 / num2 / num3 + num4)

    elif oper == '/' and oper2 == '-' and oper3 == '/':
        print(num1 / num2 / num3 - num4)

    elif oper == '/' and oper2 == '*' and oper3 == '/':
        print(num1 / num2 * num3 / num4)

    elif oper == '/' and oper2 == '+' and oper3 == '/':
        print(num1 / num2 / num3 + num4)
#more-------------------------------------------------
    elif oper == '/' and oper2 == '/' and oper3 == '/':
        print(num1 / num2 / num3 / num4)

    elif oper == '*' and oper2 == '*' and oper3 == '*':
        print(num1 * num2 * num3 * num4)

    elif oper == '-' and oper2 == '-' and oper3 == '-':
        print(num1 - num2 - num3 - num4)
#div mult add-----------------------------------------
    elif oper == '/' and oper2 == '*' and oper3 == '+':
        print(num1 / num2 * num3 + num4)

    elif oper == '*' and oper2 == '+' and oper3 == '/':
        print(num1 * num2 / num3 + num4)

    elif oper == '/' and oper2 == '+' and oper3 == '*':
        print(num1 / num2 * num3 + num4)

    elif oper == '*' and oper2 == '/' and oper3 == '+':
        print(num1 * num2 / num3 + num4)

    elif oper == '+' and oper2 == '*' and oper3 == '/':
        print(num1 * num2 / num3 + num4)

    elif oper == '+' and oper2 == '/' and oper3 == '*':
        print(num1 / num2 * num3 + num4)
#div add sub--------------------------------------------
    elif oper == '/' and oper2 == '+' and oper3 == '-':
        print(num1 / num2 + num3 - num4)

    elif oper == '/' and oper2 == '-' and oper3 == '+':
        print(num1 / num2 - num3 + num4)

    elif oper == '+' and oper2 == '/' and oper3 == '-':
        print(num1 / num2 + num3 - num4)

    elif oper == '-' and oper2 == '/' and oper3 == '+':
        print(num1 / num2 - num3 + num4)
    elif oper == '-' and oper2 == '+' and oper3 == '/':
        print(num1 / num2 - num3 + num4)    
    elif oper == '+' and oper2 == '-' and oper3 == '/':
        print(num1 / num2 + num3 - num4)
#mult add sub-------------------------------------------
    elif oper == '*' and oper2 == '+' and oper3 == '-':
        print(num1 * num2 + num3 - num4)
    elif oper == '*' and oper2 == '-' and oper3 == '+':
        print(num1 * num2 - num3 + num4)
    elif oper == '-' and oper2 == '*' and oper3 == '+':
        print(num1 * num2 - num3 + num4)
    elif oper == '+' and oper2 == '*' and oper3 == '-':
        print(num1 * num2 + num3 - num4)
    elif oper == '+' and oper2 == '-' and oper3 == '*':
        print(num1 * num2 + num3 - num4)
    elif oper == '-' and oper2 == '+' and oper3 == '*':
        print(num1 * num2 - num3 + num4)