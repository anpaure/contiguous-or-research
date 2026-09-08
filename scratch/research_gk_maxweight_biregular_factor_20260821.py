#!/usr/bin/env python3
"""Finite max-weight d-factor tests in GK orientation source graphs."""

from __future__ import annotations
import argparse
from itertools import combinations
from math import comb
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


def masks(b,r):
    return [sum(1<<i for i in cc) for cc in combinations(range(b),r)]


def top_excess(b,x,y):
    s=0; mn=0
    for i in range(b):
        s += 1 if x>>i&1 else -1; mn=min(mn,s)
        s += 1 if y>>i&1 else -1; mn=min(mn,s)
    assert s==0
    return -mn


def solve(b,r,H):
    XX=masks(b,r); YY=masks(b,b-r); N=len(XX)
    for orient in ('A','B'):
        es=[]
        for i,x in enumerate(XX):
            for j,y in enumerate(YY):
                k=top_excess(b,x,y)
                if (k%2==1)==(orient=='A'):
                    es.append((i,j,k,min(k,H)))
        D=comb(b-1,r) if orient=='A' else comb(b-1,r-1)
        dphase=abs(2*r-b)
        nr=max(0,(b-dphase-H+2)//2)
        d=nr*N//b
        assert len(es)==N*D and nr*N%b==0 and d<=D
        rows=[];cols=[];dat=[]
        for e,(i,j,k,w) in enumerate(es):
            rows.extend((i,N+j)); cols.extend((e,e)); dat.extend((1,1))
        A=coo_matrix((dat,(rows,cols)),shape=(2*N,len(es))).tocsr()
        res=linprog(-np.array([w for *_,w in es],dtype=float),
                    A_eq=A,b_eq=np.full(2*N,d,dtype=float),bounds=(0,1),method='highs')
        assert res.success
        x=res.x
        assert np.max(np.abs(x-np.rint(x)))<1e-7
        opt=-res.fun
        ws=sorted((w for *_,w in es),reverse=True)
        uncon=sum(ws[:N*d])
        full=sum(ws)
        uniform=d/D*full if D else 0
        m=D-d
        min_remove_top=None
        if m==0:
            min_remove_top=0
        else:
            for T in range(H+1):
                rem=[e for e,(*_,k,w) in enumerate(es) if w<=T]
                if not rem:
                    continue
                rr=[];cc=[];dd=[]
                for z,e in enumerate(rem):
                    i,j,k,w=es[e]
                    rr.extend((i,N+j)); cc.extend((z,z)); dd.extend((1,1))
                AR=coo_matrix((dd,(rr,cc)),shape=(2*N,len(rem))).tocsr()
                fr=linprog(np.zeros(len(rem)),A_eq=AR,b_eq=np.full(2*N,m,dtype=float),
                           bounds=(0,1),method='highs')
                if fr.success:
                    min_remove_top=T; break
        print({'b':b,'r':r,'H':H,'o':orient,'N':N,'D':D,'d':d,
               'full':full,'uncon':uncon,'factor':opt,'uniform':uniform,
               'extra_vs_uncon':uncon-opt,'loss_factor':full-opt,
               'loss_uncon':full-uncon,'remove_degree':m,
               'min_remove_top':min_remove_top})


if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--b',type=int,required=True); ap.add_argument('--r',type=int,required=True); ap.add_argument('--H',type=int,required=True)
    a=ap.parse_args(); solve(a.b,a.r,a.H)
