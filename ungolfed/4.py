def subsets(names):
    subsets = []
    backtrack(subsets, [], names, 0)
    return subsets

def backtrack(subsets, temp, names, start):
    subsets.append(temp.copy())
    for i in range(start, len(names)):
        temp.append(names[i])
        backtrack(subsets, temp, names, i + 1)
        temp.pop()

def valid(subset):
    longest = max(list(map(len, subset)))
    for i in range(longest):
        letters = set()
        for name in subset:
            if i < len(name):
                if name[i] in letters:
                    return False
                else:
                    letters.add(name[i])
    return True

f = open('./inputs/4.txt')
names = []
for line in f:
    names.append(line.strip())

longest = 0
best = []
subsets = subsets(names)
for subset in subsets:
    if len(subset) > 0 and valid(subset) and len(subset) > longest:
        longest = len(subset)
        best = subset

print(best)
