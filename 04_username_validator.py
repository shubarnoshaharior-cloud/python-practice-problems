username = input("Enter username: ")

if username.isalpha() and len(username) >= 10:
    print("Valid username")
else:
    print("Invalid username")