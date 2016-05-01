import re
'''A simple program that checks if any 3 integers (sides) form a Pythagorean triangle'''

def user_input():
    numbers = (input("Length of the triangle's sides: ").strip())
    numbers = re.sub('\s+', ' ', numbers).strip()
    if "," in numbers:
        return (numbers.replace(",","").split(" "))
    else:
        return numbers.split(" ")

def calc(numbers):
    num_list = sorted([int(n) for n in numbers if int(n) >= 0])
    try:
        a, b, c = num_list[0], num_list[1], num_list[2]
    except IndexError:
        return ("The triangle should have three sides with lengths > 0.")
    if (c**2 == a**2 + b**2):
        return ("Yes")
    else:
        return ("No")

def main():
    print("Pythagorean Triangles Checker. Is this triangle Pythagorean?")
    while True:
        print(calc(user_input()))

if __name__ == '__main__': main()
