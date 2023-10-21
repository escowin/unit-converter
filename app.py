# SEQUENCE
# 1. Import relevant libraries
# 2. Greet user with init message
# 3. Prompt user to enter weight & unit
# 4. Check if the input is valid
# 5. Handle invalid input
# 6. Perform the conversion
# 7. Display the converted value

import datetime

# Init message variables
date = datetime.date.today()
app = "unit-converter"
print(f"""
      {app} 0.0.1 
      \u00A9 {date.year} Edwin M. Escobar
      http://github.com/escowin/{app}
      """)

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
