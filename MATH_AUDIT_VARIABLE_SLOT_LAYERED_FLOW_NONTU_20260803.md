# Variable-slot Boolean particle flow: the exact non-TU row and the cross-rank decorrelation gate

**Date:** 2026-08-03  
**Status:** proof-safe route audit. No computation is used. A fixed bank
ladder is integral, but allowing each named target to choose its time/mark
slot does not preserve total unimodularity in the natural time-expanded
flow formulation. This invalidates the proposed rounding inference; it is
not a counterexample to the balanced named-flag theorem itself.

## 0. Verdict

View the `W=binom(2r,r)` owners as unit particles descending the Boolean
Hasse DAG. Without a mark budget, an integral lower-bounded flow can cover
the required lower vertices. If the target bank at every one of `d` marked
times is fixed in advance as a union of complete-layer copies and the
adjacent rank transports are feasible, normalized Boolean containment and
ordinary bipartite integrality give an integral path ladder; this is
Theorem 3.1 of
`MATH_THEOREM_MIXED_COMPLETE_LAYER_TRANSPORT_FIXED_SLOT_LADDER_20260803.md`.

The proposed final step duplicates a named target `S` over several times
and then imposes

\[
                         \sum_h z_{S,h}=1.               \tag{0.1}
\]

These are partition rows across different time layers. They are not flow-
balance rows. Already with two variable marked positions, three strictly
nested Boolean targets give a determinant-`2` minor. Hence target-to-slot
choice does not preserve the fixed-bank TU argument, and the symmetric
fractional particle flow cannot be rounded by citing network-flow
integrality.

Equivalently, the quantifier change

\[
 \text{choose target banks first, then match interfaces}
 \quad\longrightarrow\quad
 \text{choose banks and interfaces jointly}             \tag{0.2}
\]

adds a genuine correlation resource. The exact balanced named-flag theorem
therefore remains open on this route.

## 1. Fixed slots are a network; variable slots add partition rows

In a fixed time-expanded DAG, its node--arc incidence matrix is totally
unimodular. Integral lower and upper arc capacities and integral supplies
therefore give an integral flow polytope.

If every named target has already been placed in one time bank, visiting
that one target vertex can be enforced by an integral lower bound. The
fixed-bank containment matchings can also be chosen separately, as in the
mixed-complete-layer theorem. No row couples two time copies of one named
set.

For adaptive time choice, let `E(S)` be the mark choices representing the
possible time copies of target `S`. Exact coverage requires

\[
                         x(E(S))=1                       \tag{1.1}
\]

for every `S`. In an arc expansion these rows couple different time copies.
Equivalently, after projecting a two-mark path to the two targets it
contains, they become the target-degree rows of the comparability graph.
Fixed top and bottom banks give a bipartite graph; allowing the targets to
choose their roles gives a general graph.

## 2. Two determinant-2 slot-choice minors

First consider a common wait-arc time expansion containing a three-arc
directed subpath

\[
                         \cdot\xrightarrow{e_1}u
                         \xrightarrow{f}v
                         \xrightarrow{e_2}\cdot .       \tag{2.1}
\]

Suppose `e_1` and `e_2` are two admissible time-copy mark arcs for the same
named target `S`, while `f` is a transit or wait arc. Any encoding containing
this motif before the target-once row is imposed has the following minor.

Restrict the flow-balance system together with the target row for `S` to
the rows at `u,v` and the columns `e_1,f,e_2`. Up to multiplying network
rows by `-1`, the minor is

\[
 M=
 \begin{pmatrix}
  1&-1& 0\\
  0& 1&-1\\
  1& 0& 1
 \end{pmatrix}.                                         \tag{2.2}
\]

Its determinant is

\[
                         \det M=2.                       \tag{2.3}
\]

Therefore this wait-arc adaptive-slot matrix is not totally unimodular.

The failure is genuinely integral, not just a determinant diagnostic. On
this face, the integral right-hand side

\[
 e_1-f=0,\qquad f-e_2=0,\qquad e_1+e_2=1              \tag{2.4}
\]

has the unique solution

\[
                         e_1=f=e_2=\frac12.              \tag{2.5}
\]

All variables lie in `[0,1]`. Thus an integral network system can acquire a
fractional basic solution solely from the target-across-times row.

There is a second obstruction which uses strict containment and never
visits one target twice. Take three distinct Boolean targets

\[
                         A\subset B\subset C.            \tag{2.6}
\]

With two adaptive marked positions, each of `AB`, `BC`, and `AC` is a
legal two-target flag. Fix any owner containing `C`; all three flags are
legal configurations for that same owner. Restrict the target--configuration
incidence matrix to the three target rows and these three columns. In column
order `AB,BC,AC` it is

\[
 M_{\rm strict}=
 \begin{pmatrix}
  1&0&1\\
  1&1&0\\
  0&1&1
 \end{pmatrix},
 \qquad \det M_{\rm strict}=2.                          \tag{2.7}
\]

Thus even the strict two-slot adaptive configuration matrix is not totally
unimodular. Giving all three columns weight `1/2` covers every one of
`A,B,C` exactly once with total path weight `3/2`. Predetermining which
targets belong to the upper and lower banks destroys this triangle and
returns to a bipartite matching.

