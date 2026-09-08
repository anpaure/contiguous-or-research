# Task D: exact q1-factor splice/compiler postprocessor

Date: 2026-07-29

Status: theorem, executable reduction, and bounded runtime audit.  The outer
carrier model and the linear one-core compiler are exact in the scopes stated
below.  All five supplied fixed selectors are rejected.  A positive `k=11`
regression produces and independently verifies an optimal length-465 word.
The retained ten-second `k=15` H100 smoke returned `UNKNOWN`; no length-6438 `k=15`
word is claimed.

The executable is

```text
scratch/threadD_k15_splice_compiler_postprocessor.py
```

with solver-free regressions in

```text
scratch/test_threadD_k15_splice_compiler_postprocessor.py.
```

## 1. Verdict

The q1 cycle-cover splice theorem now has a literal postprocessor with two
strictly separated levels.

1. The **carrier level** chooses one catalogue edge at every lower owner,
   orients the choices as one quotient circuit, imposes unit voltage,
   residence, and upper q1 eagerly, and separates the remaining shadows by
   exact CEGAR.
2. The **compiler level** opens a completed physical Hamilton chronology at
   an upper-safe edge and solves the exact physical target-to-position
   matching coupled to one common erosion antecedent.  It can either maximize
   the number of matched lower targets or require every target and emit a
   word of length

   \[
      W+d={15\choose8}+3=6438.
   \]

At upper depth `q>=3`, the implementation has exactly one separator: the
accumulated-union reachability automaton.  It contains no fixed `q`-edge
upper witness and no legacy upper-q3 motif.

Fixed-selector failure, bounded-radius factor-search failure, and
fixed-opening compiler failure are different statements.  The executable
records these scopes separately and never promotes a Hall failure for one
compiler opening to a generic carrier cut.

When the optional whole-carrier exclusions are enabled, each stored row
contains its source round, all directed arc IDs, an arc-list hash, the full
compiler-audit hash, and the exhaustive opening status.  Any eventual UNSAT
record also serializes both minimum and maximum owner-distance restrictions.

## 2. Frozen input audit

All files contain exactly 429 distinct choices, one per lower owner, and are
q1-complete.  The exact audit is

```text
scratch/threadD_k15_q1factor_snapshot_audit_20260729.json.
```

Here `Q` is the number of quotient components, `P` the number of physical
cycles, `R` the number of residence violations, and `L2,L3,U2,U3` the
numbers of missing target orbits at the indicated depths.

| label | SHA-256 prefix | quotient `(size,voltage,gcd)` | P | R | L2 | L3 | U2 | U3 |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| d83 | `75b52aab` | `(429,0,15)` | 15 | 765 | 52 | 19 | 18 | 2 |
| d86 | `6e38e638` | `(403,5,5),(18,13,1),(8,4,1)` | 7 | 1125 | 53 | 25 | 18 | 2 |
| d92 | `0df27609` | `(416,6,3),(13,8,1)` | 4 | 1080 | 57 | 20 | 16 | 1 |
| d93 | `76a83f01` | `(429,7,1)` | 1 | 1050 | 56 | 22 | 16 | 1 |
| d94 | `d0964d71` | `(429,10,5)` | 5 | 1050 | 57 | 21 | 16 | 1 |

Every upper depth from q4 through q7 has zero holes in these factors.  The
physical cycle lengths are respectively

```text
d83: 15 x 429
d86: 5 x 1209, 270, 120
d92: 3 x 2080, 195
d93: 6435
d94: 5 x 1287.
```

The file called `d83` declares `choice_changes=82`; the name is a historical
centre label, not its literal Hamming distance.  More importantly, the word
`resident` in its filename is not a current certificate: exact validation
finds 765 residence violations.

Thus orientation or cyclic cutting alone cannot repair any frozen selector.
The d93 selector is already a unit-voltage physical Hamilton cycle, but it
still fails residence and deeper shadows.  A successful result must replace
owner choices.

## 3. Exact implicit cut/orient/splice master

Let `C` be the strict quotient choice catalogue.  Each choice `e` has one
lower-owner colour and two directed darts `a,bar(a)`.  Use binaries `x_e`
and `y_a`.  The master imposes

\[
  \sum_{e:c(e)=S}x_e=1                         \tag{3.1}
\]

for every lower owner `S`, exact choice/dart linking

\[
  x_e=\max(y_a,y_{\bar a}),\qquad
  y_a+y_{\bar a}\le1,                         \tag{3.2}
\]

and one incoming and outgoing selected dart at every quotient root.  A
literal `AddCircuit` row eliminates every proper directed subtour.  If
`alpha(a)` is the dart voltage, the total voltage satisfies

\[
 \gcd\!\left(\sum_a\alpha(a)y_a\pmod {15},15\right)=1. \tag{3.3}
\]

