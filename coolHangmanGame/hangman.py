########################################################################
#               IMPORT AND SOME TECHNICAL STUFF
########################################################################
import random
import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))
########################################################################
#               PRINTING THE CURRENT STATUS OF THE GUESSING
########################################################################
def CurrentStatus(word,hint):
    wrd=""
    for w in word:
        if(w in hint):
            wrd+=w+" "
        else:
            wrd+="_ "
    return wrd
########################################################################
#                       HANGMAN ANIMATION
########################################################################
def hangStatus(status): 
    try:
        comment=open("comments.txt",'r').read().splitlines()
    except FileNotFoundException:
        print(f"couldn't finnd comments.txt, download and place in to the pwd. i.e. {os.getcwd()}")
    comment=comment[random.randint( 0 , (len(comment) -1) )]
    if(status==0):
        print(f""" 
                  ---------
                      |
                      |
            """)
    elif(status==1):
        print(f""" 
                  ---------
                      |
                    __|__
                    |o o|
                    |_-_|
                    
            """)
    elif(status==2):
        print(f""" 
                  ---------
                      |
                    __|__  {comment}
                    |o o|
                    |_-_|
                      | 
                      |
                      |
            """)
    elif(status==3):
        print(f""" 
                  ---------
                      |
                    __|__   {comment} 
                    |o o|
                    |_-_|
                      |
                     /| 
                    / |
            """)
    elif(status==4):
        print(f""" 
                  ---------
                      |
                    __|__   {comment}  
                    |o o|
                    |_-_|
                      |
                     /|\ 
                    / | \ 
        """)
    elif(status==5):
        print(f"""
                  ---------
                      |
                    __|__   {comment} 
                    |o o| 
                    |_-_| 
                      | 
                     /|\ 
                    / | \ 
                     / 
                 ___/_______ 
        """)
    elif(status==6):
        print(f""" 
                  --------- 
                      | 
                    __|__   {comment} 
                    |o o| 
                    |_-_| 
                      | 
                     /|\ 
                    / | \ 
                     / \ 
                 ___/___\_____ 
        """)
    elif(status==7):
        print(f"""
                   ---------
                      |
                    __|__  Guess I'll Die ¯\_(ツ)_/¯ 
                    |X X|
                    |_~_|
                      | 
                     /|\ 
                    / | \ 
                     / \ 
                    /   \ 
        """)
    elif(status==8):
        print(f"""
                   ---------
                      |
                      !
                    _____  i'm saved, thanks
                    |o‿o| 
                    |___| 
                    \ | / 
                     \|/ 
                      |  
                     / \ 
                 ___/___\_____ 
        """)
########################################################################
#                           THE MAIN CODE
########################################################################
wordlist=open("./hangmanWordlist.txt",'r').readlines()
while(True):
    Hstatus=0
    hint=[]
    chosenWord = wordlist[random.randint( 0, (len(wordlist)-1) )]
    chosenWord=chosenWord[0:-1]
    #print(chosenWord)
    hint.append(chosenWord [ random.randint( 0 , len (chosenWord) -1 ) ] )
    resp='n'
    while(True):
        wrd=CurrentStatus(chosenWord,hint)
        #print(wrd.replace(" ","")+":"+chosenWord)
        if(wrd.replace(" ","")==chosenWord):
            Hstatus=8
            hangStatus(Hstatus)
            resp=input(f"Word Is: {chosenWord} play again?(y/n): ")[0]
            break
        elif(Hstatus==7):
            print("\n\tGame Over!!")
            hangStatus(Hstatus)
            resp=input(f"Word Is: {chosenWord} try again?(y/n): ")[0]
            break
        else:
            print("Guess The word:- "+wrd ,end=" ")
            hangStatus(Hstatus)
            while(True):        
                guess=input("enter an alphabet to guess :")
                if(guess not in hint):
                    break
                else:
                    print("tried already.")
            hint.append(guess)
            if(guess in chosenWord):
                print("Correct")
                continue
            else:
                print("Wrong")
                Hstatus+=1
                
    if(resp=='n'):
        break
            

    
