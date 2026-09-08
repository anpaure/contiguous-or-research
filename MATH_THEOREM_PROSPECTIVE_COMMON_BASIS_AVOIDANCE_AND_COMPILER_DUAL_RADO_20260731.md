# Prospective common-basis avoidance and the compiler dual-Rado gate

Date: 2026-07-31  
Status: exact robust common-basis theorem, exact compiler-deletion
equivalence, and an unconditional bounded-scaffold physicalization theorem.
The remaining bulk Pascal collar inequality is isolated as one dual-Rado
rank condition.  No all-parameter `B(k)+O(1)` or `nu(k)=B(k)` theorem is
claimed.

## 0. Outcome

Three previously separate prospective requirements admit one clean
formulation.

1. The synchronized two-coordinate common basis can avoid a prescribed
   exceptional bank `Z` **exactly** whenever

   ```text
                              C|Z|<N.                    (0.1)
   ```

   Since `N/C~n/4`, every fixed-size repair scaffold can be protected from
   the puncture for all sufficiently large `n`.
2. Let `H` be one final common-guard compiler graph on physical cells.  The
   exact loss after deleting cells `D` is

   ```text
        delta_D(H)=|D|-r_(M_H^*)(D),                   (0.2)
   ```

   where `M_H` is the cell-side transversal matroid.  Thus the old compiler
   survives with zero loss precisely when `D` is independent in the dual
   transversal matroid.
3. If a prepared Pascal braid exposes one independently movable deletion
   task `i` with candidate-cell list `L_i`, then all deletion tasks can be
   discharged while preserving one exact common guard if and only if

   ```text
       r_(M_H^*)(union_(i in J)L_i)>=|J|               (0.3)
       for every task family J.
   ```

   This is Rado's theorem.  On a fixed matching face it reduces further to
   ordinary Hall into the unused-cell bank.

Consequently, on the prospectively transparent packet face, (0.3) gives

```text
                   R=P=T=delta_D(H)=0
```

and hence the sharp odd no-jump exposure bound

```text
                           |U|<=4 Phi+3.               (0.4)
```

The remaining all-dimensional theorem is no longer “find a common cap.”
It is: construct the physical Pascal braid so that its **bulk** collar
deletion lists satisfy (0.3), while residence, upper witnesses and topology
are transparent under every selected option.  The scalar inequality only
says that `r(M_H^*)>=|I|`; it does not imply the proper-subfamily inequalities
in (0.3).

## 1. Exact avoidance by the synchronized common basis

Use the notation of the automatic common-basis theorem:

```text
|E|=N,                 common rank=C,
alpha=C/N,
```

and let `M_1,M_2` be the two pulled-back dual incidence matroids on `E`.
That theorem proves the rank-density inequalities

```text
                         r_i(A)>=alpha|A|              (1.1)
```

for every `A subseteq E` and `i=1,2`.

### Theorem 1.1 (forbidden-bank common basis)

If `Z subseteq E` satisfies `alpha|Z|<1`, then `M_1` and `M_2` have a
common basis of order `C` contained in `E-Z`.

#### Proof

Put `z=|Z|`, and take any `S subseteq E-Z`.  Since matroid ranks are
integral, (1.1) gives

```text
r_1(S)+r_2((E-Z)-S)
 >=ceil(alpha|S|)+ceil(alpha(N-z-|S|)).                (1.2)
```

Write `x=alpha|S|` and `epsilon=alpha z<1`.  Because `alpha N=C` is an
integer,

```text
ceil(alpha(N-z-|S|))=C-floor(x+epsilon).               (1.3)
```

For every real `x` and `0<=epsilon<1`,

```text
                         floor(x+epsilon)<=ceil(x).     (1.4)
```

Thus the right side of (1.2) is at least `C`.  Edmonds' common-base
min--max theorem, applied on `E-Z`, supplies a common independent set of
order `C`, necessarily a basis of both restrictions.  `square`

For the Boolean constants

```text
 N=binom(2n,n-1),       C=Cat_(n+1),
 N/C=n(n+2)/(2(2n+1)).                                (1.5)
```

Hence every forbidden bank with

```text
                  |Z|<n(n+2)/(2(2n+1))                (1.6)
```

can be avoided exactly.  In particular, any bank of `b` fixed lower-risk
atoms is avoidable once `n` is larger than `4b+O(1)`.

