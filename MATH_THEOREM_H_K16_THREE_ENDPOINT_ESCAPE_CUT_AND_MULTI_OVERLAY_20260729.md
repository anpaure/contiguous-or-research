# A three-endpoint escape cut and exact multi-overlay for `k=16`

Date: 2026-07-29  
Lane: H  
Status: **superseded as a feasibility proposal: the exact parametrization and
escape cuts remain valid, but a later grouped-core theorem proves the full
multi-overlay union infeasible**

> **Superseding result.**  The union proposed below is not an open positive
> lane.  `MATH_THEOREM_H_K16_GROUPED_HALL_CORE_AND_MULTIPORTAL_20260729.md`
> gives a solver-free grouped Hall/degree contradiction and the required
> exterior portal bank.  Sections 2--5 below remain valid reductions and
> censuses only.

## 1. Endpoints and audited census

Let (Q) be the dynamic q1-perfect factor and let (R_0,R_1,R_2) be the
three positive-resident PBBS descendants.  Their physical edge sets have
size 12,870.  Literal replay gives

| factor | components | lower q1 holes | upper q1 holes | positive short runs |
|---|---:|---:|---:|---:|
| (Q) | 5 | 0 | 0 | 2,205 |
| (R_0) | 7 | 758 | 993 | 0 |
| (R_1) | 2 | 492 | 698 | 0 |
| (R_2) | 4 | 443 | 646 | 0 |

Thus the resident descent improves the total q1 deficit

\[
                         1751\longrightarrow1190\longrightarrow1089,
\]

but does not enter any of the three fixed-common (Q,R_i) fibres.

The three supplied circulation transcripts all report first-round
`INFEASIBLE` with both q1 palettes and the 2,205 initial motif closures.
Their exact endpoint censuses are

\[
 |Q\cap R_i|=(392,391,390),\qquad
 |Q\setminus R_i|=(12478,12479,12480).                 \tag{1.1}
\]

There is one provenance qualification.  Each compact JSON omits
`q1_mode`, the command, and a builder/model digest.  Consequently the frozen
files alone do not certify the asserted both-q1 invocation.  Every theorem
below that invokes pairwise infeasibility is conditional on the supplied
exact assertion; the edge censuses and multi-overlay identities are
unconditional literal audits.

## 2. Exact multi-overlay factor theorem

Put

\[
 C_*:=Q\cap R_0\cap R_1\cap R_2,
 \qquad U_*:=Q\cup R_0\cup R_1\cup R_2,                \tag{2.1}
\]

and define the disjoint variable shores

\[
 B_*:=Q\setminus C_*,
 \qquad A_*:=(R_0\cup R_1\cup R_2)\setminus Q.         \tag{2.2}
\]

For (y\in\{0,1\}^{B_*}) and (x\in\{0,1\}^{A_*}), set

\[
 F(x,y)=C_*\cup\{b\in B_*:y_b=0\}
              \cup\{a\in A_*:x_a=1\}.               \tag{2.3}
\]

### Theorem 2.1 (multi-overlay parametrization)

The map (2.3) is a bijection between spanning physical 2-factors (F)
satisfying

\[
                         C_*\subseteq F\subseteq U_*                  \tag{2.4}
\]

and binary pairs ((x,y)) satisfying

\[
 sum_{a\in A_*:a\ni v}x_a
 =sum_{b\in B_*:b\ni v}y_b
 \qquad(v\in\tbinom{[16]}8).                          \tag{2.5}
\]

#### Proof

The factor (Q=C_*\sqcup B_*) has degree two.  Formula (2.3) removes
exactly the selected (B_*)-edges and adds exactly the selected
(A_*)-edges, so its degree at (v) is two precisely when (2.5) holds.
Conversely, every (F) in (2.4) uniquely specifies those removals and
additions.  QED.

This is a genuinely mixed circulation, not a choice among three previously
fixed circuit decompositions.  The (Q,R_i) pairwise fibre is recovered by
setting (y=0) on (Q\cap R_i) and (x=0) on (A_*\setminus R_i).

## 3. Exact q1 and residence rows

For a lower or upper q1 colour (t), let (P_t^\pm) be its physical
provider edges and (m_Q^\pm(t)) its multiplicity in (Q).  Both q1
palettes are equivalent to

\[
 m_Q^\pm(t)
 -\sum_{b\in B_*\cap P_t^\pm}y_b
 +\sum_{a\in A_*\cap P_t^\pm}x_a\ge1                 \tag{3.1}
\]

for every physical lower and upper colour.

For each of the 2,205 positive short runs of (Q), let (K) be its two-,
three-, or four-edge closure.  Every positive-resident factor must obey

\[
                         \sum_{b\in K\cap B_*}y_b\ge1.                \tag{3.2}
\]

The set (K\cap B_*) is nonempty: each pairwise audit found no closure
wholly contained in (Q\cap R_i), and (C_*\subseteq Q\cap R_i).
Equations (2.5), (3.1), and (3.2) are exact necessary rows.  They do not by
themselves exclude new short runs created by the mixed factor; literal
new-motif rows must be added by CEGAR until positive residence is attained.

## 4. The common consequence of the three pairwise no-gos

For (i=0,1,2), put

