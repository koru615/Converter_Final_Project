from conversion import *
from pytest import approx

def test_convert_length():
    #inches
    assert convert_length("inch", "inch", 30) == 30
    assert convert_length("inch", "foot", 12) == 1
    assert convert_length("inch", "yard", 45) == 1.25
    assert convert_length("inch", "mile", 2845) == approx(0.0449, abs=1e-4)
    assert convert_length("inch", "millimeter", 35) == 889
    assert convert_length("inch", "centimeter", 30) == approx(76.2, abs=1e-4)
    assert convert_length("inch", "kilometer", 25) == approx(0.0006, abs=1e-4)
    assert convert_length("inch", "meter", 85) == approx(2.159, abs=1e-4)

    #feet
    assert convert_length("foot", "inch", 30) == 360
    assert convert_length("foot", "foot", 12) == 12
    assert convert_length("foot", "yard", 18) == 6
    assert convert_length("foot", "mile", 200) == approx(0.0378, abs=1e-4)
    assert convert_length("foot", "millimeter", 0.5) == 152.4
    assert convert_length("foot", "centimeter", 0.5) == 15.24
    assert convert_length("foot", "kilometer", 38) == approx(0.0115, abs=1e-4)
    assert convert_length("foot", "meter", 1) == approx(0.3047, abs=1e-4)

    #yards
    assert convert_length("yard", "inch", 32) == 1152
    assert convert_length("yard", "foot", 25) == 75
    assert convert_length("yard", "yard", 18) == 18
    assert convert_length("yard", "mile", 456) == approx(0.2590, abs=1e-4)
    assert convert_length("yard", "millimeter", 0.5) == 457.2
    assert convert_length("yard", "centimeter", 0.5) == 45.72
    assert convert_length("yard", "kilometer", 38) == approx(0.0347, abs=1e-4)
    assert convert_length("yard", "meter", 1) == approx(0.9140, abs=1e-4)

    #miles
    assert convert_length("mile", "inch", 0.0687) == approx(4352.832, abs=1e-4)
    assert convert_length("mile", "foot", 101) == 533280
    assert convert_length("mile", "yard", 0.5) == 880
    assert convert_length("mile", "mile", 456) == 456
    assert convert_length("mile", "millimeter", 20) == 32180000
    assert convert_length("mile", "centimeter", 0.058) == approx(9332.2, abs=1e-4)
    assert convert_length("mile", "kilometer", 5) == approx(8.045, abs=1e-4)
    assert convert_length("mile", "meter", 13.64) == approx(21946.76, abs=1e-4)

    #millimeters
    assert convert_length("millimeter", "inch", 32) == approx(1.2598, abs=1e-4)
    assert convert_length("millimeter", "foot", 101) == approx(0.3313, abs=1e-4)
    assert convert_length("millimeter", "yard", 200) == approx(0.2187, abs=1e-4)
    assert convert_length("millimeter", "mile", 456) == approx(0.0002, abs=1e-4)
    assert convert_length("millimeter", "millimeter", 20) == 20
    assert convert_length("millimeter", "centimeter", 15) == 1.5
    assert convert_length("millimeter", "kilometer", 5) == 5e-6
    assert convert_length("millimeter", "meter", 45) == 0.045

    #centimeters
    assert convert_length("centimeter", "inch", 25) == approx(9.8425, abs=1e-4)
    assert convert_length("centimeter", "foot", 2001) == approx(65.6496, abs=1e-4)
    assert convert_length("centimeter", "yard", 35) == approx(0.3827, abs=1e-4)
    assert convert_length("centimeter", "mile", 45874) == approx(0.2851, abs=1e-4)
    assert convert_length("centimeter", "millimeter", 20) == 200
    assert convert_length("centimeter", "centimeter", 15) == 15
    assert convert_length("centimeter", "kilometer", 200) == 0.002
    assert convert_length("centimeter", "meter", 45) == 0.45

    #kilometers
    assert convert_length("kilometer", "inch", 0.006) == 236.22
    assert convert_length("kilometer", "foot", 0.8) == 2624.8
    assert convert_length("kilometer", "yard", 1) == 1094
    assert convert_length("kilometer", "mile", 14) == approx(8.70110, abs=1e-4)
    assert convert_length("kilometer", "millimeter", 0.008) == 8000
    assert convert_length("kilometer", "centimeter", 0.7) == 70000
    assert convert_length("kilometer", "kilometer", 200) == 200
    assert convert_length("kilometer", "meter", 45) == 45000

    #meters
    assert convert_length("meter", "inch", 1.54) == approx(60.6298, abs=1e-4)
    assert convert_length("meter", "foot", 0.8) == approx(2.6248, abs=1e-4)
    assert convert_length("meter", "yard", 1) == 1.094
    assert convert_length("meter", "mile", 300) == approx(0.1864, abs=1e-4)
    assert convert_length("meter", "millimeter", 0.008) == 8
    assert convert_length("meter", "centimeter", 0.7) == 70
    assert convert_length("meter", "kilometer", 200) == 0.2
    assert convert_length("meter", "meter", 45) == 45
    