### Corollary 1.2 (bounded packet puncture protection)

Fix `t=O(1)` pairwise-resource-private suspended-hex/ECO packets before
choosing the synchronized common basis.  Let `Z` contain every child atom
whose selection would puncture an auxiliary lower resource of a packet.
If `|Z|<N/C`, a synchronized common basis exists which preserves every
packet lower resource simultaneously.

Owner capacity causes no extra puncture condition when a packet reserves
only one literal slot at each private owner: a future seam anchor still has
that one slot.  The residual host must, of course, deduct the reserved slot.

This is stronger than the uniform-marginal survival estimate for a bounded
bank: it gives zero punctures, not merely expected `O(t/n)` punctures.

## 2. Compiler deletion is dual-matroid nullity

Let `H=(L,C;E_H)` be a bipartite target--cell graph with

```text
                              nu(H)=|L|=r.              (2.1)
```

Let `M_H` be the transversal matroid on the cell ground set `C`: a cell set
is independent when it can be matched injectively to distinct targets.
Then `r(M_H)=r`.  For `D subseteq C`, put

```text
                  delta_D(H)=r-nu(H-D).                (2.2)
```

### Theorem 2.1 (exact deletion-nullity identity)

For every `D subseteq C`,

```text
             delta_D(H)=|D|-r_(M_H^*)(D).              (2.3)
```

Consequently the following are equivalent:

1. `H-D` still has a target-saturating matching;
2. `r_(M_H^*)(D)=|D|`;
3. `D` is independent in the dual transversal matroid `M_H^*`.

#### Proof

The dual rank formula gives

```text
r_(M_H^*)(D)=|D|-r(M_H)+r_(M_H)(C-D)
            =|D|-r+nu(H-D).                           (2.4)
```

Rearrangement is (2.3), and the equivalences follow.  `square`

This identifies the exact extra geometry missing from scalar slack.  The
dual rank of the complete cell ground is

```text
                         r(M_H^*)=|C|-|L|,             (2.5)
```

the scalar number of unused cells.  The inequality `|D|<=r(M_H^*)` checks
only the full ground set.  It does not say that the particular Pascal
deletion bank `D` is independent.

## 3. The prospective deletion Rado theorem

Let `I` be a set of elementary deletion tasks.  Task `i` may be discharged
by deleting one cell from a nonempty list `L_i subseteq C`.  Assume that
the surrounding packet construction is option-transparent: any choice of
distinct listed cells which passes the compiler row produces the same
legal residence, upper-witness and physical-topology state.  This is a
construction hypothesis, not a consequence of the lists.

### Theorem 3.1 (dual-Rado prospective guard)

There are representatives

```text
                         d_i in L_i       (i in I)       (3.1)
```

whose deletion bank `D={d_i:i in I}` preserves a target-saturating common
guard if and only if

```text
 r_(M_H^*)(union_(i in J)L_i)>=|J|       for every J subseteq I.  (3.2)
```

Whenever (3.2) holds, a compiler matching avoiding all selected cells
exists.  If `H` is trace guarded in the sense of the guarded common-cap
theorem, that matching is automatically a literal zero-defect common-cap
compiler.

#### Proof

Rado's independent-transversal theorem applied to the lists `L_i` in the
matroid `M_H^*` gives representatives whose set is dual-independent exactly
under (3.2).  Theorem 2.1 converts dual independence into a saturating
matching in `H-D`.  Trace guarding then promotes every such matching to an
exact common cap.  `square`

The deficient form is also exact.  The maximum number of deletion tasks
simultaneously selectable while keeping the old guard feasible is

```text
 min_(J subseteq I)(|I-J|+r_(M_H^*)(union_(i in J)L_i)).           (3.3)
```

Thus a bound

```text
 r_(M_H^*)(union_(i in J)L_i)>=gamma|J|-beta                       (3.4)
```

repairs at least `gamma|I|-beta` tasks in one round and gives the usual
regenerative contraction if the same list-rank inequality is re-exported.

### Corollary 3.2 (fixed-unused-bank Hall criterion)

Fix one target-saturating matching `M_0` in `H`, and let

```text
                    B=C-cells(M_0).                    (3.5)
```

Then `B` is a basis of `M_H^*`.  If the bipartite graph

```text
                         i -- b iff b in L_i cap B      (3.6)
```

