# Fixed literal slots at positive height: exact reciprocal-\(C_8\) certification and disjoint-layer tensorization

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let \({\cal D}_s\) be the Dyck words of length \(2s\), and put

\[
                         B=C_s=\operatorname {Cat}_s.
\]

Fix a four-bit slot beginning after exactly \(t\) bits, where
\(0\le t\le2s-4\).  The replacement

\[
                U1100V\longleftrightarrow U1010V,
                \qquad |U|=t,                         \tag{0.1}
\]

is not restricted to the case in which \(U\) is a Dyck word.  Every
occurrence at positive height is also a literal, boundary-fixed lift of
the canonical rank-two reciprocal \(C_8\).  Consequently:

1. every fixed slot contains exactly
   \[
                              C_{s-2}                 \tag{0.2}
   \]
   reciprocal rectangles;
2. if \(t=2a\), the old top-level count
   \[
                         C_aC_{s-a-2}                 \tag{0.3}
   \]
   is precisely the height-zero subfamily of (0.2), not the full fixed-slot
   count;
3. pairwise disjoint four-bit slots compose simultaneously.  Their full
   ownership-overlay components are exact Boolean cubes;
4. for \(u\) disjoint slots, the exact sparse-edit moment is
   \[
   \boxed{
   \Xi_u={4\over C_s}\sum_{h=1}^u
          \binom uh h2^hC_{s-2h}};                   \tag{0.4}
   \]
5. for every fixed \(u\),
   \[
   \boxed{
   \Xi_u={u\over2}\left({9\over8}\right)^{u-1}
          +O_u(s^{-1})=O_u(1)=o(\sqrt s).}           \tag{0.5}
   \]

The ambient-distance assertion in Item 4 is essential.  A lifted
rectangle is not merely locally short: in the full rooted coordinate
order it makes exactly one adjacent transposition in the deletion list and
one in the insertion list.  Thus its ambient distance is exactly two.

Disjointness is load-bearing.  The overlapping slots on the three roots

\[
 110010S\longleftrightarrow101010S
 \longleftrightarrow101100S                         \tag{0.6}
\]

do not compose: the two precomputed changes create the consecutive states
\(145\) and \(236\), which are not Johnson adjacent.  Hence the theorem
does not license nested or overlapping slot banks.

At the raw marked-occurrence level, \(u\) layers supply \(uC_{s-2}\)
local rectangles.  Therefore a scalar demand \(\delta C_s\) requires the
exact finite threshold

\[
 u\ge
 \left\lceil\delta{C_s\over C_{s-2}}\right\rceil,
 \qquad
 {C_s\over C_{s-2}}
 ={4(2s-1)(2s-3)\over s(s+1)}=16+O(s^{-1}).          \tag{0.7}
\]

In particular a fixed demand with \(1/4\le\delta<7/16\) needs between
four and seven disjoint layers for all sufficiently large \(s\), and
these layers satisfy (0.5).  This proves that there is no component-size
or sparse-edit obstruction to the raw layer count.

For the canonical physical MWB/PCap consumer there is, however, a stronger
negative conclusion.  Choose the coherently tagged slots to begin in odd
coordinates.  Every packet is then literally a coordinate transposition
from

\[
 H_s=\langle(2\ 3),(4\ 5),\ldots,(2s-2\ 2s-1)\rangle. \tag{0.8}
\]

Consequently the total physical target mass on every \(H_s\)-orbit is
invariant, including collars and mixed-window effects.  The canonical
fatal orbit \(\{2,3\}\) contains at least \(C_s+C_{s-1}\) occurrences,
so at cap \(p=C_s/\theta\), \(4\le\theta<16\), it retains excess

\[
 C_s+C_{s-1}-2p=\Omega(C_s).                         \tag{0.9}
\]

Thus this exact shifted-layer class is quantitatively ruled out for the
physical coefficient-one gate.  The required next primitive must cross
the \(H_s\)-target orbits; a further coordinate-conjugate leaf rectangle
cannot do so.

## 1. Fixed-slot counting and the reconciliation with top-level seams

