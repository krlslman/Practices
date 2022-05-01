
# return_day, return_month, return_year = [int(e) for e in input().strip().split(' ')]
# due_day, due_month, due_year = [int(e) for e in input().strip().split(' ')]

# if return_year < due_year:
#     print(0)
# elif return_year == due_year:
#     #check month
#     if return_month < due_month:
#         print(0)
#     elif return_month == due_month:
#         #check day
#         if return_day <= due_day:
#             print(0)
#         else:
#             print(15*(return_day - due_day))    
#     else:
#         print(500*(return_month - due_month))
# else:
#     print(10000*(return_year - due_year))

n = input()
x = list(map(int, n.split()))
m = input()
y = list(map(int, m.split()))
z=0
if y[2] < x[2]:
    z = 10000
elif y[2] == x[2]:
    if y[1] < x[1]:
        z = 500*(x[1]-y[1])
    elif y[0] < x[0]:
        z = 15*(x[0]-y[0])

print(z)
