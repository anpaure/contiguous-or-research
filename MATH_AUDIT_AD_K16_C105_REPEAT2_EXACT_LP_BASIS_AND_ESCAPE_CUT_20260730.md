# AD audit: exact C=105 weight-two LP basis, directed-cycle decomposition, and a basis-escape cut

Date: 2026-07-30

## 1. Scope and verdict

This note audits only the `s1_repeat2` face of the frozen K=16 direct
balanced-service seam relaxation.  In scale-two notation this face has

\[
 C=105,\qquad \sum_e s_e x_e=1,
 \qquad \sum_{t:b_t=2}m_t=61,
\]

while the 15 price-one targets and 18 price-four targets each have total
multiplicity exactly their cardinality.  Thus an integral point repeats
exactly one of the 60 price-two targets once.  Endpoint balance and target
service are enforced.  Port capacity may be imposed, but none of its rows is
active at the audited LP point.  Separation, reverse-edge, q1, residence,
survivor, and deeper-shadow rows are outside this note.

Verdict: **PASS, as an exact rational vertex audit.**  The exported 622
positive decimals reconstruct uniquely to an exact rational circulation.  It
has a deterministic decomposition into 87 independent directed simple cycles.
The audit also proves that every integral point of this branch must use a seam
outside the 622-seam support.  It does **not** prove the whole `s1_repeat2`
branch infeasible.

## 2. Frozen lineage

The inputs used here are:

* seam binary `scratch/k16_len8_source_seam_ledger_20260730.bin`, SHA-256
  `832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657`;
* exact direct-dual certificate
  `scratch/k16_direct_cycle_dual_exact_20260730.audit.json`, SHA-256
  `29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d`;
* GLOP export
  `scratch/k16_floor105_s1_repeat2_lp_support_20260730.audit.json`, SHA-256
  `a413c6e708322513c4c8349d3b0bd031f9d6b6b5cff1603c0980a168a886e37c`,
  self-payload
  `6218487ba8aafe834c5d4d6ecf5176ad25f13defc071234ffae61052bfb286ad`.

The export names generator SHA
`8b776eaa31f42ea2579096e73e200af854efe3d4b87dd2146ea5d159db6557bd`.
The present audit does not rely on a mutable copy of that generator: it
streams the frozen binary itself, reconstructs every supported seam's
endpoints, Boolean target-hit set and exact dual slack, and then builds the
integer basis matrix afresh.

The fail-closed verifier is
`scratch/audit_ad_k16_c105_repeat2_lp_basis_20260730.py`, SHA-256
`82719bd8b549a4e65696d8b9a7dd3ae15291d7da4345afd2671d8f48b848bee5`.
Its authoritative output is
`scratch/ad_k16_c105_repeat2_exact_lp_basis_v6_20260730.audit.json`, SHA-256
`41732a47ce0f80baf87add974df2e03d1bb89f261db595a61f72b2c9e0ad39da`,
with self-payload
`88939446f997f567e2be5577e7fd2870b5e4bb5852fa0daa5456dd65788f8b62`.

## 3. The exact support geometry

Let \(S\) be the 622 seam IDs having positive exported value.  The verifier
finds:

\[
 |S|=622,\qquad |V(S)|=544,\qquad c(S)=9,
\]

with weak-component vertex sizes

\[
2,2,2,2,4,4,5,5,518.
\]

Consequently the integral circulation lattice on this support has rank

\[
d=|S|-|V(S)|+c(S)=622-544+9=87.                 \tag{3.1}
\]

All 622 exported values lie strictly between zero and one.  The maximum
outgoing mass is only `0.7835035010140846`, so no port-capacity inequality is
tight.

Exactly 85 target-service rows are tight:

\[
15\text{ price-one}+52\text{ price-two}+18\text{ price-four}=85. \tag{3.2}
\]

The remaining eight price-two targets have diffuse excess.  They are

\[
R=\{36599,40430,42115,51067,51462,60902,61297,63416\}. \tag{3.3}
\]

Their exact excesses, in the same order, are

\[
\begin{split}
&301657723488329/(3b),\quad 29983067588807/(3b),\\
&710118178397239/b,\quad 383623088159038/(3b),\\
&41995929145978/b,\quad 70173646267380/b,\\
&165462486555017/b,\quad 271898820501517/(3b),
\end{split}                                                   \tag{3.4}
\]

where

\[
b=1{,}316{,}804{,}473{,}611{,}511.
\]

These eight excesses sum exactly to one.

## 4. Exact-basis theorem

### Theorem 4.1 (the 622-seam export is one exact rational vertex)

Choose any deterministic spanning forest of the undirected support graph and
use its 87 signed fundamental circulations as a \(\mathbb Z\)-basis of the
circulation lattice.  Form the 87 by 87 integer matrix whose rows are:

