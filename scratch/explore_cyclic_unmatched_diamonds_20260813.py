#!/usr/bin/env python3
"""Try cyclic-parenthesis two-coordinate deletions for the Catalan forest."""

from collections import Counter, defaultdict
from itertools import combinations


def sets(n, w):
    for cc in combinations(range(n), w):
        x = sum(1 << i for i in cc)
        yield x


def cyclic_unmatched_ones(x, n):
    h = 0
    vals = [0]
    for i in range(n):
        h += 1 if (x >> i) & 1 else -1
        vals.append(h)
    start = max(i for i, v in enumerate(vals[:-1]) if v == max(vals[:-1])) % n
    stack = []
    free = []
    for jj in range(n):
        i = (start + jj) % n
        if ((x >> i) & 1) == 0:
            stack.append(i)
        elif stack:
            stack.pop()
        else:
            free.append(i)
    assert not stack
    return free


def comps(vertices, edges):
    ad = defaultdict(list)
    for a, b in edges:
        ad[a].append(b); ad[b].append(a)
    seen = set(); ret=[]
    for v in vertices:
        if v in seen: continue
        st=[v];seen.add(v);vv=[];ee=0
        while st:
            a=st.pop();vv.append(a);ee+=len(ad[a])
            for b in ad[a]:
                if b not in seen:seen.add(b);st.append(b)
        ret.append((len(vv),ee//2))
    return ret


def main():
    print("restricted incidence")
    for r in range(2, 10):
        n=2*r-1
        ups=list(sets(n,r+1)); lows=list(sets(n,r-1))
        ad=defaultdict(set)
        for u in ups:
            ff=cyclic_unmatched_ones(u,n)
            for rule in range(3):
                drop=[ff[(rule+j)%3] for j in range(2)]
                lo=u^(1<<drop[0])^(1<<drop[1])
                ad[("u",u)].add(("l",lo));ad[("l",lo)].add(("u",u))
        ld=Counter(len(ad[("l",l)]) for l in lows)
        seen=set(); stats=[]
        for v in [("u",u) for u in ups]+[("l",l) for l in lows]:
            if v in seen:continue
            st=[v];seen.add(v);nu=nl=0
            while st:
                x=st.pop();nu+=x[0]=="u";nl+=x[0]=="l"
                for y in ad[x]:
                    if y not in seen:seen.add(y);st.append(y)
            stats.append((nu,nl))
        print(r,"ldeg",dict(sorted(ld.items())),"components",len(stats),
              "minslack",min(nl-nu for nu,nl in stats),
              "types",Counter(stats).most_common(8))
    for rule in range(3):
        print("rule", rule)
        for r in range(2, 10):
            n=2*r-1
            edges=[]; lows=[]
            for u in sets(n,r+1):
                free=cyclic_unmatched_ones(u,n)
                assert len(free)==3,(r,bin(u),free)
                drop=[free[(rule+j)%3] for j in range(2)]
                lo=u
                for z in drop:lo^=1<<z
                a=lo|(1<<drop[0]);b=lo|(1<<drop[1])
                edges.append((a,b));lows.append(lo)
            dg=Counter(z for e in edges for z in e)
            cc=comps(list(sets(n,r)),edges)
            print(r,"lower",len(set(lows)),"maxdeg",max(dg.values(),default=0),
                  "cycles",sum(v==e and e for v,e in cc),"components",len(cc))
    for mode in ("min_after", "max_after", "min_leave", "max_leave"):
        print("size rule", mode)
        for r in range(2,10):
            n=2*r-1;edges=[];lows=[]
            for u in sets(n,r+1):
                ff=cyclic_unmatched_ones(u,n)
                sizes=[]
                for j in range(3):
                    sizes.append(((ff[(j+1)%3]-ff[j]-1)%n)//2)
                if mode.endswith("after"):
                    j=(min if mode.startswith("min") else max)(range(3),key=lambda x:(sizes[x],-ff[x]))
                    rule=j
                else:
                    leave=(min if mode.startswith("min") else max)(range(3),key=lambda x:(sizes[x],-ff[x]))
                    rule=(leave+1)%3
                drop=[ff[(rule+j)%3] for j in range(2)]
                lo=u^(1<<drop[0])^(1<<drop[1]);a=lo|(1<<drop[0]);b=lo|(1<<drop[1])
                edges.append((a,b));lows.append(lo)
            dg=Counter(z for e in edges for z in e);cc=comps(list(sets(n,r)),edges)
            print(r,"lower",len(set(lows)),"maxdeg",max(dg.values()),
                  "cycles",sum(v==e and e for v,e in cc),"components",len(cc))


if __name__=="__main__":main()
