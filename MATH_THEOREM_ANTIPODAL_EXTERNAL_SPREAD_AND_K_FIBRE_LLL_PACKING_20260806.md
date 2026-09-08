# Antipodal external spread and exact `K`-fibre LLL packing

**Date:** 2026-08-06  
**Method:** a binomial coarea identity, bounded-variable concentration, and
the symmetric Lovasz local lemma; no computation or search  
**Status:** unconditional asymptotic packing theorem for the central
antipodal dwell-and-ear bank.  Once the external swap schedules are chosen
with polynomial trace load, all owner, immediate-lower, and immediate-upper
collisions are removed simultaneously by choosing the `K` ports and
geodesics inside one local-lemma instance.  The theorem includes the
reserved residence halos and arbitrary inherited physical ports.  It does
not insert the subexponential tail splices or prove the PBBS/common-cap
interfaces.

## 1. The central bank and its random variables

Use

\[
 K\mathbin{\dot\cup}E=[2m-1],\qquad |K|=m-1,\quad |E|=m,
 \tag{1.1}
\]

and let `d=Theta(sqrt(m))`.  Retain the trace vertices in the central band

\[
             2d+1\le |T|\le m-2d-1.              \tag{1.2}
\]

At every retained trace put the cyclic-window dwell of
`MATH_THEOREM_COMMON_CORE_GRAY_SPINE_AND_RESIDENT_DWELL_REDUCTION_20260806.md`.
At every retained ordinary seam of the antipodal folded-cube order put the
two external `d`-halos of
`MATH_THEOREM_ANTIPODAL_EAR_RESERVED_HALOS_AND_PORT_QUANTIFIER_GATE_20260806.md`.
The seams meeting a deleted trace are not included in this note.  Their
number is `2^{o(m)}`.

An occurrence is one of three types:

* a rank-`m` owner;
* a rank-`m-1` immediate-lower colour; or
* a rank-`m+1` immediate-upper colour.

For an occurrence `x`, write

\[
                       \operatorname{tr}(x)=x\cap E. \tag{1.3}
\]

The random construction is exposed in two stages.

1. **External stage.**  Fix the *positions* of the two halos, but choose
   their coordinate banks as the first and last `d` entries of uniform
   external deletion and insertion orders.  Impose the at most two named
   coordinate positions required by each fork tag.  Conditional on those
   names, choose all remaining entries uniformly.  The choices belonging
   to nonincident ears are independent.
2. **`K` stage.**  At every trace choose the incoming `K` port and its
   cyclic dwell presentation symmetrically.  The adjacent dwell window is
   the outgoing port.  Conditional on the ports, independently choose the
   remaining `K` deletion and insertion orders of every ear.

The second-stage law is equivariant under the full symmetric group of
`K`.  Every one-occurrence marginal, conditional on its external trace,
is therefore uniform on the uniquely prescribed `K` layer.  For a formal
copy in the variable-length `K`--`K` block, regard the copy as either
inactive or labelled by a `K` subset.  Activity is invariant under
`Sym(K)`, so

\[
 \Pr(x\text{ is active and has }K\text{-projection }P)
 ={\Pr(x\text{ is active})\over\binom{m-1}{|P|}}. \tag{1.4}
\]

Thus formal envelope copies obey the same upper bounds as genuine fixed
positions.

There is a minor order-of-exposure point.  The number of `K`--`K` swaps
depends on the intersection of the two eventual ports.  Pair the maximum
possible external deletions with external insertions, pair the remaining
one-directional external changes with the forced opposite-direction `K`
changes, and put all residual `K`--`K` swaps in one designated block after
the first external halo.  The external trace sequence outside that block
depends only on the first-stage external orders.  At the block trace put
`m` formal copies in an **external load envelope**.  Every eventual ear
uses at most those `m` copies, whatever the two ports are.  All load bounds
below refer to this envelope and therefore remain valid after the `K`
variables are exposed.  The first and last `d` swaps remain external--
external swaps, as required by the halo theorem.

