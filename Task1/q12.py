N = int(input("Enter the value of N:"))

print("Rhombus pattern:")
for i in range(1,N+1,1):
    space = N-i
    star = 2*i-1
    print(' '*space+'*'*star)
for j in range(N,0,-1):
    space1 = N-j
    star1 = 2*j-1
    print(' '*space1+'*'*star1)

print("Butterfly pattern:")
for i in range(1, N+1):
    print('*'*i+' '*(2*(N-i))+'*'*i)
for i in range(N, 0, -1):
    print('*'*i+' '*(2*(N-i))+'*'*i)