has a matching saturating `I`, choose its cells as `D`.  The **same**
compiler matching `M_0` survives unchanged.

In particular, put

```text
 lambda=min_i |L_i cap B|,
 mu=max_(b in B)|{i:b in L_i}|.                       (3.7)
```

If `lambda>=mu`, the matching in (3.6) exists.

#### Proof

The complement of a basis of `M_H` is a basis of `M_H^*`, proving the first
claim.  A matching in (3.6) chooses distinct elements of `B`; every subset
of a dual basis is independent.  Alternatively, the chosen cells are all
unused by `M_0`.  For the final assertion, every `J subseteq I` sends at
least `lambda|J|` incidences into `N(J)`, while every cell receives at most
`mu`; hence `|N(J)|>=lambda|J|/mu>=|J|`.  Hall applies.  `square`

This is the most concrete positive target produced by the audit: construct
the Pascal deletion lists so that they expand into the unused cells of one
trace-guarded compiler matching.  The abstract counterexample in the
exposure-pressure theorem fails exactly here: every deletion list is forced
onto a used cell and misses the unused basis.

### Theorem 3.3 (one augmented matching is the whole compiler gate)

Form one bipartite graph `A(H,L)` with right shore `C` and left shore

```text
                         L disjoint union I.             (3.8)
```

An old compiler target `ell in L` keeps its neighbourhood in `H`, while a
deletion task `i in I` has neighbourhood `L_i`.  Then the following are
equivalent.

1. The deletion tasks have distinct representatives `d_i in L_i` whose
   bank `D` leaves a target-saturating matching in `H-D`.
2. `A(H,L)` has a matching saturating `L disjoint union I`.
3. For all `X subseteq L` and `J subseteq I`,

   ```text
   |N_H(X) union union_(i in J)L_i|>=|X|+|J|.          (3.9)
   ```

#### Proof

Given (1), combine the matching in `H-D` with the task representatives.
Their cell sets are disjoint, giving (2).  Conversely, restrict a matching
in (2) to the two left types.  Its task cells form `D`, and its target cells
give a matching in `H-D`, proving (1).  Finally (2) and (3) are ordinary
Hall.  `square`

This formulation also absorbs the three newborn lower targets: add them as
ordinary target vertices, with their individually sound cell incidences,
before solving the augmented matching.  Thus one integral matching chooses

```text
old target cells + newborn target cells + cells sacrificed to contraction.
                                                               (3.10)
```

There is no subsequent compiler reroute.

### Corollary 3.4 (prospective guarded-convex compiler)

Order the cell bank as `C_1<...<C_m`.  Suppose every old/new target
neighbourhood and every elementary deletion list is a nonempty interval

```text
                              [ell_a,r_a].              (3.11)
```

Suppose the target-incidence subbank is trace guarded.  Then a zero-loss
prospective compiler exists if and only if

```text
 |{a in L disjoint union I:[ell_a,r_a] subseteq [p,q]}|
       <=q-p+1                    for every [p,q].      (3.12)
```

Sorting all target and deletion objects by nondecreasing right endpoint and
assigning each the first unused allowed cell constructs it.  After the
assignment, discard the cells assigned to deletion tasks and retain the
target assignments; trace guarding makes the latter a literal common cap.

#### Proof

This is the interval-neighbourhood Hall theorem applied to the augmented
graph in Theorem 3.3.  The standard earliest-deadline exchange proves the
greedy algorithm.  Deletion objects are reservation tokens, not cap labels,
so they are ignored when the maximal common cap is formed.  Every retained
target edge lies in the trace-guarded bank.  `square`

Corollary 3.4 is a genuinely smaller construction target than arbitrary
common-cap SAT: exhibit one common cell order in which the sound target bank
and the Pascal deletion mobility are convex, then verify only interval
capacity cuts.  If the natural deletion options are coupled blocks rather
than elementary cells, this corollary does not apply without a sound block
expansion.

### Corollary 3.5 (uniform dual-density criterion)

Suppose, for some `alpha>0`,

```text
                 r_(M_H^*)(A)>=alpha|A|               (3.13)
                 for every A subseteq C.
```

If

```text
 |union_(i in J)L_i|>=|J|/alpha       for every J subseteq I,     (3.14)
```

then the prospective compiler exists.  A local sufficient condition for
(3.14) is

