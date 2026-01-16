x=121
d=0
g=0
while (x>0):
    d=x%10
    x=int(x/10)
    g+=d
    g*=10

print(int(g/10))