The exact age automaton forbids a positive coordinate run of length at most
`d=3`, and the q1 upper clauses require every rank-nine orbit.

Fix a baseline factor `F0`.  A changed owner is precisely an old choice
`e in F0` with `x_e=0`; (3.1) supplies precisely one replacement seam at
that owner.  Except for the unchanged one-cycle case, the common graph
`F0 intersect F` consists of the retained path pieces.  Equations
(3.1)--(3.3) and `AddCircuit` orient those pieces and join them into the
final circuit.  Conversely, every legal literal cut,
orientation, and splice supplies exactly this variable assignment.  Hence
the directed master is an exact implicit version of the explicit path-port
theorem; it does not need to enumerate all segment orientations in advance.

For a baseline with several quotient components the implementation adds the
redundant but useful row that at least one old choice is cut in every old
component.  Optional rows hit the closed edge span of every old short
coordinate run.  Hamming radius is exact because both old and new selectors
contain one choice at each of the same 429 owners:

\[
  \operatorname{dist}(F,F_0)\le R
  \quad\Longleftrightarrow\quad
  \sum_{e\in F_0}x_e\ge429-R.                 \tag{3.4}
\]

### Theorem 3.1 (splice equivalence)

An integral solution of the owner, dart, degree, `AddCircuit`, and unit-
voltage rows is exactly a strict equivariant owner-perfect physical
Hamilton cycle in the supplied catalogue.  Relative to `F0`, its deleted
and inserted choices are exactly the cut and seam sets, with equal
cardinality owner by owner.

#### Proof

Equation (3.1) is exact ownership.  Equation (3.2) chooses one orientation
of each used undirected choice.  `AddCircuit` gives one spanning directed
quotient cycle.  Contracting the common `F0 intersect F` pieces recovers the
explicit oriented splice.  The cyclic voltage lift has exactly
`gcd(v,15)` physical components, so (3.3) is equivalent to one physical
cycle.  Reversing the construction proves surjectivity.  QED.

## 4. Exact shadow CEGAR

Lower q2 and q3 use the consecutive Johnson-path intersection automata.
Upper q2 uses its exact two-step union automaton.  These fixed-length rows
are valid because those particular witnesses have the corresponding exact
length.

For an upper target `T` of depth `q>=3`, define a state

\[
             (U,X),                            \tag{4.1}
\]

where `X` is the current rank-eight carrier state contained in `T` and `U`
is the union accumulated since an arbitrary interval start.  A selected
physical Johnson dart `X->X'` advances

\[
             (U,X)\longmapsto(U\cup X',X').    \tag{4.2}
\]

Every central `X subset T` is an initial state.  Acceptance is `U=T`.
Therefore acceptance is equivalent to an arbitrary-length contiguous
carrier interval with union exactly `T`.

If the current selected darts do not accept, let `R_T` be their reachable
state set and let `delta(R_T)` be the distinct catalogue darts leaving it.
Then

\[
             \bigvee_{a\in\delta(R_T)}y_a      \tag{4.3}
\]

is a valid separating row and the incumbent violates it.  Every future
accepting path must cross this boundary.  Repeating (4.3) is finite and
exact because the state graph is finite.

### Theorem 4.1 (unrestricted-upper completeness)

When the CEGAR loop terminates with no missing target, the selected carrier
covers every required upper target by a literal contiguous interval.  If
the finite master becomes infeasible after all generated rows, that
infeasibility is exact in the declared catalogue/radius scope.  At no point
is an upper `q>=3` target restricted to `q` edges.

The cut ledger records every fixed state-path key and stores the full arc
list plus hash of every accumulated-union boundary, so an eventual outer
certificate can be replayed without regenerating the separators.  Fixed
q2/q3 state paths and unrestricted upper boundaries have different keys and
cannot be silently interchanged.

## 5. Exact linear one-core compiler

Let a validated physical carrier be

\[
       T=(T_0,\ldots,T_{W-1}),\qquad W=6435,\quad d=3.
\]

Choose a carrier edge whose removal leaves at least one noncrossing witness
for every upper target.  Rotate after that edge and form the maximal linear
antecedent

\[
 P_j=\bigcap_{\max(0,j-d)\le i\le\min(W-1,j)}T_i,
 \qquad 0\le j<W+d.                            \tag{5.1}
\]

Residence gives

\[
                  D^dP=T.                      \tag{5.2}
\]

The compiler assigns lower targets injectively to the `W+d` positions.  Its
literal family consists of

* every nonempty target of rank at most `h=5`; and
* every target of rank `6` or `7` which is absent from the fixed positive
  derivative rows `DP,D^2P`.

