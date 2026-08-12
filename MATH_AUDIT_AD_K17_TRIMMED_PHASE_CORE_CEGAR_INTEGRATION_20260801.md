# `k=17`: exact 3-trimmed phase-core CEGAR on the incidence-bimatching master

Date: 2026-08-01  
Lane: AD, independent integration audit  
Status: exact reduction, clause schema, and solver-free index audit.  No new
incidence Hamilton cycle, upper-safe root, compiler, or `k=17` word is
claimed.

## 0. Outcome and exact scope

The `21,778` physical targets of ranks `11,...,17` need not be represented
by eager target automata in the current `k=17` incidence-bimatching master.
The smallest proof-safe integration is:

1. keep the `1144` rank-ten orbit-cover rows eager;
2. select the two incidence perfect matchings and certify one primitive-
   voltage quotient Hamilton cycle;
3. reconstruct its literal `17*1430=24310`-owner helical lift;
4. test all `1430` normalized physical roots with the exact first-arrival
   oracle; and
5. either emit a guarded incumbent no-good, or accept one root with an
   independently replayable rank-`11,...,16` certificate of at most
   `2633` normalized witness rows.  Rank seventeen is automatic.

The previously proved `4921` cap includes rank ten.  Once rank ten is
handled by the exact multiplicity rule, the genuine higher-shadow part is

\[
 2(728+364+140)+3(40)+5(8)+9(1)=2633.              \tag{0.1}
\]

The current AD J7 SAT artifact is not an ordered chronology: it is a forest
of `4680` literal blocks.  Therefore it has no physical opening root and the
phase-core oracle is not applicable to it.  Its exact internal higher holes
remain

\[
                    (1350,777,151,5,0,0,0).         \tag{0.2}
\]

The saved strict MMM spiral is an actual chronology, but it fails the eager
rank-ten gate by `148` quotient colour orbits.  It is therefore rejected
before any rank-`11+` row is generated.

## 1. Source trimming and the offset-three owner formulation

Let the cyclic source letters be `A_i`, indexed modulo `W`, and put

\[
                       T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}. \tag{1.1}
\]

Cut immediately before `A_c` and form

\[
 A_c,A_{c+1},\ldots,A_{c+W-1},A_c,A_{c+1},A_{c+2}. \tag{1.2}
\]

The owner windows of (1.2) are

\[
                         T_c,T_{c+1},\ldots,T_{c-1}. \tag{1.3}
\]

Thus the source cut `epsilon_c` immediately before `A_c` deletes the owner
edge

\[
                         e_{c-1}:T_{c-1}\longrightarrow T_c.       \tag{1.4}
\]

### Theorem 1.1 (trim/owner identity)

For every cyclic source interval

\[
                         J=[A_a,\ldots,A_{b+3}]                    \tag{1.5}
\]

of length at least four, let `I=[T_a,...,T_b]` be its associated owner
interval.  Then

\[
  \{e_{c-1}:\epsilon_c\in\operatorname{int}_3(J)\}
                    =\operatorname{int}(I).                         \tag{1.6}
\]

Consequently the exact 3-trimmed source opening test is identical to the
ordinary nonwrapping owner-edge test after applying (1.4).

#### Proof

Unroll (1.5).  A source edge `epsilon_t` lies in its interior and has more
than three interval vertices after it exactly for

\[
                              a+1\le t\le b.                        \tag{1.7}
\]

After the shift `e_(t-1)`, these are precisely
`e_a,...,e_(b-1)`, the interior edges of `I`.  This proves (1.6).
Every source interval of rank greater than nine has length at least four,
and its OR equals the OR of its owner windows.  Hence (1.6) covers the
complete strict-upper source deck.  QED

This reconciles the two existing formulations.  An **ordinary source-edge**
crossing core would be too strong.  An ordinary **owner-edge** core is exact,
provided the offset (1.4) is not dropped.

The literal age source uses a second, shifted notation.  If its emitted
age-zero letters are `P_i=C_(i,0)`, then propagation gives

\[
                     T_i=P_{i-3}\cup P_{i-2}\cup P_{i-1}\cup P_i,
                     \qquad A_i=P_{i-3}.                           \tag{1.8}
\]

