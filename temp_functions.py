"""Two functions stored in this script
    The first is a Fahrenheit to Celsius converter and
    the second is a temperature classifier based on weather conditions"""

def fahr_to_celsius(temp_fahrenheit):
    """Function to convert temperatures from Fahrenheit to Celsius
        The temperature to be converted should be inputted
        Then the calculator returns the value of the temperature in Celsius"""
    converted_temp = (temp_fahrenheit - 32) / 1.8
    return converted_temp

def temp_classifier(temp_celsius):
    """Temperature classifier function classifying temperatures based on condtions of integer values of temperatures
        Using conditional statements the function would return an interger value of 0, 1 ,2 or 3 based on value of user inputed temperatures"""
    if temp_celsius < -2:
        return 0
    elif temp_celsius >= -2 and temp_celsius < 2: #Always insert both comparisons
        return 1
    elif temp_celsius >= 2 and temp_celsius < 15:
        return 2
    elif temp_celsius >= 15:
        return 3