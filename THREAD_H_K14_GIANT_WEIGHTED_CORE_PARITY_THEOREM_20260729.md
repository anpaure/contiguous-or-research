# The frozen k14 giant AA component has exact defect minimum 13

Date: 2026-07-29  
Lane: H  
Status: theorem; solver-free weighted implication certificate and parity
exclusion of equality

This note proves the giant-component lemma left open in

```text
THREAD_H_FIXED_K14_AA_COLORED_CUT_AND_ESCAPE_20260729.md
```

Consequently the frozen-path AA minimum 17 now has a combinatorial proof;
the CP-SAT lower bound is no longer needed.

The frozen parent path is

```text
scratch/k14_common_colour_3opt_best_20260729.json
SHA-256 eeccbd6be6edeba88a5d953a1f543c8f77895bbbec0e6ab0fd4eadb9e05af546
```

## 1. The giant categorical CSP

For every repeated rank-six colour \(X\), let \(F_X\) be its set of edge
positions.  Write \(K_p=1\) when position \(p\) is the unique retained
representative of its fibre.  Thus

\[
 \sum_{p\in F_X}K_p=1.                                  \tag{1.1}
\]

The giant component contains

\[
 611\text{ positions},\qquad 289\text{ double fibres},
 \qquad 11\text{ triple fibres}.                        \tag{1.2}
\]

There are 155 mandatory distance-one clauses

\[
 K_p\lor K_{p+1}.                                       \tag{1.3}
\]

They are exactly the projected A-owner degree constraints.  There are 310
distance-two/three pairs

\[
 E_s=\{(p,q):q-p\in\{2,3\}\}                           \tag{1.4}
\]

inside the giant component.  Put

\[
 d_{pq}=(1-K_p)(1-K_q)\in\{0,1\}.                      \tag{1.5}
\]

Then

\[
 D_G=\sum_{(p,q)\in E_s}d_{pq}                          \tag{1.6}
\]

is exactly the number of short AA components contributed by the giant.

## 2. Implication-core inequalities

For \(C\subseteq E_s\), adjoin the clauses

\[
 K_p\lor K_q\qquad((p,q)\in C).                        \tag{2.1}
\]

### Lemma 2.1 (core inequality)

If (1.1), (1.3), and all clauses (2.1) are inconsistent, then every
admissible cut set satisfies

\[
 \sum_{e\in C}d_e\ge1.                                 \tag{2.2}
\]

#### Proof

If the sum were zero, every pair in \(C\) would have at least one retained
endpoint, so all clauses (2.1) would hold, contrary to the stated
inconsistency.  ∎

The inconsistency certificates below use only elementary domain deletion.
Regard fibre \(F_X\) as a categorical variable whose domain is its set of
possible survivor positions.  For a clause \(K_p\lor K_q\) joining fibres
\(F_X,F_Y\), states \(a\in F_X,b\in F_Y\) are compatible exactly when

\[
 a=p\quad\text{or}\quad b=q.                            \tag{2.3}
\]

Delete a state if it has no compatible state in the current neighboring
domain.  A same-fibre clause deletes every state outside \(\{p,q\}\).
Each deletion preserves every global solution; hence an empty domain is a
literal proof of inconsistency.  This is arc consistency, used here as a
proof rule rather than an optimization algorithm.

## 3. The fifteen cores

The following are the fifteen certificate cores.  Every displayed pair is a member of
\(E_s\).

