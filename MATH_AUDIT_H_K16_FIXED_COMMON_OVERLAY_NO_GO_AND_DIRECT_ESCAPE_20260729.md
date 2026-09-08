# The fixed-common `k=16` endpoint overlay and its mandatory escape

## Exact scope, direct resident escape, and the required broader factor space

Date: 2026-07-29  
Lane: H  
Status: **exact fixed-common reduction; conditional trusted-transcript no-go;
broader resident search remains open**

## 1. Verdict

Let `R_0` be the oriented-port PBBS factor

```text
scratch/k16_pbbs_oriented_noaa_softq1_20260729.json
SHA-256 50c3c3786762907b67281142e33cf69c2d476282b0e1bb70a6e74a6fb43c6cbf
```

and let `Q` be the q1-perfect dynamic-cross factor

```text
scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json
SHA-256 d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8.
```

Both are spanning physical Johnson 2-factors on the 12,870 rank-eight
states.  The factor `R_0` has seven components, no positive coordinate run
of length below four, and 758 lower plus 993 upper q1 holes.  The factor `Q`
has both q1 palettes but 2,205 positive short runs.

Here “positive-resident” means exactly that every cyclic coordinate-1 run
has length at least four; no assertion about coordinate-0 run lengths is
being made.

Under the supplied assertion that the saved solve used both q1 shores, their
fixed-common affine overlay is closed.  Even allowing an arbitrary balanced
circulation—not merely a chosen circuit decomposition—there is no hybrid
which simultaneously

1. preserves all lower and upper q1 colours, and
2. destroys the closure of every one of the 2,205 short runs already present
   in `Q`.

This is already a necessary relaxation of positive residence, so the fibre
is infeasible subject to that invocation qualification.  The saved machine
transcript is

```text
scratch/k16_resident_q1_overlay_circulation_cegar_infeasible_20260729.json.
```

The conclusion is deliberately narrower than “the endpoint union is
impossible”: all 392 edges common to `R_0` and `Q` are fixed in the model.
The no-go proves the disjunction

> with respect to this endpoint pair, every positive-resident q1-perfect
> factor must either release a fixed common edge or use an edge outside
> $R_0\cup Q$.

The new direct resident descent does both.  The factor

```text
scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json
SHA-256 d28491b708d5a83e8abcde20fda8ad523cd58f9c662f46ae2d9c2507ba73e951
```

is positive-resident, has only two components, and reduces the q1 deficit
from 1,751 to 1,190.  Relative to `R_0` it changes 1,815 edges, of which
1,754 added edges lie outside $R_0\cup Q$; it also releases 62 of the 392
fixed-common edges.  Thus the useful descent direction is overwhelmingly
absent from the closed two-endpoint fibre.

## 2. Physical canonicalization

Every physical edge is represented by its unordered Johnson key

\[
                         (\min\{u,v\},\max\{u,v\}).     \tag{2.1}
\]

This is essential.  The PBBS endpoint is not `C_15`-equivariant: it uses
2,784 quotient orbit IDs with varying multiplicities, whereas the
equivariant q1 endpoint uses all 15 phases of 858 orbit IDs.  A bare quotient
support XOR loses multiplicity and phase and is not degree-balanced.

The ambient physical Johnson graph `J(16,8)` has 411,840 edges:

\[
               180180\ AA+51480\ AB+180180\ BB.        \tag{2.2}
\]

For reference, comparing `R_0` to the canonical equivariant factor

```text
scratch/k16_qfactor_q1_topresident_hamilton_20260729.json
SHA-256 f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5
```

gives 425 common edges and 12,445 edges on each difference shore.  That
entire physical symmetric difference is one connected balanced component
on all 12,870 states.  Hence connected-component toggling has only the two
endpoints.  At 12,020 vertices the residual degree is `(2,2)`, so finer
alternating-circuit decompositions depend on noncanonical local pairings.

The stronger circulation no-go below uses `Q`, not this canonical endpoint.
It therefore must not be cited as a no-go for every possible q1 endpoint.

## 3. The exact fixed-common circulation

Write

\[
 C=R_0\cap Q,\qquad R=R_0\setminus Q,
 \qquad B=Q\setminus R_0.                              \tag{3.1}
\]

The exact physical census is

\[
                         |C|=392,                      \tag{3.2}
\]

\[
                         |R|=|B|=12478.                \tag{3.3}
\]

Choose `x_r` for `r in R` and `y_b` for `b in B`.  The hybrid is

\[
      F(x,y)=C\cup\{b\in B:y_b=0\}
                    \cup\{r\in R:x_r=1\}.             \tag{3.4}
\]

Since $Q=C\cup B$ has degree two, (3.4) has degree two exactly when

\[
      \sum_{r\ni v}x_r=\sum_{b\ni v}y_b
      \qquad\text{for every physical middle state }v. \tag{3.5}
\]

Thus (3.5) is the full binary balanced-circulation family in the symmetric
difference.  It contains every union of alternating circuits for every
possible local red/blue pairing; choosing one circuit decomposition first
is only a restriction of (3.5).

