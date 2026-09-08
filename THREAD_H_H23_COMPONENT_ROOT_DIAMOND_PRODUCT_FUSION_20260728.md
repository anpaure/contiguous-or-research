# Hall 23 by direct product-box fusion and a reusable component-root diamond theorem

Date: 2026-07-28

Status: proved an exact component-root discharge theorem, identified the
H24-to-H23 compound as one direct seven-box braid, and audited its complete
DM/matching mechanism.  The next Hall-22 gate is reduced to saturating any
one of the 23 unit-defect H23 components.  No Hall-22 word, global common-word
compiler, exact `k=15` formula, or coefficient-one theorem is claimed.

## 1. Authoritative result

The certified branch is

\[
 H24\xrightarrow{\operatorname{FF}(212,3732,4717)}H24^{\rm portal}
 \xrightarrow{\operatorname{FF}(210,1501,4867)}H23.             \tag{1.1}
\]

Every state in (1.1) is a permutation of all `6435` rank-eight masks, is a
Johnson path, is depth-three resident, and has complete upper support at
every depth `1,...,7`.  The immediate-lower hole count remains four.

The full lower hole vector is not fixed: it changes from

\[
                         (4,19,4,1,0,0,0)
 \quad\hbox{to}\quad (4,19,6,1,0,0,0),              \tag{1.2}
\]

losing the depth-three lower targets `17445` and `28677`.  Thus “lower holes
remain four” means the immediate lower layer only.

The final carrier has matching size `16360`, deficiency `23`, and the same
seven degree-zero targets

\[
 2575,5801,13616,13620,17738,21641,29776.           \tag{1.3}
\]

## 2. The two moves are one direct seven-box braid

Cut the H24 path (Q) into

\[
\begin{aligned}
 A&=Q[0,210),& B&=Q[210,212),& C&=Q[212,515),\\
 D&=Q[515,3732),& E&=Q[3732,4718),\\
 F&=Q[4718,4868),& G&=Q[4868,6435).
\end{aligned}                                                     \tag{2.1}
\]

### Theorem 2.1 (literal direct fusion)

The final H23 chronology is exactly

\[
                  oxed{A,D,F,B,E,C,G}.       \tag{2.2}
\]

In particular, (1.1) is one six-seam braid moving all five interior boxes;
no legal intermediate word is needed to define the final construction.

#### Proof

The first `FF` move writes

\[
 Q[0,212),Q[3732,4718),Q[212,3732),Q[4718,6435).
\]

In this word, the second cuts at positions `210,1501,4868`.  Pulling them
back to (Q) gives the additional old positions `210,515,4868`.  Splitting
at the union

\[
                         210,212,515,3732,4718,4868
\]

and applying the second `FF` order gives (2.2).  Direct materialization is
identical, entry for entry, to the frozen H23 path.  \(\square\)

The six old seam pairs are

\[
\begin{gathered}
(30469,30245),(29741,25709),(22279,30215),\\
(30765,28781),(27693,26733),(22309,22055),
\end{gathered}                                                     \tag{2.3}
\]

and the six new pairs are

\[
\begin{gathered}
(30469,30215),(30765,26733),(22309,30245),\\
(29741,28781),(27693,25709),(22279,22055).
\end{gathered}                                                     \tag{2.4}
\]

Every pair in (2.4) is Johnson-adjacent.  The lower flag multiset on both
sides is

\[
       \{22023,22053,25645,26669,28717,30213\},     \tag{2.5}
\]

and the upper flag multiset is

\[
       \{22311,27757,29805,30471,30501,30829\}.     \tag{2.6}
\]

The signed flag recoupling is two alternating `C6` cycles; on the six upper
ports its permutation is

\[
                         (1\ 3\ 6)(2\ 5\ 4).        \tag{2.7}
\]

The two cycles are interlaced by the physical block order (2.2).  This is
the exact product-box fusion mechanism: portwise-neutral cycles need not act
independently at the deeper compiler.

The two-state block (B) has length two.  Hence its depth-three dependency
collars overlap, and a sum of isolated seam ledgers is invalid.  Direct full-
signature cancellation gives

\[
 |H|=19282,qquad |B^-|=|B^+|=29,                  \tag{2.8}
\]

and

\[
 \nu(H)=16336,qquad
 \operatorname{cap}_H(B^-)=23,qquad
 \operatorname{cap}_H(B^+)=24.                    \tag{2.9}
\]

The separate steps have banks `13` and `25` per side.  Thus the direct bank
recycles

\[
                         13+25-29=9                 \tag{2.10}
\]

profiles.  This is a literal nonadditive saving, not an asymptotic estimate.

## 3. A general component-root discharge theorem

Let (G_j=(L,R_j;E_j)), (j=0,1,2), be target/cell bipartite graphs.  Suppose
the target-reachable DM region at the neutral state (G_1) splits into

