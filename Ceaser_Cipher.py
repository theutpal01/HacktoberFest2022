# for encryption
message=input("Enter your message")
message1=message.upper()
result=""
key=input("Enter key")
key1=int(key)
Alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in message1:
    position=Alphabets.index(i)
    newpos=(key1+position)%26
    result+=Alphabets[newpos]
print(result)

# for decryption
dmessage=result
dresult=""
key2=input("Enter key")
key3=int(key2)
Alphabets1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in dmessage:
    position1=Alphabets1.index(i)
    newpos1=(position1-key3)%26
    dresult+=Alphabets1[newpos1]
print(dresult)
