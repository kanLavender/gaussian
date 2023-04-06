#获取输入数据:
matrix = []
while True:
    try:
        row = list(map(int, input().split())) #行
        matrix.append(row)
    except:
        break
n = len(matrix) #输出矩阵的行数
m = len(matrix[0]) #输出矩阵的列数
#转置矩阵
transpose_matrix = []
for j in range(m):
    col = [] #列
    for i in range(n):
        col.append(matrix[i][j])
    transpose_matrix.append(col)
#输出转置矩阵
    for i in range(m):
        for j in range(n):
          print(transpose_matrix[i][j],end = " ")
        print()