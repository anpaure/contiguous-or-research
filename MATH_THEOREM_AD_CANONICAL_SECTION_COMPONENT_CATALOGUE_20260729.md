# Canonical-section catalogue for arbitrary even equivariant factors

Date: 2026-07-29  
Status: proved factor-level normal form, encoding-size theorem, and local
splice theorem; no SAT run and no compiler-completion claim.

## 0. Result and scope

Let

\[
 K=2r,\qquad n=K-1=2r-1,\qquad
 W=\binom K r,\qquad N=W/n,
\]

and let `rho` cyclically permute the `n` old coordinates and fix the top
coordinate `z`.  Fix once and for all one representative `U_i` of each
`rho`-orbit in the middle layer, `i in [N]`.

There is a fixed, exact catalogue for **every** `rho`-invariant spanning
simple two-factor.  It has no prescribed component partition and no
prescribed voltage list.  First define its directed darts by

\[
 \mathcal A=\{(i,j,p):i,j\in[N],\ p\in\mathbb Z_n,\
                    U_i\sim \rho^pU_j\}.                 \tag{0.1}
\]

Let `a -> bar a` reverse a dart and let

\[
                  \mathcal E=\mathcal A/(a\sim\bar a)     \tag{0.2}
\]

be the catalogue of undirected physical edge orbits.  Exactly

\[
             |\mathcal A|=Nr^2,\qquad |\mathcal E|=Nr^2/2 \tag{0.3}
\]

darts and undirected edge orbits occur.  A factor is exactly a selection
from `E` having weighted quotient degree two at every owner; a quotient
loop has weight two.  If an oriented successor is wanted, it is equivalently
a one-out/one-in selection from `A`, with the two orientations of one
physical edge orbit not both selected.  At `K=16`, the exact counts are

\[
 N=858,\quad r=8,\quad |\mathcal A|=54,912,\quad
 |\mathcal E|=27,456.                                    \tag{0.4}
\]

Equivalently, the selection is encoded by only an arbitrary successor
permutation `sigma in S_N` and phases `p_i in Z_n`.  Thus arbitrary
component lengths and arbitrary zero, nonunit, or unit voltages do not
require a component selector tensor.  A width-`N` shared-control Waksman
router represents `sigma`; component annotations are optional and remain
polynomial.

This theorem is complete for equivariant simple factors.  It does **not**
say that a prescribed component-size/voltage list, a bounded maximum
component size, or a bounded shadow-window list is without loss.  It also
does not open or compile the decoded cycles into one literal OR word.

## 1. Free action and a fixed section

The action of `rho` on the middle layer is free.  Indeed, a nontrivial
rotation has old-coordinate cycles of a common length `d>1` dividing
`n=2r-1`.  An invariant old part therefore has size divisible by `d`, but a
middle mask has old size either `r` or `r-1`, while

\[
 \gcd(2r-1,r)=\gcd(2r-1,r-1)=1.
\]

Consequently every middle orbit has size `n`, and a fixed section
`{U_1,...,U_N}` exists.  Once this section is fixed, every physical middle
mask has a unique expression `rho^a U_i`.

An invariant undirected factor can be oriented equivariantly.  Choose an
orientation on one cycle from each `rho`-orbit of physical cycles and
transport it.  Any stabilizer has odd order, whereas an orientation-
reversing automorphism of a cycle has order two.  Hence transport is
consistent.

## 2. Exact canonical-section catalogue theorem

For a dart `a=(i,j,p)` define its reverse

\[
                  \bar a=(j,i,-p).                       \tag{2.1}
\]

This is a fixed-point-free involution on `A`: equality would force `i=j`
and `2p=0`; oddness of `n` gives `p=0`, contradicting the strict Johnson
adjacency in (0.1).

The action on physical Johnson edges is also free.  If a rotation fixes an
unordered edge, it either fixes both endpoints, contradicting freeness on
vertices, or swaps them.  The latter induces an element of order two, which
cannot occur in the odd-order rotation group.

### Theorem 2.0 (smallest locally exhaustive physical catalogue)

For `e in E`, let `m_i(e)` be `0`, `1`, or `2` according as the quotient
edge orbit is not incident with owner `i`, is a nonloop incident with `i`,
or is a loop at `i`.  The `rho`-invariant spanning simple two-factors are in
bijection with `y in {0,1}^E` satisfying

\[
                     \sum_{e\in\mathcal E}m_i(e)y_e=2
                     \qquad(i\in[N]).                    \tag{2.0}
\]

