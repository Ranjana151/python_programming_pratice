#Addition of matrixes
A=[[1,2,3],[2,7,8],[9,8,7]]
B=[[5,6,7],[1,0,9],[1,2,3]]
for i  in range(len(A)):
    for j in range(len(A[0])):
        print(A[i][j] + B[i][j],end=" ")
    print("")