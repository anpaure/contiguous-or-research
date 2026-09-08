# `k=17`: exact disjoint support-two rooted-flag circuit selector

Date: 2026-08-01  
Lane: K / rooted-flag circuit packing  
Status: unconditional formulation and proof protocol; no optimum of the
resulting finite instance is claimed here

## 1. Scope and seed binding

Let `V` be the 1,430 rank-eight necklace roots.  At each `q in V`, let
`F_q` be the complete set of literal rooted flags

\[
                    C_0\subset C_0\cup C_1\subset Q_q,
\]

including the type and phase data.  For a flag `f`, write `r(f)` for the
exact resource vector of
`MATH_THEOREM_A_K17_ROOTED_FLAG_PALETTE_SWITCH_BASIS_AND_SUPPORT2_WITNESS_20260801.md`:
one type row, the outer lower-colour row, and, when its rank is at least two,
the inner lower-colour row.  Inner and outer occurrences of the same
necklace use the same resource coordinate.

Fix a palette-perfect baseline `F^0=(f_q^0:q in V)` and put

\[
                         \delta_q(f)=r(f)-r(f_q^0).             \tag{1.1}
\]

The two authenticated baselines currently relevant are distinct inputs:

```text
scratch/k17_rank8_rooted_static_age_flag_20260801.certificate.tsv
  SHA256 ad9e15f724b5048c00cf43ae007d0e02c03c72204a5c169736461e946a166eab

scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/certificate_28401.tsv
  SHA256 e973061f57d1e4c141dc42489da289a0b454d4b9fd27369d887561fdea29299e
```

For the first seed, the independently enumerated catalogue has 2,557
nontrivial unary circuits and 214,711 indecomposable binary circuits; its
baseline packet statistics are `530/761/848`.  The second seed has
independently replayed packet statistics
`matching/zero-out/zero-in = 557/739/822`; these are calibration data, not
an optimized selector verdict.

The finite calibrations are bound to

```text
scratch/audit_threadA_k17_ad9e_global_support2_delta_counts_20260801.cpp
  SHA256 c922ba37d5244fb3882a6d01aee70956069a2b8cb54b14d79a00ea4bea9bf35c

scratch/threadA_k17_global_support2_delta_counts_h100_20260801/
  global_support2_delta_counts.audit.json
  SHA256 2bab3453acb297a0fc209e536b338072e4f2711275f57ee220e2262743cf8798

scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/
  certificate_28401.independent.audit.json
  SHA256 dbce1503729e36cd378e5a0375f8ed499fdf64d84478f167ecefd51ee081a93a
```

The circuit catalogue is **baseline-relative**.  Formula (1.1), and hence
every circuit identifier, must be regenerated when the input certificate
changes.  In particular, the `ad9e15...` catalogue cannot simply be applied
to the `e97306...` rows.

This note optimizes only the root-level packet-support graph.  It does not
impose the owner/state transversal, upper shadows, voltage, residence,
opening, or compiler rows.

## 2. Complete support-at-most-two catalogue

Define

\[
\begin{split}
 \mathcal{C}_1(F^0)&=\{(q;f): f\ne f_q^0,\ \delta_q(f)=0\},\\
 \mathcal{C}_2(F^0)&=\{(p,f;q,g):p<q,\
       \delta_p(f)=-\delta_q(g)\ne0\}.
                                                               \tag{2.1}
\end{split}
\]

Every member `c` has a real-root support `S(c)` of size one or two and a
specified replacement `f_c(q)` at each supported root.

### Theorem 2.1 (catalogue completeness)

1. Every member of (2.1) is a literal palette-preserving circuit.
2. Every nontrivial palette-preserving switch supported on one root belongs
   to `C_1`.
3. Every indecomposable palette-preserving switch supported on two distinct
   roots belongs to `C_2`.
4. A decomposable two-root switch is precisely a pair of disjoint unary
   circuits and need not be duplicated in `C_2`.

#### Proof

For one root, resource preservation is exactly `delta_q(f)=0`.  For two
roots it is exactly
`delta_p(f)+delta_q(g)=0`.  If either summand vanishes, then both vanish and
the switch decomposes into two unary circuits.  Otherwise the two nonzero
deltas are opposite, which is the second line of (2.1).  Literal membership
in `F_p,F_q` supplies all containment and phase conditions.  These
alternatives exhaust supports one and two.  \(\square\)

A **disjoint circuit packet** is a subset `X` of
`C_1 union C_2` satisfying

\[
                         \sum_{c:q\in S(c)}x_c\le1
                         \qquad(q\in V).                       \tag{2.2}
\]

Its final flag at `q` is `f_c(q)` if the unique selected circuit incident
with `q` is `c`, and is `f_q^0` otherwise.

### Corollary 2.2 (exact palette preservation)

Every packet satisfying (2.2) produces a literal palette-perfect factor.
Conversely, every factor obtained from `F^0` by partitioning its changed
roots into individually resource-neutral blocks of size at most two is
represented by exactly such a packet, up to duplicate catalogue records
with the same literal replacement map.

