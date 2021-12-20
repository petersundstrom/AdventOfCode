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
  cmd1 = []
  cmd2 = []
  status = 0
  for x in lines:
    if (status==0):
      x = x.replace("\n","")
      x = x.split(",")
      if (x[0]==''):
        status = 1
        continue
      lw1.append(int(x[0]))
      lw2.append(int(x[1]))
    else:
      x = x.replace("\n","")
      x = x.split(" ")
      x = x[2].split("=")
      cmd1.append(x[0])
      cmd2.append(int(x[1]))
  return(lw1,lw2,cmd1,cmd2)

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
    
def vikx(plan, col):
  plan2 = list([])

  print ("vikx",col)
  for y in range(0,len(plan)):
    yy = list(plan[y])
    yy.reverse()
    plan2.append(yy)
  return(plan2)

def viky(plan, row):
  plan2 = list([])
  for i in range(0,len(plan)):
    plan2.append(plan[len(plan)-i-1])
  return(plan2)

def orfunc(plan1,plan2,xs, typ):
  plan3 = list([])
  for i in range(0,len(plan1)):
    temp = list([])
    for j in range(0,len(plan1[0])):
      temp.append(plan1[i][j] or plan2[i][j])
    plan3.append(temp)

  plan4 = list([])
  if typ=='x':
    for i in range(0,len(plan1)):
      temp = list([])
      for j in range(0,len(plan1[0])):
        if j>=xs:
          break
        temp.append(plan3[i][j])
      plan4.append(temp)
  else:
    for i in range(0,xs):
      temp = list([])
      for j in range(0,len(plan1[0])):
        temp.append(plan3[i][j])
      plan4.append(temp)
    
  return(plan4)

def printplan(plan):
  print()
  if len(plan)>100:
    return('')
  for i in plan:
    s = ''
    for x in i:
      if x==1:
        s += 'X'
      else:
        s += ' '
    print(s)    
  return(s)


lw1,lw2, cmd1, cmd2 = readFile(lines)

xmax = max(lw1)
ymax = max(lw2)

xval = []
plan = [ [0] * (xmax+1) for _ in range(ymax+1)]


print ("lw1","lw2",len(lw1),len(lw2),"xmax","ymax",xmax,ymax)
for i in range(0,len(lw1)):
  x = lw1[i]
  y = lw2[i]
  plan[y][x] = 1

print("yyyyyyyyyyyyyyy")
planz = list(plan)

for i in range(0,len(cmd1)):
  if (cmd1[i]=="x"):
    print("vikx")
    plan2 = vikx(planz,cmd2[i])
  elif (cmd1[i]=="y"):
    print("viky")
    plan2 = viky(planz,cmd2[i])

  print("************************")
  z = 0
  for x in planz:
    z += x.count(1)
  print(z)
  printplan(planz)

  print(cmd2[i],cmd1[i])
  plan4 = orfunc(planz,plan2,cmd2[i],cmd1[i])

  planz = list(plan4)

z = 0
for x in planz:
  z += x.count(1)
print(planz)
print (z)
printplan(planz)
