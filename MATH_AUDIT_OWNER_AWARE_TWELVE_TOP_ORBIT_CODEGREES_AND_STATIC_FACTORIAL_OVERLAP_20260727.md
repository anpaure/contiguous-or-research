# Owner-aware twelve-top macros have the right static overlap scale, but matching them is already the owner-resolution theorem

Date: 2026-07-27

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
 \qquad N=\binom nM,\qquad W=\binom nm,
\]

and use the repaired twelve-top macro from
`MATH_THEOREM_TWELVE_TOP_HISTOGRAM_NEUTRAL_BIDIRECTIONAL_RECHARGE_20260727.md`.
Thus one (old, equivalently new) shore uses twelve distinct rank-\(M\)
tops and a squarefree set of \(12d\) rank-\(m\) middle owners.  Let
\({\cal P}\) be one fixed fully decorated macro and let
\({\cal H}_{12}=S_n{\cal P}\) be its **simple** relabelling orbit;
parallel labelled descriptions of one support are collapsed.

The owner-aware catalogue has two vertex orbits.  If \(E=|{\cal H}_{12}|\),
their exact degrees are

\[
 D_T={12E\over N},\qquad D_O={12dE\over W},\qquad
 {D_O\over D_T}=\rho:={dN\over W}.                 \tag{0.1}
\]

At the critical choice \(H=\lceil\sqrt{m\log m}\rceil+O(1)\),
\(\rho=1-o(1)\).  Hence the top and owner capacities are calibrated.

The complete static audit is favorable:

1. the maximum pair codegree divided by the smaller degree is
   \(O(m^{-2})\);
2. for every resource \(x\in{\cal P}\), every \(1\le p\le C_0\log m\),

   \[
   {1\over D_x}\sum_{\substack{P'\ni x\\P'\ne P}}
      (|P\cap P'|-1)_p
      \le (Cp)^{Cp}m^{-2};                         \tag{0.2}
   \]

3. the anchored first overlap moment is \(O(m^{-2})\), and the
   edge-local sum is \(\Theta(m^{-1})\).

Thus the repaired palette separation and the union-of-twelve-paths
geometry suppress static macro overlaps to the same orders as ordinary
promotion frames and domino twins.  In particular there is no static
pair-spread or finite factorial-overlap obstruction.

This still does **not** give an owner-aware matching.  The edge size is

\[
                         12+12d=\Theta(m),           \tag{0.3}
\]

and the known fixed-uniformity theorem is unavailable.  More
importantly, a matching of \((1-o(1))N/12\) augmented macros is itself a
near-perfect retained-window owner resolution: it selects one physical
word on almost every top and partitions \(W-o(W)\) middle owners.  Thus
the desired matching already contains the promotion-ring/SCD
factorization gate; it is not a consequence of the abstract twelve-top
packing.

## 1. Exact orbit-enumerator formula

The following observation gives every degree and higher codegree, not
just bounds.  If \(\Omega\) is an \(S_n\)-orbit of ordered injective
\(r\)-tuples of resources (tops and/or owners), write

\[
 a_\Omega(P)=\#\{(z_1,\ldots,z_r)\in P^r_{\ne}:
                    (z_1,\ldots,z_r)\in\Omega\}.
\]