For a word \(d=d_1\cdots d_{2s-4}\in{\cal D}_{s-2}\), write

\[
 d=UV,\qquad |U|=t,
\]

and define

\[
 I_{t,0}(d)=U1100V,
 \qquad
 I_{t,1}(d)=U1010V.                                  \tag{1.1}
\]

Both inserted words are balanced nonnegative excursions.  Hence every
prefix before the insertion keeps its old height, every prefix inside the
insertion stays at least at the incoming height, and every later prefix
has its old height.  Thus both words in (1.1) lie in \({\cal D}_s\).

Conversely, deleting the displayed four-bit block from any word in (0.1)
leaves a Dyck word in \({\cal D}_{s-2}\).  Deletion and insertion are
inverse, and the two orientations in (1.1) pair with one another.
Therefore there are exactly \(2C_{s-2}\) active roots and
\(C_{s-2}\) rectangle pairs at the fixed slot.  This proves (0.2).

Now suppose \(t=2a\).  The occurrence is at a top-level Dyck-component
boundary exactly when the prefix \(U\) has height zero.  After deletion,
this is exactly the factorization

\[
                         d=PR,
 \qquad P\in{\cal D}_a,\quad R\in{\cal D}_{s-a-2}.  \tag{1.2}
\]

It has \(C_aC_{s-a-2}\) choices.  All remaining

\[
                         C_{s-2}-C_aC_{s-a-2}        \tag{1.3}
\]

fixed-slot rectangles begin at positive height.  If \(t\) is odd, height
zero is impossible by parity, so every one of the \(C_{s-2}\) rectangles
is outside the top-level-boundary catalogue.  This proves the exact
reconciliation of (0.2) and (0.3).

## 2. The base anchored rectangle is a literal reciprocal \(C_8\)

The two canonical \({\cal D}_2\)-rooted Johnson traces are

\[
\begin{array}{c|ccc}
1100&12&14&34\\
1010&13&23&24.
\end{array}                                             \tag{2.1}
\]

The alternative traces are

\[
\begin{array}{c|ccc}
1100&12&23&34\\
1010&13&14&24.
\end{array}                                             \tag{2.2}
\]

Every consecutive pair in both tables is a Johnson edge.  The state
multiset on either shore is all six two-subsets of \([4]\), while the
adjacent-union multiset on either shore is

\[
                         \{123,124,134,234\}.          \tag{2.3}
\]

The two endpoints of each named row are unchanged and complementary.
Thus (2.1)--(2.2) are two anchored exact \({\cal D}_2\)-port factors with
the same state and colour ledgers.

In the state--union incidence graph, their symmetric difference is the
literal alternating cycle

\[
 12-124-24-234-34-134-13-123-12.                     \tag{2.4}
\]

The edges alternate between (2.1) and (2.2).  The four incidences through
the exchanged middle states which occur on both shores cancel.  Hence
(2.4) is precisely the reciprocal \(C_8\), not merely a signed ledger
identity.

## 3. Every marked Dyck gap is an aligned context

We need more than the fact that (1.1) stays Dyck: the local traces must
lift with fixed outer endpoints and with their two adjacent edits still
adjacent in the ambient rooted order.

### Lemma 3.1 (marked-gap context lemma)

Let \(d\in{\cal D}_r\) and mark any of its \(2r+1\) gaps.  The map

\[
                         z\longmapsto UzV             \tag{3.1}
\]

obtained by inserting a Dyck word \(z\) in that gap is a one-hole Dyck
context generated by concatenation and primitive wrapping.  In the MSW
trace recursion, the coordinates and phases belonging to \(z\) form one
aligned local slab.  A boundary-fixed exact port-factor replacement in
that slab remains exact in the ambient factor.

#### Proof

Use the unambiguous Dyck grammar

\[
                         w=1p0q,qquad p,q\in{\cal D}.
                                                               \tag{3.2}
\]

Induct on \(|d|\).  The empty word has only the context \(\Box\).  For
\(d=1p0q\), a marked gap is either in the copy of \(p\), in the copy of
\(q\), or at one of their boundary gaps.  The resulting context is built
from a smaller one by one of

