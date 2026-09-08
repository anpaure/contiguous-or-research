# Guarded-convex and laminar-matroid common-cap compilers

Date: 2026-07-31  
Status: unconditional sufficient theorems and sharp counterexamples  
Scope: the exact staircase/common-cap interface; no automatic all-dimensional
carrier construction is asserted

## 0. Outcome

Chain alignment, a legal maximal envelope, enough physical lower cells,
ordinary Hall, interval cells, convex target neighbourhoods, and even a
permanent owner bit at every position do **not** imply a simultaneous
integral common-cap assignment.  The natural matching-plus-cap LP is already
fractional on the smallest two-position example.

There is nevertheless a rigorous structural zero-defect route.

1. Choose a subbank of individually sound target--cell incidences carrying
   explicit position, protected-row, and selected-lower trace guards.
   These guards make **every** matching in the subbank common-cap exact.
2. If target neighbourhoods are intervals in one cell order, matching exists
   exactly under interval-capacity inequalities and is produced by an
   earliest-deadline greedy algorithm.
3. More generally, if a laminar cell-capacity family dominates every exact
   common-cap bad event, Rado's inequalities give an integral assignment via
   a laminar-tree flow.  Its signed node--arc incidence matrix is totally
   unimodular.

Combined with an owner-exact upper carrier and a chain-aligned schedule of
length \(B(k)\), either route gives a literal universal word and therefore

\[
                         \nu(k)=B(k)
\]

whenever the independent deadline lower bound supplies the reverse
inequality.

## 1. Exact residual compiler state

Let \(P\) be a finite line of physical positions.  Fixed pins have already
been intersected into nonempty envelopes

\[
                   \overline E_p\subseteq[k]\qquad(p\in P).
\tag{1.1}
\]

Let \(\mathcal P\) be the protected exact rows.  A row is a pair
\((R,D)\), with label \(R\subseteq[k]\) and physical interval
\(D\subseteq P\), and the fixed state passes

\[
 \overline E_p\subseteq R\quad(p\in D),\qquad
 \bigcup_{p\in D}\overline E_p=R.                    \tag{1.2}
\]

All scheduled middle rows and all fixed lower pins belong to
\(\mathcal P\).

Let \(\mathcal L\) be the residual lower targets and \(\mathcal C\) the
available physical cells.  An incidence \(e=(S,C)\) is retained only when
installing this one cap is individually exact.  Let \(H\) be any proved-sound
subgraph of this complete incidence graph.

For an injective target-saturating matching \(M\subseteq H\), define its
maximal common cap

\[
 A_p(M)=\overline E_p\cap
        \bigcap_{(S,C)\in M:\ p\in C}S.              \tag{1.3}
\]

The fixed-assignment maximal-cap theorem says that \(M\) is physical exactly
when \(A(M)\) is nonempty, realizes every protected row, and realizes every
selected lower cell.  Thus the only issue below is to make those equations
survive the integral selection.

Two edges \(e=(S,C)\) and \(f=(T,D)\) are **co-selectable** when
\(S\ne T\) and \(C\ne D\).  Every pair of distinct edges of a matching is
co-selectable.

## 2. Trace-guarded banks

### Definition 2.1 (complete co-selectable trace guards)

The bank \(H\) is trace guarded when the following data exist.

1. For every position \(p\), a point guard
   \(o_p\in\overline E_p\) such that every edge \((S,C)\in H\) with
   \(p\in C\) has \(o_p\in S\).
2. For every protected row \((R,D)\in\mathcal P\) and every bit
   \(b\in R\), a row guard
   
   \[
      g(R,D,b)\in D,\qquad b\in\overline E_{g(R,D,b)},              \tag{2.1}
   \]
   
   such that every edge of \(H\) whose cell covers this position has a
   label containing (b).
3. For every edge \(e=(S,C)\in H\) and every \(b\in S\), an edge guard
   
   \[
      g(e,b)\in C,\qquad b\in\overline E_{g(e,b)},                  \tag{2.2}
   \]
   
   such that every edge \(f=(T,D)\in H\) co-selectable with \(e\) and
   satisfying \(g(e,b)\in D\) has \(b\in T\).

The edge guard ignores incidences sharing the target or the cell with \(e\),
because no such incidence can coexist with \(e\) in a matching.  This is
strictly weaker than intersecting all labels of the whole bank at once.

