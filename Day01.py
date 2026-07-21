# Date : 20-07-26
# Topics Covered : Numpy Basics :: Numpy arrays, Indexing, Slicing, Stacking, Reshaping & Resizing, Splitting.
# To install Numpy library, use the command in your terminal: "pip install numpy"

#import numpy library
import numpy as np

#Numpy arrays:
#1D arrays:
lst = [1,2,3,4,5] #Python list
print("Python list:",lst)

arr = np.array(lst)
print("Numpy array:",'\n',arr,'\n')

#Numpy arrays using arange() function: it automatically creates an array of elements specified withing the range.
arr1 = np.arange(1,10,2)
print("Numpy array using arange:",'\n',arr1,'\n')

#Numpy arrays using fromiter() function: creates a 1D array form the iterable
x="Srikar"
arr2 = np.fromiter(x,dtype='S10')
print("Numpy array using fromiter:",'\n',arr2,'\n')

#Numpy arrays using linspace() function: it creates array of elements within the specified limits evenly spaced.
arr3 = np.linspace(1,20,5,retstep=False,endpoint=True,dtype=np.int64)
print("Numpy array using linspace:",'\n',arr3,'\n')

#Numpy arrays using empty() function: it creates an array of uninitialized values
arr4 = np.empty((3,3),dtype=np.int64,order='C')
print("Empty array:",'\n',arr4,'\n')

#Numpy arrays using ones() function: creates an array filled with 1s
arr5 = np.ones((2,2))
print("Ones array:",'\n',arr5,'\n')

#Numpy arrays using zeros() function: creates an array filled with 0s
arr6 = np.zeros((2,2))
print("Zeroes array:",'\n',arr6,'\n')

#Numpy arrays using eye() function: creates an 2D Identical array
arr7 = np.eye(3,3)
print("Identical Matrix:",'\n',arr7,'\n')

#Numpy arrays using diag() fucntion: creates a 2D array consisting elements specified as diagonal elements
arr8 = np.diag([1,2,3])
print("Diagonal Matrix:",'\n',arr8,'\n')

#Numpy arrays using full() function: creates an array filled with specified value
arr9 = np.full((2,2),5)
print("Full array:",'\n',arr9,'\n')

#Numpy arrays using ones_like() function: creates a ones array with same shape of another array
arr10 = np.ones_like(arr1) # creates ones array like arr1
print("Ones Like array:",'\n',arr10,'\n')

#Numpy arrays using zeros_like() function: creates a zeros array with same shape of another array
arr11 = np.zeros_like(arr10)
print("Zeros Like array:",'\n',arr11,'\n')

#Numpy arrays using random values:
#Numpy arrays using Uniform Distribution Values
arr12 = np.random.rand(2,4)
print("Uniform Dist array:",'\n',arr12,'\n')

#Numpy arrays using Normal Distribution Values
arr13 = np.random.randn(2,4)
print("Normal Dist array:",'\n',arr13,'\n')

#Numpy arrays using Random Integers
arr14 = np.random.randint(1,10,(3,3))
print("Random Integers array:",'\n',arr14,'\n')

#2D arrays:
Arr1 = np.array([[1,2,3],[4,5,6]])
print("2D array:",'\n',Arr1,'\n')

#3D arrays:
Arr2 = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print("3D array:",'\n',Arr2,'\n')

#Indexing:
#Indexing in 1D arrays: uses syntax - arr[pos]
nar = np.arange(1,10,2)
print("array:",'\n',nar,'\n')
print("Indexed with 3:",'\n',nar[2])

#Indexing in 2D arrays: uses syntax - arr[row,col]
mat = np.array([[1,2,3,4],[5,6,7,8]])
print("2D array:",'\n',mat,'\n')
print("Indexed with 0th row 2nd col:",'\n',mat[0,1])

#Indexing in 3D arrays: uses syntax - arr[slice,row,col]
cube = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("3D array:",'\n',cube,'\n')
print("Indexed array with 2nd slice, 0th row, 2nd col:",'\n',cube[1,0,1])

#Boolean Indexing or conditional Indexing:
nar1 = np.arange(1,20,2)
condition = nar1>5
print("Conditioned Array:",'\n',nar1[condition],'\n')

#Positional Indexing:
positions = [1,5,6,8]
print("Positional Indexed array:",'\n',nar1[positions],'\n')

#Integer Indexing:
print("Integer based Indexed array:",'\n',nar1[[2,5]],'\n')

#Ellipsis Indexing: works only for 2 or higher Dimensional arrays
print("Ellipsis Indexed array:",'\n',mat[...,1],'\n')

#Slicing 
#Slicing in 1D arrays:
print("Sliced from 1st to 6th position:",'\n',nar1[:5],'\n')

#slicing in 2D arrays:
print("Sliced to 2nd row:",'\n',mat[1],'\n')
print("Sliced to all rows 2nd cols:",'\n',mat[:2,2],'\n')

#slicing in 3D arrays:
print("Sliced to 1st slice, all rows, 1st col:",'\n',cube[1,:,1],'\n')
print("Sliced to all slices , all rows , 3rd col:",'\n',cube[:,:,2],'\n')

