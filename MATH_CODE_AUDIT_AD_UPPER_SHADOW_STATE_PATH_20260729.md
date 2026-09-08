# AD audit: upper compact shadow-state paths, exact scope, and an interval-flow replacement

Date: 2026-07-29

## 1. Scope and frozen source

This is an independent mathematical and line-level audit of the upper
`shadow-state-path` construction in

```text
scratch/graded_quotient_pipeline.py
```

The audit began from the membership-clause snapshot at
`2026-07-29T00:56:20+0500`, SHA-256

```text
ec0cc8e5f2b427d26b935cd890f207a9fd91f6c74d28b52b1c2afa525972d946.
```

During the audit the shared file was independently upgraded to the
distinct-defect encoding proved in Section 8.  That current audited snapshot
is `2026-07-29T01:02:08+0500`, SHA-256

```text
3ad43459b8661feaa1936fe081ae523d422ebe57395e8d5c4c8dc820edb329b8.
```

Unless explicitly described as the old membership version, line references
below refer to the latter snapshot.

No core file was edited, no solver was invoked, and no search was run.  The
only executable checks were syntax checking and direct enumeration of the
small state tables already defined by one target.

The decisive conclusion is:

* the implementation is an exact encoding of a **specified `q`-edge
  shadow witness** at every fixed `q`;
* for upper `q=2`, this is also equivalent to the arbitrary-length interval
  occurrence tested by `upper_missing`;
* for upper `q=3`, and in fact for every `q>=3`, that last equivalence is
  false as a local path statement.  The present q3 CEGAR constraint is a
  sufficient strengthening, not an exact feasibility cut.

Positive carrier certificates remain sound because the final physical
verifier is independent.  An UNSAT result obtained after installing upper-q3
minimal-window constraints would, however, apply only to the strengthened
model.

## 2. Setting

Let `k` be odd and put

\[
 r=(k+1)/2,\qquad W=\binom{k}{r}.
\]

The cyclic group `G=Z_k` rotates coordinates.  Central rank is free: if a
nonidentity rotation of order `e>1` fixed an `r`-set, its rank would be
divisible by `e`, whereas `gcd(k,r)=1`.

Let `y_a` be the selected directed quotient-arc variables.  The quotient
`AddCircuit` constraint and coprime total voltage make their physical lift
one directed cycle on all `W` central states.  For an upper target

\[
 T\in\binom{[k]}{r+q},
\]

write

\[
 V_T=\{X\in\tbinom{T}{r}\}.
\]

The code uses actual physical masks in `V_T`, not merely their central orbit
indices.

## 3. Exact local theorem at arbitrary fixed depth

### Theorem 3.1 (local state-path equivalence)

Fix `1<=q<=r-1`, a physical target `T` of rank `r+q`, and a selected
directed quotient carrier whose physical lift has one outgoing edge at each
central state.  The constraints constructed at lines 526--596 and
1256--1301 are feasible if and only if the selected physical lift contains
`q+1` consecutive states

\[
 X_0\to X_1\to\cdots\to X_q
\]

such that

\[
 X_i\subseteq T\quad(0\le i\le q),
 \qquad \bigcup_{i=0}^q X_i=T.
\]

The lower dual is also exact: for a rank-`r-q` target `S`, replace `V_T` by
the central supersets of `S` and replace union by intersection.

#### Proof

For upper mode, lines 559--562 enumerate exactly all members of `V_T`.
Lines 565--593 enumerate exactly the directed Johnson steps within `V_T`
whose directed quotient arc is present in the strict catalogue.  The table
constraint at lines 1280--1289 therefore says that each successive pair is
one such physical step.  The `Element` constraint at line 1292 says that
the corresponding quotient arc is selected.  Because the source mask of
one table row is literally the destination mask of the preceding row, the
steps concatenate physically; this is stronger than merely matching
quotient endpoints.

Every state lies in `T`.  In union mode the fourth table coordinate at
lines 585--593 is the physically inserted coordinate.  Lines 1293--1301
require the q insertion coordinates to be pairwise distinct members of the
initial hole set `T\X_0`.  That hole set has size q, so every initially
missing coordinate enters and the union is exactly `T`.  Conversely, a
q-edge full-union witness has only q insertions available for its q initial
holes, hence its insertion coordinates satisfy exactly these constraints.

