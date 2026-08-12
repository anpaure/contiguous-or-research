# Minimal service blocks and the exact depth-two signature graph at `j3959`

Date: 2026-07-30

Status: **PASS exact local classification; minimal two-row depth-two service
excluded; explicit three-row destination buffer; literal source-return braid
remains open**.

This note independently audits the frozen chronology

```text
scratch/k16_rf_halo_j_family_20260730/rank1_j3959.targets
SHA-256 edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee
```

and separates three logically different questions:

1. whether an abstract service block is internally resident;
2. whether its endpoint signature fits a destination port; and
3. whether the physical rows can be removed from their native positions and
   the source gaps closed.

The first two questions have a complete finite answer below.  They do not by
themselves give a target-multiset-preserving braid.

## 1. The nested-chain block census

Put

```text
Hc=ca79, He=ea79, Hb=eb79,
A=4a79, C0=4e39, C1=4d39.
```

Consider ordered blocks

\[
 M=(V_0,V_1,V_2,A,C_0,C_1).                         \tag{1.1}
\]

The three variable domains are

\[
\begin{aligned}
V_2&\in\binom{H_c}{8},&V_2\vee A&=H_c,\qquad &&|\mathcal V_2|=8,\\
V_1&\in\binom{H_e}{8},&V_1\cap(H_e\setminus H_c)&\ne\varnothing,
&&|\mathcal V_1|=36,\\
V_0&\in\binom{H_b}{8},&V_0\cap(H_b\setminus H_e)&\ne\varnothing,
&&|\mathcal V_0|=120.
\end{aligned}                                      \tag{1.2}
\]

Thus there are exactly

\[
 8\cdot36\cdot120=34560                              \tag{1.3}
\]

raw blocks.  Rejecting a block precisely when it has a positive coordinate
run of length one or two bounded on both sides inside the block leaves

\[
 \boxed{5166}                                        \tag{1.4}
\]

internally depth-two-resident blocks.  Every survivor satisfies

\[
\begin{aligned}
V_2\vee A&=\mathtt{ca79},\\
V_1\vee V_2\vee A&=\mathtt{ea79},\\
V_0\vee V_1\vee V_2\vee A&=\mathtt{eb79},\\
A\vee C_0&=\mathtt{4e79}.
\end{aligned}                                      \tag{1.5}
\]

For each coordinate, record at each endpoint the bit value and the length
of the maximal constant endpoint run, capped at three.  The 5,166 blocks
have exactly

\[
 \boxed{4866}                                        \tag{1.6}
\]

such full endpoint signatures: 4,566 occur once and 300 occur twice.  This
reproduces the root census from the definitions, without reading its block
list.

## 2. Exact depth-two seam criterion

For a resident word fragment \(F\), let

\[
 P_t(F),S_t(F)\quad(t=1,2,3)
\]

be the coordinates whose leading, respectively trailing, positive run has
length exactly one, exactly two, or at least three.  If \(L\) is placed
immediately before \(R\), then the new seam is depth-two resident if and
only if

\[
\begin{aligned}
S_1(L)&\subseteq P_2(R)\cup P_3(R),\\
S_2(L)&\subseteq P_1(R)\cup P_2(R)\cup P_3(R),\\
P_1(R)&\subseteq S_2(L)\cup S_3(L),\\
P_2(R)&\subseteq S_1(L)\cup S_2(L)\cup S_3(L).
\end{aligned}                                      \tag{2.1}
\]

Indeed, this is the four-case check for a coordinate run of length one or
two meeting the seam.  Runs already of length at least three impose no
condition, and zero-zero coordinates create no positive run.  Hence (2.1)
is necessary and sufficient coordinatewise.

The frozen flats are at starts 6433, 12869, and 12871.  Requiring the three
rows used to read each side of a seam to lie wholly in the constant
depth-two sector gives the 6,429 safe cuts

\[
 6438\le p\le12866.                                  \tag{2.2}
\]

The full 4,866-state signature collapses to 2,551 positive-run types for
this seam question.  Applying (2.1) on both sides of (1.1) gives:

```text
safe cuts accepting at least one M block       34
positive types accepted somewhere            2037
individual M blocks accepted somewhere       4472
type-cut edges                                9842
block-cut edges                              26227
```

The 34 cuts are

```text
6490,6622,6623,6901,7074,7109,7155,7293,7565,7621,7624,
7832,7833,7834,7877,8237,9081,9373,9500,9783,10229,10238,
10368,10568,10751,10900,11250,11258,11259,11265,11277,
11405,11912,12239.
```

In particular, cut 6490 has left and right collars

