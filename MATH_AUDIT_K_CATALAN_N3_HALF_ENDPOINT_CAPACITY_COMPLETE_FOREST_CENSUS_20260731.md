# Complete `n=3` half-endpoint-capacity census on both direct shores

Date: 2026-07-31  
Status: complete exact census and independent worst-cut replay.  The proposed
universality of the half-endpoint inequality is false already at `n=3`.

## 1. Question and normalization

For an undirected Catalan linear forest `F` on the rank-three subsets of a
six-set, give a middle vertex `v` the half-endpoint capacity

\[
 y(v)=1-\frac{C}{2N}d_F(v).
\]

At `n=3`, `N=15` and `C=14`.  Scaling by `30` gives

\[
 d_F(v)=0,1,2\quad\longmapsto\quad 30,16,2.             \tag{1.1}
\]

For each of the two direct occurrence shores and every nonempty family
`A` of outer vertices, the tested weighted Hall row is

\[
 \sum_{v\in N(A)}(30-14d_F(v))\ge 30|A|.               \tag{1.2}
\]

There are six outer vertices on either shore, so all `63` nonempty cuts are
tested.

## 2. Completeness of the catalogue

The producer enumerates a perfect matching between all `15` rank-two lower
colours and all `15` rank-four upper colours.  Every selected diamond lifts
to its unique rank-three Johnson edge.  During enumeration it enforces

1. every upper colour is used once;
2. every rank-three degree is at most two; and
3. the physical graph is acyclic.

Conversely, every undirected Catalan linear forest with both turn palettes
exact determines exactly this lower-to-upper matching, because the
intersection and union of a physical Johnson edge determine its diamond.
Thus there is neither omission nor multiplicity in the enumeration.  The
complete count is

\[
                         458{,}544.                    \tag{2.1}
\]

For each forest the two direct occurrence graphs are rebuilt from the
selected diamonds before (1.2) is tested.

## 3. Exact verdict

The complete counts are

\[
\begin{array}{c|r}
\text{quantity}&\text{count}\\ \hline
\text{upper-shore failing forests}&150{,}768\\
\text{lower-shore failing forests}&150{,}768\\
\text{upper-shore failing cuts}&233{,}568\\
\text{lower-shore failing cuts}&233{,}568.
\end{array}                                             \tag{3.1}
\]

The four forest classes are

\[
\begin{array}{c|r}
\text{passes neither shore}&87{,}408\\
\text{passes upper only}&63{,}360\\
\text{passes lower only}&63{,}360\\
\text{passes both shores}&244{,}416.
\end{array}                                             \tag{3.2}
\]

The deficit histogram is identical on the two shores:

\[
\begin{array}{c|rrrrrrrrrr}
\text{scaled deficit}&2&4&6&8&10&12&14&20&22&28\\ \hline
\text{cuts}&68400&22320&91440&19800&7200&3600&13680&3888&1440&1800.
\end{array}                                             \tag{3.3}
\]

Hence the minimum scaled slack is `-28` on each shore.

## 4. Literal worst-cut certificate

On the upper shore, forest `257` has the outer family

\[
 A=\{0x2f,0x3d\}
\]

and neighbourhood

\[
 S=\{11,14,21,25,28,35,42,44,52\}.                    \tag{4.1}
\]

One vertex of `S` has forest degree one and the other eight have degree
two.  Consequently

\[
 \sum_{v\in S}(30-14d_F(v))=16+8\cdot2=32<60=30|A|. \tag{4.2}
\]

The lower-shore dual certificate is forest `989`, outer family
`{0x02,0x10}`, and neighbourhood

\[
 \{7,11,14,25,26,35,49,52,56\},                       \tag{4.3}
\]

with the same degree profile and deficit.

## 5. Translation to the proposed cut inequality

For an outer family with middle neighbourhood `S`, put

\[
 \delta=\sum_{v\in S}(2-d_F(v)),\qquad
 \kappa=\sum_{v\in S}(n-d_F(v)-a_v),                 \tag{5.1}
\]

where `a_v` is its occurrence multiplicity from the outer family.  The
half-endpoint slack identity is

\[
 y(S)-|A|
 =\frac{n\kappa+(n+1)\delta-2|S|}{n(n+2)}.            \tag{5.2}
\]

In (4.1), `|S|=9`, the degree profile gives `delta=1`, and the two outer
vertices use all

\[
 (3-1)+8(3-2)=10=(3+2)|A|
\]

available occurrences, so `kappa=0`.  Therefore

\[
 3\kappa+4\delta=4<18=2|S|.                           \tag{5.3}
\]

This is a literal counterexample to universality of

\[
 n\kappa+(n+1)\delta\ge2|S|.                          \tag{5.4}
\]

It does not say that no useful forest satisfies (5.4): exactly `244,416`
catalogue forests satisfy the half-capacity rows on both shores.

## 6. Reproducibility and scope

The complete producer and frozen output are

```text
scratch/audit_k_catalan_n3_half_endpoint_capacity_all_forests_20260731.cpp
scratch/catalan_n3_half_endpoint_capacity_all_forests_20260731.audit.json
scratch/catalan_n3_half_endpoint_capacity_all_forests_20260731.run.log
```

with SHA-256 hashes

```text
producer  f1b63c67f85f3b780534adb6d819d68f75d6b3c60c11855b3e49449df6765c48
output    0ed1ce6fef8a2b772f1f6868de5135d4f8febe2f8e25e9485818da27b4c68762
run log   de430bfa4e2615e45aa080340f2effc4c75905522590b2db96557a2a7037efc5
```

An independent script reconstructs both worst forests from their fifteen
diamonds, checks acyclicity and degrees, rebuilds both literal occurrence
neighbourhoods, and replays the deficits:

```text
scratch/audit_k_catalan_n3_half_endpoint_capacity_witness_20260731.py
scratch/k_catalan_n3_half_endpoint_capacity_witness_20260731.audit.json
```

Their hashes are

```text
replay    304b084298cbc17e1a9b9067c4948525e4134ab7b60cb08f014e94b13c4fff31
payload   1ee5e5bf81260c58e44ce6caa477a9d69c4ac24eaa0d09ad427494f16c9e1193
canonical 23628543b5a5d67522ab55af5016717e5a2ae4f18212d987e0f0bdb4b6f91da2
```

A clean recompilation and rerun reproduced the complete JSON byte for byte.
The census concerns only the fractional half-endpoint weighted Hall rows on
the complete undirected `n=3` catalogue.  It does not decide coherent
orientation, a rooted side, direct-edgewise recursion, or antipodal filler
existence.