\[
                        (C_i,D_i),\qquad 0\le i<d,   \tag{3.1}
\]

where

\[
 D_i=N_{G_1}(C_i),qquad |C_i|=|D_i|+1,             \tag{3.2}
\]

and every (D_i) can be saturated by a matching into (C_i).  Let
(C=C_0).

For a component (X\subseteq L), define the multiset of projected cell
columns

\[
 \mathcal P_X(G)=
 \{N_G(y)\cap X:y\in R, N_G(y)\cap X\ne\varnothing\},           \tag{3.3}
\]

with physical-cell multiplicity.

### Theorem 3.1 (neutral associator plus diamond discharge)

Assume:

1. for every (i\ge1), the projected multiset
   \(\mathcal P_{C_i}(G_j)\) is independent of (j), and no changed cell
   meets two distinct components;
2. one matching covers every target exterior to the DM components and
   saturates every (D_i), (i\ge1), throughout all three graphs;
3. on (C), after projected common-column cancellation, the first move is

   \[
          \{P\cup Q,R\}\longrightarrow\{Q,P\cup R\},            \tag{3.4}
   \]

   for pairwise disjoint nonempty target sets (P,Q,R); the common core
   plus either two-column bank has rank (|C|-1);
4. after projected common-column cancellation, the second move is

   \[
       \{P,Q,T\}\longrightarrow
       \{P_0,P_1,Q_0,Q_1,T_1\},                                  \tag{3.5}
   \]

   where

   \[
       P=P_0\sqcup P_1,quad Q=Q_0\sqcup Q_1,quad
       T=T_0\sqcup T_1;                                         \tag{3.6}
   \]

   the common core leaves a four-target set (U), the old three columns
   have an SDR of size three in (U), and the five new columns have an SDR
   saturating (U).

Then

\[
 \nu(G_0)=\nu(G_1)=|L|-d,qquad
 \nu(G_2)=|L|-(d-1).                              \tag{3.7}
\]

Thus the first move is rank-neutral, while the second discharges the whole
unit-defect component (C).

#### Proof

On (C), the common matching plus either bank in (3.4) matches
(|C|-1) targets.  The shore (C) has only (|C|-1) relevant right cells,
so this is exact.  In (3.5), the common matching saturates (C\setminus U),
and the displayed four-address SDR saturates (U); hence (C) is fully
matched in (G_2).

By assumptions 1--2, the exterior matching and the matchings on
(C_i,D_i), (i\ge1), are disjoint from this local matching.  Their union
therefore leaves exactly (d), (d), and (d-1) targets unmatched in the
three graphs.  Conversely, the union of the untouched (d-1) component
shores has gap (d-1) in (G_2).  This gives the matching upper and lower
bounds in (3.7).  \(\square\)

The current of the neutral associator is explicit.  For a shore (X), put

\[
 p={\bf1}[X\cap P\ne\varnothing],quad
 q={\bf1}[X\cap Q\ne\varnothing],quad
 r={\bf1}[X\cap R\ne\varnothing].                  \tag{3.8}
\]

Then

\[
 I_N(X)=q+(p\vee r)-(p\vee q)-r=p(q-r).             \tag{3.9}
\]

In particular (I_N(C)=0), but currents on proper subshores can change.
This is why the neutral step can be essential.

For the diamond, let (p_i,q_i,t_i) be the corresponding hit indicators.
Its current is

\[
\begin{split}
 I_D(X)={}&{f1}[p_0=p_1=1]
          +{f1}[q_0=q_1=1]\\
          &-{f1}[t_0=1,t_1=0].                    \tag{3.10}
\end{split}
\]

Indeed, subtract (p_0\vee p_1), (q_0\vee q_1), and
(t_0\vee t_1) from the five new-cell indicators.  On the full component,
(I_D(C)=2): two new cell occurrences appear, but only one additional rank
is needed to saturate (C).

### Corollary 3.2 (parallel component discharge)

If (s) such packets act on pairwise target/right-disjoint DM components,
their common exterior matching survives, and their physical collars are
disjoint or are recomputed as one exact macro-collar, then matching rank
rises by (s).

This is the rigorous repeatability statement.  Equal component cardinality
alone does not supply the required four-address SDR or a physical braid.

## 4. Exact Boolean-diamond packet at root 20516

Use zero-based bit coordinates and put

\[
 K=20516=\{2,5,12,14\},quad
 a=0,quad b=13,quad c=10,quad e=3,quad f=11.     \tag{4.1}
\]

For a bit set (S), write (K+S=K\cup S).  Define