### Lemma 2.2 (every matching in a guarded bank is zero defect)

Every target-saturating matching \(M\subseteq H\) satisfies all maximal
common-cap equations.

#### Proof

At position \(p\), every selected cap covering \(p\) contains \(o_p\).
Hence \(o_p\in A_p(M)\), proving nonemptiness.

Fix a protected row \((R,D)\) and \(b\in R\).  Every selected cap covering
the row guard \(g(R,D,b)\) contains \(b\), so \(b\) survives there.  Thus the
OR of \(A(M)\) on \(D\) contains \(R\); envelope containment (1.2) gives the
reverse inclusion.

Finally fix a selected edge \(e=(S,C)\) and \(b\in S\).  The cap from \(e\)
itself contains \(b\), and every other selected edge is co-selectable with
\(e\); condition (2.2) makes each one covering \(g(e,b)\) contain \(b\).
Thus \(b\) survives in \(C\).  Since \(e\) caps every position of \(C\) by
\(S\), no bit outside \(S\) occurs there.  Therefore the selected cell has
OR exactly \(S\).  These are all common-cap equations.  \(\square\)

The guard data contain no integral matching and no physical word.  They are
a genuine preselection certificate.

## 3. Guarded-convex greedy compiler theorem

Order the available cells as

\[
                  C_1<C_2<\cdots<C_m.                 \tag{3.1}
\]

Assume every target neighbourhood in \(H\) is a nonempty interval in this
order:

\[
 N_H(S)=\{C_j:\ell_S\le j\le r_S\}.                  \tag{3.2}
\]

### Theorem 3.1 (guarded-convex zero-defect compiler)

If \(H\) is trace guarded, an \(H\)-supported simultaneous integral
common-cap assignment exists if and only if

\[
 \boxed{
 \left|\{S\in\mathcal L:
          [\ell_S,r_S]\subseteq[a,b]\}\right|
       \le b-a+1
 \quad(1\le a\le b\le m).}
                                                               \tag{3.3}
\]

When (3.3) holds, sorting targets by nondecreasing \(r_S\) and assigning each
target to the smallest currently unused cell index in
\([\ell_S,r_S]\) produces a zero-defect compiler.

#### Proof

Condition (3.3) is necessary by applying Hall to the targets whose complete
neighbourhood lies in ([a,b]).

For sufficiency, take any target set \(X\subseteq\mathcal L\).  The union
\(N_H(X)\) is a disjoint union of cell intervals \(J_1,\ldots,J_t\).  Since
each target neighbourhood is connected, every \(S\in X\) has its complete
neighbourhood inside one \(J_j\).  Partition \(X\) accordingly.  Condition
(3.3) gives

\[
                    |X_j|\le|J_j|
\]

for every part, so \(|X|\le|N_H(X)|\).  Hall gives a matching.

The stated greedy algorithm is canonical.  Compare its next choice for the
minimum-deadline target \(S\) with any matching of the remaining instance.
If the greedy cell is free, use it.  Otherwise it is assigned to a target
\(T\), while \(S\) is assigned to a weakly later cell.  Moving \(S\) to the
greedy cell and \(T\) to the old cell of \(S\) is legal because

\[
 \ell_T\le\text{greedy cell}\le\text{old cell of }S
 \le r_S\le r_T.
\]

This exchange proves the greedy choice extendible; induction completes the
matching.  Lemma 2.2 turns it into an exact common-cap compiler.  \(\square\)

### TU interpretation

For any bipartite target--cell graph, the selector matrix with target
equalities and cell-capacity inequalities is totally unimodular: after
negating the cell rows, every selector column is a directed node--arc
incidence column.  Convexity is not needed for this marginal integrality; it
reduces all Hall cuts to (3.3) and supplies the greedy algorithm.

The important order is therefore

\[
 \boxed{\text{trace guards first, matching TU second}.}             \tag{3.4}
\]

Without the guards, the exact common-cap trace rows destroy the marginal
TU conclusion; Section 5 gives the smallest fractional obstruction.

## 4. Laminar-capacity and polymatroid extension

Relative to the retained bank \(H\), let \(\mathcal B_H\) be the complete
clutter of inclusion-minimal matching-compatible causes after fixed pins and
unary closure.  Thus every \(B\in\mathcal B_H\) is a partial matching of
\(H\)-edges that causes an empty position, a lost protected-row bit, or a
lost selected-lower bit, and every failing \(H\)-supported matching contains
such a \(B\).  Same-cell collisions are handled separately by unit cell
capacity.

