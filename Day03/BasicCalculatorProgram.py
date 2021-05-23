print("Welcome To My Calculator! Please Select operation Number to perform")

operation = int(input("1. Add \n2. Subtract \n3. Multiply \n4. Divide \n"))

num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a second number: "))

def add(num1,num2):
  return round(num1+num2)

def subtract(num1,num2):
  return num1-num2

def multiply(num1,num2):
  return num1*num2

def divide(num1,num2):
  return num1/num2


if operation == 1:
  print(f"{add(num1,num2)}")
elif operation==2:
  print(f"{subtract(num1,num2)}")
elif operation==3:
  print(f"{multiply(num1,num2)}")
else:
  print(f"{divide(num1,num2)}")