The physical decoding is the union of the selected physical edge orbits.
Consequently the exact undirected pseudo-Boolean base has `Nr^2/2`
variables and `N` weighted degree-two equations.  At `K=16` this is exactly
`27,456` variables and `858` rows; the catalogue contains `28` quotient
loops, each with coefficient two in its owner row.  The loop number is the
independently replayed quotient-catalogue census in
`MATH_AUDIT_K16_CT_RECONCILIATION_AND_QUOTIENT_FACTOR_20260729.md`; it is
not inferred from regularity alone.

#### Proof

Freeness on edges makes every `e` one orbit of `n` distinct physical
edges.  A selected nonloop contributes one incident physical edge at every
lift of each endpoint owner.  A selected quotient loop represented by
`U_i -- rho^pU_i` contributes the two distinct neighbours
`rho^{s+p}U_i` and `rho^{s-p}U_i` at every `rho^sU_i`; they are distinct
because `n` is odd and `p` is nonzero.  Thus (2.0) is exactly physical
degree two at every middle vertex.  Conversely every invariant factor is a
union of full free edge orbits and its quotient degrees give (2.0).  QED.

The catalogue `E` is the unique smallest **locally exhaustive physical
edge-orbit catalogue**, because every physical Johnson edge belongs to one
unique member of `E`.  As below, global pruning below `E` requires a proof
that a deleted orbit occurs in no extendible simple factor.

### Theorem 2.0a (global minimality when `r` is even)

If `r` is even, the quotient edge-orbit multigraph `E` decomposes into
exactly `r^2/2` spanning two-factors satisfying (2.0).  Consequently every
edge orbit in `E` occurs in some equivariant simple factor, so

\[
                         \mathcal E_{\rm fact}=\mathcal E. \tag{2.0a}
\]

Hence for `K divisible by 4`, and in particular for `K=16`, the
`Nr^2/2`-member catalogue is not just locally exhaustive: it is the unique
inclusion-minimal fixed physical edge-orbit catalogue containing every
equivariant factor under the fixed coordinate labels.

#### Proof

Count a quotient loop twice in degree.  By Proposition 2.2 the quotient
multigraph is `r^2`-regular.  When `r` is even, write `r^2=2k`.  Orient an
Euler tour in every connected component; every quotient vertex then has
indegree and outdegree `k` (an oriented loop contributes one to each).
Split every vertex into a left tail and right head.  The oriented edges form
a `k`-regular bipartite multigraph, so repeated Hall matching decomposes
them into `k` perfect matchings.  Each matching gives one incoming and one
outgoing edge at every quotient vertex, hence one weighted degree-two
selection in (2.0).  The matchings partition all edge orbits, proving that
every member of `E` extends to a factor.  QED.

For odd `r`, this even-regular factorization argument is unavailable.
Equation (2.7) below remains the exact globally minimal catalogue; equality
with `E` is not asserted without a separate extension theorem.

This minimality fixes the canonical coordinate labels.  A single global
normalizer multiplier acts coherently on an entire factor and may identify
whole feasible solutions.  The theorem does not compute a smallest support
catalogue modulo that additional global action; in particular one may not
choose a different multiplier for each selected edge or component.

### Theorem 2.1 (complete fixed-section factor catalogue)

The equivariantly oriented `rho`-invariant spanning simple two-factors of
`J(K,r)` are in bijection with Boolean vectors
`x in {0,1}^A` satisfying

\[
 \sum_{a:\,\operatorname{tail}(a)=i}x_a=1
       \quad(i\in[N]),                                   \tag{2.2}
\]

\[
 \sum_{a:\,\operatorname{head}(a)=j}x_a=1
       \quad(j\in[N]),                                   \tag{2.3}
\]

and

\[
                         x_a+x_{\bar a}\le1
       \quad(\{a,\bar a\}\subseteq A).                  \tag{2.4}
\]

The directed physical dart set decoded from `x` is

\[
 D(x)=\bigl\{(\rho^sU_i,\rho^{s+p}U_j):
                 x_{(i,j,p)}=1,\ s\in\mathbb Z_n\bigr\}. \tag{2.5}
\]

Its underlying undirected edge set is obtained by forgetting the order in
each member of `D(x)`.

#### Proof

Given an oriented invariant factor, inspect the unique outgoing edge at
`U_i`.  Its head is uniquely `rho^pU_j`, so it gives one dart of `A`.
Unique indegree gives (2.3).  If both `a` and `bar a` were chosen, incoming
and outgoing edges at every lift of their common edge orbit would coincide,
contrary to degree two in a simple factor.  Thus (2.2)--(2.4) hold.