Let \(\mathcal A\) be a laminar family of subsets of the cell ground set,
with integral capacities \(b_A\).  Include singleton cell sets with capacity
one.  Normalize the capacities so that
\(0\le b_A\le|A|\) and \(A\subseteq D\) implies \(b_A\le b_D\), replacing
each capacity by the minimum over its ancestors when necessary.  Suppose
every matching-compatible bad event is dominated by a laminar
capacity:

\[
 \boxed{
 \forall B\in\mathcal B_H\ \exists A\in\mathcal A:\quad
 |\operatorname{cells}(B)\cap A|>b_A.}                \tag{4.1}
\]

The cell sets obeying

\[
       |U\cap A|\le b_A\qquad(A\in\mathcal A)          \tag{4.2}
\]

form a laminar matroid \(\mathsf M\).

### Theorem 4.1 (laminar-Rado zero-defect compiler)

Under (4.1), a simultaneous integral common-cap assignment exists whenever

\[
 \boxed{
        r_{\mathsf M}(N_H(X))\ge|X|
        \qquad(X\subseteq\mathcal L).}                 \tag{4.3}
\]

#### Proof

Rado's theorem applied to the target neighbourhoods and the matroid
\(\mathsf M\) gives distinct incident cells whose set is independent in
\(\mathsf M\).  Such a selection cannot contain a bad event: by (4.1), the
cell set of that event already violates one of (4.2).  The exact conflict-
clutter equivalence therefore gives a common-cap compiler.  \(\square\)

This theorem is constructive.  Add a super-root above the laminar forest;
cells not contained in a nonsingleton laminar set remain singleton root
leaves.  Give the arcs from the source to targets and from targets to their
incident cells unit capacity.  Direct each cell leaf toward the super-root,
put capacity \(b_A\) on the arc from each laminar node \(A\) to its parent
(including a root-to-super-root arc), and give the super-root-to-sink arc
capacity \(|\mathcal L|\).  The network

\[
 s\longrightarrow\text{targets}\longrightarrow\text{cells}
 \longrightarrow\text{laminar tree}\longrightarrow t                \tag{4.4}
\]

has an integral maximum flow because its signed node--arc incidence matrix
is totally unimodular.  It has value \(|\mathcal L|\) exactly under (4.3).
The laminar rank used in
(4.3) is computed bottom-up:

\[
 r_A(Y)=\min\!\left(
 b_A,
 |Y\cap(A\setminus\!\bigcup\operatorname{ch}(A))|
 +\sum_{D\in\operatorname{ch}(A)}r_D(Y\cap D)
 \right).                                             \tag{4.5}
\]

The theorem contains every partition-capacity certificate satisfying (4.1)
as a special case.  It is sufficient rather than automatic: genuine
interval-cell safety need not form a matroid.

## 5. Sharp failure of automatic TU and laminarity

In the natural linear relaxation, \(x_e\in[0,1]\) are incidence selectors and
\(q_{p,b}\in[0,1]\) are surviving maximal-cap bits.  For

\[
 B_{p,b}=\{(S,C):p\in C,\ b\notin S\},
\]

the exact Boolean equivalence is relaxed as

\[
 q_{p,b}+x_e\le1\quad(e\in B_{p,b}),\qquad
 q_{p,b}+\sum_{e\in B_{p,b}}x_e\ge1.                  \tag{5.0}
\]

Add the target equalities, cell capacities, nonempty-position rows,
protected-row bit coverage, and

\[
 x_{S,C}\le\sum_{p\in C:\ b\in\overline E_p}q_{p,b}
 \qquad(b\in S).                                      \tag{5.0a}
\]

This is the standard direct common-cap LP; integrality is the issue below.

Use positions \(0,1\), one chain-aligned middle row with

\[
 E_0=E_1=T=\{o,a,x\},                                 \tag{5.1}
\]

the two singleton cells, lower targets

\[
 S_0=\{o\},\qquad S_1=\{o,x\},                       \tag{5.2}
\]

and all four individually sound incidences.  The marginal graph is the
convex graph \(K_{2,2}\), has a permanent owner \(o\), satisfies every
interval-Hall inequality, and has two perfect matchings.  Every perfect
matching caps both positions by labels omitting (a), so the middle row
loses (a).

The natural exact-model LP relaxation has the fractional point

