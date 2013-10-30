from numpy import *

a = array( [2,3,4] )
b = array([1.2, 3.5, 5.1])
c = array([1, 3, 5], dtype=float)

a.dtype == int
c.dtype == float ## true

d = zeros( (3, 4) ) ## by default uses float
e = zeros( (3, 4), dtype=int )
d.dtype == float ## true
e.dtype == int ## true

a = arange(3)  ## array([0, 1, 2]]))
a = arange(10,15) # array([10, 11, 12, 13, 14])
a = array([10, 12, 14]) # array([10, 12, 14])
a = linspace(10, 15, 3) # array([ 10. ,  12.5,  15. ])
f = sin(a)

print a ## yay this works
a = arange(15).reshape(3, 5)  ## reshape to a 3x5 matrix
print a

a = array( [20, 30, 40, 50])
b = arange(4)
a.size
a.shape
a.ndim
c = a - b
d = b ** 2
sin(a)
10 * sin(a)
a < 35 ## array([ True,  True, False, False], dtype=bool)

A = array( [[1, 1], [0, 1]] )
B = array( [[2, 0], [3, 4]] )
A * B
dot(A, B)

a = ones((2, 3), dtype=int)
b = random.random((2, 3))

b.min()
b.max()

a = array([[1,11], [3,9], [5,7]])
a.sum()       ## 36
a.sum(axis=0) ## sum rows    (i.e. sum per col)  [9, 27]
a.sum(axis=1) ## sum columns (i.e. sum per row)  [12, 12, 12]
a.min()       ## 1
a.min(axis=0) ## [1, 7]
a.min(axis=1) ## [1, 3, 5]
a.cumsum()    ## [ 1, 12, 15, 24, 29, 36]

for row in a:
    print row

for element in a.flat:
    print element

## combining arrays
a = array([[1,11], [3,9], [5,7]])
b = array([[8, 2]])
c = array([[1], [2], [3]])
vstack((a, b))
hstack((a, c))
a[0, :] ## get row 0, all columns  i.e. indexing is 0-based, returns 1d array
a[:, 1] ## get all rows, column 1

d = a.copy())

a = arange(12) ** 2                ## array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100, 121])
i = array( [1, 1, 3, 8, 5] )       ## array([1, 1, 3, 8, 5])
a[i]                               ## array([ 1,  1,  9, 64, 25])
j = array( [ [ 3, 4], [ 9, 7 ] ] ) ## array([[3, 4], [9, 7]])
a[j]                               ## array([[ 9, 16], [81, 49]])

b = a > 25    ## Boolean array
              ## array([False, False, False, False, False, False,  True,  True,  True, True,  True,  True], dtype=bool)

a[b]          ## Only the elements of a greataer than 25
              ##    array([ 36,  49,  64,  81, 100, 121])
              ##    also could do a[a > 25]

a[invert(b)]  ## Only the elements of a less than or equal to 25

a[b] = 0      ## All elements of 'a' greater than  25 become 0
              ##    array([ 0,  1,  4,  9, 16, 25,  0,  0,  0,  0,  0,  0])

a[invert(b)] = 1

## linear algebra
a = array([[1.0, 2.0], [3.0, 4.0]])
b = a.transpose()) ## array([[ 1.,  3.], [ 2.,  4.]])

from numpy.linalg import *
c = inv(a)   ## inverse
dot(c, c)

A = matrix('1.0 2.0; 3.0 4.0')


A = arange(12)     ## array    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
A.shape            ##  (12,)
A.shape = (3, 4)   ##        shapes the array into a 2-d array (3x4))

M = mat(A.copy())  ## matrix
M.shape            ##  (1, 12)


M.A  ## get Array representation of a matrix
M[:, M.A[0, :] > 1]    ## super useful for indexing into a matrix


x = arange(0,10,2)                     # x=([0,2,4,6,8])
y = arange(5)                          # y=([0,1,2,3,4])
m = vstack([x,y])                      # m=([[0,2,4,6,8],
                                       #     [0,1,2,3,4]])

xy = hstack([x,y])                     # xy =([0,2,4,6,8,0,1,2,3,4])
