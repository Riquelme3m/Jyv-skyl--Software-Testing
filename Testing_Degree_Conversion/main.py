# The exercise starter code contains a fahrenheit_to_celsius function that 
# converts a temperature in Fahrenheit to Celsius.

# Write a test or tests to check that the function converts the values 
# correctly to a precision of at least five decimal places.

# A sufficiently comprehensive test suite would check for example that
# 212°F is 100°C
# 98.6°F is 37°C
# 70°F is 21.11111°C
# 32°F is 0°C
# 0°F is -17.77778°C
# -40°F is -40°C

# The test or tests should be set up so that pytest can automatically locate them.



def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9