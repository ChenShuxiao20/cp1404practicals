# 2. Temperatures
"""
function main
    get MENU
    get choice
    while choice != "Q"
        if choice == "C"
            get celsius
            fahrenheit = celsius_to_fahrenheit(celsius)
            print fahrenheit
        elif choice == "F"
            get fahrenheit
            celsius = fahrenheit_to_celsius(fahrenheit)
            print celsius
        else
            print "Invalid option"
        print MENU
        get choice
    print "Thank you."

fuunction celsius_to_fahrenheit(celsius)
    return celsius * 9 / 5 + 32

function fahrenheit_to_celsius(fahrenheit)
    return 5 / 9 * (fahrenheit - 32)
"""
MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)

main()