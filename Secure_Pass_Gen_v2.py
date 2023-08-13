import random

# Define character sets for password
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']

# Combine character sets and shuffle them
chars = lower + upper + num + special
random.shuffle(chars)

# Get the desired password length from the user
while True:
    password_length = input('How long would you like your password (min 12, max 50)? ') or random.randint(12, 50)
    while True:
        try:
            password_length = int(password_length)
            if password_length < 12 or password_length > 50:
                raise ValueError("Password length must be between 12 and 50")
            break
        except ValueError as e:
            print(e)
            password_length = input('How long would you like your password (min 12, max 50)? ')

    # Generate the password and print it
    password = ''.join(random.choice(chars) for _ in range(password_length))
    print(f"Your password is: {password}")
