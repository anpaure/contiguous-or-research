# Finite-order twisted conveyors: exact repetition, carrier norm, and the Catalan product obstruction

Date: 2026-07-26

Method: pure mathematics only.

## Authoritative geodesic correction

The serial permutation and orbit-norm algebra below is valid for abstract
open path ledgers and, conditionally, for a genuinely exterior-moving
physical packet.  It is **not** a construction inside an ordinary
fixed-exterior minimum-wreath slab.

If a nominal rank-\(r\) slab begins at
\(O_L\cup P\) and ends at
\(O_R\cup(J\setminus\tau(P))\), and
\(e=|O_L\setminus O_R|\), then

\[
 d_J\bigl(O_L\cup P,O_R\cup(J\setminus\tau(P))\bigr)
 =e+|P\cap\tau(P)|.
\tag{C.1}
\]

Every contiguous segment of a minimum wreath is geodesic.  Therefore a
physical \(r\)-step realization requires

\[
                         e=|P\setminus\tau(P)|
\tag{C.2}
\]

on every row.  With fixed exterior, \(e=0\), so
\(\tau(P)=P\) pointwise.  A later inverse or a finite-order repetition
cannot repair the first nongeodesic segment.

Accordingly, every nonidentity occurrence of “slab,” “conveyor,”
“physical copy,” or “exact factor” below must be read as conditional on:

1. exterior motion satisfying (C.2) rowwise;
2. a complete ambient state/colour, seam, and crossing-collar ledger; and
3. a globally geodesic serial realization.

The abstract cycle catalogue alone supplies none of these.  The corrected
physical supply/demand audit is in
MATH_THEOREM_BALLOT_SERIAL_TWISTED_CYCLE_SUPPLY_LEDGER_20260726.md.

## 0. Outcome

At the abstract endpoint-ledger level, a finite-order twist removes the
need for a separate inverse permutation, but only in a serial label
conveyor.  Physical promotion requires the correction above.  It is not
enough to place isomorphic atoms in independent Catalan slots.

Let a twisted local factor have port permutation `tau` of order `d` and
row semilengths `q(P)`.  Under `d` abstract serial copies—or physically
realized exterior-moving seams satisfying (C.2)—which transport the same
port label from one slab to the next, the total monodromy is `tau^d=1`.
The exact row-length condition is

\[
 \sum_{j=0}^{d-1}q(\tau^jP)=dr\qquad(P\in D).          \tag{0.1}
\]

Equivalently, every `tau`-orbit must have average row length `r`.  Thus
strict atoms, including clean same-phase alternating-cycle toggles of a
strict Chung--Feller factor, pass the length test automatically.  A general
degree factor does not.

For a row-resolved carrier vector `delta`, repetition produces the orbit
norm

\[
                     N_\tau\delta
        =(1+\tau+\cdots+\tau^{d-1})\delta.             \tag{0.2}
\]

The carrier adds as `d delta` exactly on the `tau`-invariant part.  Equal
cycle orientation is necessary but not sufficient: the physical target
charts and exterior collars must transport the carrier covariantly.

There is an exact internal implementation at the abstract path-ledger
level.  If the same `l` row strands
support `l` clean coherent alternating `C_(2l)` switches at successively
later synchronized phases, with the same cyclic strand order, then the
switches remain legal after one another, every path stays strict, and the
endpoint twist is `tau^l=1`.  Literal minimum-wreath promotion is still
subject to (C.2) and the full moving-exterior collar ledger.

The canonical recursion does **not** supply this merely by giving `l`
independent `D_s` holes.  On the Cartesian port set `D_s^l`, the `l`
slotwise atoms act as

\[
                  (P_1,\ldots,P_l)
       \longmapsto(\tau P_1,\ldots,\tau P_l),           \tag{0.3}
\]

not as `P -> tau^l P`.  Moreover the canonical first Chung--Feller
incidence matching is uniquely forced, so it contains no same-phase
alternating cycle at all.  A positive-density finite-order construction
therefore needs a new interior **label-conveyor atlas**; it is not a formal
consequence of Catalan recursion.

## 1. Exact repeated-slab theorem

Let `D` be a port set and let `F` be a twisted local path factor whose row
rooted at `P` exits with port label `tau(P)`.  Let `q(P)` be the number of
local upper-colour states in that row.  The average is `r`, but `q(P)` need
not equal `r`.

Take `k` physical copies `S_1,...,S_k`.  Let

\[
                    \alpha_j:D_j\longrightarrow D_{j+1} \tag{1.1}
\]

