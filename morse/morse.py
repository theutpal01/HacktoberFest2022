#morse code letters
morse = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",
    "...-", ".--", "-..-", "-.--", "--.."
]
#english alphabet letters
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
##  A function which converts morsecode into english letters.
def decoding(text):
    decoding_text = ""
    for i in text:
        if i in morse:
            position = morse.index(i)
            decoding_text += alphabet[position]
        else:
            decoding_text += i
    print(f"\n here is your message: {decoding_text}")

## A function to encode text into morsecode.
def encoding(text):
    encoding_text = ""
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            encoding_text += morse[position]
        else:
            encoding_text += i
    print(f"\n here is your morsecode: {encoding_text}")

is_game = True
while is_game:
    type = input("type 'en' for encoding or 'de' decoding?")
    if type == "en":
        text_input = input("enter the text letter by letter: ")
        encoding(text_input)
    elif type == "de":
        text_input = input("enter the text: ").split()
        decoding(text_input)
    continue1 = input("do you want to continue?").lower()
    if continue1 == "yes":
        is_game = True
    else:
        is_game = False

