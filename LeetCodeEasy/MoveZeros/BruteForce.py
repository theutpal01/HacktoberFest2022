def moveZeroBrute(nums):
    nonzerolist = []
    zerolist=[]
    for  i in nums:
        if i:
            nonzerolist.append(i)
        else:
            zerolist.append(0)
    print(nonzerolist)
    print(zerolist)
    nonzerolist+=zerolist
    print(nonzerolist)

moveZeroBrute([1,3,0,0,4,6,53,0,50,0,4,6,4])