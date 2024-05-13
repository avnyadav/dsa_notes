
import heapq

class LinkedList:

    def __init__(self,data,next):
        self.data=data
        self.next=next

class Node:
    def __init__(self,linkedListNode) -> None:
        self.linkedListNode=linkedListNode

    def __lt__(self,obj):
        return self.linkedListNode.data<obj.linkedListNode.data
	
	
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


def mergeKLists(listArray):
	nLinkedList = len(listArray)
	minHeap=Heap()
	for i in range(nLinkedList):
		node = Node(linkedListNode=listArray[i])
		minHeap.push(node)
	head,tail=None,None
	
	while minHeap.size!=0:
		if head is None:
			node = minHeap.top()
			head,tail=node.linkedListNode,node.linkedListNode
			minHeap.pop() 
			if tail.next is not None:
				node=Node(linkedListNode=tail.next)
				minHeap.push(node)
		else:
			node = minHeap.top()
			tail.next=node.linkedListNode
			tail=tail.next
			minHeap.pop()
			if tail.next is not None:
				node = Node(linkedListNode=tail.next)
				minHeap.push(node)

	return head


def get_linked_list(listData):
    head=None
    tail=None
    for data in listData:
        if head is None:
            node = LinkedList(data=data,next=None)
            head=node 
            tail=node 
        else:
            node = LinkedList(data=data,next=None)
            tail.next=node
            tail = tail.next
    return head 
            
def print_linked_list(linkedList):
    while linkedList is not None:
        print(linkedList.data,end=" ")
        linkedList=linkedList.next




if __name__=="__main__":
	data=[[4,6,8],[2,5,7],[1,9]]
	arr = []
	for ele in data:
		node = get_linked_list(listData=ele)
		arr.append(node)
	head =  mergeKLists(listArray=arr)
	print_linked_list(linkedList=head)