```text
 lambda=min_i|L_i|,       mu=max_c |{i:c in L_i}|,
                         alpha lambda>=mu.             (3.15)
```

#### Proof

Equations (3.13)--(3.14) imply the Rado cuts (3.2).  For (3.15), incidence
counting gives

```text
                 |union_(i in J)L_i|>=lambda|J|/mu.    (3.16)
```

`square`

Neither trace guards nor convex/laminar target neighbourhoods imply a
positive `alpha`.  Take one target whose sole cell is `c_1`, together with
arbitrarily many extra cells ordered after it.  This is a convex,
trace-guardable compiler, but `c_1` is a coloop of `M_H` and hence a loop of
`M_H^*`; (3.13) fails on `{c_1}` for every positive `alpha`.  Uniform dual
rank density is therefore a separate robustness theorem, not a consequence
of the existing guarded-convex compiler.

This failure is present in the authenticated Boolean data, not only in the
one-target abstraction.  The K16 universal-assignment closure finds 14,060
target--cell assignments present in every residual marginal perfect
matching.  Each corresponding cell is a coloop of the cell transversal
matroid and a loop of its dual.  Thus the full successful K16 marginal
compiler has dual density zero before those forced pairs are contracted.
Any positive-density argument must first contract the forced core and state
its density on the residual ground.

## 4. The actual tail-start deletion geometry is Ferrers, not matroidal

The elementary-list language above is not automatically the language of a
monotone-deadline staircase.  On the canonical tail-start face, the exact
geometry can be written explicitly.

Use the maximal depth-`d` atlas with non-tail cells

```text
       (i,ell) <-> [i,i+ell-1],
       0<=i<W,             1<=ell<=d,                 (4.1)
```

together with the unchanged triangular tail bank.  A nondecreasing deadline
threshold vector

```text
                         0<=a_1<=...<=a_d<=W            (4.2)
```

retains `(i,ell)` exactly when `i>=a_ell`.  Hence its deleted bank is

```text
             D(a)={(i,ell):0<=i<a_ell}.               (4.3)
```

This is the Ferrers-ideal form hidden in the scalar identity
`Loss(a)=sum a_ell`.

Fix a trace-guarded compiler matching `M_0` on the maximal atlas and let
`B` be its unused-cell dual basis.  Define the initial unused-prefix length
in row `ell` by

```text
 u_ell=min({i:(i,ell) is used by M_0} union {W}).       (4.4)
```

### Theorem 4.1 (exact fixed-basis Ferrers criterion)

For every monotone threshold vector `a`, the same compiler matching `M_0`
survives the staircase contraction if and only if

```text
                         a_ell<=u_ell       (1<=ell<=d). (4.5)
```

The largest scalar loss supportable inside the unused basis is

```text
 Cap_B=sum_(ell=1)^d min_(j>=ell)u_j.                 (4.6)
```

For every integer `0<=s<=Cap_B`, there is a monotone `a` of sum `s` whose
whole deletion ideal lies in `B`.

If residence supplies a nondecreasing componentwise lower threshold
`rho=(rho_1,...,rho_d)`, then a compiler-preserving tail-start schedule with
`a>=rho` and scalar budget `sum a<=sigma` exists if and only if

```text
 rho_ell<=u_ell       for all ell,
                         sum rho_ell<=sigma.            (4.7)
```

#### Proof

By (4.3), the deletion cells in row `ell` are precisely its first `a_ell`
cells.  They are all unused by `M_0` exactly when `a_ell<=u_ell`, proving
(4.5).

Monotonicity forces

```text
                 a_ell<=min_(j>=ell)u_j.               (4.8)
```

The suffix-minimum vector on the right is itself nondecreasing, so it is
the coordinatewise greatest feasible vector and gives (4.6).  Feasible
deletion banks are the order ideals of the finite Ferrers poset bounded by
that greatest vector.  Prefixes of a linear extension give an ideal of
every cardinality from zero through `Cap_B`, proving the interpolation
claim.  Finally, when `rho` is nondecreasing, choosing `a=rho` proves
sufficiency in (4.7); necessity follows from (4.5) and the scalar budget.
`square`

This is substantially cheaper than bulk Rado on the fixed-matching face:
one reads `d` unused-prefix lengths and compares them with the residence
frontier.  It is also exactly where the existing theory stops.  The current
Pascal notes prove the threshold/Ferrers formula and the residence frontier,
but do not construct a trace-guarded compiler matching whose unused prefixes
satisfy (4.7).

