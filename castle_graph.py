import networkx as nx
from itertools import tee

import custom_digraph

from gen_SIP import generate_Galleon_Minerva
from gen_VIL import generate_Arvantville
from gen_ENT import generate_Entrance
from gen_GND import generate_Gardens
from gen_TWR import generate_Towers
from gen_TRN import generate_Bridge
from gen_ARC import generate_UndSorcLab
from gen_JPN import generate_OriSorcLab
from gen_KNG import generate_Hall
from gen_SAN import generate_Cathedral
from gen_LIB import generate_Livre
from gen_TAR import generate_SecSorcLab
from gen_BIG import generate_Den
from gen_ICE import generate_Glac

def generate_castle_graph():
	g = custom_digraph.CustomDiGraph()
	
	generate_Galleon_Minerva(g)
	generate_Arvantville(g)
	generate_Entrance(g)
	generate_Gardens(g)
	generate_Towers(g)
	generate_Bridge(g)
	generate_UndSorcLab(g)
	generate_OriSorcLab(g)
	generate_Hall(g)
	generate_Cathedral(g)
	generate_Livre(g)
	generate_SecSorcLab(g)
	generate_Den(g)
	generate_Glac(g)
	
	#TERRIBLE HACK!
	#TODO: just linking the parts to get them on the same graph
	g.add_bi_edge('T4','T2')
	g.add_bi_edge('T24','BIG1')
	return g