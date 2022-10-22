def alphabet(l):
    vowel = 'a e i o u'
    consonant = 'b c d f g h j k l m n p q r s t v x z y w' 
    if l.lower() in vowel :
        return "Vowel"
    elif l.lower() in consonant:
        return "Consonant"

    if l in ('0 1 2 3 4 5 6 7 8 9'):
        return "Number"
    else:
        return "Symbol"
    
def  main():
    l = input(" ")

    print(alphabet(l))

if __name__== "__main__":
    main()