There is also an integral path-count gap inside a Boolean lattice. Choose
two three-chains

\[
 A_1\subset A_2\subset A_3,
 \qquad
 B_1\subset B_2\subset B_3,                             \tag{2.8}
\]

with every `A_i` incomparable to every `B_j`. For example, make every
`A_i` contain a coordinate `a` and avoid `b`, make every `B_j` contain `b`
and avoid `a`, and grow both chains using other coordinates. Put weight
`1/2` on each of the three two-target subchains inside each component. This
fractionally covers all six targets with three depth-two paths. Integrally,
each three-chain needs two depth-two paths and no path can mix the two
components, so four paths are necessary.

Hence the scalar rows

\[
        |\mathcal L|=dP,
        \qquad \operatorname{width}(\mathcal L)\le P    \tag{2.9}
\]

do not make the adaptive bounded-chain configuration relaxation integral,
even for a Boolean subposet (`d=2,P=3` in this example, where `P` is the
available path budget).

### Scope of the minor

The first minor applies to wait-arc encodings containing its displayed
motif. The strict minor refutes the broader claim that variable target-to-
slot choice inherits the fixed-bank bipartite TU proof. The six-target
example is a counterexample for an arbitrary Boolean subfamily, not for the
dense optimal nonboundary family of the balanced named-flag theorem.

General graph matching at depth two can be repaired by blossom
inequalities. For larger depth the analogous columns are bounded-chain
hyperedges. No such repair, and no integral extended formulation for the
dense Boolean instance, follows merely from rank normalization.

## 3. Why normalized mixed-layer coupling stops before this row

For two **fixed** unions of complete layer copies, a feasible rank-level
transport gives the uniform fractional edge weights

\[
 \frac{a_{s,t}}
 {{n\choose s}{n-s\choose t-s}},                        \tag{3.1}
\]

and every rank-`t` vertex receives the normalized load
`a_(s,t)/binom(n,t)`. Bipartite integrality then supplies a named matching.

If a rank-`s` target may choose among times, a rank-level schedule gives
only fractions `lambda_(s,h)`. Replacing every target by these symmetric
fractions restores complete-layer symmetry **fractionally**. Rounding must
then decide, for each literal set `S`, which one of its time copies survives,
while also selecting its predecessor and successor. Equations (0.1) are
exactly this decision. Theorem 2.1 of the mixed-layer note cannot be applied
until the literal banks are fixed, so applying it here would reverse the
quantifiers.

Nor does bipartite integrality preserve a prescribed internal rank
transport matrix. It guarantees some saturating named matching between the
fixed shores; adding exact type-pair quotas would add further side rows.

## 4. The third-resource interpretation

The rank-separated named-target theorem uses two matroids after taking a
direct sum over ranks:

1. containment-transversal independence in each rank; and
2. the owner-load partition matroid.

Nested flag compatibility correlates different rank summands on the same
owner. The nonadjacent residual-rank rule does not even define a matroid:
on three consecutive residual ranks, the allowed sets

\[
                         I=\{s+1\},
                  \qquad J=\{s,s+2\}                   \tag{4.1}
\]

satisfy `|I|<|J|`, but neither element of `J\I` can augment `I`. Thus the
rank-pattern row cannot simply be appended as a third matroid to the
two-matroid proof.

At the abstract level, even three genuine partition matroids already have
a sharp parity obstruction. On the four even-parity triples

\[
                         000,\quad011,\quad101,\quad110, \tag{4.2}
\]

impose, for each of the three coordinates and each bit, the equation that
exactly one chosen triple has that bit in that coordinate. Giving every
triple weight `1/2` satisfies all six equations. An integral solution would
have to choose two complementary triples, but the complement of every
even-parity triple has odd parity and is absent. Hence there is no integral
solution.

This parity system is not asserted to be a counterexample inside the
Boolean ideal. It is the exact warning against a generic ``three integral
projections therefore round jointly'' argument. In the present problem the
three resources are target identity, owner/time capacity, and compatible
predecessor--successor path choice. Boolean structure would have to supply
a new exchange theorem that is absent in general.

If one freezes the equitable rank patterns instead, the same issue is the
configuration hypergraph of
`MATH_THEOREM_EQUITABLE_PATTERN_CONFIGURATION_FRACTIONAL_MATCHING_20260803.md`:
one configuration simultaneously consumes a pattern, an owner, and all
named targets of one flag. Its canonical symmetric point is fractional, and
ordinary matching or flow integrality does not apply.

## 5. What a lower-bounded Boolean flow does prove

A symmetric lower-bounded flow on the Boolean DAG can prove marginal
coverage and marginal owner balance. After fixing marked times, its
integral decomposition gives literal descending paths. It does not, before
the marked times are fixed, imply that every one of the `W` source paths
uses at most `d` distinct named targets.

The load bound is a path-history resource: a unit of flow may pass through
many lower-bounded target vertices, and ordinary flow conservation records
neither how many marks its source path has accumulated nor which time copy
of a literal target was used. A `d`-layer mark expansion records the first
quantity, while (0.1) is needed for the second. Section 2 shows that imposing
both is not a TU operation.

