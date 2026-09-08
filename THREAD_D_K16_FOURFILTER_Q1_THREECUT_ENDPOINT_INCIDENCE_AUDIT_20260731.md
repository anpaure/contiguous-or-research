# Seed0-derived q1 three-cut endpoint-incidence audit

**Date:** 2026-07-31  
**Scope:** hand proof and lightweight exact replay; no SAT/CP search

The frozen source is

```text
scratch/k16_fourfilter_insert_aug_d2_1_targets_20260731.word
SHA-256 e483dae43cce3ca3e678958daab49f4237628f9b129df4f030fd83d83ffaa452
```

The `fourfilter` substring in this historical filename is misleading.  The
source is seed0-derived and is unrelated to the genuine four-filter K15
parent SHA `51f57125...` or its canonical natural K16 chronology SHA
`0f6d64e...`.  Every theorem below is scoped only to `e483dae4...`.

It is a path through every rank-eight mask once.  Its missing rank-nine
adjacent-union colours are exactly

\[
 U=\texttt{0xa9ce},\qquad V=\texttt{0xb8ce}.
\]

This note audits the proposed endpoint-incidence enumeration in
`scratch/threadD_k16_fourfilter_q1_threecut_20260731.py` (source SHA-256 at
the time of the audit
`02d87e939028217d74632be9c04e491d96d1b8c2884583cdef58328e66ae9e69`).

## 1. Forced facet edges

Let (P=(T_0,\ldots,T_{W-1})) be any path through distinct rank-eight
sets.  Delete three old edges and add three new edges.  If a rank-nine set
(C) was not an adjacent-union colour of (P), but is an adjacent-union
colour afterwards, then one added edge has union (C).  The endpoints of
that edge are distinct rank-eight subsets of (C), hence are two facets of
(C).

Consequently every three-edge repair of the present two holes contains an
(U)-facet edge and a (V)-facet edge.  There are

\[
 \binom 92=36
\]

choices for each service edge, hence 1296 service-edge pairs before endpoint
incidence is imposed.  This conclusion does not use an upper-window proxy:
for rank nine, an arbitrary nontrivial interval with union (C) contains an
adjacent pair with union (C).

## 2. Exact fixed-endpoint incidence reduction

For a cut set (D\subseteq\{0,\ldots,W-2\}), define its endpoint multiset

\[
 \partial D=\mathop{\biguplus}_{i\in D}\{T_i,T_{i+1}\}.
\]

If the reconstructed Hamilton path has the same two endpoints as (P),
degree balance is equivalent to

\[
 \partial D=\partial e_U\uplus\partial e_V\uplus\partial e_3             \tag{2.1}
\]

as multisets.  Thus, after choosing (e_U,e_V), one chooses an incident old
cut for every endpoint occurrence of those two edges.  For three distinct
cuts, subtract the four prescribed occurrences from \(\partial D\).  The
remainder must consist of two distinct vertices (x,y), and the third edge
is forced to be (xy).  Finally:

1. update every rank-nine colour multiplicity exactly;
2. require all rank-nine multiplicities to be positive; and
3. require the graph obtained from (P-D+\{e_U,e_V,xy\}) to be the one
   path from (T_0) to (T_{W-1}).

The degree test (degree one at the frozen endpoints and degree two
elsewhere) followed by a traversal from (T_0) is necessary and sufficient.
It also rejects a path plus a disjoint cycle.

For completeness, if global endpoints are *not* frozen, the exact incidence
version uses the eight endpoint tokens of the four components of (P-D).
After assigning four tokens to (e_U,e_V), choose two of the remaining four
tokens for (e_3); the last two tokens are the new global endpoints.  Retain
the choice exactly when the quotient on the four path components is itself a
four-vertex path (parallel component edges and a component cycle are
forbidden).  Equivalently, for final endpoint set (Z), degree balance is

\[
 d_A(v)-d_D(v)
 =\mathbf 1_{v\in\{T_0,T_{W-1}\}}
  -\mathbf 1_{v\in Z}.                                         \tag{2.2}
\]

Equation (2.2), not (2.1), is the complete arbitrary-endpoint model.

For a generic source, one must additionally handle the case in which the
four service incidences use only one or two distinct cuts and append the
remaining cuts before applying (2.1).  For this particular source that case
cannot occur: Section 3 proves that there is only one old cross-facet edge,
so two independent incidence collisions are impossible.  Therefore the
three-distinct-cut generator is complete **for endpoint-preserving
three-edge exchanges on this source**.  It is not, as presently worded,
complete for Hamilton paths whose global endpoints are allowed to change.

## 3. The shared facet and the unique cross-facet edge

The two facet families intersect in exactly one mask,

\[
 S=U\cap V=\texttt{0xa8ce},
\]

which occurs at source position 7578.  Among a (U)-facet and a (V)-facet
other than the repeated occurrence of (S), the source has exactly one
adjacent cross pair:

