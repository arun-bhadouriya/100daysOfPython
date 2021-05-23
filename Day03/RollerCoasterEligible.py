print("Welcome to the Roller Coaster Ride!!")
height = float(input("What's your Height in m? "))

height_in_cm = height*100

# if height_in_cm > 120: 
#   print("Hurray You can Ride the Roller Coaster!")
# else: 
#   print("Oops ! You Aren't Eligible To ride the roller Coaster") 


if height_in_cm <=120:
  print("Oops ! You Aren't Eligible To ride the roller Coaster")
else:
  # bill=0
  age = float(input("What's your age?"))
  if age<12:
    bill=5
  elif age<=18:
    bill=7
  else:
    bill=12

  photos = input("Do you want Photos?")
  if photos=="Yes" or photos=="yes" or photos=="YES":
    bill+=3 
  
print(f"The total bill is ${bill} .")