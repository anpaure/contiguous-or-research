#!/usr/bin/env python3
"""Monte Carlo scaling of coordinate-necklace diagonal factor loss."""

from __future__ import annotations
import argparse,math,random,statistics


def sample_block(b,r,H,rng):
    xs=set(rng.sample(range(b),r)); ys=set(rng.sample(range(b),b-r))
    x=[1 if i in xs else -1 for i in range(b)]
    y=[1 if i in ys else -1 for i in range(b)]
    defect=abs(2*r-b); n=max(0,(b-defect-H+2)//2)
    vals={'A':[],'B':[]}
    for t in range(b):
        h=0;mn=0; boundaries=[]
        for j in range(b):
            boundaries.append(h)
            h+=x[j];mn=min(mn,h)
            h+=y[(t+j)%b];mn=min(mn,h)
        assert h==0
        ks=[z-mn for z in boundaries]
        parity=ks[0]&1
        assert all((k&1)==parity for k in ks)
        w=sum(min(k,H) for k in ks)
        vals['A' if parity else 'B'].append(w)
    out={}
    for o in 'AB':
        rem=sorted(vals[o])[:len(vals[o])-n]
        out[o]=sum(rem)/(b*b)
    return out


def deterministic_block(b,r,H,kindx,kindy):
    def make(kind,ones):
        if kind=='block': return [0]*(b-ones)+[1]*ones
        if kind=='revblock': return [1]*ones+[0]*(b-ones)
        if kind=='mechanical': return [((i+1)*ones//b-i*ones//b) for i in range(b)]
        if kind=='alt':
            z=b-ones;o=ones;v=[]
            while z+o:
                if z:v.append(0);z-=1
                if o:v.append(1);o-=1
            return v
        raise ValueError(kind)
    xb=make(kindx,r);yb=make(kindy,b-r)
    x=[2*z-1 for z in xb];y=[2*z-1 for z in yb]
    defect=abs(2*r-b);n=max(0,(b-defect-H+2)//2);vals={'A':[],'B':[]}
    for t in range(b):
        h=0;mn=0;bd=[]
        for j in range(b):
            bd.append(h);h+=x[j];mn=min(mn,h);h+=y[(t+j)%b];mn=min(mn,h)
        ks=[z-mn for z in bd];o='A' if ks[0]&1 else 'B';assert all((k&1)==(ks[0]&1) for k in ks)
        vals[o].append(sum(min(k,H) for k in ks))
    return {o:sum(sorted(vals[o])[:len(vals[o])-n])/(b*b) for o in 'AB'}


def run(b,r,H,samples,seed):
    rng=random.Random(seed); rows=[sample_block(b,r,H,rng) for _ in range(samples)]
    print({'b':b,'r':r,'H':H,'n':max(0,(b-abs(2*r-b)-H+2)//2),'samples':samples,
           'loss_per_block_b2_mean':{o:statistics.mean(z[o] for z in rows) for o in 'AB'},
           'sd':{o:statistics.pstdev(z[o] for z in rows) for o in 'AB'}})
    for kx in ('block','revblock','mechanical','alt'):
      for ky in ('block','revblock','mechanical','alt'):
        print('det',kx,ky,deterministic_block(b,r,H,kx,ky))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--b',type=int,required=True);p.add_argument('--r',type=int,required=True);p.add_argument('--H',type=int,required=True);p.add_argument('--samples',type=int,default=20);p.add_argument('--seed',type=int,default=1)
    a=p.parse_args();run(a.b,a.r,a.H,a.samples,a.seed)
