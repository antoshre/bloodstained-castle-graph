def generate_Galleon_Minerva(g):
	count = g.number_of_nodes()
	#Galleon Minerva
	g.add_bi_path(['SIP000_Tutorial','SIP000','SIP001','SIP002','SIP003','SIP005','SIP006','SIP008'])
	g.add_bi_path(['SIP008-1','SIP009','SIP010','SIP011','SIP012','SIP013','SIP014','SIP015','SIP016','SIP017','SIP018','SIP019','SIP020','Vepar'])
	
	g.add_edge('SIP001','SIP022',req='(DJ|INV|HJ|RR|DS)') #Checked
	g.add_edge('SIP022','SIP001')
	g.add_bi_edge('SIP021','SIP024')
	
	g.add_bi_edge('SIP003','SIP004')
	
	g.add_edge('SIP003','SIP003-1', req='(INV|HJ)') #Checked
	g.add_edge('SIP003-1','SIP003')
	
	g.add_bi_star('SIP006',['SIP007','SIP025'])
	
	g.add_bi_edge('SIP008','SIP008-1', req='SIP008_SWITCH') #Cannon fired from SIP9 side
	
	g.add_bi_edge('SIP006','SIP017',req='(SIP17_SWITCH)') #Needs cannon fired from SIP18 to open
	
	
	g.add_edge('SIP019','SIP026', req='( (ACC&DJ) |INV|HJ|RR|DS)') #Checked
	g.add_edge('SIP026','SIP019')
	
	g.add_bi_edge('SIP020','SIP021')
	
	g.add_edge('SIP014','SIP014-1', req='(RR|DS|DJ|INV|HJ)') #Checked
	g.add_edge('SIP014-1', 'SIP014')
	
	#Galleon Mineva attributes
	#Triggers
	g.add_attribute('SIP008', {'key':'SIP008_SWITCH'}) #Trigger cannon from SIP9
	g.add_attribute('SIP017', {'key':'SIP17_SWITCH'}) #Trigger cannon from SIP18
	g.add_attribute('Vepar', {'key':'VEPAR_DEAD'}) #Kill Vepar
	
	#Hard Mode Mobs
	g.add_attribute('SIP000_Tutorial', {'mobs' : ['148992']}) #Opening demo #TODO: ensure valid shard is dropped
	g.add_attribute('SIP001', {'mobs' : ['Dullahammer', 'Morte']})
	g.add_attribute('SIP003', {'mobs' : ['Aello', 'Seama', 'Dullahammer']})
	g.add_attribute('SIP004', {'mobs' : ['Aello']})
	g.add_attribute('SIP005', {'mobs' : ['Morte']})
	g.add_attribute('SIP006', {'mobs' : ['Seama']})
	g.add_attribute('SIP008', {'mobs' : ['149504', 'Morte']}) #FireCannon special drop
	g.add_attribute('SIP009', {'mobs' : ['Bat', 'Morte']})
	g.add_attribute('SIP010', {'mobs' : ['Bone Morte', 'Seama']})
	g.add_attribute('SIP011', {'mobs' : ['Cannon Morte', 'Seama', 'Bat', 'Bone Morte', 'Morte']})
	g.add_attribute('SIP014', {'mobs' : ['Morte', 'Bone Morte', 'Seama', 'Dullahammer']})
	g.add_attribute('SIP015', {'mobs' : ['Ghost', 'Bone Morte', 'Cannon Morte']})
	g.add_attribute('SIP015', {'mobs' : ['Seama']})
	g.add_attribute('SIP016', {'mobs' : ['Seama']})
	g.add_attribute('SIP017', {'mobs' : ['Seama', 'Giant Rat', 'Dullahammer']})
	g.add_attribute('SIP019', {'mobs' : ['Aello','Seama','Dullahammer']})
	g.add_attribute('SIP021', {'mobs' : ['Giant Rat']})
	g.add_attribute('SIP021', {'mobs' : ['Poltergeist']})
	g.add_attribute('Vepar', {'mobs' : ['Vepar']})
	
	#Chests
	g.add_attribute('SIP000_Tutorial', {'chests': ['13568']})
	g.add_attribute('SIP002', {'chests' : ['13824']})
	g.add_attribute('SIP003', {'chests' : ['14080']})
	g.add_attribute('SIP003-1', {'chests' : ['125952']})
	g.add_attribute('SIP004', {'chests' : ['14336']})
	g.add_attribute('SIP005', {'chests' : ['14592', '14848']})
	g.add_attribute('SIP006', {'chests' : ['15104']})
	g.add_attribute('SIP007', {'chests' : ['15360', '15616']})
	g.add_attribute('SIP009', {'chests' : ['15872']})
	g.add_attribute('SIP011', {'chests' : ['16128','16384','16640','16896']})
	g.add_attribute('SIP012', {'chests' : ['17152']})
	g.add_attribute('SIP013', {'chests' : ['17408']})
	g.add_attribute('SIP014-1', {'chests' : ['17664']})
	g.add_attribute('SIP015', {'chests' : ['18176']})
	g.add_attribute('SIP016', {'chests' : ['18432']})
	g.add_attribute('SIP017', {'chests' : ['18688']})
	g.add_attribute('SIP018', {'chests' : ['18944']})
	g.add_attribute('SIP019', {'chests' : ['19200']})
	g.add_attribute('SIP020', {'chests' : ['19456']})
	g.add_attribute('SIP021', {'chests' : ['19968']})
	g.add_attribute('SIP024', {'chests' : ['20480']})
	g.add_attribute('SIP025', {'chests' : ['20736']})
	g.add_attribute('SIP026', {'chests' : ['21248']})
	
	#Walls
	g.add_attribute('SIP004', {'walls' : ['127744']})
	g.add_attribute('SIP009', {'walls' : ['128000']})
	g.add_attribute('SIP014-1', {'walls' : ['128256']})
	g.add_attribute('SIP016', {'walls' : ['128512']})
	
	#print("Galleon Minerva: {} nodes".format( g.number_of_nodes() - count))