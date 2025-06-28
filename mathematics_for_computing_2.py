#Convert a matrix into echelon form and find its rank
#Using numpy

#Taking Input of Matrix From user(User Define matrix Input)
#NR: Number of Rows
#NC: Number of Columns 
import numpy as np
NR=int(input("Enter number of rows :"))
NC=int(input("Enter number of columns :"))

print("Enter the entries in a single line(separated by space):")

#User input of entries in a
#single line separated by space
entries=list(map(int, input().split()))

#For printing the matrix
matrix=np.array(entries).reshape(NR,NC)
print("Matrix X is as follows:",'\n',matrix)

#For finding the Rank of a Matrix
print("Rank of a Matrix is:",np.linalg.matrix_rank(matrix))
