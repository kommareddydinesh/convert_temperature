def convert_temp(val, scale):
    # Temperature converter for F <-> C
    if scale == 'F':
        # Fahrenheit to Celsius
        c = (val - 32) * 5 / 9
        return round(c, 2)
    elif scale == 'C':
        # Celsius to Fahrenheit
        f = (val * 9 / 5) + 32
        return round(f, 2)
    else:
        return "Oops, invalid unit. Use 'F' or 'C' please."
try:
    user_temp = float(input("Enter the temperature value: "))
    user_unit = input("Enter the unit (F or C): ").strip().upper()

    result = convert_temp(user_temp, user_unit)
    print("Converted temperature:", result)
except ValueError:
    print("Hmm, that doesn't look like a number.")
