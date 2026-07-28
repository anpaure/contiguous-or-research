#!/usr/bin/env python3
"""Materialize a six-piece A/B intersection-lift braid."""

from __future__ import annotations
import argparse,json
from pathlib import Path

def main():
    p=argparse.ArgumentParser();p.add_argument('source',type=Path)
    p.add_argument('--acuts',type=int,nargs=2,required=True);p.add_argument('--bcut',type=int,required=True)
    p.add_argument('--pieces',nargs=6,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    middle=list(map(int,json.loads(a.source.read_text())['middle_path']));n=len(middle)//2;left,right=middle[:n],middle[n:]
    c0,c1=sorted(a.acuts)
    groups={'A1':left[:c0+1],'A2':left[c0+1:c1+1],'A3':left[c1+1:],
            'B1':right[:a.bcut],'B2':right[a.bcut:a.bcut+3],'B3':right[a.bcut+3:]}
    path=[]
    for spec in a.pieces:
        values=groups[spec[:2]]
        path.extend(reversed(values) if spec[2]=='R' else values)
    assert len(path)==len(middle) and len(set(path))==len(path)
    payload={'middle_path':path,'meta':{'source':str(a.source),'acuts':[c0,c1],'bcut':a.bcut,'pieces':a.pieces}}
    a.output.write_text(json.dumps(payload,indent=2)+'\n');print(json.dumps({'output':str(a.output),'length':len(path)}))
if __name__=='__main__':main()
