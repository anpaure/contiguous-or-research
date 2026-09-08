#!/usr/bin/env python3
"""Print exact strong-compatible removals for representative GK sources."""

from __future__ import annotations

from itertools import combinations


def data(n: int, ones: frozenset[int]):
    bits = [int(i in ones) for i in range(n)]
    stack=[]; matched=[False]*n; mate=[None]*n
    for i,z in enumerate(bits):
        if z: stack.append(i)
        elif stack:
            j=stack.pop(); matched[i]=matched[j]=True; mate[i]=j; mate[j]=i
    aa=tuple(reversed([i for i,z in enumerate(bits) if not z and not matched[i]]))
    return bits,matched,mate,aa


def main():
    b=5;n=10;shown=0
    for cc in combinations(range(n),b):
        s=frozenset(cc); bits,matched,mate,aa=data(n,s)
        if len(aa)<2: continue
        good=[]
        for x in s:
            sp=frozenset((s-{x})|{aa[0]}); ap=data(n,sp)[3]
            common=min(len(ap),len(aa)-1)
            if common and ap[:common]==aa[1:1+common]: good.append(x)
        if good:
            print('WORD',''.join(map(str,bits)),'AA',aa,'GOOD',good,'MATES',[mate[x] for x in good])
            shown+=1
            if shown>=15: break

if __name__=='__main__': main()
