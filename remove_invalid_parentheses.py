"""
    ### Back Tracking Problem 
    In this problem, an expression is specified that can
    contain opening and closing parentheses and optionally
    some characters. There are no other operators for strings.
    A minimum number of parentheses must be removed to make the
    input string valid. If multiple valid outputs are possible,
    remove the same number of brackets to print all of them.

    Below is the Python3 implementation of the above problem.
"""


#    'is_parenthesis' Method checks if character is parenthesis(open or closed)
def is_parenthesis(c):
    return (c == "(") or (c == ")")



#    'is_valid_string' method returns true if contains valid parenthesis
def is_valid_string(str):
    count = 0
    for i in range(len(str)):
        if str[i] == "(":
            count += 1
        elif str[i] == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0



#    'remove_invalid_parenthesis method to remove invalid parenthesis
def remove_invalid_parenthesis(str):
    if len(str) == 0:
        return

    # visit set to ignore already visited
    visit = set()

    # queue to maintain BFS
    q = []
    temp = 0
    level = 0

    # pushing given as starting node into queue
    q.append(str)
    visit.add(str)
    while len(q):
        str = q[0]
        q.pop()
        if is_valid_string(str):
            print(str)
            """
                If answer is found, make level true
                so that valid of only that level
                are processed.
            """
            level = True
        if level:
            continue
        for i in range(len(str)):
            if not is_parenthesis(str[i]):
                continue

            """
                Removing parenthesis from str and
                pushing into queue,if not visited already
            """
            temp = str[0:i] + str[i + 1 :]
            if temp not in visit:
                q.append(temp)
                visit.add(temp)


# Driver Code
statement = "((()()prathamwanmode(()()))"
remove_invalid_parenthesis(statement)
