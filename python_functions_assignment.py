def welcome_user():
    print("Welcome to our amazing weather app!")

def get_user_location_and_temperature():
    city = input("What city are you in? ")
    temperature = input(f"What is the current temperature in {city}? ")
    
    if city and temperature:
        print(f"You are in {city} and it is currently {temperature}ºC")
    else:
        print("You did not provide a city and/or temperature.")

get_user_location_and_temperature()
get_user_location_and_temperature()
