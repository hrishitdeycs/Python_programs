#Solve a system of equations using the Gauss Jordan Method
#Using numpy

import numpy as np

#Coefficient Matrix (A) Elements
print("Enter dimension of coefficient matrix (A):-")
NR=int(input("Enter number of rows :"))
NC=int(input("Enter number of columns :"))
print("Enter the elements of coefficient matrix(A) in a single line(separated by space):")
Coefficients_Entries=list(map(float, input().split()))
Coefficient_Matrix=np.array(Coefficients_Entries).reshape(NR,NC)
print("Matrix A is as follows:",'\n',Coefficient_Matrix,'\n')

#Column Matrix (B) Elements
print("Enter the elements of column matrix(B) in a single line(separated by space):")
Column_Entries=list(map(float, input().split()))
Column_Matrix=np.array(Column_Entries).reshape(NR,1)
print("Column Matrix B is as follows:",'\n',Column_Matrix,'\n')

#Solution of Homogeneous System of Equations using GAUSS JORDAN 
Inv_of_Coefficient_matrix=np.linalg.inv(Coefficient_Matrix)
Solution_of_the_system_of_Equations=np.matmul(Inv_of_Coefficient_matrix,Column_Matrix)
print("Solution of the system of Equations using GAUSS JORDAN method")
print(Solution_of_the_system_of_Equations)                                                          
