#7/12/2023
#Margarita Chistiakova

print("Hello! Welcome to the 'Advanced Calculator' program!\n")

choice = 0
while choice != 2:
  print("""We have the following operators: 
  1. Addition (+)
  2. Subtraction (-)
  3. Multiplication (*)
  4. Division (/)
  5. Modulus (%)
  6. Exponentation (**)
  7. Floor division (//)""")
  print("\nNotice, you can't use more than 6 numbers in one operation!!!")
  
  print("How many numbers do you want to use?")
  amountOfNum = int(input())
  
  if amountOfNum == 2:
    print("Please enter the first number: ")
    num1 = int(input())
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the second numer: ")
    num2 = int(input())
    if operatorChoice == "+":
      result = (num1 + num2)
      print(f"The result of the operation is {result}")
    elif operatorChoice == "-":
      result = num1 - num2
      print(f"The result of the operation is {result}")
    elif operatorChoice == "*":
      result = num1 * num2
      print(f"The result of the operation is {result}")
    elif operatorChoice == "/":
      result = num1 / num2
      print(f"The result of the operation is {result}")
    elif operatorChoice == "%":
      result = num1 % num2
      print(f"The result of the operation is {result}")
    elif operatorChoice == "**":
      result = num1 ** num2
      print(f"The result of the operation is {result}")
    elif operatorChoice == "//":
      result = num1 // num2
      print(f"The result of the operation is {result}")
    print("Do you wish to continue using the calculator? press 1 for 'yes and 2 for 'no'")
    choice = int(input())
      
  elif amountOfNum == 3:
    print("Please enter the first number: ")
    num1 = int(input())
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the second numer: ")
    num2 = int(input())
    if operatorChoice == "+":
      result = (num1 + num2)
    elif operatorChoice == "-":
      result = num1 - num2
    elif operatorChoice == "*":
      result = num1 * num2
    elif operatorChoice == "/":
      result = num1 / num2
    elif operatorChoice == "%":
      result = num1 % num2
    elif operatorChoice == "**":
      result = num1 ** num2
    elif operatorChoice == "//":
      result = num1 // num2
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the third number: ")
    num3 = int(input())
    if operatorChoice == "+":
      result2 = result + num3
      print(f"The result of the operation is {result2}")
    elif operatorChoice == "-":
      result2 = result - num3
      print(f"The result of the operation is {result2}")
    elif operatorChoice == "*":
      result2 = result * num3
      print(f"The result of the operation is {result2}")
    elif operatorChoice == "/":
      result2 = result / num3
      print(f"The result of the operation is {result2}")
    elif operatorChoice == "%":
      result2 = result % num3
      print(f"The result of the operation is {result2}")
    elif operatorChoice == "**":
      result2 = result ** num3
      print(f"The result of the operation is {result2}")
    elif operatorChoice == "//":
      result2 = result // num3
      print(f"The result of the operation is {result2}")
    print("Do you wish to continue using the calculator? press 1 for 'yes and 2 for 'no'")
    choice = int(input())
  
  elif amountOfNum == 4:
    print("Please enter the first number: ")
    num1 = int(input())
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the second numer: ")
    num2 = int(input())
    if operatorChoice == "+":
      result = (num1 + num2)
    elif operatorChoice == "-":
      result = num1 - num2
    elif operatorChoice == "*":
      result = num1 * num2
    elif operatorChoice == "/":
      result = num1 / num2
    elif operatorChoice == "%":
      result = num1 % num2
    elif operatorChoice == "**":
      result = num1 ** num2
    elif operatorChoice == "//":
      result = num1 // num2
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the third number: ")
    num3 = int(input())
    if operatorChoice == "+":
      result2 = result + num3
    elif operatorChoice == "-":
      result2 = result - num3
    elif operatorChoice == "*":
      result2 = result * num3
    elif operatorChoice == "/":
      result2 = result / num3
    elif operatorChoice == "%":
      result2 = result % num3
    elif operatorChoice == "**":
      result2 = result ** num3
    elif operatorChoice == "//":
      result2 = result // num3
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the forth number: ")
    num4 = int(input())
    if operatorChoice == "+":
      result3 = result2 + num4
      print(f"The result of the operation is {result3}")
    elif operatorChoice == "-":
      result3 = result2 - num4
      print(f"The result of the operation is {result3}")
    elif operatorChoice == "*":
      result3 = result2 * num4
      print(f"The result of the operation is {result3}")
    elif operatorChoice == "/":
      result3 = result2 / num4
      print(f"The result of the operation is {result3}")
    elif operatorChoice == "%":
      result3 = result2 % num4
      print(f"The result of the operation is {result3}")
    elif operatorChoice == "**":
      result3 = result2 ** num4
      print(f"The result of the operation is {result3}")
    elif operatorChoice == "//":
      result3 = result2 // num4
      print(f"The result of the operation is {result3}")
    print("Do you wish to continue using the calculator? press 1 for 'yes and 2 for 'no'")
    choice = int(input())
  
  elif amountOfNum == 5:
    print("Please enter the first number: ")
    num1 = int(input())
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the second numer: ")
    num2 = int(input())
    if operatorChoice == "+":
      result = (num1 + num2)
    elif operatorChoice == "-":
      result = num1 - num2
    elif operatorChoice == "*":
      result = num1 * num2
    elif operatorChoice == "/":
      result = num1 / num2
    elif operatorChoice == "%":
      result = num1 % num2
    elif operatorChoice == "**":
      result = num1 ** num2
    elif operatorChoice == "//":
      result = num1 // num2
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the third number: ")
    num3 = int(input())
    if operatorChoice == "+":
      result2 = result + num3
    elif operatorChoice == "-":
      result2 = result - num3
    elif operatorChoice == "*":
      result2 = result * num3
    elif operatorChoice == "/":
      result2 = result / num3
    elif operatorChoice == "%":
      result2 = result % num3
    elif operatorChoice == "**":
      result2 = result ** num3
    elif operatorChoice == "//":
      result2 = result // num3
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the forth number: ")
    num4 = int(input())
    if operatorChoice == "+":
      result3 = result2 + num4
    elif operatorChoice == "-":
      result3 = result2 - num4
    elif operatorChoice == "*":
      result3 = result2 * num4
    elif operatorChoice == "/":
      result3 = result2 / num4
    elif operatorChoice == "%":
      result3 = result2 % num4
    elif operatorChoice == "**":
      result3 = result2 ** num4
    elif operatorChoice == "//":
      result3 = result2 // num4
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the fifth number: ")
    num5 = int(input())
    if operatorChoice == "+":
      result4 = result3 + num5
      print(f"The result of the operation is {result4}")
    elif operatorChoice == "-":
      result4 = result3 - num5
      print(f"The result of the operation is {result4}")
    elif operatorChoice == "*":
      result4 = result3 * num5
      print(f"The result of the operation is {result4}")
    elif operatorChoice == "/":
      result4 = result3 / num5
      print(f"The result of the operation is {result4}")
    elif operatorChoice == "%":
      result4 = result3 % num5
      print(f"The result of the operation is {result4}")
    elif operatorChoice == "**":
      result4 = result3 ** num5
      print(f"The result of the operation is {result4}")
    elif operatorChoice == "//":
      result4 = result3 // num5
      print(f"The result of the operation is {result4}")
    print("Do you wish to continue using the calculator? press 1 for 'yes and 2 for 'no'")
    choice = int(input())
  
  elif amountOfNum == 6:
    print("Please enter the first number: ")
    num1 = int(input())
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the second numer: ")
    num2 = int(input())
    if operatorChoice == "+":
      result = (num1 + num2)
    elif operatorChoice == "-":
      result = num1 - num2
    elif operatorChoice == "*":
      result = num1 * num2
    elif operatorChoice == "/":
      result = num1 / num2
    elif operatorChoice == "%":
      result = num1 % num2
    elif operatorChoice == "**":
      result = num1 ** num2
    elif operatorChoice == "//":
      result = num1 // num2
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the third number: ")
    num3 = int(input())
    if operatorChoice == "+":
      result2 = result + num3
    elif operatorChoice == "-":
      result2 = result - num3
    elif operatorChoice == "*":
      result2 = result * num3
    elif operatorChoice == "/":
      result2 = result / num3
    elif operatorChoice == "%":
      result2 = result % num3
    elif operatorChoice == "**":
      result2 = result ** num3
    elif operatorChoice == "//":
      result2 = result // num3
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the forth number: ")
    num4 = int(input())
    if operatorChoice == "+":
      result3 = result2 + num4
    elif operatorChoice == "-":
      result3 = result2 - num4
    elif operatorChoice == "*":
      result3 = result2 * num4
    elif operatorChoice == "/":
      result3 = result2 / num4
    elif operatorChoice == "%":
      result3 = result2 % num4
    elif operatorChoice == "**":
      result3 = result2 ** num4
    elif operatorChoice == "//":
      result3 = result2 // num4
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the fifth number: ")
    num5 = int(input())
    if operatorChoice == "+":
      result4 = result3 + num5
    elif operatorChoice == "-":
      result4 = result3 - num5
    elif operatorChoice == "*":
      result4 = result3 * num5
    elif operatorChoice == "/":
      result4 = result3 / num5
    elif operatorChoice == "%":
      result4 = result3 % num5
    elif operatorChoice == "**":
      result4 = result3 ** num5
    elif operatorChoice == "//":
      result4 = result3 // num5
    print("Please enter the symbol of the operator you want to use: ")
    operatorChoice = input()
    print("Please enter the sixth number: ")
    num6 = int(input())
    if operatorChoice == "+":
      result5 = result4 + num6
      print(f"The result of the operation is {result5}")
    elif operatorChoice == "-":
      result5 = result4 - num6
      print(f"The result of the operation is {result5}")
    elif operatorChoice == "*":
      result5 = result4 * num6
      print(f"The result of the operation is {result5}")
    elif operatorChoice == "/":
      result5 = result4 / num6
      print(f"The result of the operation is {result5}")
    elif operatorChoice == "%":
      result5 = result4 % num6
      print(f"The result of the operation is {result5}")
    elif operatorChoice == "**":
      result5 = result4 ** num6
      print(f"The result of the operation is {result5}")
    elif operatorChoice == "//":
      result5 = result4 // num6
      print(f"The result of the operation is {result5}")
    print("Do you wish to continue using the calculator? press 1 for 'yes and 2 for 'no'")
    choice = int(input())
  


  