# Global hierarchical order catalogues and the tensor-associator entropy gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The sectorwise lower bound

\[
 \log_2\binom rq-O(\log r)
\]

does not survive unrestricted cross-sector flow. Its proof asks every
balanced target macrocell to be supplied by the balanced source sector,
whereas the exact macroprofile inclusion flow deliberately uses many source
sectors.

There is nevertheless a cross-sector invariant. A pair-flip \(q\)-window
empties a physical matching of \(q\) disjoint coordinate pairs. If that
\(q\)-matching is \(E\), every lower shadow must avoid all \(2q\) endpoints
of \(E\). Consequently one \(E\) can serve at most

\[
 \binom{2m-2q}{m-q}
\]

rank-\(m-q\) targets. This gives the global, frame-independent catalogue
bound

\[
 |\mathcal E_q|
 \geq(1-o(1))
 \frac{\binom{2m}{m-q}}{\binom{2m-2q}{m-q}}
 =2^{\,2q-q^2/(m\log 2)+o(q^2/m+1)}.
\]

It remains valid with arbitrary cross-sector flow, arbitrary packet
embeddings, and arbitrary local pair-frame associators.

If one cyclic order profile exposes at most \(\ell\) different
\(q\)-matching intervals, and a hierarchy has \(P\) base packet profiles
and at most \(2^L\) branch outcomes per base profile, then

\[
 \boxed{
 L+\log_2P
 \geq
 2q-\frac{q^2}{m\log 2}-O(\log m+q^3/m^2).
 }
\]

Thus cross-sector sharing can trade hierarchy entropy against packet
diversity, but it cannot remove their combined \(2q-o(q)\) information
cost.

This exponent is sharp up to polynomial factors at the level of shadow
support. A random catalogue of

\[
 O\!\left(
 \frac{\binom{2m}{m-q}}{\binom{2m-2q}{m-q}}\log\binom{2m}{m-q}
 \right)
\]

physical \(q\)-matchings meets the complement of every lower target.
Taking the union over \(q\leq H\) costs only

\[
 2^{\,2H-H^2/(m\log 2)+O(\log m)}
\]

profiles. Every chosen matching can be extended to a pair frame and placed
as one consecutive interval in a cyclic order.

There is also an exact multiscale ordering theorem: a binary tree in which
an internal node permits all shuffles of its two child orders generates
every leaf permutation exactly once. It has geometric height
\(O(\log m)\). Hence no lower bound on geometric hierarchy height alone is
possible; the correct quantity is the logarithm of the number of effective
profiles, equivalently the sum of local branch entropies.

For the tensor-associator architecture this gives a precise verdict.
The \(r\) local shore choices provide at most \(r\) bits of profile entropy,
and they leave the macroblock order fixed. If \(P\) external packet
embeddings are available, any coefficient-one near-resolution at
\(q=A\sqrt m\) must satisfy

\[
 r+\log_2P\geq2A\sqrt m-O_A(\log m).
\]

The proposed regime \(r/\sqrt m\to\infty\) passes this necessary test for
every fixed \(A\). But the present associator does not implement the
all-shuffle theorem: its Boolean moments lie in the kernel of macroblock
projection, and its suspension preserves the native macro-order. The exact
missing object is an owner-preserving **shuffle associator** together with
an integral packet selection. The result below solves the global profile
entropy question, not that physical splice.

## 1. Pair-flip windows and physical empty-pair matchings

Let \(\mathcal P\) be any perfect matching of the \(2m\) ground
coordinates. A pair-flip window using \(q\) distinct directions selects
\(q\) edges

\[
 E=\{e_1,\ldots,e_q\}\subseteq\mathcal P.
\]

Along the window, both endpoints of each \(e_i\) occur in some middle
state. Hence neither endpoint survives the intersection. If \(S\) is the
lower shadow, then

\[
 |S|=m-q,\qquad S\cap V(E)=\varnothing.
\tag{1.1}
\]

This statement forgets the pair-frame tag. It concerns the physical
\(q\)-matching \(E\) on the ground set and therefore remains meaningful
when different packets use different coordinate matchings.

Its scope is a window that is pair-flip geodesic in one physical frame.
That includes the present tensor architecture, where an associator chooses
one complete shore and then the Hamming bundle runs in that shore. A new
architecture which changes pair frame inside one \(q\)-window could produce
directions sharing ground coordinates, so its empty support need not be a
matching. Such a dynamic-frame splice would evade Theorem 2.1, but it would
first require a new exact chronology and is not supplied by the existing
whole-cycle associator trade.