\[
 C\longmapsto 1C0q,qquad
 C\longmapsto 1p0C,qquad
 C\longmapsto Cq,qquad
 C\longmapsto pC,                                    \tag{3.3}
\]

after decomposing a fixed Dyck prefix into primitive components.  This
proves the context assertion.

For trace alignment, use the MSW recursion

\[
 \rho(1p0q)=
 \bigl(|p|+2,\ |p|+2-\rho(\operatorname{rev}p),\ 1,
                    |p|+2+\rho(q)\bigr).             \tag{3.4}
\]

Each operation in (3.3) either appends a common permutation block, or
places the varying block inside one displayed block of (3.4), followed by
an affine coordinate relabelling and possibly reverse-complement duality.
It never interleaves that block with an exterior block.  Thus the local
four-entry \(\rho\)-block stays consecutive.  Every exterior Dyck block
has even length.  When the omitted order is converted to the rooted
coordinate order by reading positions two at a time, the first and third
positions of this four-entry block are therefore consecutive, and so are
its second and fourth positions.  These are respectively the two local
deletion and the two local insertion coordinates.  Hence the local trace
is a contiguous aligned two-transition slab.  Its two boundary states are
carried to two fixed ambient boundary states.

Inside the slab every state has the form

\[
                         O\mathbin{\dot\cup}\iota(X), \tag{3.5}
\]

where \(O\) is fixed through the slab and \(\iota\) is one affine
injection of the local coordinates.  Adjacent unions have the analogous
form \(O\dot\cup\iota(Y)\).  Therefore equality of the two local state
multisets and the two local union multisets is preserved by (3.5), while
the fixed local ports preserve the two outer incident edges.  This proves
ambient exactness. \(\square\)

### Corollary 3.2 (positive-height certification)

For every \(d\in{\cal D}_{s-2}\) and every fixed slot, the two canonical
rows in (1.1), together with the two lifted alternatives (2.2), form a
sealed, boundary-fixed affine/spectator copy of (2.4).

#### Proof

Apply Lemma 3.1 to the marked gap of \(d\), with local hole size two, and
then apply the exact ledgers and fixed ports from Section 2.  Suppressing
\(O\) and undoing \(\iota\) recovers (2.4), so the lifted packet is a
literal reciprocal \(C_8\).  No condition on the incoming height was used.
\(\square\)

For one fixed slot, distinct \(d\)'s give disjoint pairs of canonical
rows.  Since the canonical factor owns every state and union token once,
their old packet token sets are disjoint.  Each alternative packet owns
exactly the same token set as its old pair.  Hence all \(C_{s-2}\)
packets in one layer may be installed simultaneously.

## 4. Exact ambient adjacent-transposition distance

The sparse-edit theorem measures the full rooted coordinate orders, not
an abstract local distance.  We now verify the required lift exactly.

For a rooted complementary Johnson path

\[
 X_0,X_1,\ldots,X_s,
\]

write

\[
 d_i=X_{i-1}\setminus X_i,qquad
 a_i=X_i\setminus X_{i-1}.                            \tag{4.1}
\]

Its rooted coordinate order, with the distinguished coordinate last, is

\[
                    (d_1,\ldots,d_s,a_1,\ldots,a_s,\infty),
                                                               \tag{4.2}
\]

up to the fixed common convention of reversing both displayed blocks.
That harmless convention does not change adjacent-transposition distance.

For the first row of (2.1), the local deletion and insertion lists are

\[
                         (2,1),\qquad(4,3),           \tag{4.3}
\]

while in (2.2) they are

\[
                         (1,2),\qquad(3,4).           \tag{4.4}
\]

For the second row, the corresponding pairs are

\[
                 (1,3),(2,4)\quad\longleftrightarrow
                 (3,1),(4,2).                        \tag{4.5}
\]

Thus either rooted row changes by exactly two adjacent transpositions.

