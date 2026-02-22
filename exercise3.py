# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

user_name = input("Type your name: ")
name = user_name.count(" ")
if len(user_name) > 12:
    print("Your name must have less than 12 characters, Type your name again: ")
elif name > 0:
    print("Your name must not contain spaces")
elif user_name.isalpha() == False:
    print("Your name must not contain any digit")
else:
    print(f"Hello {user_name}")