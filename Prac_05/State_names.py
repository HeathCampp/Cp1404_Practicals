
HEX_COLOURS = {"aquamarine": "#7fffd4", "blue": "#0000ff", "green": "#00ff00", "dark violet": "#9400d3",
               "brown": "#a52a2a", "dark orchid": "#9932cc", "dim gray": "#696969", "firebrick": "#b22222",
               "azure4": "#838b8b", "black": "#000000"}

colour = input("Enter colour: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(HEX_COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")