# K17 physical deadline Benders master, protected-bank freedom, and the round-four 421-bank MaxSAT lift

Date: 2026-08-02  
Lane: P, replacement physical-master lane  
Status: exact sparse formulation, exact protected-bank relaxations, proof-safe
O3 C++/SAT tooling, one authenticated baseline replay, scoped H100 timeouts,
and a gated three-shell `final2822` history LNS audit.  Its first two quotient
base faces are proof-verified UNSAT and its third is UNKNOWN; no history-shell
solve was launched.  No non-equivariant `Phi<=7401` factor, lower compiler,
ranks-11--17 completion, or contiguous-OR word is claimed.

Frozen physical rebase:
`MATH_THEOREM_V_K17_DEADLINE_PARTICLE_RETHREAD_AND_MARKER58_NONFLAT_NOGO_20260802.md`,
SHA-256 `7887ba57...`.  The quotient residence/age comparison additionally uses
`MATH_THEOREM_R2_K17_ROUND1_RESIDENCE_FACTOR_BENDERS_AND_UNIT37_DM_20260802.md`;
the quotient restriction is always stated explicitly and is never imported
as a non-equivariant theorem.

## 0. Outcome

The full non-equivariant physical master has the literal `875,160` rank-eight
facet atoms required by theorem V.  It admits two useful exact realizations.

1. A sparse atom Benders master keeps the facet, owner, cap, protected-bank and
   lazy subtour rows hard.  Connected incumbents are passed first through the
   exact two-gap separator and then, only when needed, through the exact
   `rho_2,rho_3` deadline oracle.  A failed incumbent is always safely removed
   by one whole-factor no-good.
2. A directed prefix extension integrates the exact deadline row without
   assigning 24,310 integer positions.  Four nested prefix bits per owner
   encode `A,C,G_0,G_1`; the loss is one cardinality row, and length-two/three
   cluster legality is separated by local directed-path clauses.

The protected marker bank is not resource-jammed.  Its exact contraction has
20,366 residual facets, 40,732 residual owner slots, 165,886 live incidence
arcs, and 607,121 raw residual pair atoms.  Max flow saturates every slot.  All
18,462 caps not already protected retain at least four locally supported
atoms, and their cap--facet projection has a matching saturating all 18,462
caps.  The bank by itself forces no complete short-run bracket.

The physical resource CNF has `875,160` primaries, `5,178,030` variables and
`11,134,048` clauses.  The authenticated connected all-cap baseline solves and
replays immediately.  The stronger exploratory branch banning every one of
the 20,332 non-forced baseline pairs reached Kissat's 600-second limit with
status `UNKNOWN` and 973,368 KiB maximum RSS.  This is not a negative result.

Finally, the authoritative round-four 421 quotient residence blockers can be
exposed on the physical master without selector explosion.  Use one shared
relaxation literal per blocker and its 17 literal translates: 421 selectors
and 7,157 guarded physical clauses.  C10 originally supplied the `B=206`
control.  Direct authenticated evaluation of the newer `final2754` factor on
the same canonical 421 file gives score 129, so the current positive control
is `B=129` and the first strict physical proxy target is `B=128`.  Their
audit-only dimensions are respectively `5,232,631/11,249,728` and
`5,232,211/11,248,890` variables/clauses.  No physical MaxSAT solve has been
launched.  This is a strict-residence proxy objective, not the nonflat
deadline functional `Phi`.

The newest nonresident Pareto point `final2754` has 2,754 positive short runs
and deep-upper holes `1853/357/0`; ranks 13--17 are complete.  It dominates
the other rank-13-complete points currently in this lane, but C10 still has
the smaller rank-11 hole count `1802`.  These are exact factor diagnostics,
not residence, source, or deep-upper completion claims.

The requested exact-history LNS around `final2822` was also built and gated.
Its 166 current blocker orbits use 438 incumbent primaries.  The support,
one-owner-halo and two-owner-halo faces retain 4,167, 7,586 and 11,371 live
options.  Independent CaDiCaL+DRAT checks prove the first two quotient base
faces UNSAT; the third returned `UNKNOWN` under separate 300-second CaDiCaL
and 600-second Kissat controls.  Since no shell passed the required SAT/base
consistency gate, no directed-history shell was launched and no global
negative conclusion follows.

## 1. Exact physical atom master

Let

\[
 {cal F}={[17]\choose8},\qquad
 {cal V}={[17]\choose9},\qquad
 {cal U}={[17]\choose10}.
\]

For `F in F` and an unordered pair `{a,b}` in the nine-point complement of
`F`, define

