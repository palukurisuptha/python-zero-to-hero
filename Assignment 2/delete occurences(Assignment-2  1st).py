l= list(map(int, input().split()))
#print(l)
c = int(input("Enter number to remove it's occurences:"))
res = [i for i in l if i != c]
print(res)