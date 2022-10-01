import calendar

print("Enter Year: ")
yy = input()
print("\nEnter Month Number (1-12): ")
mm = input()

y = int(yy)
m = int(mm)
print("\n", calendar.month(y, m))
