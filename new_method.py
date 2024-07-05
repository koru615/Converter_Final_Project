from tabulate import tabulate
from decimal import *

units_options = [
    ["code","unit"], ["1","length"], ["2","volume"], ["3","mass"], ["4","temperature"]
]

unit_reference = {
    "1":"length", "2":"volume", "3":"mass", "4":"temperature"
}

units_length = [
    "inches", "feet", "yards", "miles", "millimeter", "centimeter", "kilometer", "meter"
]

units_volume = [
    "fluid oz", "pint", "gallon", "table spoon", "tea spoon", "quart", "cup", "liter", "milliliter"
]

units_mass = [
    "kilogram", "gram", "milligram", "metric ton", "US ton", "pounds", "ounces", "carat"
]

units_temp = [
    "celsius", "kelvin", "farenheit"
]

abbreviations = {
    "inches":"in", "feet":"ft", "yards":"yd", "miles":"mi", "millimeter":"mm", "centimeter":"cm", "kilometer":"km", "meter":"m",
    "fluid oz":"fl oz", "pint":"pt", "gallon":"gal", "table spoon":"tbsp", "tea spoon":"tsp", "quart":"qt", "cup":"cup", "liter":"L", "milliliter":"mL",
    "kilogram":"kg", "gram":"g", "milligram":"mg", "metric ton":"t", "US ton":"t (US)", "pounds":"lbs", "ounces":"oz", "carat":"ct",
    "celsius":"°C", "kelvin":"K", "farenheit":"°F",
}

conversion_factor = {
    "meter": {
        "inches": 39.37,
        "feet": 3.281,
        "yards": 1.094,
        "miles": 1 / 1609,
        "millimeter": 1000,
        "centimeter": 100,
        "kilometer": 1 / 1000,
        "meter": 1,
    },

    "liter": {
        "fluid oz": 33.814,
        "pint": 2.11338,
        "gallon": 1 / 3.785,
        "table spoon": 67.628,
        "tea spoon": 202.884,
        "quart": 1.057,
        "cup": 4.227,
        "liter": 1,
        "milliliter": 1000,
    },

    "kilogram": {
        "kilogram": 1,
        "gram": 1000,
        "milligram": 1e+6,
        "metric ton": 1 / 1000,
        "US ton": 1 / 907.2,
        "pounds": 2.20462,
        "ounces": 35.274,
        "carat": 5000,
    },
}

def main():
    print()
    print("Welcome to the basic unit converter")
    print(tabulate(units_options, headers="firstrow", tablefmt="pretty"))
    print("Please enter the code for the unit you would like to convert")
    selected_unit = get_units()
    from_type = get_data_type(selected_unit, selection_type=1)
    to_type = get_data_type(selected_unit, selection_type=2)
    print()
    print(f"You are converting From: {from_type} -> To: {to_type}")
    print()
    from_value = get_data(from_type)
    from_value = float(from_value)
    print()
    if selected_unit == "1":
        converted_data = convert_length(from_type, to_type, from_value)
    elif selected_unit == "2":
        converted_data = convert_volume(from_type, to_type, from_value)
    elif selected_unit == "3":
        converted_data = convert_mass(from_type, to_type, from_value)
    elif selected_unit == "4":
        converted_data = convert_temp(from_type, to_type, from_value)
    package_data = [from_type, to_type, from_value, converted_data]
    final_equation = format_response(package_data)
    print(final_equation)


def get_units():
    while True:
        try:
            selected_unit = input("Code: ").strip()
            if selected_unit in ["1", "2", "3", "4"]:
                print()
                print(f"You have selected {unit_reference[selected_unit]}")
                break
        except ValueError:
            pass
    return selected_unit


