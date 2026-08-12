# MLD adjacent-depth rounding gives a zero-defect named lower forest; same-depth `C=0` needs two new theorems

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional implication inside the unconditioned lower Boolean
model, conditional only on the stated fractional-configuration and reserve
hypotheses.  Fractional feasibility with exactly `D` aggregate tail rows,
cohort MLD, and the adjacent-depth reserve produce a fully named lower collar
forest with no omitted lower target at depth `D+1`.  The depth shift is the
only lower-side charge.  The note also proves that this argument cannot be
made same-depth by merely reserving sockets, and that no universal
bounded-**support** chronology absorber can repair all fractional selectors:
an even complete pair slice needs linear external parity leakage.  Neither
negative statement rules out a replicated bounded-state construction designed
jointly with the full triangular carrier.

## 1. Parameters and the off-by-one convention

Work in `B_(2r)`.  Put

\[
 C_s={2r\choose s},\qquad H_s=C_s-C_{s-1},\qquad W=C_r,
\tag{1.1}
\]

and let

\[
 D=d(2r)\ge1,\qquad t=r-D,\qquad b=t-1.
\tag{1.2}
\]

The boundary rank at old depth `D` is `t`.  The canonical nonempty residual
histogram occupies ranks

\[
                         1,\ldots,t-1.
\tag{1.3}
\]

Thus the MLD birth theorem must be instantiated with **path cutoff**

\[
                         \tau_D=t-1,
\tag{1.4}
\]

not with cutoff `t`.  A path born at rank `a` has canonical job length

\[
                         L_a=t-a.
\tag{1.5}
\]

After the adjacent shift the boundary is `b=t-1`; terminal deletion leaves
the ranks

\[
                         1,\ldots,b-1=t-2.
\tag{1.6}
\]

This is the meaning of “strictly below the new collar bottom”.  Keeping the
boundary parameter and the MLD cutoff separate removes the apparent
one-cell discrepancy between the canonical fragmentation and MLD notes.

The old and new collar tails are

\[
 K_q=W-C_{t+q-1}\quad(1\le q\le D),
\tag{1.7}
\]

and

\[
 K_q^+=W-C_{b+q-1}\quad(1\le q\le D+1).
\tag{1.8}
\]

Consequently

\[
 K_q^+-K_q=H_{t+q-1}\quad(1\le q\le D),
 \qquad K_{D+1}^+=H_r.
\tag{1.9}
\]

The hypothesis below is fractional feasibility against the tails (1.7)
themselves.  A fractional packing which additionally borrows endpoint-triangle
sockets does not satisfy that hypothesis unless those sockets are first
removed and the tail inequalities are rechecked.

## 2. Exact quantifiers

The construction has the following order of choices.

1. **Deterministic LP choice.**  Fix a feasible point of the whole-job
   configuration LP whose only aggregate constrained resources are the `D`
   tails (1.7), and choose an extreme feasible point.
2. **Deterministic basic rounding.**  Retain the unique integral
   configuration of every job with one positive extreme-point variable.
   Jobs with multiple positive variables are declared exceptional.
3. **Deterministic adjacent transport and marking.**  Apply terminal
   deletion, fragment exceptional descendants canonically, reserve new
   socket types, run one integer sorted-tail assignment, and refine every
   birth/configuration label by its complete new capacity-mark vector.
   All counts are fixed before any Boolean path is exposed.
4. **Random unconditioned lower path cover.**  At every Boolean interface,
   choose the independent uniform augmented matching used by the cohort-MLD
   theorem, and assign the fixed label counts uniformly within each birth
   cohort.
5. **Existential good realization.**  MLD plus generalized Holder and a
   union bound show that at least one realization satisfies every pointwise
   top-codegree inequality.
6. **Deterministic collar completion.**  On that realization, use
   bipartite matching integrality at every collar rank to attach all named
   chunks and all ordinary continuation vertices simultaneously.

In particular, neither the configuration nor its socket marks may be chosen
after seeing a realized Boolean path.  Conversely, the collar matching is
correctly chosen after the named tops are known.