be the literal port chart realized by the unchanged connector between
copies `j` and `j+1`.  The words *literal* and *realized* mean that the
connector has its own exact state, colour, and collar ledger; a row-name
relabeling is not a chart.

Transport every local label set to `D_1`.  Put

\[
 A_1=1,\qquad A_j=\alpha_{j-1}\cdots\alpha_1,
 \qquad \widehat\tau_j=A_j^{-1}\tau_jA_j.              \tag{1.2}
\]

### Theorem 1.1 (serial powers with all hidden conditions exposed)

Assume:

1. the slab interiors are resource-disjoint;
2. every seam and crossing collar has one exact owner;
3. the transported twists are coherent,
   `widehat(tau)_1=...=widehat(tau)_k=tau`.

Then the composite ownership ledgers are exact and its monodromy on the
first port set is

\[
                              \tau^k.                  \tag{1.3}
\]

The row entering with label `P` has total semilength

\[
 Q_k(P)=\sum_{j=0}^{k-1}q_j(\tau^jP),                 \tag{1.4}
\]

after all local length functions have been transported to `D_1`.
Consequently, if `ord(tau)=d`, then `d` coherent copies have identity
monodromy, and they fit a fixed `d r` cylinder if and only if

\[
                       Q_d(P)=dr\quad(P\in D).          \tag{1.5}
\]

For `d` identical copies of one factor, (1.5) is equivalent to

\[
       {1\over|O|}\sum_{P\in O}q(P)=r
       \quad\hbox{for every orbit }O\hbox{ of }\tau.   \tag{1.6}
\]

In particular strictness, `q(P)=r`, is sufficient.

#### Proof

At every slab, a local twisted factor partitions its two local shores and
only permutes whole outgoing tails.  The exact seam hypotheses therefore
preserve every ownership ledger inductively.  In the first label frame,
the successive tail permutations are `widehat(tau)_1,...,widehat(tau)_k`,
so coherence gives (1.3).

The row labelled `P` enters the successive local rows labelled

\[
                         P,\tau P,\ldots,\tau^{k-1}P,
\]

which proves (1.4).  If `k=d`, an orbit of length `e` dividing `d` is
traversed `d/e` times.  Hence

\[
 Q_d(P)={d\over e}\sum_{Q\in O}q(Q),
\]

and (1.5) is exactly (1.6). \(\square\)

### Remark 1.2 (the rank-three degree witness still fails)

For the explicit rank-three twist

\[
 \tau=(124\ 134\ 135),
 \qquad(q(123),q(124),q(125),q(134),q(135))=(5,3,3,3,1),
\]

the fixed orbit `{123}` has average `5`, and the three-cycle orbit has
average `7/3`, rather than `3`.  Three serial copies therefore have row
lengths `15` and `7` on those orbits, not `9`.  Finite order does not repair
its non-strictness.

## 2. Carrier accumulation is an orbit norm

Let `V` be an abelian carrier module: for example, the free abelian group
on protected target cells, or the row-resolved boundary-arm load space.
Assume port relabelling acts linearly on `V`.  Let `delta in V` be the
signed carrier increment of one oriented slab after its complete physical
push-forward.

For the statement below one needs an additional physical additivity
hypothesis: at the protected profile, the complete final histogram
difference must decompose into the transported stage increments
\(\delta,\tau\delta,\ldots,\tau^{d-1}\delta\). This holds, for example,
when every affected window meets at most one active slab. Resource
disjointness of slab interiors alone is insufficient, because one
protected window may cross two slabs.

### Theorem 2.1 (finite-order carrier norm under physical covariance)

Under the coherent repetition of Theorem 1.1 and the complete-carrier
additivity hypothesis above, the total carrier increment is

\[
                       \boxed{N_\tau\delta
                         =\sum_{j=0}^{d-1}\tau^j\delta.} \tag{2.1}
\]

Thus:

1. if `tau delta=delta`, the increment is `d delta`;
2. if the sum of `delta` on every `tau`-orbit is zero, the repeated carrier
   cancels;
3. for any linear score `Lambda` with `Lambda tau=Lambda`,
   \[
                       \Lambda(N_\tau\delta)
                             =d\Lambda(\delta).         \tag{2.2}
   \]

#### Proof

After the first slab, the row tails entering the second have been relabelled
by `tau`; after `j` slabs they have been relabelled by `tau^j`.  Equivariance
of the physical carrier chart therefore sends the `j`-th copy of the local
increment to `tau^j delta`.  The asserted complete-carrier decomposition,
not resource disjointness by itself, proves (2.1).  The three consequences
are immediate.
\(\square\)

