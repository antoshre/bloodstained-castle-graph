def generate_OriSorcLab(g):
	#Oriental Sorcery Lab
	
	g.add_bi_path(['T10','JPN1','JPN2','JPN3','JPN4'])
	
	g.add_bi_edge('JPN2','JPN2_1', req='(DS)')
	
	g.add_bi_edge('JPN2','JPN2_2', req='(DS)')
	
	g.add_bi_path(['JPN3','JPN9','T11'])
	
	g.add_bi_edge('JPN4','JPN5')
	
	g.add_edge('JPN4','JPN6', req='(INV|HJ)') #TODO: investigatee JPN4 reqs
	g.add_edge('JPN6','JPN4')
	
	g.add_edge('JPN4','JPN7', req='(INV|HJ)')
	g.add_edge('JPN7','JPN4')
	g.add_bi_edge('JPN7','JPN8')
	
	g.add_edge('JPN4','JPN10', req='(INV|HJ)') #TODO: easier req?
	g.add_edge('JPN10','JPN4')
	
	g.add_bi_edge('JPN10','JPN11')
	
	g.add_bi_edge('JPN10','JPN10_1', req='(RR|DS|INV)')
	
	g.add_edge('JPN10','JPN10_2', req='(RR|DS|DJ|INV|HJ)')
	g.add_edge('JPN10_2','JPN10')
	
	g.add_bi_edge('JPN10_1','JPN13')
	
	g.add_edge('JPN13','JPN13_1', req='(RR|DS|DJ|INV|HJ)')
	g.add_edge('JPN13_1','JPN13')
	
	g.add_bi_path(['JPN13_1','JPN14','JPN15','JPN17','JPN18'])
	g.add_edge('JPN18','JPN18_1',req='(RR|DS|DJ|INV|HJ)')
	g.add_edge('JPN18_1', 'JPN18')
	
	g.add_bi_edge('JPN18_1', 'Zang2')
	g.add_bi_edge('JPN15','JPN16')
	
	g.add_attribute('Zang2', {'key':'ZANG2_DEAD'})