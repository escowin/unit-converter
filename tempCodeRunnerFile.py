

        # Conditionally handles & displays data
        if unit.lower() == "g":
            converted = num / 28.35
            print(f"{num} {unit} = {converted} oz")
        else:
            converted = num * 28.35
            print(f"{num} {unit} = {converted} g")
    else: