import math

'''
Take the input from the user of temperature t and wind speed v 
print the windchill
w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16);
condition is if t is larger than 50 and also v is larger than 120 or less than 3 
'''


def wind_chill():
    try:
        temperature = float(input(" Enter the Temperature value (Fahrenheit) : "))
        if temperature > 50:
            print(" Enter a temperature value less than 50")

        # checking the condition wind speed is greater than 120 or wind speed less than 3
        wind_speed = float(input(" Enter the value of wind speed (Miles per hour) : "))
        if wind_speed > 120 or wind_speed < 3:
            print(" Enter a wind speed value between 120 and 3")

        # calculating the wind chill using formula
        windchill = 35.74 + 0.6215 * temperature + (0.4275 * temperature - 35.75) * math.pow(wind_speed, 0.16);
        print(" The Temperature value is: ", temperature)
        print(" The wind speed value is: ", wind_speed)
        print(" The wind Chill is: ", windchill)

    except ValueError:
        print("Something went wrong!please enter again")


if __name__ == "__main__":
    wind_chill()