Lemma 3.1 places the two local transitions consecutively in the ambient
Johnson path.  Hence the two local deletion coordinates are consecutive
in the ambient deletion block of (4.2), and the two local insertion
coordinates are consecutive in its insertion block.  Affine relabelling,
reverse-complement duality, and adjoining exterior coordinates preserve
this adjacency.  The lifted old and new ambient orders therefore differ
by the same two adjacent transpositions.

They cannot have distance less than two: one transposition changes the
relative order of only one pair, whereas (4.3)--(4.5) reverse one
deletion pair and one disjoint insertion pair.  Consequently every lifted
rectangle row has the exact ambient distance

\[
                              d_\infty=2.             \tag{4.6}
\]

## 5. Disjoint slots compose

Fix \(u\) slots \(I_1,\ldots,I_u\) whose four-bit interiors are pairwise
disjoint.  For a root \(x\), let

\[
 J(x)=\{j:x|_{I_j}\in\{1100,1010\}\}.              \tag{5.1}
\]

For \(j\in J(x)\), let \(\tau_jx\) toggle the two local words.

### Lemma 5.1 (root and slab commutation)

The set \(J(x)\) is invariant under every allowed toggle.  The maps
\(\tau_i,\tau_j\) commute.  In every row eligible at both slots, the two
lifted reciprocal rectangles act in disjoint aligned trace slabs, meeting
at most in a boundary state which both fix.

#### Proof

The first two assertions are literal: the toggles inspect and change
disjoint sets of four bit positions.

Delete all eligible blocks and regard their old positions as marked holes
in the reduced Dyck word.  The context induction in Lemma 3.1 extends to
several marked holes.  At every first-return split, two holes either enter
different displayed blocks of (3.4), or remain together in one smaller
block.  Induction therefore gives disjoint local permutation and trace
slabs.  If two holes are consecutive, their slabs share only the common
port state; both local factors fix that state. \(\square\)

### Theorem 5.2 (simultaneous exactness)

Every choice of shores for the \(u\) complete fixed-slot layers is one
anchored exact factor.  The order of applying the layers is irrelevant.

#### Proof

Within a row, Lemma 5.1 gives disjoint boundary-fixed slabs, so the local
path replacements commute and every resulting row remains a Johnson path
with its old complementary ports.  Globally, each local packet merely
permutes the state and adjacent-union tokens originally owned by its two
row slabs.  Distinct slab interiors owned disjoint tokens in the exact
base factor; a possible common boundary token is fixed by both packets.
Their replacement token multisets are the same.  Therefore all local
state and union discrepancies add to zero.  The two complete ownership
ledgers remain exact. \(\square\)

This proof is a strand recombination proof on the shared rows.  It does
not make the invalid inference that overlapping two-row packets with one
common old root are automatically independent.

## 6. Collision counts and exact full-overlay components

For a specified set \(T\subseteq[u]\), \(|T|=h\), delete all \(h\)
four-bit blocks from right to left.  Record one of the two orientations at
each slot.  The inverse inserts those excursions from left to right at the
adjusted gaps.  Hence

\[
 \boxed{
 \#\{x\in{\cal D}_s:T\subseteq J(x)\}
       =2^hC_{s-2h}.}                                  \tag{6.1}
\]

In particular, one layer has \(2C_{s-2}\) active roots and
\(C_{s-2}\) edges, while any specified \(h\) layers meet in
\(C_{s-2h}\) root \(h\)-cubes.

Compare the canonical factor with the factor in which all \(u\) layers
are installed.  Outside the eligible slots, every row segment keeps its
owner.  Inside slot \(j\), every transferred state or union token changes
owner only between \(x\) and \(\tau_jx\).  Therefore no full-overlay edge
leaves the root orbit

\[
                         \{\tau_Tx:T\subseteq J(x)\}. \tag{6.2}
\]

Conversely the lifted \(C_8\) contains a transferred token on every
\(j\)-edge of (6.2).  Thus all coordinate edges of this cube occur in the
full state-and-colour overlay, so it is connected.  Consequently (6.2)
is exactly one full component and has side size

\[
                              b(x)=2^{|J(x)|}.        \tag{6.3}
\]

