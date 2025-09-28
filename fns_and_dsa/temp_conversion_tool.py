# Global conversion factors
CELSIUS_TO_FAHRENHEIT = 9/5
FREEZING_OFFSET = 32
CELSIUS_TO_KELVIN = 273.15
FAHRENHEIT_TO_CELSIUS = 5/9
KELVIN_TO_CELSIUS = -273.15

def celsius_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT + FREEZING_OFFSET

def celsius_to_kelvin(celsius):
    return celsius + CELSIUS_TO_KELVIN

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - FREEZING_OFFSET) * FAHRENHEIT_TO_CELSIUS

def kelvin_to_celsius(kelvin):
    return kelvin + KELVIN_TO_CELSIUS

# User interaction with error handling
try:
    print("Temperature Conversion Tool")
    temp = float(input("Enter temperature value: "))
    if temp < -273.15:  # Absolute zero in Celsius
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
    
    unit_from = input("Convert from (C)elsius, (F)ahrenheit, or (K)elvin? ").lower()
    unit_to = input("Convert to (C)elsius, (F)ahrenheit, or (K)elvin? ").lower()

    # Perform conversion
    if unit_from == 'c' and unit_to == 'f':
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")
    elif unit_from == 'c' and unit_to == 'k':
        result = celsius_to_kelvin(temp)
        print(f"{temp}°C is {result}K")
    elif unit_from == 'f' and unit_to == 'c':
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {result}°C")
    elif unit_from == 'k' and unit_to == 'c':
        result = kelvin_to_celsius(temp)
        print(f"{temp}K is {result}°C")
    else:
        print("Invalid conversion combination. Please use C, F, or K.")

except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
