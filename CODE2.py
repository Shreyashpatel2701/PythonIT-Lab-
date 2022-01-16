arr=[]
n=int(input("Enter the number of rows in Matrix :\n"))
m=int(input("Enter the number of columns in Matrix :\n"))
print("Enter the elements")
for i in range(n):
    arr1=[]
    for j in range(m):
        k=int(input())
        arr1.append(k)
    arr.append(arr1)
print(arr)



flag=True
for i in range(n):
    for j in range(m):
        if i<m and j<n and arr[i][j]!=arr[j][i]:
            flag=False
            break
if flag==True:
    print("Matrix is symmetric")
else:
    print("Matrix is not symmetric")

flag=True
for i in range(n):
    for j in range(m):
        if arr[i][j]!=0 and arr[i][j]!=1:
            flag=False
            break

if flag==True:
    print("Matrix is binary")
else:
    print("Matrix is not binary")
