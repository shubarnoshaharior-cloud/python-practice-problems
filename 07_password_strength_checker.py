password = input("Enter password: ")

has_digit = any(char.isdigit() for char in password)

if len(password) >= 10 and has_digit:
    print("Strong Password")
else:
    print("Weak Password")