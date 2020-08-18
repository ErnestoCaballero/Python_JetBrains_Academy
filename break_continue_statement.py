import string


# This function prints for every given char in a string if it is a vowel or a consonant
def vowel_consonant(text):
    vowels = 'aeiouAEIOU'

    for i in text:
        if i in vowels:
            print('vowel')
        elif i in string.ascii_letters:
            print('consonant')
        else:
            break


# This function creates a list of names until a '.' is given.
def list_of_names():
    list_names = []

    while True:
        name = input()
        if name != '.':
            list_names.append(name)
        else:
            break

    print(list_names)
    print(len(list_names))


# This Function ask for numbers and add them into a list if the conditions are correct and breaks
# when a number is greater than 100
def break_continue_ex():
    numbers = []
    while True:
        n = int(input())
        if n < 10:
            continue
        elif n > 100:
            break
        else:
            numbers.append(n)
    for i in numbers:
        print(i)


# This function reads integers until the sum equal zero and print the sum of the squares
def sum_squares_sumzero():
    list_numbers = []
    while True:
        list_numbers.append(int(input()))
        if sum(list_numbers) == 0:
            print(sum(i ** 2 for i in list_numbers))
            break


# This function prints if a given word is Palindrome.
def palindrome_1(word):
    bool_ = True
    for i in range(int(len(word) / 2)):
        if word[i] == word[-i - 1]:
            bool_ = True
        else:
            bool_ = False
    print("Palindrome" if bool_ else "Not palindrome")


# This function receives numbers in different lines and stores them in a list
# finally, print the arithmetic mean once a dot is written.
def arithmetic_mean():
    list_numbers = []
    while True:
        n = input()
        if n != '.':
            list_numbers.append(int(n))
        else:
            print(sum(list_numbers) / len(list_numbers))
            break


# This function determines if a given number is prime
def is_prime():
    n = int(input())
    bool_ = True
    if n <= 1:
        print("This number is not prime")
    else:
        for i in range(2, n):
            if n % i == 0:
                bool_ = False
                break
    print("This number is prime" if bool_ else "This number is not prime")


# A less efficient way but less lines of code to solve the problem.
def is_prime_2():
    div = []
    n = int(input())
    for i in range(2, n):
        div.append(n % i)
    print("This is prime" if n > 1 and 0 not in div else "This is not prime")


# This function receives a string with 'C' (correct) and 'I'(incorrect) with an space apart.
# If the I gets to three, a Game over is display
def score_game():
    scores = input()
    c_score = 0
    i_score = 0
    for i in scores:
        if i == "C":
            c_score += 1
        elif i == "I":
            i_score += 1
            if i_score == 3:
                break
        else:
            continue
    print(f"You won\n{c_score}" if i_score < 3 else f"Game over\n{c_score}")

# Important to remember the functions split and join in Python
# word = 'This is some string'
# my_list = ['some', 'list', 'item']
# print(word.split(' '))
# print("x".join(word.split(' ')))
# print("x".join(my_list))

# my_string = "hello,this,is,a,string"
# print(my_string.split(','))
# my_list_1 = my_string.split()
# for i in my_string.split(','):
#    print(i)

# print('_'.join(my_string.split(',')))
# word_1 = "paws 12".split()
# print(int(word_1[1]) + 1)
"""
word = input().split()
print(word)
if int(word[1]) > 1:
    print("Is int and greater than 1")"""

def max_cat_shop():
    max_cats = 0
    max_name = ""
    while True:
        kitty_cafe = input().split()
        print(kitty_cafe)
        if kitty_cafe[0].upper() == 'MEOW':
            break
        if int(kitty_cafe[1]) > max_cats:
            max_cats = int(kitty_cafe[1])
            max_name = kitty_cafe[0]
    print(max_name)


# This function receives float numbers and print the minimum once a '.' is entered
def min_float():
    float_list = []
    while True:
        number = input()
        if number == '.':
            break
        float_list.append(float(number))
    print(min(float_list))


