import numpy as np
arr1=np.random.rand(3,4)
arr2=np.random.rand(3,4)
print("---arr1---")
print(arr1)
print("---arr2---")
print(arr2)
print("---after vertical stacking----")
vert_stack=np.vstack((arr1,arr2))
print(vert_stack)
hori_stacking=np.hstack((arr1,arr2))
print("---after horizontal stacking----")
print(hori_stacking)
hssplit=np.hsplit(arr1,4)
#hsplit in numpy split array horizontally into eqla division 
# so basically whatever you pass should be multiple of no of column of original array
# as here column is 4 so we can split into 4 if we will pass 3 it with throw an error
print("---after spliting----")
print(hssplit)

