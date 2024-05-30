# 3. Score
"""
function main
    get score
    grade = print_grade(score)

function print_grade(score)
    if score < 0 or score > 100
    print "Invalid score"
    elif score >= 50
        print "Passable"
    elif score >= 90
        print "Excellent"
    else
        print "Bad"
"""
def main():
    score = float(input("Enter score: "))
    grade = print_grade(score)

def print_grade(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Bad")

main()