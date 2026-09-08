# Thread A: protected fusion of the resident all-depth `k=15` factor

Date: 2026-07-29

Status: exact switching and splice theorems, plus a frozen constructive
eight-seam near-certificate.  The source factor closes residence and every
shadow-support gate.  A shadow-perfect splice or a compiler-ready connected
factor is not claimed below.

## 0. Verdict

The independently audited factor

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/u2u3l3_s801.engine.json
```

has all of the following simultaneously:

* 6,435 distinct rank-eight middle owners, each of factor degree two;
* no quotient loop;
* minimum positive coordinate run four and no depth-three residence defect;
* zero lower and upper fixed-window holes at every depth `q=1,...,7`;
* zero arbitrary-width upper holes; and
* nine physical components.

The engine SHA-256 is

```text
886877094a3eaba8950136728d131782141a4b6f882d570ecb3791827da98f83
```

and the independent audit SHA-256 is

```text
f2ab5b997199e788c1f18d2de2579020751020a35d8ef1394cb0b06a40494bd7.
```

Thus the former residence-versus-shadow intersection is closed.  There are
two exact connectivity routes.

1. **Physical open splice.**  Cut each of the nine physical cycles once and
   join the nine resulting paths by eight physical Johnson seams.  This is
   the smallest possible open splice.  Its exact finite state graph has
   12,870 oriented cut states and 96,150 residence-safe, lower-colour-
   recycling arcs.
2. **Equivariant factor switch.**  The nine physical cycles come from only
   five quotient cycles.  One legal receiver five-cycle, equivalently one
   alternating quotient `C10`, would be the smallest possible single
   alternating circuit.  The exact component-transversal `C10` catalogue for
   this factor is empty.  Thus this minimal route is refuted, and any
   equivariant solution needs a longer or compound alternating circuit.

The physical route is a constructive finite gate.  Topology alone does not
prove the exact word: the changed collars must retain every protected upper
target and the final lower compiler must pass its integral Hall test.

## 1. Exact component ledger

The quotient components have the following audited data.  The voltage is in
`Z_15`.

| quotient edges | voltage | physical lifts | physical length |
|---:|---:|---:|---:|
| 258 | 5 | 5 | 774 |
| 126 | 4 | 1 | 1890 |
| 37 | 1 | 1 | 555 |
| 5 | 4 | 1 | 75 |
| 3 | 11 | 1 | 45 |

The quotient lengths sum to 429 and the physical lengths, with
multiplicity, sum to 6,435.  In particular the five length-774 physical
cycles are the five lifts of the voltage-five quotient component.  Merely
joining the other four components cannot remove this fivefold lift; a final
equivariant cycle must have coprime voltage.

For receiver-switch calculations the coherent `tau=M_0^{-1}P` orientations
give

\[
 (37,1),\ (258,10),\ (126,4),\ (5,11),\ (3,4),
\tag{1.1}
\]

whose signed total voltage is zero.  The signs in (1.1) need not agree with
an independently chosen undirected orientation of each physical component;
only the coherent table may be used in a switch-voltage sum.

The fixed-window and arbitrary-width assertions above are replayed in

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    u2u3l3_s801.independent.full.audit.json
scratch/k15_fixed_matching_pbbs_resident_20260729/
    u2u3l3_s801.seam_endgame.audit.json
```

The latter also records the nine physical lengths, zero holes on both fixed
window shores through depth seven, 12,870 states, and 96,150 legal arcs.

## 2. Fixed-matching receiver circuits

Let `L` and `V` be the rank-seven and rank-eight physical layers.  Fix one
incidence perfect matching

\[
 M_0:L\longrightarrow V
\]

and let `P` be the second perfect matching of the factor.  Put

\[
 \tau=M_0^{-1}P.
\tag{2.1}
\]

The cycles of `tau` are exactly the suppressed middle-factor components.

### Theorem 2.1 (receiver-cycle switch)

Choose distinct sources `x_0,...,x_(s-1)` and put

\[
 y_i=\tau(x_i).
\]

For a permutation `rho` of the indices define

