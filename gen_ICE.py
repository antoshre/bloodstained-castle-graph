	#Glacial Tomb
def generate_Glac(g):
	
	g.add_bi_path(['T24','ICE1','ICE2','ICE3','ICE5','ICE6','ICE8','ICE9','ICE10'])
	
	g.add_bi_edge('ICE3','ICE4')
	g.add_bi_edge('ICE6','ICE7')
	
	g.add_edge('ICE9','ICE9_1')
	g.add_edge('ICE9_1','ICE9', req='(RS|DS|DJ|INV|HJ)')
	g.add_bi_edge('ICE9_1','ICE11')
	
	g.add_edge('ICE9_1','ICE12')
	g.add_edge('ICE12','ICE9_1', req='(RR|DS|DJ|INV|HJ)')
	
	g.add_edge('ICE12','ICE13')
	g.add_edge('ICE13','ICE12', req='(DS|INV|HJ)')
	
	g.add_bi_star('ICE14', ['ICE13','ICE15','Gremory'])
	
	g.add_bi_edge('ICE9_1','ICE16_R')
	g.add_bi_edge('ICE16_R','ICE16_L', req='(DS)')
	g.add_bi_edge('ICE16_L','ICE17')
	
	g.add_bi_edge('ICE17','ICE17_1', req='(RR|DS)')
	
	g.add_bi_star('ICE18',['ICE17_1','Dominique'])
	
	g.add_attribute('Dominique', {'key':'GAME_COMPLETE'})
	
	g.add_attribute('Gremory', {'key':'GREMORY_DEAD'})