By Section 4 and Lemma 5.1, a row eligible in \(r\) slots changes by
\(2r\) disjoint adjacent transpositions.  The reversed pairs are disjoint,
so inversion distance also gives the matching lower bound.  Hence

\[
                              d(x)=2|J(x)|.           \tag{6.4}
\]

## 7. The exact edit moment

Define the eligibility polynomial

\[
                         Z_u(z)=\sum_{x\in{\cal D}_s}
                                  z^{|J(x)|}.          \tag{7.1}
\]

The identity

\[
 z^{|J|}=\sum_{T\subseteq J}(z-1)^{|T|}
\]

and (6.1) give

\[
 Z_u(z)=\sum_{h=0}^u\binom uh
           \bigl(2(z-1)\bigr)^hC_{s-2h}.             \tag{7.2}
\]

In a component with eligibility size \(r\), every one of its \(2^r\)
roots has distance \(2r\) and the side size is \(2^r\).  Therefore the
definition of the size-weighted edit moment gives

\[
\begin{aligned}
 C_s\Xi_u
  &=\sum_{x\in{\cal D}_s}2^{|J(x)|}\,2|J(x)|\\
  &=4Z_u'(2).
\end{aligned}                                           \tag{7.3}
\]

Substitution of (7.2) proves the exact formula (0.4).

For fixed \(h\), the Catalan quotient satisfies

\[
 {C_{s-2h}\over C_s}=16^{-h}\bigl(1+O_h(s^{-1})\bigr), \tag{7.4}
\]

which follows directly by multiplying the \(2h\) consecutive ratios

\[
                         {C_{n-1}\over C_n}
                         ={n+1\over2(2n-1)}.
\]

Using (7.4) in (0.4),

\[
\begin{aligned}
 \Xi_u
 &=4\sum_{h=1}^u\binom uh h8^{-h}+O_u(s^{-1})\\
 &={u\over2}\left(1+{1\over8}\right)^{u-1}
       +O_u(s^{-1}),
\end{aligned}                                           \tag{7.5}
\]

which is (0.5).  Formula (0.4), rather than (7.5), remains authoritative
when \(u\) grows with \(s\).

## 8. Why overlap is excluded

Take the three local roots in (0.6) with \(S\) suppressed.  Their
canonical paths begin

\[
\begin{array}{c|c}
110010&125-145-345-346\\
101010&135-235-245-246\\
101100&134-234-236-256.
\end{array}                                             \tag{8.1}
\]

The first rectangle changes the shared middle row to

\[
                         135-145-245-246,              \tag{8.2}
\]

and the second changes it to

\[
                         135-235-236-246.              \tag{8.3}
\]

Applying both precomputed changes would force

\[
                         135-145-236-246.              \tag{8.4}
\]

But \(145\cap236=\varnothing\), so these two states have Johnson distance
three rather than one.  There is no four-set union colour joining them.
Adding a common exterior spectator preserves this failure.  Thus the
overlapping slots have no Boolean commutator, proving that the disjointness
hypothesis of Theorem 5.2 cannot be dropped.

## 9. Exact MWB boundary

Each fixed slot has \(C_{s-2}\) marked local packets, so \(u\) disjoint
slots have \(uC_{s-2}\) marked occurrences even though some roots support
several packets.  Equation (0.7) is therefore the exact raw-count
threshold.  The maximum number of disjoint four-bit slots is

\[
                              \lfloor s/2\rfloor,      \tag{9.1}
\]

so four through seven layers exist once \(s\ge14\).

What has been proved is the following complete implication:

\[
 \begin{array}{c}
 \text{fixed finite raw layer demand}\\
 \Downarrow\\
 \text{enough exact disjoint reciprocal-}C_8\text{ packets}\\
 \text{with }\Xi=O(1)=o(\sqrt s).
 \end{array}                                           \tag{9.2}
\]

