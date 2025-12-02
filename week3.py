def convert_celsius_to_fahrenheit(celsius_value):
    """Converts a Celsius value into Fahrenheit"""
    fahrenheit_value = (float(celsius_value) * 9/5) + 32
    return fahrenheit_value

def display_temperature(city_name, temperature):
    """Displays the temperature of a city"""
    fahrenheit_temperature = convert_celsius_to_fahrenheit(temperature)
    print(f"It is currently {temperature}ºC ({round(fahrenheit_temperature)}ºF) in {city_name.capitalize()}")

city = input("Enter the name of the city: ")
celsius_temperature = input(f"Enter the temperature in {city.capitalize()}: ")

if city and celsius_temperature:
    display_temperature(city, celsius_temperature)
else:
    print("You did not enter a city and/or temperature")
