# i = 0
# while i < 5:
#     print(i, end=" ")
#     i += 1
#     if i == 3:
#         break
#     else:
#         print(0)


# def func(x=1, y=2):
#     x = x + y
#     y += 1
#     print(x, y)


# func(y=9, x=91)


# i=12<89>90
# print(i)

# x=(~5)-4
# print(x)

# a=10
# a/=5!=5 and 6>=100>>2
# print(a)

# M = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
# print(len(M))
# print(M[1])

# N = M
# N[2] = 20  # for 2 index
# N[1][2] = 10  # fr index of 1 --> 2 element
# print(M)

# N=M[:]
# N[2] = 20
# print(M)

# P = [1, 2, 3, 4, 5]
# Q = P
# Q[2] = 10
# print(P)
# P = [1, 2, 3, 4, 5]
# Q = P[:]
# Q[2] = 10

# print(P)


# M=[[1,2,3],[4,5,6],[7,8,9]]
# N=M[:]
# N[2]=25
# print(M)
# print(N)
# N[1][0]=20
# print(M)


# A = [1, 2, [3, 4, 5], 6]
# # B = A[:]
# # B[2][0] = 10

# B = A[:]
# B[2][0] = 10

# print(A)
# print(B)


# X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Y = X.copy()
# Y[0][0] = 10
# Y[0] = 10

# print(X)
# print(Y)


# y = [20]
# y.append([3, 4, 5])
# print(y)

# y = [20]
# y.extend([3, 4, 5])  # make it one list only
# print(y)

# count=0
# for i in range(5):
#     for j in range(i):
#         count +=1
# print(count)

# X='ABCD'
# print(len(X))
# i=0
# while(i<len(X)):
#     Y=X[i]
#     i=i+2
# print(Y)


# a=[i for i in range(20) if(i%2==0)]
# print(a)
# name='snow strom'
# name[5]='X'
# print(name)


mylist = [3, 4, 9, 1, 2, 6, 8]
print(mylist[-6:4])
print(mylist[1:4])
print(mylist[-6:4] == mylist[1:4])

print(mylist[-5:4])
print(mylist[2:4])
print(mylist[-5:4] == mylist[2:4])

print(mylist[-1:3])
print(mylist[-1:4])
print(mylist[-1:3] == mylist[-1:4])


print(mylist[-4:4] == mylist[2:4])
print(mylist[-1:5] == mylist[-1:4])

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# result = numbers[2:7:2]

# print(result)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# result = numbers[-3:-8:-2]

# print(result)


# text = "Hello, World! How are you doing today?"

# result = text[::-1][::2]

# print(result)


A = [1, 10, 8, 7, 12, 14, 13, 18, 22]

i = 0

while i < len(A):
    if A[i] % 2 == 0:
        A.remove(A[i])

    else:
        i = i + 1

print(A)