\[
 \tau_\rho(x_i)=y_{\rho(i)},\qquad
 \tau_\rho(x)=\tau(x)\quad
       (x\notin\{x_0,\ldots,x_{s-1}\}),
\tag{2.2}
\]

and

\[
 P_\rho=M_0\tau_\rho.
\tag{2.3}
\]

Then `P_rho` is a perfect matching precisely when every proposed new edge
is an incidence,

\[
 x_i\subset M_0(y_{\rho(i)}),
\tag{2.4}
\]

and it is edge-disjoint from `M_0` precisely when additionally

\[
 M_0(y_{\rho(i)})\ne M_0(x_i).
\tag{2.5}
\]

If `rho` is one `s`-cycle, then `P triangle P_rho` is one alternating
`C_(2s)`.  If the selected `x_i -> y_i` arcs lie in `s` distinct cycles of
`tau`, the new permutation `tau_rho` has one cycle on their union.

#### Proof

The `y_i` are distinct because `tau` is a permutation.  Equation (2.2)
therefore only permutes their receiver slots, so `tau_rho`, and hence
`P_rho`, is bijective.  Its edges are physical incidence edges exactly under
(2.4); (2.5) is exactly the no-common-edge condition.

On the changed slots, the old matching pairs `x_i` with `M_0(y_i)` and the
new matching pairs it with `M_0(y_(rho(i)))`.  The components of their
symmetric difference are consequently the cycles of `rho`, with two
incidence edges per index.  Finally, deleting `x_i -> y_i` opens each old
`tau`-cycle into a directed path from `y_i` to `x_i`.  Contracting these
paths leaves exactly the directed graph of `rho`.  A single `s`-cycle thus
joins them into one cycle.  \(\square\)

### Corollary 2.2 (minimal quotient connector)

Any receiver permutation supported on `s` slots and having `r` nontrivial
cycles changes the number of factor cycles by at most `s-r`.  Therefore a
single alternating circuit which merges five quotient cycles must have
support at least five.  A legal support-five receiver cycle, i.e. a quotient
`C10`, is minimal.

#### Proof

A permutation with the stated cycle data is a product of `s-r`
transpositions.  Multiplying a permutation by one transposition changes its
cycle count by one.  Reducing five cycles to one needs a drop of four, so a
single receiver cycle needs `s-1>=4`.  \(\square\)

For a rotation-equivariant quotient switch, let `v` be the voltage of the
resulting 429-cycle.  Its physical lift has exactly

\[
 \gcd(15,v)
\tag{2.6}
\]

components.  Hence the `C10` succeeds topologically exactly when

\[
 v\in\{1,2,4,7,8,11,13,14\}\pmod {15}.
\tag{2.7}
\]

Component merging without (2.7) is not connectivity.

### Theorem 2.3 (artifact-specific minimal-circuit no-go)

For the audited `u2u3l3_s801` factor there is no legal support-five receiver
cycle meeting each of the five current quotient components exactly once.
Consequently there is no component-transversal quotient `C10`, before any
voltage, shadow, or residence condition is imposed.

#### Proof

In the exact fixed-`M_0` receiver graph there are 429 receiver states and
2,570 legal exchange arcs, of which 1,437 cross components.  The two shortest
components force the first receiver into

\[
 \{152,315,318\}.
\]

Exhaustive sparse path extension gives respectively `3,17,2` directed paths
which visit all five components once.  For each of the three starts, the set
of possible terminal receivers is disjoint from the exact set of legal
predecessors which closes back to the start.  Hence none of the 22 paths
closes to a receiver five-cycle.

The calculation is an exact DFS over the explicit receiver graph, not a SAT
timeout.  It is reproduced by

```text
scratch/thread_audit_k15_u2u3l3_c10_structure_20260729.py
scratch/thread_a_k15_u2u3l3_c10_sparse_prefilter_20260729.py
```

whose terminal report has

```text
raw_component_transversal_c10       0
unit_voltage_c10                    0
immediate_deck_safe_c10             0
resident_immediate_deck_safe_c10    0.
```

The scope is exactly one support-five receiver cycle with one marked arc in
each present quotient component.  It does not exclude a support-larger
circuit, two or more interacting receiver circuits, or the physical open
splice.  \(\square\)

