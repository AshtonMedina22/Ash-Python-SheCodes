def display_temperature(city, temperature, humidity=None):
    """Displays the temperature and humidity of a city."""
    message = f"The temperature in {city} is {temperature} degrees"
    if humidity:
        message = f"{message} with a humidity of {humidity}%"
    print(f"{message}.")

display_temperature("London", 7, 40)
display_temperature("New York", 7)
