import random

items = ['Rock', 'Paper', 'Scissors']
score = 10
highscore = 0
print("""Welcome to Rock, Paper, Scissors. You're starting score is 1, you lose when it reaches 0, and hints cost 1. Try to get as high a score as possible before you lose.""")

while score > 0:    
    humanItem = input('(r)ock, (p)aper, (s)cissors, (h)int, or (e)xit? ')
    robotItem = items[random.randrange(3)]
    outcome = ''
    hintedItems = ['Rock', 'Paper', 'Scissors']
    
    if humanItem == 'e':
        break
    elif humanItem == 'r':
        if robotItem == 'Rock':
            outcome = 'Tie'
        elif robotItem == 'Paper':
            outcome = 'You Lose'
        elif robotItem == 'Scissors':
            outcome = 'You Win'
    elif humanItem == 'p':
        if robotItem == 'Paper':
            outcome = 'Tie'
        elif robotItem == 'Scissors':
            outcome = 'You Lose'
        elif robotItem == 'Rock':
            outcome = 'You Win'
    elif humanItem == 's':
        if robotItem == 'Scissors':
            outcome = 'Tie'
        elif robotItem == 'Rock':
            outcome = 'You Lose'
        elif robotItem == 'Paper':
            outcome = 'You Win'
    elif humanItem == 'h':
        score += -1
        print('1 removed from score.')
        hintedItems.remove(robotItem)
        print(f"The robot is not choosing... {hintedItems[random.randrange(2)]}.")
        humanItem = input('(r)ock, (p)aper, or (s)cissors? ')
        if humanItem == 'r':
            if robotItem == 'Rock':
                outcome = 'Tie'
            elif robotItem == 'Paper':
                outcome = 'You Lose'
            elif robotItem == 'Scissors':
                outcome = 'You Win'
        elif humanItem == 'p':
            if robotItem == 'Paper':
                outcome = 'Tie'
            elif robotItem == 'Scissors':
                outcome = 'You Lose'
            elif robotItem == 'Rock':
                outcome = 'You Win'
        elif humanItem == 's':
            if robotItem == 'Scissors':
                outcome = 'Tie'
            elif robotItem == 'Rock':
                outcome = 'You Lose'
            elif robotItem == 'Paper':
                outcome = 'You Win'
        else:
            print('You have wasted your hint by using an invalid command. Pay more attention next time.')
            continue
        
    else:
        print('Use a valid command.')
        continue

    if outcome == 'You Win':
        score += 2
    elif outcome == 'You Lose':
        score+= -2
    elif outcome == 'Tie':
        score = score
        
    if score > highscore:
        highscore = score
        
    print(outcome)
    print(f"Your score is {score}")
print(f'Your highscore was {highscore}')
