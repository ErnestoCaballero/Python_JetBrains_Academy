""""# test 01
print("Enter a String: ")
my_input = input()
print('The String is: ' + my_input)

# test 02
# En esta segunda prueba así se pide el input en la misma línea.
my_input = input("Escribe un String: ")
print("El string es: " + my_input)

# test 03: parsing
# La función input simpre recibe Strings.
my_int = int(input("Ingresa un número para multiplicarlo por 2: "))
print("El número, multiplicado por dos es:",my_int * 2)

# a = input()
# b = input()
# c = input()

my_list = [a, b, c]
print(my_list)
print(my_list[1])

print((3 + 5) // 2 * 2 ** 3)
print(((3 + 5) // 2 * 2 ** 3) % 7)
print()
print(1 or True)
print(100 and 200)
print()

a = True
b = True

print((a and not b) or (not a and b))
®
hour_1 = int(input())
minute_1 = int(input())
second_1 = int(input())
hour_2 = int(input())
minute_2 = int(input())
second_2 = int(input())

print(hour_2 * 3600 + minute_2 * 60 + second_2 - hour_1 * 3600 - minute_1 * 60 - second_1)
print((hour_2 - hour_1) * 3600 + (minute_2 - minute_1) * 60 + (second_2 - second_1))

my_input = int(input())
print(my_input % 10)

# HARD problem 1 of the section
group_1 = int(input())
min_desks_1 = group_1 // 2
desks_1_rem = group_1 % 2

group_2 = int(input())
min_desks_2 = group_2 // 2
desks_2_rem = group_2 % 2

group_3 = int(input())
min_desks_3 = group_3 // 2
desks_3_rem = group_3 % 2

min_desks = min_desks_1 + min_desks_2 + min_desks_3 + desks_1_rem + desks_2_rem + desks_3_rem

print(min_desks)

# Saving accounts
amount = 1000
interest_rate = 5
years = 1
# change the next line
income = amount * (1 + interest_rate / 100) ** years

print(income)

N = int(input())
K = int(input())
print(k // N)

# Good rest on vacation
days = int(input())
food_cost_daily = int(input())
flight_cost = int(input())
night_hotel_cost = int(input())

print(flight_cost * 2 + days * (food_cost_daily) + (days - 1) * night_hotel_cost)

# How many nuts will be left after division
N = int(input())
K = int(input())

print(14 % 3)

# The first digit of a two digit number
print(321 % 1000)
print(321 % 100)
print(321 % 10)
print()
print(True + 5)

# Another test
a = 5
b = -10
c = 15

calculated_result = a == b + c  # True
calculated_result_1 = a == b
print(calculated_result)
print(calculated_result_1 + c)

number_of_halls = int(input())
capacity = int(input())
number_of_viewers = int(input())

print(number_of_halls * capacity > number_of_viewers)"""
"""
# Other exercise
number = int(input())
word = input()

# write a condition for plurals
if number != 1:
    word = word + 's'

print(number, word)"""

"""

# Exercise with if statement
pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredient = input()

if ingredient in pasta:
    print("pasta time")
if ingredient in apple_pie:
    print("pasta time")
if ingredient in ratatouille:
    print("pasta time")
if ingredient in chocolate_cake:
    print("pasta time")
if ingredient in omelette:
    print("pasta time")"""

"""
# radio isotope excercise
N = int(input())
R = int(input())
counter = 0

while N > R:
    N /= 2
    counter += 1

print(counter * 12)"""

# Factoral
"""
integer_ = int(input())
result = 1

while integer_ > 1:
    result = result * integer_
    integer_ -= 1

print(result)"""

# Another exercise
k = int(input())
i = 1
acumulate_sum = 0

while i <= k:
    acumulate_sum += i
    i += 1

print(acumulate_sum)










