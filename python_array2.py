import numpy as np
arr_1D = np.array([1,2,3,4,5,6,7,8,9,10])
a=[]
print("Original array:",arr_1D)
arr_odd_true = np.array(a, dtype=bool)
for i in range(1, 11):
    if(i% 2 == 0):
        print("True")
        a.append(i)
    else:
        print("False")
        a.append(i)
    #print("true"  if i % 2 == 0 else 'False')
    a.append(i)

#print("Boolean array:",bool)
print(a)
print("length of arr_1D", len(arr_1D))
print("length of arr_odd_true",len(arr_odd_true))
