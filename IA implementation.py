# Intelligent Agent (Vacum cleaner) implementation

import random
#0 --> clean room
#1--> dirty
def display(room):
    print(room)

room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
]
print("All the rooom are dirty")
display(room)

x =0
y= 0

while x < 4:
    while y < 4:
        room[x][y] = random.choice([0,1])
        y+=1
    x+=1
    y=0

print("Before cleaning the room we detect all of these random dirts")
display(room)
x =0
y= 0
while x < 4:
    while y < 4:
        if room[x][y] == 1:
            print("Vaccum in this location now,",x, y)
            room[x][y] = 0
            print("cleaned", x, y)
        y+=1
    x+=1
    y=0
display(room)