## 3. Every finite exceptional charge

With exactly `D` aggregate resource rows, extreme-point support counting
leaves at most

\[
                              |\mathcal E|\le D
\tag{3.1}
\]

exceptional whole jobs.  Let their post-transport lengths be at most
`L_max`.  Fragment each consecutively into pieces of length at most `D`.
The number `p` of exceptional pieces obeys

\[
 p\le D\left\lceil{L_{\max}\over D}\right\rceil=:h.
\tag{3.2}
\]

For the canonical Boolean histogram, `L_max<=t`, and therefore

\[
 h\le D\left\lceil{t\over D}\right\rceil<t+D=r.
\tag{3.3}
\]

The exact sharper post-deletion bound may replace `L_max`, but is not needed.

If the configuration LP has `R` further independent aggregate resource
rows, the proof gives at most `D+R` exceptional jobs, not `D`.  The robust
bank size becomes

\[
 h_R=(D+R)\left\lceil{L_{\max}\over D}\right\rceil.
\tag{3.4}
\]

Adding an unconstrained future role to a configuration does not create this
charge; adding a new constrained aggregate row does.

For pointwise top concentration, leave nonnegative exact-capacity reserves
`Delta_g` at the new socket types `g=1,...,D+1`.  The exact sufficient tail
conditions are

\[
 h+\sum_{g=q}^{D+1}\Delta_g\le H_{t+q-1}
 \quad(1\le q\le D),
\tag{3.5}
\]

and

\[
 h+\Delta_{D+1}\le H_r.
\tag{3.6}
\]

The `Delta_g` occurrences are unused capacity, not omitted targets.  They
are a probabilistic Hall margin.

## 4. Zero-defect lower-forest theorem

### Theorem 4.1

Assume:

1. the old depth-`D` whole-job configuration LP is feasible against exactly
   the collar tails (1.7), with no additional aggregate constrained row;
2. the ordinary configurations and exception labels are assigned at birth
   according to the quantifier order in Section 2;
3. (3.5)--(3.6) hold; and
4. for `u_g=b+g`, with

   \[
   d_g={2r-b+1\choose g+1},
   \tag{4.1}
   \]

   the reserves satisfy

   \[
   {\Delta_g^2d_g\over C_{u_g}H_{u_g}}\ge A_0(2r)
   \quad(1\le g\le D+1),
   \tag{4.2}
   \]

   where `A_0` is the absolute constant in the MLD--Holder union bound.

Then the entire canonical residual lower histogram at depth `D+1` has a
fully named, target-once collar forest with these properties.

* Every nonempty residual target occurs in exactly one fragmented inclusion
  chain.
* Every chunk carries a capacity mark fixed before path realization.
* Every chunk is attached to a different genuine Boolean collar-chain
  occurrence of sufficient capacity.
* Every chunk top is contained in that occurrence's bottom.
* The collar interfaces form one saturated Boolean chain forest.
* No lower target is appended, discarded, or left unmatched.

#### Proof

Choose an extreme feasible configuration point.  With only the `D` tail
rows, the support-rank argument gives (3.1).  Retain every nonexceptional
integral configuration.  Terminal deletion cannot increase its conjugate
piece tail, so if `A_q` denotes the ordinary transported tail,

\[
 A_q\le K_q\quad(q\le D),\qquad A_{D+1}=0.
\tag{4.3}
\]

The new exact capacity-`g` multiplicity is `H_(b+g)`.  Delete `h` maximum
occurrences and `Delta_g` occurrences of exact capacity `g`.  The remaining
tail at `q` is

\[
 K_q^+-h-\sum_{g=q}^{D+1}\Delta_g.
\tag{4.4}
\]

Equations (1.9), (3.5), and (4.3) show that this dominates `A_q` for every
`q<=D`; at `D+1` there is no ordinary demand.  Sorted decreasing matching
therefore assigns every ordinary piece to an actual remaining occurrence.
Put the `p<=h` exceptional pieces on distinct deleted maximum occurrences.

