# Ferrers containment flow lifts to a flag hypergraph, not another TU network

**Date:** 2026-08-07  
**Status:** exact nested-flag formulation, exact ordered-slice Hall
reduction, a fixed-flow counterexample, and an unconditional factor-two
fallback.  The capacity-(d) Ferrers flow does not automatically refine to
depth-(d) owner flags.  Proving that refinement in all dimensions would
cross the known uniform-chain frontier.

## 1. Exact flag-configuration formulation

Let

\[
 \mathcal L=\{S\subseteq[k]:1\le |S|<R\},
 \qquad
 \mathcal O=\binom{[k]}R.
\]

For an owner (T\in\mathcal O), let (mathfrak F_d(T)) be the family
of all strict inclusion chains

\[
 F=(S_1\subsetneq\cdots\subsetneq S_t\subset T),
 \qquad0\le t\le d.
\tag{1.1}
\]

The empty chain is allowed.  Introduce binary variables (x_{T,F}) and
boundary variables (y_S).  The exact Ferrers flag problem is

\[
 y_S+\sum_{T,F:S\in F}x_{T,F}=1
 \qquad(S\in\mathcal L),
\tag{1.2}
\]

\[
 \sum_{F\in\mathfrak F_d(T)}x_{T,F}=1
 \qquad(T\in\mathcal O),
\tag{1.3}
\]

and

\[
 \sum_{S\in\binom{[k]}s}y_S=b_s
 \qquad(1\le s<R).
\tag{1.4}
\]

### Theorem 1.1 (flag-hypergraph equivalence)

The prescribed Ferrers profile admits a residual assignment in which every
owner fibre is one chain of length at most (d) if and only if
(1.2)--(1.4) has a (0)-(1) solution.

#### Proof

A (0)-(1) solution chooses one chain at every owner.  Equation (1.2)
places every nonboundary target in exactly one chosen chain and every
boundary target in none; (1.4) gives the required rank profile.
Conversely, a nested owner assignment supplies its chosen chain variables
and boundary indicators.  \(\square\)

Equivalently, make a hypergraph whose vertices are owners and lower
targets, whose owner-(T) configuration edges are
({T}\cup F), and add the typed boundary-choice row.  The desired object
is an exact configuration matching.  Unlike the capacity network, its
columns contain whole flags.  The bipartite node-edge TU argument no longer
applies.

## 2. Exact ordered-slice Hall reduction

The flag hypergraph has an ordinary-matching representation only after a
global time slicing has been chosen.

### Theorem 2.1 (right-aligned Ferrers ladder)

Fix boundary families (mathcal B_s) of the prescribed sizes and put

\[
 \mathcal L'=\mathcal L\setminus\bigcup_s\mathcal B_s.
\]