\[
\begin{aligned}
 P&=\{K,K+a,K+b,K+a+b\},\\
 Q&=\{K+c+a,K+c+b,K+c+a+b\},\\
 R&=\{K+f,K+f+a,K+f+b,K+f+a+b\},\\
 T&=\{K+e,K+e+a,K+e+b,K+e+a+b\}.                  \tag{4.2}
\end{aligned}
\]

The neutral braid realizes exactly (3.4).  Its projected common core has
rank `158`; either boundary bank contributes two further ranks, giving

\[
                         160\longrightarrow160.      \tag{4.3}
\]

For the improving braid, one unchanged projected column cancels first.  The
remaining old columns are (P,Q,T), and the new columns are

\[
\begin{array}{c|l}
P_0&20516,20517\\
P_1&28708,28709\\
Q_0&21541\\
Q_1&29732,29733\\
T_1&28716,28717.
\end{array}                                                       \tag{4.4}
\]

The projected common core has rank `157` and can leave

\[
                 U=\{20517,28709,28717,29733\}.      \tag{4.5}
\]

The old cells cover only three addresses, for example

\[
 P\mapsto20517,qquad Q\mapsto29733,qquad T\mapsto28717,         \tag{4.6}
\]

while the new bank covers all four:

\[
 P_0\mapsto20517,quad P_1\mapsto28709,quad
 T_1\mapsto28717,quad Q_1\mapsto29733.             \tag{4.7}
\]

Thus the component rank is

\[
                         160\longrightarrow161.      \tag{4.8}
\]

The component has `161` targets and `160` old neighbours.  Its target rank
profile in ranks four through seven is

\[
                         (1,9,43,108),               \tag{4.9}
\]

and every target contains the root (20516).  After the compound it has
`162` neighbour occurrences and matching rank `161`; the entire component
disappears from the canonical DM shore, with no replacement target added.

The direct full-signature calculation is slightly smaller than the sum of
the projected steps: on this component its common rank is `155`, and its
contracted boundary contribution rises `5 -> 6`.  Globally the direct
contraction is (2.8)--(2.9).

If (X_0,X_1,X_2) are the canonical DM shores of H24, the portal state, and
H23, their cross-gap matrix is

\[
 \begin{pmatrix}
 24&24&23\\
 24&24&23\\
 22&22&23
 \end{pmatrix}.                                     \tag{4.10}
\]

The final shore was already a gap-23 shore before either move.  The compound
removes exactly the extra root component.

## 5. Exact H23 decomposition and the next H22 gate

The H23 canonical DM shore has

\[
                         |S_{23}|=1007,qquad |N(S_{23})|=984,    \tag{5.1}
\]

rank profile

\[
                         (6,54,274,673),             \tag{5.2}
\]

and target digest

```text
88895c0ced520217a65802ba03060bf7ff2ed3aec192c90c6e666585f76b5c89.
```

It has exactly 23 connected components, each of gap one:

| size targets/cells | roots |
|---|---|
| `169/168` | `1920` |
| `161/160` | `960, 8217, 24610` |
| `160/159` | `449, 8218` |
| `5/4` | `4213, 7504` |
| `3/2` | `1103, 18970` |
| `2/1` | `2420, 2676, 4877, 9524, 17683, 19568` |
| `1/0` | `2575, 5801, 13616, 13620, 17738, 21641, 29776` |

Each root is the intersection of all target masks in its component.

### Theorem 5.1 (native common-word transversal)

On every one of the `984` right cells of the H23 canonical DM shore, take
the native target equal to the union of its maximal-controller positions.
These `984` targets are distinct, every target/cell pair is a literal
compiler incidence, and their complement in the `1007`-target shore is
exactly the set of 23 component roots displayed in the table.

#### Proof

For a cell (c=(h,s)), its native target is

\[
                         \tau(c)=\bigcup_{p=s}^{s+h}P_p,          \tag{5.3}
\]

where (P) is the maximal erosion controller of H23.  By construction this
target contains the mandatory mask, meets every controller position of the
cell, and lies in the envelope, so it is adjacent to (c).  Direct audit of
the 984 DM-right cells finds 984 different values of \(\tau\).  Subtracting
them from the canonical DM target list gives precisely the 23 roots.  Since
all native targets are realized simultaneously by the one word (P), this
is a common-word transversal, not 984 separate rankwise choices.  \(\square\)

Thus the next descent has an especially small literal form: retain or rematch
the 984 native pairs and add one additional physical pin for any one root.
Replacing one native target by a root is only a Robin--Hood swap and does not
increase rank.

### Corollary 5.2 (sharp H22 sufficient condition)

To reach Hall deficiency at most `22`, it is enough to find one resident,
all-upper-safe macro which:

1. preserves a maximum matching outside one listed component (C);
2. gives (C) a matching of size (|C|) on right cells disjoint from that
   exterior matching.

The union of the other 22 components remains a gap-22 shore, so the final
deficiency is then exactly `22`.

