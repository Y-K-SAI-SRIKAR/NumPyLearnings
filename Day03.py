# Date : 22-07-26
# Topics Covered : Basic Arthimetic operations, Aggregartions, Universal Functions.

import numpy as np

#Basic Arthimetic Operations:
#Note : To perform Arthimetic Operations , the arrays must be of same shape. else Numpy will raises an error.
#Note : The operations perfromed under are element wise operations in the arrays.
arr = np.arange(1,6)
arr1 = np.array([7,3,1,2,9])
print("Array 1:",'\n',arr,'\n')
print("Array 2:",'\n',arr1,'\n')
#Addition : uses np.add() method or we can use '+' operator
res = np.add(arr,arr1)
print("Addition of arrays:",'\n',res,'\n')

#Subtraction : uses np.subtract() method or we can use '-' operator
res1 = np.subtract(arr,arr1)
print("Subtraction of arrays:",'\n',res1,'\n')

#Multiplication : uses np.multiply() method or we can use '*' operator
res2 = np.multiply(arr,arr1)
print("Multiplication of arrays:",'\n',res2,'\n')

#Division : uses np.divide() method or we can use '/' operator
res3 = np.divide(arr,arr1)
print("Division of arrays:",'\n',res3,'\n')

#Modulus : uses np.mod() method or we can use '%' operator
res4 = np.mod(arr1,arr1)
print("Modulus of arrays:",'\n',res4,'\n')

#Exponentiation : uses np.power() method or we can use '**' operator
res5 = np.power(arr,arr1)
print("Exponentiation of arrays:",'\n',res5,'\n')

#Aggregations : Operations performed on entire data object and returns a combined result of operation.
#sum() aggregation : 
a1 = np.array([[12,14,55,36],[55,19,36,22]])
a2 = np.array([[78,63,11,20],[5,36,47,69]])
print("Array A1:",'\n',a1,'\n')
print("Array A2:",'\n',a2,'\n')
sa = np.sum(a1,axis=0,dtype=np.int16,keepdims=True) # here axis = 0 : col wise operation, keepdims is used to preserve the dimension of array
sa1 = np.sum(a2,axis=1,dtype=np.int16,keepdims=True) #here axis = 1 : row wise operation.
sa2 = np.sum(a1,axis=None,dtype=np.int16,keepdims=False) #dimensions will change here
print("Sum Aggr on A1:",'\n',sa,'\n')
print("Sum Aggr on A2:",'\n',sa1,'\n')
print("Sum Aggr on A1 with axis = None",'\n',sa2,'\n')

#mean() aggregation :
ma = np.mean(a1,axis=0,dtype=np.float64) # mean of arr a1 with col order
ma1 = np.mean(a2,axis=1,dtype=np.int64) # mean of arra a2 qith row order
ma2 = np.mean(a1,axis=None,dtype=np.int64)
print("Mean Aggr on A1:",'\n',ma,'\n')
print("Mean Aggr on A2:",'\n',ma1,'\n')
print("Mean Aggr on A1 with axis=None:",'\n',ma2,'\n')

#max() aggregation :
#Note : for max() and min() aggreagtions arrays must not be of same shape, broadcasting will be applied here.
a3 = np.array([22,16,5,4])
mx = np.maximum(a1,a3,dtype=np.int16) # Broadcasting happens here
mx1 = np.maximum(a1,a2,dtype=np.int32)
print("Max Aggr on A1 and A3:",'\n',mx,'\n')
print("Max Aggr on A1 and A2:",'\n',mx1,'\n')

#min() aggregation :
mm = np.minimum(a1,a3,dtype=np.int16) # Broadcasting happens here
mm1 = np.minimum(a1,a3,dtype=np.int32) 
print("Min Aggr on A1 and A3:",'\n',mm,'\n')
print("Min Aggr on A1 and A2:",'\n',mm1,'\n')

