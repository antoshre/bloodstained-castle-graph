def generate_ForbWaterWay(g):
	g.add_bi_edge('T2','UGD1')
	g.add_edge('UGD1','UGD1-2', req='SWIM') #Aqua Stream
	g.add_edge('UGD1-2','UGD1')
	g.add_bi_edge('UGD1','UGD2',req='AS|SWIM')
	
	g.add_bi_edge(['UGD2','UGD3','UGD4'])
	
	g.add_edge('UGD4-1','UGD4',req='(RR|DS|DJ|INV|HJ)')
	g.add_edge('UGD4','UGD4-1')
	
	g.add_bi_edge('UGD4-1','UGD6')
	g.add_edge('UGD6','UGD6-1')
	g.add_edge('UGD6-1','UGD6',req='(RR|DS|DJ|INV|HJ)')
	
	g.add_bi_edge('UGD6-1','UGD7')
	g.add_bi_edge('UGD6-1','UGD8')
	g.add_bi_edge('UGD8','UGD9')
	g.add_bi_edge('UGD9','UGD10')
	
	g.add_edge('UGD9','UGD9-1')
	g.add_edge('UGD9-1','UGD9', req='(RR|DJ|INV|HJ)')
	
	g.add_edge('UGD9-1','UGD9-2', req='(SWIM)')
	g.add_edge('UGD9-2','UGD9-1')
	
	g.add_bi_edge('UGD9-1','UGD11')
	g.add_bi_edge('UGD11','UGD12')
	
	g.add_edge('UGD11','UGD13',req='(AS|SWIM)')
	g.add_edge('UGD13','UGD11')
	
	g.add_edge('UGD11','UGD11-1',req='SWIM')
	g.add_edge('UGD11-1','UGD11')
	
	g.add_edge('UGD11','UGD14-R', req='(AS|SWIM)')
	g.add_edge('UGD14-R','UGD11', req='(AS|SWIM)')
	
	g.add_bi_edge('UGD14-R','UGD14-L',req='(RR|DS)')
	
	g.add_bi_edge('UGD14-L','UGD15',req='(AS|SWIM)')
	
	g.add_edge('UGD15','UGD15-1', req='(RR|DS|DJ|INV|HJ)')
	g.add_edge('UGD15-1','UGD15')
	
	g.add_edge('UGD15','UGD15-2',req='(RR|DS)')
	g.add_edge('UGD15-2','UGD15')
	
	g.add_bi_edge('UGD4-1','UGD16')
	g.add_edge('UGD16','UGD16-1',req='((ACC&DJ)|INV|HJ)')
	g.add_edge('UGD16-1','UGD16')
	
	g.add_bi_path(['UGD17','UGD19','UGD20','UGD21','UGD22'])
	g.add_edge('UGD22','UGD22-1', req='(RR|DS)')
	
	g.add_bi_edge('UGD17','UGD18')
	
	g.add_bi_edge('UGD22-1','UGD23-L')
	
	g.add_bi_edge('UGD23-L','UGD23-R', key='UGD23_R_SWITCH')
	
	g.add_bi_edge('UGD21','UGD24')
	
	g.add_edge('UGD24','UGD24-1',req='(AS|SWIM)')
	g.add_edge('UGD24-1','UGD24')
	
	g.add_bi_edge('UGD24-1','UGD25', req='(AS|SWIM)')
	g.add_bi_edge('UGD25','UGD26',req='(AS|SWIM)')
	g.add_bi_edge('UGD26','UGD27',req='(AS|SWIM)')
	g.add_bi_edge('UGD27','UGD28',req='(AS|SWIM)')
	g.add_bi_edge('UGD28','UGD29',req='(AS|SWIM)')
	g.add_bi_edge('UGD29','UGD30',req='(AS|SWIM)')
	g.add_bi_edge('UGD30','T8',req='(AS|SWIM)')
	