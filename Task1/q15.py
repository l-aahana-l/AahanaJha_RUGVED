N = int(input("Enter the dimension of the matrix: "))
print("Enter elements of the matrix:")
matrix = []
for i in range(N):          
    a =[]
    for j in range(N):
         a.append(int(input()))
    matrix.append(a)
def rotateClockwise(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for i in range(n):
        mat[i].reverse()

def print_spiral(mat):
    n = len(mat)
    spiral = []
    top, bottom, left, right = 0, n-1, 0, n-1
    while top <= bottom and left <= right:
        for i in range(left, right+1):
            spiral.append(mat[top][i])
        top += 1
        for i in range(top, bottom+1):
            spiral.append(mat[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, -1):
                spiral.append(mat[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                spiral.append(mat[i][left])
            left += 1
        print("Spiral Order:", spiral)

rotateClockwise(matrix)
print("Matrix after 90° rotation:")
for row in matrix:
    print(' '.join(map(str, row)))

print_spiral(matrix)
