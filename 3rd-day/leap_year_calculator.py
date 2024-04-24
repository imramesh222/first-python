print("Leap year calculator!")

year=int(input("Enter a year which you want to check whether it is leap year or not\n"))

if year%4==0:
  if year%100==0:
    if year%400==0:
      print(f"{year} is a leap year")
    else:
      print(f"{year} is not a leap year")
  else:
    print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")