For a physical lower or upper q1 colour $t$, let $P_t^-$ and $P_t^+$
be its lower and upper provider sets, and let $m_Q^-(t)$ and $m_Q^+(t)$
be its multiplicities in $Q$.  Exact q1 preservation is

\[
 m_Q^\pm(t)-\sum_{b\in B\cap P_t^\pm}y_b
             +\sum_{r\in R\cap P_t^\pm}x_r\ge1.       \tag{3.6}
\]

Every short run of `Q` has a forcing closure of two, three, or four selected
physical edges.  Because no closure is wholly contained in `C`, each has a
nonempty set $S\subseteq B$ of removable edges.  Destroying all initial
motifs requires

\[
                         \sum_{b\in S}y_b\ge1           \tag{3.7}
\]

for each of the 2,205 closures.  These are necessary for residence; newly
created motifs would require further CEGAR rows only after a solution of
(3.5)--(3.7).

### Lemma 3.1 (exact fixed-common parametrization)

The map (3.4) is a bijection between binary solutions of (3.5) and spanning
physical 2-factors (F) satisfying

\[
                         C\subseteq F\subseteq R_0\cup Q.               \tag{3.8}
\]

#### Proof

For a binary pair ((x,y)), the degree of (F(x,y)) at (v) equals the
degree two of (Q), minus the number of selected (B)-edges removed at
(v), plus the number of selected (R)-edges added there.  It is therefore
two exactly when (3.5) holds.  Conversely, a factor between (C) and
(R_0\cup Q=C\sqcup R\sqcup B) uniquely specifies which (B)-edges were
removed and which (R)-edges were added.  Its degree-two equations are
exactly (3.5).  QED.

### Conditional Theorem 3.2 (fixed-common endpoint-fibre no-go)

Assume the saved run used `q1_mode=both`, as asserted in the supplied result.
Then the integral system (3.5), all lower and upper rows (3.6), and all 2,205
rows (3.7) is infeasible.

#### Audit

The intended model has 24,956 Boolean variables and 37,954 rows: 12,869
nontrivial degree equalities, 22,880 physical q1 rows, and 2,205 distinct
motif rows.  It has 392 fixed common edges and no fixed-common initial motif.
The saved transcript returns `INFEASIBLE` in its first solve.  The literal
model builder is

```text
scratch/solve_k16_resident_q1_overlay_circulation_cegar_20260729.py.
```

This is a trusted CP-SAT infeasibility transcript, not a standalone
proof-logging certificate.  There is also a provenance defect: the saved
JSON records both endpoint hashes, all 2,205 distinct initial rows, and the
first-round `INFEASIBLE` status, but it does not record the command,
`q1_mode`, builder/model digest, dependency hashes, or solver parameters.
The current builder postdates the artifact by about five minutes and emits
fields absent from it.  The supplied theorem statement and the builder's
default both specify `both`; the JSON alone does not bind that invocation.
Subject to this explicit transcript qualification, the
algebraic scope (3.4)--(3.7) is exact: no circuit pairing or Boolean subset
inside this fixed-common fibre was omitted.

### Conditional Corollary 3.3 (mandatory escape)

Let $F$ be a positive-resident q1-perfect factor.  If $F$ retains every
edge of $C$, then it cannot be contained in $R_0\cup Q$.  Equivalently,
every global solution obeys

\[
 |C\setminus F|+
 |F\setminus(R_0\cup Q)|\ge1.                         \tag{3.9}
\]

This is the smallest correct replacement for the now-closed alternating
overlay lane.  It does not assert that releasing only one common edge, or
adding only one exterior edge, is sufficient.

## 4. The direct resident descent leaves the fibre

Let `R_1` be the two-component 1,190-hole resident factor above.  Exact
physical replay gives

```text
components                 2 = 4435 + 8435
lower q1 holes             492
upper q1 holes             698
positive residence defects 0.
```

Its symmetric difference from `R_0` has 1,815 edges on each shore.  Of the
1,815 added edges,

\[
                         1754                            \tag{4.1}
\]

lie outside $R_0\cup Q$, with sector census

\[
                         239\ AA+386\ AB+1129\ BB.      \tag{4.2}
\]

It also removes 62 fixed-common edges:

\[
                         6\ AA+19\ AB+37\ BB.           \tag{4.3}
\]

The q1 change is not merely a lower total with unrelated colours.  Relative
to `R_0`, `R_1` repairs 357 lower and 519 upper holes, while newly losing 91
lower and 224 upper colours, for net improvement

\[
 (357-91)+(519-224)=561.                               \tag{4.4}
\]

Among the repaired colours, 346 of 357 lower and 505 of 519 upper colours
have a selected provider on an edge outside the closed endpoint union.
Only 12 repaired lower and 14 repaired upper colours have a selected
provider in the dynamic-`Q`-only shore retained by `R_1` (one lower colour
has both kinds).  Since a colour absent from `R_0` can only be repaired by
an added edge, these data witness that exterior edges supply almost all of
the observed repairs.  They are not a lower bound on the exterior support
of a different future solution.

