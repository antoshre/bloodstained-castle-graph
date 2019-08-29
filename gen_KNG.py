def generate_Hall(g):
	#Hall Of Termination
	
	g.add_bi_path(['T20','KNG1','KNG3','KNG4','KNG5','KNG6','KNG7','KNG8','KNG9','KNG10','KNG11','KNG12','KNG15','KNG16','KNG20','KNG21'])
	#TODO: KNG16 _> KNG20 without DJ or better?
	
	g.add_bi_edge('KNG1','KNG2')
	g.add_bi_edge('KNG2','KNG15', req='(KNG15_SWITCH)')
	g.add_attribute('KNG15', {'key':'KNG15_SWITCH'})
	
	g.add_bi_edge('KNG10','T18')
	g.add_bi_star('KNG12',['KNG13','KNG14'])
	
	g.add_edge('KNG14', 'KNG14_1', req='(DJ|INV|HJ)') #TODO: RR or DS?
	g.add_edge('KNG14_1', 'KNG14')
	g.add_bi_edge('KNG16','KNG17')
	g.add_bi_star('KNG18',['KNG16','KNG19'])
	
	g.add_edge('KNG18','KNG18_1', req='(INV|HJ)') #TODO: accel + dj?
	g.add_edge('KNG18_1', 'KNG18')
	
	g.add_bi_edge('KNG19', 'Gebel', req='ZANGETSUTO & ZANG2_DEAD') #TODO: if you get the sword early, wtf happens?  Is beating Zang2 a hard requirement?
	
	g.add_attribute('Gebel', {'key':'GEBEL_DEAD'})