import numpy as np
#--- Linear Equations--#
#−𝑥1+3𝑥2=7,
# 3𝑥1+2𝑥2=1,
#---------------------#
#A*x=B
A = np.array([[-1,3],[3,2]])
B=np.array([7,1])
print("Matrix A:")
print(A)
print("\nArray B:")
print(B)
print(A.shape)
try:
    x= np.linalg.solve(A,B)
except np.linalg.LinAlgError as err:
    print(err)
# np.linalg.solve() function return solution of linear equations
print(f"Solution is {x}")
print(np.linalg.det(A))
#solving by elimination

A_system = np.hstack((A, B.reshape((2, 1))))

print(A_system)
A_system_res= A_system.copy()

A_system_res[1] = 3 * A_system_res[0] + A_system_res[1]

print(A_system_res)
A_system_res[1] = 1/11 * A_system_res[1]

print(A_system_res)