The local shared-variable pairs cause no bad events.  Roles inside one
dwell or one monotone ear are distinct.  A dwell and either incident ear
are separated by the external halo theorem.  The two ears incident with
one dwell are separated by the two-coordinate fork tag.  Intended common
chronology endpoints are identified rather than counted twice.

## 2. A polynomial maximum external load

The key point is to freeze the external schedules **before** choosing any
physical `K` roles.

### Lemma 2.1 (binomial coarea identity)

Let `M` external coordinates be split by a starting trace of size `u`.
At a specified profile, suppose `alpha` old coordinates have been deleted
and `beta` new coordinates inserted.  For a fixed resulting trace `S` of
size `s=u-alpha+beta`, the sum of its occurrence probabilities over all
rank-`u` starts is

\[
 {\binom s\beta\binom{M-s}\alpha
  \over\binom u\alpha\binom{M-u}\beta}
       ={\binom M u\over\binom M s}.              \tag{2.1}
\]

If `s` lies between `u` and `M-u`, the quantity in `(2.1)` is at most one.

#### Proof

There are

\[
                         \binom s\beta\binom{M-s}\alpha
\]

compatible starts.  For each start, the two unordered prefix sets are
uniform and independent, giving the denominator on the left of `(2.1)`.
Cancelling factorials proves the identity.  Binomial unimodality and
symmetry prove the final assertion.  \(\square\)

The almost-complement seams and fork tags have only a bounded number of
named exceptional coordinates.  Delete those coordinates, condition on
their states and forced positions, and apply Lemma 2.1 to the remaining
ground set.  Forcing a bounded number of positions costs only a polynomial
adjacent-binomial factor.  Crucially, the `2d` halo coordinates are **not**
conditioned in advance: they are the random first and last blocks of the
same permutations.  The prescribed type word
keeps the external rank between its endpoint ranks.  Immediate palette
traces differ from an incident owner trace in at most one coordinate, so
the adjacent binomial ratio costs only a polynomial factor.  Grouping by
the start rank, profile, exceptional-coordinate state, occurrence type,
and position gives the following bound.

### Lemma 2.2 (mean external load)

There is an absolute `c_0` such that, for every external trace `S` and
every one of the three occurrence ranks,

\[
 \sum_i \mathbb E Z_i(S)\le m^{c_0},              \tag{2.2}
\]

where `Z_i(S)` is the number of envelope occurrences on ear `i` having
external trace `S`.  Also

\[
                         0\le Z_i(S)\le C m        \tag{2.3}
\]

for an absolute `C`.

#### Proof

For one fixed group, Lemma 2.1 bounds the sum over all possible starts by
one, up to an adjacent-binomial polynomial for palette roles.  The actual
antipodal starts form a subfamily, so restricting to them can only
decrease this nonnegative sum.  There are only polynomially many groups.
The formal `K`--`K` block merely multiplies the contribution of one such
group by at most `m`, which is absorbed by the polynomial.  An ear has at
most `m` genuine transitions and its envelope has at most `Cm`
occurrences of one rank.  \(\square\)

The fork prescriptions couple only incident ears.  Three-colour the
cyclic ear-index graph; inside each colour the variables in Lemma 2.2 are
independent.  Bernstein's bounded-variable inequality says that for
independent `0<=X_i<=b`, with mean sum `mu`,

\[
 \Pr\!\left(\sum_iX_i-\mu\ge t\right)
 \le
 \exp\!\left(-{t^2\over2b\mu+2bt/3}\right).       \tag{2.4}
\]

Take `b=Cm` and

\[
                     t=A(\mu+b m),                 \tag{2.5}
\]

where `A` is a sufficiently large absolute constant.  The exponent in
`(2.4)` is at least `cAm`.  A union bound over the three colours, the three
role ranks, and all `2^m` external traces proves the next theorem.  Dwell
roles add only `O(m)` to the unique trace of their dwell.

### Theorem 2.3 (deterministic polynomial trace spread)

The external coordinate orders can be chosen so that

