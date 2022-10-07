from random import randint

def main():
  pos = ['rock', 'paper', 'scissors']
  
 s = int(input('Give a number (1) rock (2) paper (3) scissors (4) exit: '))
  
  while s != 4 and s in (1,2,3):
    pc = randint(0,2)
    
    if pos[s] == pos[pc]:
      print('Equals')
    elif (pos[s] == 'paper' and pos[pc] == 'rock') or (pos[s] == 'scissors' and pos[pc] == 'paper') or (pos[s] == 'rock' and pos[pc] == 'scissors'):
      print('User wins')
    else:
      print('PC wins')
    
    s = int(input('Give a number (1) rock (2) paper (3) scissors (4) exit: '))
    
print('End Game')
