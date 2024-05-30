# 3. Score
"""
function main
    score = get_a_valid_score()
    grade = print_grade(score)

function get_a_valid_score()
    get score
    while score < 0 or score > 100
        print "Invalid score"
        get score
    return score

function print_grade(score)
    if score >= 50
        print "Passable"
    elif score >= 90
        print "Excellent"
    else
        print "Bad"
"""
def main():
    score = get_a_valid_score()
    grade = print_grade(score)

def get_a_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def print_grade(score):
    if score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Bad")

main()