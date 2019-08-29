#Inferno Cave
def generate_Inferno(g):
	g.add_bi_edge('T3','RVA1')
	
	g.add_edge('RVA1','RVA1-2')
	g.add_edge('RVA1-2','RVA1', req='(RR|DS|DJ|INV|HJ)')
	
	g.add_bi_edge('RVA1-2','RVA2')
	
	g.add_edge('RVA2','RVA2-1', req='(RR|DS|DJ|INV|HJ)')
	g.add_edge('RVA2-1','RVA2')
	g.add_edge('RVA2','RVA2-2', req='(INV&(RR|DS))')
	g.add_edge('RVA2-2','RVA2')
	
	g.add_bi_edge('RVA2','RVA3')
	
	g.add_bi_edge('RVA3','RVA3-1', req='(RR|DS|INV)')
	
	g.add_bi_edge('RVA3','RVA4')
	
	g.add_bi_edge('RVA4','RVA5')
	
	g.add_edge('RVA5','RVA5-1', req='(RR|DS|DJ|INV|HJ)')
	g.add_edge('RVA5-1','RVA5')
	g.add_bi_edge('RVA5-1','RVA5-2', req='(RR|DS|DJ|INV|HJ)')
	g.add_bi_edge('RVA5-2','RVA5-3', req='(RR|DS|INV)')
	
	g.add_bi_edge('RVA5-3','RVA6')
	g.add_edge('RVA6','RVA6-1', req='(INV)')
	g.add_edge('RVA6-1','RVA6', req='(RR|DS|INV)')
	
	g.add_bi_edge('RVA6','RVA8')
	
	g.add_bi_edge('RVA8','RVA9')
	g.add_bi_edge('RVA9','RVA10')
	
	g.add_edge('RVA10','RVA10-1',req='(RR&DJ)|INV|HJ') #TODO: check with RR level 1
	g.add_edge('RVA10-1','RVA10')
	
	g.add_edge('RVA10-1','RVA10-2',req='(RR|INV|HJ)') #TODO: check RR level 1
	g.add_edge('RVA10-2','RVA10-1')
	
	g.add_bi_edge('RVA10-2','RVA11')
	g.add_edge('RVA11','RVA11-1',req='(RR|DS|INV)')
	g.add_edge('RVA11-1','RVA11', req='(RR|DS|INV)')
	
	g.add_edge('RVA11','RVA11-2')
	g.add_edge('RVA11-2','RVA11',req='(INV|HJ)')
	
	g.add_edge('RVA11-2','RVA11-3',req='(RR|INV|HJ)')
	g.add_edge('RVA11-3','RVA11-2') 
	
	g.add_bi_edge('RVA11-2','RVA12')
	g.add_edge('RVA12','RVA12-1',req='(ACC|RR|DS|DJ|INV|HJ)')
	g.add_edge('RVA12-1','RVA12')
	
	g.add_bi_edge('RVA12-1','RVA13')
	g.add_edge('RVA13','RVA13-1',req='(INV|HJ)')
	g.add_edge('RVA13-1','RVA13')
	
	g.add_bi_edge('RVA13','RVA14')
	
	g.add_bi_path(['RVA13-1','T6','RVA15','RVA16'])
	
	g.add_edge('RVA16','RVA16-2')
	g.add_edge('RVA16-2','RVA16', req='(INV)')
	
	g.add_bi_edge('RVA5-1','RVA17')
	
	