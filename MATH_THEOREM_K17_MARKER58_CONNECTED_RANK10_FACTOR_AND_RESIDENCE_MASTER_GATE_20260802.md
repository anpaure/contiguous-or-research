# `k=17`: connected marker58 rank-ten factor and the exact residence master gate

Date: 2026-08-02  
Status: independently replayed finite theorem and exact negative residence
certificate.  The first-58/open-3 protected marker bank has a connected
`Z_17`-equivariant rank-eight-rainbow, rank-nine-degree-two factor covering
every rank-ten cap.  That particular factor is not a depth-three resident
host under any opening cut, so its compiler is deliberately not evaluated.

## 1. Frozen inputs and interpretation

The quotient instance is bound to

```text
88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403
  k17_marker_orbit.witness.tsv
7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3
  marker58_upper_q1_quotient.map.tsv
9bde5d02f17025fd354259c941174e70bece6a2f321b93495c27ea50782e08a8
  marker58_upper_q1_quotient.cnf
```

The promoted sparse primary witness and its literal development are

```text
70f48c248ab7e8fb7d08895048fcf7d5b27fca5ff6f389832e5c4f35cf25adb6
  c68b.double_fusion.model
7d39e3aee641521df2d441d0342a2bd060dafb05cc7f5703ef206f53b6d21e3c
  c68b.double_fusion.factor.tsv
85ae3d42671eea04fb016988b9095cb79fd20217ea6eec02d480910403bfe31b
  c68b.double_fusion.audit.json
```

The model contains exactly 1,198 positive primary identifiers.  It is not a
complete 204,167-variable DIMACS assignment and has no DRAT claim.  The
theorem below follows from direct resource reconstruction, not from the word
`SATISFIABLE` in the sparse file.

## 2. Exact quotient equations

There are 1,430 rank-eight facet orbits, 1,430 rank-nine owner orbits and
1,144 rank-ten cap orbits.  The 58 base modules opened at native edge 3 give
232 fixed protected edge orbits.  For every residual option `e`, write
`f(e)` for its facet orbit, `a(e),b(e)` for its owner orbits, and `u(e)` for
its cap orbit.  A quotient loop has `a(e)=b(e)` and contributes two to that
owner degree.  With `r_o=2-d_fixed(o)`, the exact primary system is

\[
 \sum_{e:f(e)=f}x_e=1,                                      \tag{2.1}
\]

\[
 \sum_e\bigl(1_{a(e)=o}+1_{b(e)=o}\bigr)x_e\le r_o,        \tag{2.2}
\]

\[
 \sum_{e:u(e)=u}x_e\ge1                                   \tag{2.3}
\]

for every residual facet, owner and not-already-protected cap orbit.  The
endpoint ledger has total capacity `2*1198`, so (2.2) is automatically tight
when all 1,198 facet choices are made.

An independent O3 C++ audit reconstructs the complete option catalogue and
all sequential-counter clauses.  It byte-matches the frozen map and no-cut
CNF and reports

```text
fixed=232  primary=35713  auxiliary=168454
variables=204167  clauses=439145  same-owner-options=8
```

This static replay is separate from the sparse-witness semantic replay.

## 3. Connected factor theorem

### Theorem 3.1

The frozen `double_fusion` selection, together with the 232 protected edge
orbits, develops to one simple cycle on all 24,310 rank-nine owners.  It uses
every rank-eight facet exactly once, contains all 3,944 protected edges of
the 986 developed first-58/open-3 paths, and covers every one of the 19,448
rank-ten caps.

### Proof

The independent decoder reconstructs every fixed protected row from the
marker witness and every selected option from the full map.  It verifies
exactly one edge at each of the 1,430 quotient facet orbits, degree two at
each of the 1,430 quotient owner orbits, and positive load at all 1,144 cap
orbits.  Developing each row through all 17 rotations gives 24,310 literal
edges.  A second physical ledger verifies every rank-eight mask once, every
rank-nine mask at degree two, every rank-ten mask at positive load, and the
exact protected set.