```text
b742,a762,a572 | a53a,a13b,b03b
```

and accepts the block

```text
a179,a279,8a79,4a79,4e39,4d39.                       (2.3)
```

Direct coordinate-run replay on the resulting 12-row word finds no bounded
positive run shorter than three.  Thus boundary residence is genuinely
possible for the nested-chain block; the canonical fixed-flank failure is
not an invariant of all 5,166 blocks.

## 3. Complete classification of minimal `6f79` blocks

Let \(U=\mathtt{6f79}\), of rank eleven.  A minimal rank-eight realization
of \(U\) has two rows \((X,Y)\) with \(X\vee Y=U\).  Necessarily

\[
 X=I\mathbin{\dot\cup}A',\qquad
 Y=I\mathbin{\dot\cup}B',                            \tag{3.1}
\]

where \(|I|=5\), \(|A'|=|B'|=3\), and
\(U=I\mathbin{\dot\cup}A'\mathbin{\dot\cup}B'\).  Conversely every such
ordered partition works.  Hence

\[
 |\mathcal Y|=\binom{11}{5}\binom63=9240,             \tag{3.2}
\]

or 4,620 modulo reversal.  All 9,240 blocks are internally depth-two
resident, have rank-five intersection, and have distinct full capped
endpoint signatures.  Two rows are minimal because one rank-eight row
cannot have rank-eleven OR.

### The two-row port lemma

At a cut write the two left rows as \(L_{-2},L_{-1}\), the two right rows
as \(R_0,R_1\), and put

\[
 L_2=L_{-2}\cap L_{-1},\quad
 R_2=R_0\cap R_1,\quad
 K=L_{-1}\cup R_0.                                   \tag{3.3}
\]

Let \(S_1,S_2\) be the trailing short-run sets on the left and
\(P_1,P_2\) the leading short-run sets on the right.  Then insertion of
the entire block \((X,Y)\) at this cut is depth-two resident if and only if

\[
\begin{aligned}
A'&\subseteq L_2,& B'&\subseteq R_2,& I&\subseteq K,\\
S_1\cup P_1&\subseteq I,& S_2&\subseteq A'\cup I,&
P_2&\subseteq B'\cup I.                              \tag{3.4}
\end{aligned}
\]