Conversely, (2.2)--(2.3) define a permutation `sigma` and a phase `p_i` by
the unique selected dart `(i,sigma(i),p_i)`.  The map

\[
 F(i,s)=(\sigma(i),s+p_i)                                \tag{2.6}
\]

is a permutation of `[N] x Z_n`.  Every decoded edge is a Johnson edge by
(0.1).  Each vertex has one incoming and one outgoing edge, and (2.4) says
these are distinct.  Hence the undirected decoding is a spanning simple
two-factor and `D(x)` is its chosen equivariant orientation.  The two
constructions are inverse because the fixed section makes every oriented
head phase unique.  QED.

### Proposition 2.2 (exact catalogue cardinality)

Every tail `i` has exactly `r^2` darts, and therefore (0.3) holds.

#### Proof

The rank-`r` mask `U_i` has exactly `r(K-r)=r^2` physical Johnson
neighbours.  Freeness and the fixed section express every such neighbour
as one unique `rho^pU_j`.  This is a bijection between physical neighbours
of `U_i` and darts with tail `i`.  Summing over `i` proves (0.2).  Reversal
then gives exactly `Nr^2/2` unordered dart pairs.  QED.

Thus the oriented pseudo-Boolean lift uses exactly `Nr^2` dart bits, `2N`
exact-one rows, and, in its symmetric form, `Nr^2/2` reverse-pair
inequalities.  If `L` is the number of directed quotient-loop darts, the
`L/2` loop reverse-pair inequalities are already implied by the outgoing
exact-one rows, so only `(Nr^2-L)/2` are needed explicitly.  At `K=16`,
`L=56`, giving `27,428` nonloop reverse-pair rows.  A particular CNF
cardinality encoding may add auxiliaries, but those are not part of the
mathematical catalogue count.

### Minimality statement that is actually proved

`A` is the unique smallest **locally exhaustive oriented fixed-section dart
catalogue**: every legal outgoing Johnson edge orbit at every fixed owner
is one distinct member of `A`, so any oriented catalogue promising local
exhaustion must contain all `Nr^2` darts.  Without orientation, Theorem 2.0
is smaller by the exact factor two.

The inclusion-minimal undirected catalogue containing every globally
extendible simple factor is

\[
 \mathcal E_{\rm fact}=\bigcup\{\operatorname{supp}(y):
          y\text{ satisfies (2.0)}\}.                    \tag{2.7}
\]

It is exact by definition.  Theorem 2.0a proves `E_fact=E` for even `r`.
For odd `r` it may be a proper subset; equality would require an additional
extension theorem.

For the oriented catalogue there is no additional loss.  If the underlying
edge orbit of `a` occurs in an invariant factor, orient the orbit of physical
cycles containing that edge so that its representative is directed as `a`,
and transport by `rho`; odd stabilizers make this consistent.  Hence

\[
 \mathcal A_{\rm fact}
 =\{a\in\mathcal A:[a]\in\mathcal E_{\rm fact}\}.       \tag{2.8}
\]

In particular Theorem 2.0a gives `A_fact=A` for even `r`, although the
oriented representation uses twice as many literals as the smaller
undirected physical catalogue.

## 3. Gauge, components, and the complete type data

Changing a section to `U_i'=rho^{q_i}U_i` sends

\[
                 p_i'=p_i+q_i-q_{\sigma(i)}.              \tag{3.1}
\]

It does not change `sigma`.  For a `sigma`-cycle `C`, the voltage

\[
                     v_C=\sum_{i\in C}p_i\pmod n          \tag{3.2}
\]

is invariant.  The component lifts to `gcd(n,v_C)` physical cycles, each
of length

\[
                 |C|n/\gcd(n,v_C).                       \tag{3.3}
\]

Thus the fixed-section `(sigma,p)` datum contains all component information
without component fields.  It is the unique representative of its section-
gauge class once the physical orientation is fixed.

If only component **types** are to be tabulated, every actual type belongs
to the polynomial safe list

\[
 \begin{split}
 \mathcal T_{N,n}^{\rm safe}={}&
   (\{1,2\}\times(\mathbb Z_n\setminus\{0\}))\\
   &{}\cup(\{3,\ldots,N\}\times\mathbb Z_n).
 \end{split}                                              \tag{3.4}
\]

