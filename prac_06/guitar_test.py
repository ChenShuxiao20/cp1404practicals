# Guitar Test
"""
Guitar Test
Estimate: 10 minutes
Actual:   15 minutes
"""
from prac_06.guitar import Guitar

def main():
    guitar= Guitar("Gibson L-5 CES", 1922, 16035.40)
    other = Guitar("Another Guitar", 2013, 1512.9)

    print(f"{guitar.name} get_age() - Expected {guitar.get_age()}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {other.get_age()}. Got: {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {guitar.is_vintage()}. Got: {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {other.is_vintage()}. Got: {other.is_vintage()}")

main()