The full physical conclusion is negative, not merely unproved.  A lifted
packet has an exact signed local entrance/exit pair, and physical target
collisions can obscure its four separate arms.  Nevertheless those
collisions cannot move mass between the coordinate-group orbits proved in
Section 10.  Moreover, for a fixed consecutive intersection window, every
rectangle strictly inside the window cancels by the octahedral
triple-intersection identity; only the rectangles at the two window
boundaries can remain visible.

Thus the construction certifies the fixed-slot count, simultaneous factor
legality, full component sizes, and the required sparse-edit scale, but
Section 10 closes it as a canonical physical coefficient-one repair.

## 10. Coordinate-orbit obstruction, with ports and collars audited

Return to the four local labels

\[
                         \alpha,\beta,\gamma,\delta
\]

in their physical order.  After rotating the common outside order behind
them, the two old and two new coordinate orders are

\[
\begin{aligned}
 C&=(\delta,\beta,\gamma,\alpha,T),&
 D&=(\beta,\alpha,\delta,\gamma,T),\\
 C'&=(\delta,\gamma,\beta,\alpha,T),&
 D'&=(\gamma,\alpha,\delta,\beta,T).
\end{aligned}                                           \tag{10.1}
\]

Therefore, for \(\tau=(\beta\ \gamma)\),

\[
                              C'=\tau C,qquad D'=\tau D. \tag{10.2}
\]

The roots are exchanged by \(\tau\).  Equivalently, after anchoring rows
by their Dyck ports, the new row rooted at \(P\) is

\[
                         \omega_1(P)=\tau\omega_0(\tau P). \tag{10.3}
\]

This is an identity of the complete physical coordinate orders, not only
of the local three-state traces.

Choose the coherently oriented slots to start in odd coordinates.  Then
\(\beta\) is even, \(\gamma=\beta+1\) is odd, and every corresponding
\(\tau\) belongs to the group \(H_s\) in (0.8).  The transpositions of
disjoint slots commute.  On a root cube with eligibility set \(J\), the
factor obtained by installing a set \(A\subseteq J\) of layer bits obeys

\[
 \omega_A(P)=\sigma_A\omega_0(\sigma_AP),
 \qquad
 \sigma_A=\prod_{j\in A}\tau_j\in H_s.              \tag{10.4}
\]

### Theorem 10.1 (full physical orbit invariance)

Fix a protected rank and let \(\mu_F(T)\) be the complete physical target
histogram of a factor \(F\), including every row, every relevant cyclic
start, and its literal exterior collar.  For every factor obtained by
legal disjoint-slot cubical composition and every \(H_s\)-orbit
\({\cal O}\),

\[
                \boxed{
                \sum_{T\in{\cal O}}\mu_F(T)
                =\sum_{T\in{\cal O}}\mu_{F_0}(T).}   \tag{10.5}
\]

The identity holds separately at every rank, so it also holds after the
standard rank weights are applied.

#### Proof

For a coordinate order \(\omega\) and a pointed cyclic start \(r\), let
\(\Gamma(\omega,r)\) be its physical target.  Intersections, unions, and
adjoining an exterior collar are coordinate-equivariant.  Extending
\(\sigma\in H_s\) by the identity on all exterior coordinates gives

\[
                         \Gamma(\sigma\omega,r)
                         =\sigma\Gamma(\omega,r).     \tag{10.6}
\]

Equation (10.3) gives a bijection from the old occurrences on the two
packet rows to the new occurrences, using the same cyclic start \(r\),
and (10.6) sends each target to another member of the same
\(H_s\)-orbit.  Summing over the packet preserves every orbit total.

For several disjoint slots, (10.4) gives the same bijection on every root
cube with \(\sigma_A\in H_s\).  Alternatively one may install the layers
sequentially and apply the one-packet argument at each step.  This proof
uses the literal simultaneous factor, so every mixed-window term is
already included; no additivity of isolated four-arm columns is assumed.
Summing the component identities proves (10.5). \(\square\)

There is no collar loophole in (10.6): (10.2) is an equality of the full
ambient row orders after the local transposition is extended by the
identity outside the hole.  There is also no port-rotation loss.  The
transposition fixes \(\infty\) and maps the old port \(\tau P\) to the new
port \(P\) at the same cyclic cut, so the pointed start is transported
without rotating or reversing the row.