#conditional Aggregation in max() and min()
a4 = np.array([44,12,28,17,18,20])
a5 = np.array([89,25,46,10,9,16])
mma = np.maximum(a4[a4>18],a5[a5>18])
mma1 = np.minimum(a4[a4>18],a5[a5>18])
print("Array a4:",'\n',a4,'\n')
print("Array a5:",'\n',a5,'\n')
print("Max Conditional Aggr filter result:",'\n',mma,'\n')
print("Min Conditional Aggr filter result:",'\n',mma1,'\n')

#Universal Functions : Universal functions in numpy are fast, vectorised element wise operable functions.
# ufuncs include Arithmetic, Statistical, Trigonometric, Bitwise operations.
#Creating a custom ufunc:
def myfunc(a,b):
    return np.power(a,b)
myfunc = np.frompyfunc(myfunc,2,1)
a,b = np.arange(1,4),np.arange(4,7)
print("Array A:",'\n',a,'\n')
print("Array B:",'\n',b,'\n')
print("Custom UFunction output:",'\n',myfunc(a,b))
print("Verifying the Custom ufunc:",'\n',type(myfunc),'\n')

#Trigonometric Functions:
s1 = np.sin(a)
c1 = np.cos(a)
t1 = np.tan(a)
s2 = np.arcsin(-0.62)
c2 = np.arccos(0.92)
t2 = np.arctan(-0.12)
s3 = np.sinh(b)
c3 = np.cosh(b)
t3 = np.tanh(b)
s4 = np.arcsinh(b)
c4 = np.arccosh(b)
t4 = np.arctanh(b)
dr = np.deg2rad(a)
rd = np.rad2deg(b)
print("sine values of Array A:",'\n',s1,'\n')
print("Inverse sine value: ",'\n',s2,'\n')
print("Hyperbolic sine values of Array B:",'\n',s3,'\n')
print("Inverse Hyperbolic sine values of Array B:",'\n',s4,'\n')
print("cos values of Array A:",'\n',c1,'\n')
print("Inverse cos value:",'\n',c2,'\n')
print("Hyperbolic cos values of Array B:",'\n',c3,'\n')
print("Inverse Hyperbolic cos values of Array B:",'\n',c4,'\n')
print("tan values of Array A:",'\n',t1,'\n')
print("Inverse tan value:",'\n',t2,'\n')
print("Hyperbolic tan values of Array B:",'\n',t3,'\n')
print("Inverse Hyperbolic tan values of Array B:",'\n',t4,'\n')
print("Degrees to Radians conversion of Array A:",'\n',dr,'\n')
print("Radians to Degrees conversion of Array B:",'\n',rd,'\n')

#Statistical UFunctions:
m1 = np.mean(a)
m2 = np.average(b)
m3 = np.median(a) 
s5 = np.std(b) # standard deviation
v1 = np.var(b) # variance
cs = np.cumsum(b) # cummulative sum of array B
cp = np.cumprod(a) # cummulative sum of array A
m4 = np.amax(a) # same as max()
m5 = np.amin(b) # same as min()
p1 = np.ptp(a) # calculates range 
p2 = np.percentile(a,20) # 20th percentile of 55
print("Mean of Array A:",'\n',m1,'\n')
print("Average of Array B:",'\n',m2,'\n')
print("Standard Deviation of Array A:",'\n',s5,'\n')
print("Variance of Array B:",'\n',v1,'\n')
print("Cummulative sum of Array B:",'\n',cs,'\n')
print("Cummulative Product of Array A:",'\n',cp,'\n')
print("Percentile of Array A:",'\n',p2,'\n')
print("Range of Array A:",'\n',p1,'\n')

#Bitwise UFunctions:
ba = np.bitwise_and(a,b)
bo = np.bitwise_or(a,b)
iv = np.invert(a)
bx = np.bitwise_xor(a,b)
lf = np.left_shift(a,2) # left shifts to 2 positions
rf = np.right_shift(b,2) # right shifts to 2 positions
print("Bitwise AND :",'\n',ba,'\n')
print("Bitwise OR :",'\n',bo,'\n')
print("Bitwise XOR :",'\n',bx,'\n')
print("Bitwise NOT :",'\n',iv,'\n')
print("Left Shift of A:",'\n',lf,'\n')
print("Right Shift of B:",'\n',rf,'\n')

