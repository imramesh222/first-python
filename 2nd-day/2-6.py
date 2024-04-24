height=input("Enter your height: ")
weight=input("Enter your weight: ")

height_int=int(height)
weight_int=int(weight)
bmi=weight_int/height_int**2
bmi_int=int(bmi)
print(bmi_int)
