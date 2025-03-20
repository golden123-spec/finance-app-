# simple temperature converter program in python 
# Goal: The program’s purpose is to convert a temperature from one unit to another, for example, from Celsius to Fahrenheit.
# User Interaction: The program will prompt the user to enter a temperature value (say, in Celsius) and then output the corresponding temperature in Fahrenheit.


# function to take in users input

# input variable to recieve user input
print("temperature converter program")


tempinput = int(input("Enter the temprature(Celcius(1) or Fahrenheit(2))"))


if tempinput  == 1:
    Celcius = float(input("Enter temperature in Celcius: "))
    celcius_temperature = (Celcius * 9/5) + 32
    print("The tempreture is" , celcius_temperature,"in fahrenheit")
elif tempinput == 2:
    Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    fahrenheit_temperature = (Fahrenheit - 32) * 5/9 
    print("The temperature is ", fahrenheit_temperature, "in celcius")
else:
    pass





