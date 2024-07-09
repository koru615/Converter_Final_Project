# Basic Unit Converter
#### Video Demo:  [Basic Unit Converter Demo](https://youtu.be/4fvFLjTBCJs)

## Why a converter?
This is my submission for the final project of the CS50P course. It was my first introduction to Python and coding in general. Working through the course, I discovered a newfound passion for coding. I had been asking myself, "How had I not discovered this sooner?"

I did have trouble trying to choose a subject for my final project. However, after much deliberation, I finally decided on a unit converter. In my day job, I work at a wholesale gem and mineral company here in the United States. We import crystals from all over the world. Not only do many of the packages come to us with labels in different languages, but of course many of the items are labeled with weights and lengths using the metric system!

Because of this, I have become much more comfortable with different units of measurement like kilograms and centimeters. I decided I would use this as inspiration to make a conversion app. But little did I know how frustrating it would actually be.

## Issues with development
I thought this project would be simple. It was not. First, finding a comprehensive chart with each conversion seems like it would be simple. What I found was that most of the websites I visited would simply be converters themselves. It was actually difficult to find the formulas necessary for each conversion. For example, I was coding lines and lines of formulas using the decimals I was receiving from a converter online and didn't notice a crucial discrepancy.

When I went to test my program, I told the program to give me 1 foot back in inches. To my surprise, I got "11.9999904"! Looking back at the code, it was because instead of simply multiplying the value by 12 (the number of inches in a foot), I had ended up dividing by 0.08333334. This was because one of the converters I had used to get my conversion rates had simply given me the result of the fraction (1/12) which is 0.08333 repeating. I had been going too fast and not noticed something anyone who uses the imperial system would know and implement immediately. Just multiply by 12 to get the number of inches relative to the number of feet.

Because this converter had been giving me a decimal from a ratio of the relative measurements for each conversion, I was one step removed from my program actually doing the math itself. This was incredibly frustrating. What was more frustrating was that each of these websites seemed to either have imperial to metric or metric to imperial conversions for one unit on each page. Then, when I tried to find other conversions on the same page, they would be missing certain conversions (like carats).

## What's in a measurement anyway?
The focus of this program was to provide frequently used units of measurement a simple and easy to use conversion app. The measurements that I found on each website I visited were there in dizzying amounts. Light years, atomic mass units, nautical miles, micrograms... Which ones should I use in my app anyway?? It took quite a bit of deliberation to decide on which measurements to include to make the app feel complete.

There was another issue. Different apps were giving me different calculations on which formulas to use when converting between measurements. In the end, I decided to use the basic unit converter that Google has. It will show up if you type in something like "kilograms to pounds" in a Google search. But this was also confusing.

When converting between smaller and larger units of measurement in either the imperial or metric system, the numbers like to play nice. Inches go into feet which go into yards which go into miles. Of course, the metric system was invented for this very reason. Converting between these systems was not easy to find information for. 

Google provides the formulas for each conversion under their app. These are the conversion formulas I used. However, frequently when going from metric to imperial or vice versa, it would state that the formula would produce an "approximate" result. Doing the math yourself, you would find that your result would differ from the result the app on Google gives you! Which begs the question, why is the actual formula so hard to find?

Without getting too verbose here, I must inform you that I started to question measurement and how we use it in our world. What's in a measurement? Is the only thing that matters if we agree on what a measurement is? Why are the conversions between metric and imperial so approximate? Is converting between units just something we would like to think is simple (i.e. 4 quarts in a gallon), but in reality can never be achieved?

Decisions needed to be made and the app needed to be completed.

## Verbosity
Speaking of verbosity, looking at the code will reveal that each individual conversion is included in the code. For example, going to and from inches and feet are their own lines in their respective functions. This results in about 500 lines of code, all of which are unit conversions for each possible combination. Is there a better way?

One could postulate that going to and from meters would significantly reduce the amount of code used. Here is a simple example of a dictionary including each conversion to and from meters with a simple formula to achieve the conversions:

```
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
}

def convert_length(from_type, to_type, from_value):
    value_in_meters = from_value / conversion_factor["meter"][from_type]
    return value_in_meters * conversion_factor["meter"][to_type]

```

While this approach appears to be "cleaner" and more concise, it is in fact highly inaccurate. I desperately tried to make code like this work, but one would simply have to know what the answer SHOULD be, and try to get the code to comply. This produces lots of inaccuracies with the results, which as I've already stated, finding accurate conversion factors for each unit of measurement was already complicated enough. 

