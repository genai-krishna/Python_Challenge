# Weather Temperature Converter
# ------------------------------
# This program converts temperature between Celsius, Fahrenheit, and Kelvin.
# It also gives basic weather advice based on the temperature value.
# Concepts used: functions, conditional logic, user input, and math operations.

# Function to convert temperature between different units
def convert_temperature(value, from_unit, to_unit):
    # Convert input temperature to Celsius first
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = (value - 32) * 5 / 9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        return None  # Invalid input unit

    # Now convert Celsius to target unit
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return (celsius * 9 / 5) + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:
        return None  # Invalid target unit


# Function to provide weather advice based on Celsius temperature
def weather_advice(celsius):
    if celsius < 0:
        return "It's freezing! Dress warmly."
    elif 0 <= celsius < 15:
        return "It's quite cold. Wear a jacket."
    elif 15 <= celsius < 25:
        return "The weather is pleasant!"
    elif 25 <= celsius < 35:
        return "It's quite warm! Stay hydrated."
    else:
        return "It's very hot! Avoid going out in the sun for long."


# Main program logic
def main():
    print("===== Weather Temperature Converter =====")

    # Get user inputs
    value = float(input("Enter temperature value: "))
    from_unit = input("Enter current unit (C/F/K): ").upper()
    to_unit = input("Enter target unit (C/F/K): ").upper()

    # Perform conversion
    converted = convert_temperature(value, from_unit, to_unit)

    # If invalid input, handle it
    if converted is None:
        print("❌ Invalid temperature unit entered!")
        return

    # Convert the input temperature to Celsius to get advice
    celsius_equiv = convert_temperature(value, from_unit, 'C')

    # Get advice based on Celsius temperature
    advice = weather_advice(celsius_equiv)

    # Display results
    print(f"\nConverted Temperature: {round(converted, 2)}°{to_unit}")
    print(f"Weather Advice: {advice}")


# Run the program
if __name__ == "__main__":
    main()
