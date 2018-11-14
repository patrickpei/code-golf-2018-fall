t = int(input())
for i in range(t):
    numbers = input().split(' ')
    k = int(input())
    print(sorted(set(numbers), key = lambda e:float(e))[-k])