\[
 C_i:=Q\cap R_i,qquad U_i:=Q\cup R_i.                 \tag{4.1}
\]

### Theorem 4.1 (three endpoint-escape cuts)

Assume the three supplied pairwise no-gos.  Every positive-resident,
q1-perfect spanning factor (F) satisfies, for each (i),

\[
                         |C_i\setminus F|+|F\setminus U_i|\ge1.       \tag{4.2}
\]

Within the multi-overlay (2.3), (4.2) is the linear row

\[
 \sum_{b\in(C_i\setminus C_*)}y_b
 +\sum_{a\in(A_*\setminus R_i)}x_a\ge1.              \tag{4.3}
\]

#### Proof

If (4.2) failed, then (C_i\subseteq F\subseteq U_i), placing (F) in
the pairwise fixed-common fibre declared infeasible.  In (2.3), the first
term of (4.2) consists exactly of removed (Q)-edges belonging to (R_i),
and the second consists exactly of selected additions not belonging to
(R_i), which gives (4.3).  QED.

These are the strongest proof-safe common cuts extractable from the three
status artifacts alone.  They are endpoint escape cuts, not a recovered
CP-SAT Hall core: the compact transcripts contain no assumptions,
unsatisfiable core, proof log, or dual multipliers from which a common
palette--motif shore could be reconstructed.

### Corollary 4.2 (aggregate escape cut)

For an edge (e), let

\[
 S(e):=\{i:e\in R_i\}.
\]

Summing (4.3) gives

\[
 \sum_{b\in B_*}|S(b)|y_b
 +\sum_{a\in A_*}(3-|S(a)|)x_a\ge3.                  \tag{4.4}
\]

Every coefficient in (4.4) is at most two: an edge of (B_*) cannot lie
in all three residents, while every edge of (A_*) lies in at least one.
Hence every feasible multi-overlay factor must select at least two escape
variables.  This is a lower bound on endpoint-boundary crossings, not on
total replacement radius.

## 5. Exact size of the proposed move

The four-endpoint physical census is

\[
 |C_*|=324,\quad |B_*|=12546,\quad |A_*|=14700,
 \quad |U_*|=27570.                                   \tag{5.1}
\]

Thus the proposed master has 27,246 meaningful Boolean variables.  All
12,870 middle vertices occur in (2.5).  With both physical q1 shores, the
2,205 initial motif rows, and the three escape cuts, its initial row count
is

\[
 12870+22880+2205+3=37958.                            \tag{5.2}
\]

Relative to the three pairwise models, it adds only

| excluded pair | extra removable common edges | extra addition edges | total new columns |
|---|---:|---:|---:|
| (R_0) | 68 | 2,222 | 2,290 |
| (R_1) | 67 | 2,221 | 2,288 |
| (R_2) | 66 | 2,220 | 2,286 |

These are exactly the columns appearing in the corresponding escape row
(4.3).  In particular, another pairwise circuit search cannot use any of
them; the three-factor master adds precisely the missing directions forced
by the three no-gos.

The resident addition-edge membership histogram, with bits ordered
((R_2,R_1,R_0)), is

\[
\begin{array}{c|rrrrrrr}
\text{mask}&001&010&011&100&101&110&111\\\hline
\text{count}&1670&339&211&468&83&1415&10514.
\end{array}                                           \tag{5.3}
\]

The 2,286--2,290 extra columns are therefore not a cosmetic enlargement:
they permit cross-descendant combinations that no single (Q,R_i)
circulation can express.

## 6. Precise boundary

Proved unconditionally:

1. the endpoint edge censuses and resident/q1 audits;
2. the exact multi-overlay parametrization (2.3)--(2.5);
3. the q1 and old-motif necessary rows; and
4. the 27,246-variable/37,958-row initial master census.

Conditional only on the asserted both-q1 pairwise solve invocations:

1. the three escape rows (4.3);
2. the aggregate cut (4.4); and
3. the two-escape-variable lower bound.

Unproved: feasibility of the multi-overlay, destruction of all newly
created motifs, connectivity, and the full `k=16` compiler/word.  A common
deeper Hall shore has not been certified by the current compact
infeasibility artifacts.

## 7. Artifacts

```text
scratch/audit_k16_three_resident_overlay_geometry_20260729.py
SHA-256 31fdf457f6c8ffab0f3646016d08fbede43b9ca7f5113ff77abcd6faba9cde28

scratch/k16_three_resident_overlay_geometry_20260729.audit.json
SHA-256 6ee426f3be4c576e5a94a0136816fdab1cd74fdee07a0d6b8c77628621aa4ff9

scratch/k16_resident_q1_overlay_circulation_cegar_infeasible_20260729.json
SHA-256 ec86d9378c2e64f7c343b9fbbff59c1d66439b1de43e2d01ebc474912564991d

scratch/k16_resident_resume1_q1_overlay_circulation_infeasible_20260729.json
SHA-256 bf8ec3b31fa5e7b7ec0b209689d8787f041bbcd4fe5737108e4df3a1d5623a09

scratch/k16_resident_resume2_q1_overlay_circulation_infeasible_20260729.json
SHA-256 5ff8c16bf8df803c0ff2132b19d6a48b680b58344860e1434014dc6a408c0250
```

No heavy local search, SAT, GPU, or web access was used.