In general assign exactly once to \(N_\tau\delta\) only those protected
occurrences which genuinely form the asserted covariant stage orbit, and
let \(\Xi^{\rm rem}\) be the signed aggregate of every unassigned
occurrence.  This remainder includes connector-only terms,
noncovariant singleton terms, transported-tail dependencies, and
windows meeting several active regions.  Then the always-valid formula
is

\[
 \boxed{\Delta^{\rm final}=N_\tau\delta+\Xi^{\rm rem}.} \tag{2.1a}
\]

Thus (2.1) applies to the final histogram only after
\(\Xi^{\rm rem}=0\), equivalently after every affected occurrence has
been included exactly once and covariantly in the stage carrier.

The theorem makes the orientation issue exact.  Using the same cyclic
orientation for every alternating cycle fixes the abstract sign of the
local switch, but does **not** by itself prove `tau delta=delta`.  One must
also verify:

* the exterior collars transport the same protected target cell to the
  same `tau`-orbit;
* no chart reverses the active cyclic orientation; and
* every protected window crossing two active slabs is either assigned to
  one slab or included in the row-resolved composition tensor.

If the carrier is strictly internal to each resource-disjoint slab, the
aggregate (non-row-resolved) increment of every identical physical copy is
literally the same, and the total is `d delta`.  The orbit norm is needed
at crossing boundaries.

## 3. An internal same-phase conveyor

The cleanest implementation uses one strict Chung--Feller cylinder rather
than external seam charts.

Let the current strict path factor be oriented from its Dyck roots to its
complementary exits.  Fix `l` distinct root strands

\[
                              P_0,\ldots,P_{l-1}
\]

and phases

\[
                              t_0<t_1<\cdots<t_{l-1}.
\]

At phase `t_j`, suppose the selected incidence edges on those strands form
one clean alternating `C_(2l)` with a common `(r-1)`-core and with cyclic
strand order

\[
                         \tau=(P_0\ P_1\ \cdots\ P_{l-1}). \tag{3.1}
\]

Call the family a **coherent `l`-stage conveyor** when:

1. all selected edges in one cycle have the same path orientation;
2. the `l` cycles are pairwise edge-disjoint;
3. after any initial segment of toggles, the next cycle is still
   factor-alternating and clean, occurs at the stated synchronized phase,
   and its transported endpoint operation is the same `tau` (not
   `tau^{-1}` and not a conjugate outside `<tau>`).

The third condition is the exact switch-stability condition.  It is
automatic when the later cycles lie on the suffixes permuted by the earlier
ones and their cyclic strand order is `tau`-equivariant.

### Theorem 3.1 (abstract strict finite-order conveyor theorem)

Toggling all cycles of a coherent `l`-stage conveyor gives an abstract
strict port factor with the original endpoint pairing.  It gives a literal
minimum-wreath factor only after the exterior-moving hypotheses in the
authoritative correction are proved.

#### Proof

An alternating-cycle toggle preserves every local `X`- and `Y`-degree.
Clean coherent orientation reconnects root prefixes to complementary
suffixes and induces the `l`-cycle (3.1).  Because all cuts of one toggle
occur at one synchronized phase, every new row joins a prefix of length
`t_j` to a suffix of length `r-t_j`; it therefore still has semilength
`r`.

Switch-stability permits the toggles to be made successively.  Their
endpoint operations multiply to `tau^l=1`, while every intermediate and
final factor retains the complete two-shore ledgers and strict row lengths.
Thus the final factor has the original complementary endpoints. \(\square\)

### Corollary 3.2 (carrier criterion for a conveyor)

If the complete row-resolved carrier increments of the `l` stages are
`delta,tau delta,...,tau^(l-1)delta`, then the final increment is the norm
`N_tau delta`.  In particular a `tau`-invariant parent-visible arm adds
`l` times, while a zero-orbit-sum arm cancels exactly.

This is the precise replacement for the informal assertion that identical
orientation makes the carrier add.  Identical orientation supplies the
same abstract sign; carrier invariance is the remaining physical theorem.

## 4. Power versus tensor in Catalan recursion

The ordinary Dyck concatenation law gives Cartesian cylinders.  With `l`
independent size-`s` holes, their port set is

\[
                              D_s^l.                    \tag{4.1}
\]

Installing the same twisted atom in the `j`-th hole acts on the `j`-th
port coordinate:

\[
 T_j(P_1,\ldots,P_l)
  =(P_1,\ldots,P_{j-1},\tau P_j,P_{j+1},\ldots,P_l).  \tag{4.2}
\]

### Proposition 4.1 (independent recursive holes give a tensor, not a power)

The `l` slot operations commute and their product is

\[
             T_l\cdots T_1(P_1,\ldots,P_l)
                  =(\tau P_1,\ldots,\tau P_l).         \tag{4.3}
\]