This sorted assignment changes exact socket types, so record it before
path realization.  Group equal capacity-mark vectors within every
birth/configuration class and uniformly refine the class by those fixed
integer multiplicities.  Give each exception label its canonical block
fragmentation and maximum-capacity marks.  This is a deterministic
fixed-count cohort refinement and hence preserves MLD.

The lower path cover partitions every residual rank, and cutting its paths
at their marked boundaries covers every target once.  For each `(s,u)`, the
rank-`s` tops marked for start rank `u` form a union of persistent MLD
labels.  The generalized-Holder weighted Bernstein theorem, (4.2), and a
union bound yield one realization in which every normalized top codegree is
at most `H_u/C_u`.  The pointwise-codegree matching theorem then matches all
rank-`u-1` continuations and all requests to distinct containing rank-`u`
sets.  Doing this at every `u` gives the collar forest and every named
attachment.  No target was removed at any step. `square`

### Corollary 4.2 (eventual implication)

For the coefficient-one asymptotic `D=Theta(sqrt(r))`, the adjacent-tail
and vanishing-spread reserves satisfy (3.5)--(3.6) for every sufficiently
large `r`.  Hence fractional `D`-row configuration feasibility plus the
unconditioned cohort-MLD construction imply a zero-lower-defect named forest
at depth `D+1`.

#### Proof

Uniformly for `t<=s<=r`,

\[
 H_s={2r-2s+1\over2r-s+1}{2r\choose s}
 \ge c{W\over r}.
\tag{4.5}
\]

Thus `h=O(r)=o(H_s)`.  The spread theorem gives

\[
 \sum_{g=q}^{D+1}\Delta_g=o(H_{t+q-1}),
 \qquad \Delta_{D+1}=o(H_r),
\tag{4.6}
\]

and its choice of `Delta_g` satisfies (4.2) after increasing one absolute
constant. `square`

## 5. What “zero defect” does and does not charge

There is no lower sidecar in Theorem 4.1.  Its complete charge ledger is:

* at most `D` fractional whole jobs before absorption;
* at most `h<r` exceptional pieces;
* `h` maximum-capacity occurrences used by those pieces;
* `Delta_g` deliberately empty occurrences used only as Hall margin;
* zero omitted, duplicated, or appended lower target;
* one increase of the allowed depth, from `D` to `D+1`.

That last item is not yet a proved one-letter OR-word construction.  The
theorem builds a Boolean lower forest, not a source chronology.  A separate
protected serialization theorem would have to turn it into physical suffix
cells while preserving upper coverage and coordinate residence.

If a deterministic triangular boundary bank was removed before forming the
residual histogram, its targets remain a separate already-priced bank.  The
phrase “zero lower defect” refers to every target in the resulting canonical
residual histogram; it does not silently re-prove the boundary bank.

## 6. Why the same proof cannot stay at depth `D`

### Proposition 6.1 (zero-margin obstruction to a disjoint reserve)

Let an ordinary integral selection at depth `D` have piece tail `A`.  If

\[
                         A_q=K_q
\tag{6.1}
\]

for some `q`, then no positive-capacity bank containing a socket of capacity
at least `q` can be reserved while keeping the ordinary configurations
fixed.

#### Proof

Deleting one such socket changes the available `q`-tail to at most
`K_q-1`, while the fixed ordinary demand remains `A_q=K_q`.  The sorted-tail
criterion fails. `square`

Thus the adjacent proof uses something genuinely new: the exponential
margins (1.9).  At exact depth `D`, a successful absorber must reconfigure
ordinary jobs jointly with the exceptional jobs.  It cannot consist merely
of an occurrence-disjoint bank carved from an arbitrarily saturated
packing.

More exactly, if `p_a^0` are the retained ordinary Ferrers vectors,
`S=K-sum_a p_a^0` is the residual tail slack, and `F` is the exceptional
family, same-depth completion is equivalent to finding alternative ordinary
configurations `p_a` and exception configurations `q_f` such that

\[
 \sum_a(p_a-p_a^0)+\sum_{f\in F}q_f\le S
 \quad\hbox{coordinatewise}.
\tag{6.2}
\]