def test_convert_volume():
    #fluid oz
    assert convert_volume("fluid oz", "fluid oz", 1) == 1
    assert convert_volume("fluid oz", "pint", 35) == 2.1875
    assert convert_volume("fluid oz", "gallon", 1) == approx(0.0078, abs=1e-4)
    assert convert_volume("fluid oz", "table spoon", 14) == 28
    assert convert_volume("fluid oz", "tea spoon", 10) == 60
    assert convert_volume("fluid oz", "quart", 55) == approx(1.7187, abs=1e-4)
    assert convert_volume("fluid oz", "cup", 20) == 2.5
    assert convert_volume("fluid oz", "liter", 5) == approx(0.1478, abs=1e-4)
    assert convert_volume("fluid oz", "milliliter", 0.056) == approx(1.6561, abs=1e-4)

    #pint
    assert convert_volume("pint", "fluid oz", 5) == 80
    assert convert_volume("pint", "pint", 35) == 35
    assert convert_volume("pint", "gallon", 48) == 6
    assert convert_volume("pint", "table spoon", 22) == 704
    assert convert_volume("pint", "tea spoon", 1.18) == 113.28
    assert convert_volume("pint", "quart", 14) == 7
    assert convert_volume("pint", "cup", 5) == 10
    assert convert_volume("pint", "liter", 5) == approx(2.3663, abs=1e-4)
    assert convert_volume("pint", "milliliter", 87) == approx(41168.4, abs=1e-4)
    
    #gallon
    assert convert_volume("gallon", "fluid oz", 4) == 512
    assert convert_volume("gallon", "pint", 1) == 8
    assert convert_volume("gallon", "gallon", 48) == 48
    assert convert_volume("gallon", "table spoon", 0.6) == 153.6
    assert convert_volume("gallon", "tea spoon", 1.5) == 1152
    assert convert_volume("gallon", "quart", 3) == 12
    assert convert_volume("gallon", "cup", 2) == 32
    assert convert_volume("gallon", "liter", 0.785) == approx(2.9712, abs=1e-4)
    assert convert_volume("gallon", "milliliter", 0.5) == approx(1892.5, abs=1e-4)

    #table spoon
    assert convert_volume("table spoon", "fluid oz", 4) == 2
    assert convert_volume("table spoon", "pint", 33) == approx(1.0312, abs=1e-4)
    assert convert_volume("table spoon", "gallon", 48) == 0.1875
    assert convert_volume("table spoon", "table spoon", 0.6) == 0.6
    assert convert_volume("table spoon", "tea spoon", 1.5) == 4.5
    assert convert_volume("table spoon", "quart", 3) ==  approx(0.0468, abs=1e-4)
    assert convert_volume("table spoon", "cup", 2) == 0.125
    assert convert_volume("table spoon", "liter", 0.785) == approx(0.0116, abs=1e-4)
    assert convert_volume("table spoon", "milliliter", 3) == approx(44.361, abs=1e-4)

    #tea spoon
    assert convert_volume("tea spoon", "fluid oz", 5) == approx(0.8333, abs=1e-4)
    assert convert_volume("tea spoon", "pint", 20) == approx(0.2083, abs=1e-4)
    assert convert_volume("tea spoon", "gallon", 3) == approx(0.0039, abs=1e-4)
    assert convert_volume("tea spoon", "table spoon", 15) == 5
    assert convert_volume("tea spoon", "tea spoon", 1.5) == 1.5
    assert convert_volume("tea spoon", "quart", 5) == approx(0.0260, abs=1e-4)
    assert convert_volume("tea spoon", "cup", 0.2) == approx(0.0041, abs=1e-4)
    assert convert_volume("tea spoon", "liter", 400) == approx(1.9714, abs=1e-4)
    assert convert_volume("tea spoon", "milliliter", 3) == 14.787

    #quart
    assert convert_volume("quart", "fluid oz", 4) == 128
    assert convert_volume("quart", "pint", 5) == 10
    assert convert_volume("quart", "gallon", 50) == 12.5 
    assert convert_volume("quart", "table spoon", 0.008) == 0.512
    assert convert_volume("quart", "tea spoon", 1.5) == 288
    assert convert_volume("quart", "quart", 5) == 5
    assert convert_volume("quart", "cup", 5.5) == 22
    assert convert_volume("quart", "liter", 1) == approx(0.9460, abs=1e-4)
    assert convert_volume("quart", "milliliter", 14) == approx(13249.6, abs=1e-4)

    #cup
    assert convert_volume("cup", "fluid oz", 3.6) == 28.8
    assert convert_volume("cup", "pint", 4) == 2
    assert convert_volume("cup", "gallon", 16) == 1
    assert convert_volume("cup", "table spoon", 2.5) == 40
    assert convert_volume("cup", "tea spoon", 44) == 2112
    assert convert_volume("cup", "quart", 2) == 0.5
    assert convert_volume("cup", "cup", 7) == 7
    assert convert_volume("cup", "liter", 1) == approx(0.2365, abs=1e-4)
    assert convert_volume("cup", "milliliter", 3.4) == approx(804.44, abs=1e-4)

    #liter
    assert convert_volume("liter", "fluid oz", 3.6) == approx(121.7304, abs=1e-4)
    assert convert_volume("liter", "pint", 4) == approx(8.452, abs=1e-4)
    assert convert_volume("liter", "gallon", 16) == approx(4.2272, abs=1e-4)
    assert convert_volume("liter", "table spoon", 2.5) == 169.07
    assert convert_volume("liter", "tea spoon", 44) == approx(8927.6, abs=1e-4)
    assert convert_volume("liter", "quart", 24) == approx(25.368, abs=1e-4)
    assert convert_volume("liter", "cup", 7) == approx(29.589, abs=1e-4)
    assert convert_volume("liter", "liter", 1) == 1
    assert convert_volume("liter", "milliliter", 3.4) == 3400

    #milliliter
    assert convert_volume("milliliter", "fluid oz", 20) == approx(0.6762, abs=1e-4)
    assert convert_volume("milliliter", "pint", 15) == approx(0.0316, abs=1e-4)
    assert convert_volume("milliliter", "gallon", 700) == approx(0.1849, abs=1e-4)
    assert convert_volume("milliliter", "table spoon", 2.5) == approx(0.1690, abs=1e-4)
    assert convert_volume("milliliter", "tea spoon", 33) == approx(6.6951, abs=1e-4)
    assert convert_volume("milliliter", "quart", 482) == approx(0.5092, abs=1e-4)
    assert convert_volume("milliliter", "cup", 65) == approx(0.2747, abs=1e-4)
    assert convert_volume("milliliter", "liter", 20) == 0.02
    assert convert_volume("milliliter", "milliliter", 3.4) == 3.4