\[
 e=(F;\{a,b\}),\qquad
 \partial e=\{F+a,F+b\},\qquad u(e)=F+a+b.
\]

There are 36 atoms per facet and hence

\[
                  |E|=24310\cdot36=875160.
\]

With `x_e` binary, the exact resource/topology master is

\[
 \sum_{e:f(e)=F}x_e=1                                    \tag{1.1}
\]

for every rank-eight facet,

\[
 \sum_{e:v\in\partial e}x_e=2                            \tag{1.2}
\]

for every rank-nine owner,

\[
 \sum_{e:u(e)=U}x_e\ge1                                  \tag{1.3}
\]

for every rank-ten cap,

\[
 x_e=1\quad(e\in P),                                     \tag{1.4}
\]

and

\[
 x(\delta(S))\ge2
 \quad(\varnothing\ne S\subsetneq{cal V}).              \tag{1.5}
\]

Equations (1.1)--(1.2) select a spanning owner two-factor.  Equation (1.5)
makes it one Hamilton cycle.  Facet exactness also excludes singleton
positive coordinate runs: a `0,1,0` trace would repeat the same rank-eight
intersection on its entering and leaving edges.  Thus theorem V's
no-singleton normal form applies, and the final exact row is

\[
                         \Phi(T(x))\le7401.               \tag{1.6}
\]

Passing (1.1)--(1.6) is only the abstract resource/deadline gate.  The opening
facet and any cap whose unique provider is the removed seam still require a
literal boundary/top-port witness.  The lower occurrence matching,
simultaneous common-cap replay, ranks 11--17 and universal-word verifier remain
separate.

## 2. Protected-bank contraction and exact presolve

The 3,944 protected edges form 986 pairwise owner-disjoint four-edge paths on
five owners.  Contracting the bank gives the residual owner-degree histogram

```text
protected degree 0: 19380 owners, residual demand 2
protected degree 1:  1972 owners, residual demand 1
protected degree 2:  2958 owners, residual demand 0
```

and therefore

\[
 1972+2(19380)=40732=2(20366).                            \tag{2.1}
\]

The exact contracted incidence relaxation is the network

```text
source -> residual facet F     capacity 2
F -> containing owner v       capacity 1
v -> sink                     capacity 2-d_P(v).
```

It is integral.  A deficient source cut is precisely the protected-bank Hall
separator

\[
 b(A)\le b(D)+|E(A,{cal V}\setminus D)|.                \tag{2.2}
\]

The new literal audit gives

```text
active residual facets                         20366
residual demand / max-flow value               40732 / 40732
live facet-owner incidences                    165886
raw residual pair atoms                        607121
forced selected incidence halves                  102
forced-incidence-closed pair atoms             606169
```

The live-owner count per residual facet is

```text
2:34  4:170  5:1054  6:697  7:2380  8:5253  9:10778.
```

The alternating residual digraph has one giant SCC on 41,667 active nodes.
The reported SCC total includes the 2,958 saturated owners as isolated nodes;
after deleting those trivial nodes the only further tight pieces are the
forced local units.  All 125,154 unselected live incidences are exchangeable
in the facet/degree projection.  This is marginal support, not a theorem that
any two marginal incidences form a jointly extendable atom.

Every protected path has one eligible endpoint-closing atom.  After
contraction it is a self-loop sealing an isolated five-cycle, so all 986 such
atoms are forbidden by (1.5).  Exact forced-half propagation then identifies
34 complete residual edges.  A maximally presolved implementation may work on
20,332 contracted supervertices and about 605 thousand genuinely free atoms;
the current proof tool deliberately retains all 875,160 primary names and
fixes invalid choices by clauses, which keeps decoding simple.

### 2.1 Cap projections and redundant exact rows

The 986 protected caps already have load four.  For residual cap load `r_U`,
put

\[
 \eta_U=
 \begin{cases}
 r_U,&U\text{ protected},\\
 r_U-1,&U\text{ unprotected}.
 \end{cases}
\]

Then every cap-complete residual factor obeys

\[
 \sum_U\eta_U=1904,
 \qquad
 \sum_{U\ni j}\eta_U=1120\quad(j\in[17]).               \tag{2.3}
\]

The initial cap--facet support projection has 18,462 left caps, 20,366 right
facets and a matching of size 18,462, leaving exactly 1,904 repeat facets.
After forced-incidence closure the audited support has 592,195 arcs and still
matches all 18,462 caps; every cap has degree at least four.  This is a strong
polynomial relaxation, but it does not enforce the two owner endpoints of all
chosen facet atoms simultaneously.

