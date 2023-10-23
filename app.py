# SEQUENCE
# 1. Import relevant libraries
# 2. Set up global scope variables and functions
# 3. Greet user with init message
# 4. Prompt user to select type of measurement
# 5. Prompt user to select unit of measurement
# 6. Prompt user to specify quantity amount
# 7. Calculate & display converted value
# 8. Prompt user to repeat, switch or exit the program

# IF-THEN-ELSE:
# - Conditionally check user input to carry out application options.

import datetime

# Global scope variables
app = "unit-converter"
calculate = {
    "measurement": ("(l)ength", "(m)ass", "(v)olume"),
    "length": ("(cm)", "(in)"),
    "mass": ("(g)", "(oz)"),
    "volume": ("(l)itre", "(g)allon"),
    "menu": ("(1) calculate new amount", "(2) switch units", "(3) switch measurement", "(0) exit")
}


def generate_prompt(option):
    # Dynamically generates user prompt
    prompt = f"\n: : {option.upper()} SELECTION : : \n"
    for choice in calculate[option]:
        prompt += f"\n{choice}"
    prompt += "\n\nenter selection: "
    return prompt


def init():
    # Initial start up message
    date = datetime.date.today()
    print(f"""
    {app} 0.0.2
    \u00A9 {date.year} Edwin M. Escobar
    https://github.com/escowin/{app}""")
    # Prompts user to select a unit of measurement
    select_measurement("measurement")


def select_measurement(param):
    # To-do:
    # - Iterate through each prompt level (measurement > unit > amount > menu options) to coalesce functions
    # - Increment 'calculate' to dynamically determine conditional statement

    # Displays a prompt to capture user input
    prompt = generate_prompt(param)
    selected_measurement = input(prompt)

    # Invalid user input reprompts the user
    if selected_measurement != "l" and selected_measurement != "m" and selected_measurement != "v":
        print(f"invalid measurement: {selected_measurement}")
        select_measurement(param)

    # Valid user input progresses user to the next prompt
    select_unit(selected_measurement.lower())


def select_unit(measurement):
    # Displays corresponding prompt

    print(measurement)
    measurement = measurement + "string"
    print(measurement)
    # if measurement == "l":
    #     prompt = generate_prompt("length")
    # elif measurement == "m":
    #     prompt = generate_prompt("mass")
    # elif measurement == "v":
    #     prompt = generate_prompt("volume")
    # else:
    #     # invalid input sends user to previous prompt
    #     print(f"\ninvalid measurement: {measurement}")
    #     select_measurement()

    # selected_unit = input(prompt)
    # convert_unit(selected_unit.lower(), measurement)


def convert_unit(unit, type):
    # Captures & type converts user data
    num = float(input("enter amount: "))

    # Conditionally calculates & displays data
    if unit == "g":
        converted = num / 28.35
        print(f"\n{num} {unit} = {converted} oz")
    elif unit == "oz":
        converted = num * 28.35
        print(f"\n{num} {unit} = {converted} g")
    else:
        print(f"\nformula not yet implemented for unit: {unit}")
    display_menu(unit, type)


def display_menu(unit, type):
    # Displays prompt to dynamically capture user data
    prompt = generate_prompt("menu")
    selected_option = input(prompt)

    # Conditionally handles user selection
    if selected_option == "1":
        convert_unit(unit, type)
    elif selected_option == "2":
        select_unit(type)
    elif selected_option == "3":
        select_measurement()
    else:
        print(f"\n: : exiting {app} : : ")
        return


init()
