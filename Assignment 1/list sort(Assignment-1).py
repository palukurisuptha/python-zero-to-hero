l= list(map(int, input().split()))
i = 0
while(i < len(l)):
    j = i + 1
    while(j < len(l)):
        if(l[i] < l[j]):
            t = l[i]
            l[i] = l[j]
            l[j] = t
        j = j + 1
    i = i + 1

print(l)