#### Proof

The supports are disjoint, so the total resource change is the sum of the
individual zero circuit changes.  Conversely, Theorem 2.1 identifies the
circuit on every block.  \(\square\)

Combinatorially, make one multigraph whose real vertices are the roots,
whose binary circuits are parallel edges, and whose unary circuit `c` at
`q` is the edge from `q` to a private dummy vertex `d_c`.  Then (2.2) is
exactly a matching in this multigraph.  This observation makes additive
circuit objectives easy.  It does **not** make the chronology objective
additive: a turn between two changed roots depends jointly on the two
selected circuits.

## 3. Literal recomputation of packet turns

Let `Q_p` be the physical representative at source root `p`.  A rooted
transition geometry is a tuple

\[
                   \gamma=(p,\beta,x,q,\Delta)                  \tag{3.1}
\]

with `beta notin Q_p`, `x in Q_p union {beta}`, and

\[
 \rho^\Delta Q_q=(Q_p\cup\{\beta\})\setminus\{x\}.             \tag{3.2}
\]

For source flag `f=(C_0,C_1,C_2)` and target flag
`g=(D_0,D_1,D_2)`, rotate every `D_i` by `Delta` and put `D_3={x}`.
The geometry works exactly when

\[
 D_1\subseteq C_0,\qquad D_2\subseteq C_1,\qquad D_3\subseteq C_2,
                                                                    \tag{3.3}
\]

and

\[
 D_0=\{\beta\}\cup(C_0\setminus D_1)
                  \cup(C_1\setminus D_2)
                  \cup(C_2\setminus D_3).                       \tag{3.4}
\]

Define `T_pq(f,g)=1` iff at least one geometry (3.1) satisfies
(3.2)--(3.4).  For a selected packet `X`, its exact packet graph is

\[
       G_X=(V_L,V_R,E_X),\qquad
       pq\in E_X\iff T_{pq}(f_p^X,f_q^X)=1.                     \tag{3.5}
\]

Here the left and right copies of `V` are distinct, so a geometrically
legal `p=q` turn is a legitimate bipartite edge and contributes to both
degrees.  This is the “including loops” convention used by the authenticated
packet audits.  A nonloop objective is obtained simply by fixing every
`e_pp=0`; the convention must be recorded in the run manifest.

Write

\[
 \mu(X)=\nu(G_X),\quad
 Z^+(X)=|\{p:d^+_{G_X}(p)=0\}|,\quad
 Z^-(X)=|\{q:d^-_{G_X}(q)=0\}|.                               \tag{3.6}
\]

### Proposition 3.1 (why delta scoring is insufficient)

The data consisting of the individual edge additions/deletions of each
circuit do not determine `G_X`: when circuits incident with distinct roots
`p` and `q` are both selected, the truth of `pq` is
`T_pq(f_c(p),f_d(q))`, not either circuit's score against the old opposite
endpoint.  Formula (3.5) recomputes all old--old, changed--old,
old--changed, and changed--changed interactions and is therefore exact.

#### Proof

Exactly one literal option is final at each endpoint.  Equations
(3.2)--(3.4) are necessary and sufficient for the physical rooted
transition between those two options.  Taking their existential union over
geometries gives (3.5).  No additive single-circuit score contains the
changed--changed table entry in general.  \(\square\)

The permissive graph obtained by independently choosing a different option
at a root for every incident arc is only an upper-bound relaxation.  Its
matching number may be used as a safe ceiling, but it is not a realizable
selector certificate.

## 4. Exact zero-one formulation

Use one binary `x_c` per circuit and impose (2.2).  Let `O_q` be the set
consisting of the baseline flag and every distinct flag assigned at `q` by
some catalogue circuit.  Introduce final-mode variables `y_qf`.  They are
channelled exactly by

\[
\begin{split}
 y_{q,f_q^0}&=1-\sum_{c:q\in S(c)}x_c,\\
 y_{q,f}&=\sum_{c:q\in S(c),\ f_c(q)=f}x_c
                         &&(f\ne f_q^0).                       \tag{4.1}
\end{split}
\]

Because of (2.2), the right sides are zero-one and (4.1) gives exactly one
final mode per root while retaining the two-end correlation of every binary
circuit.

For every compatible quadruple `(p,f,q,g)` with `T_pq(f,g)=1`, introduce

\[
                         w_{pfqg}=y_{pf}\wedge y_{qg}.          \tag{4.2}
\]

Use one `e_pq` for each geometrically possible ordered root pair and impose

\[
                 e_{pq}=\bigvee_{f,g:T_{pq}(f,g)=1}w_{pfqg}.   \tag{4.3}
\]

Standard three-clause AND gates and a Tseitin OR make (4.2)--(4.3) an exact
CNF.  If the compatible list is empty, fix `e_pq=0`.  Notice that only
actually compatible option pairs need a witness variable; an all-pairs
table is unnecessary.

