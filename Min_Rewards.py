#######################################################################################################################################################################################
                                                                     MIN REWARDS
'''                                                                     
Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student scores on the final exam in a particular order (not necessarily sorted),
and you want to reward your students. You decide to do so fairly by giving them arbitrary rewards following two rules: 
1) All students must receive at least one reward. 
2) Any given student must receive strictly more rewards than an adjacent student (a student immediately to the left or to the right) with a lower score and must
receive strictly fewer rewards than an adjacent student with a higher score. 
Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out to students to satisfy the two rules. 
You can assume that all students have different scores; in other words, the scores are all unique.

'''

####################################################################################################################################################################################

#brute force approach


def minRewards(scores):
	rewards=[1]*len(scores)
	for i in range(1,len(scores)):
		j=i-1
		if scores[i]>scores[j]:
			#agar sirf aage waale bada hai ,to only one no. to be incremented
			rewards[i]=rewards[j]+1
		else :
			while j>=0 and scores[j+1]<scores[j]:
				#if peeche wala bada hai to sabko inc karna padega,jabtak all in dec order
				rewards[j]=max(rewards[j],rewards[j+1]+1)
				j-=1
	return sum(rewards)
  
  #######################################################################################################################################################
  
  #best soln:
  order of n O(n)
  
  
  def minRewards(scores):
	#all the students to get atleat one reward
	Rewards=[1]*len(scores)
	
	#first loop from left to right.........
    for i in range(0,len(scores)-1):
		
		#if score of next student high,just make his reward 1 more than 
		#the current student
		if(scores[i]<scores[i+1]):
			Rewards[i+1]=Rewards[i]+1
	
	#2nd loop from right to left..................	
    for i in range(len(scores)-1,0,-1):
		#if score of prev student more than current student's score,
		#if reward of prev student>reward of current stud+1,
		# then only make his reward 1+current students reward 
		if scores[i]<scores[i-1]:
			Rewards[i-1]=max(Rewards[i-1],Rewards[i]+1)
	return sum(Rewards)
  
  
  #######################################################################################################################################################
  
	
	
	
	
	
    
  