The intersection proof is identical after reversing containment: all states
contain `S`, while every coordinate outside `S` is omitted by at least one
state.  QED.

### Exact sizes

Before quotient-self-loop transitions are removed, the generic table sizes
are

\[
 \begin{array}{c|c|c}
 &\text{states}&\text{directed transition rows}\\ \hline
 \text{lower depth }q&
 \binom{r-1+q}{q}&
 \binom{r-1+q}{q}\,q(r-1)\\
 \text{upper depth }q&
 \binom{r+q}{q}&
 \binom{r+q}{q}\,rq.
 \end{array}
\]

Thus the same implementation is mathematically valid for every fixed `q`;
its state count is polynomial in `k` of degree `q`.

## 4. Directed phase and cyclic-boundary audit

Let `rho` denote one coordinate rotation.  If

\[
 u=\rho^{s_u}\bar u,\qquad v=\rho^{s_v}\bar v
\]

with canonical central representatives `bar u,bar v`, normalizing the
physical edge `u->v` at its source gives

\[
 \bar u\longrightarrow \rho^{s_v-s_u}\bar v.
\]

This is exactly the shift stored at lines 255--275 and recomputed at
lines 311--323.  Since the central action is free, an oriented physical edge
has a unique directed orbit once its lower intersection and orientation are
fixed.  Consequently `directed_arc(u,v)` is invariant under simultaneous
rotation of `u,v` and identifies the correct quotient arc.

No extra phase variable is missing from the state-path table: each state
variable is an actual physical mask and therefore already fixes its phase.
When the quotient circuit crosses its last-to-first arc, the stored shift is
the phase update.  Coprime total voltage makes the lift one `W`-cycle, so a
state path may cross either the quotient boundary or the physical cyclic
boundary without a special case.

This audit checked directly, for all 680 retained transitions of the short
rank-ten target described in Section 7 and all 15 rotations of each
transition, that

```text
directed_arc(rho^s u,rho^s v) = directed_arc(u,v).
```

The transition triples were also all distinct.

## 5. Upper q=2 really is an exact CEGAR cut

The function `upper_missing` at lines 393--407 accepts an upper target if it
is the union of an interval of **any** length.  A priori Theorem 3.1 only
encodes a three-state interval when `q=2`.  At q2 these notions coincide.

### Theorem 5.1 (two-hole shortening)

Let

\[
 X_0,X_1,\ldots,X_L\in\binom{T}{r},\qquad |T|=r+2,
\]

be a Johnson path.  If `union_i X_i=T`, then some three consecutive states
have union `T`.

#### Proof

Put `H_i=T\X_i`.  Each `H_i` has size two and adjacent `H_i,H_{i+1}` differ
by one exchange, so their intersection is a singleton; call its element
`c_i`.  If every consecutive triple of the `X` path failed to cover `T`,
then every triple

\[
 H_i,H_{i+1},H_{i+2}
\]

would have nonempty intersection.  This is equivalent to `c_i=c_{i+1}`.
All the `c_i` would therefore be one common element of every `H_i`, contrary
to

\[
 \bigcap_iH_i=T\setminus\bigcup_iX_i=\varnothing.
\]

QED.

It follows that the union-mode q2 constraints installed at lines 1368--1371
and 1437--1440 are necessary as well as sufficient for the exact q2 target
tested by `upper_missing`.

## 6. Sharp local obstruction at every q>=3

The preceding shortening theorem stops sharply at q2.

### Theorem 6.1 (long interval with no minimal-depth window)

For every `q>=3` and every `r>=q+1`, there is a Johnson path

\[
 X_0,X_1,\ldots,X_{q+1}\in\binom{T}{r},
 \qquad |T|=r+q,
\]

whose full union is `T`, but no `q+1` consecutive states have union `T`.

#### Construction and proof

Choose pairwise distinct symbols

\[
 p,s,x,y,z,
 a_1,\ldots,a_{q-2},
 b_1,\ldots,b_{q-2}
\]

inside `T`; this uses `2q+1<=r+q` symbols.  Put

\[
 A=\{a_1,\ldots,a_{q-2}\},\qquad
 B=\{b_1,\ldots,b_{q-2}\}.
\]

