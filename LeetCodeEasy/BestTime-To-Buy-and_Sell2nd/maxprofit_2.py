def maxprofit(prices):
    prev =0 
    next =1 
    mprofit = 0
    while next<len(prices):
        if(prices[next]>prices[prev]):
            mprofit+=prices[next]-prices[prev]
        prev+=1
        next+=1
    return mprofit
print(maxprofit([7,1,5,6,3,4]))