\[
\begin{array}{c|c|l}
i&w_i&C_i\\ \hline
0&1&(547,549),(2241,2244),(2242,2244)\\
1&1&(548,550),(2207,2209),(2207,2210)\\
2&1&(1557,1559),(1616,1618),(2735,2737)\\
3&1&(1821,1824),(1822,1824),(3330,3332)\\
4&1&(1260,1262),(1465,1468),(1594,1596),(1594,1597)\\
5&1&(1890,1892),(2083,2085),(3347,3350),(3351,3353),(3351,3354)\\
6&1&(129,131),(422,424),(1047,1050),(1048,1050),
       (1179,1181),(1292,1295),(2608,2610)\\
7&1&(614,616),(853,856),(1204,1207),(1564,1566),
       (2015,2017),(2015,2018),(3272,3274)\\
8&\tfrac12&(500,502),(623,626),(911,913),(1429,1432),
       (2637,2640),(2638,2640),(3203,3206),(3308,3311)\\
9&1&(371,373),(816,818),(816,819),(2300,2302),(2372,2375),
       (2774,2776),(2975,2977),(3053,3056),(3054,3056),(3393,3395)\\
10&\tfrac12&(158,161),(443,445),(808,810),(1356,1359),(1697,1700),
       (1889,1891),(1889,1892),(2198,2200),(2314,2317),
       (2398,2400),(2398,2401),(2794,2797),(2847,2850),(3004,3007)\\
11&\tfrac12&(842,844),(1154,1156),(2314,2317),(2989,2992),(3002,3004)\\
12&\tfrac12&(136,138),(136,139),(1429,1432),(1881,1883),
       (1881,1884),(3203,3206)\\
13&\tfrac12&(136,138),(136,139),(500,502),(623,626),(911,913),
       (1881,1883),(2638,2640),(3308,3311)\\
14&\tfrac12&(158,161),(443,445),(808,810),(842,844),(1356,1359),
       (1697,1700),(1889,1891),(1889,1892),(2198,2200),
       (2794,2797),(2848,2850),(2989,2992).
\end{array}                                               \tag{3.1}
\]

### Proposition 3.1 (literal verification of the cores)

Every \(C_i\) in (3.1) satisfies the hypothesis of Lemma 2.1.

#### Proof

Starting from the exact fibre domains and using the hard clauses (1.3) and
the soft clauses indexed by \(C_i\), arc consistency empties the following
fibre after the displayed number of dependency-relevant deletions:

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
i&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14\\ \hline
\text{empty fibre}
 &2379&335&14504&5345&5032&7685&4631&5240&1740&8419
 &10002&13588&1740&13066&13588\\
\text{deletions}
 &2&3&7&2&4&5&6&9&12&11&18&10&9&7&17.
\end{array}                                               \tag{3.2}
\]

For example, in \(C_0\), fibre 2379 is \(\{547,2244\}\).  If 547 is its
survivor, the clauses at 2244 force both 2241 and 2242 to survive in fibre
1355, impossible.  If 2244 is its survivor, the hard/soft clauses at 547
force both 548 and 549 to survive in fibre 2251, again impossible.  Thus
both states of fibre 2379 are deleted.

All 122 elementary deletions, including the current neighboring domain and
the exact hard/soft clauses which remove each state, are recorded in

```text
scratch/k14_giant_weighted_core_trace_table_20260729.md
SHA-256 f64966529dab2e6795ca33cbdfd3afa59cabfb252f0770dd01ed835c81db5e44
```

Every line is an instance of the sound rule (2.3), so (3.2) proves all
fifteen inconsistencies without a SAT or integer solver.  ∎

## 4. The weighted lower bound 12

For an edge \(e\in E_s\), let

\[
 \lambda_e=\sum_{i:e\in C_i}w_i.                       \tag{4.1}
\]

A direct tally of (3.1) gives

\[
 \sum_iw_i=9+6/2=12,                                   \tag{4.2}
\]

and

\[
 0\le\lambda_e\le1.                                    \tag{4.3}
\]

More precisely, 67 edges have load one, nine have load one half, and all
other edges have load zero.  The half-loaded edges are

\[
\begin{split}
 &(1154,1156),(1881,1884),(2398,2400),(2398,2401),\\
 &(2637,2640),(2847,2850),(2848,2850),(3002,3004),
 (3004,3007).
\end{split}                                               \tag{4.4}
\]

Weighting the fifteen inequalities (2.2) gives

\[
\begin{aligned}
 D_G
 &=\sum_e d_e
 \ge \sum_e\lambda_ed_e\\
 &=\sum_iw_i\sum_{e\in C_i}d_e
 \ge\sum_iw_i=12.                                      \tag{4.5}
\end{aligned}
\]

This is an exact rational inequality, not an LP objective rounded from
floating point.

## 5. Equality 12 is parity-impossible

Assume for contradiction that \(D_G=12\).  Equality must then hold at every
step of (4.5).  Since

\[
 D_G-\sum_e\lambda_ed_e
 =\sum_e(1-\lambda_e)d_e,                               \tag{5.1}
\]

