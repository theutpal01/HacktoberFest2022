import re
# For EMail
pattern = re.compile(r"(^[a-zA-Z0-9_,+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-,]+$)")
# For Password
pattern2 = re.compile(r"[A-Za-z0-9$%@]{8,}\d")

string = 'b@b.com'
# password should be any string of 8 number and endes with number  
password = "hejdodd485$8@57"

a = pattern.search(string)
check = pattern2.fullmatch(password)
print(a)
print(check)
