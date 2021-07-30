l=list(map(int,input().split()))
ans = []
for _ in range(0,len(l)):
    ans.append(0)
#print(ans)
for i in range(len(l)):
    ans[l[i]-1] = i+1
    
print(ans)