When `S=0`, the ordinary exchanges must pay the entire positive exceptional
tail.  This is an integer augmentation/normality theorem for the
configuration semigroup.  Fractional feasibility, MLD, and a finite state
label do not presently imply (6.2).

Moreover, `D` exceptional jobs of length `Theta(r)` can contain
`Theta(r^(3/2))` target cells.  Since one depth-`D` socket carries only
`O(sqrt(r))` cells, a worst-case residue needs `Omega(r)` socket
occurrences.  Therefore an absorber with `O(1)` **physical support** cannot
be universal.  A bounded set of local states replicated over `Omega(r)`
occurrences is not excluded.

## 7. The independent chronology parity obstruction

The complete-pair-slice theorem supplies a different obstruction.  On an
even label set of size `n`, selecting every pair owner once gives an
orientation of `K_n`.  Every literal state has odd imbalance parity.  Exact
owner and named-target fractional marginals exist, and the positive support
is connected, but any balanced integral chronology needs at least `n`
external incidences at the slice states, hence at least `n/2` external arcs.
An open Euler trail still needs at least `(n-2)/2` external arcs.

### Theorem 7.1 (bounded-support universal serializer no-go)

There is no universal rounding theorem which, from only

* exact fractional owner marginals;
* exact fractional named-target marginals;
* literal stationarity; and
* connected regular positive support,

produces a one-copy Euler circuit or open trail using only `O(1)` external
repair arcs.

#### Proof

Apply the proposed theorem to complete even pair slices with unbounded
`n`.  The exact fractional hypotheses hold, while the parity-leakage theorem
requires at least `(n-2)/2` external repair arcs even for an open trail.
`square`

This is a genuine parity obstruction, not a failure of socket arithmetic:
it survives exact named targets and every internal orientation exchange.
It is also sharp, since odd complete pair slices have an exact connected
stationary selector.

The obstruction must not be overread.

1. It concerns one-copy Euler serialization, not the static lower collar
   forest of Theorem 4.1.
2. It rules out bounded total repair **support**, not a bounded-state rule
   instantiated at linearly many slice vertices.
3. It does not prove that the full triangular carrier contains an isolated
   even pair slice.  Cross-core transitions may supply the required leakage.
4. Linear internal rethreading need not cost an additional word position.
   Therefore the theorem does not imply `nu(k)>B(k)`.

## 8. Exact `C=0` frontier

Removing the one-depth shift and proving an exact coefficient-one
construction requires two logically separate results.

### Lower semigroup augmentation

Prove (6.2) for the actual Boolean job histogram and socket tails, or prove
an equivalent normality/absorber theorem.  This would round the lower system
at depth `D` without an auxiliary socket margin.

### Protected parity-aware serialization

Co-realize the resulting named collar forest with a central owner chronology
which has residence, the full arbitrary-width upper deck, and one Euler
component.  Its support must avoid closed even pair slices or provide their
required distributed parity leakage.

The adjacent-depth theorem closes neither statement, but it removes all
lower target loss after paying one depth.  Conversely, the pair-slice no-go
does not refute a `C=0` construction designed jointly from the start.  It
only proves that exact marginals plus a bounded portal gadget cannot be that
construction.

## 9. Dependencies

1. `MATH_THEOREM_MLD_BIRTH_CONFIGURATION_CHAINIZATION_AND_WEIGHTED_HALL_GATE_20260805.md`;
2. `MATH_THEOREM_MLD_EXCEPTIONAL_BANK_ADJACENT_TAIL_RESERVE_AND_JOINT_NAMED_LIFT_20260805.md`;
3. `MATH_THEOREM_FRAGMENTATION_FERRERS_SEMIGROUP_BASIC_ROUNDING_AND_ABSORBER_20260805.md`;
4. `MATH_THEOREM_SPREAD_TOP_NAMING_POINTWISE_CODEGREE_AND_RANDOM_PARTITION_20260805.md`;
5. `MATH_THEOREM_COMPLETE_PAIR_SLICE_TARGET_EXACT_PARITY_AND_LINEAR_LEAKAGE_NOGO_20260805.md`.
