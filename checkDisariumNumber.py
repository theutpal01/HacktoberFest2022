# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def buildComplementaryNumber(val):
    complementaryNumber, curr = 0, 1
    for each in str(val):
        complementaryNumber += int(each) ** curr
        curr += 1
    return complementaryNumber

def checkDisariumNumber(val):
    return val == buildComplementaryNumber(val)


if __name__ == '__main__':
    # print_hi('PyCharm')
    val = int(input())
    print("The provided number Disariumity is :{}".format(checkDisariumNumber(val)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
