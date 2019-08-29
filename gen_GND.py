def generate_Gardens(g):
	g.add_bi_path(['T15', 'GND1', 'GND2_L','GND4','GND5','GND6','GND7','T16'])
	
	g.add_edge('GND1','GND6',req='(INV|HJ)')
	g.add_edge('GND6','GND1')
	
	g.add_bi_edge('GND2_L','GND3')
	
	g.add_edge('GND2_L','GND2_R', req='(CW|INV|HJ)') #TODO: can ACC&DJ cross?
	g.add_edge('GND2_R','GND2_L', req='(CW|INV|HJ)') #TODO: can DJ alone get back?
	
	g.add_bi_path(['GND2_R','GND8','GND9','GND10','GND11','GND12','GND13','GND15','GND16','GND17','T23'])
	g.add_bi_edge('GND16','T22')
	g.add_bi_edge('GND13','GND18')
	g.add_bi_edge('GND18','T9')
	
	g.add_bi_edge('GND13','GND14')