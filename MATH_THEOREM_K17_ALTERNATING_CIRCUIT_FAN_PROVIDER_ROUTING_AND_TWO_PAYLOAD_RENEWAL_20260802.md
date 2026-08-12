# K17 alternating-circuit fans, planted-provider routing, and two-payload renewal

**Date:** 2026-08-02  
**Status:** exact abstract lemma with three independently replayed local
calibrations.  The result gives a checkable sufficient fan condition and an
exact finite counter-cut.  It does not prove that every positive-residence
K17 state has a fan.  Source, lower compiler, arbitrary-width upper closure,
residency, and a word are outside scope.

## 1. Literal factor and exchange states

Let `E` be the fixed rank-eight/rank-nine incidence universe and let a factor
`F` be represented by its selected-incidence vector `y(F)`.  At an ordinary
rank-eight root `q` exactly two incidences are selected.  If their rank-nine
owners are `u,v`, write

\[
 p_{q;uv}(F)=y_{q,u}(F)y_{q,v}(F)=1.                 \tag{1.1}
\]

For each positive pair-provider row `rho`, let `P_rho` be its literal set,
let `b_rho` be its required load (one for the frozen q1/guard rows), and put

\[
 \lambda_\rho(F)=\sum_{p\in P_\rho}p(F).             \tag{1.2}
\]

Opened rank-ten rows are indexed separately by `(omega,U)`, where
`omega=0,1` is one complete topology-derived opening.  Their load includes
the ordinary pair literals (1.1) and the exact exceptional seam witness.
The opening and its seam state are rebuilt from the materialized factor; they
are not inherited from the parent.

Let `X` be the literal hard face consisting of:

1. exact lower and owner degrees and the protected boundary incidences;
2. every frozen guard, with every `p` rebuilt by (1.1);
3. all 19,412 ordinary non-`D` q1 rows;
4. all 19,448 opened rank-ten rows in each orientation; and
5. one connected augmented lollipop and its two decoded opening states.

The strict exchange graph `G_X` has vertex set `X`.  An arc

\[
                 F\mathrel{\mathop{\longrightarrow}^{C}}F'
\]

is a current-state alternating circuit `C` (in the present calibration, a
C6 or rank-seven-core star-C8) whose deletions are selected, whose additions
are absent, and whose materialized head is again in `X`.  The circuit may be
absent from the catalogue at another state.  This is a groupoid of
state-relative exchanges, not a fixed additive move group.

For each opening, let `D_omega(F)` be the multiset of canonically labelled
internal coordinate runs of length one or two, and let

\[
 R_\omega(F)=|D_\omega(F)|.                            \tag{1.3}
\]

Let `h_{omega,r}(F)` be the exact number of missing opened rank-`r` targets.
The two payload totals used below are

\[
 S(F)=R_0(F)+R_1(F),\qquad
 U(F)=\sum_{\omega=0}^1\sum_{r=11}^{17}h_{\omega,r}(F). \tag{1.4}
\]

Keeping the full vector `(R_0,R_1,h_{0,11},...,h_{1,17})` is stronger; the
two scalars in (1.4) are only a convenient cone projection.

## 2. Neutral pivots, quench spokes, and planted pair literals

Fix `F in X`.  A **neutral pivot** is a nonempty strict path `A` in `G_X`
from `F` to `G` such that

\[
                 R_\omega(G)=R_\omega(F),\quad\omega=0,1. \tag{2.1}
\]

It may change pair locations, exact provider loads, component traces, and
upper witnesses.  A **quench spoke at G** is a current-state alternating
circuit `B` applicable at `G`.  Write `H=B(G)` before deciding whether `H`
is hard-legal.

For a provider row `rho`, let

\[
\begin{aligned}
 O_\rho(B\mid G)&=\{p\in P_\rho:p(G)=p(H)=1\},\\
 N_\rho(B\mid G)&=\{p\in P_\rho:p(G)=0,\ p(H)=1\}.
\end{aligned}                                           \tag{2.2}
\]

These sets give the exact terminal load identity

\[
       \lambda_\rho(H)=|O_\rho(B\mid G)|+|N_\rho(B\mid G)|. \tag{2.3}
\]

The **critical rows** of the spoke are

\[
 L(B\mid G)=\{\rho:|O_\rho(B\mid G)|<b_\rho\}.        \tag{2.4}
\]

