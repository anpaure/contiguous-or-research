# Candidate1911 all-support one-side rethread master

Date: 2026-08-02  
Lane: L  
Status: **exact next-class reduction; no finite solve claimed**

## 1. Why the next class is large

Fix the authenticated candidate1911 factor and its phase-labelled quotient
chronology.  For a length-two run orbit starting at `s`, let

\[
                         I_s=\{s-1,s,s+1\}
\]

be its outgoing-transition span.  The 69 such spans have transversal number
exactly

\[
                              \tau=67.                    \tag{1.1}
\]

The lower bound is the 67 pairwise-disjoint spans frozen in
`length2_disjoint_spans.tsv`.  For the reverse inequality, choose one point
from each of those 67 spans, choosing 558 in `I_558`, 850 in `I_849`, and 852
in `I_853`.  These choices also hit the two omitted spans `I_559` and `I_851`.

Consequently every flat factor rethread attaining minimum positive run at
least three changes at least 67 old phase-labelled quotient transitions.
The span and sign rows do not exclude a one-side elementary assignment
circuit of support 67.  They do not prove that such a circuit exists or is
topologically admissible.  This fixed-`H`, arbitrary-`D` family is the first
genuinely new flat class attacked here after the bounded C6/C8 shells.

## 2. Exact fixed-H formulation

Freeze candidate1911's `H` perfect incidence matching and reselect an
arbitrary phase-labelled `D'` perfect matching.  This is not support-capped;
relative to the old `D`, every terminal `D'` is a vertex-disjoint product of
elementary assignment cycles, with any legal phase-only loops kept literal.

For every incidence

\[
                    e=(u,f,s(e))
\]

which is not the fixed `H` edge at owner `u`, introduce
$x_e\in\{0,1\}$.  There
are exactly 11,440 allowed incidences.  Since `H` is fixed, each `e` has four
literal labels determined before optimization:

```text
L(e)       lower rank-7 q1 turn at owner u
U(e)       upper rank-10 q1 turn at facet f
q(e)       successor owner H^{-1}(f)
delta(e)   signed phase increment s(e)-s(H_f)
```

The exact matching core is

\[
 \sum_{e:u(e)=u}x_e=1\quad(u\in O),\qquad
 \sum_{e:f(e)=f}x_e=1\quad(f\in F).                     \tag{2.1}
\]

This is the integral bipartite assignment/min-cost-flow polytope.  Every
selected edge gives one directed transition

\[
                  u\longrightarrow q(e)\quad\text{of weight }\delta(e).
\]

The facet equations and the fixed `H` bijection make the selected transitions
a permutation of the 1,430 owners.

## 3. Exact q1 and old-run rows

The terminal q1 loads are linear:

\[
 \mu'_7(T)=\sum_{e:L(e)=T}x_e,\qquad
 \mu'_{10}(T)=\sum_{e:U(e)=T}x_e.                       \tag{3.1}
\]

The weakest protected condition is hole-monotonicity:

\[
 \mu'_{10}(T)\ge1\quad\text{for every rank-10 target }T,
\]

\[
 \mu'_7(T)\ge1\quad
 \text{for every rank-7 }T\notin
 \{\texttt{0x00e0f},\texttt{0x01547}\}.                \tag{3.2}
\]

Full lower-q1 repair adds the two omitted inequalities.  Coefficientwise
neutrality instead imposes equality in (3.1) to every old occurrence load.
These predicates must not be conflated.

Let `o_p` be the old owner at chronology position `p`.  For an old tail
position `p`, put

\[
 w_p=1-\sum_{e:u(e)=o_p,\,(q(e),\delta(e))=
                 (q_0(o_p),\delta_0(o_p))}x_e.          \tag{3.3}
\]

Thus `w_p=0` exactly when both the successor and signed phase increment are
the old transition.  Every baseline short run supplies the necessary row

\[
                  \sum_{p\in I}w_p\ge1,                 \tag{3.4}
\]