def get_data_type(selected_unit, selection_type):
    print()
    if selection_type == 1:
        phrase = "from"
    elif selection_type == 2:
        phrase = "to"

    if selected_unit == "1":
        print(tabulate(enumerate(units_length, start=1), tablefmt="pretty"))
        print(f"Please enter the code for the unit you would like to convert {phrase}")
        while True:
            try:
                from_unit = input("Code: ").strip()
                if from_unit in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                    from_unit = units_length[(int(from_unit) - 1)]
                    print(f"You have selected {from_unit}")
                    break
                else:
                    pass
            except ValueError:
                pass
    elif selected_unit == "2":
        print(tabulate(enumerate(units_volume, start=1), tablefmt="pretty"))
        print(f"Please enter the code for the unit you would like to convert {phrase}")
        while True:
            try:
                from_unit = input("Code: ").strip()
                if from_unit in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    from_unit = units_volume[(int(from_unit) - 1)]
                    print(f"You have selected {from_unit}")
                    break
                else:
                    pass
            except ValueError:
                pass
    elif selected_unit == "3":
        print(tabulate(enumerate(units_mass, start=1), tablefmt="pretty"))
        print(f"Please enter the code for the unit you would like to convert {phrase}")
        while True:
            try:
                from_unit = input("Code: ").strip()
                if from_unit in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                    from_unit = units_mass[(int(from_unit) - 1)]
                    print(f"You have selected {from_unit}")
                    break
                else:
                    pass
            except ValueError:
                pass
    elif selected_unit == "4":
        print(tabulate(enumerate(units_temp, start=1), tablefmt="pretty"))
        print(f"Please enter the code for the unit you would like to convert {phrase}")
        while True:
            try:
                from_unit = input("Code: ").strip()
                if from_unit in ["1", "2", "3"]:
                    from_unit = units_temp[(int(from_unit) - 1)]
                    print(f"You have selected {from_unit}")
                    break
                else:
                    pass
            except ValueError:
                pass
    return from_unit


def get_data(from_type):
    while True:
        try:
            value = input(f"Enter data ({from_type}): ").strip()
            if check_data(value):
                break
        except ValueError:
            pass
    return value
    

def check_data(value: str):
    if value.isalpha():
        print("Data must be a number")
        return False
    else:
        try:
            float(value)
            return True
        except ValueError:
            return False


def convert_length(from_type, to_type, from_value):
    value_in_meters = from_value / conversion_factor["meter"][from_type]
    new_value = Decimal(value_in_meters * conversion_factor["meter"][to_type]).quantize(Decimal(".001"))
    print(new_value)
    return float(new_value)


def convert_volume(from_type, to_type, from_value):
    value_in_liters = from_value / conversion_factor["liter"][from_type]
    new_value = Decimal(value_in_liters * conversion_factor["liter"][to_type]).quantize(Decimal(".001"), rounding=ROUND_UP)
    print(new_value)
    return float(new_value)

def convert_mass(from_type, to_type, from_value):
    value_in_kilograms = from_value / conversion_factor["kilogram"][from_type]
    new_value = Decimal(value_in_kilograms * conversion_factor["kilogram"][to_type]).quantize(Decimal(".001"))
    print(new_value)
    return float(new_value)

def convert_temp(from_type, to_type, from_value):
    if from_type == "celsius":
        if to_type == "celsius":
            return from_value
        elif to_type == "kelvin":
            return from_value + 273.14
        elif to_type == "farenheit":
            return (from_value * 9/5) + 32
    if from_type == "kelvin":
        if to_type == "celsius":
            return from_value - 273.15
        elif to_type == "kelvin":
            return from_value
        elif to_type == "farenheit":
            return ((from_value - 273.15) * 9/5) + 32
    if from_type == "farenheit":
        if to_type == "celsius":
            return (from_value - 32) * 5/9
        elif to_type == "kelvin":
            return (from_value - 32) * 5/9 + 273.15
        elif to_type == "farenheit":
            return from_value



def format_response(data: list):
    if data[2] % 1 == 0:
        initial_data = int(data[2])
    else:
        initial_data = data[2]

    if data[3] % 1 == 0 and data[3] < 1000000 and data[3] > -1000000:
        converted_data = int(data[3])
        print("whole")
    elif data[3] > 1000000 or data[3] < -1000000:
        converted_data = "{:.4e}".format(data[3])
        print("big")
    elif (data[3] - int(data[3])) > 0 and data[3] > 1e-6:
        converted_data = round(data[3], 4)
        print("decimals")
    elif data[3] > 0 and data[3] < 1e-6:
        converted_data = "{:.4e}".format(data[3])
        print("very small")
    elif data[3] < 0 and data[3] > -1:
        converted_data = round(data[3], 4)
    elif data[3] < -1 and data[3] > -1000000:
        converted_data = round(data[3], 4)
    else:
        converted_data = data[3]

    info = str(f"{initial_data} {abbreviations[data[0]]} = {converted_data} {abbreviations[data[1]]}")
    return info


if __name__ == "__main__":
    main()