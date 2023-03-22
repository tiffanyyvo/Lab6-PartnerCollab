def encode(password):
    new_password = ""
    for i in password:

        new_char = str(int(i) + 3)
        new_password += new_char
    return new_password


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()

        if option == "2":
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")
            print()

        if option == "3":
            break

if __name__ == '__main__':
    main()