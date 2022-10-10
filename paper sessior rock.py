



import random

count = 0
count_limit = 5
you = 0
PC = 0

def play():

      user = input("what is your choice ? 'r' for rock,'p' for paper, 's' for scissors \n")
      computer = random.choice(['r', 'p', 's'])


      if user == computer:
        print("tied the round")
        increment()

      if is_win(user, computer):
        print("you won the round")
        increment()
        user_WIN()

      elif is_win(computer, user):
        print("you lost the round")
        increment()
        PC_WIN()

def is_win(player, oponent):
    if(player == 'r' and oponent == 's') or (player == 's' and oponent == 'p') or (player == 'p' and oponent == 'r'):
        return True

def increment():
    global count
    count+=1

def PC_WIN():
    global PC
    PC +=1

def user_WIN():
    global you
    you += 1

def decision(x,y):
    if x > y :
        print("you won the game")
    elif x < y :
        print("you lost the game")


def run():
  while count < count_limit:
        print(play())
  else:
        print(decision(you, PC))


print(run())


