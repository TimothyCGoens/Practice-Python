# exercize 4 - divisors

numbers = []

for i in range(1, 101):
    numbers.append(i)

random_number = int(input("""
    Please select any number between 1-100:
    """))

for num in numbers:
    if random_number % num == 0:
        print(num)
