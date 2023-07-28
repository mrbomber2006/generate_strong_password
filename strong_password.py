from pathlib import Path
import random

file_name = input(
    "What is the name of the file you want to write your password to?: ")
number_of_characters = int(
    input("How many characters should your password have?: "))
password_file = Path(file_name + ".txt")

while True:
    password = "".join(random.choices(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=number_of_characters))
    password_file.write_text(password)
    checking = input(
        f"Please check the contents of ({file_name}.txt). If you don't like it, enter (n) to change it, or (y) to save it: ")
    if checking.lower() == "n":
        continue
    elif checking.lower() == "y":
        break
    else:
        print("Please enter y or n only.")
print("Your password is ready!")
