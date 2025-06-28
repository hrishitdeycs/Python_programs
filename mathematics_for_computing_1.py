#Find cofactor, determinant, adjoint and inverse of a matrix using numpy
#Taking Input of Matrix From user(User Define matrix Input)
#NR: Number of Rows
#NC: Number of Columns 
import numpy as np
NR=int(input("Enter the number of rows :"))
NC=int(input("Enter the number of columns :"))
print("Enter the entries in a single line(separated by space):")

#User input of entries in a
#single line separated by space
entries=list(map(int, input().split()))

#For printing the matrix
A=np.array(entries).reshape(NR,NC)
print("Matrix X is as follows:",'\n',A)

A_inverse=np.linalg.inv(A)
Transpose_of_A_Inverse=np.transpose(A_inverse)
Determinant_of_A=np.linalg.det(A)
Cofactor_of_A=np.dot(Transpose_of_A_Inverse,Determinant_of_A)

#For finding the cofactor of a Matrix
print("The Cofactor of a Matrix is:",'\n',Cofactor_of_A)

#For finding the determinant of a Matrix
print("The determinant of a Matrix is:",'\n',Determinant_of_A)

#For finding the Adjoint of a Matrix
Adjoint_of_A=np.transpose(Cofactor_of_A)
print("The Adjoint of a Matrix is:",'\n',Adjoint_of_A)

#For finding the inverse of a Matrix
print("The Inverse of a Matrix is:",'\n',A_inverse)                                 








