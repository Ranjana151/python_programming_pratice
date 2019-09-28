# Generate multi demsional_array
row_num=int(input("Enter the number of row"))
col_num=int(input("Enter the number of column"))
multi_array=[[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        multi_array[row][col]=int(input("Enter the number"))
print(multi_array)

