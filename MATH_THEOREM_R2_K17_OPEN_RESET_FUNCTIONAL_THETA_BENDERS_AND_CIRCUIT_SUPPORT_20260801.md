# `k=17`, `d=3` R2: opened-reset functional attachment, exact punctured-Hall Benders cuts, and circuit support

Date: 2026-08-01  
Lane: R2 / compact quotient flag--owner co-design  
Status: exact theorem and compact formulation; no new finite calibration

## 0. Result and boundary

This note rebases R2 on the two frozen inputs

```text
MATH_THEOREM_D3_QUOTIENT_FLAG_NORMAL_FORM_FUNCTIONAL_HALL_AND_COMPACT_CODESIGN_20260801.md
SHA256 e6d3524a802139d0b754bab47c7387919239850a1b5d7c55b94a1f79ef02e916

MATH_THEOREM_K17_RESET_CONDITIONED_THREE_MATROID_AND_FUNCTIONAL_FLOW_GATE_20260801.md
SHA256 5647ac545ddcafa37e4ada27d3105c00c6f4739eb6956072ac0876b5de4ba9f6
```

Open the verified eight-flag reset between `f_7` and `f_0` and retain the
seven turns

\[
 {\cal S}=\{(T_a,T_{a+1},U_a):0\le a<7\}.                  \tag{0.1}
\]

After deleting their used tail, head, and owner resources, all three
residual shores have size `1423`.  There is an exact compact co-design:

1. choose one normalized depth-three flag option at every root, with the
   reset flags fixed and all named high targets offered;
2. choose one aligned head--owner column at every residual head and owner;
   its owner projection is the functional bijection `theta`;
3. separate the remaining predecessor matching by exact symbolic
   punctured-containment Hall cuts.

The separator is one bipartite min cut.  After physical alignment labels
are exposed, it decomposes into at most sixteen independent punctured-facet
blocks.  Every Benders row remains valid while the flags change because its
neighbourhood bits are Boolean functions of the master variables; incumbent
neighbourhood coefficients are never frozen.

There is no instance-independent numerical circuit-support minimum beyond
the following exact boundary.

* A cut-crossing exchange has joint root support at least one.
* Support one is possible only through a same-root coupled flag/column
  substitution which keeps the owner fixed and preserves alignment flux.
* A nonparallel change of `theta` has support at least two; its smallest
  possible component is a two-head/two-owner alternating four-cycle.
* For a frozen integral incumbent and a returned shore `X`, the exact
  support is the optimum of the compact binary programme in Section 6.
* Relative to the audited independent flag table, any **full** functional
  completion must change at least `287` flag-root options.  This is a rank
  lower bound, not a one-shore crossing witness.

The existing opened-reset audit does not freeze an aligned `theta` or a
canonical punctured Hall shore.  Its `850/1423` value is for the more
permissive uncoloured predecessor graph.  Consequently a numerical
incumbent-specific support calibration would require an arbitrary new
choice of data and is not claimed here.

The construction encodes an owner-exact directed cycle cover containing the
seven prescribed reset turns and the depth-three `P/T` high-target offers,
including only the reset `q1/q2` colours already priced by the input theorem.
It does not encode connected topology, nonzero voltage, any additional
`q2`/upper rows, residence outside the reset, global opening, or the
compiler.

## 1. Normalized flags, aligned columns, and the opened residual

Put `n=17`, `m=8`, and

\[
 {\cal R}=\binom{\mathbb Z_{17}}8/C_{17},
 \qquad
 {\cal O}=\binom{\mathbb Z_{17}}9/C_{17}.                   \tag{1.1}
\]

Both have size `1430`.  A normalized flag option is

\[
 f=(S,z),\qquad |S|=6,\quad 0,z\notin S,\quad z\ne0,        \tag{1.2}
\]

representing

\[
 S\cup\{0,z\}\supset S\cup\{0\}\supset S.               \tag{1.3}
\]

Write

\[
 r(f)=[S\cup\{0,z\}],\qquad P(f)=[S\cup\{0\}],
 \qquad T(f)=[S].                                          \tag{1.4}
\]

There are `56` options at each root and

\[
 |{\cal F}|=16\binom{15}{6}=80,080.                         \tag{1.5}
\]

If `g` has head signature `(H_g,gamma_g)`, an aligned column is a record

\[
 a=(g,z),\qquad z\notin H_g\cup\{0\},                      \tag{1.6}
\]

with