## 3. Exact shadow and residence transport

Let an orientation-coherent switch delete a set `D_-` of projected
transitions and insert `D_+`.  For a fixed `q`, let `r_q(S)` and `a_q(S)`
be the numbers of old and new correct-rank `q`-edge windows with target
`S` that meet the changed transitions.  If `mu_q(S)` is the old
multiplicity, then

\[
 \boxed{\mu'_q(S)=\mu_q(S)-r_q(S)+a_q(S).}
\tag{3.1}
\]

Consequently fixed-window support is retained exactly when

\[
 \boxed{r_q(S)-a_q(S)\le \mu_q(S)-1}
\tag{3.2}
\]

for every target at every protected depth.  This is targetwise; aggregate
repeat slack is not a substitute.

For unrestricted upper intervals, let `W^+(S)` be the family of old cyclic
intervals whose union is `S`.  A cut set `C` and a family of new seams
preserve `S` exactly when either

\[
 \exists I\in W^+(S)\quad E(I)\cap C=\varnothing,
\tag{3.3}
\]

or a new interval crossing a seam has union `S`.  At one seam all new
upper values are unions of a suffix-union state on the left and a
prefix-union state on the right.  Starting from a rank-eight middle set,
each profile changes at most seven more times before reaching `[15]`.
Thus at most `8*8=64` distinct seam values need be checked.  This finite
profile is exact; limiting the check to minimal-width windows is not.

Residence is equally local.  On a fixed-`M_0` factor write a directed lower
arc as `e=(X,Y)` and put

\[
 \iota(e)=Y\setminus X,qquad
 \delta(e)=X\setminus Y.
\tag{3.4}
\]

The nonloop width-two/three residence theorem gives

\[
 \boxed{
 \iota(e_i)\ne\delta(e_{i+1}),\qquad
 \iota(e_i)\ne\delta(e_{i+2})
 }
\tag{3.5}
\]

for every final arc.  Since the source factor already satisfies (3.5), only
the radius-two collars of changed arcs need checking.  Interacting collars
must be tested in the final chronology, not independently.

## 4. The exact eight-seam open-splice theorem

Cut one transition from each of the nine physical cycles and orient each
resulting path.  A state is such an oriented cut.  Join eight states by
physical Johnson seams.

### Theorem 4.1 (protected open-splice certificate)

The resulting middle order is a depth-three-resident, all-upper path with
the standard one-hole lower-q1 interface if all of the following hold.

1. Exactly one state is chosen from each physical component, and the eight
   seam arcs form one directed path on the nine states.
2. Every seam is a Johnson edge and every final width-two/three comparison
   (3.5) holds.
3. The eight seam intersections are eight distinct colours among the nine
   deleted lower-q1 colours.
4. The fixed-window inequalities (3.2) hold at every required depth.
5. Every arbitrary-width upper target satisfies (3.3) or occurs in an exact
   suffix/prefix seam profile.

Under these hypotheses the final path contains every rank-eight owner
exactly once, has exactly one internal lower-q1 hole, has no residence
defect, and retains the entire upper Boolean filter.

#### Proof

Items 1 and 2 give one Johnson Hamilton path on the unchanged middle-owner
set and prove residence by (3.5).  The original factor uses each physical
lower-q1 colour exactly once.  Nine cuts therefore remove nine distinct
colours; item 3 restores eight of them without collision and leaves exactly
one for the endpoint/compiler interface.  Formula (3.1) and item 4 prove all
fixed-window rows.  Every old upper interval is either wholly retained in
one piece or crosses a cut.  Item 5 is therefore precisely the exhaustive
partition of its possible witnesses and proves unrestricted upper support.
\(\square\)

This theorem is only the carrier part of the exact word.  Let `P` be the
maximal depth-three erosion of the final path.  One still needs a common
lower assignment whose legal cells satisfy the full physical Hall
inequalities and the endpoint equations.

## 5. Constructive finite progress

The solver-free catalogue attached to the source factor has

\[
 2W=12{,}870
\]

oriented cut states and exactly 96,150 arcs satisfying Johnson adjacency,
local residence, and the lower-q1 recycling rule.  Thus topology,
residence, and the tight q1 ledger are already a concrete finite routing
problem, not an unbounded absorber hypothesis.

A retained eight-seam path is

```text
scratch/THREAD_A_u2u3l3_eight_seam_nearpath_round001_20260729.json
```

with SHA-256

```text
dc39bfd9377a2d806d50c84f941b0e943f0dc2742000864dec9659713085c3e1.
```

Independent local replay gives:

```text
middle owners                 6435 distinct
Johnson seams                 8
residence defects             0
D^3(maximal erosion)=middle   true
lower holes q1..q7            1,6,0,0,0,0,0
upper holes q1..q7            1,1,1,0,0,0,0
arbitrary-width upper holes   1,1,1,0,0,0,0
base ranks<=5 Hall deficiency 0
```

The three upper missing masks are respectively

\[
 1917\quad(\operatorname{rank}9),\qquad
 18299\quad(\operatorname{rank}10),\qquad
 28475\quad(\operatorname{rank}11).
\tag{5.1}
\]

This is an unconditional connected/resident/q1-tight near-certificate.  The
displayed Hall check covers only the 4,943 base targets of ranks at most
five.  It is diagnostic, not the complete generalized lower compiler; in
particular the six missing rank-six targets remain to be assigned.

## 6. Exact compiler extension

Fix any old lower matching outside a promoted collar, discard every old
edge incident with the collar, and let `D` be the displaced targets.  Let
`K^+` be the genuinely free positions of the recomputed physical compiler,
not merely the geometrical seam positions.  The retained matching extends
if and only if

\[
 \boxed{|N(Y)\cap K^+|\ge |Y|\qquad(Y\subseteq D).}
\tag{6.1}
\]

This is ordinary bipartite Hall after the outside matching is frozen.
Cardinality slack checks only the set `Y=D`; it does not prove (6.1) for
proper subsets.  If no complete outside matching is frozen, the unrestricted
Hall inequalities on the entire lower target family are required instead.

The physical eight-seam architecture has a genuinely bounded collar.  A
hypothetical quotient `C10` would change five quotient matching slots and
hence 75 physical matching incidences, but Theorem 2.3 proves that no such
component-transversal circuit exists here.  Any surviving compound
equivariant route has at least this phase-expansion issue and must be audited
independently.

## 7. Smallest remaining hypotheses

Either of the following would finish the carrier part.

* **Physical splice lemma.**  Find one path in the 12,870-state/96,150-arc
  graph satisfying items 4--5 of Theorem 4.1 and whose maximal erosion passes
  the full generalized lower Hall/endpoint audit.
* **Compound equivariant lemma.**  Find a support-larger circuit or a sequence
  of interacting receiver circuits which evades Theorem 2.3, produces one
  quotient cycle of unit voltage, satisfies (3.2)--(3.5) after all fifteen
  phase lifts, and whose opening passes the full lower Hall/endpoint audit.

No shadow completion hypothesis remains before these switches.  The missing
statement is now a protected connectivity-plus-compiler theorem.

## 8. Adversarial audit

1. The factor is not PBBS/complement coherent merely because it lies in a
   PBBS-derived fixed-matching fibre.  A nontrivial fixed-`M_0` switch does
   not inherit the automatic complementary shadow identity.
2. Nine physical components and five quotient components are different
   ledgers.  Eight physical joins make an open path; a closed physical splice
   needs nine.  A quotient `C10` changes five full edge orbits, not five
   physical edges.
3. One quotient cycle is not one physical cycle unless its voltage is a unit.
4. Fixed-window support does not by itself prove arbitrary-width upper
   support after splicing; condition (3.3) is separately necessary.
5. The base Hall value 4,943 in Section 5 does not include the complete
   rank-six/rank-seven endpoint compiler.
6. The near-certificate is not a length-6,438 word.  The current rigorous
   numerical bound remains `6438 <= nu(15) <= 6458`.
7. Theorem 2.3 is not a general `C10` no-go.  It is an exact statewise no-go
   for this fixed factor and the component-transversal support-five class.