The quotient graph is one 1,430-edge cycle.  In the frozen fibre convention
its signed voltage is

\[
                              4\pmod {17}.                    \tag{3.1}
\]

The regular lift of a quotient cycle of voltage `v` has
`gcd(17,v)` components.  Since `gcd(17,4)=1`, this predicts one physical
cycle of length `1430*17=24310`.  A literal BFS on the developed factor
independently returns one component.  This proves the claim.  `square`

The independent output is byte-identical to the promoted factor and audit:

```text
PASS_CONNECTED_NONZERO_VOLTAGE
quotient_components=1 physical_components=1 voltage=4
```

The search/fusion history is not used in this proof and was not rerun.

## 4. Exact residence no-go for this factor

For depth `d=3`, an internal positive coordinate run must have length at
least `d+1=4`.  The independent residence audit reconstructs the unique
physical owner-cycle order from the factor and obtains the cyclic short-run
census

\[
  N_1=0,\qquad N_2=2873,\qquad N_3=2499,\qquad
  N_{<4}=5372.                                               \tag{4.1}
\]

It then tests all 24,310 possible opening edges.  A cut may turn only the
short runs meeting that boundary into clipped boundary runs.  No cut is
legal.  The best value is attained first at cut 46 and leaves

\[
                              5369                           \tag{4.2}
\]

short internal runs.  The complete all-cut histogram is

```text
5369:272  5370:3417  5371:10965  5372:9656.
```

At cut 46, the canonical maximal depth-three antecedent envelope has 24,313
slots, no empty envelope, and rank histogram

```text
rank6:21435  rank7:2874  rank8:2  rank9:2.
```

It restores only 12,670 of the 24,310 owner rows.  Thus the exact maximal
erosion mismatch is

\[
                         24310-12670=11640.                   \tag{4.3}
\]

Consequently `maximal_erosion_exact=false`.  The lower/compiler graph is
correctly skipped with status `SKIPPED_NONRESIDENT` and matching value `-1`.
This is a fail-closed skip, not evidence about compiler feasibility.

### Corollary 4.1

No operation which leaves this factor order fixed and merely chooses a cut,
source labelling or terminal compiler can turn it into a depth-three
resident host.  Residence must be imposed while selecting or changing the
factor.

## 5. Proof-safe integrated master

The next common-master gate is therefore factor selection, orientation,
opening and residence together.  Let `x_e` select physical Johnson edges
(or their tied `Z_17` orbits), and let `y_(A,B)` orient a selected edge from
owner `A` to owner `B`.  The resource rows are (2.1)--(2.3), the protected
rows are fixed to one, and

\[
 y_{A,B}+y_{B,A}=x_{\{A,B\}},\qquad
 \sum_B y_{A,B}=\sum_B y_{B,A}=1.                            \tag{5.1}
\]

Connectivity is separated exactly by the directed subtour cuts

\[
 \sum_{A\in S,\ B\notin S}y_{A,B}\ge1
       \qquad(\varnothing\ne S\subsetneq V).                \tag{5.2}
\]

In the equivariant subclass, a connected quotient selection must additionally
have nonzero voltage.  A zero-voltage incumbent may be rejected by its exact
primary no-good, or voltage may be carried explicitly as a finite state.

Choose one selected directed edge as the opening seam with variables
`h_(A,B)<=y_(A,B)` and `sum h=1`.  For each coordinate `j`, use residence
states `q in {0,1,2,3,4}`.  State 0 means the current owner omits `j`; states
1, 2 and 3 are the exact terminal positive-run ages; state 4 means age at
least four.  On every nonseam selected arc the deterministic transition is

```text
bit 1: 0->1, 1->2, 2->3, 3->4, 4->4
bit 0: 0->0, 4->0
```

