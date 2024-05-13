import heapq

class Heap:

	def __init__(self):
		self.arr=[]
	
	def push(self,item):
		heapq.heappush(self.arr,item)
	
	def pop(self):
		return heapq.heappop(self.arr)
	
	@property
	def size(self):
		return len(self.arr)
	
	def top(self):
		if self.size>0:
			return self.arr[0]


def getKthLargest(arr, k):
	#	Write your code here.

	size = len(arr)
	heap = Heap()
	for i in range(size):
		total = 0
		for j in range(i,size):
			total=  total+arr[j]
			if heap.size<k:
				heap.push(total)
			else:
				if total>heap.top():
					heap.pop()
					heap.push(total) 
	return heap.top()




	#===============Old Solution
 
    ##Time Complexity = n^2Logn
	##Space Complexity = n^2
	# size = len(arr)

	# sumOfSubArr=[]
	# for i in range(size):
	# 	total=0
	# 	for j in range(i,size):
	# 		total=total+arr[j]
	# 		sumOfSubArr.append(total)
	
	# sumOfSubArr.sort()
	# return sumOfSubArr[-k]