For quotient length one, voltage zero would be a vertex loop rather than a
Johnson edge.  For quotient length two, voltage zero makes the two darts
reverses and is exactly forbidden by (2.4).  At quotient length at least
three, simple-factor legality imposes no further length/voltage restriction.
Some pairs in (3.4) may nevertheless be unrealizable because the required
local darts do not exist.  The exact realized type list is obtained by
decoding (2.2)--(2.4), not by assuming all pairs in (3.4).
For `N>=2`, the safe list has exactly

\[
                         |\mathcal T_{N,n}^{\rm safe}|=Nn-2. \tag{3.5}
\]

This polynomial type list is only a root predicate.  A pair `(ell,v)` does
not specify the `ell` owner slots or their dart sequence, so it cannot
replace `sigma,p` in an exact decoder.

## 4. Exact SAT encodings

### 4.1 Sparse explicit edge and dart encodings

For unoriented factor existence, use the `Nr^2/2` variables and `N` rows
of Theorem 2.0.  This is the smallest proved locally exhaustive physical
catalogue.  Components can be oriented equivariantly after decoding.

When a successor chronology is required inside SAT, use the `Nr^2` dart
variables and rows (2.2)--(2.4), or add orientation bits to selected
undirected edges with

\[
                         x_a+x_{\bar a}=y_{\{a,\bar a\}}. \tag{4.0}
\]

The one-in/one-out rows force these orientations to be consistent around
every decoded component.  Component cycles, lengths, and voltages are then
decoded in linear time.

For longer successor windows, derive `sigma(i)` and `p_i` from the unique
selected outgoing dart and feed them to a shared router.  This linkage is
linear in `|A|` times the binary field width, not quadratic in the number
of owner pairs.

### 4.2 Implicit canonical-section Waksman encoding

Alternatively encode `sigma` directly by a width-`N` Waksman network and
store one `b=ceil(log_2 n)`-bit phase `p_i` at every input, forbidding the
`2^b-n` invalid codes.  Route the fixed head masks backward and the fixed
tail masks together with their phases forward through the same switch
controls.  After the two phase rotations, impose outgoing Johnson adjacency
and inequality between the incoming and outgoing neighbours.

Let `S(N)` be the switch count.  Before the local adjacency and inequality
comparators, a conservative Boolean-variable bound is

\[
 \boxed{
 S(N)+2(2K+b)S(N)+Nb+2nbN.}                              \tag{4.1}
\]

The terms are respectively the shared controls, the two directions of
`2K+b` routed payload bits (two output variables per switch), the phase
fields, and two old-coordinate barrel rotations.  Standard mux equivalences
give at most

\[
             8(2K+b)S(N)+8nbN                           \tag{4.2}
\]

multiplexer clauses, plus `N(2^b-n)` invalid-code clauses and
`O(KN)` local comparator circuitry.  These are upper bounds independent of
syntactic constant propagation, not an implemented CNF census.

At `K=16`, `N=858`, `b=4`, and `S(858)=8078`, (4.1) is

\[
 8078+581616+3432+102960=696086.                          \tag{4.3}
\]

This factor base is substantially smaller than routing thirteen aligned
window layers; those layers are added only when the requested shadow or
residence catalogue needs them.

### Proposition 4.1 (completeness and lower bounds)

The undirected edge encoding projects exactly to Theorem 2.0.  Its oriented
dart lift and the implicit Waksman encoding project exactly to Theorem 2.1.
No component or voltage annotation is needed merely to allow all components
and voltages.

Any binary-control rearrangeable network that can realize every permutation
of `N` labelled slots has at least

\[
                       \lceil\log_2(N!)\rceil             \tag{4.4}
\]

control bits.  Hence a width-`N` Waksman router with `O(N log N)` controls
is asymptotically optimal among topology-oblivious arbitrary-permutation
routers.  This lower bound concerns the promised ability to realize all
`S_N`; the set of successor permutations that extend to legal factors may
be smaller, and no stronger factor-count lower bound is claimed.

For the abstract interface of `c` labelled oriented all-unit component
voltages, quotienting by the one global coordinate multiplier leaves
`phi(n)^(c-1)` relative-voltage classes.  Any interface promised to admit
and distinguish all those abstract tuples needs at least

\[
                  (c-1)\log_2\phi(n)                     \tag{4.5}
\]

bits.  Thus a constant-size selector is not complete for that declared
tuple domain, whereas one bounded residue per root, or the `N` dart phases,
has the correct polynomial information scale.  This is not an unconditional
lower bound for the locally legal factor family: realizing every abstract
relative-voltage class by a spanning factor is not proved.  For a restricted
legal family the corresponding lower bound is the logarithm of the number
of relative-voltage classes it actually realizes.

