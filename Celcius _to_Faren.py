print('To convert CELSIUS to FAHRENHEIT press "1" \nTo convert FAHRENHEIT to CELSIUS press "2"')
num = input('Enter number for selection :')
val = input("Enter the value to be converted:")

if num == '1':
    num1 = (float(val)*9/5)+32
    print('CELSIUS to FAHRENHEIT is : ',num1)

elif num == '2':
    num1 = (float(val)-32)*5/9
    print('FAHRENHEIT to CELSIUS : ',num1)

else:
    print('Unkown Command!!!! /n Exiting!!!')
    exit()