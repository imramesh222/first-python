print("BMI(Body Mass Index) calculator 2.0!")

weight=float(input("Enter your weight in kg\n"))
height=float(input("Enter your height in metre\n"))
bmi=float(weight/height**2)
print(bmi)

if bmi<18.5:
  print(f"Your bmi is {bmi}, You are Underweight")
elif bmi>18.5 and bmi<25:
    print(f"Your bmi is {bmi}, You are Normal weight")
elif bmi>25 and bmi<30:
    print(f"Your bmi is {bmi}, You are Overweight")
elif bmi>30 and bmi<35:
    print(f"Your bmi is {bmi}, You are Moderately obese")
else:
  print(f"Your bmi is {bmi}, You are clinically Obese")