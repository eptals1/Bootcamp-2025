user_answer = input('Welcome to input checker! Do you wish to proceed? [y] or [n]: ')

def input_checker():
    user_selection = input("""What do you want to do?
    press [1] check if input is 'ALPHABET'
    press [2] check if input is 'NUMERIC'
    press [3] check if input is 'LOWERCASE'
    press [4] check if input is 'UPPERCASE'
    press [5] count inputted characters
    """)
    
    if user_selection == "1":
        user_input = input('Input characters to check: ')
        is_alpha = user_input.isalpha()
        if is_alpha is True:
            print("Yes! it's an alphabet")
        else:
            print("NOT ALPHABET")
    elif user_selection == "2":
        user_input = input('Input characters to check: ')
        is_numeric = user_input.isnumeric()
        if is_numeric is True:
            print("Yes! it's numeric")
        else:
            print("NOT NUMERIC")
    elif user_selection == "3":
        user_input = input('Input characters to check: ')
        is_lower = user_input.islower()
        if is_lower is True:
            print("Yes! it's lowercase")
        else:
            print("NOT LOWERCASE")
    elif user_selection == "4":
        user_input = input('Input characters to check: ')
        is_upper = user_input.isupper()
        if is_upper is True:
            print("Yes! it's uppercase")
        else:
            print("NOT UPPERCASE")
    elif user_selection == "5":
        user_input = input('Input characters to check: ')
        count = len(user_input)
        print(f"Number of characters: {count}")
    else:
        print("Invalid input")

while user_answer == "y":
    input_checker()