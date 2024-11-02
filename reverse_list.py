"""
Reversing a List in Python
Input : list = [10, 11, 12, 13, 14, 15]
Output : [15, 14, 13, 12, 11, 10]
"""
# Reversing a list using reversed()
def Reverse(lst):
	return [ele for ele in reversed([10, 11, 12, 13, 14, 15])]
	
# Driver Code
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))
