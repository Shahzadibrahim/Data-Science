# 1- Import the numpy package under the name `np`
import numpy as np

# 2 -Print the numpy version
# print(np.__version__)

# 3 -Create a vector of zeros with the size 10
# x = np.zeros(10)
# print(x)

# 4- How to find the memory size of any array
# a = np.array([100, 20, 34, 55])
# print("Size of the array:", a.itemsize)

# 5- How to get the documentation of the numpy add function from the IPython console?
# np.add.__doc__


# 6- Create a vector of zeros with the size 10 but the fifth value which is 1
# with different ways
# b=np.array([int(x==4) for x in range(10)])
# print(b)
# print((np.arange(10) == 4).view(np.uint8))
# print((np.arange(10) == 4).astype(int))


# 7- Create a vector with values ranging from 10 to 49
# v = np.arange(10,50)
# print(v)


# 8- Reverse a vector (first element becomes last)
# v = np.arange(10, 50)
# print(v[::-1])


# 9- Create a 3x3 matrix with values ranging from 0 to 8
# x = np.arange(0, 9).reshape(3,3)
# print(x)


# 10- Find indices of non-zero elements from \[1,2,0,0,4,0\]
# x = np.array([1,2,0,0,4,0])
# print(np.nonzero(x))


# 11- Create a 3x3 identity matrix
# x = np.identity(3)
# print(x)


# 12- Create a 3x3x3 array with random values
# x = np.random.random((3,3,3))
# print(x)


# 13- Create a 10x10 array with random values and find the minimum and maximum values
# x = np.random.random((10,10))
# print(x)
# xmin, xmax = x.min(), x.max()
# print(xmin, xmax)


# 14- Create a random vector of size 30 and find the mean value
# x = np.random.random(30)
# np.mean(x)
# print(np.mean(x))


# 15- Create a 2d array with 1 on the border and 0 inside
# x = np.ones((5,5))
# x[1:-1,1:-1] = 0
# print(x)


# 16- How to add a border (filled with 0's) around an existing array?
# x = np.ones((3,3))
# x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
# print(x)


# 17- What is the result of the following expression?
# 0 * np.nan
# np.nan == np.nan
# np.inf > np.nan
# np.nan - np.nan
# 0.3 == 3 * 0.1
#
# print(0 * np.nan)
# print(np.nan == np.nan)
# print(np.inf > np.nan)
# print(np.nan - np.nan)
# print(0.3 == 3 * 0.1)



# 18- Create a 5x5 matrix with values 1,2,3,4,7 on the diagonal
# x = np.diag([1, 2, 3, 4, 7])
# print(x)


# 19- Create a 8x8 matrix and fill it with a checkerboard pattern
# x = np.zeros((8,8))
# x[1::2,::2] = 1
# x[::2,1::2] = 1
# print(x)


# 20- Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
# print(np.unravel_index(99,(6,7,8)))


# 21- Create a checkerboard 8x8 matrix using the tile function
# array= np.array([[0,1], [1,0]])
# x = np.tile(array,(4,4))
# print (x)



# 22 - Normalize a 5x5 random matrix
# x = np.random.random((5,5))
# xmax, xmin = x.max(), x.min()
# x= (x-xmin)/(xmax-xmin)
# print(x)


# 23- Create an array of 2x4 with dtype numpy.int16, print the dtype of the array (RGBA)
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = x.reshape(2,4)
# # print(np.int16(arr))
# print(x.dtype)
# color = np.dtype([("r", np.ubyte, 1),
#                   ("g", np.ubyte, 1),
#                   ("b", np.ubyte, 1),
#                   ("a", np.ubyte, 1)])
# print(color)

# 24-  Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
# x = np.random.random((5,3))
# y = np.random.random((3,2))
# z = np.dot(x, y)
# print(z)


# 25- Given a 1D array, negate all elements which are between 3 and 8, in place.
# x = np.arange(11)
# x[(3 < x) & (x < 8)] *= -1
# print(x)


# 26-What is the output of the following script? (★☆☆)

# Author: Jake VanderPlas
# print(sum(range(5),-1))
# print(sum(range(5),-1))


# 27- Consider an integer vector Z, which of these expressions are legal?
# z=np.arange(10)
# print(z**z)
# print(z <- z)
# print(1j*z)


# 28- What are the result of the following expressions?
# print(np.array(0) / np.array(0))
# print(np.array(0) // np.array(0))
# print(np.array([np.nan]).astype(int).astype(float))


# 29- How to round away from zero a float array?
# z = np.array([-5.5,2.3,1.4,-3.2,-5.3])
# print(z)
# zz=np.copysign(np.ceil(np.abs(z)),z)
# print(zz)
# z1=np.abs(z)
# print(z1)
# z2=np.floor(z1)
# print(z2)
# z3=np.copysign(z2,z)
# print(z3)


# 30- How to find common values between two arrays?
# Z1 = np.random.randint(0,10,10)
# print(Z1)
# Z2 = np.random.randint(0,10,10)
# print(np.intersect1d(Z1,Z2))


# 31- How to ignore all numpy warnings (not recommended)?
# defaults = np.seterr(all="ignore")
# Z = np.ones(1) / 0
#
# _ = np.seterr(**defaults)
# with np.errstate(all="ignore"):
#     np.arange(3) / 0


# 32- Is the following expressions true?
# np.sqrt(-1) == np.emath.sqrt(-1)


# 33- How to get the dates of yesterday, today and tomorrow?
# yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
# print("Yestraday: ",yesterday)
# today     = np.datetime64('today', 'D')
# print("Today: ",today)
# tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
# print("Tomorrow: ",tomorrow)


# 34- How to get all the dates corresponding to the month of August 2016?
# print("August, 2016")
# print(np.arange('2016-08', '2016-09', dtype='datetime64[D]'))


# 35- How to compute ((A+B)\*(-A/2)) in place (without copy)?
# A = np.ones(3)*1
# B = np.ones(3)*2
# print(np.add(A,B,out=B))
# print(np.divide(A,2,out=A))
# print(np.negative(A,out=A))
# print(np.multiply(A,B,out=A))


# 36- Extract the integer part of a random array using 5 different methods
# Z = np.random.uniform(0,10,10)
# print(Z - Z%1)
# print(Z // 1)
# print(np.floor(Z))
# print(Z.astype(int))
# print(np.trunc(Z))


# 37- Create a 5x5 matrix with row values ranging from 0 to 4
# Z = np.zeros((5,5))
# Z += np.arange(5)
# print(Z)


# 39- Create a vector of size 10 with values ranging from 0 to 1, both excluded
# Z = np.linspace(0,1,11,endpoint=False)[1:]
# print(Z)

# 40- Create a random vector of size 10 and sort it
# Z = np.random.random(10)
# Z.sort()
# print(Z)
