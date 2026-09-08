# Audit of the central two-bank reduction and Dong--Mao range

**Date:** 2026-08-02  
**Audited notes:**

* `MATH_THEOREM_CENTRAL_TWO_INTERVAL_BANK_REDUCTION_AND_ENGEL_RANGE_GATE_20260802.md`;
* `MATH_THEOREM_DONG_MAO_FIXED_CORE_DIAMOND_BANK_AND_TWO_BANK_FUSION_GATE_20260802.md`.

**Verdict:** PASS after the terminology, converse, and capacity repairs
listed below. Dong--Mao does not cover the central three-level instance.
The fixed-core lift gives an unconditional large partial diamond bank, but
the complementary two-bank/common-base statement remains **unproved**.

## 1. Two-bank reduction

A central interval

\[
 [L,U]=\{L,T,H,U\}
\]

is determined by its Johnson edge \(TH\): necessarily
\(L=T\cap H\) and \(U=T\cup H\). Inside one interval bank, literal
vertex-disjointness therefore makes the Johnson edges a matching. The union
of two banks is a simple graph of maximum degree two; its nontrivial
components are paths or even cycles, with bank colours alternating.

If the two lower palettes partition the full lower level and the two upper
palettes partition the full upper level, then orienting each path
consistently and each cycle cyclically gives:

* every lower and upper colour exactly once; and
* every middle vertex at most once as a tail and at most once as a head.

This proves the four partition/resource rows. It does **not** prove the
graphic row when a cycle remains. The audited theorem was corrected to use
the established terminology: only an acyclic union is an ordered
four-transversal/Catalan linear forest.

Deleting one edge from each of \(c\) cycles loses exactly \(c\) lower and
\(c\) upper colours and leaves a linear forest. Conversely, alternately
two-colouring every path in any Catalan linear forest produces two interval
banks with complementary outer palettes. Hence the zero-cycle
complementary bi-packing statement is equivalent to the central
ordered-four-transversal gate. The original one-way wording was too weak.

The cross-overlap formulation in the companion note is equivalent. Its
vertices are selected diamonds and its edges are shared middle vertices.
It is exactly the line graph of the physical maximum-degree-two Johnson
lift. Complementary outer palettes rule out parallel copies of one physical
edge. Thus the overlap graph is a forest exactly when the physical lift is
a linear forest.

## 2. Exact capacity arithmetic

Put

\[
 N={2m\choose m-1},\qquad W={2m\choose m}.
\]

Direct cancellation gives

\[
                         N={m\over m+1}W
                          =W-{W\over m+1}.            \tag{2.1}
\]

If the bank sizes are \(b_0,b_1\), palette complementarity gives
\(b_0+b_1=N\). Each interval uses two distinct middle vertices, so
\(b_e\le W/2\). Applying this bound to the other bank gives the exact
two-sided window

\[
             {W\over2}-{W\over m+1}
             \le b_e\le {W\over2}.                   \tag{2.2}
\]

Equivalently, with \(\Delta_e=W-2b_e\),

\[
       \Delta_0,\Delta_1\ge0,\qquad
       \Delta_0+\Delta_1={2W\over m+1}
       =2\operatorname {Cat}_m.                      \tag{2.3}
\]

Thus two complementary banks are correlated almost-perfect middle
matchings. Total size \(N\) itself is larger than one bank's \(W/2\)
ceiling for \(m>1\); it is the individual sizes in (2.2), not \(N\), that
lie below that ceiling.

## 3. Primary-source scope

Dong--Mao Theorem 1.2 proves

\[
 n\ge(\ell+1)r+\ell
 \quad\Longrightarrow\quad
 \nu_{n;\ell,\ell+r}={n\choose\ell}.                 \tag{3.1}
\]

At equality their Section 2 gives the cycle-lemma construction;
Proposition 2.5 proves that the resulting intervals are pairwise disjoint.
Section 3 extends the theorem to larger \(n\) by coordinate recursion.

For central diamonds,

\[
                    (n,\ell,r)=(2m,m-1,2).
\]

Condition (3.1) becomes \(2m\ge3m-1\), false for every \(m\ge2\).
Complementation does not help because the central three-level poset is
self-complementary.

Problem 4.2 explicitly leaves

\[
                 {3\ell+4\over2}<n<3\ell+2
\]

open and asks whether the elementary minimum of the two endpoint counts
and half the middle count is always attained. Substituting
\((n,\ell)=(2m,m-1)\) puts every \(m\ge2\) strictly inside that open range
and specializes the conjectured value to

\[
                  \left\lfloor{1\over2}{2m\choose m}\right\rfloor.
\]