where `I` has three tails for a length-two run and four tails for a
length-three run.  An exact depth-three master includes all 69+187 baseline
rows.  The 69 length-two rows alone imply `sum_p w_p >= 67`.

For one endpoint-changing elementary assignment cycle of support `t`, every
changed row gives a changed transition, so `t>=67`.  Hamilton sign requires

\[
                         (-1)^{t-1}=1,
\]

hence `t` is odd and the smallest support not excluded by the span and sign
rows is 67.  More
generally, for `c` nontrivial disjoint endpoint cycles and no phase loops,

\[
 t\ge\max(67,2c),\qquad t\equiv c\pmod2.                \tag{3.5}
\]

This parity row is necessary, not sufficient for Hamiltonicity.

## 4. Topology, voltage and new-run cuts

Let

\[
 p_{uvd}=\sum_{e:q(e)=v,\,\delta(e)=d,\,u(e)=u}x_e.
\]

The permutation is one quotient cycle exactly when every nonempty proper
owner set has an outgoing selected transition:

\[
 \sum_{u\in S,\,v\notin S,\,d}p_{uvd}\ge1
 \quad(\varnothing\ne S\subsetneq O).                  \tag{4.1}
\]

These are ordinary directed subtour-elimination cuts.  The physical lift is
one primitive cycle exactly when its quotient cycle has nonzero voltage:

\[
 \sum_{u,v,d}d\,p_{uvd}=17z+r,\qquad r\in\{1,\ldots,16\}. \tag{4.2}
\]

Rows (3.4) destroy every old short run but do not prevent new short runs.  For
an integer incumbent, reconstruct the literal 24,310-owner lift.  A positive
run of length `ell` is bracketed by a zero at each end and therefore uses the
full zero-to-zero span of `j=ell+1` selected phase-labelled transitions
`e_1,...,e_j`.  Add

\[
                       \sum_{i=1}^j x_{e_i}\le j-1.      \tag{4.3}
\]

Retaining that entire path retains the bad run, so (4.3) is sound.  All cuts
must be accumulated.  Repeating (4.1) and (4.3) gives a finite exact
CEGAR/branch-and-cut procedure.  Only
after a q1-safe, one-cycle, nonzero-voltage, resident factor is obtained may
the rank-11/12 trim oracle and terminal compiler be run.

## 5. Complexity and the tractable face

The generalized exact problem is NP-complete even after deleting the q1,
span and residence rows and making voltage automatic: an arbitrary directed
graph can be represented by allowing `u -> f_v` exactly for its arcs.  The
matching core gives a directed cycle cover and (4.1) asks for a Hamilton
cycle.  This is a family-level reduction, not an atlas-specific hardness
claim for candidate1911.

The proof-safe polynomial core remains useful:

- (2.1) alone is min-cost bipartite matching;
- fractional subtour cuts separate by directed min-cut;
- integer subtours separate by strongly connected components;
- Lagrangian relaxation of q1/span rows returns to min-cost matching;
- the 16 voltage residues can be encoded by explicit finite branching, but
  this does not turn the remaining q1/topology problem into ordinary
  min-cost matching.

Thus the exact next execution is an assignment master with literal q1 and
256 old-run rows, followed by lazy topology and physical-residence cuts.  It
contains every fixed-`H`, arbitrary-`D` terminal, including every product of
one-shore `D` assignment circuits, and does not duplicate the earlier
provider-rooted support-at-most-ten DFS.  It does **not** contain a shell that
changes `H` as well as `D`; simultaneous `H+D` moves remain outside this
master.

The hardened staged separator replays direct owner/facet matching, both q1
predicates and every authenticated span row before it separates topology,
voltage or new residence defects.  It still cannot infer which cumulative
CNF produced an arbitrary solver transcript.  A proof-safe execution must
therefore retain and hash-bind the factor (`c082621d...`), span table
(`daa15269...`), variable map, exact base-plus-cumulative CNF, and solver
transcript.  Each emitted cut file contains only the newly separated clauses
and must be merged into the base with a corrected DIMACS header before the
next solve.

