height = float(input("what is your height in m? "))
weight = float(input("What is your weight in kg "))

bmi = round(weight/height**2)

if bmi<18.5 : 
  print(f"Your Bmi is: {bmi} , You Are slightly Underweight.")
elif bmi<25:
  print(f"Your Bmi is: {bmi} , You Have a Normal Weight.")
elif bmi<30:
  print(f"Your Bmi is: {bmi} , You Are Slightly OverWeight.")
elif bmi<=35:
  print(f"Your Bmi is: {bmi} , You Are Obese.") 
else:
  print(f"Your Bmi is: {bmi} , You Are Clinically Obese.")