Additional exact propagation rows are available.  Every palette/owner-degree
factor has exactly 2,860 coordinate-toggle edges per coordinate.  After the
protected and forced-edge constants are removed, the free master has a fixed
toggle marginal for each of the 17 coordinates.  Cap loads also satisfy the
pointwise excess equations (2.3) and the safe bounds `r_U<=6` on protected
caps and total load at most ten on every cap.

## 3. Sparse exact Benders loop

The recommended first exact solver is:

1. contract/fix the protected bank, saturated owners, 986 path-closing loops
   and the 34 locally forced residual edges;
2. impose residual facet exact-one, owner exact-degree, the 18,428 remaining
   cap ALOs, and the redundant marginal rows;
3. solve an integral atom factor;
4. separate every owner component by (1.5);
5. once connected, run the two-gap oracle in both directions and over every
   opening;
6. only if two-gap passes, evaluate the exact `rho_2,rho_3` subproblem; and
7. on failure emit at least the exact whole-incumbent no-good

\[
 \sum_{e:x_e^*=1,\ e\notin P}x_e\le20365.               \tag{3.1}
\]

In SAT form (3.1) is one clause, not one unit per incumbent edge.  The
exploratory `--ban-releasable-baseline` option intentionally fixes all 20,332
releasable incumbent edges to zero simultaneously; it is a distance face and
must never be confused with (3.1).

For an integral degree-two model, a component clause asking for one crossing
atom is equivalent to at least two crossings by parity.  For an LP relaxation,
separate `x(delta(S))>=2` with a global minimum cut.  The protected incidence
Hall cut (2.2), cap--facet matching cuts, and standard two-matching/blossom
rows are additional polynomial projections.

### 3.1 Exact fixed-cut deadline oracle

For one oriented opening, let `S_2,S_3` be the occurrence-labelled starts of
internal positive runs of lengths two and three.  For `0<=d<=W`, define

\[
 P_2(d)=\max(\{a\in S_2:a\le W-d-3\}\cup\{0\}),
\]

\[
 P_3(d)=\max(\{a\in S_3:a\le W-d-4\}\cup\{0\}).         \tag{3.2}
\]

For `d_1>=d_2`, theorem V gives exactly

\[
 A=P_2(d_1),\qquad
 C=\max\{P_2(d_2),P_3(d_1)\},                            \tag{3.3}
\]

and cost

\[
 d_1+d_2+A+C.                                             \tag{3.4}
\]

For fixed `d_1`, the inner problem is

\[
 \min_{0\le d_2\le d_1}
 \bigl(d_2+\max\{P_2(d_2),P_3(d_1)\}\bigr).             \tag{3.5}
\]

Because `P_2` is nonincreasing, (3.5) is the minimum of one prefix-RMQ value
`d+P_2(d)` and the first `d` at which `P_2(d)<=P_3(d_1)`.  The implemented
oracle is `O(W log W)` per candidate opening and exports `A,C,d_1,d_2`.
Its independent built-in test exhausts every pair of short-run subsets for
`W=5,...,12` against direct `d_1,d_2` enumeration, including the legal middle
length-two disjunct.

The two-gap prefilter rejects an opening when

\[
 G_2<20610,
 \qquad
 G_2=\max\{a_1+2,\max_i(a_{i+1}-a_i+2),W-a_m\}.          \tag{3.6}
\]

If every opening and both directions fail (3.6), then `Phi>7401` exactly and
the expensive oracle is unnecessary.

## 4. Exact directed prefix extension

The Benders loop is simplest, but the deadline row also has a sparse exact
extension.  Replace each undirected atom by its two directed arc literals
`y_uv,y_vu`, with

\[
 y_{uv}+y_{vu}=x_e,qquad
 \sum_wy_{vw}=\sum_wy_{wv}=1.                            \tag{4.1}
\]

Directed subtour cuts make this one directed Hamilton cycle.  Let `h_v` mark
the first owner, equivalently the seam gap immediately before `v`.  For each
threshold `q in {A,C,G_0,G_1}`, let `t^q_v` mark its gap and let `u^q_v` mean
that owner `v` lies strictly before threshold `q`.  Impose

\[
 \sum_vh_v=1,qquad \sum_vt^q_v=1,                       \tag{4.2}
\]

and, on every selected arc `p->v`,

\[
 u^q_p-u^q_v=t^q_v-h_v.                                  \tag{4.3}
\]

For MILP, (4.3) is guarded with a safe big-M value two.  For SAT, use the
constant-size truth-table clauses.  Thresholds may coincide with one another
or with the seam; when `t^q=h`, the constant all-zero/all-one prefix encodes
`q=0/W`.