Conversely, if a rank-\(m-q\) set \(S\) avoids \(V(E)\), choosing one
endpoint of every edge of \(E\) gives a middle set \(X\supset S\) whose
pair-flip \(q\)-face has lower corner \(S\). This converse realizes the
face. Extending it to a prescribed long cycle can require additional split
pairs, so it is a support statement rather than a long-residence theorem.

For fixed \(E\), the number of possible lower targets in (1.1) is exactly

\[
 C_{m,q}:=\binom{2m-2q}{m-q}.
\tag{1.2}
\]

Dually, the upper shadow contains all of \(V(E)\), and the number of
rank-\(m+q\) upper targets containing it is the same \(C_{m,q}\).
Complementation sends a lower target avoiding \(V(E)\) to an upper target
containing \(V(E)\). Thus every catalogue statement below is automatically
two-sided after this identification.

## 2. A global catalogue lower bound

Let \(\mathcal E_q\) be the collection of distinct physical
\(q\)-matchings that occur as consecutive direction sets anywhere in a
family of pair-flip packets. Let \(\mathcal T_q\) be the rank-\(m-q\)
targets represented by those packets.

### Theorem 2.1 (cross-sector matching-catalogue bound)

For every packet family,

\[
 |\mathcal T_q|
 \leq|\mathcal E_q|\binom{2m-2q}{m-q}.
\tag{2.1}
\]

Consequently, if

\[
 |\mathcal T_q|\geq(1-\delta_q)N_q,
 \qquad N_q=\binom{2m}{m-q},
\]

then

\[
 \boxed{
 |\mathcal E_q|
 \geq(1-\delta_q)R_{m,q},
 \qquad
 R_{m,q}:=
 \frac{\binom{2m}{m-q}}{\binom{2m-2q}{m-q}}.
 }
\tag{2.2}
\]

#### Proof

Equation (1.2) bounds the targets served by each \(E\). Taking the union
over \(E\in\mathcal E_q\) proves (2.1); overlaps can only decrease the
union. Rearrangement gives (2.2). \(\square\)

No source-sector label occurs in this proof. A target may receive flow from
any middle macroprofile and from any associator shore. The only retained
datum is the physical empty-pair matching forced by its actual window.

The exact ratio in (2.2) is

\[
 R_{m,q}
 =\frac{(2m)!(m-q)!}{(m+q)!(2m-2q)!}
 =\frac{(2m)_{\underline{2q}}}
        {(m+q)_{\underline{2q}}}.
\tag{2.3}
\]

For \(q=o(m^{2/3})\),

\[
 \log R_{m,q}
 =2q\log 2-\frac{q^2}{m}
  +O\!\left(\frac qm+\frac{q^3}{m^2}\right),
\tag{2.4}
\]

and therefore

\[
 \log_2R_{m,q}
 =2q-\frac{q^2}{m\log 2}
  +O\!\left(\frac q m+\frac{q^3}{m^2}\right).
\tag{2.5}
\]

The coefficient \(2q\), rather than the intrafiber coefficient \(q\),
comes from forgetting the pair frame: a physical empty direction occupies
two ground coordinates.

## 3. Order profiles and hierarchy entropy

An order profile consists of a physical pair frame and a cyclic order of
some \(\ell\) of its pair directions. For \(q<\ell\), one profile exposes
at most \(\ell\) physical \(q\)-matchings.

### Corollary 3.1 (profile lower bound)

If \(T\) order profiles represent at least
\((1-\delta_q)N_q\) lower targets, then

\[
 \boxed{
 T\geq
 \frac{(1-\delta_q)R_{m,q}}{\ell}.
 }
\tag{3.1}
\]

This remains true if the profiles are distributed over different sectors,
cores, tensor packets, or associator shores.

Now suppose a hierarchical architecture starts from \(P\) base packet
profiles. Along a construction branch, node \(j\) has at most \(b_j\)
effective choices, so the total number of resulting profiles is at most

\[
 P\prod_jb_j.
\tag{3.2}
\]

### Corollary 3.2 (branch-entropy lower bound)

Under the hypotheses of Corollary 3.1,

\[
 \boxed{
 \log_2P+\sum_j\log_2b_j
 \geq
 \log_2R_{m,q}-\log_2\ell+\log_2(1-\delta_q).
 }
\tag{3.3}
\]