This is not the identity unless every `P_j` is fixed by `tau`, even when
`tau^l=1`.

#### Proof

Each `T_j` changes a different coordinate, giving (4.3) directly. \(\square\)

Therefore the formal Catalan product decomposition does not implement
Corollary 3.3 of the twisted-monodromy note.  A genuine finite-order escape
requires all stages to act successively on **one transported port label**.
That is precisely the conveyor condition of Section 3, or an external
connector satisfying Theorem 1.1.

## 5. The canonical first incidence layer has no cycle atom

There is a second exact obstruction to obtaining the conveyor for free.
Let

\[
                  C_0=\{g(P):P\in D_{2r}^0\}
\]

be the canonical first upper-colour layer.  Consider the bipartite
inclusion graph between `D_(2r)^0` and `C_0`.

### Theorem 5.1 (the canonical first matching is unique)

The matching

\[
                              P\longmapsto g(P)         \tag{5.1}
\]

is the unique perfect matching of this graph.  Consequently it contains no
alternating cycle of any length, and in particular no same-phase
`C_(2l)` twist atom.

#### Proof

Let the first return of the Dyck word `P` be at position `2j`.  The first
Chung--Feller insertion is exactly coordinate `2j`, so

\[
                              g(P)=P\cup\{2j\}.         \tag{5.2}
\]

Suppose another Dyck root `Q` is contained in `g(P)`.  If `Q!=P`, then

\[
                              Q=g(P)\setminus\{a\}      \tag{5.3}
\]

for one `a in P`.  Necessarily `a>2j`: if `a<2j`, then immediately before
the first return the height of `P` is one, while deleting the earlier
up-step lowers it to minus one.  Thus `Q` would not be Dyck.

It follows that `Q` agrees with `P` before `2j`, changes the closing
down-step at `2j` to an up-step, and deletes an up-step only later.  Hence
the first return of `Q` is strictly later than that of `P`.

Orient every off-diagonal inclusion `Q subset g(P)` from `Q` to `P`.
The first-return position strictly decreases along every such arc.  A
noncanonical perfect matching, compared with (5.1), would contain a
nontrivial permutation cycle of off-diagonal arcs, which is impossible
under a strictly decreasing potential.  Therefore (5.1) is unique.
\(\square\)

The same argument applies at the entrance of every literal recursive
`D_s` child cylinder: its local first matching is cycle-free.  Any conveyor
must use genuinely interior phases or a noncanonical local factor.

## 6. The exact density gate

A clean `C_(2l)` atom moves `l` root strands.  To act on an
`epsilon`-fraction of the `C_s` roots by disjoint conveyors requires at
least

\[
                       {\epsilon C_s\over l}           \tag{6.1}
\]

row-disjoint conveyors and hence `Omega(C_s)` synchronized alternating
cycles across their `l` stages.

What the canonical recursion currently supplies is:

1. Cartesian families of independent child holes, which fail by
   Proposition 4.1;
2. a cycle-free matching at every child entrance, by Theorem 5.1; and
3. isolated bounded-rank interior routers, none proved to form a growing
   switch-stable conveyor atlas.

Thus positive density is **not** a consequence of the recursive normal
form.  The exact missing theorem is:

> For some bounded `l>=3` and growing `s`, the strict Chung--Feller
> cylinder contains `Omega(C_s)` row-disjoint, parent-visible, coherent
> `l`-stage conveyors whose carrier vectors have a common positive
> `tau`-invariant projection.

The row-disjoint wording may be weakened to bounded congestion, but the
total active carrier supply must remain `Omega(C_s)`.

No such theorem is presently proved.  In particular, the finite-order
identity closes the monodromy gate once a conveyor exists; it does not
create the conveyor.

## 7. Cross-check with the preceding twisted-factor notes

The serial monodromy formula in
`MATH_THEOREM_TWISTED_PORT_MONODROMY_COMPOSITION_20260726.md` is correct
as abstract path-ledger algebra, and conditionally for exterior-moving
physical seams satisfying (C.2).  The present note adds the
qualifications needed in the ambient construction:

* for non-strict atoms, finite order must be supplemented by the orbitwise
  length equation (1.6);
* repeated recursive holes act tensorially unless a physical connector
  transports one port label through every stage.

The boundary-histogram formulas in
`MATH_ATTACK_S_TWISTED_PORT_TWO_SLAB_COMPOSITION_20260726.md` are also
consistent with Theorem 2.1: same orientation does not identify the first
and last carrier histograms; only an explicit invariant carrier chart does.

No constant-one conclusion is claimed here.
