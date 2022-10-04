hexdecnum = input("Enter the Hexadecimal Number: ")

chk = 0
decnum = 0
hexdecnumlen = len(hexdecnum)
hexdecnumlen = hexdecnumlen-1
i = 0
while hexdecnumlen>=0:
    rem = hexdecnum[hexdecnumlen]
    if rem>='0' and rem<='9':
        rem = int(rem)
    elif rem>='A' and rem<='F':
        rem = ord(rem)
        rem = rem-55
    elif rem>='a' and rem<='f':
        rem = ord(rem)
        rem = rem-87
    else:
        chk = 1
        break
    decnum = decnum + (rem * (16 ** i))
    hexdecnumlen = hexdecnumlen-1
    i = i+1

if chk==0:
    i = 0
    octnum = []
    while decnum!=0:
        rem = decnum%8
        octnum.insert(i, rem)
        i = i+1
        decnum = int(decnum/8)

    print("Equivalent Octal Value is: ")
    i = i-1
    while i>=0:
        print(octnum[i], end="")
        i = i-1
    print()
else:
    print("\nInvalid Input!")