### Theorem 4.1 (the broader directions are quantitatively active)

The direct resident descent `R_0 -> R_1` is not representable by any
circulation (3.4).  It uses 1,754 exterior edges and releases 62 common
edges, while preserving positive residence and improving q1 by 561.

#### Proof

Canonicalize both physical edge sets by (2.1).  Direct set difference gives
the 1,815/1,815 exchange, (4.1)--(4.3), and provider intersections give
(4.4).  Either an exterior edge or a released common edge already excludes
representation by (3.4); `R_1` has both.  Literal traversal verifies degree
two, components, q1 support, and every positive run.  QED.

## 5. Why the broader factor space is genuinely new

The fixed-common model is not failing because an alternating-cycle
decomposition was chosen badly.  Equation (3.5) is the entire integral
balanced-circulation space on the physical symmetric difference.  Changing
the pairing of red and blue half-edges, combining intersecting circuits, or
toggling any collection of such circuits produces no variable outside
(3.5).

There are exactly two ways to add columns to that system without changing
the endpoint pair:

1. deleting $c\in C$ creates one unit of deficit at each endpoint of a
   formerly frozen common edge; and
2. selecting $e\notin R_0\cup Q$ supplies a new endpoint-incidence column
   and potentially a new lower/upper provider pair.

The descent $R_0\to R_1$ uses both mechanisms.  Of its 1,815 additions,
only 61 are `Q`-only edges and 1,754 are exterior; of its 1,815 deletions,
62 are formerly common edges.  Thus over 96 percent of its added support is
not expressible in the old circulation lattice.  This does not prove that a
completed factor needs comparable edit radius.  It proves the sharper
architectural point: further circuit enumeration inside the closed overlay
cannot even represent the known improving direction.

## 6. Correct next model

Starting from `Q`, add variables of three kinds:

1. `y_b` removes `Q`-only edges `b in B`;
2. `z_c` removes common edges `c in C`;
3. `x_e` adds any permitted unselected edge `e`, including both `R` and an
   exterior bank `E_out`.

The exact degree equation is

\[
 \sum_{e\ni v}x_e
 =\sum_{b\ni v}y_b+\sum_{c\ni v}z_c                 \tag{6.1}
\]

after separating additions from selected source edges.  Q1 rows become

\[
 m_Q^\pm(t)-y(P_t^\pm)-z(P_t^\pm)+x(P_t^\pm)\ge1,    \tag{6.2}
\]

and each old motif may be hit by either a `y` or a `z` edge.  Literal new
motifs remain a CEGAR condition.

The no-go proves the mandatory escape row

\[
                         \sum_c z_c+
                         \sum_{e\in E_{out}}x_e\ge1.   \tag{6.3}
\]

The useful practical center is now `R_1`, not a Boolean subset of a fixed
endpoint decomposition.  Its 1,190-hole deficit and two components are both
strictly smaller than those of `R_0`.  A target-aware exterior bank can be
seeded by the 1,754 exact edges in (4.1), while the oriented-port residence
constraints remain hard.  This enlarges the state space in precisely the
two directions that the fixed-common model omitted.

## 7. Provenance and artifacts

The first PBBS artifact has incomplete generation provenance.  It binds the
A-cycle file (`bc58e466...`) and B certificate (`91c43465...`) but omits the
PBBS baseline hash, generator/dependency hashes, command, seed, workers,
time limit, and a payload digest.  Its saved soft counters are stale:
metadata says `772+998` holes and objective `21110`, while literal replay of
the saved edges gives `758+993` and objective `21129`.  Only the physical
witness and literal audit are used here.

New solver-free comparison audit:

```text
scratch/audit_k16_overlay_escape_and_direct_descent_20260729.py
SHA-256 7c4efce50859a6eaf4eb915a428ccddd97ac64d7d321752b30481ac4da85d166

scratch/k16_fixed_common_overlay_no_go_direct_escape_20260729.audit.json
SHA-256 a3a142f25fc37f29bb3eccc6725582b935f8b74ce141707637514010904536ad

scratch/k16_resident_q1_overlay_circulation_cegar_infeasible_20260729.json
SHA-256 ec86d9378c2e64f7c343b9fbbff59c1d66439b1de43e2d01ebc474912564991d

scratch/solve_k16_resident_q1_overlay_circulation_cegar_20260729.py
SHA-256 9d33579e787cf209e4de7d9aba0f2e7aaff119f7fd6203af8e2f5a20ea57df51
```

It independently reconstructs `R_0`, `R_1`, dynamic `Q`, and canonical `Q`,
then verifies every count in Sections 2 and 4.  No SAT search, GPU, or web
access was used.  The Boolean circuit CEGAR file created during the previous
sub-lane was deliberately not run after the unrestricted circulation no-go
arrived; its narrower search is subsumed by Theorem 3.1.
