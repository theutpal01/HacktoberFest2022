print('To convert CELCIUS to FARENHEIT press "1" \nTo convert FARENHEIT to CELCIUS press "2"')
num = input('Enter number for selection :')
val = input("Enter the vslue to be converted:")

if num == '1':
    num1 = (float(val)*9/5)+32
    print('CELCIUS to FARENHEIT is : ',num1)

elif num == '2':
    num1 = (float(val)-32)*5/9
    print('FARENHEIT to CELCIUS : ',num1)

else:
    print('Unkown Command!!!! /n Exiting!!!')
    exit()