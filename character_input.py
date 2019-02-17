# Exercise 1: character input

print("""
Hello and welcome to 100 Years in the Future!  You will
tell me your current age and I will tell you how old you'll be in
exactly 100 years.  Sound fun?  Let's give it a shot.
""")

user_name = input("""
                What is your name?
                """)
user_age = int(input("""
                How old are you?
                """))
number_of_copies = int(input("""
                How many copies of this would you like?
                """))
old_age = user_age + 100

# function to print the info
def print_info():
    print(f"""
                Name: {user_name}
                Age:  {user_age}

                You will be {old_age} in 100 years!
                """)


print_info()

#for loop to be able to print the info multiple times
for i in range (1, number_of_copies):
        print_info()