#Arithmetic UFunctions:
num1 = 4
num2 = 7
arr1 = np.array([1,2,5,5,4,3,3,1,1,7,8,9])
arr2 = np.array([9,2,2,4,6,6,7,8,3,3,5,1])
farr = np.array([1.5,2.7,3,66.9,0.27,3.695])

#Set operations:
se1 = np.unique(arr1) #creates a set from array
se2 = np.unique(arr2)
u1 = np.union1d(se1,se2) # performs union operation
d1 = np.setdiff1d(se1,se2) # performs set difference between a&b
d2 = np.setdiff1d(se2,se1) # performs set difference between b&a
d3 = np.setxor1d(se1,se2) # performs symetrical difference between a&b
i1 = np.intersect1d(se1,se2) # performs intersection between a&b
print("Set 1:",'\n',se1,'\n')
print("Set 2:",'\n',se2,'\n')
print("Union :",'\n',u1,'\n')
print("Intersection :",'\n',i1,'\n')
print("Diff b/w A&B:",'\n',d1,'\n')
print("Diff b/w B&A:",'\n',d2,'\n')
print("Symmetric Diff b/w:",'\n',d3,'\n')

#Logarithms:
l1 = np.log2(num1)
l2 = np.log10(num2)
l3 = np.log(arr1)
print("Log with base 2:",'\n',l1,'\n')
print("Log with base 10:",'\n',l2,'\n')
print("Natural log:",'\n',l3,'\n')

#LCM & GCD:
lc1 = np.lcm(num1,num2) 
gc1 = np.gcd(num1,num2)
lc2 = np.lcm.reduce(arr1) # performs lcm between elements of arr1
gc2 = np.gcd.reduce(arr2) # performs gcd between elements of arr2
print("LCM b/w numbers:",'\n',lc1,'\n')
print("GCD b/w numbers:",'\n',gc1,'\n')
print("LCM of Array:",'\n',lc2,'\n')
print("GCD of Array:",'\n',gc2)

#Numerical Operations:
com1 = 2+3j
fl1 = np.floor(farr)
cl1 = np.ceil(farr)
tr1 = np.trunc(farr)
r1 = np.rint(farr)
po1 = np.power(num1,num2)
po = np.positive(-88)
neg = np.negative(52) 
rn2 = np.real(com1) # verifies the number is real or not
coj = np.conj(com1) # returns the conjugate of the number
coj1 = np.conj(66)
sq = np.square(25)
sr = np.sqrt(66)
cr = np.cbrt(27)
rec = np.reciprocal(se1)
nnu = np.nan_to_num(t4)
clp = np.clip(farr,2,9)
print("Floor values:",'\n',fl1,'\n')
print("Ceil values:",'\n',cl1,'\n')
print("Truncated values :",'\n',tr1,'\n')
print("Rounded values:",'\n',r1,'\n')
print("Power of values:",'\n',po1,'\n')
print("positive value :",'\n',po,'\n')
print("Negative value :",'\n',neg,'\n')
print("Real Number of Complex:",'\n',rn2,'\n')
print("Conjugate of complex :",'\n',coj,'\n')
print("Conjugate :",'\n',coj1,'\n')
print("Squared value:",'\n',sq,'\n')
print("Square root of 66:",'\n',sr,'\n')
print("Cube root of 27:",'\n',cr,'\n')
print("Reciprocals of:",'\n',rec,'\n')
print("NaN to Num conversion:",'\n',nnu,'\n')
print("Limited Array:",'\n',clp,'\n')

#<<<<<<<< ------- completed  Day 03 ------- >>>>>>>> < Author : Srikar Yerraguntla > < 22-07-2026 @ 23:30 PM >