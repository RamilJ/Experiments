# Prompt the user for input
user_input = input("Enter a string: ")

# Use match case to check if the input string contains the letter 'a'
match user_input:
    case d if 'a' in d:
        print("The input string contains the letter 'a'.")
    case _:
        print("The input string does not contain the letter 'a'.")
