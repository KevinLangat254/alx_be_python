FAHRENHEIT_TO_CELSIUS_FACTOR= 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR  = 9 / 5
def  convert_to_celsius(fahrenheit) :
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def  convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
while True:
    try:
        temperature = float(input('Enter the temperature to convert: '))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

while True:
    unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ')
    if unit.upper() == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
        break
    elif unit.upper() == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
        break
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")