There is a second scope condition.  Retiming changes the middle support
intervals as well as deleting lower-cell identities.  A matching which is
exact for one threshold vector is not automatically trace guarded for a
different vector.  Theorem 4.1 controls the **cell-disjointness/compiler
matching row**.  To call the retained matching a literal common cap, its
bank must carry the point/row guards for the chosen final threshold vector.

The K16 optimum calibrates the prefix mechanism without proving its
inheritance.  Its construction threshold is

```text
                         tau=(0,0,6386),               (4.9)
```

while the selected lower matching first uses length-one, length-two and
length-three cells at starts `0,2,6390`, respectively.  Hence, on cell
identities alone, the length-three row retains four further prefix units.
The independently computed residence frontier is `(0,0,6384)`.  This is
exactly the favourable inequality predicted by (4.7), but the K16 common
cap was solved at the final threshold and does not constitute a backward
maximal-atlas trace-guard theorem.

### Proposition 4.2 (the Ferrers choices are not a matroid)

Fixed-cardinality staircase deletion banks do not in general form the bases
of a matroid.  At `d=2,W=4`, the sum-four threshold vectors

```text
                         a=(0,4),       b=(2,2)         (4.10)
```

give two legal deletion ideals.  Take `x=(2,2)` from `D(a)-D(b)`.  Neither
element of `D(b)-D(a)={(0,1),(1,1)}` can replace `x` while leaving a Ferrers
ideal of order four.  Basis exchange fails.

Consequently one may not treat the `sum a_ell` deleted cells as independent
Rado tasks unless the physical braid supplies additional one-cell mobility.
The correct native object is an order ideal (or a monotone-flow path), and
Theorem 4.1 is the exact fixed-basis solution on that native face.

### Proposition 4.3 (literal K16 nonconvexity)

The complete authenticated K16 individually sound target--cell graph is not
convex on the cell shore under **any** cell order.  Three physical cells are

```text
 c_1=17918=[8101,8102],
 c_2= 8976=[4488,4488],
 c_3=  626=[ 313, 313],                              (4.11)
```

and three lower targets have the restricted incidence rows

```text
 target  8712 : 1 1 0,
 target 40968 : 0 1 1,
 target 24584 : 1 0 1.                               (4.12)
```

No ordering of three columns makes all three two-element supports
consecutive: whichever column is placed in the middle makes the other two
the nonconsecutive pair in one row.  Since the consecutive-ones property is
hereditary under deleting columns, (4.12) is a Tucker obstruction to every
global cell order.

In the builder's natural start/length cell order, 10,053 of the 26,331
target neighbourhoods are intervals and 16,278 are not.  Therefore
Corollary 3.4 cannot be applied to the full natural bank.  A positive convex
proof must prune to a matching-complete trace-guarded subbank and prove that
the pruning removes this and every other Tucker obstruction; convexity is
not inherited from physical interval cells themselves.

## 5. Bounded protected scaffolds coexist with the arbitrary-`Q` forest

The arbitrary-common-basis physical-forest theorem remains valid after a
fixed number of literal packet resources is reserved.

### Theorem 5.1 (bounded-scaffold physicalization)

Fix `t=O(1)` pairwise-resource-disjoint packet off states whose physical
projection is a forest.  Choose a synchronized common basis avoiding their
lower puncture-risk bank by Theorem 1.1.  On each punctured shore there is a
`P-o(P)` physical side forest disjoint from every reserved outer resource
and literal owner slot.  After deleting `O(t)` additional selected atoms,
the union of the side forest with the fixed packet projection is again a
linear forest.  The statement is uniform over the resulting common basis.

#### Proof

Delete from `G_Q` every host atom incident with a reserved resource.  There
are `O(t)` such resource vertices and every host degree is at most

```text
                         D_0=2(n+1)(n+2).              (5.1)
```

Thus the edge ledger loses only `O(tD_0)` atoms.  Maximum degree,
codegree, and every short-cycle configuration degree can only decrease.
The Delcourt--Postle colouring argument therefore still returns a
`P-o(P)` matching; removal of its long projected cycles gives a linear
forest, exactly as in the arbitrary-`Q` theorem.