The nesting rows are

\[
 u^A_v\le u^C_v\le u^{G_0}_v\le u^{G_1}_v.              \tag{4.4}
\]

They imply the correct cyclic order of the four marked gaps.  The exact loss
row is simply

\[
 \sum_v\bigl(u^A_v+u^C_v+1-u^{G_0}_v+1-u^{G_1}_v\bigr)
 \le7401.                                                 \tag{4.5}
\]

For a selected directed bracket path

\[
 w_0,w_1,\ldots,w_\ell,w_{\ell+1}
\]

whose coordinate trace is `0,1^ell,0`, define

```text
EA = uA[w1] OR tA[w1]
EC = uC[w1] OR tC[w1]
L0 = NOT uG0[w(ell+1)]
L1 = NOT uG1[w(ell+1)].
```

The exact lazy cluster clauses are

```text
length 3:  EC OR L0
length 2:  (EA OR EC OR L1) AND (EA OR L0 OR L1),
```

each guarded by the negations of the three/four path arcs.  These are exactly
the theorem-V conditions

\[
 a\le C\ \lor\ b+1\ge G_0
\]

and

\[
 a\le A\ \lor\
 (a\le C\ \land\ b+1\ge G_0)\ \lor\ b+1\ge G_1.
\]

Integral separation is `O(17W)` after traversing the cycle.  Fractional
separation of each fixed-length path-clause family is polynomial by layered
shortest-path dynamic programming.  This extension is exact for (1.6) and
does not assume `Z_17` equivariance.

## 5. Strong two-gap and cluster-core cuts

The strongest cheap incumbent test is the exact all-cut two-gap value (3.6).
At budget 7,401 every feasible opening clusters its internal length-two starts
in an early/late collar with

\[
 A+d_2\le3700,                                           \tag{5.1}
\]

and its length-three starts in a shared collar of span at most

\[
 C+d_1+3\le7404.                                         \tag{5.2}
\]

For safe support-reduced Benders cuts, retain a fully selected directed path
segment, treat its complement as an empty gap, and run the exact particle
oracle in both directions over every seam placement.  Adding more forced
short runs can only increase the frontiers.  If this optimistic segment is
already above 7,401, negate the mutable atom support of the segment.  Shrink
the segment deletion-wise to obtain an inclusion-minimal cluster core.

No quotient strict-residence clause may be imported as a hard row of the
non-equivariant particle master.  A physical length-two or length-three run
can be legal near the deadline/start collars.  Without a checked segment
certificate, the only generic factor-only particle cut is the full no-good
(3.1).

## 6. Proof-safe tooling and finite runs

The local package is

```text
scratch/p_k17_physical_deadline_master_20260802/
```

and contains:

```text
audit_p_k17_protected_bank_flow_20260802.cpp
  exact protected contraction, max flow, alternating SCC, cap support and
  cap--facet matching audit;

build_p_k17_physical_resource_cnf_20260802.cpp
  deterministic 875,160-primary DIMACS compiler with signed baseline phase,
  sequential counters, protected units/path-loop bans, optional component
  shores, exact baseline no-good, and scoped distance branches;

decode_verify_p_k17_physical_resource_model_20260802.cpp
  independent semantic model replay, component export, two-gap separation,
  and exact Phi<=7401 gate with explicit thresholds.
```

The baseline resource CNF compiled to

```text
primary options       875160
variables            5178030
clauses             11134048
DIMACS size            230 MiB approximately.
```

On H100 CPU, Kissat 4.0.4 returned the authenticated baseline SAT model in
2.57 seconds with roughly 711 MiB RSS.  Independent replay recovered one
24,310-owner cycle, all 19,448 caps and all 3,944 protected edges, then
reproduced the exact `G_2=36` particle rejection.

The maximal-release branch imposed one unit ban on every one of the 20,332
non-forced mutable baseline pairs.  It compiled to 5,178,030 variables and
11,154,380 clauses.  On

```text
/home/amodo/or15/work/p_k17_physical_deadline_master_20260802
```

Kissat reached its internal 600-second limit:

```text
status                    UNKNOWN
solver exit code                0
wall time                  600.20 s
maximum RSS                973368 KiB
release.cnf SHA-256
  c38b5a98200e212c0a2ffce9bb390b3777068e78da6d0eebbe0cb71ff6db57de
```

This branch is an exploratory simultaneous-disjointness face.  Its timeout
proves nothing about the ordinary physical master or even the existence of a
far completion.

