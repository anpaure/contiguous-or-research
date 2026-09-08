#!/usr/bin/env python3
"""Find canonical labels for U--B projection components (H100 only)."""

from __future__ import annotations
import argparse,collections,json
from pathlib import Path

def gk(x,n):
 st=[];ma={}
 for i in range(n):
  if x>>i&1:st.append(i)
  elif st:j=st.pop();ma[j]=i;ma[i]=j
 fr=[i for i in range(n) if i not in ma]
 return ma,[i for i in fr if not(x>>i&1)],[i for i in fr if x>>i&1]

def word(x,n):return ''.join(str(x>>i&1) for i in range(n))

def dyck(w):
 h=0
 for c in w:
  h+=1 if c=='1' else -1
  if h<0:return False
 return h==0

def primitive_count(w):
 h=0;k=0
 for c in w:
  h+=1 if c=='1' else -1
  if h==0:k+=1
 return k

def audit(path):
 d=json.load(open(path));n=d['n'];m=d['m'];rs=[r for r in d['records'] if r['q']>r['p']]
 us=sorted({r['upper'] for r in d['records']});bs=sorted({r['b'] for r in rs})
 ua={u:set() for u in us};ba={b:set() for b in bs}
 for r in rs:ua[r['upper']].add(r['b']);ba[r['b']].add(r['upper'])
 seen=set();cs=[]
 for seed in us:
  if seed in seen:continue
  cu={seed};cv=set();seen.add(seed);q=collections.deque([('u',seed)])
  while q:
   side,x=q.popleft()
   if side=='u':
    for v in ua[x]:
     if ('b',v) not in seen:seen.add(('b',v));cv.add(v);q.append(('b',v))
   else:
    for u in ba[x]:
     if u not in seen:seen.add(u);cu.add(u);q.append(('u',u))
  cs.append((cu,cv))
 # Repair mixed-type seen sentinel bug harmless because ints != tuples.
 print('INSTANCE',m,'components',len(cs))
 for idx,(cu,cv) in enumerate(sorted(cs,key=lambda z:(-len(z[0]),-len(z[1])))):
  def feats(x):
   w=word(x,n);ma,fz,fo=gk(x,n)
   # all balanced gap words from the unique GK free factorization
   free=fz+fo;cuts=[-1]+free+[n];gaps=[w[cuts[i]+1:cuts[i+1]] for i in range(len(cuts)-1)]
   return {
    'word':w,'rev':w[::-1],
    'D0':gaps[0], 'Dlast':gaps[-1],
    'central':gaps[len(fz)],
    'first_nonempty_gap':next((z for z in gaps if z),''),
    'last_nonempty_gap':next((z for z in reversed(gaps) if z),''),
    'min_gap':min(gaps), 'max_gap':max(gaps),
    'min_nonempty_gap':min((z for z in gaps if z),default=''),
    'pc_D0':primitive_count(gaps[0]),
    'pc_central':primitive_count(gaps[len(fz)]),
    'fz':len(fz),'fo':len(fo),'firstfo':fo[0],
   }
  allx=cu|cv
  keys=feats(next(iter(allx))).keys()
  const={k:next(iter(v)) for k in keys if len(v:={feats(x)[k] for x in allx})==1}
  mins={k:min(feats(x)[k] for x in allx) for k in ('word','D0','central','first_nonempty_gap','min_nonempty_gap')}
  print('COMP',idx,len(cu),len(cv),len(cu)-len(cv),'const',const,'mins',mins,
        'minU',min(map(lambda x:word(x,n),cu)),'maxU',max(map(lambda x:word(x,n),cu)),
        'minB',min(map(lambda x:word(x,n),cv)),'maxB',max(map(lambda x:word(x,n),cv)))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('catalogue',type=Path);a=p.parse_args();audit(a.catalogue)
