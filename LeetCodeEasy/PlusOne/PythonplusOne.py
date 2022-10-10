from audioop import add


def plusOne(digits):
    a=1
    for i in range(len(digits)-1,-1,-1):
        # print(digits[i])
        if a==1 and digits[i]!=9:
            digits[i]=digits[i]+1
            a=0
            break
            # return digits
            
        else:
            digits[i]=0
            a=1
    if(a==1):
        digits.insert(0, 1)
    return digits
    
print(plusOne([9]))