\[
 \boxed{
  \#\{x:\operatorname{tr}(x)=S, |x|=r\}\le L_m=m^{c_1}}
 \tag{2.6}
\]

simultaneously for every `S subseteq E` and
`r in {m-1,m,m+1}`, for one absolute `c_1`.

This is a maximum-load statement, not merely an average-load statement.
It is the input which prevents an endpoint-facet blocker from hiding on
one external fibre.

## 3. Every central physical fibre is superpolynomial

Freeze external schedules satisfying Theorem 2.3.  Along a retained ear,
external ranks stay between the two endpoint ranks.  Including the possible
one-coordinate shift of an immediate palette, every occurrence uses a
`K` subset whose size lies between

\[
                     2d-2\quad\hbox{and}\quad(m-1)-(2d-2).
 \tag{3.1}
\]

Thus every conditional `K` fibre has size at least

\[
                 B_m:=\binom{m-1}{2d-2}.           \tag{3.2}
\]

Since `d=Theta(sqrt(m))`,

\[
                 B_m=\exp(\Omega(d\log(m/d)))=m^{\omega(1)}.
 \tag{3.3}
\]

Let `F` be an already protected fixed bank.  It may be included provided
its maximum same-trace, same-rank load `F_m` obeys

\[
                    {m(L_m+F_m)\over B_m}=o(1).     \tag{3.4}
\]

This permits every polynomial-load bank.  It also permits any whole fixed
bank of size

\[
             \exp\bigl((1/2+o(1))d\log m\bigr),    \tag{3.5}
\]

because `(3.2)` has logarithm `(1+o(1))d log m`.
In particular the complete rolling low-collar bank may be treated as a
fixed obstacle: its incidence size is at most

\[
 m\sum_{j\le d}\binom{2m-1}j
 =\exp\bigl((1/2+o(1))d\log m\bigr).              \tag{3.6}
\]

## 4. Exact collision-free packing by the local lemma

Use independent base variables as follows.  A dwell variable `xi_i`
chooses the incoming port and cyclic presentation at trace `i`; an ear
variable `eta_i`, conditional on the two incident dwell variables, chooses
the remaining `K` orders.  Equivalently, `eta_i` is an independent uniform
seed passed through the corresponding equivariant conditional sampler.

A base variable affects `O(m)` occurrences: one dwell and at most two
incident ears for `xi_i`, or one ear for `eta_i`.  Every occurrence has at
most `L_m-1` random possible collision partners and at most `F_m` fixed
partners, because equality requires the same rank and the same frozen
external trace.

For every nonlocal pair of random occurrences of the same rank and
external trace, let `A_(x,y)` be the event that their `K` projections are
equal.  For every compatible fixed obstacle `f in F`, define the unary
event `A_(x,f)` analogously.  The local-separation facts in Section 1 mean
that every listed random pair has disjoint base-variable sets.  Hence its
two `K` projections are independent uniform members of the same layer,
and

\[
               \Pr(A_{x,y})\le B_m^{-1},\qquad
               \Pr(A_{x,f})\le B_m^{-1}.           \tag{4.1}
\]

One bad event uses only a bounded number of base variables.  Each such
variable occurs in at most

\[
                         C'm(L_m+F_m)               \tag{4.2}
\]

bad events.  Therefore the variable-overlap dependency graph has maximum
degree

\[
                         D_m\le C''m(L_m+F_m).       \tag{4.3}
\]

By `(3.4)`, for all sufficiently large `m`,

\[
                         eB_m^{-1}(D_m+1)<1.         \tag{4.4}
\]

The symmetric Lovasz local lemma supplies one simultaneous choice in
which no bad event occurs.

### Theorem 4.1 (central antipodal private-ear packing)

For all sufficiently large `m`, all central retained antipodal dwells and
ordinary ears admit one simultaneous physical realization such that:

1. every owner is private, except for intended identified chronology
   endpoints;
2. every immediate-lower colour is private;
3. every immediate-upper colour is private;
4. all inherited incoming ports and adjacent outgoing ports belong to the
   same physical opened dwell;
5. both external `d`-halos at every ear are retained, so every exported
   positive and zero residence flag is discharged; and
6. the whole bank avoids every fixed protected bank satisfying `(3.4)`.

#### Proof

The external schedules are fixed by Theorem 2.3.  The local facts in
Section 1 dispose of all pairs sharing a base variable.  The local lemma
disposes of every remaining equality in each of the three physical ranks
and every equality with `F`.  The inherited-port and residence assertions
are deterministic properties of every point in the second-stage sample
space.  \(\square\)

This theorem defeats the endpoint blocker without contradicting it.  The
blocker in Proposition 5.1 of the reserved-halo note is built **after** a
port is frozen.  Here the port itself is a local-lemma variable, and the
polynomial maximum external load makes its entire physical `K` fibre
available during selection.

### Corollary 4.2 (nonlocal enlarged-halo separation)

Enlarge every central macro by the Ore halo used in the protected-factor
theorems: all lower facets of its owners, all owners over its protected
lower colours, its immediate upper roles, and the endpoint-neighbour roles.
The choice in Theorem 4.1 can be made so that

1. every two halo roles generated by disjoint variable neighbourhoods are
   distinct; and
2. the complete enlarged central halo avoids the enlarged halo of every
   fixed protected bank satisfying `(3.4)` after polynomial rescaling.

#### Proof

One base occurrence generates only `m^{O(1)}` indexed halo roles.  Its
external trace changes by at most two coordinates, so Theorem 2.3 gives a
polynomial maximum envelope load for the indexed halo roles as well.  Its
`K`-projection size remains between `2d-O(1)` and
`(m-1)-(2d-O(1))`; replace `B_m` by

\[
                         B'_m=\binom{m-1}{2d-4}.    \tag{4.5}
\]

For a fixed halo index, equivariance again makes the output uniform on its
`K` layer.  Enumerating the polynomially many indices multiplies both the
event degree and, if one uses unindexed set-events, the event probability
by only a polynomial.  Since `B'_m=m^{omega(1)}`, the local-lemma
inequality `(4.4)` still holds.  Add all nonlocal halo equalities and all
halo equalities with the fixed bank to the same instance.  \(\square\)

The word "nonlocal" is necessary.  Two incident ears and their common
dwell share intended stars.  Their bounded local exposure ledger is a
deterministic path calculation; Corollary 4.2 says that no remote macro
adds a second contribution to that ledger.

## 5. Co-selection with the common-core witness reservoir

The deterministic top and low parts of the common-core reservoir have
only polynomial enlarged-halo load at one external trace.  Their base
paths have one exact trace; taking a radius-two physical halo introduces
only polynomially many neighbouring traces.

The random high-tail part has at most

\[
 m^{O(1)}\sum_{j\le d}\binom mj
 =\exp\bigl((1/2+o(1))d\log m\bigr)                \tag{5.1}
\]

enlarged-halo roles in total.  The rolling low-collar bank has the same
upper scale by `(3.6)`.  Therefore the **entire already co-selected**
common-core reservoir and rolling bank, with their enlarged halos, satisfy
`(3.4)` relative to `B'_m`.  Put that union directly into `F` and apply
Corollary 4.2.  No reselection of the protected reservoir is required.

### Corollary 5.1 (central ears coexist with the protected reservoir)

The collision-free central antipodal dwell-and-ear bank, the complete
clipped-resident common-core reservoir, and the complete rolling low-collar
bank have a simultaneous realization with private owners, both private
immediate palettes, and pairwise separated nonlocal enlarged halos.

## 6. Exact remaining scope

Closed here:

1. polynomial **maximum** load in every external trace fibre;
2. joint selection of inherited ports, dwell presentations, endpoint
   halos, and free middle geodesics;
3. simultaneous global owner/lower/upper privacy for all central ordinary
   antipodal ears; and
4. co-selection with the existing protected common-core and rolling-collar
   banks.

Still open:

1. insert and join the `2^{o(m)}` tail traces and exceptional splice ears;
2. preserve or rebuild the complete PBBS all-width upper occurrence bank;
3. transport the terminal common-cap/compiler state; and
4. deduce `nu(k)<=B(k)+O(1)`.

The global central-ear packing gap is therefore not a polynomial repair
problem.  It is already collision-free after one two-stage spread argument.
The decorated construction now fails only at the subexponential tail and
the downstream all-width/cap interfaces.
