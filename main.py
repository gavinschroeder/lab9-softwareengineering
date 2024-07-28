def encode(password):
    encoded_password = ''.join(str((int(digit) + 3) % 10) for digit in password)
    return encoded_password

def decode(password):
    decoded_password = "".join(str((int(digit)- 3) % 10) for digit in password)
    return decoded_password

def main():
    encoded_password = None

    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("\nPlease enter an option: ")

        if option == "1":
            password = input("Please enter the password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == "2":
            if encoded_password is None:
                print("No encoded password to decode.")
            else:
                original_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")

        elif option == '3':
            # Quit
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please enter a valid option (1, 2, or 3).")

        if __name__ == "__main__":
            main()
