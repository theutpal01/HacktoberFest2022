```
  "Kosaraju's algorithm" 

A directed graph is strongly connected if there is a path between 
all pairs of vertices. A strongly connected component (SCC) of a 
directed graph is a maximal strongly connected subgraph.
```

# Python implementation of Kosaraju's algorithm to print all SCCs

from collections import defaultdict

#This class represents a directed graph using adjacency list representation
class Graph:

	def __init__(self,vertice):
		self.V= vertice #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph

	# function to add an edge to graph
	def add_edge(self,u,v):
		self.graph[u].append(v)

	# A function used by DFS
	def DFS_Util(self,v,visited):
		# Mark the current node as visited and print it
		visited[v]= True
		print (v)
		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.DFS_Util(i,visited)


	def fill_order(self,v,visited, stack):
		# Mark the current node as visited
		visited[v]= True
		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.fill_order(i, visited, stack)
		stack = stack.append(v)
	

	# Function that returns reverse (or transpose) of this graph
	def get_transpose(self):
		g = Graph(self.V)

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph:
			for j in self.graph[i]:
				g.add_edge(j,i)
		return g



	# The main function that finds and prints all strongly
	# connected components
	def print_SCC(self):
		
		stack = []
		# Mark all the vertices as not visited (For first DFS)
		visited =[False]*(self.V)
		# Fill vertices in stack according to their finishing
		# times
		for i in range(self.V):
			if visited[i]==False:
				self.fill_order(i, visited, stack)

		# Create a reversed graph
		gr = self.get_transpose()
		
		# Mark all the vertices as not visited (For second DFS)
		visited =[False]*(self.V)

		# Now process all vertices in order defined by Stack
		while stack:
			i = stack.pop()
			if visited[i]==False:
				gr.DFS_Util(i, visited)
				print("")

# Create a graph given in the above diagram
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)


print ("Following are strongly connected components " +
						"in given graph")
g.print_SCC()
