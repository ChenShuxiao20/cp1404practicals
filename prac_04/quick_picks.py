# 6. Quick Pick" Lottery Ticket Generator
"""
import random

"""
import random
MIN = 1
MAX = 45
PICK_COUNT = 6

def main():
    num_quick = int(input("How many quick picks? "))
    quick_picks_number = generate_picks(num_quick)

def generate_picks(num_quick):
    for i in range(num_quick):
        quick_picks =[]
        for j in range(PICK_COUNT):
            number = random.randint(MIN, MAX)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))

main()