For a binary hierarchy with \(L\) effective decisions and
\(\ell\leq m\),

\[
 \boxed{
 L+\log_2P
 \geq
 2q-\frac{q^2}{m\log 2}
 -O\!\left(\log m+\frac{q^3}{m^2}\right)
 }
\tag{3.4}
\]

whenever \(\delta_q=o(1)\).

At \(q=A\sqrt m\), for fixed \(A>0\),

\[
 L+\log_2P
 \geq2A\sqrt m-O_A(\log m).
\tag{3.5}
\]

At \(q=\sqrt{m\log m}\), if relative near-coverage is required at that
depth, then

\[
 L+\log_2P\geq2\sqrt{m\log m}-O(\log m).
\tag{3.6}
\]

For the coefficient-one SCD criterion, (3.5) is the unconditional
consequence. The criterion permits total \(o(W)\) misses, while
\(N_q=\Theta_A(W)\) for fixed \(q=A\sqrt m\), so
\(\delta_q=o(1)\). At the calibrated growing endpoint,
\(N_H=o(W)\), and missing that entire endpoint could still cost only
\(o(W)\). Thus (3.6) needs a stronger layerwise relative-near-cover
hypothesis and must not be inferred merely from aggregate \(o(W)\) defect.

## 4. A matching upper bound for global shadow support

The entropy lower bound is sharp up to polynomial factors even when all
sector labels are forgotten.

Choose a uniformly random physical \(q\)-matching \(E\) on \([2m]\). Its
set of \(2q\) endpoints is a uniformly random \(2q\)-subset. For a fixed
target \(S\in\binom{[2m]}{m-q}\),

\[
 \Pr(V(E)\cap S=\varnothing)
 =\frac{\binom{m+q}{2q}}{\binom{2m}{2q}}
 =R_{m,q}^{-1}.
\tag{4.1}
\]

### Theorem 4.1 (global interval-catalogue theorem)

For every \(q<m\), there is a collection \(\mathcal C_q\) of at most

\[
 \boxed{
 R_{m,q}\bigl(\log N_q+2\bigr)
 }
\tag{4.2}
\]

physical \(q\)-matchings such that every rank-\(m-q\) target avoids the
endpoints of at least one member of \(\mathcal C_q\).

Each member of \(\mathcal C_q\) can be extended to a perfect matching of
\([2m]\) and then placed as a consecutive \(q\)-interval in a cyclic order
of that perfect matching. The same catalogue covers every complementary
rank-\(m+q\) upper target.

#### Proof

Take

\[
 K=\left\lceil R_{m,q}(\log N_q+1)\right\rceil
\]

independent random \(q\)-matchings. By (4.1), a fixed target is missed by
all of them with probability at most

\[
 (1-R_{m,q}^{-1})^K
 \leq e^{-K/R_{m,q}}<e^{-1}N_q^{-1}.
\]

A union bound over the \(N_q\) targets gives expected uncovered count less
than one, so some realization covers all targets. The rounding allowance
gives (4.2).

The unused \(2m-2q\) vertices have even cardinality, so every chosen
\(q\)-matching extends to a perfect matching. Order its \(q\) distinguished
edges consecutively and put the remaining edges arbitrarily after them.
\(\square\)

Taking the union of these catalogues gives simultaneous support at all
depths.

### Corollary 4.2 (multiscale support catalogue)

For \(H=o(m)\), there is one order-profile library supporting every lower
target at every depth \(q\leq H\), of size

\[
 T_{\leq H}
 \leq\sum_{q=1}^H R_{m,q}(\log N_q+2).
\tag{4.3}
\]

In particular,

\[
 \log_2T_{\leq H}
 \leq
 2H-\frac{H^2}{m\log 2}
 +O\!\left(\log m+\frac{H^3}{m^2}\right).
\tag{4.4}
\]

#### Proof

Use Theorem 4.1 independently at every depth and take the union. For
\(q\leq H=o(m)\), the exact successive ratio is

\[
 \frac{R_{m,q+1}}{R_{m,q}}
 =\frac{2(2m-2q-1)}{m+q+1}=4-o(1).
\]

Hence the last term dominates the sum up to a polynomial factor, which
contributes only \(O(\log m)\) to its binary logarithm. Apply (2.5).
\(\square\)

The library in Corollary 4.2 is not an owner-disjoint cycle factor. It
certifies that cross-sector global sharing reduces the sectorwise
\(\binom rq\) demand to the essentially optimal \(4^q\) physical interval
demand. Long-residence extension, phase compatibility, and integral owner
selection remain separate.

