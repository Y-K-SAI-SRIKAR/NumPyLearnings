# Date : 23-07-26
# Topics Covered : Linear Algebra.

import numpy as np

#Numpy has built in functions which makes solving Linear Algebra simple and used in scientific computing and ML applications.
#Matrix Multiplication: 
mat1 = np.array([[1,2,3],[4,5,6]])
mat2 = np.array([[9,8,7],[4,2,3]])
mat3 = np.array([[2,3],[4,7],[8,6]])
mat4 = np.array([[1,2],[4,5]])
mm1 = np.dot(mat1,mat3) 
mm3 = np.inner(mat1,mat2) # functions same as dot() method. but ensures a row order multiplication
mm4 = np.outer(mat1,mat4) # every element multiplied with other element
# performs scalar multiplication instead of vector multiplication, returns a expanded matrix product values.
# for outer() matrices need not be of same shape.
mm2 = mat1*mat2
print("Matrix A:",'\n',mat1,'\n')
print("Matrix B:",'\n',mat2,'\n')
print("Matrix C :",'\n',mat3,'\n')
print("Matrix D:",'\n',mat4,'\n')
print("Matrix Multiplication:",'\n',mm1,'\n') # performs matrix multiplication instead of element wise multiplication
print("Element wise multiplication in matrix:",'\n',mm2,'\n')
print("Matrix Multiplication:",'\n',mm3,'\n')
print("Matrix Multiplication:",'\n',mm4,'\n')
#Matrix Operations: For matrix operations the matrix must be a square matrix
#inverse of matrix :
inm = np.linalg.inv(mat4)
print("Inverse of Matrix:",'\n',inm,'\n')
#Determinent of Matrix:
dtr = np.linalg.det(mat4)
print("Determinent of Matrix D:",'\n',dtr,'\n')
#Determinent of Matrix using exponent method: using exponent method, handles the higher values and very lower values of matrix effectively by sign conversions.
sign, det = np.linalg.slogdet(mat4) 
res = sign*np.exp(det)
print("Determinent of Matrix D:",'\n',res,'\n')
#Eigne Values and Eigen Vectors of matrix:
egv, egV = np.linalg.eig(mat4)
print("Eigen Values of Matrix D:",'\n',egv,'\n')
print("Eigen Vectors of Matrix D:",'\n',egV,'\n')
#Transpose of matrix:
trn = mat1.T
print("Transpose of Matrix:",'\n',trn,'\n')

#Vectors Multiplication and Manipulation:
v1 = np.array([[1,2,3],[4,5,6]])
v4 = np.array([[5,6],[7,5],[5,8]])
v2 = np.array([1,2])
v3 = np.array([4,10])
vm1 = np.dot(v4,v2) # returns a scalar value by multiplying those vectors
vm2 = np.inner(v2,v3) # same as dot()
vm3 = np.outer(v1,v3) 
vm4 = np.cross(v1,v3)
print("Vector v1:",'\n',v1,'\n')
print("Vector v2:",'\n',v2,'\n')
print("Vector v3:",'\n',v3,'\n')
print("vector v4:",'\n',v4,'\n')
print("Dot product of vectors v4,v2:",'\n',vm1,'\n')
print("Inner product of vectors v2,v3:",'\n',vm2,'\n')
print("Outer product of vectors v1,v3:",'\n',vm3,'\n')
print("Cross product of vectors v1,v3:",'\n',vm4,'\n')
#working with real vector representations:
vec1 = 2-3j
vec2 = 4+6j
vd = np.dot(vec1,vec2)
vs = np.outer(vec1,vec2)
print("Vector dot Product:",'\n',vd,'\n')
print("vector scalar product:",'\n',vs,'\n')

#<<<<<<<< ------- completed  Day 04 ------- >>>>>>>> < Author : Srikar Yerraguntla > < 23-07-2026 @ 23:30 PM >