\[
 T_{6478}=\texttt{0xb84e},\qquad
 T_{6479}=\texttt{0x89ce}.                                      \tag{3.1}
\]

Their union is the rank-ten set `0xb9ce`.  There is no old adjacency between
two (U)-facets or between two (V)-facets, since such an adjacency would
already cover the corresponding missing colour.

There are 64 nominal service-edge pairs using (S) in both edges.  Exact
degree balance leaves only one configuration (the two assignments to the
two incident cuts of (S) are the same configuration):

```text
cuts       6478, 7577, 7578
new U edge 0x89ce -- 0xa8ce
new V edge 0xb84e -- 0xa8ce
third edge 0xa8dc -- 0x88ee
```

This is a connected path, and the three-vertex service interval
`0xb84e,0xa8ce,0x89ce` recovers `0xb9ce`.  It is nevertheless not
(q=1)-complete: cuts 7577 and 7578 remove the unique colours `0xa8de` and
`0xa8ee`, while the third new edge has rank-ten union `0xa8fe`.  Thus the
shared-facet shortcut trades the two original holes for two new rank-nine
holes.

For disjoint service edges, four distinct service vertices must receive four
cut incidences from only three cuts.  Hence one cut joins a (U)-facet to a
(V)-facet.  By (3.1), every such repair is forced to cut 6478 and to use

```text
0x89ce -- (one other U facet),
0xb84e -- (one other V facet).
```

This is the principal structural invariant: every fixed-endpoint three-cut
repair either passes through the shared facet (S), or splits the unique
old witness edge of `0xb9ce`.

## 4. Complete census and the rank-ten third seam

The endpoint-incidence counts are:

```text
service-edge pairs                         1296
  disjoint                                 1232
  sharing S in both edges                    64
raw incident-cut assignments              18432
assignments with three distinct cuts        716
valid residual endpoint assignments         238
distinct (cuts,new-edge-set) configurations 237
  disjoint                                  236
  shared-S                                    1
```

The rank of the forced third edge's union is distributed as

```text
rank 9   11
rank 10  62
rank 11 113
rank 12  51
```

Exact rank-nine multiplicity accounting leaves four (q=1)-complete edge
configurations.  Three reconstruct as a path plus a cycle.  The unique
connected fixed-endpoint repair is

```text
cuts:       2128, 6404, 6478
removed:    0x09cf--0x29ce   union 0x29cf, old multiplicity 2
            0x38ce--0x31ce   union 0x39ce, old multiplicity 3
            0xb84e--0x89ce   union 0xb9ce, rank 10
added:      0x09cf--0x31ce   union 0x39cf, rank 10
            0x29ce--0x89ce   union 0xa9ce
            0x38ce--0xb84e   union 0xb8ce
```

Equivalently, if (A=P[0,2128]), (B=P[2129,6404]),
(C=P[6405,6478]), and (D=P[6479,W-1]), the new order is

\[
 A\,C\,B^{\mathrm{rev}}\,D.                                    \tag{4.1}
\]

The serialized target order in (4.1) has SHA-256
`1133c5d4c7aff3a9888125c9d34b5ac29b0463bb03d8d8fc34b9c5e745124a89`.
Direct multiplicity replay proves that it has no rank-nine holes.

This exposes a fatal error in the proposed census source: it currently
contains

```python
if (third[0] | third[1]).bit_count() != RANK + 1:
    continue
```

There is no such necessity.  If the removed rank-nine colours retain other
witnesses, the third seam may have larger rank.  In fact the unique connected
repair (4.1) has a rank-ten third seam, so the current filter deletes the only
connected positive.  The exact colour-multiplicity test later in the source
is the correct test and makes this rank filter unnecessary.

## 5. Upper and schedule consequences

A full arbitrary-width interval-union replay of (4.1) leaves exactly

```text
0x7bce  rank 11
0xb8cf  rank 10
0xb9ce  rank 10
0xb9fe  rank 12
```

uncovered.  In particular, splitting (3.1) destroys the source's unique
interval witness `[6478,6479]` for `0xb9ce`; the disjoint repair does not
replace it.  The frozen source schedule

```text
X = [6479,10451,12872],  Y = [0,1,2]
```

also fails maximal-envelope reconstruction on (4.1).  Hence the corrected
three-cut census yields a genuine (q=1) repair, but no upper-complete or
fixed-schedule compiler candidate.

## 6. Sharp scope

The proved negative statement is:

> No endpoint-preserving exchange deleting exactly three source edges and
> adding exactly three edges can make this frozen carrier simultaneously
> (q=1)-complete and arbitrary-width upper-complete.

It does not exclude endpoint-changing paths, four or more cuts, a compound
exchange, or a different target order/schedule.  Any implementation claiming
the broader class must either permit endpoint changes in its degree equation
or state the fixed-endpoint hypothesis explicitly.