## 5. An exact all-shuffle hierarchy

There is no lower bound on geometric hierarchy height alone.

Let a rooted binary tree have a set of labelled leaves. At an internal node
whose left and right subtrees contain \(a\) and \(b\) leaves, respectively,
an \((a,b)\)-shuffle is a binary word with \(a\) left symbols and \(b\)
right symbols. It interleaves a left child order and a right child order
without changing either internal order.

### Theorem 5.1 (exact hierarchical permutation resolution)

At every internal node allow all \(\binom{a+b}{a}\) shuffles. Starting from
the one-point orders at the leaves and making independent recursive choices,
the root outputs every linear order of the leaves exactly once.

#### Proof

Every root order has unique restrictions to the left and right leaf sets,
and a unique binary word recording from which side each successive element
came. By induction the two restricted orders each have a unique recursive
description, and the binary word is the unique root shuffle. Conversely
every pair of child orders and every shuffle gives one root order.
\(\square\)

The product of all local branch counts is consequently

\[
 \prod_{\text{internal }v}
 \binom{|v|}{|v_L|}
 =n!
\tag{5.1}
\]

for \(n\) leaves. A balanced tree has height \(\lceil\log_2n\rceil\), but
its total branch entropy is \(\log_2(n!)\).

After quotienting by cyclic rotation, every cyclic order occurs equally.
For any \(q\)-subset \(J\) of the leaves, incidence counting gives

\[
 \#\{\text{cyclic orders in which }J\text{ is an interval}\}
 =q!(n-q)!.
\tag{5.2}
\]

Indeed, the total number of pairs consisting of a cyclic order and one of
its \(n\) length-\(q\) intervals is \(n!\), and symmetry over the
\(\binom nq\) choices of \(J\) gives
\(n!/\binom nq=q!(n-q)!\).

Thus an all-shuffle hierarchy is an exact simultaneous consecutive-block
\(q\)-design for every \(q\). It is much larger than the catalogue of
Section 4, but it proves that “hierarchy depth” is not an invariant unless
the branching available at each node is bounded. Corollary 3.2 is properly
an entropy theorem.

Every resulting leaf order \(\pi\) is a legal isometric pair-flip necklace:
the direction word \(\pi\pi\) gives an isometric \(2n\)-cycle in \(Q_n\).
The all-shuffle theorem does not say that cycles carrying different root
orders partition \(Q_n\). Thus it solves the hierarchical order-resolution
problem but not the common-owner 2-factor problem.

## 6. Exact fractional sharing across all source sectors

The all-shuffle theorem also recovers the global cross-sector inclusion
flow without choosing a separate construction at each depth.

For every middle set \(X\in\binom{[2m]}m\), take all \(m!\) linear orders
of its elements. For an order \(\pi\), let

\[
 L_q(X,\pi)=X\setminus\{\pi_1,\ldots,\pi_q\}.
\tag{6.1}
\]

### Theorem 6.1 (simultaneous uniform flag multicover)

For every \(q\leq m\), every
\(S\in\binom{[2m]}{m-q}\) occurs as \(L_q(X,\pi)\) exactly

\[
 \boxed{
 \binom{m+q}{q}\,q!(m-q)!
 =\frac{(m+q)!(m-q)!}{m!}
 }
\tag{6.2}
\]

times.

#### Proof

Choose the \(q\)-set \(D=X\setminus S\) from the \(m+q\) coordinates
outside \(S\), giving \(\binom{m+q}{q}\) choices. For fixed \(D\), the first
\(q\) entries of \(\pi\) are precisely \(D\) in any of \(q!\) orders, and
the remaining \(m-q\) elements occur in any of \((m-q)!\) orders.
\(\square\)

The same \(\pi\) supplies the nested flags for every \(q\), so this is an
exact multiscale theorem rather than a collection of independent
depthwise flows. It is fractional from the coefficient-one viewpoint
because every middle owner is repeated \(m!\) times. Reducing this
multicover to one order per owner while retaining balanced loads is exactly
the labelled synchronization/integral-resolution problem.

## 7. Application to the tensor associator

Tensor \(r\) copies of the eight-coordinate pair-frame associator. A shore
vector

\[
 \varepsilon\in\{0,1\}^r
\]