For example, a coordinate in \(A'\) has trace `10` inside the block, so it
needs two preceding ones; a coordinate in \(I\) has trace `11`, so it needs
one continuation on at least one side.  The last three conditions are the
same argument applied to runs inherited from the two surrounding fragments.
This proves necessity and sufficiency.

For each coordinate of \(U\), (3.4) gives a list of allowed classes among
\(A',B',I\), of capacities 3,3,5.  On every one of the 6,429 safe cuts,
failure occurs before any nontrivial capacitated Hall test:

* either a short inherited run demands a coordinate outside \(U\); or
* one coordinate of \(U\) has an empty class list.

The deterministic one-coordinate certificate census is

| certificate | cuts |
|:--|--:|
| outside `U`, bit 1 | 1450 |
| outside `U`, bit 2 | 1083 |
| outside `U`, bit 7 | 1042 |
| outside `U`, bit 12 | 818 |
| outside `U`, bit 15 | 4 |
| empty list, bit 0 | 883 |
| empty list, bit 3 | 550 |
| empty list, bit 4 | 280 |
| empty list, bit 5 | 167 |
| empty list, bit 6 | 81 |
| empty list, bit 8 | 47 |
| empty list, bit 9 | 17 |
| empty list, bit 10 | 6 |
| empty list, bit 11 | 1 |

These counts sum to 6,429.  Therefore

\[
 \boxed{\text{no minimal two-row `6f79` block fits any safe depth-two cut.}}
                                                               \tag{3.5}
\]

This is a solver-free obstruction: each cut carries a single-coordinate
certificate.

### Sharpness: one extra row gives a destination port

The two-row obstruction is sharp at the boundary-signature level.  At cut
6622 the collar

```text
c74a,c56a,e562 | e532,b532,b1b2
```

accepts the three-row block

```text
2a79,6a39,4f19.                                      (3.6)
```

Its full OR is `6f79`, whereas its two adjacent pair ORs are respectively
`6a79` and `6f39`.  Hence the target is first realized by the entire
three-row block.  This block is row-disjoint from (2.3), and simultaneous
insertion of (2.3) at cut 6490 and (3.6) at cut 6622 has exact depth-two
positive-run replay throughout the interval joining the two ports.

This is a destination certificate only: it inserts nine extra rows.  The
nine physical donors are unique, and their source gaps have not been
closed.  The three rows in (3.6) occur at

```text
2a79 @ 913,       4f19 @ 1633,       6a39 @ 4513,
```

all in the depth-three sector.  The combined local replay spans original
rows `[6487,6625)` and has zero bounded positive-run defects.

## 4. Native cross-fragment seams

There is a different way to obtain the same upper witness.  Keep the native
left context ending at the unique occurrence of \(X\), keep the native
right context beginning at an occurrence of \(Y\), and join the two
fragments by the new seam \(X-Y\).  Criterion (2.1) is exact for this join.

Among the 9,240 ordered value pairs, exactly 933 admit at least one such
native join.  There are 940 physical occurrence edges because
`4e71`, which is below `6f79`, occurs twice at the first flat.  Their sector
distribution is

| native left sector | native right sector | physical edges |
|:--|:--|--:|
| depth 3 | depth 3 | 898 |
| first flat | depth 3 | 25 |
| depth 3 | first flat | 4 |
| depth 3 | depth 2 | 8 |
| depth 2 | depth 3 | 5 |

There is no depth-two-to-depth-two edge.  For example,

```text
2765,2771,0779 | 6939,693c,6d34
```

is valid, with `0779 | 6939 = 6f79`, but both endpoints are native to the
depth-three sector.

Consequently a minimal-pair `6f79` service is possible by a native fragment
join, but not inside a braid whose participating endpoint contexts all
remain in the depth-two sector.  It must import a depth-three/first-flat
endpoint or change at least one endpoint signature.  Alternatively, the
three-row destination block (3.6) stays wholly in depth two.

## 5. Source-donor closure is an independent obstruction

The fixed rows of every block (1.1) occur uniquely at

```text
4a79 @ 3959,       4e39 @ 4620,       4d39 @ 4621.
```

They lie in the depth-three sector, where every positive run must have
length at least four.  If `4a79` is removed while the residual order is
kept, the following original runs are shortened:

```text
bit 3: [3956,3960), length 4 -> 3;
bit 4: [3957,3961), length 4 -> 3.
```

If the adjacent pair `4e39,4d39` is removed, then

```text
bit 4: [4620,4625), length 5 -> 3;
bit 9: [4617,4621), length 4 -> 3.
```

Thus residual-order singleton extraction of the fixed suffix is impossible
even when the destination port is valid.  If each source gap is repaired by
one returned row, the row at the first gap must contain `0018` and the row
at the second must contain `0210`.  The two gaps are disjoint, so this is a
two-return floor for that extraction normal form.

This does not rule out moving larger source fragments or giving the source
gaps different flanks.  It does prove that a destination signature edge is
not a literal splice certificate.

## 6. Exact conclusion and remaining braid class

The classification gives the following sharp architecture-specific result.

> A compound splice consisting of one six-row block (1.1) and one minimal
> two-row `6f79` block, with all destination and native endpoint contexts
> confined to the frozen depth-two sector, does not exist.

There are two independent reasons: (3.5) closes direct two-row insertion,
and the native cross-fragment graph has no depth-two-to-depth-two edge.

This does **not** exclude a buffered depth-two service.  Equation (3.6)
proves that one extra row already removes the destination obstruction.  The
remaining obstruction to a literal compound splice is source closure:
extracting the fixed suffix of the otherwise-compatible nested block opens
the two depth-three source defects in Section 5, and extracting the three
rows of (3.6) creates three additional donor gaps.

The obstruction is deliberately scoped.  A surviving literal braid may
still:

1. use one of the 34 valid nested-block destination cuts;
2. import a depth-three or first-flat `6f79` endpoint;
3. use the explicit three-row port (3.6), or another buffer changing an
   endpoint signature;
4. move larger donor fragments to close the two fixed source gaps; and
5. then pass maximal-envelope reconstruction, arbitrary-upper preservation,
the private-top condition, and the lower Hall compiler.

No claim about those later gates is made here.

## Reproducibility

```text
scratch/audit_k16_j3959_service_signature_graph_independent_20260730.py
SHA-256 bf99d59495d7863fd15b84d2a9a361e0c2f5ab73bcf7d24379eb3ccf44f2ec8c

scratch/k16_j3959_service_signature_graph_independent_20260730.audit.json
SHA-256 ebdc97473afec3f1f387e5beb10f8805bda367cd0913dd2f8a665f06c2ed6091
payload ef1e2b7d03acf7a83572f96a924ba24ea20f4ac012db2e2583b2f13e1082079b
```

The script performs no SAT call and no segment-permutation search.  Its
largest explicit families have 34,560 and 9,240 members.