and all other transitions are forbidden.  Standard arc-state
linearizations make this a finite exact formulation.  The seam transition
is replaced by the explicitly allowed left/right collar signature; it may
not be treated as an untyped free edge.

Equivalently, this state system has an exact lazy separator.  If the current
cycle contains a forbidden `0,1^ell,0` window `P` with `1<=ell<=3`, then

\[
 \sum_{a\in P}y_a-\sum_{a\in P}h_a\le |P|-1               \tag{5.3}
\]

is valid: either at least one window arc changes or the unique seam cuts the
window.  The present incumbent supplies 5,372 such physical rows, in 316
`Z_17` orbits.  The all-cut audit is a literal separation certificate that
no assignment of the existing `h` variables can satisfy them.

On the tied quotient-primary face, let `supp(P)` be the set of option
variables supporting the physical window and let `B(P)` be its internal and
two flanking physical edges.  With physical opening variables `o_g`, the
same exact row is

\[
 \sum_{e\in\operatorname{supp}(P)}x_e
 \le |\operatorname{supp}(P)|-1+\sum_{g\in B(P)}o_g.        \tag{5.4}
\]

Removing the opening term gives the strict-cyclic sufficient face.  Equal
quotient supports may collapse rows, so the current 316 violated run orbits
give at most 316 distinct primary clauses; every later incumbent must be
decoded and separated again.

## 6. Source and compiler incidence after residence

Source placement must use a joint atlas option, not independent rolewise
mask matches.  For each developed marker module `m`, let `A_m` be the set of
literal five-state atlas placements that simultaneously specify its
primitive state, labelled source/buffer occurrences, ordered factor
positions, boundary ages, fixed-root incidence and protected resources.  Use

\[
 \sum_{a\in A_m}z_{m,a}=1                                  \tag{6.1}
\]

and condition each `z_(m,a)` on every required `y`, seam/collar state and
named-resource capacity.  This is the missing occurrence-position bridge;
the protected factor edges alone do not provide it.
All forbidden joint tuples must be excluded explicitly; absent a
rectangularity theorem, no collection of independent rolewise Hall rows is
equivalent to (6.1).

This is the interface retained in
`MATH_AUDIT_R2_K17_MARKER_RESERVOIR_REBASE_20260802.md`: module and buffer
occurrences must acquire immutable host positions before any downstream
catalogue can be transported.  The exact token-capacity and forbidden-tuple
form is Theorem 2.1 of
`MATH_THEOREM_H3_K17_MARKER58_FIVE_STATE_SOURCE_ATLAS_AND_UNBUFFERED_PH_FUSION_GATE_20260802.md`.

After a resident opening has been chosen, let `T_i` be its ordered owner
rows and put

\[
 E_p=\bigcap_{i:\ p\in[i,i+3]}T_i.                         \tag{6.2}
\]

The flat depth-three face requires every `E_p` to be nonempty and

\[
                       T_i=E_i\cup E_{i+1}\cup E_{i+2}\cup E_{i+3}. \tag{6.3}
\]

Only after this literal maximal-envelope replay passes may a lower/compiler
subproblem be materialized.

For a fixed resident master `(x,y,h,z)`, construct the complete live
occurrence-labelled compiler graph `G^+` in one orientation.  Its edges must
encode the joint lower/root/head/graphic predicate, including the fixed
predecessor relation

\[
 M_0(\psi(R)\cap\phi(R))=\psi(R),                            \tag{6.4}
\]

not merely the disjoint second-facet projection.  A functional compiler
exists exactly when `G^+` has a matching saturating all demand rows.  The
max-flow separator returns a deficient shore `X` with

\[
                         |\Gamma^+(X)|<|X|.                  \tag{6.5}
\]

This is the proof-safe Benders interface.  Every provider incidence used in
the cut must be conditioned on a complete surviving atlas state; a unary
socket supported only by a counterpart that is simultaneously removed is
not live.  A cut may be written with exact incidence-availability variables
`lambda_(d,p)` and their shore OR variables `w_(X,p)` as

