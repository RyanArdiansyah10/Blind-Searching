class adjacent_Node:
	
	def __init__(self, v):
		
		self.vertex = v
		self.next = None


class bidirectional_Search:
	
	def __init__(self, vertices):
		
		self.vertices = vertices
		self.graph = [None] * self.vertices
		
		self.src_queue = list()
		self.dest_queue = list()
		
		
		self.src_visited = [False] * self.vertices
		self.dest_visited = [False] * self.vertices
		
		
		self.src_parent = [None] * self.vertices
		self.dest_parent = [None] * self.vertices
		
	
	def AddEdge(self, src, dest):
		
		node = adjacent_Node(dest)
		node.next = self.graph[src]
		self.graph[src] = node

		node = adjacent_Node(src)
		node.next = self.graph[dest]
		self.graph[dest] = node
		
	
	def breadth_fs(self, direction = 'forward'):
		
		if direction == 'forward':
		
			current = self.src_queue.pop(0)
			connected_node = self.graph[current]
			
			while connected_node:
				vertex = connected_node.vertex
				
				if not self.src_visited[vertex]:
					self.src_queue.append(vertex)
					self.src_visited[vertex] = True
					self.src_parent[vertex] = current
					
				connected_node = connected_node.next
		else:
			
			current = self.dest_queue.pop(0)
			connected_node = self.graph[current]
			
			while connected_node:
				vertex = connected_node.vertex
				
				if not self.dest_visited[vertex]:
					self.dest_queue.append(vertex)
					self.dest_visited[vertex] = True
					self.dest_parent[vertex] = current
					
				connected_node = connected_node.next
				
	
	def is_intersecting(self):
		
		#
		for i in range(self.vertices):
			if (self.src_visited[i] and
				self.dest_visited[i]):
				return i
				
		return -1

	
	def path_st(self, intersecting_node,
				src, dest):
						
	
		path = list()
		path.append(intersecting_node)
		i = intersecting_node
		
		while i != src:
			path.append(self.src_parent[i])
			i = self.src_parent[i]
			
		path = path[::-1]
		i = intersecting_node
		
		while i != dest:
			path.append(self.dest_parent[i])
			i = self.dest_parent[i]
			
		print("*****Path*****")
		path = list(map(str, path))
		
		print(' '.join(path))
	
	def bidirectional_search(self, src, dest):
		
		self.src_queue.append(src)
		self.src_visited[src] = True
		self.src_parent[src] = -1
		
		self.dest_queue.append(dest)
		self.dest_visited[dest] = True
		self.dest_parent[dest] = -1

		while self.src_queue and self.dest_queue:
			
		
			self.breadth_fs(direction = 'forward')
			
			self.breadth_fs(direction = 'backward')
				
			intersecting_node = self.is_intersecting()
			
			if intersecting_node != -1:
				print("Path exists between {} and {}".format(src, dest))
				print("Intersection at : {}".format(intersecting_node))
				self.path_st(intersecting_node,
								src, dest)
				exit(0)
		return -1


if __name__ == '__main__':
	
	n = 15
	
	src = 0
	
	dest = 6
	
	graph = bidirectional_Search(n)
	graph.AddEdge(0, 4)
	graph.AddEdge(1, 4)
	graph.AddEdge(2, 5)
	graph.AddEdge(3, 5)
	graph.AddEdge(4, 6)
	graph.AddEdge(5, 6)
	graph.AddEdge(6, 7)
	graph.AddEdge(7, 8)
	graph.AddEdge(8, 9)
	graph.AddEdge(8, 10)
	graph.AddEdge(9, 11)
	graph.AddEdge(9, 12)
	graph.AddEdge(10, 13)
	graph.AddEdge(10, 14)
	
	out = graph.bidirectional_search(src, dest)
	
	if out == -1:
		print("No path between {} and {}".format(src, dest))