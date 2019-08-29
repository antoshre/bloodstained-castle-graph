import networkx as nx

from collections import defaultdict
from itertools import tee
#from itertools recipe
def pairwise(iterable):
	"s _> (s0,s1), (s1,s2), (s2, s3), ..."
	a, b = tee(iterable)
	next(b, None)
	return zip(a, b)

class CustomDiGraph(nx.DiGraph):
	def __init__(self, *args, **kargs):
		super().__init__(*args, **kargs)
	#Add bi-directional path to graph
	#['1','2','3',...,'n'] -> add_bi_edge('1','2'), add_bi_edge('2','3'), add_bi_edge('3,'4')...
	def add_bi_path(self, path):
		for n1,n2 in pairwise(path):
			self.add_bi_edge(n1,n2)
	#Add bi-directional edge between nodes
	#Supports duplicate attribute assignment on edges
	def add_bi_edge(self, n1, n2, *args, **kargs):
		self.add_edge(n1, n2, *args, **kargs)
		self.add_edge(n2, n1, *args, **kargs)
	#Add bi-directional edges between star and others
	#['1', ['2','3','4']] -> bi_edge('1','2'), bi_edge('1','2'), bi_edge('1','3'), bi_edge('1','4')
	def add_bi_star(self, star, others):
		for node in others:
			self.add_bi_edge(star, node)
	#Set node attribute
	#Overrites existing attributes!
	#Attr is a dict: {key : value}
	def set_attribute(self, node, attr):
		for k,v in attr.items():
			nx.set_node_attributes(self, {node : v}, k)
	#Adds attribute to list if same key exists
	def add_attribute(self, node, attr):
		merged = defaultdict(list)
		ndata = self.node[node]
		for d in (attr, ndata):
			for k,v in d.items():
				if isinstance(v, list):
					for x in v:
						merged[k].append(x)
				else:
					merged[k].append(v)
		#write this back over existing data
		self.set_attribute(node, merged)
		
	#Breadth-first search of the castle graph, taking edge requirements and game state into account
	#Must be repeatedly run until the game state indicates no progression has been made
	#acceptance: function run on each edge.  True->accept, False->reject
	#foreach: function run on each accepted node and any data attached to that node
	def BFS(self, root, acceptance=lambda x: True, foreach=lambda x,y: None):
		#visited = defaultdict(bool)
		visited = {}
		for node in self.nodes():
			visited[node] = False
		
		queue = []
		queue.append(root)
		visited[root] = True
		
		while queue:
			cur = queue.pop(0)
			for adj in self.neighbors(cur):
				if not visited[adj]:
					if acceptance( self.get_edge_data(cur, adj, default={}) ):
						visited[adj] = True
						queue.append(adj)
						foreach(adj, self.node[adj])