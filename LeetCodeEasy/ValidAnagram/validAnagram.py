from typing import Counter


def V_A_method_string(s,t):
    return sorted(s)==sorted(t)

print(V_A_method_string("anagram","nagaram"))
print(V_A_method_string("cat","kat"))

def V_A_method_Counter_Obj(s,t):
    return Counter(s)==Counter(t)

print(V_A_method_Counter_Obj("anagram","nagaram"))
print(V_A_method_Counter_Obj("cat","kat"))

def isAnagram( s , t):
    if len(s) != len(t):
        return False
    counts={}
    countt={}
    for i in range(len(s)):
        counts[s[i]]=1+counts.get(s[i],0)
        countt[t[i]]=1+countt.get(t[i],0)
    for c in counts:
        if counts[c] != countt.get(c,0):
            return False
    
    return True


print("Is Anagram : ",isAnagram("cat","cat"))
    