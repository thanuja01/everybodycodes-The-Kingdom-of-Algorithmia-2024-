potionsForCreatures = {'A':0,'B':1,'C':3,'D':5}
potionsneeded = 0

def quest1a():
    f = open("quest1.txt", "r")
    for x in f:
        for ch in x:
            potionsneeded+=potionsForCreatures[ch]
        print(potionsneeded)

def quest1b(potionsneeded,potionsForCreatures):
    f = open("quest1b.txt", "r")
    paircheck = ""
    for x in f:
        for ch in x:
            paircheck +=ch
            if len(paircheck) ==2:      
              if 'x' in paircheck and 'A' in paircheck:
                paircheck = ""
                continue
              elif 'x' in paircheck:
                paircheck = paircheck.replace('x','')
                if paircheck:
                   if 'D' in paircheck:
                     potionsneeded=potionsneeded+potionsForCreatures[paircheck]
                   else:
                      potionsneeded=potionsneeded+potionsForCreatures[paircheck]
                   print(paircheck,':',potionsForCreatures[paircheck]+1)
              else:
                potionsneeded= potionsneeded+potionsForCreatures[paircheck[0]]+potionsForCreatures[paircheck[1]]+2
                print(paircheck,':',potionsForCreatures[paircheck[0]]+potionsForCreatures[paircheck[1]]+2)
              paircheck = ""
    return potionsneeded

def quest1c(potionsneeded,potionsForCreatures):
    f = open("quest1c.txt", "r")
    groupcheck = ""
    #groupnum = 0
    checkplace = 0
    for x in f:
        xlen = len(x)
        for ch in x:
            checkplace +=1
            groupcheck +=ch
            if len(groupcheck) ==3:    
             # groupnum+=1  
              
              if 'x' in groupcheck:
                groupcheck = groupcheck.replace('x','')
                if groupcheck:
                   if 'A' in groupcheck and len(groupcheck)==1:
                      groupcheck =''
                      continue
                   if len(groupcheck)==1 :
                     potionsneeded=potionsneeded+potionsForCreatures[groupcheck]
                     print(groupcheck,':',potionsForCreatures[groupcheck])
                     groupcheck = ''
                   else:
                      tempprint = 0
                      for i in range(len(groupcheck)):
                         potionsneeded += potionsForCreatures[groupcheck[i]]+1
                         tempprint+=potionsForCreatures[groupcheck[i]]+1
                      print(groupcheck,':',tempprint)
                      tempprint = 0
                      groupcheck = ''
                     # potionsneeded=potionsneeded+potionsForCreatures[groupcheck[0]]+potionsForCreatures[groupcheck[1]]+2
                      #print(groupcheck,':',potionsForCreatures[groupcheck]+potionsForCreatures[groupcheck[1]]+2)
              else:
                potionsneeded= potionsneeded+potionsForCreatures[groupcheck[0]]+potionsForCreatures[groupcheck[1]]+potionsForCreatures[groupcheck[2]]+6
                print(groupcheck,':',potionsForCreatures[groupcheck[0]]+potionsForCreatures[groupcheck[1]]+potionsForCreatures[groupcheck[2]]+6)
                groupcheck = ""
            if checkplace == xlen  and groupcheck:
               
               for i in range(len(groupcheck)):
                         potionsneeded += potionsForCreatures[groupcheck[i]]+1
                         tempprint+=potionsForCreatures[groupcheck[i]]+1
               print(groupcheck,':',tempprint)
                
    return potionsneeded
print(quest1c(potionsneeded,potionsForCreatures))