"""
print colour codes
get colour name
while colour name != ""
    if colour name in colour codes
        print code
    else
        print invalid
    get colour name
"""
COLOUR_CODES = {"aliceblue": "#fof8ff", "amaranth": "#e52b50",
                "amber": "#ffbf00", "amethyst": "#9966cc",
                "antiquewhite": "#faebd7", "apricot": "#fbceb1",
                "aqua": "#00ffff", "asparagus": "#87a96b",
                "aureolin": "#fdee00", "beaver": "#9f8170"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(f"{colour_name}'s code is {COLOUR_CODES[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").lower()