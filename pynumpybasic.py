import numpy as np
import sys # this is to get size of allocated space
a=np.array([1,2,3])
# array function in numpy takes a list of values and return a 1-D array
print(a)
print(sys.getsizeof(a))
ar=np.arange(start=3,stop=100,step=3)
#this function will return an array of evenly spaced step is the interval you want
print(ar,sys.getsizeof(ar))
arr_linspc = np.linspace(start=0.333,stop=0.3331,num=10,endpoint=True,retstep=True,dtype=int)
# It will return an array of evenly spaced
# endpoint=True means it will include stop in the array if false it will exclude
#retstep=True it will return the common difference i.e difference between successive number
#dtype is the type of number you want to be returned
print(arr_linspc)
print(np.ones(shape=(5,3),dtype=int,order="F"))
#it will return an array of 1 as each element 
#order here defines whether to store array in row major or column major
#"C" in double quote for row major and "F" for column major
print(np.zeros((5,4),float,"C"))
# similar to np.ones
print(np.empty(shape=(6,6),dtype=float))
empt_arr = np.empty(3)
print(empt_arr)
print(np.random.rand(15,9))
md_arr=np.array([[i for i in range(10)],[x**2 for x in range(10)],[y**3 for y in range(10)]])
print(md_arr)
md_arr_size=np.size(md_arr)
md_arr_row,md_arr_column=np.shape(md_arr)
print(md_arr_row,md_arr_column)
new_formated_arr=np.reshape(md_arr,(6,5))
#Using np.reshape() you can reshape the array like for a (3,10) we reshaped it to (6,5)
print(new_formated_arr)
print(np.ndim(new_formated_arr))