This precisely reconciles the four input theorems:

* exact rank multiplicities and equitable scalar loads round;
* rankwise named containment and equitable owner loads round;
* fixed sparse cross-SCD banks couple by one Hall matching;
* the fully correlated pattern--owner--flag point is only known
  fractionally.

## 6. A rigorous fixed-cut expectation lemma

There is a plausible randomized continuation, but only its one-cut
expectation is presently rigorous.

Let `Omega` be the `W` propagated path labels. For every named target `S`,
let `V(S) subseteq Omega` be its nonempty visitor block: the path labels to
which `S` could be assigned in the proposed downward matching construction.
Assume that, conditional on its size, `V(S)` is invariant under every
permutation of `Omega`. No independence between different targets is
assumed.

For a fixed `Q subseteq Omega`, put

\[
 F(Q)=\#\{S:V(S)\subseteq Q\}.                          \tag{6.1}
\]

These are the targets forced into the path-label set `Q` in the associated
capacitated Hall graph.

### Lemma 6.1 (exchangeable fixed-cut bound)

Let `|Q|=qW`. If `c_(s,l)` rank-`s` targets have visitor-block size `l`,
then

\[
 \mathbb E F(Q)
 =\sum_{s,l}c_{s,l}
   \frac{{qW\choose l}}{{W\choose l}}
 \le\sum_{s,l}c_{s,l}q^l.                              \tag{6.2}
\]

In particular, if every visitor block is nonempty and the number `N` of
targets is at most `dW`, then

\[
                         \mathbb E F(Q)\le qN\le d|Q|. \tag{6.3}
\]

### Proof

Permutation invariance makes a size-`l` visitor block uniform among the
`l`-subsets of `Omega`. This gives the equality in (6.2). Moreover

\[
 \frac{{qW\choose l}}{{W\choose l}}
 =\prod_{i=0}^{l-1}\frac{qW-i}{W-i}\le q^l             \tag{6.4}
\]

when `l<=qW`; if `l>qW`, the left side is zero. Since `l>=1`,
`q^l<=q`. Summing proves (6.3). \(\square\)

When each rank has only block sizes `m_s` and `m_s+1`, (6.2) is exactly the
suggested expression

\[
 c_{s,m_s}q^{m_s}+c_{s,m_s+1}q^{m_s+1}.                \tag{6.5}
\]

For `q>0`, after division by `qW`, each monomial is nondecreasing in `q`;
its maximum is at `q=1`.

## 7. Why the fixed-cut lemma does not prove all Hall cuts

There are exponentially many path-label sets `Q`. An expectation at or
below the Hall threshold for each fixed `Q` does not imply that one outcome
satisfies every cut. The estimate (6.3) can have zero slack at `q=1` and
arbitrarily small slack near `q=1`.

A direct entropy union bound would require, uniformly in the density `q`,
a tail estimate strong enough to beat the number

\[
                         {W\choose qW}
                  =\exp\bigl(H(q)W+o(W)\bigr)           \tag{7.1}
\]

of cuts. The propagated labels at different ranks come from shared
integral matchings, so their visitor-block events are highly dependent. No
negative-association, switching-count, or cut-compression theorem giving
the required tails follows from permutation invariance or from the
near-uniform block sizes alone.

Accordingly the randomized proposal should be recorded as the following
remaining problem, not as a proof.

### Cross-rank decorrelation conjecture

For the optimal nonboundary rank inventory, there is a joint choice of the
balanced downward Boolean `b`-matchings and propagated owner labels such
that every target has a jointly valid visitor block and

\[
             \#\{S:V(S)\subseteq Q\}\le d|Q|
             \qquad\text{for every }Q\subseteq\Omega.  \tag{7.2}
\]

If simultaneous choices from the visitor blocks can interfere at a time
or transition, (7.2) must be strengthened by the corresponding time- and
transition-indexed Hall cuts. A proof would need either:

1. an entropy-plus-switching tail bound beating (7.1) in every density
   regime;
2. an uncrossing theorem reducing (7.2) to a polynomial or laminar family
   of cuts; or
3. a deterministic cross-rank exchange algorithm maintaining every cut.

None of these follows from the present normalized transport identities.

## 8. Proof-safe conclusion

The proposed particle route proves an integral `W`-path cover only on the
fixed-slot, mixed-complete-layer face. The adaptive target-to-slot choice
adds partition rows, destroys the direct configuration TU property by
(2.7), and returns the
problem to the correlated flag/configuration gate.

Therefore one may safely cite:

\[
 \boxed{
 \text{rank transport}
 \Longrightarrow
 \text{integral named matching between fixed complete-layer banks}.}
\]

One may not cite:

\[
 \boxed{
 \text{symmetric lower-bounded particle flow}
 \Longrightarrow
 \text{balanced integral named flags}.}
\]

The latter implication would also cross the static additive-uniform chain
frontier identified in
`MATH_THEOREM_EQUITABLE_RANK_SIMPLE_IDEAL_SDR_AND_MTF_CHAINIZATION_GATES_20260803.md`.
