# Z pattern with var n

def z_pattern(n):
    for i in range(1, n+1):
        if i == 1 or i == n:
            print("* " * n)
        else:
            print("  "*(n-i) + "*")

if __name__ == "__main__":
    print("Printing sample pattern with n = 5")
    z_pattern(5)
else:
    print("This is not main module.")