\[
 w_{X,p}\ge\lambda_{d,p}\quad(d\in X),\qquad
 w_{X,p}\le\sum_{d\in X}\lambda_{d,p}.                     \tag{6.6}
\]

For a demand shore `Q`, cloned occurrence cells `C`, and requested matching
cardinality `M`, max-flow/min-cut gives the exact maximum-closure rows

\[
 M+|X|-\sum_{c\in C}w_{X,c}\le |Q|
       \qquad(X\subseteq Q).                               \tag{6.7}
\]

Indeed the maximum matching value is

\[
 |Q|-\max_{X\subseteq Q}\bigl(|X|-|\Gamma^+(X)|\bigr).      \tag{6.8}
\]

For binary variables (6.6) is exactly
`w_(X,c)=OR_(d in X) lambda_(d,c)`.  When `|Q|=M=1430`,
(6.7) is the synchronized Hall row
`1430+|X|-|Gamma^+(X)|<=1430`.  Thus the separator is exact rather than a
marginal projection.  This is the live occurrence-cell specialization of
Theorem 3.1 and the min-cut separator in Section 4 of
`MATH_THEOREM_R2_K17_AE88_SYNCHRONIZED_COMMON_MASTER_20260801.md`.

Hall feasibility is still only the functional incidence layer.  For a
selected compiler matching `theta`, replay the literal maximal caps

\[
 A_p=E_p\cap
 \bigcap_{(S,c):\ \theta_{S,c}=1,\ p\in c}S,                \tag{6.9}
\]

and require nonempty `A_p`, exact `D^3A=T`, the protected/module rows and
selected-cell equality.  A failed minimal tuple becomes an exact guarded
core row in the master.  It may not be hidden inside a marginal provider
count.  This replay is equation (7.4) of
`MATH_AUDIT_L_AGE_COMPOSITION_AND_TERMINAL_COMPILER_SCOPE_20260801.md`;
the flat individual incidence predicate is equations (1.3)--(1.6) of
`MATH_THEOREM_INDEPENDENT_COATOM_TENSOR_DMAC_PROFILE_AND_PREFIX_COMPILER_20260801.md`.

Global
reversal requires only this one oriented matching: the complete certificate
is reflected with the chronology.  No fixed-address intersection
`G^+ intersect G^-` is required, by
`MATH_THEOREM_GLOBAL_REVERSAL_QUOTIENT_INDUCTION_AND_RELATIVE_PHASE_OBSTRUCTION_20260801.md`.

For the present `double_fusion` factor, Sections 4--5 reject the master
before (6.1)--(6.9); no source or compiler verdict is inferred.

## 7. Scope and frozen audit package

The theorem closes, for the frozen first-58/open-3 bank, exactly:

* protected-path containment;
* the complete rank-eight q1 palette;
* degree two and one connected cycle on every rank-nine owner;
* complete rank-ten cap coverage; and
* nonzero quotient voltage and literal one-component development.

It does not close source/buffer occurrence binding, residence, maximal
depth-three erosion, ranks 11--17, exterior cross-windows, the rooted
lower/head/graphic compiler, common cap, regeneration or a universal word.

The self-contained replay package is

```text
scratch/r2_k17_marker58_upper_q1_double_fusion_replay_20260802/
```

Its `FROZEN_SHA256SUMS` has SHA-256

```text
1f91e656c6574b367169b6572ea17522aed48d997699e4c3f6f3bc8bbe1750a4
```

and passes `sha256sum -c`.  The independent H100 replay root is

```text
/home/amodo/or15/work/r2_k17_marker58_upper_q1_replay_20260802
```

Both semantic decoders were compiled with `g++ -O3 -std=c++20 -DNDEBUG`
and produced byte-identical factor, topology, residence and all-cut audit
artifacts.  No fusion search or pricing loop was launched by this audit.
