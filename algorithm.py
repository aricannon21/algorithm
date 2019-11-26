
#check if right element is less, if so than swap
#list_1 = [1,2,-1,0,10]
#not sorted so do it again
#list_1 = [1,-1, 0, 2, 10]
#sort one more time
#list_1 = [-1,0,1,2,10]
list_1 = [2,1,10,-1,0]
n = len(list_1) #=5
for i in range(0,n): #in first iteration i = 0
	#you cant use same iterator variable, you will override i
	#for each iteration of the outer loop, the unsorted portion will decrease by 1
	for j in range(0,n-i-1):
		#j is also zero
		if (list_1[j]>list_1[j+1]):
			temp = list_1[j]
			list_1[j] = list_1[j+1]
			list_1[j+1] = temp
			print(list_1)