## 6. Nonflat scope boundary

Changing only source letters, compiler cells, a global gauge, or the opening
cannot change a retained four-owner `0,1,1,0` path.  A phase loop changes the
signed phase increment and is already counted by `w_p=1` at that tail.

One literal escape from the one-copy factor is an occurrence split,
for example replacing `A,B,C,D` by `A,B,B,C,D`.  After contraction it looks
transition-transparent, but it is not the same occurrence-labelled factor.
One stutter raises a physical length-two run only to length three; two are
needed for the required length four.  Across the 67 disjoint quotient orbits
this costs at least

\[
                 67\cdot17=1139
\]

extra physical occurrences merely to leave length two, and at least

\[
                 2\cdot67\cdot17=2278
\]

for the depth-three run floor before any boundary exemption.  These bounds
apply to repeated-owner stutter insertion that preserves the old path system;
they are not lower bounds for arbitrary occurrence replacement, nonflat
compilation, or another occurrence-changing actuator.  This particular
stutter route is therefore not a bounded sidecar.  Any retimed stutter also
needs fresh lower-q1,
upper-witness and common-cap replay; none is inherited automatically from the
flat candidate1911 ledger.

## 7. Audited executable formulations

Three occurrence-labelled implementations now realize the fixed-`H` static
gate.  They all bind the authenticated factor and short-run coordinate system;
none changes `H`.

1. `build_l_k17_candidate1911_fixedH_D_master_20260802.cpp` emits either a
   sequential exactly-one CNF (31,460 variables, 62,602 clauses) or an
   equivalent pairwise CNF (11,440 variables, 85,482 clauses).  Its hardened
   separator replays owner/facet matching, both q1 predicates and all 256
   authenticated old-span rows before separating quotient subtours, zero
   voltage or newly created physical short runs.  Emitted lazy cuts are
   accumulated by a checked DIMACS merge operation.

2. `solve_l_k17_candidate1911_fixedH_D_matching_dpll_20260802.cpp` is an
   exact matching-oracle DPLL for the static gate.  It uses forced/forbidden
   literal incidences, exact-one and q1/span propagation, residual
   Hopcroft--Karp feasibility, Dulmage--Mendelsohn edge filtering and disjoint
   exhaustive branches.  A node limit returns `UNKNOWN`, never `UNSAT`.

3. `search_l_k17_candidate1911_fixedH_D_assignment_cycles_20260802.cpp` is a
   candidate generator on the full fixed-`H` incidence fibre.  Its move atlas
   includes the eight support-one parallel-incidence phase loops as well as
   support-two, support-three and unrestricted longer alternating assignment
   cycles.  Every move preserves a literal owner/facet perfect matching.  The
   code maintains the exact q1/span objective incrementally, then replays it
   from scratch.  It emits a qualified matching only at objective zero;
   nonzero best tables are labeled
   `CANDIDATE_ONLY_UNKNOWN_NOT_STATIC_WITNESS`.

The master, DPLL, and final assignment-cycle sources were independently
audited.  In particular, `(owner,successor,delta)` is injective on all 11,440
legal choices, so comparing the selected incidence to the old incidence is
equivalent to comparing the full old phase-labelled transition in every span
row.

## 8. Finite status: static gate remains UNKNOWN

The sequential CNF was interrupted without a verdict after 14 minutes 10
seconds of Kissat process time; its partial proof stream is not a certificate.
On the pairwise CNF, Kissat and Cadical each reached an independent 900-second
limit without a verdict.  These are timeouts, not negative evidence.

The exact matching-oracle search then explored 5.8 million DPLL nodes over
seed zero and sixteen deterministic menu orders; branches are disjoint within
each run, while different menu orders may revisit assignments.  Every run ended
`UNKNOWN_NODE_LIMIT`.  No residual perfect-matching failure occurred; the
search recorded zero Hall prunes.  This localizes the observed difficulty to
correlation among q1 and old-span rows rather than raw owner/facet
perfect-matchability, but proves neither feasibility nor infeasibility.