Define q-element hole sets

\[
 H_0=\{p\}\cup A\cup\{x\},\qquad
 H_{q+1}=\{s\}\cup B\cup\{y\}.
\]

For `1<=j<=q`, let `H_j={p,s} union R_j`, where the `(q-2)`-sets
`R_j` form the exchange path

\[
 A,quad A-a_1+z,quad A-a_1+b_1,quad
 A-\{a_1,a_2\}+\{b_1,b_2\},\quad\ldots,\quad B.
\]

There are exactly q displayed bridge states: the detour through `z` supplies
the one transition beyond the `q-2` exchanges needed to turn `A` into `B`.
Every consecutive pair of hole sets differs by one exchange.  Set
`X_i=T\H_i`; these are adjacent r-sets.

The endpoint holes are disjoint, so `intersection_i H_i` is empty and the
full union of the `X_i` is `T`.  But the only two windows of `q+1` states are
indices `0,...,q` and `1,...,q+1`.  Their hole intersections contain `p`
and `s`, respectively.  Neither window covers `T`.  QED.

For q3 an explicit five-state hole path is

\[
 \{p,a,x\},\{p,s,a\},\{p,s,z\},\{p,s,b\},\{s,b,y\}.
\]

Its five-state complement path covers `T`; its first four complements miss
`p` and its last four miss `s`.

### Concrete strict-carrier counterexample at k=15

The obstruction occurs in the current residence-perfect strict k15 seed,
not only in an abstract Johnson path.  Reconstructing the physical cycle
from

```text
scratch/fixtures/k15_residence_hint_explicit_v1.json
```

gives, at cyclic position 102, the five consecutive central states

```text
30264, 29242, 29214, 29230, 23086.
```

Each consecutive pair is a rank-eight Johnson edge.  Their union is

```text
32318, rank 11, canonical representative 4031.
```

The two four-state subwindow unions are respectively

```text
30270, rank 10, canonical representative 4027;
31294, rank 10, canonical representative 4029.
```

An independent scan of this fixed 6435-cycle found no three-edge witness for
the target orbit 4031; its minimum witness length is four edges, attained at
exactly the 15 equivariant translates of the displayed interval.  The same
audit gives minimum length four, again with 15 translates, for rank-eleven
representatives 7675 and 12155.  Thus this valid strict carrier satisfies
the exact arbitrary-interval upper condition for those three target orbits
but violates their compact q3 minimal-window constraints.

### Consequence for the current code

The q3 table at lines 1256--1301 is locally exact, but lines 393--407 test
arbitrary interval length.  Therefore the q3 additions at lines 1368--1371
and 1437--1440 are not proved consequences of the intended upper-coverage
condition; the fixed k15 seed above proves that the two conditions genuinely
differ even inside the strict equivariant carrier class.  The q3 table may
be used as an explicitly declared search
strengthening, and any resulting positive carrier remains valid.  They may
not support an UNSAT claim for the unrestricted carrier problem.

The same qualification is required in
`MATH_LEMMA_COMPACT_Q3_STATE_PATH_20260729.md` where the upper dual is called
one common exact representation, and in item 1601 of
`MATHEMATICAL_HANDOFF.md`.  Those statements are correct for an exact
`q`-edge window, not for the arbitrary-length upper occurrence used by
`upper_missing`.

Until an exact variable-length constraint is installed, the complete CEGAR
fallback for a missing upper q3 target is the whole-selection no-good already
used for deeper upper targets.

## 7. Composite k=15 and the short upper target orbit

At `k=15,r=8`, rank ten has orbit profile

\[
 15^{200}+3^1.
\]

Indeed, the only nonfree masks have a length-three pattern of weight two
repeated five times; the three rotations form one orbit.  A representative
is

```text
T = 14043
  = {0,1,3,4,6,7,9,10,12,13}.
```

It is fixed by shifts `{0,3,6,9,12}` and has orbit size three.  Its compact
q2 table has exactly

```text
45 physical states,
720 directed Johnson transitions before strict self-loop omission,
680 retained transition rows.
```

