from decimal import *


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

abbreviations = {
    "inches":"in", "feet":"ft", "yards":"yd", "miles":"mi", "millimeter":"mm", "centimeter":"cm", "kilometer":"km", "meter":"m",
    "fluid oz":"fl oz", "pint":"pt", "gallon":"gal", "table spoon":"tbsp", "tea spoon":"tsp", "quart":"qt", "cup":"cup", "liter":"L", "milliliter":"mL",
    "kilogram":"kg", "gram":"g", "milligram":"mg", "metric ton":"t", "US ton":"t (US)", "pounds":"lbs", "ounces":"oz", "carat":"ct",
    "celsius":"°C", "kelvin":"K", "farenheit":"°F",
}

def main():
    from_type = input("From: ")
    to_type = input("To: ")
    from_value = input("Value: ")
    converted_data = convert_length(from_type, to_type, from_value)
    package_data = [from_type, to_type, from_value, converted_data]
    final_equation = format_response(package_data)
    print(final_equation)


def convert_length(from_type, to_type, from_value):
    from_value = float(from_value)
    value_in_meters = from_value / conversion_factor["meter"][from_type]
    new_value = Decimal(value_in_meters * conversion_factor["meter"][to_type]).quantize(Decimal(".001"))
    return float(new_value)


def format_response(data: list):
    info = str(f"{data[2]} {abbreviations[data[0]]} = {data[3]} {abbreviations[data[1]]}")
    return info

if __name__ == "__main__":
    main()