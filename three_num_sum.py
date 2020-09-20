#####################################################################################################################
'''
                                                            Three Number Sum .n• 
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold. 
If no three numbers sum up to the target sum, the function should return an empty array. 
Sample Input 

= [12, 3, 1, 2, -6, 5, -8, 6] target=0
output:  [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
'''
#######################################################################################################################
#my brute soln
def threeNumberSum(array, targetSum):
    array.sort()
	l=[]
	for i in range(len(array)-2):
		for j in range(i+1,len(array)-1):
			for k in range(j+1,len(array)):
				if array[i]+array[j]+array[k]==targetSum:
					l.append([array[i],array[j],array[k]])
	return l
					
#########################################################################################################################




#effecient code
def threeNumberSum(array, targetSum):
	array.sort()
	l=[]
	if len(array)==0:
		return l
    for i in range(len(array)-2):
		
		lptr=i+1
		rptr=len(array)-1
		while lptr<rptr:
			if array[i]+array[lptr]+array[rptr]==targetSum:
				l.append([array[i],array[lptr],array[rptr]])
				lptr+=1
				rptr-=1
			elif array[i]+array[lptr]+array[rptr]>targetSum:
				rptr-=1
			else:
				lptr+=1
	return l