There is also a witness-free exact table encoding which can be smaller in
the O3 builder.  For every compatible pair add

\[
                  \neg y_{pf}\vee\neg y_{qg}\vee e_{pq},       \tag{4.3a}
\]

and, for each source mode `f`, add

\[
 \neg e_{pq}\vee\neg y_{pf}\vee
       \bigvee_{g:T_{pq}(f,g)=1} y_{qg}.                       \tag{4.3b}
\]

An empty last disjunction is allowed.  Since exactly one mode is true at
each endpoint, (4.3a)--(4.3b) are equivalent to (4.3).  The builder may
instead condition on target modes when that produces fewer literals; the
semantic map must record which orientation was used.

Introduce `o_p^+,o_q^-` and encode

\[
 o_p^+\longleftrightarrow\bigwedge_q\neg e_{pq},\qquad
 o_q^-\longleftrightarrow\bigwedge_p\neg e_{pq}.                \tag{4.4}
\]

For example, the first equivalence consists of

\[
 (\neg o_p^+\vee\neg e_{pq})\quad(q),
 \qquad
 (o_p^+\vee\bigvee_q e_{pq}).                                  \tag{4.5}
\]

Finally use matching variables `m_pq` with

\[
 m_{pq}\le e_{pq},\qquad
 \sum_qm_{pq}\le1,qquad \sum_pm_{pq}\le1.                    \tag{4.6}
\]

### Theorem 4.1 (selector exactness)

The integral solutions of (2.2), (4.1)--(4.6) project exactly to disjoint
support-at-most-two circuit packets together with a matching in their fully
recomputed packet graph.  Consequently

\[
 \max\sum_{pq}m_{pq}=\max_X\mu(X).                              \tag{4.7}
\]

At any fixed selector, (4.4) gives exactly `Z^+(X),Z^-(X)`.

#### Proof

Corollary 2.2 proves the selector claim.  Equations (4.1) choose its unique
final literal row at every root.  The AND/OR equivalences force `e` to be
exactly (3.5), including interactions between two selected circuits.
Equations (4.6) are precisely a bipartite matching in this graph.  Maximizing
its size therefore gives the maximum matching number.  Equations (4.4)
are the truth tables for zero degree.  \(\square\)

For the lexicographic objective requested here, maximize

\[
                \bigl(\mu(X),-Z^+(X),-Z^-(X)\bigr).             \tag{4.8}
\]

It can be solved in three bounded stages.  Equivalently, with
`W=|V|+1=1431`, maximize the 64-bit integer

\[
       W^2\sum m_{pq}-W\sum_po_p^+-\sum_qo_q^-.                 \tag{4.9}
\]

One unit in an earlier coordinate dominates the full possible range of all
later coordinates, so (4.9) is exactly (4.8), not a heuristic weighting.
If a different lexicographic order is desired, the same formulation remains
valid and only the staged bounds change.

## 5. Checkable optimum and ceiling certificate

Suppose a candidate packet independently replays to

\[
                         (\mu,Z^+,Z^-)=(M,P,Q).                 \tag{5.1}
\]

A proof-safe optimum package consists of the following.

1. A selector file listing the input-certificate SHA, canonical circuit
   IDs, and their literal replacement flags.
2. An independent replay which checks catalogue membership, root
   disjointness, the complete resource ledger, all geometries
   (3.2)--(3.4), zero degrees, and a fresh Hopcroft--Karp computation of
   `M`.
3. A deterministic DIMACS map and three independently DRAT-checked UNSAT
   formulas:

\[
\begin{array}{ll}
 \text{(i)}   & \text{base selector plus }\sum m\ge M+1,\\
 \text{(ii)}  & \text{base selector plus }\sum m\ge M,
                    \ \sum o^+\le P-1,\\
 \text{(iii)} & \text{base selector plus }\sum m\ge M,
                    \ \sum o^+\le P,
                    \ \sum o^-\le Q-1.
\end{array}                                                     \tag{5.2}
\]

The first proof is the global packet-matching ceiling.  Conditional on it,
the second proves the optimal zero-out count; conditional on both, the third
proves the optimal zero-in count.  A SAT assignment without the independent
Hopcroft--Karp replay proves only a lower bound on `mu`, because its selected
`m` need not itself be maximum.

Every proof bundle must retain the input-certificate hash, catalogue hash,
builder hash, variable map, DIMACS header/count audit, solver exit status,
full DRAT (or a verified trimmed core), and verifier logs.  Timeout,
resource exhaustion, a truncated proof, or a proof for only one fixed
circuit root is `UNKNOWN`, never a ceiling for (2.1).

### Corollary 5.1 (precise finite scope)

If (5.2) verifies for the catalogue generated from `ad9e15...`, then
`(M,P,Q)` is the exact optimum over every simultaneous root-disjoint packing
of its 2,557 unary and 214,711 indecomposable binary circuits, including all
nonadditive interactions between selected circuits.  It says nothing about
overlapping/sequential circuits, primitive support at least three, or a
catalogue regenerated from `e97306...`.
