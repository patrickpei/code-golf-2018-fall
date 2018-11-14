i=input
t=int(i())
for _ in range(t):n,k=i().split(' '),int(i());print(sorted(set(n),key=lambda e:float(e))[-k])