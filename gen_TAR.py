def generate_SecSorcLab(g):
	#Secret Sorcery Lab
	g.add_bi_path(['T4','TAR1','TAR2','TAR4','Doppelganger','TAR5'])
	g.add_bi_path(['TAR5-2','TAR7','TAR8','TAR9','T3'])
	
	g.add_bi_edge('TAR2','TAR3')
	
	g.add_edge('TAR5','TAR5-1',req='(RR|DS|DJ|INV|HJ)')
	g.add_edge('TAR5-1','TAR5')
	g.add_edge('TAR5-2','TAR5', req='(RR|DS|DJ|INV|HJ)')
	g.add_edge('TAR5','TAR5-2')
	
	
	g.add_bi_edge('TAR5-1','TAR6')
	g.add_bi_edge('TAR6','TAR6-1', req='(RR|DS|DJ|INV|HJ)') #spike room
	
	g.add_attribute('Doppelganger', {'key':'DOPPELGANGER_DEAD'})