These statements were checked against [Dong--Mao, Theorem 1.2 and
Problem 4.2](https://arxiv.org/abs/2607.04794). No central full-bank claim
is imported.

## 4. Unconditional fixed-core bank

Let

\[
 q=\lfloor m/2\rfloor,\qquad
 \ell'=m-1-q,\qquad n'=2m-q.
\]

Then \(n'\ge3\ell'+2\): for \(m=2s+1\) equality gives
\((q,\ell',n')=(s,s,3s+2)\), while for \(m=2s\) one gets
\((s,s-1,3s)\). Fixing a \(q\)-set \(R\), applying Dong--Mao on the
remaining \(n'\) coordinates, and adjoining \(R\) to every interval gives

\[
 b_m={2m-\lfloor m/2\rfloor\choose
             m-1-\lfloor m/2\rfloor}
 =\begin{cases}
   {3s\choose s-1},&m=2s,\\
   {3s+2\choose s},&m=2s+1
  \end{cases}                                        \tag{4.1}
\]

pairwise vertex-disjoint *central* diamonds. Their lower endpoints are
exactly the rank-\((m-1)\) sets containing \(R\). Deleting the fixed core
from a hypothetical collision proves literal disjointness.

Stirling gives

\[
 b_m=\Theta\!\left({(3\sqrt3/2)^m\over\sqrt m}\right),
\qquad
 {b_m\over {2m\choose m-1}}
 =\Theta\!\left((3\sqrt3/8)^m\right).                \tag{4.2}
\]

The exact comparison \(2b_m<N\) also replays. For \(m=2s\),

\[
 { {3s\choose2s-1}\over {3s\choose s-1}}
 ={2(2s+1)\over s+1}>2,
\]

and enlarging the ground set from \(3s\) to \(4s\) only increases the
relevant binomial coefficient. For \(m=2s+1\), the corresponding ratio is
\(2(2s+1)/(s+2)\), equal to two at \(s=1\) and larger thereafter; the
strict ground-set enlargement gives \(N>2b_m\) in every case. Hence two
fixed-core banks of this size cannot cover the central outer palette.

## 5. Five-coordinate fibre bank

The stronger stratified construction also replays. Split
\([2m]=H\dot\cup K\) with \(|K|=5\). For each fixed \(H\)-pattern, the
required outside lower rank is \(j=0,1,2,3\). The exact one-fibre packing
capacities are

\[
 \min\left\{{5\choose j},
       \left\lfloor{1\over2}{5\choose j+1}\right\rfloor,
       {5\choose j+2}\right\}=(1,5,5,1).             \tag{5.1}
\]

The \(j=1\) value is attained by the critical Dong--Mao
\((5,1,2)\) construction. Directly on \(\mathbb Z_5\), use

\[
 [\,\{i\},\{i,i+1,i+2\}\,]\qquad(i\in\mathbb Z_5).
\]

Its ten middle pairs \(\{i,i+1\},\{i,i+2\}\) are all ten two-subsets of
\(\mathbb Z_5\); the lower and upper endpoints are also distinct.
Complementation supplies \(j=2\), and the trivial packing supplies
\(j=0,3\). Distinct \(H\)-patterns are disjoint Boolean fibres, so their
union is one literal central bank of size

\[
 D_m=2{2m-5\choose m-1}+10{2m-5\choose m-2}.         \tag{5.2}
\]

Binomial cancellation gives the exact capacity density

\[
 {D_m\over\frac12{2m\choose m}}
 ={m(3m-4)\over(2m-1)(2m-3)}
 \longrightarrow {3\over4},                         \tag{5.3}
\]

and residual fraction

\[
 { (m-1)(m-3)\over(2m-1)(2m-3)}.
\]

Because (5.1) is the elementary endpoint/middle capacity bound in every
fibre, this bank is maximum among banks preserving every \(H\)-pattern.
It reaches full central capacity at \(m=3\). The exact comparison

\[
                         2D_m<{2m\choose m-1}
\]

holds precisely for \(m\ge6\), since it reduces to
\(m^2-7m+7>0\). Thus the five-fibre bank is a genuine asymptotic
three-quarter partial absorber, but two copies are cardinality-insufficient
for the all-\(m\) complementary-bank target.

The independent replay

    scratch/audit_dong_mao_five_fibre_bank_20260802.py

literalizes the \(\mathbb Z_5\) bank and checks (5.2)--(5.3) through
\(m=200\).

## 6. Fixed ground-cut parity obstruction

The fixed-bipartition overload proposition is correct with its stated
scope. Let \([2m]=A\dot\cup B\), and require every diamond increment to
contain one point from each side. If \(|A|\le m-1\), an
\((m-1)\)-set containing all of \(A\) has no available \(A\)-increment;
the symmetric argument gives \(|B|\ge m\). Full lower-palette coverage
therefore forces \(|A|=|B|=m\).

For every \(a\in A\), the lower colour \(A-\{a\}\) must then use an
increment \(\{a,b_a\}\) with \(b_a\in B\). Its Johnson edge has the common
middle endpoint \(A\). The other endpoints
\(A-\{a\}+\{b_a\}\) are distinct as \(a\) varies, so \(A\) has physical
degree at least \(m\). Tail/head capacity allows degree at most two.
Therefore no such fixed ground-cut construction exists for \(m\ge3\).

This excludes only coordinate-fixed parity. It does not exclude a
bipartition chosen after the physical linear forest, a state-dependent
parity, or any selected-graph two-colouring. Those are the viable
common-base formulations.

## 7. Common-base consequence and fail-closed scope

On ordered diamonds, the lower, upper, tail, and head rows are four
partition matroids and the physical Johnson edges give the graphic
matroid. A complementary bank pair automatically meets the four partition
rows. Its union is a common independent set of the required size exactly
when the graphic/acyclic row also holds. This is the proof-safe insertion
into the common-base route.

Dong--Mao supplies neither:

* a bank in the central parameter range;
* complementary lower and upper palettes for two banks;
* cross-bank middle collision control; nor
* acyclicity of the aggregate physical lift.

The following remain **UNPROVED**: the central maximum-bank equation,
the complementary two-bank lemma, aggregation of many fixed-core banks,
all protected-host/common-cap correlations, and every literal
serialization or regenerative consequence.