1. the 85 tight target-incidence rows from (3.2);
2. total price-two occurrence, with right-hand side 61;
3. total dual slack, with right-hand side 1.

For the verifier's seam-order spanning forest this matrix is nonsingular and
has determinant

\[
\det A=-126{,}413{,}229{,}466{,}705{,}056=-96b.       \tag{4.1}
\]

The unique solution reconstructs all 622 GLOP values with maximum absolute
error below

\[
7.03\cdot10^{-14}.
\]

It replays exactly: endpoint imbalance zero, selected mass 105, slack mass 1,
every target multiplicity at least one, and price-two total multiplicity 61.

The least common denominator of all 622 reduced flow values is

\[
D=7{,}900{,}826{,}841{,}669{,}066=6b,                \tag{4.2}
\]

and \(|\det A|=16D\).  The complete denominator histogram is

| reduced denominator | number of seams |
|---:|---:|
| \(b\) | 238 |
| \(2b\) | 2 |
| \(3b\) | 372 |
| \(6b\) | 10 |

In particular, the large denominator is structural; it is not decimal noise.

#### Proof

The signed fundamental-cycle construction gives a genuine integral basis:
each nonforest edge occurs with coefficient one in its own basis vector and
zero in every other nonforest coordinate.  The 544 vertex rows have rank
\(544-9=535\), leaving the 87 coordinates in (3.1).

The verifier computes the 87 rows above directly from the raw seam records.
Fraction-free Bareiss elimination gives (4.1), hence uniqueness.  Exact back
substitution gives the rational seam values.  Direct substitution checks all
balance, service, occurrence and slack identities.  Reducing each fraction
and taking their least common multiple gives (4.2) and the displayed
histogram.  No floating-point assertion is used in this replay, except to
identify which exported rows were claimed tight; exact substitution then
proves those identities.  QED.

The count row is redundant in this square system.  On every circulation the
direct-dual identity telescopes to

\[
2C=\sum_t b_t m_t+\sum_e s_ex_e.
\]

The 85 exact target rows, price-two total 61 and slack total 1 therefore force
\(C=105\).  Replacing the price-two aggregate row by the count row produces
the same exact solution and the same determinant in this basis.

## 5. Exact directed-cycle decomposition

### Theorem 5.1 (87 independent positive directed cycles)

The exact flow from Theorem 4.1 has a decomposition

\[
x^*=\sum_{i=1}^{87}\lambda_i\mathbf 1_{C_i},\qquad \lambda_i>0, \tag{5.1}
\]

where every \(C_i\) is a directed simple cycle and the 87 cycle vectors are
linearly independent.  Thus they form a real cycle-space basis.  Eight cycles
belong to the eight small rank-one components; the other 79 lie in the
518-vertex, 596-edge component.

The coefficient denominators are:

| reduced denominator | number of cycle coefficients |
|---:|---:|
| \(b\) | 34 |
| \(2b\) | 1 |
| \(3b\) | 49 |
| \(6b\) | 3 |

Cycle lengths range from 2 through 177.  The exact ordered decomposition has
semantic SHA-256
`45b56e88c5beeb71e2826191521a54d2833c620dac60c445da313f2babe7ffcb`;
the complete seam lists and coefficients are in the authoritative audit JSON.

#### Proof

Starting from the exact positive residual circulation, follow the least-ID
available outgoing edge until the first repeated vertex, subtract the minimum
residual on that directed simple cycle, and repeat.  Exact balance ensures the
walk never encounters a dead end.  The procedure terminates after 87 cycles
and replays every seam value exactly.

At each iteration choose one seam deleted by that subtraction as its pivot.
That pivot never occurs in a later cycle.  In iteration order, the matrix of
cycle vectors restricted to the 87 pivot seams is triangular with diagonal
one.  Hence the cycles are independent.  Their number equals the dimension
in (3.1), so they form a basis.  QED.

## 6. A compact exact separating cut

Let \(T\) be the 52 price-two targets whose rows are tight at \(x^*\), namely

```
33609 34450 36132 36343 36969 37389 39496 39791 39918 41170
42010 46224 46814 46835 47003 47068 47327 47343 48092 48347
48583 48867 49572 50939 51252 52663 53825 56185 56269 56431
56439 56941 57059 57201 58237 58301 59099 59680 60860 60983
60987 61238 61368 61886 61918 62317 63259 63261 63926 64397
64398 64966
```

The compact JSON serialization of this ordered list has SHA-256
`22757b569099f66fe9fe71b9aba694a7c896a6cc84732c2a0f7f5ca3afd3c414`.
The ordered support-ID list has SHA-256
`3fa1c8d6e8ca9396a39bb95ccb32400f11ede3f7eb76ab83f131ec9992aafbcd`.