The stabilizer acts freely on the 45 central states, giving nine state
orbits of size five.  The present implementation is correct: it enumerates
physical states, canonicalizes only the selected arc, and one witness for
`T` rotates to witnesses for all three physical targets.  Stabilizer copies
create harmless duplicate witnesses, not false target multiplicity.

A valid symmetry breaker is available: restrict the first state of a local
path to one representative from each stabilizer orbit.  Every witness has a
common stabilizer rotation satisfying that restriction, so this cuts the
rank-ten short-target start domain from 45 to 9 without losing a witness.
One must not quotient every later state independently, because independent
stabilizer phases can change the accumulated union.

Rank eleven has profile `15^91`, so there is no short upper-q3 target orbit.
Independent direct table enumeration gave these retained-row distributions:

```text
upper q2: 680^1, 702^4, 716^14, 718^16, 720^166;
upper q3: 3920^1, 3942^10, 3954^4, 3956^34, 3958^20, 3960^22.
```

For the current residence seed, the 27 missing rank-ten targets are all
full orbits and have row counts `720^21,716^4,718^2`.  Its one missing
rank-eleven target is representative 7807 and has 3958 rows.

## 8. The current smaller exact local encoding

The source changed during this audit from coordinate-membership auxiliaries
to the following distinct-defect implementation.  The replacement is
correct for local q-edge witnesses.

### Theorem 8.1 (distinct-entry certificate)

For an upper q-edge path `X_0->...->X_q` inside `T`, let `i_j` be the
coordinate inserted on transition `j`.  Then

\[
 \bigcup_{j=0}^qX_j=T
\]

if and only if the `i_j` are pairwise distinct and every `i_j` is absent
from `X_0`.

#### Proof

The initial state misses exactly q coordinates of `T`.  In q Johnson steps,
at most q previously missing coordinates can first enter.  Full union holds
exactly when every step inserts a different member of `T\X_0`.  QED.

The lower dual exposes the deleted physical coordinate `d_j`: exact
intersection with `S` is equivalent to the `d_j` being pairwise distinct
members of `X_0\S`.

Thus the current four-column transition table

```text
(source_state, target_state, quotient_arc, physical_inserted_coordinate)
```

together with one `AllDifferent` and q `(state_0,coordinate)` incidence
constraints replaces `(r+q)(q+1)` upper membership Booleans.  This is
implemented at lines 585--593 and 1276--1301.  At upper q3, the auxiliary
count drops from

```text
4 state integers + 3 arc integers + 44 Booleans = 51
```

to

```text
4 state integers + 3 arc integers + 3 coordinate integers = 10.
```

The implementation correctly takes `inserted` from the physical loop that
constructs `target` at lines 576--590.  It does not misuse the
normalized-frame coordinate stored in `arc_data`, which would require a
phase conversion.

This compression is exact only for minimal q-edge witnesses, so it does not
repair Section 6.

## 9. Exact arbitrary-interval network-flow encoding

There is an exact replacement for the upper-q3 strengthening which retains
literal chronology.

For a proper target `T`, let `E_T` be the directed physical Johnson edges
inside `V_T` retained by the strict quotient catalogue, and write `alpha(e)`
for the directed quotient arc of `e`.  Introduce binary variables

```text
f_e                         (e in E_T),
s_v,t_v                     (v in V_T).
```

Impose

\[
 s_v+\sum_{e\in\delta^-(v)}f_e
 =t_v+\sum_{e\in\delta^+(v)}f_e\le1                 \tag{9.1}
\]

for every `v`,

\[
 \sum_vs_v=\sum_vt_v=1,                              \tag{9.2}
\]

and

\[
 f_e\le y_{\alpha(e)}.                                \tag{9.3}
\]

Finally, for each `x in T`, impose the entry cut

\[
 \sum_{v:x\notin v}s_v
 \le
 \sum_{e=(u,v):x\in v\setminus u}f_e.                \tag{9.4}
\]

### Theorem 9.1 (interval-flow equivalence)

Assume the selected quotient arcs lift to one physical `W`-cycle and
`T` is proper.  Equations (9.1)--(9.4) are feasible if and only if some
contiguous carrier interval consists of states in `V_T` and has union `T`.

#### Proof

An interval supplies its internal edges, first state, and last state; these
satisfy (9.1)--(9.3).  If `x` is absent from the first state, full union says
that some interval edge first inserts it, giving (9.4).

