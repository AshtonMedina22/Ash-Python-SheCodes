def calculate_fahrenheit_temperature(celsius_temperature):
    """Calculates the farenheit value from celsius value."""
    farenheit_temperature = (float(celsius_temperature) * 9/5) + 32
    return farenheit_temperature

temperature = 15
fahrenheit_temperature = calculate_fahrenheit_temperature(temperature)
city = "London"
print(f"It is currently {temperature}ºC ({round(fahrenheit_temperature)}ºF) in {city}.")
