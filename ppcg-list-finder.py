import random
# Initial prime search
w=[2,3,5,7,11,13,17,19,23,29,31] # 2-3-5 wheel
#pl=set([2])
#n=0
#while max(pl,)<16777216:
#  n+=30
#  for p in w:
#    pl.add(p+n)
#  for p in pl:
#    for i in range(p*2,max(pl)+1,p):
#      try:
#        pl.remove(i)
#      except:
#        pass
#pl=list(pl)
#pl=random.shuffle(pl) or pl
#print("Prime list: %r\n"%pl)
#a=[[[[pl[(((((n0*3)+n1)*4)+n2)*4)+n3] for n3 in range(4)] for n2 in range(4)] for n1 in range(4)] for n0 in range(3)]
#print("Prime array: %r\n"%a)

pl=[]
m=16777216

def genPrimes():
  global pl,w,best
  big=1
  for n in w:
    big*=n
  if best!=[]:
    for i in range(512):
      if random.random()<=0.03125:
        n=1
        while n<big/2:
          n*=random.choice(w)
        pl[i]=n
      elif random.random()<=0.03125:
        n=random.randrange(len(pl))
        pl[i],pl[n]=pl[n],pl[i]
      elif random.random()<=0.03125:
        pl[i]=best[i]
  else:
    for i in range(512):
      n=1
      while n<big/2:
        n*=random.choice(w)
      pl.append(n+1)

#def cppcgStep(x1,x2,x3):
#  xp=lambda n1,n2,n3:pow(x1,n1)*pow(x2,n2)*pow(x3,n3)
#  y1=sum([a[0][n1][n2][n3]*xp(n1,n2,n3) for n3 in range(4) for n2 in range(4) for n1 in range(4)])%m
#  y2=sum([a[1][n1][n2][n3]*xp(n1,n2,n3) for n3 in range(4) for n2 in range(4) for n1 in range(4)])%m
#  y3=sum([a[2][n1][n2][n3]*xp(n1,n2,n3) for n3 in range(4) for n2 in range(4) for n1 in range(4)])%m
#  return y1,y2,y3

#x123=(0,1,2)
#for i in range(64):
#  x123=cppcgStep(*x123)
#  print(x123)

def p(x):
  return pl[((x*pl[x%512])+pl[(x+pl[x%512])%512])%512]

def ppcg(x):
  return ((p(x)*x*x)+(p(p(x))*x)+p(p(p(x))))%m

best=[]
bestn=0
i=0
try:
  fail=True
  while fail:
    genPrimes()
    bench=set([])
    x=0
    fail=False
    i=0
    while i<16777216:
      x=ppcg(x)
      if x in bench:
        fail=True
        if bestn<i:
          best=pl
          bestn=i
          print(best,bestn)
        else:
          print(i)
        break
      bench.add(x)
      i+=1
  print(pl)
finally:
  print("\n\n")
  if i>bestn:
    print(pl,i)
  else:
    print(best,bestn)