The exact first Benders continuation added only the width-20,366 baseline
no-good (3.1).  Its 5,178,030-variable, 11,134,049-clause CNF also returned
`UNKNOWN` at a separate 300-second Kissat limit, with 1,018,912 KiB maximum
RSS.  No second atom factor and no UNSAT certificate were produced.  This is
likewise a nonterminal search result, not a lower bound.

## 7. Round-four 421-bank physical partial MaxSAT objective

The authoritative round-four ledger first forms the exact 413-row union
`385 U floor_c14clean220`, then merges the 206 blockers exposed by the C10
factor:

```text
round-three cumulative blockers       413
C10 current blockers                   206
overlap                                198
new                                      8
round-four cumulative blockers        421
arity histogram        1:45  2:17  3:201  4:158.
```

The canonical bank SHA-256 is
`8caaf19d74b161146e312a99e6e25d46d8e2e67b9e20785a4382bd066dc28106`;
the merge-audit SHA-256 is
`ea8f828a525bfafa234a3f6af78bd47fb0fc72385022bf761a424857eee36bbc`.
The exact C10 factor falsifies 206 round-four clauses, with violated arities
`1:34, 2:10, 3:90, 4:72`; it has 3,502 short runs, all rank-ten caps, the
protected bank, and one physical component.  It was the authenticated control
when round four was frozen.  The C10 factor/model hashes are `33d6719d...` and
`4e49661a...`.

The later factor `final2754` (factor SHA-256 `fac9ad6c...`, model SHA-256
`edc93794...`) was evaluated directly against the same canonical 421 clauses,
not inferred from its separate 445-bank score.  It falsifies 129 groups with
arity histogram `1:28, 2:7, 3:50, 4:44`; all 129 groups violate their complete
17-phase families, or 2,193 physical guard rows.  Consequently `B=129` is now
the positive control and `B=128` the first strict canonical-421 bound.  The
literal evaluation audit has SHA-256 `08149d71...`.

The separate union that also imports C16's three novel rows has 423 blockers.
It is preserved only as an exploratory next-round closure and is not the
authoritative round-four objective.

### 7.1 Exact physical lift with 421 selectors

For blocker `b`, choose one authenticated physical representative of its
short-run bracket.  If its mutable quotient support is

\[
 Q_b=\{q_1,\ldots,q_s\},\qquad1\le s\le4,
\]

the representative determines relative physical phases
`sigma_(b,1),...,sigma_(b,s)`.  Let `p(q,sigma+t)` be the literal physical
atom obtained by rotating that quotient option by `t`.  Introduce one
relaxation literal `r_b` and add

\[
 \bigvee_{j=1}^s\neg x_{p(q_j,\sigma_{b,j}+t)}\ \lor\ r_b
 \qquad(t\in\mathbb Z_{17}).                             \tag{7.1}
\]

The fail-closed phase audit accepts every source overlap, so the complete
lift adds exactly

```text
relaxation selectors                         421
translated guarded clauses          421*17 = 7157
physical atom literal occurrences           22338
distinct physical option variables          15164
selector literal occurrences                 7157
physical arity histogram       1:765 2:289 3:3417 4:2686.
```

The objective/bound row is

\[
                         \sum_{b=1}^{421}r_b\le B.        \tag{7.2}
\]

At `B=129`, (7.1)--(7.2) has `final2754` as a control witness: exactly 129
groups and `129*17=2193` translated guard rows are selected.  The first strict
physical proxy target is therefore `B=128`.  C10 remains a historical
`B=206` control for reproducing the original round-four freeze.

One selector per blocker is exact for the following robust orbit objective:
the blocker costs one if any of its 17 translated physical clauses remains
violated.  On an equivariant assignment all 17 clauses have the same truth
value, so (7.1) reduces exactly to the original quotient objective.  If the
desired objective were the number of violated physical occurrences instead,
use 7,157 selectors; even that count is negligible next to 5.18 million base
variables.

The selector count does not explode.  A direct Sinz `at-most-128` counter on
421 selectors adds 53,760 auxiliary variables and 107,685 clauses.  With the
uncut physical base and 7,157 guarded rows, the exact audit-only fixed-bound
totals are

```text
variables      5232211
clauses       11248890.
```

The `B=129` control uses 54,180 counter auxiliaries and 108,523 counter
clauses, for 5,232,631 variables and 11,249,728 clauses.  Both refreshed
audit-only builds pass under manifest SHA-256 `9178cb01...`; no refreshed CNF
was materialized and no solver was called.  The older `B=205/206` CNFs remain
frozen with hashes `ea0f725e.../76296823...`, but their bounds are stale as
search calibrations.

