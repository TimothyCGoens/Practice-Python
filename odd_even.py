# exercise 2 - odd/even

print("""
    Hello and welcome to Odd or Even!  This is the game where you give
    us a number and we tell you if it's odd or even!
    """)

number = int(input("""
    Please give us a number.
    """))

if number % 2 == 0:
    print("""
    EVEN!
    """)
    if number % 4 == 0:
        print("""
    This number is also divisible by 4!
    """)
else:
    print("""
    ODD!
    """)
