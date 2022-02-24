n = int(input())
dict_ = {}

for i in range(n):
    text = input().split()
    dict_[text[0]] = text[1]
    
while True:
    try:
       inp_ = input()
       if inp_ in dict_:
            print(inp_+"="+dict_[inp_])
       else:
            print("Not found")
    except EOFError:
        break
