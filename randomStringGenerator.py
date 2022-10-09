import secrets
import string
N = int(input("Enter Desired length of string"))
S = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation)
              for i in range(N))
print("The random string generated is"+str(S))