\[
 q(a)=r(g),\qquad o(a)=[H_g\cup\{0,z\}],\qquad z(a)=z.    \tag{1.7}
\]

Parallel physical alignments are distinct columns even when their head and
owner orbits agree.  The complete predecessor list of `a` is the punctured
facet star

\[
 {\cal P}(a)=
 \{(H_g\setminus\{\beta\},z):
       \beta\in H_g\setminus\{\gamma_g\}\}.               \tag{1.8}
\]

It has exactly six members.  Thus the complete host has `720,720` aligned
columns and `4,324,320` flag--column predecessor incidences.

For the opened reset (0.1), put

\[
 \begin{aligned}
 P'&={\cal R}\setminus\{T_0,\ldots,T_6\},\\
 Q'&={\cal R}\setminus\{T_1,\ldots,T_7\},\\
 O'&={\cal O}\setminus\{U_0,\ldots,U_6\}.
 \end{aligned}                                             \tag{1.9}
\]

Each set has size `1423`.  Restrict (1.8) to unused tail roots:

\[
 {\cal P}^{\cal S}(a)=
 \{f\in{\cal P}(a):r(f)\in P'\}.                           \tag{1.10}
\]

The residual head set contains the incoming socket `T_0`, and the residual
tail set contains the outgoing socket `T_7`.  The seven internal turns stay
fixed.  The residual model neither prescribes nor forbids choosing the
omitted seam again; excluding a closed reset component is a later
opening/topology row.

## 2. Compact flag and functional-attachment master

Use `x_f in {0,1}` for every flag option.  The root and high-target rows are

\[
 \sum_{f:r(f)=R}x_f=1\qquad(R\in{\cal R}),                  \tag{2.1}
\]

\[
 \sum_{f:P(f)=P}x_f\ge1,
 \qquad
 \sum_{f:T(f)=T}x_f\ge1                                   \tag{2.2}
\]

for every required rank-seven and rank-six target orbit.  Coverage, rather
than an offer bijection, is exact here: a provider can subsequently be
marked separately for each named target.  Write the literal reset flag as

\[
 f_a^{\rm lit}=(T_a;X_a,X_{a+1})
\]

and tail-normalize it by its second deletion:

\[
 \bar f_a=(S_a,z_a),\qquad
 S_a=\tau^{-X_{a+1}}
       (T_a\setminus\{X_a,X_{a+1}\}),\qquad
 z_a=X_a-X_{a+1}\pmod {17}.                               \tag{2.3a}
\]

Fix the eight normalized reset options by

\[
                         x_{\bar f_a}=1\qquad(0\le a<8).    \tag{2.3}
\]

Let `X_reset` be the exact authenticated reset-compatible selector face,
intersected with (2.1)--(2.3).  All of its quotient containment, coherent
phase, rail, and protected-reset equations are retained unchanged.  The
Benders theorem below adds the functional chronology gate to that frozen
face; it does not relax any selector row.

Let `A_S` be the aligned columns with head in `Q'` and owner in `O'`.  Use
`u_a in {0,1}` and impose

\[
 \sum_{a:g(a)=g}u_a=x_g
       \qquad(g\in{\cal F},\ r(g)\in Q'),                   \tag{2.4}
\]

\[
 \sum_{a:q(a)=q}u_a=1\qquad(q\in Q'),
 \qquad
 \sum_{a:o(a)=O}u_a=1\qquad(O\in O').                     \tag{2.5}
\]

The first equality couples the selected head flag to its physical owner
column.  The other two select a perfect matching of residual head and owner
resources.  Define

\[
 \theta_{qO}=\sum_{a:q(a)=q,\ o(a)=O}u_a.                  \tag{2.6}
\]

Then `theta` is a binary containment bijection `Q' -> O'`.  Together with
the seven fixed reset columns it is a full functional root--owner matching.
The selected `u_a` also retains the physical alignment `z(a)`, information
which the orbit map `theta` alone would lose.

Equations (2.1)--(2.6) are the non-TU master.  They choose the flags and the
functional owner attachment together; no predecessor edge has yet been
selected.

## 3. Exact predecessor logic and the recourse matching

For every compatible pair `f in P^S(a)`, introduce the binary conjunction

\[
                         c_{fa}=x_f\wedge u_a.               \tag{3.1}
\]

Its exact binary linearization is

\[
 c_{fa}\le x_f,\qquad c_{fa}\le u_a,
 \qquad c_{fa}\ge x_f+u_a-1.                              \tag{3.2}
\]

For `p in P'`, `q in Q'`, define the active predecessor incidence

\[
 e_{pq}=\bigvee_{\substack{a:q(a)=q\\
                 f\in{\cal P}^{\cal S}(a),\ r(f)=p}}c_{fa}. \tag{3.3}
\]

Every OR is imposed in both directions.  At an integral master point,
`e_pq=1` exactly when the selected flag at `p` is one of the six legal
punctured facets of the selected aligned column at `q`.

All `c_fa`, `e_pq`, and lazily introduced `v_aX`, `w_aX`, `n_qX` variables
are binary.  Only the recourse-flow variables below may remain continuous.

If retained explicitly, predecessor variables `pi_pq` satisfy

\[
 0\le\pi_{pq}\le e_{pq},\qquad
 \sum_q\pi_{pq}=1\ (p\in P'),
 \qquad
 \sum_p\pi_{pq}=1\ (q\in Q').                            \tag{3.4}
\]

The variables `pi` may remain continuous: for fixed binary `e`, the
bipartite matching matrix is totally unimodular and every feasible instance
has an integral extreme point.

### Theorem 3.1 (exact opened-reset compact master)

Equations (2.1)--(3.4), together with `x in X_reset`, are feasible if and
only if the encoded depth-three flag table has an owner-exact literal
directed cycle cover containing all seven opened-reset turns.

#### Proof

The normalized flag and turn theorems make (1.8) the complete literal
predecessor list of every aligned column.  Equations (2.1)--(2.3) choose the
flag table and preserve the reset and encoded target gate.  Equations
(2.4)--(2.6) use every residual head and owner once.  Equations (3.1)--(3.3)
activate exactly the compatible selected tail flags, and (3.4) uses every
residual tail and head once.  Adding the seven protected triples therefore
uses every tail, head, and owner once.

Conversely, remove the seven protected turns from any encoded owner-exact
cycle cover.  Its residual head columns give `u`, and its actual predecessor
turns give `pi`; the normal form forces (3.1)--(3.4).  \(\square\)

This is exactly the three-matroid common-base theorem in extended form.
Fixing `u`, hence the aligned functional attachment, saturates the head and
owner partition matroids and leaves the one transversal matching (3.4).

## 4. Proof-safe Hall/Benders separation

The `pi` variables can be eliminated without freezing flag-dependent edge
coefficients.  For a fixed root shore `X subseteq P'`, define

\[
 v_{aX}=\bigvee_{\substack{f\in{\cal P}^{\cal S}(a)\\r(f)\in X}}x_f,
 \qquad
 w_{aX}=u_a\wedge v_{aX},                                  \tag{4.1}
\]

and

\[
 n_{qX}=\bigvee_{a:q(a)=q}w_{aX}.                           \tag{4.2}
\]

Use the ordinary exact OR/AND linearizations.  Thus `n_qX=1` if and only if
the selected aligned column at head `q` has a selected legal predecessor
whose root lies in `X`.

If `C` denotes the residual predecessor matching value, its exact Hall
hypograph is

\[
 \boxed{
 C+|X|-\sum_{q\in Q'}n_{qX}\le1423
                  \qquad(X\subseteq P').}                   \tag{4.3}
\]

For fixed `(x,u)`, maximizing `C` subject to (4.3) gives the exact matching
value.  For the completion decision, simply fix `C=1423`; an arbitrary
smaller feasible `C` is only a lower target, not the matching value itself.

In particular a complete residual matching exists exactly when

\[
 \boxed{
 \sum_{q\in Q'}n_{qX}\ge|X|
                  \qquad(X\subseteq P').}                   \tag{4.4}
\]

### Theorem 4.1 (exact min-cut separator)

For an integral master incumbent `(x,u)`, construct

```text
source -> residual tail p     capacity 1
tail p -> residual head q     capacity 1424 when e_pq=1
residual head q -> sink       capacity 1.
```

The minimum cut equals the maximum matching of the incumbent predecessor
graph.  If it is below `1423`, its source-side tail set `X` violates (4.4),
and (4.1)--(4.4) give a globally valid symbolic Benders row.

#### Proof

Capacity `1424` is larger than the all-tail cut of value `1423`, so a
minimum cut crosses no tail--head arc.  If its source-side tails are `X`,
closure puts precisely `N(X)` on the source-side head shore.  Its value is

\[
                    1423-|X|+|N(X)|.                        \tag{4.5}
\]

Minimizing (4.5) is the vertex-cover form of bipartite matching, hence gives
the maximum matching value.  Equations (4.1)--(4.2) equal the neighbourhood
indicator for every future integral master point, so the returned row is
globally valid.  \(\square\)

A row of the form

\[
 \sum_{q,a}1[{\cal P}_{F^0}^{\cal S}(a)\cap X\ne\varnothing]u_a
 \ge|X|                                                     \tag{4.6}
\]

with the incumbent flag table `F0` baked into its coefficients is valid only
after fixing `F=F0`.  It is **not** a valid co-design cut.  The symbolic
legality variables in (4.1) are essential.

## 5. Alignment flux and exact punctured-containment blocks

Every predecessor in (1.8) has the same alignment label as its column.
Define selected tail and head label bits

\[
 L_{pz}=\sum_{\substack{f:r(f)=p\\z(f)=z}}x_f,
 \qquad
 R_{qz}=\sum_{\substack{a:q(a)=q\\z(a)=z}}u_a.             \tag{5.1}
\]

An exact completion necessarily satisfies

\[
 \sum_{p\in P'}L_{pz}=\sum_{q\in Q'}R_{qz}
       \qquad(z\in\mathbb Z_{17}\setminus\{0\}).          \tag{5.2}
\]

For a root set `X`, define `n_qXz` as in (4.1)--(4.2), but retain only
columns and predecessor options with label `z`.  The sharp block cuts are

\[
 \boxed{
 \sum_{q\in Q'}n_{qXz}
     \ge\sum_{p\in X}L_{pz}
 \quad(X\subseteq P',\ z\ne0).}                            \tag{5.3}
\]

At an integral incumbent, take the selected tail block

\[
 L_z=\{(S,z):x_{S,z}=1,\ r(S,z)\in P'\}                    \tag{5.4}
\]

and selected head block

\[
 R_z=\{g:u_{(g,z)}=1,\ r(g)\in Q'\}.                       \tag{5.5}
\]

Then (5.3) is equivalently the punctured-containment family

\[
 \left|
 \{(H_g\setminus\{\beta\},z)\in L_z:
       g\in Y,\ \beta\in H_g\setminus\{\gamma_g\}\}
 \right|\ge|Y|
       \qquad(Y\subseteq R_z).                              \tag{5.6}
\]

### Theorem 5.1 (exact block separation)

Subject to the label balances (5.2), the full Hall family (4.4) is
equivalent to the sixteen block families (5.3), or equivalently (5.6).
Each family is separated by one bipartite max flow; their disjoint union is
the network of Theorem 4.1.

#### Proof

Every active predecessor edge preserves `z`, so the graph is a disjoint
union of its `z`-blocks.  A disjoint union has a perfect matching exactly
when every equal-shore block has one.  Hall in each block is (5.3)/(5.6).
\(\square\)

There is an additional exact projection if the master first selects only a
head flag and owner orbit.  Let

\[
 a_{gO}=\sum_{a:g(a)=g,\ o(a)=O}u_a,
 \qquad
 Z(g,O)=\{z:(g,z)\text{ is an aligned column of }O\},       \tag{5.7}
\]

and `ell_z=sum_p L_pz`.  A physical alignment with this histogram exists if
and only if

\[
 \boxed{
 \sum_{g,O:Z(g,O)\subseteq A}a_{gO}
       \le\sum_{z\in A}\ell_z
 \qquad(A\subseteq\mathbb Z_{17}\setminus\{0\}).}         \tag{5.8}
\]

These `2^16` alignment-flux cuts are exactly separable by capacitated flow.
They assign labels only.  They neither imply nor replace the punctured-facet
Hall cuts (5.3).

## 6. Exact cut-crossing circuit support

Circuit support is meaningful only relative to a complete integral master
incumbent.  Let `B_kept` denote the symbolic Benders rows already retained
by the current master, excluding the row being crossed if it is not yet
present.  Fix

\[
                         (x^0,u^0)                           \tag{6.1}
\]

satisfying `x^0 in X_reset`, (2.1)--(2.6), the label balances (5.2), and
every row in `B_kept`, and let `X` be a deficient shore returned by
Theorem 4.1.  Put

\[
                         h_X^0=|N_{B(x^0,u^0)}(X)|.          \tag{6.2}
\]

For another integral master point, define flag and aligned-column change
bits

\[
 d_R^F=1-x_{f_R^0},
 \qquad
 d_R^A=1-u_{a_R^0}\quad(R\in Q'),                          \tag{6.3}
\]

where `f_R^0` and `a_R^0` are the incumbent choices.  Set `d_R^A=0` outside
`Q'`, and use one joint root-support bit

\[
 s_R\in\{0,1\},\qquad
 s_R\ge d_R^F,\qquad s_R\ge d_R^A,
 \qquad s_R\le d_R^F+d_R^A.                               \tag{6.4}
\]

The eight reset flags are fixed, so `d_R^F=0` for
`R in {T_0,...,T_7}`.  Their attachment status is different: `T_1,...,T_7`
are outside `Q'`, while `T_0` is the residual incoming socket and its
column-change bit `d_{T_0}^A` remains allowed and counted.  Record also

\[
 \sigma_F=\sum_Rd_R^F,qquad
 \sigma_A=\sum_Rd_R^A,qquad
 \sigma=\sum_Rs_R.                                        \tag{6.5}
\]

A **cut-crossing master exchange** (called a circuit below) means a
support-minimal feasible opened-reset master difference whose final
neighbourhood gains a net distinct head on `X`.  It is not asserted to be a
circuit of the raw constraint matrix.  Its exact support is the following.

\[
 \boxed{
 \sigma_X^{\rm cross}=
 \min\left\{
   \sum_Rs_R:
   x\in{\cal X}_{\rm reset},\quad
   (x,u)\text{ satisfies (2.1)--(2.6) and (5.2)},\quad
   (x,u)\in{\cal B}_{\rm kept},\quad
   \sum_{q\in Q'}n_{qX}\ge h_X^0+1
 \right\}.}                                               \tag{6.6}
\]

All `n_qX` in (6.6) use the symbolic logic (4.1)--(4.2).  To close the
entire returned Hall violation, replace `h_X^0+1` by `|X|`.  To certify a
complete chronology, retain every Benders row (4.4), not merely the one
shore in (6.6).  Including (5.2) prevents a nominal phase switch from
crossing one cut by merely moving an unmatched unit of alignment flux to the
wrong label block.

Thus (6.6) is a local Benders-repair minimum scoped to the declared cut pool
`B_kept`.  Taking `B_kept` to contain every other Hall row gives the
intrinsic full-master version; the returned exchange still becomes a
chronology only when the crossed row is closed as well.

### Theorem 6.1 (smallest-support structural boundary)

For every frozen incumbent and shore:

1. if (6.6) is feasible, `sigma_X^cross >= 1`;
2. `sigma_X^cross=1` if and only if one root support admits a
   master-feasible coupled flag/column substitution, keeping every other
   root choice fixed, whose signed neighbourhood change on `X` is positive;
3. in such a support-one change, the head root and owner orbit stay fixed,
   while the tail-flag label delta and aligned-column label delta are equal
   so that (5.2) survives; and
4. if no support-one substitution exists, every nonparallel `theta` circuit
   has support at least two.  Equality requires a feasible alternating
   four-cycle on two heads and two owners, together with any flag changes on
   those same two root supports, and positive net cut gain.

Here “master-feasible” means satisfying every row displayed in (6.6),
including the alignment balances and `B_kept`.

#### Proof

Zero support leaves `x,u`, hence every `n_qX`, unchanged.  This proves the
first assertion and reduces equality to the explicit one-root test in the
second.

Changing the owner of only one head in a bijection makes its old owner
unused and its new owner repeated.  Therefore a one-head attachment change
must keep the owner.  Since only one root support changes, (5.2) further
forces the change in the tail-label histogram to equal the change in the
head-column histogram.  In the normalized `k=17` column host a nontrivial
support-one move is consequently a coupled flag/column substitution at the
same root; a pure phase change with `x` fixed moves flux between blocks and
is infeasible.  Conversely, any such coupled substitution satisfying every
row of (6.6) and giving positive signed neighbourhood change is a feasible
support-one cut-crossing exchange.

The symmetric difference of two distinct head--owner perfect matchings is a
disjoint union of alternating even cycles.  A nonparallel component has at
least two heads and two owners, giving the four-cycle lower bound.  Its
columns and any coupled flag changes must satisfy every row of (6.6),
including (5.2) and `B_kept`, which is exactly the stated equality
condition.  \(\square\)

The theorem deliberately does not freeze a predecessor matching while
changing `theta`.  For a fixed literal turn `p -> q`, its owner is uniquely
`p union q`; a genuine owner reassignment must reroute predecessor edges at
the same time.  The full min-cut recourse must therefore be recomputed after
every circuit.

### Corollary 6.2 (what is and is not a numerical minimum)

The two frozen inputs supply no exclusion of the conditional one-root case
in Theorem 6.1.  This note therefore claims only the universal lower bound
one, not an unconditional support-two or support-three bound.  The universal
lower bound for a **nonparallel owner-map** circuit is two, and it is attained
exactly when a feasible cut-crossing alternating four-cycle exists.  The
actual reset-conditioned cut-crossing minimum is the incumbent-dependent
number (6.6).

The earlier ae88 support-three theorem concerns a different common-live
projection and supplies no bound for (6.6).

### Theorem 6.3 (audited full-completion support lower bound)

Let `F_ind` be the opened-reset flag table whose residual uncoloured
predecessor graph `G_ind` has matching number `850`.  Let another flag table
`F` differ from it on the root set `S`, and let `theta` be any aligned
functional attachment for `F`.  Then

\[
 \boxed{
 \nu(B_\theta(F))
 \le 850+|S\cap P'|+|S\cap Q'|
 \le 850+2|S|.}                                           \tag{6.7}
\]

Consequently every functional completion of size `1423` obtained from
`F_ind` has

\[
                         |S|\ge
 \left\lceil{1423-850\over2}\right\rceil=287.             \tag{6.8}
\]

#### Proof

Let `G(F)` be the uncoloured legal predecessor graph of the new flag table.
Every functional graph `B_theta(F)` is a subgraph of `G(F)`.  Take any
matching in `G(F)` and delete its edges incident with a changed tail root in
\(S\cap P'\) or a changed head root in \(S\cap Q'\).  At most the sum of
those two cardinalities is deleted.  Every remaining edge joins two unchanged
flags, hence belongs to `G_ind`, where at most `850` such edges can remain.
This proves (6.7), and (6.8) follows.  \(\square\)

The bound concerns full rank recovery from the particular audited table.
It neither supplies a support-287 witness nor determines the one-cut value
(6.6): one changed flag can alter many neighbours of a fixed shore even
though it raises total matching rank by at most two.

## 7. Why no finite support calibration is frozen here

The authenticated reset audit is

```text
scratch/audit_k17_necklace_selector_reset_bank_20260801.cpp
SHA256 7b974c89c0c87a3e34182080c02c2c7aae66b8b5318bda3d30fed0188b35ad24

scratch/audit_k17_necklace_selector_reset_bank_20260801.txt
SHA256 012f211a76ebeacacca19089a8d8e5d4c03754b51f7818e5c04beebe2b2c2ab8
```

It proves

```text
opened reset owner attachment extension       1423 / 1423
opened reset uncoloured state matching          850 / 1423
universally dead tails                                  406
```

The owner extension and state matching are separate computations.  The
audit does not output a common aligned attachment `u^0`, a functional graph
`B_theta`, or a canonical deficient shore `X`.  Thus it does not supply the
input pair (6.1)--(6.2).  Running a support census would first require
choosing a new `theta`, its parallel phases, and a support metric; different
choices can have different values of (6.6).

For the fixed audited flag table, every functional graph `B_theta` is a
subgraph of that uncoloured legal-turn graph.  Hence `850` is an upper bound
for every such `B_theta`, not a calibration of any one functional
attachment.

Accordingly no H100 job was launched.  A future finite calibration is
proof-safe only after freezing, with hashes:

1. the reset-compatible incumbent flag option at every root;
2. the aligned functional attachment column at every residual head;
3. the exact incumbent predecessor graph and returned Hall shore;
4. whether support counts flags, aligned columns, or their root union as in
   (6.5); and
5. complete support-`s` rejection transcripts or a checked SAT proof for
   every `s` below the first witness.

## 8. Exact scope

The theorem closes the quotient `d=3` normal form, opened-reset resource
contraction, joint flag/aligned-owner master, functional `theta`, exact
alignment flux, exact punctured-containment Hall separation, and the
parametric circuit-support decision problem.

It does not prove that the master is feasible at `C=1423`.  A feasible point
would give an owner-exact quotient directed cycle cover containing the seven
reset turns, possibly with many components and zero voltage.  The only
`q1/q2` information encoded is the depth-three `P/T` target coverage and the
reset colours identified in the input theorem.  No conclusion is made about
connected topology, nonzero voltage, any additional `q2` or upper rows,
residence outside the reset, a global opening argument, or compiler
correctness.
