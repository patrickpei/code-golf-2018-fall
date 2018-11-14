for i in range(1, 34):
    first = int(str(i)[:1])
    last = i % 10
    divisble = any([i % j == 0 for j in [3, 5, 7]])
    # if first == last and (i % 3 == 0 or i % 5 == 0 or i % 7 == 0):
    if first == last and any([i % j == 0 for j in [3, 5, 7]]):
        print(i)
