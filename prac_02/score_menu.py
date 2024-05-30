# 4. Score Menu
"""
function main
    get score
    get MENU
    get choice
    while choice != "Q"
        if choice == "G"
            get_a_valid_score()
        elif choice == "P"
            print_grade(score)
        elif choice == "S"
            print_star(score)
        else
            print "Invalid choice"
        get MENU)
        get choice
    print "Farewell"

function get_a_valid_score()
    get score
    while score < 0 or score > 100:
        print "Invalid score"
        get score
    return score

function print_grade(score)
    if score < 0 or score > 100
    print "Invalid score"
    elif score >= 50
        print "Passable"
    elif score >= 90
        print "Excellent"
    else
        print "Bad"

function print_star(score)
    print '*' * score
"""
MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""

def main():
    score = get_a_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            get_a_valid_score()
        elif choice == "P":
            print_grade(score)
        elif choice == "S":
            print_star(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")

def get_a_valid_score():
    score = int(input("Enter score 0-100: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score 0-100: "))
    return score

def print_grade(score):
    if score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Bad")

def print_star(score):
    print('*' * score)

main()