Thus a row is critical exactly when the providers surviving the quench are
insufficient, whether or not the row had large load before the move.

A new literal `p_{q;uv}` in (2.2) is **pivot-planted and quench-completed**
if one of its two incidence halves was installed by `A`, is selected at `G`,
and survives `B`, while the other half is installed by `B`.  Denote the set
of such literals in row `rho` by `N^x_rho(A,B)`.  The exact provider-cover
condition is

\[
 |N_\rho(B\mid G)|\ \ge\ b_\rho-|O_\rho(B\mid G)|,
 \qquad \rho\in L(B\mid G),                            \tag{2.5}
\]

and the **pure planted-handoff** specialization additionally requires that
enough distinct literals on the left side belong to `N^x_rho(A,B)`.
There is no capacity-one matching between rows: a true pair literal may
occur in more than one guard row.  Equation (2.5) is a rowwise Boolean-cover
test, not a scalar Hall projection.

The exact sequential pair current at a touched root is worth recording.  If
the pivot and spoke incidence updates are `z^A,z^B`, then

\[
\begin{aligned}
p(y+z^A)-p(y)
 &=y_u z^A_v+y_v z^A_u+z^A_u z^A_v,\\
p(y+z^A+z^B)-p(y+z^A)
 &=(y_u+z^A_u)z^B_v+(y_v+z^A_v)z^B_u+z^B_u z^B_v.
\end{aligned}                                           \tag{2.6}
\]

The terms `z^A_u z^B_v+z^B_u z^A_v` are the planted cross-current.  Formula
(2.6), or a literal rebuild of `p` at both prefixes, remains valid when `B`
deletes an incidence installed by `A`; in that activated-schema case the
hypothetical corner `B(F)` need not be a binary factor at all.

## 3. The alternating-circuit fan lemma

For a fixed neutral pivot `A:F->G`, let `Q_A(G)` be any finite collection of
current-state C6/star-C8 spokes at `G`.  It is a
**residence-accepting fan** if at least one spoke satisfies the following
conditions.

1. **Alternation and protection.**  `B` is literally applicable at `G`, and
   neither retained prefix deletes a protected incidence.
2. **Pair-provider routing.**  Equation (2.5) holds for every positive
   ordinary q1/guard row; every critical last-provider row has an explicitly
   named planted or otherwise new replacement literal.  Every nonpositive or
   non-pair guard is evaluated literally at `G` and `H`.
3. **Opened routing.**  The analogue of (2.3)--(2.5), including exceptional
   seam providers, holds for all 19,448 targets in each newly decoded
   opening.
4. **Topology.**  The exact fragment-splice permutation at `G` and at `H`
   has the prescribed one-lollipop type.  Equivalently, `G,H` are connected
   members of the hard topology face; component count at the root is not
   used as a proxy.
5. **Trace absorption.**  For some positive integers `delta_0,delta_1`,

   \[
           R_\omega(H)\le R_\omega(F)-\delta_\omega,
           \qquad\omega=0,1.                            \tag{3.1}
   \]

### Theorem 3.1 (alternating-circuit fan)

Every residence-accepting fan contains a strict negative ordered packet `A;B` on
`X`.  All exact degrees, protected incidences, guards, ordinary q1 rows,
both opened q1 decks, and topology hold at every retained prefix, and the
terminal residence decreases in both openings by (3.1).

#### Proof

Every prefix of `A` is in `X` by the definition of a neutral pivot.  Circuit
alternation gives the linear degree rows for `B`, and condition 1 gives its
occupancy and protection rows.  For a positive pair row, the live terminal
literals split disjointly into the survivors and births in (2.2), so (2.5)
is exactly the required load inequality.  Conditions 2 and 3 cover all
ordinary, guard, and opened rows; condition 4 supplies the nonlinear
topology/opening predicate.  Hence `H in X`.  Finally (2.1) and (3.1) give
strict descent from the root in both orientations.  No cost computed for
`B` at `F` is used.  \(\square\)

The theorem is useful as a local certificate: circuit formulas prove degree
balance, (2.3)--(2.6) prove every threatened pair row, a port permutation
proves topology, and a capped boundary-run replay proves (3.1).  A full
materialized replay is the fail-closed implementation of the same proof.