For a branch point write \(m_t=\sum_{e:t\in H(e)}x_e\), and let
\(E_1^{\rm cyc}\) be the frozen 15,340 cycle-eligible seams of slack zero or
one.  Then every integral balanced-service point in `s1_repeat2` obeys

\[
\boxed{
\sum_{e\in E_1^{\rm cyc}\setminus S}x_e
+\sum_{t\in T}(m_t-1)\ge 1.}                         \tag{6.1}
\]

### Proof

All summands are nonnegative integers.  Suppose the left side were zero.
Then the integral point would use only seams in \(S\), and none of the 52
targets in \(T\) would be repeated.  Price-one and price-four targets cannot
repeat in this branch.  Hence all 85 target rows used in Theorem 4.1 would be
equalities.  The branch itself supplies price-two total 61 and slack total 1.
The point would therefore solve the same nonsingular 87 by 87 system as
\(x^*\), so it would equal \(x^*\).  This is impossible because every
coordinate of \(x^*\) is strictly fractional.  QED.

No port-capacity, separation, q1, residence, survivor or deeper row is used in
this proof.  Operationally, (6.1) says that an integer solution which repeats
one of the eight diffuse targets in (3.3) must import at least one seam outside
the 622-seam support.

### Theorem 6.2 (pure 622-support escape)

Every integral `s1_repeat2` point satisfies the stronger inequality

\[
\boxed{\sum_{e\in E_1^{\rm cyc}\setminus S}x_e\ge 1.}          \tag{6.2}
\]

#### Proof

An integral point in this branch has exactly one repeated price-two target,
so there are 60 possible exact service right-hand sides.  For each label
\(r\), reuse the nonsingular 87 by 87 matrix of Theorem 4.1, changing the
right-hand side of its target row from one to two when \(r\in T\).  This fixes
the unique real circulation on \(S\) that could satisfy the 85 basis target
rows, price-two aggregate 61, and slack one.

One simultaneous fraction-free elimination with 60 right-hand sides replays
the eight omitted target rows exactly.  None of the 60 candidates has the
required full 93-target service vector.  The single omitted row for target
36599 already disagrees in all 60 cases.  Its ordered exact residual vector
has SHA-256
`ba670cdc79881a710971053aebfe0ddce172bddaf882f631c9bf0a23c115b1e9`;
the complete fixed-label rows have SHA-256
`eac725d055b709019f843ba3fefdf432899e151c46ab1eddbd29f78aa35bdea5`.

Thus no real circulation supported on \(S\) realizes any integral branch
multiplicity pattern.  A fortiori an integral branch point must use at least
one seam outside \(S\), proving (6.2).  QED.

This is an exact row-span calculation, not an optimization run.  It used no
CP-SAT, CNF, or timed search.  No port-capacity or omitted physical row enters
the argument.

## 7. Sharp proximity obstruction

### Theorem 7.1 (nearest count-105 binary vector)

For every binary vector \(y\) on the whole branch arc bank with
\(\sum_e y_e=105\),

\[
\|y-x^*\|_1\ge
\frac{406{,}993{,}663{,}932{,}636{,}184}
     {3{,}950{,}413{,}420{,}834{,}533}
=103.025587597\ldots .                              \tag{7.1}
\]

This bound is sharp in the cardinality-only binary cube: equality is attained
by selecting the 105 largest coordinates of \(x^*\).  That nearest binary
vector is not asserted to satisfy balance or service.

#### Proof

Since \(\sum_e x_e^*=\sum_e y_e=105\),

\[
\|y-x^*\|_1=210-2\sum_{e:y_e=1}x_e^*.
\]

The final sum is maximized by the 105 largest exact coordinates.  Their sum is

\[
\frac{211{,}296{,}577{,}221{,}307{,}873}
     {3{,}950{,}413{,}420{,}834{,}533},
\]

which gives (7.1).  QED.

Thus a proximity or Graver search centered at this LP vertex cannot possibly
find a count-105 integer endpoint inside \(L^1\) radius 103.  This is a sharp
negative proximity result, not a general upper-bound theorem.  The determinant
is so large that generic determinant-based Graver bounds would not be useful;
the pure support cut (6.2) is the actionable reduction.

## 8. Precise remaining boundary

Proved here:

1. the 622-decimal export is an exact, unique rational vertex on its active
   support face;
2. its exact denominator, determinant, component structure and a complete
   independent directed-cycle decomposition;
3. the pure support-escape cut (6.2), valid already in the no-capacity
   balanced-service branch and stronger than (6.1);
4. the sharp cardinality-cube distance (7.1).

Not proved here:

1. infeasibility of the full `s1_repeat2` branch;
2. existence of an integer point after crossing (6.2);
3. any claim for seams outside the frozen 211,604-seam catalogue;
4. any q1, residence, separation, reverse-edge, survivor, or literal compiler
   conclusion.
