favorite_countries = {
    "Japan": "Tokyo",
    "Ecuador": "Quito",
    "Colombia": "Bogota"
}

print("Countries I'd like to visit:")

index = 0
for country, capital_city in favorite_countries.items():
    print(f"{index + 1}. {country} (Capital city: {capital_city})")
    index = index + 1
