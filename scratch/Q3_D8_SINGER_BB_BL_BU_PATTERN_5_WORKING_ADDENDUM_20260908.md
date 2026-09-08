# Pure pattern-5 obstruction

2026-09-08. Author: ternary_lift. Full independent end-to-end hand audit
by direct_route: PASS, including exhaustive BL/BB branches and both AP
orientations. No mathematical computation was run. This is a complete
pure obstruction for the stated pattern, independent of the earlier
finite inventory. The existing filename is retained for stable links.

Use the original endpoint and cyclic notation from
Q3_D8_SINGER_BB_ALL_POSITIONS_AND_PATTERN_2_OBSTRUCTION_20260908.md.
Write its forbidden triples and pairs as

    F={123,126,135,146,234,245,456},
    P={16,35,25,26,45,56}.

Pattern 5 puts infinity at BB interior, BL L-interior, and BU B-D.
The all-position BB theorem says BB cannot supply infinity-one223;
BU B-D has no infinity-one flag. Thus BL must supply223.

## 1. Exhaustive BL reduction

Orient BL as AABBCCDD / EFEFGHGH with F=infinity, and translate cyclic
C to zero. Its infinity-one triples are ABE and DGH. Its odd classes
are l1=AEG and l2=DGH. Let u be BU's odd complementary class, one of
115,133,223. The parity rule says l1=l2 if u=115; otherwise
{l1,l2}={115,u}. DGH cannot itself be115.

If DGH supplies223, avoiding endpoint triple F at the flag (DGH;C)
and avoiding two equal infinity-one necklaces forces

    DGH=136, ABE=245.

For u=115, l1=l2=223. The only AEG=223 possibility is AE=24,B=5,
G=6,DH=13, but the pair AE-G=35 is forbidden. For u different from115,
u must be223 and AEG must be115. The possible (AE,B,G) are

    (24,5,3), (45,2,3), (45,2,6).

Pairs AE-G rule out the first and last (16 and56). Thus AE=45,B=2,
G=3,DH=16. The triple BCD-H rules out D=1,H=6 by123, so D=6,H=1.
The triple ABC-E rules out A=5,E=4 by135, so A=4,E=5.

If instead ABE supplies223 and DGH does not, complementary triples
and endpoint avoidance leave ABE=146,DGH=235. Here l2=124, so parity
requires u=115 and AEG=124. The possible (AE,B,G) are

    (14,6,2), (16,4,5), (46,1,3).

Pairs AE-B rule out the first and last (25 and35). In the middle case
DH=23; BCD-H forces D=3,H=2, but CDH-G=245 is forbidden. This branch
is impossible.

The unique surviving BL assignment is therefore

    (A,B,C,D,E,F,G,H)=(4,2,0,6,5,infinity,3,1).

Its infinity-one necklaces are142 and223. Its infinity-zero triple
flags are246,156,345,136, and its infinity-two pair flags are12,23.

## 2. Exhaustive BB reduction

BB must supply the other necklaces124 and133. Normalize its block
orders as (a,infinity,c,d)/(e,f,0,h). Its infinity-one triples
U=aef and V=cdh must be the partition125/346 in one of its two orders.

For U=125,V=346, the triple (ef0)-a forces a=2. If (e,f)=(1,5),
the pair ae-c is56,45,or23 for c=3,4,6, respectively, all forbidden
by the endpoint or BL. Hence (e,f)=(5,1). Pair ae-c excludes c=3.
For c=4, pair cd-h forces d=6,h=3. For c=6 it forces d=4,h=3,
but then (f0h)-d=346 repeats the flag V. Thus the sole
survivor has block orders

    (2,infinity,4,6)/(5,1,0,3).

For U=346,V=125, triple (dh0)-c forces c=2. Pair ae-f forces
f=3 and {a,e}=46. The pair ac-e is then35 or25, both forbidden.
This reverse orientation is impossible.

The displayed BB has infinity-zero flags125,346,356,236,256,124
and infinity-two flags14,15,46,13. Together with BL and the endpoint,
the three remaining infinity-zero flags are134,145,235, and the
three remaining infinity-two flags are24,34,36.

## 3. BU contradiction

BL's two odd classes are115 and223, so BU's odd class must be223.
For BU AABBCCDD / EFGEFGHH with D=infinity, the complementary odd
triples FGH and CGH are translates in class223, sharing G,H. Normalize
their four-term AP union to {0,2,4,6}, with {C,F}={0,6} and
{G,H}={2,4}. The four possible assignments give

| C | F | G | H | Pair CH-G |
| ---: | ---: | ---: | ---: | --- |
| 0 | 6 | 4 | 2 | 35 |
| 0 | 6 | 2 | 4 | 25 |
| 6 | 0 | 4 | 2 | 25 |
| 6 | 0 | 2 | 4 | 24 |

The first three repeat endpoint pairs. In the last assignment the
remaining axes A,B,E are {1,3,5}. The pair CH-B is35,13,or16 as
B=1,3,5. None is among BU's required remaining pairs24,34,36:
35 and16 are endpoint-covered and13 is supplied by the forced BB.
Thus no BU can complete the flags. The exhaustive hand reductions above
exclude every provider triple in pattern5 for the original endpoint.

The independent audit checked the complete BL complementary-necklace
branch list, both BB orientations and every elimination, the resulting
residual signatures, and both AP directions. The theorem is scoped to
pattern5 with the original endpoint and these literal provider profiles;
it does not exclude other endpoints, profiles, or position patterns.