def test_convert_mass():
    #kilogram
    assert convert_mass("kilogram", "kilogram", 30) == 30
    assert convert_mass("kilogram", "gram", 30) == 30000
    assert convert_mass("kilogram", "milligram", 30) == 30000000
    assert convert_mass("kilogram", "metric ton", 30) == 0.03
    assert convert_mass("kilogram", "US ton", 30) == approx(0.0330, abs=1e-4)
    assert convert_mass("kilogram", "pound", 30) == approx(66.15, abs=1e-4)
    assert convert_mass("kilogram", "ounce", 30) == 1058.22
    assert convert_mass("kilogram", "carat", 30) == 150000

    #gram
    assert convert_mass("gram", "kilogram", 30) == 0.03
    assert convert_mass("gram", "gram", 30) == 30
    assert convert_mass("gram", "milligram", 30) == 30000
    assert convert_mass("gram", "metric ton", 30) == 3e-5
    assert convert_mass("gram", "US ton", 30) == approx(3.3068e-5, abs=1e-4)
    assert convert_mass("gram", "pound", 30) == approx(0.0661, abs=1e-4)
    assert convert_mass("gram", "ounce", 30) == approx(1.0582, abs=1e-4)
    assert convert_mass("gram", "carat", 30) == 150

    #milligram
    assert convert_mass("milligram", "kilogram", 30) == 3e-5
    assert convert_mass("milligram", "gram", 30) == 0.03
    assert convert_mass("milligram", "milligram", 30) == 30
    assert convert_mass("milligram", "metric ton", 30) == 3e-8
    assert convert_mass("milligram", "US ton", 30) == approx(3.3068e-8, abs=1e-4)
    assert convert_mass("milligram", "pound", 30) == approx(6.6137e-5, abs=1e-4)
    assert convert_mass("milligram", "ounce", 30) == approx(0.0010, abs=1e-4)
    assert convert_mass("milligram", "carat", 30) == 0.15

    #metric ton
    assert convert_mass("metric ton", "kilogram", 30) == 30000
    assert convert_mass("metric ton", "gram", 30) == 3e+7
    assert convert_mass("metric ton", "milligram", 30) == 3e+10
    assert convert_mass("metric ton", "metric ton", 30) == 30
    assert convert_mass("metric ton", "US ton", 30) == approx(33.06, abs=1e-4)
    assert convert_mass("metric ton", "pound", 30) == approx(66150, abs=1e-4)
    assert convert_mass("metric ton", "ounce", 30) == approx(1058100, abs=1e-4)
    assert convert_mass("metric ton", "carat", 30) == 1.5e+8

    #US ton
    assert convert_mass("US ton", "kilogram", 30) == approx(27216, abs=1e-4)
    assert convert_mass("US ton", "gram", 30) == approx(27216000, abs=1e-4)
    assert convert_mass("US ton", "milligram", 30) == approx(27216000000, abs=1e-4)
    assert convert_mass("US ton", "metric ton", 30) == approx(27.2232, abs=1e-4)
    assert convert_mass("US ton", "US ton", 30) == 30
    assert convert_mass("US ton", "pound", 30) == 60000
    assert convert_mass("US ton", "ounce", 30) == 960000
    assert convert_mass("US ton", "carat", 30) == approx(1.3608e+8, abs=1e-4)

    #pound
    assert convert_mass("pound", "kilogram", 30) == approx(13.6054, abs=1e-4)
    assert convert_mass("pound", "gram", 30) == approx(13608, abs=1e-4)
    assert convert_mass("pound", "milligram", 30) == approx(13608000, abs=1e-4)
    assert convert_mass("pound", "metric ton", 30) == approx(0.0136, abs=1e-4)
    assert convert_mass("pound", "US ton", 30) == 0.015
    assert convert_mass("pound", "pound", 30) == 30
    assert convert_mass("pound", "ounce", 30) == 480
    assert convert_mass("pound", "carat", 30) == approx(68040, abs=1e-4)

    #ounce
    assert convert_mass("ounce", "kilogram", 30) == approx(0.8504, abs=1e-4)
    assert convert_mass("ounce", "gram", 30) == approx(850.5, abs=1e-4)
    assert convert_mass("ounce", "milligram", 30) == approx(850500, abs=1e-4)
    assert convert_mass("ounce", "metric ton", 30) == approx(8.5058e-4, abs=1e-4)
    assert convert_mass("ounce", "US ton", 30) == approx(0.0009, abs=1e-4)
    assert convert_mass("ounce", "pound", 30) == 1.875
    assert convert_mass("ounce", "ounce", 30) == 30
    assert convert_mass("ounce", "carat", 30) == approx(4251, abs=1e-4)

    #carat
    assert convert_mass("carat", "kilogram", 30) == approx(0.006, abs=1e-4)
    assert convert_mass("carat", "gram", 30) == 6
    assert convert_mass("carat", "milligram", 30) == 6000
    assert convert_mass("carat", "metric ton", 30) == 6e-6
    assert convert_mass("carat", "US ton", 30) == approx(6.6137e-6, abs=1e-4)
    assert convert_mass("carat", "pound", 30) == approx(0.0132, abs=1e-4)
    assert convert_mass("carat", "ounce", 30) == approx(0.2117, abs=1e-4)
    assert convert_mass("carat", "carat", 30) == 30

def test_convert_temp():
    #celsius
    assert convert_temp("celsius", "celsius", 25) == 25
    assert convert_temp("celsius", "kelvin", 25) == 298.15
    assert convert_temp("celsius", "farenheit", 25) == 77
    
    #kelvin
    assert convert_temp("kelvin", "celsius", 25) == approx(-248.15, abs=1e-4)
    assert convert_temp("kelvin", "kelvin", 25) == 25
    assert convert_temp("kelvin", "farenheit", 25) == approx(-414.67, abs=1e-4)
    
    #farenheit
    assert convert_temp("farenheit", "celsius", 25) == approx(-3.8888, abs=1e-4)
    assert convert_temp("farenheit", "kelvin", 25) == approx(269.261, abs=1e-3)
    assert convert_temp("farenheit", "farenheit", 25) == 25