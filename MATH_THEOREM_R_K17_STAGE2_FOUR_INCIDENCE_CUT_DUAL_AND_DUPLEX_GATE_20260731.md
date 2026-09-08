# K17 Stage-2 service: the exact cut dual, the four-incidence scope, and the staggered duplex gate

## 0. Status

This note concerns the frozen K17 Stage-2 service assignment built on

```text
scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_support7115_20260731.components
scratch/k17_fragment_endpoint_matching_recycle_protected_20260731.result.json
```

and the two exact downstream audits

```text
scratch/k17_stage2_old_target_cut_kernel_20260731.audit.json
scratch/bflow_service_maxretention.json.
```

It proves three things.

1. There is an explicit Hoffman cut of deficit two.  Consequently **no
   alternating circuit of any length** can install all 1,838 Stage-2 seams
   while retaining the entire advertised protected-incidence bank.  By the
   first all-service state, at least two incidences from an explicit
   twenty-edge entering set must already be absent; no fixed pair is
   individually forced.
2. The supplied maximum-retention factor loses four protected incidences, but
   these four losses do **not** create four service-target holes.  All four
   affected service targets have explicit alternative literal intervals in
   the factor, and all 1,838 service targets survive.
3. Incidence retention is nevertheless far from all-target protection: that
   same factor has 6,499 old upper-target holes.  Thus arbitrary balanced
   b-flow, even at the exact four-incidence retention optimum, is not the
   missing protected alternating-circuit theorem.

An exact staggered-duplex criterion is stated in Section 6.  No K17 word and
no assertion that `nu(17)=B(17)` is made.

## 1. Residual factor notation

Let `G=(U,L;E)` be a finite bipartite graph with `|U|=|L|`.  In the K17 application, `U` is
the rank-nine shore, `L` is the rank-eight shore, and `uv in E` means
`v subset u`.  A balanced incidence factor is a set `F subset E` with

```text
d_F(u)=2  (u in U),             d_F(v)=2  (v in L).       (1.1)
```

Each rank-eight vertex then pairs its two selected rank-nine neighbours and
therefore contributes one Johnson edge and one lower-q1 colour.  Hence every
balanced incidence factor is automatically exact on the complete lower-q1
palette.  This says nothing about residence or upper intervals.

Let `K subset E` be a prescribed incidence bank with `d_K<=2` on both
shores.  Put

```text
a_K(u)=2-d_K(u),       c_K(v)=2-d_K(v),       H=G\K.       (1.2)
```

Thus completing `K` to a balanced factor is the unit-capacity transportation
problem which sends `a_K(u)` units from each `u` through `H` and receives
`c_K(v)` units at each `v`.

## 2. Exact Hoffman cut and release calculus

### Theorem 2.1 (residual balanced-factor criterion)

The bank `K` extends to a balanced incidence factor if and only if, for every
`A subset U` and `B subset L`,

```text
a_K(A) <= c_K(B) + e_H(A,L\B).                         (2.1)
```

Here `a_K(A)=sum_(u in A)a_K(u)`, similarly for `c_K(B)`, and
`e_H(A,L\B)` is the number of available unit-capacity incidences from `A`
to `L\B`.

#### Proof

Use the standard network with source-to-`u` capacity `a_K(u)`, every edge of
`H` directed from `U` to `L` with capacity one, and `v`-to-sink capacity
`c_K(v)`.  Total source and sink demands agree.  The cut whose source side is
the source together with `A union B` has capacity

```text
a_K(U\A)+e_H(A,L\B)+c_K(B).
```

It has capacity at least `a_K(U)` exactly when (2.1) holds.  Max-flow/min-cut
and integrality of unit-capacity flow prove the claim.  QED.

Let `P subset K` be a collection of protected incidences which may be
released.  For `R subset P`, set `K_R=K\R` and `H_R=G\K_R`.  Define the cut
defect

```text
Delta_K(A,B)=a_K(A)-c_K(B)-e_H(A,L\B).                  (2.2)
```

