import math

notInfiltrator = []
allMembers = []

def findShieldMembers(sender, rec1, rec2, rec3):
	# notInfiltrator = new Array()
	if(sender == 'Nick Fury'):
		notInfiltrator.append(sender, rec1, rec2, rec3);

	else:
		for i in notInfiltrator:
			if(sender == i):
				notInfiltrator.append(rec1, rec2, rec3)

def addAllMembers(m1, m2, m3, m4):
	allMembers.append(m1, m2, m3, m4)

def findInfiltrators(shield, all):
	return list(set(all) - set(shield))

def input():
	sender = input("\n Who is the sender?")
	for x in xrange(3):
		r[x] = input("\n Who is the receiver No."+x+"?")
		findShieldMembers(sender, r[0], r[1], r[2])
		addAllMembers(sender, r[0], r[1], r[2])		
	result()

def main():
	print "Welcome to Shield Vs. Hydra Algorithm"
	answer = input("\nShould we start this algorithm?")
	if(answer == "no"):
		return
	elif(answer == "yes"):
		input();

def result():
	Infiltrator = findInfiltrators(notInfiltrator, allMembers)
	print "The infiltrators are: "
	for x in xrange(Infiltrator):
		print "\n"+x+"\n"
