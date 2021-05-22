print("Welcome to Tip Calculator")

total_bill = float(input("What is the Total Bill? $"))
total_person = float(input("Ho many people to split the bill? "))
percent = float(input("What Percentage tip you would like to give? 10,12, or 15? "))

# Calculation for the tip and the share each person will pay
each_person_pay = (total_bill/total_person)+((total_bill/total_person)*(percent/100))

print(f"each person pays ${round(each_person_pay,2)}")



# num_char = len(input("wht is your name? "))
# print(type(num_char))
# print("your name is of " + str(num_char) + " charachters")

# print(((3*(3+3))/3)-3)