A reusable unary totalizer is preferable for descent: compile once
and impose `not output[B+1]` by an assumption/unit at each bound.

No reverse implication is needed for projected feasibility.  The 17 forward
rows force `r_b=1` whenever any translated support is fully selected; if none
is selected, `r_b=0` is available and an optimum/bounded witness can choose
it.  A literal biconditional would need one phase-conjunction auxiliary per
translated clause; quotient-style reverse clauses attached directly to the
shared `r_b` would be wrong.  The independent validator should always
recompute the current bank score from the physical factor.

### 7.2 Phase reconstruction is mandatory

The cumulative quotient clause stores only the set of quotient variable
numbers; it does not store their relative physical shifts.  A sound refreshed
lift reconstructs representatives from four authenticated source
ledgers:

```text
round1.blocks.cnf   from the connected double_fusion factor
current.blocks.cnf  from paired_escape005.factor.tsv.
c14clean.current.blocks.cnf from floor_c14clean.factor.tsv.
c10.current.blocks.cnf from c10_escape_from3553.factor.tsv.
```

For every short-run occurrence, record its physical mutable edge keys,
canonicalize the set over all 17 rotations, and bind it to the sorted quotient
support.  Require exactly one orbit of 17 occurrences for each source blocker.
First reconstruct the old 385-bank union (316 plus 237 with 168 overlaps),
then merge the 220 clean blockers, requiring all 192 overlaps with the old
bank to have identical physical support orbits.  Finally merge the C10 source:
it overlaps the 413-bank in 198 groups and contributes eight.  All six
pairwise source overlaps have identical physical phase orbits; every one of
the 421 merged groups therefore has exactly 17 physical rows.  Applying one
common shift to the map's canonical edge of every literal without this
relative-phase audit is not proof-safe.

The compiler also binds every occurrence edge back to its quotient variable
through all 607,121 developed capacity-valid option edges, checks the 232
fixed facet orbits against the 3,944-edge protected bank, and authenticates
every input by SHA-256.  The signed polarity baseline is the connected,
cap-complete double-fusion factor (`7d39e3ae...`), not the cap-free diagnostic
flow factor.  With the correct polarity the guard complements split as
20,213 positive and 2,125 negative literals.

### 7.3 Objective scope

The 421 blockers are model-specific strict cyclic-residence necessities.  The
partial MaxSAT objective measures progress against these known motif orbits;
it is not the exact number of short runs, is not residence sufficiency, and is
not the nonflat `Phi` row.  New incumbents can expose new blockers, so the
objective remains inside a cumulative lazy loop.  In the non-equivariant
deadline lane, use it as a complementary search score only; particle-feasible
collared short runs must not be hard-forbidden.

Topology remains lazy.  Every SAT/MaxSAT incumbent is semantically replayed;
disconnected factors receive exact physical component shores before the next
bound solve.  A final UNSAT claim at any `B` requires a frozen DIMACS/proof and
independent DRAT/LRAT verification.  Timeout is `UNKNOWN`.

### 7.4 Eager quotient-age alternative

The eager quotient Hamilton/voltage/age formulation conditionally supersedes
the blocker proxy only on the connected nonzero-voltage `Z17`-equivariant
face.  There it enforces cyclic positive residence at least four exactly, so
all current and future short-run blocker rows become redundant.  It does not
supersede the 875,160-option non-equivariant lane, and it is stronger than the
deadline row `Phi<=7401`, where a collared short run may remain legal.

The reusable quotient census is

```text
owner/facet/cap orbits                 1430 / 1430 / 1144
fixed protected edge orbits                         232
residual facets / option orbits             1198 / 35713
nonloop options / excluded loops              35705 / 8
optional / fixed / total directed darts 71410 / 464 / 71874.
```

Fix the direction of one nonloop protected dart `a_*=(t_*,r_*)`.  Every
Hamilton factor contains this edge and global reversal chooses its direction,
so this loses no solution.  Require one selected incoming and outgoing dart
at every owner.  With `T_(r_*)=0`, `0<=T_v<=1429`, impose on every selected
dart other than `a_*`

\[
                y_{vw}=1\Longrightarrow T_w=T_v+1.                    \tag{7.3}
\]

Removing `a_*` leaves no directed cycle because (7.3) would strictly increase
around it.  The remaining cycle cover is therefore one Hamilton path, and the
bounds force its orders to be exactly `0,...,1429` even if the `T` variables
are continuous.  This is the smallest ILP connectivity layer; a binary-order
multiplexer is the preferred CNF layer.

For an oriented map row with endpoints `A=rho^alpha a` and
`B=rho^beta b`, put `delta=beta-alpha mod 17`.  At source phase `r` the
physical dart is

