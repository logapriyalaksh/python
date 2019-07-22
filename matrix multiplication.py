X=[[1,2,3],
   
   [6,5,4],
   [7,8,9]]
Y=[[4,6,2],
   [8,4,6],
   [7,3,9]]
res=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range (len(X)):
     for j in range(len(Y[0])):
          for k in range(len(Y)):
                    res[i][j]+=X[i][k]*Y[k][j]
for r in res:
     print(r) 