### Corollary 3.2 (the two calibrated exposure modes)

The hypotheses of Theorem 3.1 are met by either of the following local
exposure mechanisms, once its provider, topology, and trace conclusions have
been checked.

1. **Complementary-port handoff.**  The spoke is incidence-applicable at
   `F` but would destroy a last provider `p_old`.  The pivot retains
   `p_old` through `G` and installs one half of `p_new`; the spoke installs
   the other half while deleting `p_old`.  The row truth pattern is
   `(1,1,0,1)` on `(F,G,B(F),H)`.  This is the seed13 two-C6 mode.
2. **Activated spoke.**  Write `A^+` for the incidences installed by the
   pivot path and `D(B)` for the spoke deletions.  There is a nonempty
   activation set

   \[
        E_{act}=A^+\cap D(B),                            \tag{3.2}
   \]

   absent at `F` and selected at `G`; every other deletion of `B` is selected
   at `G` and every addition is absent there.  The spoke therefore has no
   root arc but is alternating at the hub.  This is the frozen-root
   C6/star-C8 mode, with `E_act={y11158}`.

The two modes can coexist, but neither is necessary: a pivot can expose a
quench solely by transporting a trace socket or by changing topology while
all pair rows retain slack.

#### Proof

In the first mode the four-state Boolean calculation and (2.5) prove the
critical provider row; in the second, (3.2) and the remaining occupancy
hypotheses are exactly the state-relative alternation test for `B` at `G`.
The other stated checks are conditions 2--5 of Theorem 3.1.  \(\square\)

## 4. Exact trace interaction

For any retained transition `C:K->K'`, define multiset differences

