print("Enter a decimal Number:")

dec_num = input()
try:
    print("The Number %s  is in hex : %s" %(int(dec_num), hex(int(dec_num))))
except:
    print("No valid input")