## 5. Optional polynomial component annotation

When a SAT master must constrain component count, length, or voltage, give
slot `i`:

* a root label `a_i in [N]`;
* an order `h_i in {0,...,N-1}`;
* a phase potential `q_i in Z_n`;
* a root bit `R_i`.

Route successor values of these fields through the **same** controls used
for `sigma`.  Require

\[
 a_{\sigma(i)}=a_i,\quad a_i\le i,\quad
 R_i\Longleftrightarrow a_i=i,                            \tag{5.1}
\]

\[
 R_i\Rightarrow h_i=0,\quad \neg R_i\Rightarrow h_i>0,
 \quad\neg R_{\sigma(i)}\Rightarrow
 h_{\sigma(i)}=h_i+1.                                    \tag{5.2}
\]

A rootless cycle would strictly increase `h` around a loop, and the
constant propagated root label permits at most one root.  Hence every cycle
has exactly one root, its minimum-index slot.  Put `q=0` at the root,
accumulate `q_{sigma(i)}=q_i+p_i` on nonclosing edges, and on the closing
edge record

\[
 L_{\sigma(i)}=h_i+1,\qquad
 V_{\sigma(i)}=q_i+p_i\pmod n.                            \tag{5.3}
\]

Then `L,V` are exactly the quotient length and voltage at each root.
Component count is `sum_i R_i`; physical component count is
`sum_{i:R_i=1}gcd(n,V_i)`.

Writing `a=ceil(log_2N)`, the routed root/order/potential/flag fields use at
most

\[
                        2(2a+b+1)S(N)                    \tag{5.4}
\]

multiplexer variables, plus `N(2a+b+1)` stored bits and
`O(N(a+b))` local gates.  Root-only `L,V` outputs add `N(a+b)` stored bits
if a solver predicate needs them.  This is polynomial shared-control
annotation, not a selector over partitions of `N` or over `n^c` voltage
tuples.

A componentwise closing-voltage gauge is also WLOG, but it is not a smaller
variable-topology SAT base.  It replaces direct dart phases by `N` section
potentials plus root voltages and requires the root/closing annotation that
the direct fixed-section form may omit.  It is useful only when component
boundary formulas exploit the zero internal phases.

## 6. Exact splice and locality theorem

### Theorem 6.1 (alternating catalogue splice)

Let `x` satisfy (2.2)--(2.4).  Select two distinct old darts

\[
 a=(i,j,p),\qquad b=(k,l,q),
\]

with distinct tails and heads.  Suppose

\[
 a'=(i,l,p'),\qquad b'=(k,j,q')                           \tag{6.1}
\]

belong to `A`, and replacing `a,b` by `a',b'` creates no selected reverse
pair.  Then the replacement decodes to another equivariant spanning simple
two-factor.

If `a,b` lie on distinct `sigma`-cycles of voltages `v_1,v_2`, the two
quotient cycles merge and the new voltage is

\[
                 v'=v_1+v_2-p-q+p'+q'\pmod n.             \tag{6.2}
\]

The merged quotient component lifts to exactly `gcd(n,v')` physical
cycles.  In particular the merge produces one physical cycle on its joined
vertices if and only if `v'` is a unit.

If `a,b` lie on one quotient cycle, removing them leaves directed paths
`j -> ... -> k` and `l -> ... -> i`.  Let their internal phase sums be
`s_(j,k)` and `s_(l,i)`.  The replacement splits the quotient cycle into
two, with voltages

\[
                         s_{j,k}+q',\qquad s_{l,i}+p'.     \tag{6.3}
\]

#### Proof

The replacement preserves one outgoing dart at every tail and one incoming
dart at every head.  Membership in `A` preserves Johnson legality, and the
reverse-pair hypothesis preserves simplicity, so Theorem 2.1 applies.
The usual two-edge permutation surgery merges distinct cycles and splits
one cycle.  Summing retained and replacement phases gives (6.2)--(6.3),
and (3.3) gives the physical lift statement.  QED.

The same proof applies to any alternating circuit in the bipartite
tail--head catalogue: toggle its old and new darts, check new-dart legality
and reverse pairs, and decode.

### Proposition 6.2 (bounded-window recourse after a splice)

Suppose two selections differ only at a set `D` of `d` outgoing tails,
including every tail whose successor or phase changed.  For a raw successor
window of `w` states, only starts in

