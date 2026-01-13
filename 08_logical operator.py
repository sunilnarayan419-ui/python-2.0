# logical operators = evaluate multiple conditions ( or , and , not )
# or = at least one condition must be True 
# and = both  condition must be True 
# not = inverts the conditions ( not False , not True )

temp = 34
is_sunny = False


if temp >= 28 and is_sunny:
    print(f"It is HOT outside 🥵🥵")
    print(f" It is SUNNY 🌞🌞")
elif temp <= 0 and is_sunny:
    print(f"It is COLD outside 🥶😰")
    print(f" It is SUNNY 🌞🌞") 
elif temp < 28 and temp > 0 and is_sunny:
    print(f"It is WARM outside 😊")
    print(f" It is SUNNY 🌞🌞")
    
if temp >= 28 and not is_sunny:
    print(f"It is HOT outside 🥵🥵")
    print(f" It is CLOUDY ⛅⛅")
elif temp <= 0 and not  is_sunny:
    print(f"It is COLD outside 🥶😰")
    print(f" It is CLOUDY ⛅⛅") 
elif temp < 28 and temp > 0 and not is_sunny:
    print(f"It is WARM outside 😊")
    print(f" It is CLOUDY ⛅⛅")
    
    
    
    