I also tried to create separate dictionaries for imperial and metric units, with a crossover dictionary if you were converting between the two. This also produced similar inaccuracies. The fact is, there is a separate conversion for each unit of measurement, and the simplest way to get the most accurate conversions was to simply brute force each conversion formula. 

I am also aware of the issues surrounding the "float" type when performing mathematics in code. The inaccuracies I was receiving while trying to use the dictionary conversion method were not in fact due to this issue. I attempted using the "Decimal" package included in Python to try and force the numbers to behave, but it simply wasn't their fault. The truth is each conversion needed its own formula, so that is how the program is coded. There are almost 500 lines of formulas in this program.

## Accuracy
In terms of accuracy, each individual formula has been tested in the [Unit Test](docs/test_conversion.py) I used to verify the accuracy of the project. I will admit, at least 2 different functions in my program were accidentally multiplying when they should have been dividing! But of course, each formula has been verified through testing, and I will stand behind the accuracy of the conversions.

The results given to the user are formatted for clarity. Numbers with decimal places are rounded to the millionth "0.0001", and numbers greater than one million "1000000" (positive or negative) are given to the user in scientific notation. If you prefer a higher clarity, you can adjust the precision in the `format_response()` function near the end of the program.

## User friendly
### Requirements
This application uses "tabulate".

`pip install tabulate`

It also uses the "sys" and "argparse" libraries which are included in Python.

### Usage
Running this app `python conversion.py` will produce a console app that is very user friendly. It will allow the user to continue converting until they decide they are done.

Running this app so many times during testing, I found the desire to implement a command line interface to quickly convert between units. This can be done two different ways.

## Using the command line
### The first method
This method is useful for converting a single measurement from one unit to another. If using this method, you must use these three arguments:

```
-x, --value
    >> the value (float) to be converted
-f, --from
    >> the unit you are converting from
-t, --to
    >> the unit you will be converting to
```

Here are a couple examples of using this method:

`python conversion.py -x 12 -f inch -t foot`

This will convert 12 inches to its value in feet.

`python conversion.py -x 1 -f gallon -t quart`

This will convert 1 gallon to its value in quarts.

`python conversion.py --value 32 --from fahrenheit --to celsius`

This will convert 32 degrees Fahrenheit to its value in Celsius.

The positions of each argument do not matter, but they must all three be included:

`python conversion.py -t pound -x 1 -f kilogram`

This will convert 1 kilogram into pounds.

When using the command line version, each unit should be singular, and if there is usually a space between the words for a unit, an underscore "_" must be used so that the program doesn't try to interpret the second word as an extra argument.

Here are the units that this program accepts via the command line:

```
length:
    "inch", "foot", "yard", "mile", "millimeter", "centimeter", "kilometer", "meter"

volume:
    "fluid_oz", "pint", "gallon", "table_spoon", "tea_spoon", "quart", "cup", "liter", "milliliter"

mass:
    "kilogram", "gram", "milligram", "metric_ton", "US_ton", "pound", "ounce", "carat"

temperature:
    "celsius", "kelvin", "fahrenheit"
```

Of course, each of these are listed if the `-h` function is used in the command line for users who need clarification on how to use the app. Also, the program will throw an error if measurements from different types of units are used. I.e. be sure to use "fluid_oz" instead of "ounce" if you are converting between volume units.

### The second method
This method of using the command line produces a list of each possible conversion for a given measurement. When using this method you must include:

```
-x, --value
    >> the value (float) to be converted
-f, --from
    >> the unit you are converting from
-a, --all
```

For example:

`python conversion.py -x 1 -f inch -a`

This will print each possible conversion from 1 inch to each other unit the program converts in length.

You need not supply an argument after `-a`, it will simply be marked as true and then print each possible conversion. Of course, using them in any order is acceptable as well:

`python conversion.py -a -f quart -x 15`

This will print each possible conversion from 15 quarts to each other unit the program converts in volume.

It must be noted that if the `--to` argument is given as well as the `--all` argument, the program will default to printing all of the possible conversions. Conversely, if you only provide the `--value` value to be converted and the `--from` unit you are starting with and do not provide either the `--to` or the `--all` argument, the program will produce an error.

## In conclusion
Of course, the frustration and difficulty in producing an accurate and coherent program was well worth the final result. I am very proud of this project and am so very grateful to David Malan and the team at Harvard who made this class possible.

I did my best to produce a practical conversion app for commonly used units we might find in our daily life. I would be thrilled if someone adopted this program for quick conversions in their day to day life.

This app could easily be expanded to many more conversion types. I would highly encourage and accept collaboration on this project.