\[
 x_{S_i,C_j}=\tfrac12,qquad
 q_{p,o}=1,qquad q_{p,a}=q_{p,x}=\tfrac12.            \tag{5.3}
\]

It satisfies target equalities, cell capacities, every blocker inequality,
middle-bit coverage, and selected-lower-bit coverage.  No integral compiler
exists.  Hence the augmented matching-plus-common-cap matrix is not TU.

Cell laminarity alone also fails: the two singleton cells above are disjoint.
For genuine intervals, safe selected families need not even satisfy matroid
exchange.  On positions \(\{1,2,3\}\), let all candidate labels oppose one
protected bit and take

\[
 A=[2,3],\qquad B=[1,1],\qquad C=[1,2].                \tag{5.4}
\]

Both \(\{A\}\) and \(\{B,C\}\) are safe, but neither \(B\) nor \(C\) can
augment \(\{A\}\).  Thus neither consecutive-ones geometry nor physical
intervals manufacture the laminar matroid required in Section 4.

There is a sharper carrier-level obstruction.  Take the rank-three Johnson
neighbours

\[
 T_0=\{o,a,u\},\qquad T_1=\{o,a,v\},                 \tag{5.5}
\]

on the chain-aligned schedule

\[
 I_0=[0,1],\qquad I_1=[1,2].                          \tag{5.6}
\]

The legal maximal envelope is

\[
 (\{o,a,u\},\{o,a\},\{o,a,v\}).                    \tag{5.7}
\]

The complete lower atlas has three singleton cells.  For residual targets
\(\{o,u\}\) and \(\{o\}\), exact individual replay forces the unique
matching

\[
       \{o,u\}\mapsto[0,0],\qquad \{o\}\mapsto[1,1].               \tag{5.8}
\]

It has scalar surplus one, but its maximal cap loses \(a\) from the first
middle row.  Thus even distinct Johnson rows, legal maximal envelopes,
chain alignment, disjoint cells, permanent owners, scalar surplus, and a
unique marginal matching do not imply a common cap.

The frozen audit also embeds the absolute core into a complete \(k=r=3\)
instance containing all six nonempty proper lower targets.  Four legal
singleton pins leave the residual \(K_{2,2}\); the complete atlas has 16
cells for six targets, and no exact common cap exists.  This removes any
possible objection that the small core omitted other lower targets.

## 6. Deadline particles and the K16 calibration

For an arbitrary-start schedule, an interior coordinate run \([u,v]\) has
safe physical corridor

\[
              J_x=[q_{u-1}+1,s_{v+1}-1].              \tag{6.1}
\]

The particle-threshold theorem proves that every owner row meets this
corridor.  These corridor points are candidates for the protected-row guards
of Definition 2.1.  The threshold theorem does **not** say that a large
target--cell bank preserves any chosen corridor point.  That is precisely
the extra trace-guard hypothesis.

Likewise the scalar loss inequality is only the full-ground-set capacity
test.  It implies neither the proper interval cuts (3.3) nor the Rado cuts
(4.3).

For the authenticated K16 construction:

\[
 \rho=(0,0,6384),\qquad \tau=(0,0,6386),               \tag{6.2}
\]

and the successful compiler schedule is

\[
 X=\{12870,12871,12872\},\qquad Y=\{0,1,6388\}.       \tag{6.3}
\]

It has 32,230 physical lower cells for 26,332 lower targets and deliberately
spends two loss units beyond the row-exact minimum to expose the singleton
cap at position 6,389.  This is the construction schedule; the distinct
first-middle staircase read from the final word has
\(Y=\{0,2,6389\}\) and must not be substituted into the compiler
certificate.

K16 was closed by an exact maximal-cap SAT witness, not by a pre-proved
convex or laminar bank.  Dulmage--Mendelsohn support pruning exposes 14,059
cap-neutral degree-one targets and leaves 12,272 target parts with 238,472
selectors.  A separate iterative universal-assignment closure reports
14,060 forced assignments and leaves 12,271 targets with 237,467 edges;
these two normalizations must not be conflated.  The final selected matching
supplies trace guards ex post, so it calibrates the theorem, but taking
\(H=M\) is not a noncircular all-dimensional proof.

The scalable construction target is therefore exact:

> Use arbitrary-start safe corridors to reserve trace guards; retain a
> guard-safe bank whose target neighbourhoods are convex, or whose exact
> conflicts are dominated by a laminar cell-capacity matroid; then prove
> (3.3) or (4.3).

