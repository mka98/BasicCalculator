num1 = int(input("Enter First Number: "))#takeing only int input
op = input("Enter Operater + - / *: ")
num2 = int(input("Enter Second Number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator") 
    
    
    
    
    
#result = num1 + num2 #or i could change the varibles to int e.g. int(num1) + int(num2)
#print(result)