"""A program to reverse a string using the function reverse."""
# Defining a function to reverse a given string.
def reverse(word):

    word = list(word) # First convert the string to a list
    word.reverse()

    return " ".join(word) # Using join function to combine the list to a string

reversed_word = reverse('Hacktober Fest') # Function calling
print(reversed_word) # Outputs the reversed word