# 1. Password Star
"""
MINIMUM_LENGTH = 6
function main
    password = get_valid_password
    stars = print_asterisks

function get_valid_password
    get password
    while len(password) < MINIMUM_LENGTH:
        print "too short"
        get password
    return password

function print_asterisks
    print "*" * len(password)
"""
MINIMUM_LENGTH = 6

def main():
    password = get_valid_password()
    stars = print_asterisks(password)

def get_valid_password():
    password = input(f"Enter password is at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short")
        password = input(f"Enter password is at least {MINIMUM_LENGTH} characters: ")
    return password

def print_asterisks(password):
    print("*" * len(password))

main()