The second bullet is the necessary graded endpoint correction.  A higher
target already present in `DP` or `D^2P` needs no source literal; a target
absent there must be placed literally in the source row.  Omitting this
family produced a false first k11 smoke and is now covered by a regression.

For each target `S` and source position `p` with `S subset P_p`, let
`f_(S,p)` be binary.  Impose

\[
 \sum_pf_{S,p}=1,
 \qquad
 \sum_Sf_{S,p}\le1.                           \tag{5.3}
\]

If `S` is assigned at `p`, put `A_p=S`; otherwise put `A_p=P_p`.  Define the
omission indicator

\[
 o_{p,x}=\sum_{S:x\in P_p\setminus S}f_{S,p}.           \tag{5.4}
\]

It remains to require `DA=DP`.  For every adjacent pair and coordinate in
`P_p union P_(p+1)`, the exact omission row is

\[
 o_{p,x}+o_{p+1,x}
 \le {\mathbf 1}_{x\in P_p\cap P_{p+1}}.                \tag{5.5}
\]

Only existing incidence variables occur in these sums.

### Theorem 5.1 (eliminated one-core equivalence)

Equations (5.3)--(5.5) are feasible if and only if this fixed opening admits
a common one-core `A subset P`, with `DA=DP`, and an injective occurrence
assignment for every required literal target.  A feasible all-target
solution is an exact universal OR word of length `W+d`.

#### Proof

An unassigned position equals `P_p`; an assigned position omits exactly the
coordinates of `P_p minus S`.  Thus (5.5) says precisely that no coordinate
present in `P_p union P_(p+1)` is omitted at both positions.  Since
`A subset P`, this is equivalent coordinatewise to `DA=DP`.  Hence

\[
 D^dA=D^{d-1}(DA)=D^{d-1}(DP)=D^dP=T.           \tag{5.6}
\]

Ranks at most five occur literally by (5.3).  Ranks six and seven either
occur in a fixed positive derivative row or belong to the residual literal
family.  Rank eight is the exact Hamilton middle row.  Every upper carrier
witness remains inside the opened chronology; expanding its middle interval
through (5.6) gives a source interval with the same union.  Thus every
nonempty mask occurs as a contiguous OR.  The reverse construction reads
the literal assignments from any one-core solution.  QED.

Before CP-SAT, ordinary bipartite matching supplies an exact necessary Hall
certificate for the target-position incidence graph.  Passing this Hall
test is not sufficient because (5.5) couples adjacent assignments.  The
CP-SAT system is the exact conflict layer.

With `--score`, (5.3) becomes at-most-one on the target side and the model
maximizes `sum f_(S,p)`.  Since the residual target family varies with the
opening, openings are compared by

\[
  \operatorname{def}(P)
  =|\mathcal F(P)|-\max\sum_{S,p}f_{S,p},               \tag{5.7}
\]

not by the raw objective.  An `OPTIMAL` opening result gives its exact
deficiency.  The best score is exact over all upper-safe openings only if all
of them were tested optimally.  A time-limited or truncated opening scan is
labelled `BOUNDED`, never `OPTIMAL`.

## 6. Certificate scopes

The program uses the following noninterchangeable statuses.

* `FIXED_FACTOR_REJECTED`: exact for the supplied owner choices and component
  reversals only.  It says nothing about owner replacement.
* `SPLICE_SEARCH_RELAXATION_INFEASIBLE`: exact only for the printed catalogue,
  Hamming radius, and currently installed exact constraints.  An `UNKNOWN`
  or `MAX_ROUNDS` status is not a certificate.
* `FIXED_OPENING_HALL_INFEASIBLE`: exact for one directed carrier and one
  opening, before adjacent omission conflicts.
* `FIXED_OPENING_ADAPTIVE_CORE_INFEASIBLE`: exact for that carrier/opening in
  the linear one-core architecture.
* `ALL_SAFE_OPENINGS_COMPILER_INFEASIBLE`: exact for the fixed directed
  carrier in the upper-safe linear adaptive-one-core architecture, only
  after every safe opening has been solved conclusively.
* `VERIFIED_OPTIMAL`: a stored length-`W+d` word passed the independent
  exhaustive verifier, including the exact middle row.

Compiler failures are not converted to local outer-master cuts.  With the
explicit `--exclude-compiler-failures` option, only a completely exhausted
fixed directed carrier may receive a whole-directed-carrier nogood.  A
sampled core, one failed opening, or an incomplete solve never yields such a
nogood.

## 7. Regressions and runtime audit

### Solver-free local tests

The local regression performs no SAT search.  It checks all five frozen
factor counts, stable hashes, orientation reconstruction, old-run cut rows,
the d83 naming mismatch, and the k11 linear-envelope/Hall front.