\[
 K_\omega(C\mid K)=D_\omega(K)\setminus D_\omega(K'),\qquad
 N_\omega(C\mid K)=D_\omega(K')\setminus D_\omega(K). \tag{4.1}
\]

Then

\[
 R_\omega(K')-R_\omega(K)
   =|N_\omega(C\mid K)|-|K_\omega(C\mid K)|,           \tag{4.2}
\]

and an ordered pivot/quench obeys the exact telescoping ledger

\[
 1_{D_\omega(H)}-1_{D_\omega(F)}
 =1_{N_\omega(A\mid F)}-1_{K_\omega(A\mid F)}
 +1_{N_\omega(B\mid G)}-1_{K_\omega(B\mid G)}.        \tag{4.3}
\]

A pivot-born carrier is an element of

\[
 C_\omega(A,B)=N_\omega(A\mid F)\cap K_\omega(B\mid G). \tag{4.4}
\]

It cancels from the terminal ledger.  Neutrality says only
`|N_omega(A|F)|=|K_omega(A|F)|`; it does not say that the two multisets, their
ports, or their future quench incidence are equal.  A simple sufficient
trace test for (3.1) is

\[
 |K_\omega(B\mid G)|-|N_\omega(B\mid G)|
       \ge\delta_\omega.                               \tag{4.5}
\]

When `B` is also geometrically applicable at `F`, its residence interaction
is the mixed finite difference

\[
 I_{R_\omega}(A,B;F)
 =\Delta_B R_\omega(G)-\Delta_B R_\omega(F).           \tag{4.6}
\]

The exact seed13 two-C6 square has `Delta_A R=0`, passive
`Delta_B R(F)=0`, and `I_R=-2` in each orientation.  At shared lower root
`24264`, the pivot transports the coordinate-6 doubleton
`{56424,56904}` to the socket `{24264,24137}`.  It simultaneously absorbs
the coordinate-7 doubleton `{28328,24232}` (cost `-1`) and ejects the
coordinate-15 doubleton `{56424,64552}` (cost `+1`), which is the exact
neutrality identity.  The quench then merges `{24264,24137}`, the second
coordinate-6 doubleton `{7881,6873}`, and a length-29 component into runs of
lengths `22,3,8`, removing two shorts.  Without the pivot, the same quench
removes only `{7881,6873}` and creates the coordinate-9 singleton `{24264}`;
its passive residence cost is therefore zero.  At the same time the pair row
for target `24300` is handed from

```text
p262698 = y10993*y10996
```

to the pivot-planted/quench-completed literal

```text
p387503 = y42197*y42195.
```

Its four-corner truth pattern is `(1,1,0,1)`.  This is exactly Theorem 3.1
with one critical row and a nonzero trace interaction.  The complete
component partition is frozen in
`scratch/k17_h1_fullq1_escape_res1994_bridge_theorem_20260802/EXACT_COMPONENT_IDENTITY.md`.

The independently replayed C6/star-C8 pair at residence 1994 realizes a
different fan channel.  The neutral C6 changes the selected pair channel at
root `7962` from `p263326` to `p263328`; the star-C8 consumes the
bridge-installed incidence `y11158` and changes it to `p263327`.  Thus the
spoke has no root arc and (4.6) is not the appropriate square.  Literal
prefix replay instead gives

\[
 (\Delta R_0,\Delta R_1;\Delta h_{11},\Delta h_{12},\Delta h_{13})
             =(-1,-1;+1,0,0),                          \tag{4.7}
\]

with full q1 and all hard rows at both prefixes.  This is an
occupancy-activated fan whose second payload is one unit of rank-11 debt.

## 5. What positive residence, q1 multiplicity, and connectedness do not imply

Positive residence asserts only that `D_0(F)` or `D_1(F)` is nonempty.  It
does not put an alternating circuit through a short component, provide an
absorbing port, or preserve the one-component splice.  Provider
multiplicities constrain (1.2), but do not place complementary incidence
halves at a quench destination.  Connectedness is a property of the current
factor, not of the factors obtained after an exchange.

The frozen two-C6 square already separates these data from fan exposure:
`F` and `A(F)` are connected, full-q1, and have the same residence, yet the
same geometric quench is q1-illegal and residence-neutral at `F` and is
q1-legal and residence-minus-two at `A(F)`.  This comparison uses equality
of q1 coverage, not equality of the complete provider-load vector.  It proves
that those displayed coarse statistics are not a Markov quotient.

There is also a rigorous abstract no-go for the stronger load projection.
Let `H+` contain every positive ordinary, guard, and opened row, and define

\[
 \pi(F)=\bigl(R_0(F),R_1(F),(\lambda_j(F))_{j\in H^+},
                    \#\operatorname{comp}(F)\bigr).    \tag{5.1}
\]

### Proposition 5.1 (typed-twin no-go)

The projection `pi` is not a congruence of factor exchange graphs.  In
particular, equality of the complete positive-row load vector, positive
residence, and one-component topology does not determine whether a neutral
pivot exposes a legal negative quench.

#### Proof

Take two exact-degree exchange gadgets with the same fixed connected spine,
trace cardinalities, and provider-load vector.  In both, a neutral pivot
leaves a sole old provider `p_old=y_r*y_d` alive; the quench deletes `y_d`,
plants `y_b`, and removes one typed short component.  Complete each selected
slot substitution to a C6 with two private roots and owners, using the cyclic
shift of a `3 by 3` perfect matching to balance every current.

In the compatible twin, the pivot plants `y_a` with
`p_new=y_a*y_b in P_j`.  In the twisted twin it plants the same number of
incidences but of type `y_a'`, with `y_a'*y_b notin P_j`.  The compatible
quench has `p_old:1->0,p_new:0->1`; the twisted quench has the same scalar
currents but sends `lambda_j:1->0` and is rejected.  Untouched pair providers
can give all other rows any prescribed common load.  If `j` is a guard row,
all q1 loads may be made arbitrarily large.  Thus the root twins have equal
(5.1) but different fan answers; their difference is one typed compatibility
entry discarded by `pi`.  \(\square\)

This is a factor/exchange countermodel, not an assertion that either twin is
embedded in the current K17 Pascal geometry.  Its complete proof and the
private-C6 construction are frozen in
`MATH_LEMMA_K17_NEUTRAL_PIVOT_FAN_COMPATIBILITY_AND_MINIMAL_CUT_20260802.md`
(SHA-256 `31ed09f76477025ac30228c2aad49727a2d622604894ed074f8a590a226c02ee`).

Multiplicity has one precise but limited consequence.  A primitive touching
`m` ordinary roots kills at most `m` ordinary pair providers of one target.
Thus ordinary load at least four protects a row from one C6, and load at
least five protects it from one four-root star-C8.  These bounds do not
produce an alternating circuit, a negative trace socket, or a safe topology
splice, and they do not protect exceptional opened seam/history targets.
Compound paths require the bound at every materialized prefix.

Here is the exact obstruction.  Fix a pivot length bound `b`, an upper-debt
bound `D`, and a quench family.  Let `Z_b^D(F)` be all endpoints of strict
residence-neutral pivot paths of length at most `b` whose prefixes respect
the debt bound.  Build the bipartite **fan compatibility graph** with left
vertices `G in Z_b^D(F)` and right vertices the current-state quench schemas
at `G`.  Retain an edge exactly when conditions 1--4 of Section 3 hold, and
mark it negative exactly when (3.1) holds.

### Proposition 5.2 (minimal fan counter-cut)

A bounded residence-accepting fan exists if and only if the fan compatibility graph
has a negative edge.  Consequently the exact bounded counter-cut is

\[
 \delta^-_{\rm fan}(Z_b^D(F))=\varnothing.             \tag{5.2}
\]

Every rejected boundary schema must have a literal blocker of one of five
types:

```text
occupancy/alternation,
pair or opened-provider cover,
protected incidence,
topology/opening,
nonnegative trace (or an excluded upper-debt cone).
```

The smallest cut is one state: if `F` has no legal neutral outgoing pivot and
no legal negative root quench, then `{F}` is already an accepting-shore cut.
The smallest nontrivial planted-provider cut has one neutral endpoint, one
geometrically negative quench, and one row `rho` satisfying

\[
 |O_\rho(B\mid G)|+|N_\rho(B\mid G)|<b_\rho.           \tag{5.3}
\]

For a sole-provider row this is the single missing complementary-half
obstruction.  It cannot be removed by a scalar provider count.

#### Proof

A residence-accepting fan is, by definition, a left endpoint and a negative
compatible right edge.  This proves the equivalence and (5.2).  A strict packet has a
first arc, so the one-state statement is immediate.  Equation (2.3) proves
that (5.3) is an exact failed hard row, not a relaxation.  \(\square\)

Without assuming a pivot, one hard state is the smallest cut.  If a
positive-length legal neutral pivot and a geometrically negative quench are
required, the smallest nontrivial cut has exactly the two legal states
`S={F,G=AF}`; the proposed quench head fails (5.3) or another literal row.
Let `N` be the head-minus-tail incidence matrix of the retained fan graph and
`d=e_t-e_F`.  Then

\[
             z=-\mathbf1_S,\qquad N^Tz\le0,\qquad d^Tz=1 \tag{5.4}
\]

is the exact Farkas certificate that no unit flow reaches the accepting sink.
If the sink is reachable but every path has nonnegative chosen scalar cost,
a Bellman--Ford potential is the exact dual certificate.  A sampled miss or
a root-disjoint plateau is neither certificate.

Thus positive residence plus q1 coverage/multiplicity and connectedness
**does not** imply a fan.  The exact extra hypothesis is product expansion.
For each hard state `F`, form `K_F^lit` with neutral pivots on the left and
regenerated quench spokes on the right.  Join a pivot to a spoke exactly when
current alternation, the circuit-coherent typed cover (2.5), every exceptional
opened history, protection, and topology pass.  Label the edge by its exact
two-opening trace and upper current.  A residence fan exists exactly when
the residence-negative edge set of `K_F^lit` is nonempty.  Uniform renewal
requires this nonemptiness, with the chosen head returning to the endpoint-
closed family, at every positive state.  Ruling out (5.2) for the actual K17
component requires such an expansion theorem or a complete finite audit.

## 6. Two-payload renewal

For one opening put

\[
 H_\omega(F)=\sum_{r=11}^{17}h_{\omega,r}(F).
\]

There are exactly

\[
       \sum_{r=11}^{17}{17\choose r}=21778             \tag{6.1}
\]

possible deeper targets, so

\[
       \Lambda_\omega(F)=21779R_\omega(F)+H_\omega(F)  \tag{6.2}
\]

is an exact mixed-radix encoding of lexicographic
`(R_omega,H_omega)`.  Across the two openings one must retain
`(Lambda_0,Lambda_1)` (or use successive optimal faces on the declared full
vector); taking coordinatewise best values from different orientations is
invalid.

### Corollary 6.1 (exact per-opening lex calibration)

The residence-1994 neutral-C6/activated-star-C8 fan has per-opening payload

\[
                (\Delta R_\omega,\Delta H_\omega)=(-1,+1)
\]

and hence `Delta Lambda_omega=-21778`.  The independently replayed low-
residence upper star-C8

```text
core 33913, labels 13,1,14,12,
old y 75418,59038,90856,67103,
new y 75412,59039,90862,67102
```

preserves ordinary q1 `19412/19412`, both opened q1 decks
`19448/19448`, all guards, protection, and one component.  In each opening
it changes

\[
 (R;h_{11},h_{12},h_{13})
 =(1980;1516,269,4)\longrightarrow(1983;1512,267,3),
\]

so its payload is `(+3,-7)` and
`Delta Lambda_omega=65330`.  Thus it is a genuine upper payload bought with
residence and is correctly rejected by residence-first lex order.  Its
independent semantic and complete-CNF audit SHAs are `228083d4...` and
`03545a24...`; the full bindings are frozen under
`scratch/k17_two_objective_renewal_20260802/`.

Call any strict path in `X` a **payload-accepting packet** when its exact
payload lies in a declared acceptance cone.  This includes a hard-compatible
fan satisfying conditions 1--4 of Section 3 and also a direct upper primitive;
it does not inherit the residence decrease required in condition 5.

Suppose an endpoint-closed renewal family `Y` supplies state-relative packets
of types

\[
 Q:\ (\Delta R_\omega,\Delta H_\omega)\le(-a,+b),\qquad
 V:\ (\Delta R_\omega,\Delta H_\omega)\le(+c,-d)       \tag{6.3}
\]

in both openings, with fixed `a,d>0`, `b,c>=0`, every physical prefix in
`X`, and every endpoint back in `Y`.

### Theorem 6.2 (two-payload exchange-rate renewal)

If

\[
                         bc<ad,                         \tag{6.4}
\]

choose rational `w` with `b/a<w<d/c`, with `d/c=+infinity` when `c=0`.
Every available `Q` or `V` packet
strictly decreases

\[
             L_w(F)=\sum_{\omega=0}^1
                         (wR_\omega(F)+H_\omega(F)).    \tag{6.5}
\]

After clearing denominators this is a nonnegative integer potential.  If
every state of `Y` with `R_0+R_1+H_0+H_1>0` has at least one such branch,
repeated literal regeneration reaches `R_0=R_1=H_0=H_1=0` in finitely many
commits.

#### Proof

A `Q` packet changes each summand by at most `-wa+b<0`; a `V` packet changes
it by at most `wc-d<0`.  Endpoint closure regenerates the hypothesis.  The
scaled potential cannot descend indefinitely.  If it stopped at a positive
state, the quantified branch would supply a further strict descent; hence it
stops only at the zero-payload face.  \(\square\)

For the authenticated payload bounds `Q=(-1,+1)` and `V=(+3,-7)`, take
`w=2`; each decreases `2R_omega+H_omega` by one.  Algebraically, a strictly
composable schedule with `n` Q packets and `m` V packets has

\[
 \Delta R_\omega\le-n+3m,\qquad
 \Delta H_\omega\le n-7m.                              \tag{6.6}
\]

The least positive integral ratio giving coordinatewise descent is
`m=1,n=4`, for the formal bound

\[
                         4Q+V\le(-1,-3)                 \tag{6.7}
\]

in each opening.  This is a cone calculation, not an authenticated compound
K17 path: the two payloads were verified at different states.  Their
state-relative composability, endpoint closure, and uniform product expansion
remain unproved.  The complete two-payload derivation and upper witness are
also frozen in `MATH_THEOREM_K17_TWO_OBJECTIVE_ALTERNATING_FAN_RENEWAL_20260802.md`.

## 7. Exact scope of the conclusion

The fan lemma closes the local logical gap between a neutral circuit and a
regenerated negative circuit.  Its essential state is

```text
full incidence assignment;
rebuilt pair variables and exact row loads;
both topology-derived openings and trace ports;
protected/topology state;
residence and upper payload vectors;
all persistent renewal tickets.
```

Neither positive residence, full q1, provider histograms, nor one current
component may replace that state.  A universal descent theorem now has one
precise remaining target: rule out the fan counter-cut (5.2) in every
positive endpoint-closed renewal state, with a common two-payload cone such
as (6.3).  The existing K17 witnesses prove several edges of this graph; they
do not prove that every positive shore has one.