The full-fibre candidate generator did produce a literal large-support escape
from the bounded-shell residence obstruction.  Across 656 million proposed
assignment cycles, every best long run hit all 256 authenticated old short-run
spans.  A checkpointed run had exact static debt 37, and one warm-started run
improved it to

```text
upper rank-10 q1 holes                         13
forbidden lower rank-7 regressions             21
authenticated old-span misses                   0
exact static objective                         34
changed D incidences                          1232
quotient components                              5
smallest quotient component                      7
```

The candidate-only matching is
`anneal_warm32x5m.best_D_matching.tsv`, SHA
`497de28d878bbc7a8a0391af749ee7602b4f948bc4d3a7d7be6db1863161adbf`.
An independent incidence reconstruction verified 1,430 owners and facets
exactly once, zero fixed-`H` collisions, every derived transition/q1 field,
and all 256 span rows.  Its five quotient cycles have `(size,voltage)`

```text
(1257,12), (85,7), (52,9), (29,14), (7,7).
```

This is **not** a static witness: it still has 34 q1 debts and is not one
quotient component.  New physical short runs, a global voltage, ranks 11+,
trim casualties and the compiler were therefore not promoted.

The exact next gate is q1 compensation on this or another zero-span-miss
large-support matching, followed—only after static objective zero—by the lazy
topology, voltage and literal physical-residence separator.  Another bounded
C6/C8 shell cannot address the 67-span obstruction.

## 9. Binding artifacts

```text
fixed-H master source
  64f5d800eb24048f4d5f0f7e85bf328d1df11206aea5b56f854a1f9387af544d
sequential CNF / map
  67012dd88287156b9fb4715571e0dad2b5feb3d16e3f92a8daee3d476fc19e74
  d8ed140e5eba91f29e0cd101e997c1f3df2c5f97e7ba20c8ce1cd20f0919ded1
pairwise CNF / map
  e912734305c1af852f3009825f5fd3a456b11b2a81adf4fa1d764b9161ccf6bc
  2d753b61da0b502bd539905f8c848359c556b2c7a0206183804fa0451f1d4b7c
matching-oracle DPLL source
  a6a01fd77327e888f2692a27f2d0b0a8b45bea74cf9aea9fb1ac59956ef0bf06
one-million-node seed-zero report / audit
  acf62eb417130c052a8bfc8d857ab1ff6d1e9fc253a2421e40a05866c35940e6
  c48925b19cae2a41bb22d035ba01c53d6b06b57816d6f87066dd0ea4a8077941
DPLL portfolio summary
  85622e9fa89d8c8d98a451d14d50db10ed917cabb1025fe0898198547a335f17
full-fibre assignment-cycle source / H100 binary
  89ac041e66e24a3e71704cf942bd1b034b29c5e0cecc811ac6aba4bd5389c3f3
  49b6f87112057e695d478ea09e01835a44c3c1de619065a6b0a0a387b7e4cd82
checkpoint audit / candidate
  c057a2228dcc566d7c0217efe9df6bed92e04ee750a04bbfefdb546962227775
  f408b88bbd51a0c531441987f0de09b38c841fe00afb915ac25bff3779ba878b
warm-start frontier audit / candidate
  0815ed051ffda06617f9de865ea6bb72d7584c3a32cc4ac83e9af24762eb0989
  497de28d878bbc7a8a0391af749ee7602b4f948bc4d3a7d7be6db1863161adbf
one-step exact loader/replay audit
  692464b8eb1c5d42146fa9b3f245e179ca749a39cda3e3abd86dcde4d17bee5b
independent raw frontier-34 replay
  f53b065bdb653c7be5ff1ed42478b790bf76b81d243177d30aa0e1c782c4c84b
```
