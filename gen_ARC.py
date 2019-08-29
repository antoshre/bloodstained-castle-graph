def generate_UndSorcLab(g):
	#Underground Sorcery Lab
	
	g.add_bi_path(['T25','ARC1','ARC2','ARC3','Bathin','ARC6'])
	g.add_edge('ARC3','ARC4',req='(DJ|INV|HJ|RR|DS)')
	g.add_edge('ARC4','ARC3')
	g.add_bi_edge('ARC4','ARC5')
	g.add_bi_edge('ARC6','ARC6_1', req='(RR|DS)')
	g.add_edge('ARC6','ARC7')
	g.add_edge('ARC7','ARC6', req='(DJ|INV|HJ|RR|DS)')
	
	g.add_attribute('Bathin', {'key':'BATHIN_DEAD'})