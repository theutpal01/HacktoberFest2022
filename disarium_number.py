def numOfDigits(num):
    numDigits = 0
    while num>0:
        num//=10
        numDigits+=1
    return numDigits

def is_Disarium_Number(num):
    digitCount = numOfDigits(num)
    sumOfTerms,copyNum = 0,num
    
    while num>0:
        rem = num%10
        sumOfTerms += int(rem**digitCount)
        digitCount-=1
        num//=10
    
    return sumOfTerms == copyNum

if __name__ in '__main__':
    n = int(input('Enter a Number: '))
    
    if is_Disarium_Number(n):
        print(f'{n} is a Disarium Number')
    else:
        print(f'{n} is NOT a Disarium Number')