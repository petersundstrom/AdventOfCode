import re
from numpy import loadtxt
with open('data7_1.txt') as my_file:
    lines = my_file.readlines()

def readFile(lines):
  words = []

  row = []
  lw = []
  lw1 = []
  lw2 = []
  for x in lines:

    x = x.replace("\n","")
    x = x.split("-")
    for z in x:
      words.append(z)
      if z not in lw:
        lw.append(z)
    lw1.append(x[0])
    lw2.append(x[1])
    lw2.append(x[0])
    lw1.append(x[1])

  print (lw)
  print (lw1)
  print (lw2)
  return(lw,lw1,lw2)

r = ''


numw = 0

# One of the small caves can be visited twice
def checklist(busy2,s):
  if busy2.count(s)==0:
    return True
  elif busy2.count(s)>=2:
    return(False)
  else:
    n = 0
    for i in range(0,len(busy2)):
      for j in range(0,len(busy2)):
        if i==j:
          continue
        if (busy2[i]==busy2[j]):
          n += 1
    if n>0:
      return(False)
  return(True)


def findWays(startid,lw1,lw2, n, busy2, way):
  global numw
  for s in range(0,len(lw1)):
    w = lw2[s]
    q = lw.index(w)
    
    if lw1[s]==startid and checklist(busy2,lw2[s])==True and lw2[s]!="start":
      if lw2[s]=="end":
        numw += 1
        continue
      elif lw2[s].islower():
        findWays(lw2[s],lw1,lw2, n+1, busy2 + [lw2[s]], way+"-,"+lw2[s])
      else:
        findWays(lw2[s],lw1,lw2, n+1, busy2,way+"-,"+lw2[s])
    
  

lw,lw1,lw2 = readFile(lines)
busy = []

qq = lw.index('start')


for i in range(0,len(lw)):
  busy.append(0)

print("index of start",qq)
qq = lw.index('start')
busy[qq] = 1

startid = lw1.index("start")

paths = 0
findWays("start", lw1,lw2,0, ["start"], "start")

print("Result:",numw)





