#Small pizza : $15
#Medium pizza : $20
#Large pizza : $25
# Pepperoni for small pizza : +$2
# Pepperoni form large pizza : +$3  
# Extra cheese for any size pizza : +$1

print("# Small pizza : $15 \n# Medium pizza : $20 \n# Large pizza : $25 \n# Pepperoni for small pizza : +$2 \n# Pepperoni form large pizza : +$3 \n# Extra cheese for any size pizza : +$1",end = " ") 

input("\n\nTo buy please press ENTER")

size = input("Please enter your preffered size for the pizza? S,M,L ")
wants_pepperoni = input("Extra Pepperoni? Y , N? ")
wants_chesse = input("Extra Cheese? Y, N? ")
bill=0 


if size == "S" :
  bill=15
elif size =="M" :
  bill=20
  # print(f"your bill for Medium pizza is ${bill}")
else:
  bill=25
  # print(f"your bill for Medium pizza is ${bill}")

if wants_pepperoni=="Y" and size=="S":
  bill+=2
else:
  bill+=3

if wants_chesse == "Y":
  bill+=1

print(f"\nYou'r total bill is ${bill} , Have a Great Meal! :)")
