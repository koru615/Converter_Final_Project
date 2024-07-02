from tabulate import tabulate

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
    "kilogram", "gram", "milligram", "metric ton", "long ton", "short ton", "pounds", "ounces", "carat"
]

units_temp = [
    "celsius", "kelvin", "farenheit"
]

abbreviations = {
    "inches":"in", "feet":"ft", "yards":"yd", "miles":"mi", "millimeter":"mm", "centimeter":"cm", "kilometer":"km", "meter":"m",
    "fluid oz":"fl oz", "pint":"pt", "gallon":"gal", "table spoon":"tbsp", "tea spoon":"tsp", "quart":"qt", "cup":"cup", "liter":"L", "milliliter":"mL",
    "kilogram":"kg", "gram":"g", "milligram":"mg", "metric ton":"t", "long ton":"t (UK)", "short ton":"t (US)", "pounds":"lbs", "ounces":"oz", "carat":"ct",
    "celsius":"°C", "kelvin":"K", "farenheit":"°F",
}

decimal_options = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
]


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
                if from_unit in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
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
    if from_type == "inches":
        if to_type == "inches":
            return from_value
        elif to_type == "feet":
            return from_value / 12
        elif to_type == "yards":
            return from_value / 36
        elif to_type == "miles":
            return from_value / 63360
        elif to_type == "millimeter":
            return from_value * 25.4
        elif to_type == "centimeter":
            return from_value * 2.54
        elif to_type == "kilometer":
            return from_value / 39370
        elif to_type == "meter":
            return from_value / 39.37
    elif from_type == "feet":
        if to_type == "inches":
            return from_value * 12
        elif to_type == "feet":
            return from_value
        elif to_type == "yards":
            return from_value / 3
        elif to_type == "miles":
            return from_value / 5280
        elif to_type == "millimeter":
            return from_value * 304.8
        elif to_type == "centimeter":
            return from_value * 30.48
        elif to_type == "kilometer":
            return from_value / 3281
        elif to_type == "meter":
            return from_value / 3.281
    elif from_type == "yards":
        if to_type == "inches":
            return from_value * 36
        elif to_type == "feet":
            return from_value * 3
        elif to_type == "yards":
            return from_value
        elif to_type == "miles":
            return from_value / 1760
        elif to_type == "millimeter":
            return from_value * 914.4
        elif to_type == "centimeter":
            return from_value * 91.44
        elif to_type == "kilometer":
            return from_value / 1094
        elif to_type == "meter":
            return from_value / 1.094
    elif from_type == "miles":
        if to_type == "inches":
            return from_value * 63360
        elif to_type == "feet":
            return from_value * 5280
        elif to_type == "yards":
            return from_value * 1760
        elif to_type == "miles":
            return from_value
        elif to_type == "millimeter":
            return from_value * 1.609e+6
        elif to_type == "centimeter":
            return from_value * 160900
        elif to_type == "kilometer":
            return from_value * 1.609
        elif to_type == "meter":
            return from_value * 1609
    elif from_type == "millimeter":
        if to_type == "inches":
            return from_value / 25.4
        elif to_type == "feet":
            return from_value / 304.8
        elif to_type == "yards":
            return from_value / 914.4
        elif to_type == "miles":
            return from_value / 1.609e+6
        elif to_type == "millimeter":
            return from_value
        elif to_type == "centimeter":
            return from_value / 10
        elif to_type == "kilometer":
            return from_value / 1e+6
        elif to_type == "meter":
            return from_value / 1000
    elif from_type == "centimeter":
        if to_type == "inches":
            return from_value / 2.54
        elif to_type == "feet":
            return from_value / 30.48
        elif to_type == "yards":
            return from_value / 91.44
        elif to_type == "miles":
            return from_value / 160900
        elif to_type == "millimeter":
            return from_value * 10
        elif to_type == "centimeter":
            return from_value
        elif to_type == "kilometer":
            return from_value / 100000
        elif to_type == "meter":
            return from_value / 100
    elif from_type == "kilometer":
        if to_type == "inches":
            return from_value * 39370
        elif to_type == "feet":
            return from_value * 3281
        elif to_type == "yards":
            return from_value * 1094
        elif to_type == "miles":
            return from_value / 1.609
        elif to_type == "millimeter":
            return from_value * 1e+6
        elif to_type == "centimeter":
            return from_value * 100000
        elif to_type == "kilometer":
            return from_value
        elif to_type == "meter":
            return from_value * 1000
    elif from_type == "meter":
        if to_type == "inches":
            return from_value * 39.37
        elif to_type == "feet":
            return from_value * 3.281
        elif to_type == "yards":
            return from_value * 1.094
        elif to_type == "miles":
            return from_value / 1609
        elif to_type == "millimeter":
            return from_value * 1000
        elif to_type == "centimeter":
            return from_value * 100
        elif to_type == "kilometer":
            return from_value / 1000
        elif to_type == "meter":
            return from_value


def convert_volume(from_type, to_type, from_value):
    if from_type == "fluid oz":
        if to_type == "fluid oz":
            return from_value
        elif to_type == "pint":
            return from_value / 16
        elif to_type == "gallon":
            return from_value / 128
        elif to_type == "table spoon":
            return from_value * 2
        elif to_type == "tea spoon":
            return from_value * 6
        elif to_type == "quart":
            return from_value / 32
        elif to_type == "cup":
            return from_value / 8
        elif to_type == "liter":
            return from_value / 33.814
        elif to_type == "milliliter":
            return from_value * 29.574

def convert_mass(from_type, to_type, from_value):
    ...

def convert_temp(from_type, to_type, from_value):
    ...
    
# double check scientific notation for negative numbers
def format_response(data: list):
    if data[2] % 1 == 0:
        initial_data = int(data[2])
    else:
        initial_data = data[2]

    if data[3] % 1 == 0:
        converted_data = int(data[3])
    elif data[3] > 10000000 or data[3] < 1e-6:
        converted_data = "{:.4e}".format(data[3])
    elif (data[3] - int(data[3])) > 0 and data[3] > 1e-6:
        converted_data = round(data[3], 4)
    else:
        converted_data = data[3]

    info = str(f"{initial_data} {abbreviations[data[0]]} = {converted_data} {abbreviations[data[1]]}")
    return info




if __name__ == "__main__":
    main()