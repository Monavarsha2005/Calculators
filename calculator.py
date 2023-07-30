while True:
    a=input("enter the value of a or 'g' to exit the program:")
    if a == 'g': 
       break
       
    b=input("enter the value of b:")
    operator = input("Enter the operator: ")


    if operator == '+':
        result=int(a)+int(b)
        print(result)
    elif operator == '-':
        result=int(a)-int(b)
        print(result)
    elif operator == '*':
        result=int(a)*int(b)
        print(result)
    elif operator == '/':
        if int(b)!=0:
          result=int(a)/int(b)
          print(result)
        else:
            print("Error in division operator")
    elif operator == '//':
        result=int(a)//int(b)
        print(result)
    elif operator == '^':
        result=int(a)^int(b)
        print(result)
    else:
        print("INVALID OPERATOR, Please try again.")
print("The calculator program is end")
        
