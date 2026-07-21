# Date : 21-07-26
# Topics Covered : Numpy Broadcasting, Copy & View, join, Sorting, Stack Functions.

import numpy as np

#Numpy Join : joining is nothing but merging of arrays
#1D join: using concatenate() method
arr = np.arange(1,6)
arr1 = np.arange(6,11)
res = np.concatenate((arr,arr1))
print("Array 1:",'\n',arr,'\n')
print("Array 2:",'\n',arr1,'\n')
print("concatented Array:",'\n',res,'\n')

#2D join: using concatenate() method
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.array([[7,8,9],[10,11,12]])
res1 = np.concatenate((arr2,arr3),axis=0) # implements row order joining
res2 = np.concatenate((arr2,arr3),axis=1) # implements col order joining
print("2D array 1:",'\n',arr2,'\n')
print("2D array 2:",'\n',arr3,'\n')
print("Row order Join:",'\n',res1,'\n')
print("Col order join:",'\n',res2,'\n')

#Stacking functions:
#using vstack() method: stacks based on col order
#1D arrays:
ans = np.vstack((arr,arr1))
print("1D Stacked arrays using vstack():",'\n',ans,'\n')

#2D arrays:
ans1 = np.vstack((arr2,arr3))
print("2D stacked arrays using vstack():",'\n',ans1,'\n')

#using hstack() method: stacks based on row order
#1D arrays
ans2 = np.hstack((arr,arr1))
print("1D stacked arrays using hstack():",'\n',ans2,'\n')

#2D arrays
ans3=np.hstack((arr2,arr3))
print("2D stacked arrays using hstack():",'\n',ans3,'\n')

#using dstack() method: stacks based on height or 3rd dimension, converts any lower order array to 3D array
ans4 = np.dstack((arr,arr1))
ans5 = np.dstack((arr2,arr3))
print("1D stacked array using dsplit():",'\n',ans4,'\n')
print("2D stacked array using dstack():",'\n',ans5,'\n')

#Copy : copy in numpy is just duplicating the parent array and creating a duplicate array with the parent data
#Note : changes made to the data in the copied array does not reflect in parent array

orgArr = np.arange(1,11)
copArr = orgArr.copy() # creates copy array
copArr[0] = 22 # changing the data in copied array
print("Original Array:",'\n',orgArr,'\n')
print("Copied and mutated Array:",'\n',copArr,'\n')

#View : view in numpy is representing the parent array
#Note : unlike copy, the changes made to the view array will reflect in the parent array

orgArr1 = np.arange(1,7)
print("Original Array:",'\n',orgArr1,'\n')
viwArr = orgArr1.view() # creates view array
viwArr[2]=69 # changing the data in the view array
print("View Array:",'\n',viwArr,'\n')
print("original Array after updating view array:",'\n',orgArr1,'\n')

#Sorting : arranging elements in the array into a particular order 
#Numpy Sorting : sorting in Numpy uses a pre defined method / function called .sort()

a1 = np.array([1,55,22,69,7,2,33,4,6,52,77,99,37,25])
print("Unsorted Array:",'\n',a1,'\n')
s = np.sort(a1) # sortes array a1
print("Sorted Array:",'\n',s,'\n')

#BroadCasting : Broadcasting allows to perform mathematical operation without reshaping the arrays.
#BroadCasting Procedure : 
# 1. Dimension verification : verifies wether the operating arrays have same shape
# 2. Dimension padding : if the shape does not matches, the array with smaller shape is left padded with ones
# 3. Shape compatibility : the arrays are comptaible if their dimensions are equal or equals to 1

#Broadcasting a Scalar to 1D array:
b1 = np.arange(1,5)
print("Array before Broadcasting scalar :",'\n',b1,'\n')
x = 5
res3 = b1+x
print("Array after Broadcasting scalar :",'\n',res3,'\n')

#Broadcasting 1D array to 2D array:
b2 = np.array([[1,2,3,4],[5,6,7,8]])
print("Array befor broadcasting with 1D array :",'\n',b2,'\n')
res4 = b1+b2
print("Array after broadcasting with 1D array :",'\n',res4,'\n')

#Broadcasting in conditionals:
ages = np.array([12,55,48,96,74,3,14,18])
tags = ["Elgible","Not Elgible"]
cond = np.where(ages>18,tags[0],tags[1]) 
# Here, we are using np.where() function in which it considers boolean condition for the result to be alloted. 
# after the conditional value, we have to give what to return if true, then what to return if it fails to meet the conddition. 
print("Ages Array:",'\n',ages,'\n')
print("Filtered Ages Array elgible to vote:",'\n',cond,'\n')

#Broadcasting for matrix multiplication:
mat = np.array([[10,20,30],[40,50,60]])
vals = np.array([2,3,4])
print("Matrix before multiplying :",'\n',mat,'\n')
mmat = mat*vals
print("Matrix after multiplying :",'\n',mmat,'\n')

#Broadcasting for Adjusting values:
temps = np.array([[31.5,33,28.6,37.2,33.4],[28,33,35,29.3,32.5],[34,36.2,25.6,29.9,31.6]])
corr = np.array([-2,+1,-0.5])
ct = temps+corr[:,None] 
# we have kept None because the shape of corr is (3,) it means 3 elements in 1D array
print("Temperatures before correcting :",'\n',temps,'\n')
print("Temperatures after correcting :",'\n',ct,'\n')

#<<<<<<<< ------- completed  Day 02 ------- >>>>>>>> < Author : Srikar Yerraguntla > < 21-07-2026 @ 22:30 PM >