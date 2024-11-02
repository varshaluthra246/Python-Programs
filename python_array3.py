import numpy as np
arr_1D = np.array([1,2,3,4,5,6,7,8,9,10])
arr_odd_true = []
for i in arr_1D:
    even = 'False' if i % 2 == 0 else 'True' 
    arr_odd_true.append(even)
    
#print("Even elements in array = ",[True for i in arr_1D if i % 2 == 0 ])
#print("Odd elements in array = ",[False for i in arr_1D if i % 2 != 0 ])

print("arr_1D=" , arr_1D)
print("arr_odd_true = ",arr_odd_true)
