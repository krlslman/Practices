# Exceptions - String to Integer
S = input().strip()
try:
    x = int(S)
    print(x)
except ValueError:
    print("Bad String")
