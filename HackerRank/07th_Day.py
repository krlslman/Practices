#given
n = int(input().strip())  # 4

arr =  list(map(int, input().rstrip().split())) #[1,2,3,4]

# Method 1
for i in reversed(arr):
	print(i, end=' ')
  
# Method 2
#print (*arr[::-1], sep=' ')