The selected forest uses none of the reserved slots, so adjoining a packet
off state preserves every degree cap.  Add the `O(t)` packet edges one at a
time.  Whenever an added edge closes a cycle, delete one selected body edge
from the old path between its endpoints.  The packet projection is itself
a forest, so this process deletes at most one body edge per packet edge and
leaves a forest.  The total loss remains `o(P)`.  `square`

This theorem gives a genuine quantifier order:

```text
bounded prospective packet scaffold
 -> synchronized common basis avoiding it
 -> arbitrary-Q near-forest body around it.            (4.2)
```

It does not turn the `P-o(P)` body into an exact `P`-edge side factor.

## 6. Exact implication for sparse exposure

Combine the preceding theorem with the exposure decomposition.  Consider
an odd no-jump same-parity step and assume a prepared packetized child lift
with the following properties.

1. Every old live token has at most four passive child descendants.
2. The packet baseline and every option are resident, preserve the declared
   all-width upper witnesses, and preserve the contracted physical forest;
   hence no fresh residence, provider or topology task is born.
3. Apart from the three genuinely newborn lower targets, every compiler
   change is one elementary deletion task with list `L_i`.
4. One trace-guarded common compiler `H` satisfies the dual-Rado inequalities
   (3.2) for those lists.

### Theorem 6.1 (prospective packet implication)

Under clauses 1--4 one may choose the packet options and one terminal
common-cap matching so that

```text
                         R=P=T=delta_D(H)=0,            (5.1)
```

and therefore

```text
                              |U|<=4 Phi+3.             (5.2)
```

#### Proof

Theorem 3.1 chooses the compiler-safe deletion options and supplies a
terminal matching in `H-D`; trace guarding makes it a literal common cap.
Clause 2 makes the other three fresh pressures zero.  The proof-safe
exposure decomposition contributes four descendants per old token and the
three lower births, giving (5.2).  `square`

This theorem is an actual construction once its lists and trace guards are
displayed: solve one matroid independent-transversal instance, then retain
the resulting matching.  It is stronger than checking separate marginal
Hall rows.

## 7. Exact remaining Boolean theorem and scope obstruction

For the odd no-jump scalar recurrence, the bulk deletion count is

```text
                  |I|=d Cat_r+3 binom(d+1,2).          (6.1)
```

up to the three newborn target insertions already separated in the exposure
ledger.  The scalar no-jump inequality implies only

```text
                         |I|<=r(M_H^*).                (6.2)
```

The missing positive theorem is the proper-subfamily strengthening (3.2).

It cannot be omitted.  Let `M_H^*` have one nonloop element `b` and let
every deletion task have the singleton list `{b}`.  Every task is
individually compiler-safe and (6.2) may be made true by adjoining unused
dual elements which occur in no list.  Nevertheless two tasks violate
(3.2), and no simultaneous deletion choice exists.  This is the exact
matroid form of “scalar slack without mobility.”

There is one further scope lock.  Theorem 3.1 treats **elementary** tasks:
one option chooses one deleted cell.  If one braid option simultaneously
forces a block of several deleted cells, the problem becomes an
independent-block selection (matroid parity/hypergraph-transversal) problem;
splitting the block into independent lists is unsound unless every
combination of its cell choices is physically realizable.  A positive
Pascal construction should therefore either:

* expose independently movable one-cell deletion packets; or
* prove a block-Rado analogue for its actual coupled option family.

The automatic synchronized common basis and the arbitrary-`Q` near-forest
theorem now remove two genuine quantifier difficulties: bounded protected
scaffolds can be chosen before `Q` and physically surrounded afterwards.
They do not prove the bulk dual-Rado inequality, exact side cover-down, or
trace-guarded compiler bank.  Those are the remaining integral correlation
rows.

## 8. Audit

The accompanying dependency-free audit checks:

* the ceiling identity in Theorem 1.1 for the exact Boolean ratios through
  a broad finite range;
* the deletion-nullity identity on exhaustive small bipartite graphs;
* the Rado/Hall fixed-basis criterion on exhaustive small list systems; and
* the exact odd no-jump scalar deletion ledger.

Run

```text
python3 scratch/audit_prospective_common_basis_and_dual_rado_20260731.py
```

which writes

```text
scratch/prospective_common_basis_and_dual_rado_20260731.audit.json.
```
