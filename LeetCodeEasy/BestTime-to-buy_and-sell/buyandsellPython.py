
import math

# Brute force solution
def maxprofBruteF (prices):
    maxprofit = 0 
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            profit = prices[j]-prices[i]
            if(profit>maxprofit):
                maxprofit=profit
    return maxprofit
print(maxprofBruteF([7,1,5,3,6,4]))




def maxProfit(prices):
    minprice=float('inf')
    maxprofit=0
    for i in range(len(prices)):
        minprice=min(minprice,prices[i])
        maxprofit=max(maxprofit,prices[i]-minprice)
    return maxprofit
print(maxProfit([7,1,5,3,6,4]))


        