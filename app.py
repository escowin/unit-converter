import datetime

date = datetime.date.today()
app = "unit-converter"
print(f"""
      {app} 0.0.1 
      \u00A9 {date.year} Edwin M. Escobar
      http://github.com/escowin/{app}
      """)

weight = input("weight: ")
unit = input("(g) or (oz): ")

print(weight + " " + unit)