#Reshaping: converting of arrays from a dimension to another , Temporary process
a1 = np.arange(1,6)
print("Shape of a1:",'\n',np.shape(a1),'\n')
print("Reshaped array:",'\n',a1.reshape(1,5),'\n') #converts 1D array to 2D array

a2 = np.array([[1,2,3,4,5]])
print("Shape of a2:",'\n',np.shape(a2),'\n')
print("Reshaped array:",'\n',a2.reshape(5,1),'\n') # converts into col major order

a3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("Shape of a3:",'\n',np.shape(a3),'\n')
print("Reshaped array:",'\n',a3.reshape(3,2,2),'\n') 

#Reshaping using -1 value: it lets numpy to calculate the unknown dimension and reshapes accordingly
#Note : The count of Elements in the Array must satisfy the product of dimensions in shape
a4 = np.array([[1,2,3,4,5,6]])
print("Actual a4 array:",'\n',np.shape(a4),'\n')
print("Reshaped array using -1:",'\n',a4.reshape(3,-1)) # calculates -1 and fixes with 2 

#Note : To rollback to the original shape from reshaped , use any of : .flattern() or .ravel() or simply use .reshape(-1)
print("Reshaped array:",'\n',a3.reshape(3,2,2),'\n') 
print("Rolled back to original shape of a3:",'\n',a3.reshape(-1),'\n')#using .reshape(-1)
print("Reshaped array:",'\n',a1.reshape(1,5),'\n')
print("Rolled back to original shape of a1:",'\n',a1.flatten(),'\n')#using .flatten()

# Resizing: permanently converting the dimensions of arrays
a5 = np.array([10, 20, 30, 40, 50, 60])
print("shape of a5:", '\n', np.shape(a5), '\n')
a5.resize((3, 2))
print("Resized array a5:", '\n', a5, '\n')
print("Shape of resized array a5:", '\n', np.shape(a5), '\n')

#new axis: converts the order of the array
a6 = np.arange(1,6)
print("Order changed array a6:",'\n',a6[:,np.newaxis],'\n')

#Stacking of arrays: stacking is combining of arrays without changing the data in arrays to higher dimension
#1D stacking: 
b1 = np.array([1,2,3,4,5])
b2 = np.array([6,7,8,9,10])
res1 = np.stack((b1,b2),axis=0)
res2 = np.stack((b1,b2),axis=1)
print("Stacked array with axis = 0:",'\n',res1,'\n') # converts to 2D array 
print("Stacked array with axis = 1",'\n',res2,'\n') # converts to 2D col major order , if axis = -1 result will be same as axis = 1

#2D stacking:
b3 = np.array([[1,2,3],[4,5,6]])
b4 = np.array([[10,20,30],[40,50,60]])
res3 = np.stack((b3,b4),axis = 0)
res4 = np.stack((b3,b4),axis = 1)
res5 = np.stack((b3,b4),axis=2)
print("2D Stacked array with axis = 0",'\n',res3,'\n') # converts into 3D plane
print("2D Stacked array with axis = 1",'\n',res4,'\n') # converts into 3D row major order
print("2D Stacked array with axis = 2",'\n',res5,'\n') # converst into 3D col major order

#3D stacking:
b5 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
b6 = np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,110,120]]])
res6 = np.stack((b5,b6),axis=0)
res7 = np.stack((b5,b6),axis=1)
res8 = np.stack((b5,b6),axis=2)
res9 = np.stack((b5,b6),axis=3)
print("3D Stacked with axis = 0",'\n',res6,'\n') # combines two 3D arrays to 4D plane
print("3D Stacked with axis = 1",'\n',res7,'\n') # combines those two 3D planes
print("3D Stacked with axis = 2",'\n',res8,'\n') # converts to row specific order
print("3D Stacked with axis = 3",'\n',res9,'\n') # comverts to col specific order

#Splitting: dividing the arrays into sub-arrays
npr=np.arange(1,11)
#using .split() method: allows only equal sub array division
ans = np.split(npr,2) # divides into two sub arrays - if not possible raises an error.
print("Splitted using split() method:",'\n',ans,'\n')

#using .array_split() method: allows unequal sub array division, elements will be automatically adjusted by Numpy
npr1= np.arange(1,10)
print("1D array before splitting:",'\n',npr1)
ans1 = np.array_split(npr1,4) # divides into 4 sub arrays
print("Splitted using array_split() method:",'\n',ans1,'\n')

#using .vsplit() method:: splits based upon the row order
npr2= np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("2D array before splitting:",'\n',npr2,'\n')
ans2= np.vsplit(npr2,2) # divides into 2 sub arrays based on rows
print("Splitted using vsplit() method:",'\n',ans2,'\n')

#using .hsplit() method: splits based on col order
ans3 = np.hsplit(npr2,3) # divides into 3 sub arrays
print("Splitted using hsplit() method:",'\n',ans3,'\n')

#using .dsplit() method : splits based on diagonal order
npr3=np.arange(24).reshape((2,3,4))
print("3D array before splitting:",'\n',npr3,'\n')
ans4 = np.dsplit(npr3,2) # splits into two sub arrays
print("Splitted using dsplit() method:",'\n',ans4,'\n')

#<<<<<<<< ------- completed  Day 01 ------- >>>>>>>> < Author : Srikar Yerraguntla > < 20-07-2026 @ 22:30 PM >