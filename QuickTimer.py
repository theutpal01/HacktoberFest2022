import time
def timer(t):
    while t>0:
        print(t,end=" ")
        t-=1
        time.sleep(0.5)
    print()    
    print("STOP")

print("Hello USER!!, How many seconds till countdown")
print("ENTER AN INTEGER value")
seconds= int(input())
timer(seconds)
#Here we have used the time module to count time and used while loop  with a gap of 0.5 sec as display gap between next sec on screen
