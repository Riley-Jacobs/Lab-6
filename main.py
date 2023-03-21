# Riley Jacobs

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password


def main():
    encoded_password = None

    while True:
        menu()
        option = input("Please enter an input option: ")

        if option == "1":
            password = input("Pleas enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
                print("\n")
            else:
                print("Invalid input")
        elif option == "2":
            if encoded_password is not None:
                original_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
                print("\n")
            else:
                print("A password has not been encoded.")
                print("\n")
        elif option == "3":
            break
        else:
            print("Invalid option.")
            print("\n")


if __name__ == "__main__":
    main()

