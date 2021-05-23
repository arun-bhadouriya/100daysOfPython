year = int(input("Enter a year to check If it's a Leap year Or not?"))

if year%4!=0:
  print(f"{year} is Not Leap Year!")
elif year%100!=0:
  print(f"{year} is a Leap Year")
elif year%400==0:
  print(f"{year} is a Leap Year")
else:
  print(f"{year} is not a leap year. ")