There is one wording caveat.  A geometrically named subfamily of starts
need not itself be fixed under the reanchoring \(P\leftrightarrow\tau P\).
Thus invariance should be asserted for the full orbit histogram, or for a
marked occurrence family transported through the above bijection, not for
an untransported start label.  This caveat does not weaken the fatal-pair
argument.

### Corollary 10.2 (fatal two-cell orbit)

In the canonical one-step parent, choose the distinguished canonical
occurrences whose singleton targets are \(2\) and \(3\).  The target-2
occurrences are indexed by all \({\cal D}_s\), while deleting the forced
initial leaf indexes the target-3 occurrences by \({\cal D}_{s-1}\).
Their numbers are therefore

\[
                              C_s,qquad C_{s-1}.      \tag{10.7}
\]

Transport these marked occurrences through the packet bijections in the
proof of Theorem 10.1.  They remain distinct physical occurrences and,
because the \(H_s\)-orbit of the singleton \(\{2\}\) is exactly
\(\{\{2\},\{3\}\}\), every transported target is still \(2\) or \(3\).
Hence the complete final loads satisfy the robust inequality

\[
                         \mu_F(2)+\mu_F(3)
                         \ge C_s+C_{s-1}.             \tag{10.8}
\]

If the two canonical distinguished families exhaust the initial singleton
orbit, then (10.5) gives equality in (10.8); equality is not needed.

For \(p=C_s/\theta\), \(4\le\theta<16\), convexity gives

\[
\begin{aligned}
 (\mu_F(2)-p)_++(\mu_F(3)-p)_+
 &\ge \mu_F(2)+\mu_F(3)-2p\\
 &\ge C_s+C_{s-1}-{2C_s\over\theta}\\
 &=C_s\left(
    1+{s+1\over2(2s-1)}-{2\over\theta}
           \right)\\
 &\ge {1\over2}C_s.                                  \tag{10.9}
\end{aligned}
\]

Here

\[
                         {C_{s-1}\over C_s}
                         ={s+1\over2(2s-1)},          \tag{10.10}
\]

and the last inequality uses \(2/\theta\le1/2\).  Thus the surviving
physical PCap is \(\Omega(C_s)\), uniformly in the whole fatal range.

The only qualification to Theorem 10.1 would be a deliberately
non-equivariant artificial carrier whose weights depend on the original
root/start name rather than on the literal physical occurrence.  The MWB
and PCap histograms at a fixed rank count literal occurrences uniformly,
so that qualification is irrelevant here.  A successful constructive
replacement must use at least one non-coordinate packet that transfers
mass between distinct \(H_s\)-orbits while retaining exact ports and
\(\Xi=o(\sqrt s)\).

### Corollary 10.3 (arbitrary slot parity)

The PCap obstruction holds for every family of pairwise disjoint fixed
slots, without the odd-start restriction.

#### Proof

Let \(\Gamma\) be generated by the middle-pair transpositions of all
chosen slots.  The proof of Theorem 10.1 uses only membership of each
packet transposition in \(\Gamma\), so it preserves every
\(\Gamma\)-orbit total.

A valid middle pair contains coordinate \(2\) only for the slot
\([1,4]\).  If this slot is absent, \(\Gamma\) fixes \(2\), and the
\(C_s\) transported distinguished occurrences at target \(2\) give

\[
                         K_p\ge C_s-p
                              =\left(1-{1\over\theta}\right)C_s.
\]

If \([1,4]\) is present, disjointness forces every other slot to begin at
coordinate \(5\) or later.  Hence the \(\Gamma\)-orbit of \(2\) is
exactly \(\{2,3\}\), and already the same \(C_s\) distinguished
occurrences give

\[
                         K_p\ge C_s-2p
                              =\left(1-{2\over\theta}\right)C_s
                              \ge {1\over2}C_s.
\]

The additional \(C_{s-1}\) family in Corollary 10.2 only strengthens the
second bound. \(\square\)
