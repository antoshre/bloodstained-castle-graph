def generate_Den(g):
	#Den of Behemoths
	g.add_bi_edge('GND5','BIG1', req='(GEBEL_DEAD & ZANGETSUTO)')
	
	g.add_bi_path(['BIG3','BIG2','BIG1','BIG4','BIG5'])
	g.add_edge('BIG5','BIG6',req='(RR|DS|DJ|INV|HJ)')
	g.add_edge('BIG6','BIG5')
	
	g.add_edge('BIG5','BIG7')
	g.add_edge('BIG7','BIG5', req='(INV|HJ)')
	
	g.add_bi_edge('BIG7','BIG8')
	
	g.add_edge('BIG8','BIG8_1')
	g.add_edge('BIG8_1', 'BIG8', req='((ACC&DJ)|INV|HJ)')
	
	g.add_bi_edge('BIG8_1', 'BIG9')
	g.add_edge('BIG9','BIG9_1')
	g.add_edge('BIG9_1', 'BIG9', req='(RR|DS|DJ|INV|HJ)')
	
	g.add_bi_edge('BIG9_1', 'BIG10')