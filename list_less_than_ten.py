# exercise 3 - list less than ten

numbers = [1, 4, 7, 10, 3, 200, 3, 90, 69, 5, 2]
new_numbers = []

random_number = int(input("""
    Please enter a number greater than 0:
    """))

for num in numbers:
    if num < random_number:
        new_numbers.append(num)

print(new_numbers)
