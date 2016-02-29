def findShieldMembers(sender, rec1, rec2, rec3):
	notInfiltrator = new Array()
	if(sender == 'Nick Fury'):
		notInfiltrator.append(sender, rec1, rec2, rec3);

	for i in notInfiltrator:
		if(sender == i):
			notInfiltrator.append(rec1, rec2, rec3)

def addAllMembers(m1, m2, m3, m4):
	allMembers.append(m1, m2, m3, m4)

def findInfiltrators(shield, all):
	return list(set(all) - set(shield))

def main():
	print "Welcome to Shield Vs. Hydra Algorithm"
