N = int(input())
counter = [0 for x in range(101)]
for i in range(N):
    x = int(input())
    counter[x] += 1

for x in range(100, -1, -1):
    for i in range(counter[x]):
        print(x)