```text
python3 -m py_compile \
  scratch/threadD_k15_splice_compiler_postprocessor.py \
  scratch/test_threadD_k15_splice_compiler_postprocessor.py
python3 scratch/test_threadD_k15_splice_compiler_postprocessor.py

PASS threadD splice/compiler solver-free regressions
```

For the k11 fixture, the first safe opening has envelope ranks

```text
3^459, 4^2, 5^2, 6^2.
```

The base literal family has 231 targets and 3,373 incidences.  The exact
graded correction adds masks `57,61`, producing 233 targets and 3,378
incidences.

### H100 positive compiler smoke

Using OR-Tools `9.15.6755` through `PYTHONPATH=/dev/shm/orlib`, the first
safe k11 opening solved on H100 CPU with

```text
3,378 variables
2,560 constraints
1,862 adjacent-omission rows
0.096 solver seconds
0.656 total compiler seconds.
```

The emitted 465-letter word has SHA-256

```text
137973ee940f063921ee9ab6eb75fc46b01d5ab27a873e7836ad70c94e6e7151.
```

An independent local verifier found all 2,047 nonempty masks, exact middle
width 462, and `middle_row_exact=true`.  The score-mode smoke independently
returned objective 233 and bound 233 for that opening.  A second H100
regression inserted one deliberately impossible target: ordinary Hall then
matched only 233 of 234, while partial score mode correctly solved past that
failure and returned the exact optimum 233 and deficiency one.

### Bounded k15 construction smoke

The outer master was run on H100 for one round around d93 with
radius 120, overlap maximization, and its 70 old-run rows.  Model construction
gave

```text
46,292 variables
456,763 constraints
10.430 solver seconds
13.142 total seconds
status UNKNOWN.
```

The unconstrained base count is 456,692 constraints; the smoke adds one
radius row and 70 run rows.  No candidate was returned, no CEGAR boundary was
added, and no compiler was invoked.  This run is solely an executable/model-
size regression and proves neither feasibility nor infeasibility of the
radius-120 neighborhood.

## 8. Artifacts and hashes

```text
4004f01c...  scratch/threadD_k15_splice_compiler_postprocessor.py
ff6d4886...  scratch/test_threadD_k15_splice_compiler_postprocessor.py
91d38fc6...  scratch/test_threadD_splice_compiler_score_ortools.py
b921b327...  scratch/threadD_k15_q1factor_snapshot_audit_20260729.json
a70a36f2...  scratch/threadD_k11_exact_compiler_smoke_20260729.audit.json
ac29541c...  scratch/threadD_k11_exact_compiler_score_smoke_20260729.audit.json
aca9bb3d...  scratch/threadD_k11_hall_deficient_score_regression_20260729.audit.json
137973ee...  scratch/threadD_k11_exact_compiler_smoke_20260729.word
2f4ee5bf...  scratch/threadD_k15_d93_radius120_h100_smoke_20260729.audit.json
```

The bounded k15 audit is

```text
scratch/threadD_k15_d93_radius120_h100_smoke_20260729.audit.json.
```

The executable imports the repo-owned exact catalogue and carrier master
from `scratch/graded_quotient_pipeline.py`, but it does not modify that file.

## 9. Reproduction boundary

Lightweight local audit:

```text
python3 scratch/threadD_k15_splice_compiler_postprocessor.py audit \
  d83 d86 d92 d93 d94 \
  --output scratch/threadD_k15_q1factor_snapshot_audit_20260729.json
```

Heavy carrier search belongs on H100 CPU:

```text
ssh -o ClearAllForwardings=yes h100 \
  'cd /dev/shm/k15_rotation/threadD_splice_postprocessor_20260729 && \
   PYTHONPATH=/dev/shm/orlib python3 \
   scratch/threadD_k15_splice_compiler_postprocessor.py search d93 \
   --output candidate.audit.json --word candidate.word \
   --radius 120 --max-rounds 500 --timeout 3600 \
   --compiler-timeout 3600 --workers 8 \
   --add-run-cut-rows --maximize-overlap'
```

For a carrier which already passes residence and every shadow:

```text
PYTHONPATH=/dev/shm/orlib python3 \
  scratch/threadD_k15_splice_compiler_postprocessor.py compile carrier.json \
  --output compiler.audit.json --word candidate.word
```

Replace `--word candidate.word` by `--score` to optimize the compiler score
without emitting a word.

## 10. Sharp remaining gate

The missing result is no longer a formulation.  It is an integral existence
or search result for the outer strict catalogue master which simultaneously
passes residence, the lower q2/q3 paths, upper q2, and every unrestricted
upper accumulated-union automaton, followed by a feasible linear one-core
opening.  None of d83, d86, d92, d93, or d94 is such a carrier without owner
replacement.  The present iteration supplies the exact postprocessor and
certificate boundary, but not the `k=15` carrier or a length-6438 word.