### Lemma 2.2 (exact release cancellation)

For every `A,B,R`,

```text
Delta_(K_R)(A,B)
  = Delta_K(A,B) - |R intersect E(U\A,B)|.              (2.3)
```

In particular, releasing an incidence with upper endpoint in `A` cannot
improve this cut, regardless of its lower endpoint.  The only useful releases
are incidences entering `B` from outside `A`.

#### Proof

Removing one prescribed incidence raises the residual demand at its upper
endpoint and the residual capacity at its lower endpoint, and makes that
incidence available in `H_R`.  Therefore

```text
a_(K_R)(A)=a_K(A)+|R intersect E(A,L)|,
c_(K_R)(B)=c_K(B)+|R intersect E(U,B)|,
e_(H_R)(A,L\B)=e_H(A,L\B)+|R intersect E(A,L\B)|.
```

Substitution cancels the `E(A,B)` and `E(A,L\B)` terms, leaving precisely
`-|R intersect E(U\A,B)|`.  QED.

This cancellation is the relevant cut dual for circuit absorbers.  It is
independent of whether the eventual exchange is a C6, C8, or a nonlocal
alternating circuit.

## 3. The frozen K17 cut

Let `S` be the 3,676 incidence set of the 1,838 fixed service seams, and let
`P` be the 13,600 occurrence-labelled protected incidences (6,800 complete
old Johnson edges) advertised by their chosen service witnesses.  Set
`K=S union P`.  The frozen bank has no local degree overload.

Take

```text
A = {73379,109258},

B = {7843,43722,69283,71331,72867,73251,73347,73377,
     73378,101066,107210,108746,109130,109194,109250,
     109256}.                                            (3.1)
```

The independent cut payload records

```text
a_K(A)=4,        c_K(B)=0,        e_H(A,L\B)=2.          (3.2)
```

Direct replay also gives

```text
|P intersect E(U\A,B)|=20.                              (3.3)
```

The cut therefore identifies an explicit twenty-edge release class, not an
individually forced pair.

### Corollary 3.1 (unavoidable protected release)

Every balanced incidence factor containing all 1,838 service seams omits at
least two incidences of `P` which enter `B` from `U\A`.

#### Proof

The cut defect is `Delta_K(A,B)=2`.  If `R` is the set of protected
incidences not retained, feasibility and Lemma 2.2 give

```text
0 >= Delta_(K_R)(A,B)
  = 2-|R intersect E(U\A,B)|.
```

QED.

### Corollary 3.2 (one-shot duplex obstruction)

There is no balanced factor which simultaneously contains all service seams
and the complete advertised old protected bank.  Consequently there is no
one-shot make-before-break exchange—of any circuit length—which first
installs every service seam and only afterwards releases old protected
incidences.

Any successful protected transport must instead change witness selection
before or while at least two incidences entering (3.1) are released.

The four incidences omitted by the supplied exact maximum-retention factor
are

```text
(7847,  7843),
(79406, 71214),
(96540, 80156),
(109506,109250).                                         (3.4)
```

The first and fourth are the two releases entering the displayed deficient
lower set in this particular optimum; the cut does not force these two named
incidences individually.  The supplied integral maximum-cost b-flow has objective 13,596
out of 13,600, so its exact retained-incidence loss is four.  This numerical
four-optimum is an input artifact of this note; Theorem 2.1 and Corollary 3.1
give the solver-free two-unit cut certificate and the exact cut semantics.

For reference, the complete weighted transportation dual which certifies a
claimed four-optimum is the following.  With service incidences fixed, let
`d_u,d_v` be residual degrees and let `w_e=1` on optional protected
incidences and zero otherwise.  The integral primal is

```text
max sum_e w_e x_e,
sum_(e at u)x_e=d_u,  sum_(e at v)x_e=d_v,  0<=x_e<=1.   (3.5)
```

Its TDI dual is

