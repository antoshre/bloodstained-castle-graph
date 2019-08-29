def generate_Arvantville(g):
	#Arvantville
	g.add_bi_path(['Vepar','VIL001','VIL002','VIL003'])
	g.add_bi_star('VIL003',['VIL004','VIL005'])
	
	
	
	g.add_bi_edge('VIL003','VIL006',req='(VillageKey)')
	
	g.add_bi_edge('VIL005', 'VIL005-1', req='(FOOD_QUEST_COMPLETE)') #Food Quest reward
	g.add_bi_edge('VIL005', 'VIL005-2', req='(SILVER_BROMIDE)') #Photo event
	
	g.add_bi_path(['VIL006','VIL007','VIL008','T1'])
	g.add_bi_path(['VIL006','VIL009','VIL011','VIL012', 'T2'])
	
	g.add_bi_edge('VIL009','VIL010')
	g.add_bi_edge('VIL011','VIL008')
	
	#Arvantville attributes
	g.add_attribute('VIL005', {'key':'VillageKey'}) #Receive key in VIL5 from Dominique on first visit in vanilla
	g.add_attribute('VIL005-2', {'key':'PhotoID'}) #Get photo in scripted event
	
	#Hard Mode Mobs
	g.add_attribute('VIL001', {'mobs' : ['Morte', 'Bone Morte', 'Aello', 'Giant Rat']})
	g.add_attribute('VIL006', {'mobs' : ['Morte', 'Bone Morte', 'Bat', 'Aello']}) 
	g.add_attribute('VIL011', {'mobs' : ['Giant Rat', 'Bat']})
	g.add_attribute('VIL012', {'mobs' : ['Bat']})
	#Chests
	g.add_attribute('VIL001', {'chests' : ['21760']})
	g.add_attribute('VIL003', {'chests' : ['22016']})
	g.add_attribute('VIL005', {'chests' : ['4864']}) #Village Key 'chest'
	g.add_attribute('VIL005-1', {'chests' : ['22272']}) #Gebel's Glasses
	g.add_attribute('VIL006', {'chests' : ['22528', '22784']})
	g.add_attribute('VIL007', {'chests' : ['23552']})
	g.add_attribute('VIL010', {'chests' : ['24320']})