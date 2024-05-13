
from typing import List,Dict,Tuple
import heapq

class Node:
    def __init__(self,distance:int,node:int) -> None:
        self.distance:int=distance
        self.node:int=node
    def __repr__(self):
        return f"Node(distance={self.distance},node={self.node})"

    def __lt__(self,obj):
        return self.distance<obj.distance

class Heap:

	def __init__(self):
		self.arr:List[Node]=[]
	
	def push(self,item:Node):
		heapq.heappush(self.arr,item)
	
	def pop(self):
		return heapq.heappop(self.arr)
	
	@property
	def size(self):
		return len(self.arr)
	
	def top(self):
		if self.size>0:
			return self.arr[0]



def prepareAdjList(vertices:int,vec:List[List[int]],adjList:Dict[int,Tuple[int,int]]):
    """
    vec:[[0,1,2],[0,1,2]]
    """
    for v in range(vertices):
        adjList[v]=list()
    for item in vec:
        srcNode,dstNode,dist = item[0],item[1],item[2]
        adjList[srcNode].append(Node(distance=dist,node=dstNode))
        adjList[dstNode].append(Node(distance=dist,node=srcNode))
        
        

def dijkstra(vec, vertices, edges, source):
    adjList=dict()
    distance=[]
    for i in range(vertices):
        distance.append(float('inf'))

    prepareAdjList(vertices,vec,adjList)
    
    minHeap = Heap()
    node = Node(distance=0,node=source)
    minHeap.push(node) 
    distance[source]=0
    while minHeap.size!=0:
        minNode:Node = minHeap.pop()
       
        for neighbour in adjList[minNode.node]:
            if minNode.distance+neighbour.distance<distance[neighbour.node]:
                while neighbour in minHeap.arr:
                    minHeap.arr.remove(neighbour)
                distance[neighbour.node]=minNode.distance+neighbour.distance
                #minHeap.push(neighbour)
                minHeap.push(item=Node(distance=distance[neighbour.node],
                                       node=neighbour.node
                                       )
                             )

    return distance


if __name__=="__main__":
    vec = [[0, 1, 5], [0, 2, 8], [1, 2, 9], [1, 3, 2], [2, 3, 6]]
    edges=5
    source=0
    vertices=4
    #vec = [[0, 1, 5], [0, 2, 8], [1, 2, 9], [1, 3, 2], [2, 3, 6]]
    
    print(dijkstra(vec,vertices=vertices,edges=edges,source=source))