Consequently owner dart `T_i->T_(i+1)` is the source cut before
`A_(i+1)=P_(i-2)`.  If the first owner after opening is `T_r`, the emitted
source starts at `P_(r-3)` and the deleted owner dart is
`T_(r-1)->T_r`.  A physical certificate must record the owner dart and the
emitted-`P` start separately; the formula “cut before `P_c` means dart
`c-1`” is false by three positions.

## 2. Phase sign and the helical root

Fix quotient edge orbit `i`; write `e_i^g` for its physical copy in phase
`g`.  If a normalized witness `I` contains phases `g` of this edge, define

\[
 P_i(I)=\{-g:e_i^g\in\operatorname{int}(I)\}.       \tag{2.1}
\]

For the source formulation, replace `int(I)` in (2.1) by `int_3(J)` and use
the offset (1.4).

### Lemma 2.1 (sign audit)

The minus sign in (2.1) is necessary and sufficient: rotating the witness
by phase `p` makes an edge of phase `g` cross the normalized phase-zero cut
exactly when

\[
                              g+p=0\pmod {17}.       \tag{2.2}
\]

Thus `p=-g`, as in (2.1).  QED

Selecting quotient root index `i` removes only `e_i^0`.  The other sixteen
physical copies of edge orbit `i` remain and join the seventeen quotient
laps into one opened helical path.  In particular, neither incidence
matching variable at quotient position `i` may be set to zero merely because
`i` is the root.  Doing that removes the entire orbit, namely seventeen
physical edges, and is not an admissible strengthening.

## 3. Exact first-arrival phase-core oracle

Let selected incidence matchings `D,H` induce an oriented quotient order
`O_0,...,O_(N-1)` and labelled quotient voltages `v_i`.  Put

\[
 p_0=0,\qquad p_{i+1}=p_i+v_i,\qquad V=p_N\pmod {17}.              \tag{3.1}
\]

After rejecting `V=0`, reconstruct the physical cycle

\[
                 T_{qN+i}=\rho^{qV+p_i}T_{O_i},
                 \qquad 0\le q<17.                                \tag{3.2}
\]

For each physical start `a` and each of the eight coordinates outside
`T_a`, record its first future arrival before `a+W`.  Sort the at most eight
arrival positions and add all coordinates tied at each position.  The
resulting at most eight owner intervals are exactly the first-growth,
undominated interval-OR witnesses from `a`.

For every quotient root orbit choose its unique physical phase-zero copy.
For a witness owner interval `[a,b]`, mark precisely those roots whose
physical cut edge is outside `[a,b)`.  By Theorem 1.1 this is also the exact
3-trimmed source survival set.  OR these survival bits over all witnesses
with the same physical target.  The root is higher-safe exactly when every
rank-`11,...,16` target bit is set.  The full rank-seventeen target is
witnessed by the whole opened source period.

The oracle uses at most `8W=194480` first-growth events.  A dense
`21778 x 1430` survival table costs `3,892,818` bytes before word padding,
or `4,007,152` bytes with 23 64-bit words per target; equivalently it may be
streamed rootwise.  No target-state variables are required in the incidence
master.

### Theorem 3.1 (certificate cap)

Fix a root that the oracle accepts.  A rank-`s<17` witness contains at most
`binom(s,9)` distinct owners, so it meets a fixed quotient edge orbit in at
most

\[
 b_s=\left\lceil {\binom{s}{9}-1\over1430}\right\rceil            \tag{3.3}
\]

physical phases.  For `s=10,...,16`, these values are

\[
                           1,1,1,1,2,4,8.                          \tag{3.4}
\]

For one target orbit, take any normalized witness `I_0`.  If its crossing
mask is empty, it alone certifies survival.  Otherwise, for every phase in
`P_i(I_0)`, choose one witness omitting that phase.  At most `b_s+1` rows
then have empty mask intersection.  Summing gives `4921` rows for ranks
ten through sixteen and, after the separate rank-ten rows, exactly the
`2633` cap (0.1) for ranks eleven through sixteen.  QED

An accepted certificate row records:

```text
rank, normalized target representative,
physical start (quotient slot, lap), physical endpoint,
target-normalizing phase, root quotient slot,
17-bit trimmed crossing mask.
```

The verifier reconstructs (3.2), checks the literal interval OR, checks the
mask using either source `int_3` or the shifted owner interior, and checks
that each target-orbit bank has empty intersection.  These semantic rows,
together with a DRAT proof for the emitted CNF, give a proof-producing CEGAR
certificate without encoding the automata eagerly.

