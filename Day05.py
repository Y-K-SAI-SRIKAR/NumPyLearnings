# Date : 24-07-26
# Topics Covered : Random Variables and Probability, Practical application of Numpy in Neural Networks.

import numpy as np

#Random Number generation:
arr1 = np.random.randint(10,20,(2,3)) # takes input as lower bound, upper bound and shape of resultant array
print("Random Integer 2D Array:",'\n',arr1,'\n')
arr2 = np.random.randint(1,5,5)
print("Random Integer 1D array:",'\n',arr2,'\n')

#Random varaibles & Probability Distributions:
#Normal Distirbution:
ri1 = np.random.normal()
print("Random Normal Distribution value:",'\n',ri1,'\n')
arr3 = np.random.normal(loc=10,scale=2,size=5)
print("Normal Distribution Spread Across centre of 10 and STD of 2:",'\n',arr3,'\n')
arr4 = np.random.normal(loc=5,scale=2.5,size=(2,4))
print("Normal Distribution Spread Across centre of 5 and STD of 2.5:",'\n',arr4,'\n')

#Binomial Distribution: binomial(n,p) where n = total observations or sample , p = possibilty rate
ri2 = np.random.binomial(8,0.32)
print("Random Binomial Distribution value with n=8 and p=0.32:",'\n',ri2,'\n')
arr5 = np.random.binomial(55,0.27,size=(3,3))
print("Binomial Distribution Spread with n=55 and p=0.27:",'\n',arr5,'\n')

#Poisson Distribution: poisson(lam) f(x)= (lam^x*e^-lam)/x!
ri3 = np.random.poisson(lam=4)
print("Random Poisson Distribution value where lambda = 4:",'\n',ri3,'\n')
arr6 = np.random.poisson(lam=2.7,size=(5,1))
print("Poisson Distribution spread with lambda = 2.7:",'\n',arr6,'\n')

#Uniform Distribution: uniform(a,b) f(x): 1/b-a
ri4 = np.random.uniform()
print("Random Uniform Distribution value:",'\n',ri4,'\n')
arr7 = np.random.uniform(10,20,size=(2,4))
print("Uniform Distribution Spread across range of 10&20:",'\n',arr7,'\n')

#exponential Distribution: exponential(b) where b is inverse of possibility
ri5 = np.random.exponential()
print("Random Exponential Distribution value:",'\n',ri5,'\n')
arr8 =  np.random.exponential(0.22,size=(5,1))
print("Exponential Distribution Spread with inverse rate of possibility b = 0.22:",'\n',arr8,'\n')

#Chi-Square Distribution: chisquare(df) where df = degrees of freedom
ri6 = np.random.chisquare(0.55)
print("Chi-Square Distribution value with df = 0.55:",'\n',ri6,'\n')
arr9 = np.random.chisquare(0.2,size=(2,2))
print("Chi-Square disribution spread with degrees of freedom = 0.56:",'\n',arr9,'\n')

# Practical Application: Loan Provision Prediction Through Multi Layer Perceptron Model:
x1 = int(input("Enter the Tenure in Yrs:"))
x2 = float(input("Enter your current Credit Score:"))
w11 = 0.55
w12 = -0.35
w21 = 0.65
w22 = -0.42
b1 = 0.4
b2 = -0.5
b3 = 0.3
v1 = 0.6
v2 = -0.8
hi1 = x1*w11+x2*w12+b1
hi2 = x1*w21+x2*w22+b2

#Activation Function:
def sigmoid(k):
    return 1/(1+np.exp(-k))

h1 = sigmoid(hi1)
h2 = sigmoid(hi2)
m = h1*v1+h2*v2+b3
op = sigmoid(m)

print("Tenure:",'\n',x1,'\n')
print("Credit Score:",'\n',x2,'\n')
print("Provision of Loan Status:")
pred = ""
if 0<op<=0.5:
    pred="Loan will not be Provisioned"
else:
    pred = "Loan will be Provisioned"
print(pred)

#<<<<<<<< ------- completed  Day 05 ------- >>>>>>>> < Author : Srikar Yerraguntla > < 24-07-2026 @ 23:35 PM >