There is an anchored depth-(d) chain factor of (mathcal L') if and
only if (mathcal L') has a partition

\[
 \mathcal L'=A_1\mathbin{\dot\cup}\cdots
 \mathbin{\dot\cup}A_d
\tag{2.1}
\]

and containment injections

\[
 m_0:A_1\hookrightarrow\mathcal O,
 \qquad
 m_j:A_{j+1}\hookrightarrow A_j
 \quad(1\le j<d),
\tag{2.2}
\]

where every image strictly contains its preimage.

For fixed slices, this is equivalent to the ordinary Hall systems

\[
 |N_{\mathcal O}(X)|\ge|X|quad(X\subseteq A_1),
\tag{2.3}
\]

and

\[
 |N_{A_j}(X)|\ge|X|quad(X\subseteq A_{j+1}).
\tag{2.4}
\]

#### Proof

Given owner chains, put their members at distance (j-1) below the owner
in (A_j); consecutive members and the owner give (2.2).  Conversely,
orient the injections toward smaller slice index.  Every target has one
outgoing edge and at most one incoming edge, and slice indices strictly
decrease.  The components are disjoint inclusion paths ending at distinct
owners, hence the required chains.  Hall's theorem proves
(2.3)--(2.4).  \(\square\)

Normalized matching helps only after (2.1) is supplied.  For example, if

\[
 |A_d|\le\cdots\le|A_1|\le W
\]

and every adjacent slice graph has the normalized matching property in the
needed direction, then (2.3)--(2.4) follow.  The Ferrers capacity flow
chooses no such correlated slicing.

## 3. A fixed integral flow need not admit any owner-local uncrossing

Take (k=5,R=3,d=2) and no boundary.  The following is a complete
capacity-two containment assignment:

\[
\begin{array}{c|c@{\qquad}c|c}
123&13,2&124&12,4\\
125&15&134&14\\
135&35,1&145&45\\
234&23&235&25,3\\
245&24,5&345&34.
\end{array}
\tag{3.1}
\]

Every singleton and pair occurs exactly once and lies in its displayed
owner.  Five owners have load two and the rest load one.  In every load-two
fibre, the singleton is outside the displayed pair, so the two targets are
incomparable.

Consequently no reordering inside the fixed owner fibres turns (3.1) into
flags; at most ten of the fifteen targets can be retained while keeping the
owners fixed.  The capacity flow may therefore return an integral point
which is maximally bad for local chainization.

This is not a Boolean no-go for global re-assignment.  Indeed (k=5)
does have a depth-two chain assignment after exchanging targets between
owners.  The example proves the exact quantifier:

\[
 \boxed{
 \text{TU containment integrality does not admit ownerwise local
 refinement; a macroscopic reflow may be necessary.}}
\tag{3.2}
\]

## 4. Why a general depth-(d) theorem is a major static frontier

Put

\[
 \rho=\Lambda/W,qquad D=\lceil\rho\rceil.
\]

In every dimension in which the optimal Ferrers boundary is empty,
(d=D).  A depth-(d) strengthening would then partition the complete
strict lower ideal into (W) anchored chains of maximum length (D).
Appending the distinct rank-(R) owner to each chain gives a partition of
the lower half into exactly (W) chains of maximum size (D+1).

In odd dimension, complement-pairing these lower chains yields a
full-lattice (W)-chain partition with maximum size at most (2D+1), up
to the empty/full endpoint convention.  This is an all-chain additive
uniformity statement substantially stronger than what ordinary normalized
matching currently proves.  It lies on the one-sided Füredi
uniform-chain frontier.

An unmodified symmetric-chain decomposition does not close the gap.  In
even dimension, cutting every lower SCD segment into pieces of length at
most (D), without cross-chain splicing, creates at least

\[
 (1+e^{-\pi/4}-o(1))W
\]

pieces.  Thus any SCD proof at sharp depth needs
(\Theta(W)) correlated cross-chain splices.  Merely selecting the
Ferrers boundary, whose size is only (O(d^2)) in the exceptional
dimensions, does not supply those splices.

Therefore neither normalized matching nor “use one SCD inside each owner”
proves the requested strengthening.

## 5. An unconditional factor-two flag theorem

There is nevertheless a proof-safe general fallback.

### Theorem 5.1 (factor-two Ferrers flag assignment)

For every prescribed boundary profile, one may choose boundary families of
those sizes so that the residual targets admit distinct containing owners
and ownerwise chains of maximum length at most

\[
 2D+6.
\tag{5.1}
\]

For the optimal deadline/Ferrers profile, where (D\le d+1), this is at
most (2d+8).

In fact the conclusion remains true after deleting any boundary families
of the prescribed ranks from a suitable full lower-half chain partition.

#### Proof

The poset

\[
 P_k=\{S\subseteq[k]:1\le |S|\le R\}
\]

is a unimodal normalized-matching poset of width (W) and size
(\Lambda+W).  Tomon's chain-partition theorem gives a partition into
exactly (W) chains, each of size at most

\[
 \frac{2(\Lambda+W)}W+5=2\rho+7.
\]

The (W) rank-(R) owners form an antichain, so every one of the (W)
chains contains exactly one owner.  Remove that owner and remove any chosen
boundary targets.  What remains is an anchored residual chain factor of
maximum length at most

\[
 \lfloor2\rho+7\rfloor-1\le2D+6.
\]

For the optimal deadline, the already-proved inequality (D\le d+1)
gives the advertised (2d+8) specialization.  \(\square\)

The constant is inessential; the load-bearing point is the factor two.
Current normalized-matching technology does not reduce it to
(D+O(1)) for every chain.

## 6. Exact remaining statement

The sharp Ferrers flag theorem is now isolated as follows:

> Choose the named boundary families and a rank-interleaved partition
> (A_1,\ldots,A_d) of the residual lower ideal so that every adjacent
> Boolean containment graph satisfies (2.3)--(2.4).

For odd dimensions with every coatom retained, (A_1) may be fixed as the
coatom shore and subsequently matched to the owner shore.  The unresolved
part is the simultaneous choice of the lower slices and their adjacent Hall
matchings.  Even after this static flag factor exists, one common
move-to-front chronology and the upper interval deck remain separate gates.

Thus the exact answer is:

\[
 \boxed{
 \text{capacity-(d) Ferrers flow passes, but sharp nested flags do not
 follow from TU, normalized matching, or an unmodified SCD.}}
\]

The strongest unconditional general replacement currently justified is
depth (2d+O(1)), not depth (d).
