"""Problem 1 (50 pts)
Write a program that prompts the user to enter a temperature in Fahrenheit,
then calculates and displays the corresponding temperature in Celsius, using the formula:
"""

#problem 1
#formula = temperature_celsius = (temperature_fahrenheit-32) * 5/9

#ask user inputs
asking_temperature = float(input("Enter the temperature in Fahrenheit: "))

#calculate and convert
temperature_in_celsius = (asking_temperature - 32) * 5/9

#print output and if-statement
print(f"The temperature in Celsius is {temperature_in_celsius:.1f}")

if temperature_in_celsius <= 0:
    print("Ice")
elif (temperature_in_celsius > 0) and (temperature_in_celsius <= 100):
    print("Liquid")
else:
    print("Gas")