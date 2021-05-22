current_age = float(input("what is your current age "))

months = (90-current_age)*12
years = months/12
weeks = years*52
days = years*365

print(f"You have {days} days , {weeks} weeks , {months} months left to live")