chooses one of at most \(2^r\) physical pair frames on the common tensor
owner support. Under the native Hamming bundling, each shore vector carries
one macro-order, so \(P\) external packet embeddings and all tensor corners
supply at most

\[
 P2^r
\tag{7.1}
\]

effective order profiles.

### Corollary 7.1 (tensor entropy condition)

If these profiles represent a \(1-o(1)\) fraction of the physical lower
targets at depth \(q\), then

\[
 \boxed{
 r+\log_2P
 \geq
 2q-\frac{q^2}{m\log 2}-O(\log m+q^3/m^2).
 }
\tag{7.2}
\]

In particular, at \(q=A\sqrt m\),

\[
 r+\log_2P\geq2A\sqrt m-O_A(\log m).
\tag{7.3}
\]

This condition includes all cross-sector flow. If the flow uses many
packet embeddings, their diversity is counted by \(P\); if it relies on
the local associator tensor, its diversity is counted by \(2^r\).

The condition is necessary but not sufficient. The current local
associator has two additional rigidities.

1. Every shore preserves the physical owner support, but its Boolean
   moment action satisfies
   \[
    \Pi_{\rm mac}A_{q,I}=0\qquad(I\ne\varnothing).
   \]
   Thus shore choices do not alter macroblock occupancy support.
2. The all-length suspension appends the same tail order to both shores.
   It changes the local pair frame but does not provide an arbitrary
   interleaving of the direction necklaces belonging to different
   macroblocks.

Therefore the \(r\) shore bits are frame entropy, not shuffle entropy. They
can meet (7.2) only by using the global cross-sector flow; they cannot
repair the native sectorwise support defect internally.

The abstract frame catalogue is nevertheless compatible with the local
move type of the associator.

### Lemma 7.2 (pair-frame flip connectivity)

The graph of perfect matchings of \([2m]\), with an edge for every
four-coordinate recoupling

\[
 ab\mid cd\longleftrightarrow ac\mid bd,
\tag{7.4}
\]

is connected. Any two perfect matchings can be joined by at most \(m-1\)
such recouplings.

#### Proof

The union of two perfect matchings is a disjoint union of alternating even
cycles. On an alternating \(2k\)-cycle, a recoupling of two adjacent old
matching edges installs one desired edge and leaves an alternating
\(2(k-1)\)-cycle. Thus \(k-1\) recouplings transform the old matching into
the new one on that component. Summing \(k-1\) over components gives at
most \(m-1\). \(\square\)

The bounded local pair-frame associator is an exact owner-preserving lift
of one edge (7.4), after adding its reservoir pairs. Hence every frame in
the support catalogue is reachable at the abstract matching level.
However, a sequence of overlapping recouplings is not automatically a
sequence of simultaneous factor trades: reservoirs overlap, the ownership
components need not remain disjoint, and the long-cycle phases must agree.
Lemma 7.2 proves reachability, not composability.

The existing recursive isometric-cube 2-factor illustrates the same
distinction on the ordering side. It has logarithmic geometric depth and
many state-dependent orders, but every internal merge uses an alternating
shuffle. Its direction intervals therefore retain the dyadic-balance
invariant. Replacing those alternating merges by the all-shuffle resolution
would remove the order-support invariant, but no owner-preserving torus
factorization realizing all those shuffles is presently proved.

## 8. The exact successor theorem

The profile question is now quantitatively settled:

* sectorwise balance costs
  \(\log_2\binom rq-O(\log r)\) macro-order bits;
* unrestricted physical cross-sector sharing costs only
  \(2q-q^2/(m\log 2)-O(\log m)\) combined frame/order bits;
* the latter exponent is achievable up to \(O(\log m)\) at the support
  level;
* geometric tree height can be \(O(\log m)\), provided the internal shuffle
  nodes carry the required entropy.

What remains for the tensor architecture is the following physical theorem.

> **Owner-preserving shuffle-associator theorem.** Construct a hierarchy of
> exact associator trades which, on a common owner support, realizes a
> profile subcatalogue of entropy at least \(2q-o(q)\), places each selected
> \(q\)-matching consecutively in a long isometric-cycle necklace, and
> permits one integral packet selection whose physical lower and upper
> shadows have total \(o(W)\) collision excess through every fixed Gaussian
> window.

The existing pair-frame associator supplies exact owner-preserving frame
switches. The all-shuffle theorem supplies the correct abstract multiscale
order resolution. Neither supplies their common physical realization.
That common realization, rather than a deeper native Hamming hierarchy, is
the remaining constant-one gate.
