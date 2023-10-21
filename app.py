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

def init(): 
    date = datetime.date.today()
    app = "unit-converter"
    print(f"""
        {app} 0.0.2
        \u00A9 {date.year} Edwin M. Escobar
        http://github.com/escowin/{app}
        """)
    convert_unit()

def convert_unit():
    # Terminal prompt variables
    weight = input("weight: ")
    unit = input("(g) or (oz): ")

    # Handles input data through conditional statements
    if unit.lower() == "g":
        # Converts var from string to float type to allow calculation
        converted = float(weight) / 28.35 
        print(f"{weight} {unit} = {converted} oz")
    else:
        converted = float(weight) * 28.35
        print(f"{weight} {unit} = {converted} g")
    prompt()

def prompt():
    # allows users to convert units again or exit the program
    answer = input("(c)onvert or (e)xit? ")
    if answer.lower() == "c":
        convert_unit()
    else:
        print("exiting program")
        return

init()