import networkx as nx

import logging
import re
import sys
import os
import random

import castle_graph

module = sys.modules['__main__'].__file__
log = logging.getLogger(module)

class GameChecker():
	def __init__(self):
		self.Castle = castle_graph.generate_castle_graph()	
		
		if not nx.is_strongly_connected(self.Castle):
			print("Castle graph is malformed! Not strongly connected!")
			s = nx.strongly_connected_components(self.Castle)
			for g in s:
				print(g)
			sys.exit(0)
		self.State = GameState( self._get_progression_keys() )
		
		print("Castle has {} nodes".format( len(self.Castle.nodes())))
		
	#Extract progression keys from the edge requirements and node 'key' triggers
	def _get_progression_keys(self):
		#Get the strings on each edge
		raw_edge_reqs = [req for _,req in nx.get_edge_attributes(self.Castle, 'req').items()]
		#Get the contents of 'key' for each node dict, it's a list
		raw_node_keys = [key for _,key in nx.get_node_attributes(self.Castle, 'key').items()]
		
		#flatten list-of-lists to a list, set to make unique
		all_keys = set( sum(raw_node_keys, []) )
		
		#Use regex to isolate terms from req string
		delimiters = ' ', '&', '|', '(', ')'
		regex = '|'.join(map(re.escape, delimiters))
		for reqstr in raw_edge_reqs:
			terms = re.split(regex, reqstr)
			for t in terms:
				if len(t) > 0:#Eliminate empty strings
					all_keys.add(t)
		return all_keys
		
	#Given a config, check if it's possible to reach GAME_COMPLETE
	#config = {node_name : value} dict
	#ie {'SIP0' : 'DJ', 'SIP1' : 'INV'}	
	def verify(self, config):
		log.debug("Applying config:")
		for k,v in config.items():
			log.debug("\t{}\t{}".format(k,v))
			self.Castle.add_attribute(k, {'key':v})
			
		self.State.made_progress = True #Make it through the first while condition
		
		iter = 0
		log.debug("Starting config verification...")
		while self.State.made_progress:
			iter += 1
			self.State.made_progress = False
			log.debug("Iter {}".format(iter))
			if self.State.Keys['GAME_COMPLETE']:
				log.debug("Success")
				return True
			self.Castle.BFS('SIP000_Tutorial', acceptance=self.State.eval_edge, foreach=self.State.visit_node)
			
			log.debug("End of iter {}".format(iter))
		else:
			#log.info("Configuration failed")
			#log.info(config)
			return False
	
	
	
class GameState():
	def __init__(self, state_vars):
		self.Keys = {}
		#Set up all variables as dictated by the checker
		log.debug("Initializing game state with attributes:")
		for name in state_vars:
			log.debug(name)
			self.Keys[name] = False
			
		self.made_progress = False
	def eval_edge(self, edge_data):
		if 'req' not in edge_data: #If there is no req...
			return True
		#log.debug("Evaluating {}".format( edge_data['req']))
		#Move self.Keys keys into local variable context
		for k,v in self.Keys.items():
			#log.debug("Exec'ing '{} = {}'".format(k,v))
			exec("{} = {}".format(k,v))
		
		return eval(edge_data['req'])
	def visit_node(self, node, data):
		log.debug("Visiting {}".format(node))
		if 'key' in data: #Does the node have a key item?
			for k in data['key']:
				if self.Keys[k] == False: #Is this a new key item?
					log.debug("\tFound: {}".format(k))
					self.Keys[k] = True #Add it
					self.made_progress = True #Indicate progress has been made
	def __str__(self):
		s = "GameState("
		for k,v in self.Keys.items():
			if v:
				s += "{}:{}, ".format(k,v)
		return s + ")"

class ConfigurationGenerator():
	def __init__(self, verbose=False, seed=os.urandom(64)):
		self.verbose = verbose
		self.seed = seed
		
		self.checker = GameChecker()
		
		self.All_keys = self.checker.State.Keys.keys()
		
		badnames = [
			'_DEAD',
			'_SWITCH',
			'_ELEVATOR',
			'_COMPLETE',
			'VillageKey',
			'PhotoID',
		]
		self.Locked = set()
		for key in self.All_keys:
			for name in badnames:
				if name in key:
					self.Locked.add(key)
		self.To_randomize = self.All_keys - self.Locked
		
		log.debug("Progression keys: {}".format(self.All_keys))
		log.debug("Locked keys: {}".format(self.Locked))
		log.debug("To be randomized: {}".format(self.To_randomize))
		
	def generate_unchecked_config(self):
		nodes = random.sample(self.get_valid_nodes_for_randomizer(), len(self.To_randomize))
		return dict(zip(nodes, self.To_randomize))
	def generate_config(self, max_iter=500):
		
		random.seed(self.seed)
		
		iter = 0
		while (iter < max_iter):
			iter += 1
			conf = self.generate_unchecked_config()
			
			
			if self.checker.verify(conf):
				log.info("Good config found after {} iterations".format(iter))
				return conf
			else:
				log.debug("Bad config, retrying")
		else:
			log.warn("{} iterations reached".format(iter))
			return None
			
	#Get nodes that are valid places to assign progression items.
	def get_valid_nodes_for_randomizer(self):
		#get all nodes
		nodes = self.checker.Castle.nodes()
		
		#Drop transition rooms, named T1, T2, etc
		regex = re.compile(R"T[\d]+")
		nodes = [n for n in nodes if not regex.match(n)]
		
		log.info("{} nodes valid for randomization".format(len(nodes)))
		return nodes
		

if __name__ == '__main__':
	import argparse
	
	parser = argparse.ArgumentParser(
		description=module,
		usage="%(prog)s"
	)
	
	parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
						
	args = parser.parse_args()
	if (args.verbose):
		logging.basicConfig(level=logging.DEBUG)
	
	

	confgen = ConfigurationGenerator()
	print(confgen.generate_config(max_iter=100))