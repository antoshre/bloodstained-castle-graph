def generate_Towers(g):
	#Towers of Twin Dragons
	
	g.add_bi_path(['T22','TWR1','TWR2','TwinDragons_2'])
	
	g.add_bi_path(['TWR1','TWR3','TWR4','TWR6','TWR7','T21'])
	g.add_bi_edge('TWR4','TWR5')
	
	g.add_bi_edge('TWR5','TWR2_1', req='TWR_ELEVATOR')
	g.add_bi_edge('TWR18','TWR2_2', req='TWR_ELEVATOR')
	g.add_bi_edge('TWR2','TWR2_1', req='TWR_ELEVATOR')
	g.add_bi_edge('TWR2_1','TWR2_2', req='TWR_ELEVATOR')
	g.add_bi_edge('TWR2_2','TWR2_3', req='TWR_ELEVATOR')
	g.add_attribute('TWR2_3', {'key':'TWR_ELEVATOR'})
	
	g.add_edge('TWR4','TWR8',req='(DJ|INV|HJ|RR|DS)')
	g.add_edge('TWR8','TWR4')
	
	g.add_bi_path(['TWR8','TWR9','TWR10','TWR11','TWR12','TWR2_3','TWR13','TWR14', 'TWR16','TWR17','TWR19','TwinDragons'])
	
	g.add_bi_edge('TwinDragons', 'TwinDragons_2', req='TWIN_DRAGONS_DEAD')
	
	
	g.add_edge('TwinDragons_2','TwinDragons_1', req='(INV|HJ)')
	g.add_edge('TwinDragons_1', 'TwinDragons_2')
	
	g.add_bi_edge('TWR17','TWR18')
	
	g.add_bi_edge('TWR19','TWR19_1', req='(DS)')
	
	#Tower attributes
	
	g.add_attribute('TwinDragons', {'key':'TWIN_DRAGONS_DEAD'})