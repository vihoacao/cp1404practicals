COLORS_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                  "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00",
                  "Chocolate": "#d2691e", "Dartmouth Green": "#00703c", "Deep Peach": "#ffcba4",
                  "Iceberg": "#71a6d2"}
print(COLORS_TO_CODE)


color_name = input("Enter a color name: ").title()
while color_name != "":
    if color_name in COLORS_TO_CODE:
        print(f"{color_name} is {COLORS_TO_CODE[color_name]}")
    else:
        print("Invalid color name")
    color_name = input("Enter a color name: ").title()

for color_name, color_code in COLORS_TO_CODE.items():
    print(f"{color_name} is {color_code}")

while True:
    color_name = input("Enter a color name: ")
    if not color_name:
        break
    try:
        color_code = COLORS_TO_CODE[color_name.title()]
        print(f"{color_name.title()} is {color_code}")
    except KeyError:
        print("Invalid color name")
