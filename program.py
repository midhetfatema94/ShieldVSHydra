import math

notInfiltrator = []
allMembers = []
temp = []

def findShieldMembers(sender, rec):
  #print "in the function!"
  if(sender == 'Nick Fury' and (sender and rec) not in notInfiltrator and not " "):
    notInfiltrator.append(sender)
    notInfiltrator.append(rec)
    #print("Here2")
    
  elif(sender in notInfiltrator and rec not in notInfiltrator and not " "):
    notInfiltrator.append(rec)
    #print("Here1")
    for i in temp:
      #print(i['sender'])
      if(rec in notInfiltrator and rec == i['sender']):
        #print ("In the if statement")
        if(i['rec'] not in notInfiltrator and not " "):
          notInfiltrator.append(i['rec'])

  else:
    temp.append({'sender':sender, 'rec':rec})
    #print("Here")
    
def addAllMembers(m1, m2):
  allMembers.append(m1)
  allMembers.append(m2)

def findInfiltrators(shield, allMem):
  return list(set(allMem) - set(shield))

def inputSender():
  sender = raw_input("Who is the sender? ")
  for i in range(0,3):
        rec = raw_input("\n Who is the receiver No."+str(i+1)+"? ")
        print(rec)
        findShieldMembers(sender, rec)
        addAllMembers(sender, rec)  
  main()
def main():
  print ("Welcome to Shield Vs. Hydra Algorithm\n")
  answer = raw_input('Should we start this algorithm? ')
  if(answer == "yes"):
    inputSender();
  elif(answer == "no"):
    choice = raw_input('Should we give you the result? ')
    if (choice == 'yes'):
      traitors = findInfiltrators(notInfiltrator, allMembers)
      print ("\nTraitors: ")
      for i in traitors:
        print i
  return

main()