every defect with \(\lambda_e<1\) is zero.  Moreover,

\[
 \sum_iw_i\left(\sum_{e\in C_i}d_e-1\right)=0          \tag{5.2}
\]

is a positive weighted sum of nonnegative integers, so every core
inequality is tight.

After deleting its unique half-loaded edge, the load-one support of
\(C_8\) is

\[
\begin{split}
 A=\{&(500,502),(623,626),(911,913),(1429,1432),\\
     &(2638,2640),(3203,3206),(3308,3311)\}.
\end{split}                                               \tag{5.3}
\]

The corresponding support of \(C_{12}\) is

\[
 B=\{(136,138),(136,139),(1429,1432),(1881,1883),
       (3203,3206)\}.                                    \tag{5.4}
\]

The support of \(C_{13}\) is exactly

\[
 A\mathbin\triangle B
 =\{(136,138),(136,139),(500,502),(623,626),(911,913),
       (1881,1883),(2638,2640),(3308,3311)\}.             \tag{5.5}
\]

Tightness and (5.1) therefore give

\[
 \sum_{e\in A}d_e=\sum_{e\in B}d_e
 =\sum_{e\in A\triangle B}d_e=1.                       \tag{5.6}
\]

But modulo two,

\[
 \sum_{e\in A\triangle B}d_e
 \equiv \sum_{e\in A}d_e+\sum_{e\in B}d_e
 \equiv 1+1\equiv0,                                    \tag{5.7}
\]

contradicting the third equality in (5.6).

### Theorem 5.1 (exact giant minimum)

Every admissible giant-component survivor choice has

\[
 \boxed{D_G\ge13}.                                      \tag{5.8}
\]

The frozen AA witness has exactly thirteen giant defects, so

\[
 \boxed{\min D_G=13}.                                   \tag{5.9}
\]

#### Proof

Equation (4.5) gives \(D_G\ge12\); Section 5 excludes equality.  The
literal witness gives the reverse inequality.  ∎

## 6. Consequence for the complete frozen AA problem

The other 60 coloured-cut components have combined minimum four: the four
hand gadgets in the preceding note give the lower bound, and the same
witness attains it.  Components share neither fibre choices nor defect
edges.  Therefore

\[
 \boxed{\min D_{\mathrm{AA}}=4+13=17}.                  \tag{6.1}
\]

This proves the former trusted-solver optimum combinatorially.  Since every
full lower/degree or full-`q1` generalized braid projects to this AA CSP,
17 is also an unconditional lower bound in those narrower systems.  The
known lower/degree witness physically completes the value 17; the reported
full-`q1` incumbent remains 33.

## 7. Independent verifier

The compact certificate and solver-free verifier are

```text
scratch/k14_giant_weighted_core_certificate_20260729.json
SHA-256 021234800635a7137bd22f7913a10797b74fc1adff283358887b85182db2f15b

scratch/verify_k14_giant_weighted_core_certificate_20260729.py
SHA-256 e14ca408c75e25264de9b19d6729163106c8e2ae920a7167be1478e9f0f7609d
```

The verifier reconstructs the giant directly from the hash-bound parent
path, checks the entire rank-seven deck and Johnson chronology, verifies
all fifteen cores by domain deletion, checks the rational loads and parity
identity, and checks the thirteen-defect witness.  It uses no SAT, CP, LP,
or integer solver.  Its output is

```text
PASS rows=15 trace_steps=122 weight=12 loads=1:67,1/2:9 giant_witness=13
```

## 8. Adversarial audit

1. The ordinary fractional survivor/defect LP is not being used; it is far
   weaker.  The proof uses the integrality of the categorical fibre choice
   in each implication core and the final parity exclusion.
2. Arc consistency is used only in the sound direction: every deleted
   state lacks a compatible state in a neighboring current domain.  Empty
   domain is sufficient for inconsistency; no converse is assumed.
3. The weighted sum gives only 12.  The strict improvement to 13 genuinely
   requires the symmetric-difference parity identity; rounding an LP value
   is not being smuggled in.
4. This settles the frozen AA minimum and the fixed-path lower bound.  It
   does not construct a hard-resident changed chronology or close the
   full-`q1` incumbent gap \(17\) versus \(33\).
