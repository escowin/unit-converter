# SEQUENCE
# 1. Import relevant libraries
# 2. Greet user with init message
# 3. Prompt user to enter weight & unit
# 4. Convert 'weight' variable from string to float type to calculate number
# 5. Display result in terminal
# 6. Prompt user to repeat or exit the program

# IF-THEN-ELSE:
# - Conditionally check user input to carry out unit conversion
# - Conditionally check user input to determine whether app should repeat or exit

import datetime

app = "unit-converter"


def init():
    date = datetime.date.today()
    print(f"""
    {app} 0.0.2
    \u00A9 {date.year} Edwin M. Escobar
    http: //github.com/escowin/{app}\n""")
    select_measurement_type()


def select_measurement_type():
    # Prompts user to select type of measurement
    measurement_type = input("""
    :: MEASUREMENT SELECTION ::
    (l)ength (m)ass (v)olume 
    enter: """)
    convert_unit(measurement_type.upper())


def convert_unit(type):
    # Converts units based, grouped by type of measurement

    print(f"""\n    :: {type} OPTIONS :: """)  # prints single char, but should print word
    # Variables defined by user input
    if type == "M":
        unit = input("    (g) or (oz): ")
        num = float(input("    amount: "))

        # Conditionally handles & displays data
        if unit.lower() == "g":
            converted = num / 28.35
            print(f"\n    {num} {unit} = {converted} oz")
        else:
            converted = num * 28.35
            print(f"\n    {num} {unit} = {converted} g")
    else:
        print(f"\n    invalid type: {type}")
    prompt(type)


def prompt(measurement_unit):
    # allows users to convert units again or exit the program
    answer = input("\n    (c)onvert again, s(witch) units, or (e)xit? ")
    if answer.lower() == "c":
        convert_unit(measurement_unit)
    elif answer.lower() == "s":
        select_measurement_type()
    else:
        print(f"\n    :: exiting {app} :: ")
        return


init()
