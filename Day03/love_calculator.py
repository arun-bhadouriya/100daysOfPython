print("Hey there! Welcome to Love calculator")

name = input("Please Enter Your Name ? ")
lover_name = input("Please Enter Their Name? ")

combined_str = (name+lover_name).lower()

t_count = combined_str.count("t")
r_count = combined_str.count("r")
u_count = combined_str.count("u")
e_count = combined_str.count("e")
l_count = combined_str.count("l")
o_count = combined_str.count("o")
v_count = combined_str.count("v")
e_count = combined_str.count("e")



first = t_count+r_count+u_count+e_count;

second = l_count+o_count+v_count+e_count;


while second>9 : 
  second=second-10
  first+=1


percentage = first*10 + second

print(f"Your Love percentage is {percentage}")