```text
min sum_u d_u alpha_u + sum_v d_v beta_v + sum_e z_e,
alpha_u+beta_v+z_e >= w_e,       z_e>=0,                (3.6)
```

where `alpha,beta` are free.  Thus an independently portable certificate of
the exact four floor is a feasible (3.6) assignment of value 13,596 together
with the displayed primal factor.  The current JSON freezes the primal and
the exact solver status but does not list these dual multipliers.

## 4. Four incidence losses are not four target losses

The four partial protected old edges affect the advertised service rows
(using zero-based indices in the frozen assignment)

```text
814, 1024, 1325, 1352.                                  (4.1)
```

All other service rows retain their entire advertised old suffix/prefix and
residence-protection edge set.  Since the corresponding service seam is
fixed, their literal service intervals remain in the factor.

The four affected targets also survive, but by alternative intervals.  In
the largest cycle of the maximum-retention factor the following consecutive
rank-nine strings occur (positions are zero-based in that frozen cycle):

```text
row 814,  position 2607:
  15ea2,14fa2,14ba3,14b33       OR = 15fb3;

row 1024, position 11683:
  17c1c,1791c,1790e             OR = 17d1e;

row 1325, position 2671:
  1a3aa,193aa,197a2,117a6       OR = 1b7ae;

row 1352, position 5649:
  1b343,193c3,18bc3             OR = 1bbc3.              (4.2)
```

Every listed vertex has rank nine and every consecutive symmetric difference
has size two.  Hence these are literal Johnson intervals, not merely setwise
OR identities.  This proves that all 1,838 newly serviced targets remain
covered in the maximum-retention factor.

The conclusion is deliberately limited.  The alternative intervals (4.2)
do not certify the coordinate residence DFA at their external collars, nor
do they restore any unrelated old target.

## 5. Exact counterexample to incidence-only protection

The direct Stage-2 cut-and-seam partial chronology has the following exact
ledger:

```text
new holes serviced                         1838 / 1838,
old upper targets lost                     3489,
loss by rank                         10:1864, 11:1221,
                                     12:386, 13:18,
open lower colours                         1498.          (5.1)
```

Completing the same service bank by maximum protected-incidence retention
does not repair the old-target problem.  Its balanced factor has eight
components of lengths

```text
21322,2964,7,5,3,3,3,3,
```

and, although all 1,838 service targets survive, it has

```text
old upper holes                            6499,
by rank                              10:4066, 11:2036,
                                     12:388, 13:9.        (5.2)
```

Because the old factor's only holes were exactly the 1,838 service targets,
and all of those are now covered, every hole in (5.2) was previously covered.

### Theorem 5.1 (four-incidence blindness)

For the frozen K17 Stage-2 atlas, the following implication is false:

> all service seams + maximum retention of their occurrence-labelled
> protected incidences + exact balanced lower-q1 factor
> implies all-depth upper retention.

It is false even when only four of 13,600 optional protected incidences are
lost.  Therefore an arbitrary b-flow or a matroidal incidence-exchange
argument cannot substitute for an all-target protected-circuit theorem.

The reason is quantifier-level: `P` protects one chosen interval for each
new service target.  It is not a witness transversal for every previously
covered target.  The all-target survivor condition is a blocker-clutter
condition on literal paths, not an incidence-cardinality objective.

## 6. The exact staggered-duplex theorem

Let `T` be a finite target family.  For a factor `F`, let `W_F(t)` be the
family of occurrence-labelled directed or undirected factor intervals whose
literal OR equals `t`.  Let `D` be the selected residence DFA, including both
external collars.  A guard section is a choice

```text
Q={Q_t in W_F(t): t in T}.                                 (6.1)
```

Write `supp(Q)` for the incidence edges used by all chosen intervals and by
their certified DFA collars.

### Theorem 6.1 (staggered duplex bridge factors, exact finite form)

Suppose guard sections `Q^0,...,Q^m` and service-incidence banks
`S^0,...,S^(m-1)` have been chosen.  There are balanced bridge factors
`F^0,...,F^(m-1)` such that, at stage `i`,

