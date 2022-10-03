# Binary to Octal Converter
# This program lets you convert a binary number to an octal number
# Created by Amey Karan

binNum = str(input("Enter the binary number: "))
if len(binNum) % 3 == 1:
    binNum = "00" + binNum
elif len(binNum) % 3 == 2:
    binNum = "0" + binNum

result = ""
for i in range(0, len(binNum), 3):
    bit = binNum[i:i + 3]

    if bit == "000":
        result += "0"
    if bit == "001":
        result += "1"
    if bit == "010":
        result += "2"
    if bit == "011":
        result += "3"
    if bit == "100":
        result += "4"
    if bit == "101":
        result += "5"
    if bit == "110":
        result += "6"
    if bit == "111":
        result += "7"

print(result.lstrip("0"))
