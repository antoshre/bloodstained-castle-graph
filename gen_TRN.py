def generate_Bridge(g):
	#Bridge Of Evil
	
	g.add_bi_path(['T23','TRN1','TRN2'])
	g.add_bi_edge('TRN2','TRN3', req='(Passplate)')
	g.add_bi_edge('TRN3','GluttonTrain')
	g.add_bi_edge('GluttonTrain', 'TRN4', req='(Passplate)')
	g.add_bi_path(['TRN4','TRN5','TRN6','T25'])
	
	g.add_attribute('GluttonTrain', {'key':'GLUTTONTRAIN_DEAD'})