```text
S^i union supp(Q^i) union supp(Q^(i+1)) subset F^i        (6.2)
```

if and only if all local prescribed degrees in (6.2) are at most two and,
for every `i` and every `A subset U,B subset L`, the residual bank in (6.2)
satisfies (2.1).

Successive bridge factors `F^(i-1),F^i` both contain `supp(Q^i)`.  Their
symmetric difference therefore decomposes into alternating circuits disjoint
from `supp(Q^i)`.  Thus the bridge factors give an incidence-level
make-before-break transport which never deletes the currently designated
target witnesses.

If in addition

1. every projected added/deleted Johnson edge multiset has the same lower
   colour ledger (automatic when each `F^i` spans both inclusion shores),
2. every selected target interval in `Q^i` and `Q^(i+1)` is literal in the
   relevant factor, and
3. the alternating circuits between successive bridge factors admit an
   order and orientation for which the product residence DFA accepts every
   intermediate reconnected collar,

then the sequence has zero selected-target and zero residence defect at every
handoff.

#### Proof

Necessity of the degree and cut conditions follows from Theorem 2.1 applied
to each `F^i`.  Conversely those conditions give an integral completion of
each bank (6.2).  Since both the old and new guard sections coexist in
`F^i`, one may designate `Q^(i+1)` before retiring `Q^i`.  Moreover, the
red and blue degrees in `F^(i-1) triangle F^i` agree at every vertex, so its
edges decompose into even alternating circuits, none meeting the common bank
`supp(Q^i)`.  Toggling those circuits transports between the bridge factors.
The three final conditions respectively give the lower-q1 ledger, literal
target coverage throughout the circuit sequence, and residence throughout
that sequence.  QED.

This theorem is stagewise.  To obtain transport from a prescribed source
factor `F_src` to a prescribed destination factor `F_dst`, one must also
anchor the endpoint guards by

```text
supp(Q^0) subset F_src intersect F^0,
supp(Q^m) subset F^(m-1) intersect F_dst,                (6.3)
```

or identify those endpoints with the first and last bridge factors.  The
two endpoint symmetric differences must themselves admit residence-safe
circuit orders.  More generally, the residence hypothesis quantifies over
every intermediate toggle state, including cyclic closure.  If the DFA is
not reversal-closed, each guard section must carry its oriented occurrence
and collar state; undirected incidence support alone is insufficient.

### Corollary 6.2 (what a long-circuit absorber must do here)

Circuit length alone cannot repair the Stage-2 obstruction.  A successful
C8 or longer PBBS switch bank must provide a staggered sequence of new guard
sections.  Before the complete Stage-2 service bank is present, it must
replace at least two protected incidences entering the explicit lower set
`B` in (3.1); in the supplied maximum-retention face, four incidence roles
are changed.  Every intermediate union of old/new guards must pass all
Hoffman cuts, and its collars must pass the residence DFA.

For the four advertised service rows, targetwise replacement is already
available through (4.2).  The genuinely missing absorber is instead a guard
section for the thousands of old targets in (5.1)--(5.2), compatible with
the same balanced factor and residence.  No such section is constructed in
the present data.

## 7. Sharp remaining theorem

The finite PBBS task is now the following, with no ambiguity between edge
retention and target retention.

> Choose an all-target occurrence-labelled guard section, and a collection
> of C8 or longer alternating circuits, so that the guards admit a
> staggered-duplex ordering satisfying every cut (2.1), every lower-colour
> row, and the full residence DFA; the last factor must be connected (or
> openable at controlled seam cost).

The Stage-2 assignment proves provider abundance and moves all 1,838 current
holes.  The cut (3.1) proves that its advertised guard bank cannot be kept
monotonically.  The four-incidence optimum shows that the balanced degree
obstruction is small, while (5.2) proves that the all-target obstruction is
not.  This is the precise boundary; it is not a proof or disproof of
`nu(17)=B(17)`.
