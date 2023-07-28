a = int(input())
k = int(input())
n = 0
lists=[] 
for i in range(a):
    lists.append(int(input()))
for ball in lists:
    if ball>k:
        n+=1
    else:
        continue
print(n)