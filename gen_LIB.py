	#Livre Ex Machina
def generate_Livre(g):	
	g.add_bi_path(['T21','LIB1','LIB2','LIB3','LIB4','LIB6','LIB7','LIB9','LIB10','LIB11','LIB12','Andrealphus'])
	g.add_bi_edge('LIB4','LIB5')
	g.add_bi_edge('LIB7','LIB8')
	
	g.add_bi_edge('LIB1', 'LIB8', req='LIB8_SWITCH')

	g.add_attribute('LIB8', {'key':'LIB8_SWITCH'})
	
	g.add_bi_edge('LIB10','LIB13')
	g.add_bi_edge('LIB13','LIB13_1', req='(RR|DS)')
	g.add_bi_edge('LIB7_1','LIB13')
	
	g.add_edge('LIB7','LIB7_1', req='(DJ|INV|HJ|RR|DS)')
	g.add_edge('LIB7_1','LIB7')
	
	g.add_bi_edge('LIB7_1','LIB19')
	
	g.add_edge('LIB19','LIB19_1', req='(RR|DS|INV|HJ)') #TODO: inv works?
	g.add_edge('LIB19_1','LIB19')
	
	g.add_bi_edge('LIB19_1','LIB20')
	g.add_bi_edge('LIB20','LIB21')
	
	g.add_bi_edge('LIB20','LIB20_1', req='CW')
	g.add_bi_edge('LIB20_1','LIB22',req='LIB21_SWITCH')
	g.add_attribute('LIB20_1', {'key':'LIB20_1_SWITCH'})
	
	g.add_bi_edge('LIB10','LIB14')
	
	g.add_bi_edge('LIB14','LIB14_1',req='(RR|DS)')
	
	g.add_bi_path(['LIB14_1','LIB15', 'LIB16','LIB17','LIB18'])
	
	g.add_bi_edge('LIB18','LIB18_1',req='(RR|DS)')
	
	g.add_bi_star('LIB24',['LIB23','LIB25','LIB26'])
	
	g.add_bi_path(['LIB26','LIB20','LIB27','LIB31','LIB32','LIB37','LIB36','LIB35','LIB34','LIB33','LIB30_1'])
	
	g.add_edge('LIB30_1', 'LIB30')
	g.add_edge('LIB30', 'LIB30_1', req='(RR|DS|INV)') #TODO: verify HJ can't pass
	
	g.add_bi_edge('LIB30','LIB23_1')
	g.add_edge('LIB23_1','LIB23') #fall down to dragon
	g.add_edge('LIB25','LIB23') #fall down to dragon
	g.add_bi_edge('LIB23_1', 'LIB25', req='LIB23_1_SWITCH')
	g.add_attribute('LIB23_1', {'key':'LIB23_1_SWITCH'})
	
	g.add_bi_path(['LIB23_1','LIB28','LIB29'])
	
	g.add_bi_edge('LIB29','LIB29_1', req='LIB29_1_SWITCH')
	g.add_bi_edge('LIB29_1', 'T19')
	g.add_attribute('LIB29_1', {'key':'LIB29_1_SWITCH'})
	
	g.add_bi_path(['LIB38','LIB37','LIB39','LIB43','AbyssalGuardian','LIB44','T20'])
	
	g.add_bi_edge('LIB37','LIB42')
	g.add_bi_edge('LIB39','LIB40')
	g.add_bi_edge('LIB35','LIB41', req='LIB35_SWITCH')
	g.add_attribute('LIB35', {'key':'LIB35_SWITCH'})
	
	g.add_attribute('AbyssalGuardian', {'key':'ABYSSALGUARDIAN_DEAD'})
	g.add_attribute('Andrealphus', {'key':'ANDREALPHUS_DEAD'})