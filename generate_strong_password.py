from pathlib import Path
import random
import string

file_name = input("What is the name of the file you want to write your password to?: ")
number_of_characters = int(input("How many characters should your password have?: "))
password_file = Path(f"{file_name}.txt")

contents = input("What kind of password would you like?\n1. Only numbers\n2. Any type of letters\n3. Only lowercase\n4. Only uppercase\n")
Type = string.digits
while True:
    if contents == "1":
        break

    if contents != "1":
        have_number = input("1. With number\n2. Without number\n")

        if contents == "2":
            if have_number == "1":
                Type += string.ascii_letters 
                break
            else:
                Type = string.ascii_letters
                break
        elif contents == "3":
            if have_number == "1":
                Type += string.ascii_lowercase
                break
            else:
                Type = string.ascii_lowercase
                break
        elif contents == "4":
            if have_number == "1":
                Type += string.ascii_uppercase
                break
            else:
                Type = string.ascii_uppercase
                break
        if contents not in ["1", "2", "3", "4"] or have_number not in ["1", "2"]:
            print("Please enter only 1, 2, 3, or 4.")

while True:
    password = "".join(random.choices(Type, k=number_of_characters))
    password_file.write_text(password)
    checking = input(f"Please check the contents of ({file_name}.txt). If you don't like it, enter (n) to generate it again, or (y) to save it: ")
    if checking.lower() == "n":
        continue
    elif checking.lower() == "y":
        break
    else:
        print("Please enter only y or n.")
print("Your password is ready!")