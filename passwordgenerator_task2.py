import random
import math

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

def get_password_length():
    while True:
        try:
            pass_len = int(input("Enter Password Length: "))
            if pass_len > 0:
                return pass_len
            else:
                print("Please enter a positive integer for password length.")
        except ValueError:
            print("Please enter a valid integer for password length.")

def generate_password(length, array, is_alpha=False):
    password = [random.choice(array) for _ in range(length)]
    if is_alpha:
        password = [random.choice([char.lower(), char.upper()]) for char in password]
    return ''.join(password)

def main():
    pass_len = get_password_length()

    alpha_len = pass_len // 2
    num_len = math.ceil(pass_len * 30 / 100)
    special_len = pass_len - (alpha_len + num_len)

    alpha_password = generate_password(alpha_len, alpha, True)
    num_password = generate_password(num_len, num)
    special_password = generate_password(special_len, special)

    final_password = ''.join(random.sample(alpha_password + num_password + special_password, pass_len))
    
    print(final_password)

if __name__ == "__main__":
    main()