## 7. Equality corollary

Assume a rank-\(r\) chronology owns every middle target once and is complete
for arbitrary-width upper targets.  Let a length-\(B(k)\) schedule be legal,
chain aligned, and have the complete lower-cell atlas.  After all fixed pins,
suppose either Theorem 3.1 or Theorem 4.1 supplies every residual lower
target.

The maximal common cap realizes every lower and middle target.  Chain
alignment makes the union of every consecutive block of middle intervals a
physical interval, so every upper carrier witness transfers literally.  The
result is a universal word of length \(B(k)\).  With the monotone-deadline
lower bound,

\[
                          \boxed{\nu(k)=B(k)}.          \tag{7.1}
\]

This corollary is a sufficient construction theorem.  The counterexamples in
Section 5 prove that its guard or laminar-domination hypothesis cannot be
replaced by scalar capacity, ordinary Hall, or interval geometry alone.

## 8. Authentication and relation to existing results

The exact chain-aligned counterexamples are independently enumerated by

```text
scratch/audit_commoncap_chain_aligned_minimal_counterexample_20260731.py
scratch/commoncap_chain_aligned_minimal_counterexample_20260731.audit.json
```

with script SHA-256
`ffb44523c28a27baeecc6dc6e0d00c0eba64dc1a2fd3e21976d35ca1ce8177df`,
JSON SHA-256
`f3ccc762072f68974eb5025b4d77a8d7be8adb56278fc5abfc48d7fb8a8b32b0`,
and payload
`f47bfdb1e734e5cda7ff2cbbff8d06080719b7c5d4a6fff9ab159b6edd80e3d7`.

The full tiny-instance proof is recorded in
`MATH_AUDIT_COMMON_CAP_CHAIN_ALIGNED_MINIMAL_COUNTEREXAMPLE_20260731.md`.

The interval-cut/greedy equivalence and fractional boundary have a separate
finite audit:

```text
scratch/audit_guarded_convex_commoncap_compiler_20260731.py
  SHA-256 4ade68468da990a68b47e0f396ca14f35a50c5d5c2cd49454e458fffe9dc5fba
scratch/guarded_convex_commoncap_compiler_20260731.audit.json
  SHA-256 d5794e60a804e0d3ecb2afe3e4165e527e5c88199f4a7b73041bff386bfa5f67
  payload 34b48021acd330e139df6ab83ce4018a208c7d6fdf709ec3b78902d1df29b215
```

It exhausts all 11,385 labelled convex interval-neighbourhood systems with
\(1\le m\le4\) cells and \(0\le n\le m\) targets; cases \(n>m\) are
trivially infeasible.  It finds exact agreement among (3.3), brute-force
matching, and earliest-deadline greedy in every enumerated case.  It also
checks every row of the fractional \(K_{2,2}\) point and independently replays
the forced Johnson core.

The guarded part of Theorem 3.1 specializes the previously proved
co-selectable guarded-Hall compiler; its new contribution here is the exact
convex interval-cut reduction and canonical greedy assignment.  Theorem 4.1
packages exact conflict-clutter domination as a laminar-matroid/Rado
certificate.  Neither theorem assumes a completed matching or physical word.

K16 and the arbitrary-start calibration are frozen in:

```text
MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md
  SHA-256 89689b4a26ed9c02a58b13aca206238e4492eccdda779a893b2f929ef8bcbf88
scratch/k16_c7be_commonq_chain_independent_20260731.audit.json
  SHA-256 d451c9b3ef40d62c54cec9139b1a969d21c1952283ba82f037f122b58d42735d
  payload 80a94b84551c6c04a6c9a44d29e9615553ef721bb1409e700f65a933a9c030d2
MATH_AUDIT_MONOTONE_DEADLINE_RUN_STAIRCASE_ARBITRARY_STARTS_20260731.md
  SHA-256 1709fe2293ab93c5f4ce98153047621804e4c67c5e1f6a93562321307221a894
scratch/monotone_deadline_run_staircase_arbitrary_starts_20260731.audit.json
  SHA-256 2962af618842e751c8ed0c20f3d9d102090acbf09a1f7bbcb82e7e4173309f4a
  payload 12aaa0a0436ae9248f7031b6eeced84d3ef1801c9e03b0f769929418b877d0bc
```
