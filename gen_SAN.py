def generate_Cathedral(g):
	#Cathedral
	
	g.add_bi_path(['T13','SAN1','SAN3','SAN4','SAN5','SAN6','SAN7','SAN8','SAN9','Craftwork'])
	g.add_bi_star('Craftwork',['SAN10','SAN11'])
	g.add_bi_path(['SAN8','SAN12','T17'])
	g.add_bi_path(['SAN1','SAN2','T12'])
	
	g.add_bi_edge('SAN4','SAN4_3', req='(RR|DS)')
	
	g.add_edge('SAN4','SAN4_1', req='(RR|DS|DJ|INV|HJ)')
	g.add_edge('SAN4_1','SAN4')
	
	#TODO: 4_1 to 4_2?
	
	g.add_bi_path(['SAN4_1','SAN13','SAN14','SAN15','SAN16','SAN18','SAN19','SAN20','Bloodless','SAN21','T19'])
	
	g.add_bi_edge('SAN14','SAN17')
	#TODO: SAN17 <_> SAN16 switch situation
	
	g.add_bi_edge('SAN16','SAN8_1')
	
	g.add_bi_edge('SAN8','SAN8_1',req='SAN8_1_SWITCH')
	g.add_attribute('SAN8_1', {'key':'SAN8_1_SWITCH'})
	
	g.add_edge('SAN19','SAN19_1',req='(INV|HJ)') #TODO: DJ? RR? DS?
	g.add_edge('SAN19_1','SAN19')
	
	g.add_bi_edge('SAN19_1','T18')
	
	g.add_attribute('Craftwork', {'key':'CRAFTWORK_DEAD'})
	g.add_attribute('Bloodless', {'key':'BLOODLESS_DEAD'})