\[
             (\rho^r a)\longrightarrow(\rho^{r+\delta}b).              \tag{7.4}
\]

Once Hamiltonicity is hard, the smallest ILP voltage row needs no owner
potentials:

\[
       \sum_a\delta_a y_a=17z+\rho,\qquad1\le\rho\le16.               \tag{7.5}
\]

The nonzero remainder makes the physical `Z17` lift one 24,310-owner cycle.
If downstream fibre addresses are required, fix `R_(r_*,0)` and use one-hot
potentials.  If `B_0=rho^delta b`, the source-frame deleted and inserted labels are the
unique elements of `a-B_0` and `B_0-a`; the target-local inserted label is
shifted by `-delta`.  On nonclosing darts the potential propagation is

\[
 R_{v,r}\wedge y_{vw}\Longrightarrow R_{w,r+\delta}.                  \tag{7.6}
\]

and the selected closing dart requires `R_(t_*,r) -> not
R_(r_*,r+delta)`.  This is larger than (7.5) but exports the physical gauge.

A direct five-state age variable on each of the nine present labels records
ages `1,2,3,4`, with 4 saturated.  The deleted label must be at age 4, the
inserted label receives age 1, and every survivor follows
`q -> min(q+1,4)` while its local label shifts by `-delta`.  These transitions
must also cross the chosen quotient gauge dart: that dart represents an orbit
of 17 physical edges, not one removable physical seam.

Equivalently, with absent state zero implicit, the complete DFA is

```text
0->0, 0->1, 1->2, 2->3, 3->4, 4->4, 4->0;
only state 4 may leave to state 0.
```

The proposed quotient seam must not delete this transition.  A quotient dart
develops to 17 physical edges, so exempting it would create 17 openings.  A
literal physical seam is one separately chosen fibre lift after a strict
cyclic-age solution is found.  If exact left/right collar ages must be carried
inside the master, the five cyclic states are insufficient: retain the
physical nine-state interface `0,1,2,3,4,L1,L2,L3,L4` from theorem R2.

The independently audited high-level sizes are

```text
uncontracted global-voltage model       86176 variables / 795990 rows/tables
uncontracted explicit-potential model   87604 variables / 867864 rows/tables
contracted protected-path model         85420 variables / 793530 rows/tables.
```

The contraction has 1,198 supervertices, 35,646 usable option edges and
71,292 darts.  Its 67 self-arcs split as eight original loops and 59 options
closing a fixed path component; only 58 of the latter have effective voltage
zero, while one has voltage eight.  All 67 are topology-forbidden on the final
one-component equivariant Hamilton face, but it would be wrong to call all 67
literal loops of the unrestricted physical contraction.

Starting from the 204,167-variable/439,145-clause no-cut quotient CNF,
orientation plus the sparse one-hot age interface gives exactly the projected
census `327,521` variables and `3,119,103` clauses.  A direct binary
order/multiplexer and one-hot potential extension is estimated at about
`0.40` million variables and `6.2--7.7` million clauses, depending on the
increment/comparator circuit; this is an encoder estimate, not a frozen
DIMACS.  The repository Waksman recurrence uses 14,430 switches at width 1,430
(11,814 after protected contraction).  Once 11-bit owner/successor and phase
payloads are routed and linked back to the sparse option catalogue, its
conservative estimate is about 1,016,911 variables and 7,701,564 clauses.
Thus Waksman does not beat the sparse order formulation here.

The existing exact three-history compiler materializes 348,971 variables and
3,904,557 clauses on the strengthened round-one base.  On its authenticated
loopless directed-cycle-cover face, its three insertion histories
semantically enforce the same strict cyclic positive-residence language as
the age DFA; Hamiltonicity and nonzero voltage remain lazy.  This is semantic
equivalence of the residence layers, not syntactic CNF subsumption.  The full
physical master and its directed-prefix `Phi` extension are broader but do
not contain this compressed eager quotient layer.  The dimension auditor
source/output hashes are `f9da4109.../e80e3437...`; no full eager
topology/voltage DIMACS or duplicate solve was launched.

### 7.5 Authenticated nonresident Pareto/source ledger

```text
factor       positive short runs   blocker score (scope)   holes r11/r12/r13
C10                  3502          206 (canonical421)          1802/425/17
final2992            2992          162 (separate 445)          1921/425/0
final2822            2822          146 (separate 445)          1870/391/0
final2754            2754          129 (canonical421)          1853/357/0
```