\[
          \bigcup_{t=0}^{w-2}\sigma^{-t}(D)               \tag{6.4}
\]

can change.  Hence at most `d(w-1)` quotient occurrences change.  All lower
intersections, upper unions, and trace motifs computed from unchanged raw
windows remain literally identical.  Exact coverage can therefore be
updated from the lost and gained occurrences in (6.4), rather than by
rebuilding an occurrence-by-target selector tensor.

If all old and new physical component lengths are at least the maximum
audited width `H`, the same locality statement holds for active one-pass
windows through width `H`.  Without that hypothesis, a splice can change a
component return length, so the one-pass **activity bit** can change at every
start of an affected component even though the raw width-`H` word changes
only near (6.4).  This is the exact short-component caveat.

#### Proof

Old and new successor walks agree until they first encounter a tail in
`D`.  A window of `w` states traverses `w-1` darts, proving (6.4) and its
cardinality bound.  Intersections, unions, and trace motifs are deterministic
functions of the raw state window.  The final claim follows because activity
is automatic below the physical return length but is a global component
length predicate otherwise.  QED.

## 7. Completeness boundary for component and window catalogues

### Proposition 7.1 (why fixed whole-component blocks are not WLOG)

Suppose a catalogue partitions the `N` owner slots in advance into blocks
of size at most `B` and permits successor routing only within blocks.  Every
encoded `sigma`-cycle then has length at most `B`.  Section gauge leaves
`sigma` unchanged, while global coordinate multiplication merely relabels
the owner orbits and conjugates `sigma`.  Hence neither operation changes
the multiset of cycle lengths.  Any actual factor with a quotient cycle of
length greater than `B` is therefore outside the catalogue in every gauge.

In particular, the existing `K=16` equivariant physical Hamilton factor
has a quotient cycle of length `858`, so every such block catalogue with
`B<858` is a proper sufficient subclass.

If instead one tries to support arbitrary `sigma` by explicitly listing
whole-component orders, then already the one-component topology-oblivious
library has `(N-1)!` directed cyclic orders before phases.  A type label
`(N,v)` does not distinguish or decode those orders.  The shared Waksman
controls are precisely the symbolic `O(N log N)` replacement for this
template enumeration.  This factorial statement concerns a library that
promises every permutation; the locally legal factor subset may be smaller,
and no factorial lower bound for the number of actual factors is claimed.

#### Proof

The first assertion is immediate from invariance of blocks.  Gauge and
global relabelling preserve cycle lengths as stated.  A directed cyclic
order on `N` labelled slots is a permutation modulo choice of its starting
point, giving `N!/N=(N-1)!` orders.  QED.

The following are WLOG for equivariant factor representation:

1. fixing the canonical section `U_i`;
2. using all darts in `A`, or equivalently arbitrary `sigma,p` satisfying
   the local rows;
3. concentrating each cycle's phases on one closing dart if the necessary
   section-potential annotation is retained;
4. decoding component length and voltage rather than selecting them from a
   Cartesian catalogue.

The following are only sufficient subclasses:

1. a prescribed partition `(M_1,...,M_c)` of `N`;
2. a prescribed voltage vector, all voltages unit, or all voltages one;
3. a maximum quotient component length `B<N`;
4. a fixed list of shadow widths used as a surrogate for all literal
   intervals;
5. a splice that merges quotient cycles without the unit test in (6.2).

Section gauge leaves `sigma` and hence every quotient component length
unchanged.  Global coordinate multiplication and component reversal also
preserve component lengths and preserve `gcd(n,v_C)`.  Therefore no
bounded-length component catalogue can be declared WLOG unless an external
theorem proves that every relevant factor has that bound.  At `K=16`, the
existing equivariant physical Hamilton certificate already has one quotient
cycle of length `N=858`; every catalogue with maximum quotient length below
`858` excludes it.

There is no contradiction with the width-one catalogue (0.1): local darts
plus global degree rows encode arbitrarily long components **implicitly**.
What is not WLOG is an explicit bounded list of whole-component templates
or the use of bounded raw windows as a proof of unmodelled all-width shadow
and compiler requirements.

Finally, if the decoded factor has one quotient cycle and unit voltage,
(3.3) proves that it is one physical Hamilton cycle.  Opening it at one edge
gives a linear middle chronology, with exactly the windows crossing that cut
removed.  If several physical components remain, or if cut-crossing
colours must be restored, a separate seam/boundary Hall/compiler theorem is
still required.  The catalogue and splice theorem do not silently supply
that literal completion.