The frozen machine-readable field contract is

```text
scratch/ad_k17_trimmed_phase_core_certificate_schema_20260801.tsv
```

## 4. Exact rank-ten rows on incidence variables

At a quotient facet `F`, a selected outgoing incidence `d` and selected head
incidence `h` determine a turn atom

\[
                            z_{d,h}=D_d\wedge H_h.                  \tag{4.1}
\]

The atom may be channelled by the usual three CNF clauses.  Let `c(d,h)` be
the rank-ten target orbit of the two physical rank-nine endpoints.  Cyclic
rank-ten completeness is exactly

\[
                 \bigvee_{(d,h):c(d,h)=U}z_{d,h}
                    \qquad (U\text{ a rank-ten orbit}).            \tag{4.2}
\]

There are `1144` rows (4.2).  Suppose `r_i` chooses quotient slot `i` as the
normalized physical root.  For every possible turn `t` at slot `i`, exact
rank-ten opening safety is

\[
 \boxed{\neg r_i\ \vee\ \neg z_t\ \vee
        \bigvee_{t'\ne t:\ c(t')=c(t)}z_{t'}.}                     \tag{4.3}
\]

Indeed, if `r_i=z_t=1`, the cut deletes one physical occurrence of each
target in that orbit phase.  A different selected quotient turn of the same
colour orbit supplies every phase once more.  Conversely, every rank-ten
owner witness contains a rank-ten-coloured Johnson edge, so a uniquely
provided cut colour has no alternative longer witness.

If opening variables `o_t` are attached directly to labelled selected turn
occurrences, (4.3) is the smaller inequality

\[
                          o_t\le
                 \sum_{t'\ne t:c(t')=c(t)}z_{t'}.                  \tag{4.4}
\]

The smallest master may omit root variables entirely: solve the unrooted
factor, compute the multiplicities, and retain as candidate roots exactly
the selected turns whose colour multiplicity is at least two.  Requiring
every colour orbit to have multiplicity at least two is strictly stronger
than existence of one safe root and is not WLOG.

### Actual unordered incidence-factor host

The current compact K host does not materialize `D,H`.  It selects one
degree-two incidence factor with variables `x_e` and has one unordered
facet-turn atom

\[
                             z_{e,f}=x_e\wedge x_f                 \tag{4.5}
\]

for each of `1430*binom(9,2)=51480` pairs.  The usual three clauses make
(4.5) exact.  Exactly eight such pairs are quotient loops and are forbidden.
For each of the `51472` nonloop turns introduce an opening atom `o_t`.  The
exact companion rows are

\[
 o_t\longrightarrow z_t,
 \qquad
 o_t\longrightarrow\bigvee_{t'\ne t:c(t')=c(t)}z_{t'},           \tag{4.6}
\]

together with exactly one `o_t`.  With a Sinz one-hot encoding this adds

\[
 51472+51471=102943\text{ variables},\qquad
 8+2(51472)+(3(51472)-3)=257365\text{ clauses}.                    \tag{4.7}
\]

The host's `1144` rank-ten ALO rows remain required.  This is the literal
unordered-factor version of (4.2)--(4.4), not an additional `D/H` model.

## 5. Lazy clauses over the bimatching/root master

If a complete family of witness atoms `w_I` is explicitly channelled to the
incidence order, then the exact target-phase row is

\[
 \neg r_i\ \vee
 \bigvee_{I:\operatorname{OR}(I)=U,\ p\notin P_i(I)} w_I .        \tag{5.1}
\]

This is exact but needlessly introduces the interval bank.  The two
variable-free separation forms below keep those atoms outside the master.

### 5.1 Smallest always-sound incumbent clause

Let `(D^*,H^*)` be a selected oriented incidence Hamilton cycle.  If a fixed
root `r_i` fails, the clause

\[
 \neg r_i\ \vee
 \bigvee_{d:D_d^*=1}\neg D_d\ \vee
 \bigvee_{h:H_h^*=1}\neg H_h                              \tag{5.2}
\]

is sound and incumbent-violated.  Fixing all `2N=2860` selected matching
incidences fixes the labelled successor cycle and all voltages, hence fixes
the failed physical opening.  If all `1430` roots fail, the root literal may
be omitted.  This is coarse but requires no interval variables and is the
recommended first proof-producing CEGAR row.

### 5.2 Stronger labelled-DFA frontier clause

For one missed physical target `U`, build states `(T,M)`, where `T subset U`
is a physical rank-nine owner and `M` is the nonempty part of `U` not yet
seen by the current compatible suffix.  A selected physical dart
`a:T->T'` with `T' subset U` sends

\[
                          (T,M)\longmapsto(T',M-T').                \tag{5.3}
\]

All compatible owners are possible starts; a state with empty missing set
is accepting.  The phase-zero root dart is suppressed, while its other
sixteen copies remain.

For an incumbent miss, let `R` be the reachable state set.  For every
candidate transition leaving `R`, choose one activation literal false in
the incumbent: an unselected required incidence literal, or `not r_i` for
the selected suppressed root transition.  Deduplicate the chosen blockers
into `B`.  Then

\[
                              \bigvee_{b\in B} b                   \tag{5.4}
\]

is valid.  Every accepting path must leave `R`; activating that frontier
transition forces its chosen blocker.  A certificate consists of the closed
reachable set and, after greedy minimization, one restoring accepting path
per retained blocker.  This is exactly the labelled-frontier proof rule;
it is stronger than (5.2) but should be generated only for misses actually
encountered.

For the actual unordered host, let `S^*` be its `2N` selected incidence
variables.  Replace the two matching guards in (5.2) by

\[
                              \bigvee_{e\in S^*}\neg x_e.         \tag{5.5}
\]

If all roots are audited simultaneously, the exact guarded row for one
higher target orbit `U` is

\[
 \left(\bigvee_{e\in S^*}\neg x_e\right)
 \vee
 \left(\bigvee_{t\in T(S^*):\ L_t(U)=\varnothing}o_t\right).      \tag{5.6}
\]

Here `T(S^*)` is the selected turn set; in the second disjunction, `t`
ranges over those turns whose
lost-phase core for `U` is empty.  Under the exact-one opening rows, the
family (5.6) forces one root safe for every orbit while the factor is
unchanged.  It is generally stronger than one whole-factor no-good and uses
no interval variables.

## 6. Regression boundary

The authenticated J7/q1 assignment decoded in
`scratch/ad_k17_j7_higher_shadow_cegar_20260801/` partitions all owners into
`4680` blocks.  It does not select their order, orientations at every free
boundary, connector words, a primitive monodromy, or a root.  Therefore a
rank-`11+` miss cannot soundly be projected from that artifact to the
incidence/root master.  Its internal replay (0.2) is a chronology-master
obligation only.

The strict MMM quotient cycle is a valid helical-oracle regression, but its
rank-ten quotient deck omits `148` of `1144` orbits.  The proper CEGAR order
rejects it by (4.2); reporting a deeper-opening outcome for it as if q1 had
passed would be misleading.

No SAT incidence-bimatching chronology satisfying the fixed age/deletion-
spine rows is presently frozen.  Thus the phase-core integration is exact
and executable, but its first positive incumbent test remains pending such
a chronology.

The existing O3 implementation

```text
scratch/audit_ad_k17_age_skeleton_upper_opening_cegar_20260801.cpp
```

already carries out the first-arrival scan and emits the whole-incumbent
no-good for the older directed-dart variable model.  It opens an ordinary
owner edge; by Theorem 1.1 this is exactly the 3-trimmed source test, with
the source root shifted by one position.  Porting it to the incidence
bimatching master requires only replacing each selected dart literal in the
incumbent guard by its selected `D` and `H` incidences, and moving rank ten
to (4.2)--(4.4).  No new rank-`11+` state variables are required.

## 7. Independent lightweight audit

The solver-free checker

```text
scratch/audit_ad_k17_trimmed_phase_core_integration_20260801.py
```

exhaustively verifies (1.6) for all cyclic intervals of lengths at least four
in periods `4,...,40`, verifies both the theorem-`A` and emitted-`P` cut
offsets, verifies the sign (2.2) in all `17^2` cases, checks the
orbit/crossing table and the constants `21778`, `4921`, and `2633`, and
replays the exact J7 forest scope.  Its output is

```text
scratch/ad_k17_trimmed_phase_core_integration_20260801.audit.json
status PASS_K17_TRIMMED_PHASE_CORE_INTEGRATION_ARITHMETIC_AND_OFFSET
```

This audit is deliberately local and solver-free.  It neither launches a
new H100 job nor treats a forest as a rooted chronology.
