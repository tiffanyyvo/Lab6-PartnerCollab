def encode(password):
    new_password = ""
    new_char = ""
    for i in password:
        if int(i) == 7:
            new_char = "0"
        elif int(i) == 8:
            new_char = "1"
        elif int(i) == 9:
            new_char = "2"
        else:
            new_char = str(int(i) + 3)
        new_password += new_char
    return new_password


# Anya Roselin
def decode(encoded_password):
    original_password = ""
    new_char = ""
    for i in encoded_password:
        if int(i) == 0:
            new_char = "7"
        elif int(i) == 1:
            new_char = "8"
        elif int(i) == 2:
            new_char = "9"
        else:
            new_char = str(int(i) - 3)
        original_password += new_char
    return original_password


def main():
    encoded_password = None
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
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            print()

        if option == "3":
            break


if __name__ == '__main__':
    main()
