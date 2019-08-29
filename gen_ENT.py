def generate_Entrance(g):
	#Entrance
	
	g.add_bi_path(['T1','ENT1','ENT4','ENT5','ENT8','ENT9','ENT11','ENT13','ENT14','T15'])
	
	g.add_edge('ENT1','ENT1_1',req='(INV|HJ)')
	g.add_edge('ENT1_1','ENT1')
	
	g.add_bi_star('ENT1_1',['ENT4','T12'])
	
	g.add_edge('ENT1_1', 'ENT1_2', req='(AP&CW&(DJ|INV|HJ))')
	g.add_edge('ENT1_2','ENT1_1', req='(AP&CW)')
	
	g.add_edge('ENT3','ENT1_2')
	g.add_edge('T10','ENT1_2')
	g.add_edge('ENT1_2','ENT3', req='(INV|HJ)')
	g.add_edge('ENT1_2','T10', req='(INV|HJ)')
	
	g.add_edge('ENT5','ENT5_1',req='(DJ|INV|HJ|RR|DS)')
	g.add_edge('ENT5_1','ENT5')
	g.add_bi_edge('ENT5_1','ENT6')
	g.add_edge('ENT6','ENT6_1', req='(DJ|INV|HJ|RR|DS)')
	g.add_edge('ENT6_1','ENT6')
	g.add_bi_edge('ENT6_1','ENT7')
	
	g.add_bi_edge('ENT9','ENT10')
	g.add_edge('ENT9','ENT12',req='(BS)')
	g.add_edge('ENT12','ENT9') #TODO: check what happens if approach from beneath without BS
	g.add_bi_edge('T5','ENT12')
	
	g.add_edge('ENT13','ENT13_1', req='(DJ|INV|HJ|RR|DS)')
	g.add_edge('ENT13_1','ENT13')
	g.add_bi_edge('ENT13_1','ENT15')
	
	g.add_bi_path(['T16','ENT13_1','ENT16','ENT17','ENT18','ENT21','T13'])
	
	g.add_bi_star('ENT18', ['ENT19','ENT20'])
	
	g.add_edge('ENT18', 'ENT22', req='(CW|DJ|INV|HJ)') #TODO: check if this can be jumped over, RR, DS?
	g.add_edge('ENT22','ENT18')
	g.add_bi_path(['ENT22','ENT23','T17'])
	g.add_bi_edge('ENT23','ENT24')
	
	g.add_bi_edge('ENT13','T14',req='ENT_FUW_SWITCH')
	
	g.add_bi_edge('T14','ENT25')
	
	#Entrance attributes
	g.add_attribute('T14', {'key':'ENT_FUW_SWITCH'}) #Trigger switch from T14 side