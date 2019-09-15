X=[[1,2],[3,4],[1,9]]
res=[[0,0,0],[0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        res[j][i]=X[i][j]

for r in res:
    print(r)