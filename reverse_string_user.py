
# Author: Álvaro Masanori Sato

if(__name__ == "__main__"):
    user_input = input("Enter a string: ")
    reverse_input = user_input[::-1] # Using Slicing
    print(reverse_input)

    # Alternative forms
    # reverse_input = ''
    # for c in user_input:
    #     reverse_input = c + reverse_input
    # print(reverse_input)