Every tuple in \(\Omega\) has the same codegree, and double counting
\((P',(z_1,\ldots,z_r))\) gives the exact identity

\[
 \boxed{d(\Omega)={E\,a_\Omega(P)\over|\Omega|}.}    \tag{1.1}
\]

For pairs this becomes especially explicit.  Put

\[
 v^{TT}_r=\binom Mr\binom{n-M}{M-r},\qquad
 v^{TO}_j=\binom Mj\binom{n-M}{m-j},\qquad
 v^{OO}_t=\binom mt^2.                                \tag{1.2}
\]

Let \(A^{TT}_r,A^{TO}_j,B_t\) be the numbers of ordered internal
top--top, top--owner and distinct owner--owner pairs of the indicated
intersection type, where owner distance is
\(t=m-|X\cap Y|\).  Then

\[
 {d^{TT}_r\over D_T}={A^{TT}_r\over12v^{TT}_r},\qquad
 {d^{TO}_j\over D_T}={A^{TO}_j\over12v^{TO}_j},\qquad
 {d^{OO}_t\over D_O}={B_t\over12d\,v^{OO}_t}.         \tag{1.3}
\]

Equation (1.1) is also the promised exact higher-overlap formula.

## 2. Top and top--owner pairs

The twelve tops are the edges of \(K_6\) minus a perfect matching,
adjoined to one common \((M-2)\)-core.  This graph has 36 unordered
adjacent edge pairs and 30 unordered disjoint edge pairs.  Hence

\[
 A^{TT}_{M-1}=72,\qquad A^{TT}_{M-2}=60,
\]

and (1.3) gives exactly

\[
 {d^{TT}_{M-1}\over D_T}={6\over M(n-M)},\qquad
 {d^{TT}_{M-2}\over D_T}
 ={20\over M(M-1)(n-M)(n-M-1)}.                       \tag{2.1}
\]

All other top-pair codegrees vanish.

Every owner in the packet lies in one of its twelve tops, while any two
packet tops differ in at most two coordinates.  Therefore

\[
 A^{TO}_j=0\quad\hbox{unless }j\in\{m,m-1,m-2\}.
\]

Since \(A^{TO}_j\le144d\), and the smallest denominator in these three
classes is \(v^{TO}_m=\binom MH\),

\[
 \max_j{d^{TO}_j\over D_T}
 \le {12d\over\binom MH}.                              \tag{2.2}
\]

At the Gaussian calibration this is smaller than every fixed inverse
power of \(m\).

## 3. A cyclic-window ball lemma

The owner calculation uses a short deterministic fact.

### Lemma 3.1

Let \(V\) be an \(M\)-set with a cyclic order, \(M>3H\), and let
\({\cal I}\) be any subfamily of its cyclic \(H\)-intervals.  For an
arbitrary \(m\)-set \(X\) and integer \(h<H/2\),

\[
 \#\{I\in{\cal I}:d_J(X,V\setminus I)\le h\}\le2h+1.  \tag{3.1}
\]

In particular the bound is three when \(h=1\).

#### Proof

Put \(a=|X\setminus V|\).  If the displayed set is nonempty then
\(a\le h\).  For two eligible intervals \(I,J\), each differs in at
most \(h\) positions from the same set \(V\setminus X\), with the
obvious \(H+a\)-set interpretation when \(a>0\).  Directly,

\[
 |I\setminus J|\le |I\setminus(V\setminus X)|
                    +|(V\setminus X)\setminus J|\le2h.
\]

For two length-\(H\) intervals whose cyclic start separation is \(r\),
their Johnson distance is
\(\min\{r,M-r,H\}\).  Hence every two eligible starts have cyclic
distance at most \(2h\).  Since \(M>6h\), a subset of an \(M\)-cycle
whose pairwise cyclic distances are at most \(2h\) lies in one arc of
\(2h+1\) consecutive starts (otherwise three successive gaps would
sum to at most \(6h\)).  This proves (3.1). \(\square\)

For \(h=1\) and \(|X\setminus V|=1\), the sharper bound two follows
because the deleted interval must be an \(H\)-subset of the fixed
\((H+1)\)-set \(V\setminus X\), but three is sufficient below.

Since the macro owner support is a disjoint union of twelve retained
interval-complement paths, Lemma 3.1 gives

\[
 |B_{J}(X,h)\cap O(P)|\le12(2h+1)\qquad(h<H/2).          \tag{3.2}
\]

This is where the repaired squarefreeness is essential: occurrences
and owner resources coincide.

## 4. Owner-pair codegrees

For a fixed owner occurrence, (3.2) with \(h=1\) gives at most 36
other packet owners at Johnson distance one.  Consequently

\[
 B_1\le 12d\cdot36,
 \qquad
 {d^{OO}_1\over D_O}\le {36\over m^2}.                 \tag{4.1}
\]

For \(t\ge2\), squarefreeness alone gives

\[
 {d^{OO}_t\over D_O}\le {12d-1\over\binom mt^2}
 \le O(m^{-3}),                                         \tag{4.2}
\]

and \(B_t=0\) for \(t>H+2\), because two packet owners lie in tops
whose union has size at most \(M+2\).

Equations (2.1), (2.2), (4.1), and (4.2), together with \(\rho=1-o(1)\),
prove

\[
 \boxed{\Delta_2/d_{\min}=O(m^{-2}).}                   \tag{4.3}
\]

## 5. Edge-local first overlap

For \(x\in P\), define

\[
 \beta_P(x)={1\over D_x}\sum_{P'\ni x}(|P\cap P'|-1)
            =\sum_{y\in P\setminus\{x\}}{d(x,y)\over D_x}. \tag{5.1}
\]

If \(x\) is a top, (2.1)--(2.2) give

\[
                         \beta_P(x)=O(m^{-2}).           \tag{5.2}
\]

If \(x\) is an owner, there are at most 36 distance-one owner
neighbours in \(P\); all remaining owner neighbours have distance at
least two.  Thus the coarse explicit estimate

\[
 \beta_P(x)\le {36^2\over m^2}
       +(12d){12d\over\binom m2^2}+o(m^{-2})
 \le {1872+o(1)\over m^2}.                              \tag{5.3}
\]

Therefore

\[
 {1\over2}\sum_{x\in P}\beta_P(x)=O(m^{-1}).           \tag{5.4}
\]

There is a matching lower bound.  Each of the twelve retained linear
owner paths contains \(d-1\) unordered consecutive pairs.  Hence

\[
 B_1\ge24(d-1),
\]

and the distance-one part of the owner-pair energy alone is

\[
 {B_1\over2}\,{d^{OO}_1\over D_O}
 ={B_1^2\over24d\,m^2}
 \ge {24(d-1)^2\over d\,m^2}
 ={24+o(1)\over m}.                                    \tag{5.5}
\]

For comparison, an ordinary promotion frame has edge-local collision
mass \((2+o(1))/m\), while the domino twin has
\((50+o(1))/m\).  The present coarse constant is much worse, but the
order is the same.  Palette repair has not introduced a new
constant-order collision wall.

## 6. Static logarithmic factorial overlap

### Theorem 6.1

For each fixed \(C_0>0\) there is \(C=C(C_0)\) such that (0.2) holds
for every \(x\in P\) and \(1\le p\le C_0\log m\).

#### Proof

As usual, after removing the diagonal packet \(P\),

\[
 \sum_{\substack{P'\ni x\\P'\ne P}}(|P\cap P'|-1)_p
 =p!\sum_{\substack{A\subseteq P\setminus\{x\}\\|A|=p}}
       \bigl(d(\{x\}\cup A)-1\bigr)
 \le p!\sum_{\substack{A\subseteq P\setminus\{x\}\\|A|=p}}
       d(\{x\}\cup A).                                 \tag{6.1}
\]

First let \(x\) be a top.  A cluster containing only tops has at most
eleven further members, so (2.1) and a constant enumeration dispose of
it.  Every other cluster contains an owner, and the pair consisting of
the anchor \(x\) and that owner supplies the top--owner factor (2.2).
Even after multiplying by
\((12+12d)^p=\exp[O((\log m)^2)]\), this is
\(o(m^{-A})\) for every fixed \(A\), because
\(H\asymp\sqrt{m\log m}\).  This proves (0.2) for top anchors.

Now let \(x\) be an owner.  Clusters containing a top are disposed of
by the same top--owner estimate, so take all members of \(A\) to be
owners.  Let \(h\) be the Johnson diameter of
\(\{x\}\cup A\).  For \(h=1\), (3.2) and (4.1) give at most
\(36^p\) ordered choices and normalized cluster degree at most
\(36/m^2\).

For \(2\le h<H/2\), (3.2), a farthest pair, and (4.2) give total
contribution at most

\[
 [12(2h+1)]^p\,{12m\over\binom mh^2}.                  \tag{6.2}
\]

For \(h\ge H/2\), use the crude \((12d)^p\) count; the denominator
\(\binom mh^2\) is then
\(\exp[\Omega(H\log(m/H))]\), which dominates
\(\exp[O((\log m)^2)]\).

To sum (6.2), split at \(h=C_1p\).  Below the split the numerator is
absorbed by \((Cp)^{Cp}\) and the pair degree is at most
\(O(m^{-2})\).  Above the split,
\(\binom mh\ge(m/h)^h\) makes the terms geometrically decreasing after
enlarging \(C_1=C_1(C_0)\).  Multiplication by the outer \(p!\) in
(6.1) is again absorbed by \((Cp)^{Cp}\).  This proves (0.2).
\(\square\)

Thus the owner-aware twelve-top catalogue meets the same time-zero
finite ACLE/factorial-overlap scale already proved for domino twins.
As there, a stopped hereditary version would still be a separate
dynamic theorem.

## 7. The usual growing-rank slow-bite hypothesis is still critical

Let \(K=12+12d=(12+o(1))m\) and let \(V_{\rm aug}=N+W\) be the number
of augmented resources.  The unavoidable within-row pairs above give

\[
 {\Delta_2\over d_{\min}}\ge {2+o(1)\over m^2}.
\]

Since \(\log V_{\rm aug}=(2\log2+o(1))m\),

\[
 K\,{\Delta_2\over d_{\min}}\,\log V_{\rm aug}
 \ge48\log2-o(1).                                      \tag{7.1}
\]

Thus a growing-uniformity theorem requiring
\(K\Delta_2\log V_{\rm aug}=o(d_{\min})\) still cannot be invoked.
The logarithmic factorial estimate (0.2) is a genuine improvement over
maximum-codegree bookkeeping, but it is only time-zero.  To drive a
slow bite to a near-factor one would need its stopped/hereditary
analogue normalized by the current links.  The same dynamic issue is
open for the domino-twin catalogue.

## 8. Why this does not round

At the critical calibration, a matching containing
\((1-o(1))N/12\) macros uses

\[
 (1-o(1))N\quad\hbox{tops},\qquad
 (1-o(1))dN=(1-o(1))W\quad\hbox{owners}.                \tag{8.1}
\]

Because packet tops are disjoint, the selected macros choose one
literal retained word on almost every selected top.  Because packet
owner supports are disjoint, those words partition all but \(o(W)\)
middle owners.  In other words:

> an owner-aware near-perfect macro matching is already a near-perfect
> cyclic retained-window frame factorization, with the additional
> twelve-top source-word constraints.

The uniform fractional point is immediate from (0.1): weight
\(1/D_T\) saturates every top and gives every owner load \(\rho=1-o(1)\).
But growing edge size, the known determinant-two frame triangles, and
the equivalence (8.1) prevent promoting this fractional point to an
integral matching by pair-spread alone.

## 9. Exact boundary

Proved here:

1. exact two-orbit degrees and all orbit codegrees;
2. \(O(m^{-2})\) maximum relative pair codegree;
3. \(O(m^{-1})\) edge-local collision mass;
4. the logarithmic static factorial-overlap/ACLE profile; and
5. exact equivalence of a near-perfect augmented matching to a physical
   owner-resolution theorem.

Not proved:

1. one owner-aware augmented matching;
2. a stopped hereditary factorial-overlap theorem;
3. an absorber crossing the frame odd triangles; or
4. chronological compatibility between successive owner-aware layers.

The repaired twelve-top primitive has therefore passed every static
local-overlap test.  Its globalization is now identified with the same
integral owner-resolution gate already present before the primitive,
not with a missing degree computation.
