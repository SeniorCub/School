# my_string = "Hello"
# def exclamation(my_string):
#     my_string = "!!" + my_string + "!!"
#     return my_string
# exclamation(my_string)
# print(my_string)

import random


def generate_random_password():
    password_length = random.randint(7, 10)
    passord = ''.join(chr(random.randint(33, 126)) for _ in range(password_length))
    return passord


if __name__ == "_main_":
    random_password = generate_random_password()
    print("Generated Random Password:",
random_password)
