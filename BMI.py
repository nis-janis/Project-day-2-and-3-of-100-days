height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = weight / (height ** 2)
BMI = round(BMI)
# variable to test the calculation of each level
# BMI=50
if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are UNDERWEIGHT.")
elif BMI <= 25:
    print(f"Your BMI is {BMI}, you are NORMAL WEIGHT.")
elif BMI <= 30:
    print(f"Your BMI is {BMI}, you are SLIGHTLY OVERWEIGHT.")
elif BMI <= 35:
    print(f"Your BMI is {BMI}, you are OBESE.")
else:
    print(f"Your BMI is {BMI}, you are CLINICALLY OBESE.")
