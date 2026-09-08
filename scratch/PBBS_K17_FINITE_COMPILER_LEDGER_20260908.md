# Finite PBBS compiler ledger at k=17

2026-09-08. One tiny exact binomial evaluation executed remotely through
`ssh h100`; reported remote hostname: `arboghast`. No PBBS factor enumeration,
packing computation, or word search was performed. No mathematical code was
executed on the Mac.

The published compiler ledger in
`PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md`,
equation (11), is

    B(r,H) = W_r + 2H Cat_r
             + 2(5H-1) P(T<=H-1) + 2L_r(r-H).

At k=17, r=8, W_r=24310, Cat_r=1430, and the admissible positive integer
depths under 2H<=r+1 are H=1,2,3,4. The known comparison word has length
25745.

The exact evaluations, setting the nonnegative packing term to zero, are:

| H | 2H Cat_8 | L_8(8-H) | 2L_8(8-H) | Packing coefficient | B(8,H) with P=0 | Excess over 25745 |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2860 | 35308 | 70616 | 8 | 97786 | 72041 |
| 2 | 5720 | 32172 | 64344 | 18 | 94374 | 68629 |
| 3 | 8580 | 24108 | 48216 | 28 | 81106 | 55361 |
| 4 | 11440 | 13580 | 27160 | 38 | 62910 | 37165 |

Thus none of these four instances of this ledger can certify a word shorter
than 25745, even if its packing number were zero. Already the baseline plus
collar term is at least 24310+2860=27170>25745 for every admissible H, so the
tail evaluation is supplementary and no packing enumeration is necessary.

These are lower bounds on the numerical right-hand side of a sufficient
upper-bound ledger. They are not lower bounds on all complete words, nor
lower bounds on the actual length of every word made by a more economical
implementation of the construction. They rule out improving the known
k=17 word using this published ledger alone. The proposed asymptotic
coefficient-one proof does not supply an effective k=17 improvement.

## Exact remote evaluation provenance

The following Python body was supplied once to `ssh h100 'python3 -'` by
heredoc. It uses the exact tail formula from equation (11)'s source.

```python
from math import comb
import socket
r = 8
W = comb(2*r+1, r)
cat = comb(2*r,r)//(r+1)

def C(t):
    return 0 if t < 0 else comb(r, min(t,r//2))

def L(s):
    return 2*sum((comb(r,a)-(comb(r,a-1) if a else 0))*(r if a == 0 else r-2*a+1)*C(s-a) for a in range(r//2+1))

print('Remote host:', socket.gethostname())
print('r=',r,'W=',W,'Cat_r=',cat,sep='')
print('H | collar | L_r(r-H) | odd_tail=2L | packing_coefficient | ledger_with_P=0 | excess_over_25745')
for H in range(1,5):
    collar=2*H*cat
    tail=2*L(r-H)
    val=W+collar+tail
    print(H,collar,L(r-H),tail,2*(5*H-1),val,val-25745,sep=' | ')
```