`final2754` has exact facet/owner/cap/protected, quotient connectivity and
nonzero-voltage gates, and ranks 13--17 are complete.  Its 2,754 positive
short runs are `1,377+1,377` of lengths two and three, so it remains
`NONRESIDENT/NEED_CEGAR`.  Neither the 445-bank scores nor rank-13 completion
make it a source word: a literal resident opening, collar/source envelopes,
lower compiler and final universal-word verification are still absent.

### 7.6 `final2822` exact-history defect-support LNS

The LNS seed remains the explicitly requested authenticated `final2822`
factor, rather than being silently replaced by the newer Pareto point.  Its
2,822 physical short runs collapse to 166 quotient blocker clauses, 83 of
length two and 83 of length three, each with translation multiplicity 17.
Their union `S` contains 438 selected primary variables.

Let the halo graph have only the 1,198 incumbent-selected primaries as its
vertices, joining two exactly when their quotient edges share a rank-nine
owner.  It does not transmit through rank-ten caps, protected edges or
unselected catalogue options.  Fix every selected incumbent primary outside
the retained shell positively; leave every other primary unconstrained.  The
audited nested faces are

```text
shell                    membership  effective free  +units  free owners  live options
S0 blocker support              438             438     760          554          4167
S1 one owner halo               601             600     597          699          7586
S2 two owner halos              725             724     473          812         11371.
```

Every literal of all 166 current blocker clauses remains changeable in every
shell.  The difference between membership and effective freedom accounts for
positive primary units already present in the history master; inherited
negative units are also replayed explicitly.  The materialized quotient-base
controls have 204,167 variables and respectively 440,223, 440,060 and
439,936 clauses.  Their SHA-256 values are `9dc8514d...`, `1115b220...` and
`29736dd5...`.  The corresponding directed-history faces have 348,971
variables and 3,905,317, 3,905,154 and 3,905,030 clauses, with hashes
`794c2c36...`, `420be604...` and `b85a8d4a...`.

The launch rule was deliberately stronger than mere CNF construction: an
independent solver first had to return SAT on the exact quotient-base face,
then a separate checker had to replay the complete assignment, resource
rows, caps and all appended positive units.  The H100 controls at

```text
/home/amodo/or15/work/p_k17_final2822_history_lns_20260802
```

gave the following outcomes:

```text
S0  CaDiCaL 0.13 s  UNSAT, DRAT SHA d430b58f..., drat-trim: VERIFIED
S1  CaDiCaL 0.13 s  UNSAT, DRAT SHA a6349694..., drat-trim: VERIFIED
S2  CaDiCaL 300 s   UNKNOWN (exit 0, no verdict)
S2  Kissat   600 s  UNKNOWN (exit 0, no verdict).
```

Thus the two smaller local faces are rigorously excluded, but this says
nothing negative about S2, any larger shell, the unrestricted quotient
history master, or the physical 875,160-option master.  In particular, a
partial S2 proof stream is not a certificate and was not admitted to the
frozen bundle.  S1 contains S0, so the S1 proof subsumes the S0 exclusion;
both certificates are kept as independent audit milestones.  These shells
are restricted positive-unit overlays on the topology-lazy three-history
CNF, not instances of the still-unbuilt full eager Hamilton/voltage model.
No directed-history LNS solve was authorized or launched.

## 8. Current verdict and next exact steps

The protected bank leaves abundant certified physical resource freedom:

* one connected cap-complete protected factor already exists;
* the degree fibre has a giant alternating component;
* both facet/owner flow and cap/facet Hall projections pass;
* no complete short bracket is fixed at the root; and
* more than 600 thousand non-equivariant residual atoms survive exact local
  presolve.

Whether that freedom can cluster every short run enough to achieve
`Phi<=7401` remains open.  The next proof-safe computation is:

1. independently review the frozen four-source phase compiler, canonical-421
   hash and `final2754` literal audit;
2. if the physical proxy lane remains preferable to the eager quotient-age
   lane, materialize one reusable totalizer with the current `B=129` control
   and first strict assumption `B=128`, then separate topology lazily;
3. keep the `final2822` S0/S1 proof exclusions local; S2 is `UNKNOWN`, and a
   larger history shell is launchable only after its exact quotient base is
   independently SAT and the complete model passes semantic replay;
4. implement the sparse quotient order/voltage/age master only under a fresh
   resource budget and hash comparison, rather than duplicating an
   unrestricted history solve;
5. in parallel, continue ordinary atom Benders with exact no-goods and the
   two-gap/exact-`Phi` oracle; and
6. send any `Phi`-passing cycle to the opening-resource, lower compiler and
   ranks-11--17 replays without inferring inheritance from its predecessor.
