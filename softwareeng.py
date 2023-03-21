#encode a string of 8 numbers to a new encoded password
def encoder(password):

    encoded_password = ""
    for digit in password:
        # Shift the digit up by 3 numbers
        shifted_digit = str((int(digit) + 3) % 10)
        encoded_password += shifted_digit
    return encoded_password

def main():
    #Menu
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        choice = int(input("Please enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded = encoder(password)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            print(f"The encoded password is {encoded}, and the original password is {password}.") 
        elif choice == 3:
            break

