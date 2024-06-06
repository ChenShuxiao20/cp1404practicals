# Files
# 1.
out_file = open("name.txt", "w")
name = input("What's your name? ")
print("name", file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name1 = in_file.read()
in_file.close()
print(f"Hi {name1} !")

# 3.
input_file = open("numbers.txt", "r")
number1 = int(input_file.readline())
number2 = int(input_file.readline())
input_file.close()
print(number1 + number2)

# 4.
input_file = open("numbers.txt", "r")
total = 0
for line in input_file:
    total += int(line)
input_file.close()
print(total)