For a zero component (C=\{z\}), this condition is simply a genuinely free
new candidate cell for (z).  It would simultaneously give `H22` and lower
the zero count to six.  The separate Pareto branch proves that target `2575`
can be made nonzero in a legal/common-controller branch, but that branch
does not preserve the Hall-23 matching and therefore does not satisfy this
corollary.

The three remaining `161/160` components have the same size/rank census as
one another, but equal census does not prove port isomorphism, chronology
compatibility, or the four-address leave (4.5).  A transported diamond is
valid only after those data are exhibited literally.

### Theorem 5.3 (H23 one-braid local minimum)

The complete resident, all-upper-safe `FF/RF/FR/RR` catalogue at H23 has

```text
553356 Johnson candidates,
12001 resident candidates,
9143 all-upper-safe candidates.
```

Its minimum ordered score `(Hall deficiency, zero count)` is `(23,7)`.
There is no Hall-22 move and no move with at most six zero targets.  Thus the
next descent must be a compound/multiblock move or leave this catalogue.

The deterministic native scan used carrier SHA-256

```text
8feab1da65f3924d29609246798fc543dc50d076ca9db363e8796dda2c22598d
```

and source SHA-256

```text
889379685f55e1938f24fceffd889951332966fe547021874b5482b1c2fa7d29.
```

An exact seam-collar filter finds only three one-braids which give any old
zero target a candidate:

| move | gained old zero | final score | newly zero targets |
|---|---:|---:|---|
| `FR(236,3020,3221)` | `5801` | `(23,8)` | `4781,5929` |
| `FF(1816,2084,5151)` | `13616` | `(27,8)` | `22192,29745` |
| `FF(3501,4289,5413)` | `2575` | `(26,10)` | `1567,2095,3117,3119` |

Hence a one-braid zero portal always opens at least two replacement zero
holes in this catalogue.

#### Proof

For each first cut, the native enumerator lists every possible new endpoint
among the Johnson neighbours of the exposed state and then every compatible
second and third endpoint.  These four loops are exactly the four
`FF/RF/FR/RR` endpoint normal forms, so the catalogue is exhaustive.  Each
materialized candidate is tested for every depth-three run and every upper
last witness through depth seven; the surviving `9143` words receive an
exact compiler graph and maximum matching.  The terminal minimum is
`(23,7)`.  The separate zero filter recomputes every affected cell using its
full dependency interval `[s-6,s+h+3]`, mandatory mask, envelope, and
nonempty-hit test; it returns exactly the three rows above.  \(\square\)

The smallest exact replacement lemma is:

> **H23 component-root selector (unproved).**  For one of the sixteen
> nonzero H23 components, construct a deck-exact, resident, all-upper-safe
> compound of at least two elementary braids whose direct common-signature
> contraction saturates that component
> and preserves the 984 native DM pairs (or an equally large rematching) and
> a maximum matching on the exterior.  The strongest version uses one of the
> seven zero singletons and simultaneously reaches zero count six.

Hall descent is still not the complete finite formula.  The immediate lower
holes must ultimately fall from four to at most two, the depth-two holes from
nineteen to at most five, and one injective target/cell assignment must pass
the common physical word test.

## 6. Adversarial audit

1. The two new cells in the diamond give current `+2`, but component rank
   rises only one.  Cell count alone is not a matching proof; (4.5)--(4.7)
   are essential.
2. The neutral associator is not shorewise neutral.  Equation (3.9) shows
   its proper-subshore current, which is precisely how it moves the active
   obstruction.
3. Componentwise reasoning is valid only with the no-cross-column and common
   exterior-matching hypotheses.  Otherwise two nominal components may
   compete for one physical right cell.
4. The short block in (2.1) makes isolated collar addition invalid.  The
   authoritative Hall certificate is the direct 29-profile bank.
5. Immediate lower holes stay four, but lower depth three worsens to six.
6. The theorem proves an outer target/cell matching gain.  It does not select
   one global common word or prove coefficient one.

## 7. Frozen artifacts

The direct product-box verifier is

```text
scratch/audit_k15_h24_h23_direct_seven_box_fusion.py
```

with SHA-256

```text
569a69c713571ae7a327cbef261ce3b8dcac53e937b5245bc886d64a22ae98e1.
```

The frozen H23 file is

```text
scratch/k15_segment_braid_hall23.json
```

with file SHA-256

```text
8feab1da65f3924d29609246798fc543dc50d076ca9db363e8796dda2c22598d
```

and middle-list digest

```text
09b779278edaff5d00d4ef119a1ae6d15df8858557a3c700d9cac4764ef9c66b.
```

The H25-to-H24 direct product-box verifier is

```text
scratch/audit_k15_h25_direct_seven_box_fusion.py.
```
