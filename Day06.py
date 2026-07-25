# Date : 25-07-26
# Topics Covered : AdOps, File I/O, Exception Handling.

import numpy as np

#AdOps : Advance Operations in numpy include conditional selection, filtering with the numerical data.
# AdOps has some built-ins which makes flitering and manipulating the numerical data simplier and faster.

#np.where() : conditional masking - maps the filter based on conditions to the array
#let us consider a simple vote elgibility calculator.
ages = np.array([18,22,10,6,3,88,94,69])
filter = np.array(["Elgible","Not Elgible"])
cond = ages>18
res = np.where(cond,filter[0],filter[1])
print("Ages Data:",'\n',ages,'\n')
print("Filtered Data:",'\n',res,'\n')

#np.select() : selects and maps the filter among the choices and conditions
nums = np.array([55,20,16,73,11,6,9,7,69,23])
conds = [nums%2==0, nums%2!=0]
options = ["Even","Odd"]
res = np.select(conds,options,default='F')
print("Nums Data:",'\n',nums,'\n')
print("Mapped Result:",'\n',res,'\n')

#np.choose() : its a mapping technique used based on Indices of the filter array and value array
filter_array = np.array([[0,1],[1,0],[1,1],[0,0]])
val_array = np.array([68,69])
res = np.choose(filter_array,val_array)
print("Filter Array:",'\n',filter_array,'\n')
print("Value Array:",'\n',val_array,'\n')
print("Resultant Array:",'\n',res,'\n')

#np.correlate() : its a mathematical application which finds the correlation between 2 1D arrays
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([0.2,0.6,0.8,0.9,0.4])
res1 = np.correlate(arr1,arr2,mode='full') # calculates all possible correlated values within the array ranges
res2 = np.correlate(arr1,arr2,mode='valid') # calculates correlated values where the both arrays completely overlap
res3 = np.correlate(arr1,arr2,mode='same') # calculates correlated values within the length of arrays
print("Array 1:",'\n',arr1,'\n')
print("Array 2:",'\n',arr2,'\n')
print("Full Correlation:",'\n',res1,'\n')
print("Valid Correlation;",'\n',res2,'\n')
print("Same Correlation:",'\n',res3,'\n')

#np.convolve() : its a mathematical application which finds the convolution between 2 1D arrays
res4 = np.convolve(arr1,arr2,mode='full')
res5 = np.convolve(arr1,arr2,mode='valid')
res6 = np.convolve(arr1,arr2,mode='same')
print("Full Convolution:",'\n',res4,'\n')
print("Valid Convolution:",'\n',res5,'\n')
print("Same Convolution:",'\n',res6,'\n')

#File Operations:
data1 = np.random.randint(1,20,(10,3))
data2 = np.random.randint(10,40,(10,4))
data3 = np.random.normal(loc=5,scale=2,size=(10,5))
#saving as a numpy Array file - .npy
np.save('rand1.npy',data1)
print("file Saved successfully as : rand1.npy",'\n')
#saving as a numpy zip file - .npz
np.save('rand2.npz',data2)
print("file saved successfully as : rand2.npz",'\n')

#loading the saved file
x1 = np.load('rand1.npy')
print("Loaded rand1.npy:",'\n',x1,'\n')
x2 = np.load('rand2.npz.npy')
print("Loaded rand2.npz:",'\n',x2[0],'\n')

#zipping n files:
np.savez('RandData.npz',a1=data1,a2=data3)
print("files Zipped Successfully!")
#loading files from Zipped file:
x = np.load('RandData.npz')
for i in x:
    print(i)
print("A1:",'\n',x['a1'],'\n')

#Numpy Exceptions : Numpy exceptions can be handled by defining scope in seterr() block
# set err block handles floating point exceptions such as :
# divide - exceptions while performing divisions
# over - when the stack is overflowing 
# invalid - if any invalid call is being passed.

# the scopes of these exceptions can be handled in these ways;
# np.seterr(divide='raise') : raises exception
# np.seterr(divide = 'warn') : prints a warn message on the console
# np.seterr(divide = 'ignore') : ignores the exception 

# Examples:
def divCase():
    ar1 = np.array([1,5,9])
    ar2 = np.array([2,0,6])
    np.seterr(divide='warn')
    res = np.divide(ar1,ar2)
    return res

def OverCase():
    num = 10000
    np.seterr(over='warn')
    ans = np.exp(num)
    return ans

def InvCase():
    n = -1
    np.seterr(invalid='raise')
    ans1 = np.sqrt(n)
    return ans1

print("Divide Case:",'\n',divCase(),'\n')
print("Over Case:",'\n',OverCase(),'\n')
print("Invalid Case:",'\n',InvCase(),'\n')

#<<<<<<<< ------- completed  Day 06 ------- >>>>>>>> < Author : Srikar Yerraguntla > < 25-07-2026 @ 23:45 PM >