import numpy as np
arr1=np.random.rand(15,9)
arr2=np.random.rand(15,9)
print(arr1,arr2)
addition= arr1+arr2
subtraction=arr1-arr2
multiplication=arr1*arr2
print("----------Addition Started------------")
print(addition)
print("----------Addition Completed----------")
print("----------subtraction Started----------")
print(subtraction)
print("----------subtraction Completed----------")
print("----------multiplication Started----------")
print(multiplication)
print("-------Multiplication Completed----------")

arr3 = 5* arr1
print(arr3)
print("--stuff done----")

arr4=np.random.rand(5,5)
sliced_arr4= arr4[0:-3]
print(arr4)
print("-----After slicing-----")
print(sliced_arr4)