Conversely, (9.1)--(9.2) make the chosen `f`-edges one directed start-to-end
path plus possible directed cycles.  By (9.3), every chosen edge belongs to
the selected physical carrier cycle.  A nonempty `f`-cycle would therefore
be the whole carrier cycle.  That is impossible inside `V_T` for proper
`T`, since not every central state is a subset of `T`.  Hence only the one
path remains, and it is a contiguous carrier interval.  Every coordinate
present at its start is covered; (9.4) makes every coordinate absent at the
start enter later.  Its union is `T`.  QED.

For the current missing k15 upper-q3 target, this exact formulation has

```text
3958 edge variables + 330 endpoint variables = 4288 binary variables
```

and about 4301 principal linear constraints.  This is larger in variable
count than the strengthened four-state table but has the correct
arbitrary-interval semantics and only sparse linear constraints.  It should
be benchmarked on the remote CPU, not locally.

With the arc selection fixed, (9.1)--(9.3) are a standard network path
system.  The entry cuts (9.4), when arc variables are jointly selected, are
additional covering rows; no total-unimodularity claim for the combined
matrix is made here.

## 10. Additional line findings and required regressions

1. Lines 580--584 catch both `KeyError` and `ValueError` and describe both as
   deliberate quotient-self-loop omission.  Only `KeyError` is the expected
   absent-choice signal.  `directed_arc` raises `ValueError` at lines
   324--327 when uniqueness fails; swallowing that exception silently
   under-approximates the transition graph and can turn a catalogue defect
   into a false UNSAT.  A future core patch should catch `KeyError` only and
   let `ValueError` fail closed.
2. Lines 541--543 check the upper target rank but not that `orbit_rep` is
   canonical.  Current CEGAR callers pass representatives from
   `upper_missing`, so this is not a present correctness error.  Either
   canonicalize at the API boundary or rename the parameter to
   `physical_target`; otherwise rotated duplicate cache entries are easy to
   create.
3. The existing lightweight regression exercises a lower-q3 state table but
   has no upper q3 global-scope test.  A permanent solver-free regression
   should reconstruct the fixed k15 seed and assert simultaneously:

   ```text
   canonical(union(cycle[102:107])) == 4031,
   bit_count(union(cycle[102:107])) == 11,
   minimum edge length for orbit 4031 == 4,
   no three-edge state-path witness for orbit 4031.
   ```

4. A composite regression should retain the rank-ten representative 14043,
   its orbit size 3, stabilizer size 5, 45 states, and 680 retained rows.
   This checks actual target-orbit handling independently of the all-full
   rank-eleven case.
5. The four-column change has made two existing audit programs stale:
   `scratch/audit_compact_q3_equivalence.py:20` and
   `scratch/audit_compact_shadow_state_paths.py:21` still unpack
   `(source,destination,arc)`.  At the current hash they raise an unpacking
   error before performing their claimed oracle comparisons.  They must
   ignore or audit the fourth defect-coordinate field explicitly.  Until
   rerun, prior three-column PASS output validates the earlier snapshot, not
   the current one.
6. The supplied build statistic `49,309` variables and `460,437` constraints
   belongs to the earlier membership-Boolean snapshot.  The current
   distinct-defect model has a materially different auxiliary count; those
   numbers should not be provenance-attached to hash `3ad43459...` without a
   fresh deterministic model build.

## 11. Audited boundary

Proved:

1. exact lower and upper local q-edge state-path semantics for arbitrary
   fixed q;
2. correct directed frame transport, quotient wrap, and physical cyclic
   chronology;
3. equivalence of minimal and arbitrary upper occurrence at q2;
4. a sharp obstruction to that equivalence at every q>=3;
5. correctness of the k15 short rank-ten target handling;
6. an exact distinct-entry compression for local paths;
7. an exact binary interval-flow formulation for arbitrary upper
   occurrence.

Not proved and false as a generic local statement:

```text
arbitrary upper-q3 interval occurrence
    => a four-state upper-q3 witness.
```

Therefore the current positive-search path is usable, but upper-q3 UNSAT
scope must be explicitly restricted until the interval-flow formulation or
the exact whole-selection no-good fallback replaces the minimal-window cut.
