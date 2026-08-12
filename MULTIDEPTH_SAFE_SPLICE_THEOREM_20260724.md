# Multidepth-safe splicing of cyclic-strip Johnson cycles

## Scope and conclusion

This note isolates the exact operation that would remove the
`p H^2` independent-cut loss in
`RAINBOW_MULTIDEPTH_STRIP_MATCHING_20260724.md`.

There are two different questions.

1. **Geometric safety.**  Does a two-cycle switch remain a Johnson cycle,
   retain the correct ranks of every depth-`q` intersection and union, and
   avoid short coordinate runs?
2. **Colour safety.**  Are all new depth-`q` shadows distinct from one
   another and from every retained shadow in the whole packing?

The first question has a dense answer.  For the complete family of cyclic
strips, a regular rectangular-switch incidence multigraph is available.
When `ell>2H`, all but `O(H^2/m)` of its ambient incidences are geometrically
safe; after imposing vertex-disjointness, the loss is
`O((H^2+ell^2)/m)`.

The second question is exactly a simultaneous hole-routing condition.  It
does not follow from the number of uncovered shadow colours.  Already at
depth one, every rectangular switch needs two prescribed lower holes and
two prescribed upper holes.  This is the remaining obstruction to turning
the dense ambient switch graph into a component-merging graph.

No claim of a full constant-one construction is made here.

---

## 1. Transition separation and shadow ranks

Let

\[
 T=(T_i)_{i\in\mathbb Z_s}
\]

be an oriented cycle in `J(2m,m)`.  Write

\[
 T_{i+1}=T_i-r_i+a_i,
 \qquad
 \tau_i=\{r_i,a_i\}.
\tag{1.1}
\]

Thus `tau_i` is the two-coordinate transition label of the `i`-th edge.
Call the cycle **`g`-separated** when

\[
 \tau_i\cap\tau_j=\varnothing
 \quad\text{whenever}\quad
 0<\operatorname{dist}_{\mathbb Z_s}(i,j)\le g.
\tag{1.2}
\]

### Lemma 1.1 -- separated transitions give exact shadows

If a path is `q`-separated on a block of `q` consecutive transitions, then

\[
 \left|\bigcap_{j=0}^{q}T_{i+j}\right|=m-q,
 \qquad
 \left|\bigcup_{j=0}^{q}T_{i+j}\right|=m+q.
\tag{1.3}
\]

#### Proof

No coordinate toggles twice in the block.  Hence the `q` removed
coordinates are distinct members of `T_i`, the `q` inserted coordinates are
distinct members of its complement, and no inserted coordinate is later
removed.  The intersection is `T_i` minus the `q` removals and the union is
`T_i` plus the `q` insertions.  This proves (1.3).  ∎

In particular, `H`-separation forbids both internal one-runs and internal
zero-runs of length at most `H`.  To separate the several crossing windows
created at one splice, we impose one additional local condition: all
transition labels among the `H` old edges before the seam, the new seam
edge, and the `H` old edges after the seam are pairwise disjoint.  Call this
the **`H`-seam condition**.

### Lemma 1.2 -- crossing windows at one separated seam are distinct

Suppose the transition labels in the `2q-1`-edge neighbourhood of one seam
are pairwise disjoint.  The `q` depth-`q` lower shadows crossing that seam
are pairwise distinct, and so are the `q` upper shadows.

#### Proof

Compare crossing windows beginning at edges `u<v`.  The coordinate added
on edge `u` is absent from the first vertex of the earlier window, so it is
absent from its intersection.  It is present throughout the later window,
because it is not toggled again in the combined neighbourhood, so it belongs
to the later intersection.  Thus the lower shadows differ.  Dually, the
coordinate removed on edge `u` belongs to the union of the earlier window
and is absent throughout the later window, so the upper shadows differ. ∎

### Lemma 1.3 -- exact local run criterion

Assume the two retained old pieces are already `H`-separated and distinct
new seams are more than `H` transitions apart.  At one seam, let `sigma` be
the new transition label, and let `alpha_i`, respectively `beta_j`, be the
labels of the `i`-th transition before, respectively `j`-th transition
after, the seam.  The merged word is `H`-separated at this seam if and only
if

\[
 \sigma\cap\alpha_i=\sigma\cap\beta_i=\varnothing
 \quad(1\le i\le H),
\tag{1.4}
\]

and

\[
 \alpha_i\cap\beta_j=\varnothing
 \quad\text{whenever }i+j\le H.
\tag{1.5}
\]

#### Proof

Every pair of transitions at distance at most `H` is either wholly inside
one retained old piece, contains the seam edge, or straddles the seam.  The
old-piece premise handles the first class, (1.4) handles the second, and
(1.5) handles the third.  The same classification proves necessity. ∎

The `H`-seam condition used below is deliberately stronger than
(1.4)--(1.5): it also supplies the crossing-window injectivity of Lemma 1.2.

---

## 2. The exact two-cycle splice ledger

Take two vertex-disjoint oriented Johnson cycles belonging to a packing
whose lower and upper shadow colours are globally distinct through depth
`H`.  On the first choose the
directed edge

\[
 e=(A,A'),
\]

and on the second choose

\[
 f=(B,B').
\]

Deleting `e,f` and adding

\[
 (A,B'),\qquad (B,A')
\tag{2.1}
\]

merges the two cycles if and only if

\[
 |A\mathbin\triangle B'|=|B\mathbin\triangle A'|=2.
\tag{2.2}
\]

This is the exact set-theoretic switchability criterion; the orientation of
the second cycle is chosen so that its retained segment runs from `B'` to
`B`.

### Proposition 2.0 -- complete local form of a switch

Put

\[
 A'=A-a+b,qquad B'=A-c+d,
\tag{2.2a}
\]

where `a,c in A` and `b,d notin A`.  The four middle vertices are assumed
distinct.  Every solution `B` of (2.2) is one of the following.

1. If `a!=c` and `b!=d`, put `K=A-{a,c}`.  Then

   \[
   B\in\{K+b+d,\ K+c+d,\ K+a+b\}.
   \tag{2.2b}
   \]

   The first choice is the induced rectangular switch of Section 3.  The
   other two choices give a four-cycle with a Johnson chord.
2. If `a=c` and `b!=d`, then `A'=A-a+b` and `B'=A-a+d` are adjacent with
   common lower facet `A-a`.  Their common neighbours are the union of the
   lower clique on that facet and the upper clique inside
   `(A-a)+b+d`.
3. If `a!=c` and `b=d`, the dual statement holds: `A',B'` lie in a common
   upper clique, and their common neighbours are the union of that upper
   clique and the corresponding lower clique.

If the two old lower colours are distinct and the two old upper colours are
distinct, the clique choice which repeats an old colour is excluded in
items 2--3.  In every remaining nonrectangular case, exactly one new lower
colour equals a destroyed old lower colour and exactly one new upper colour
equals a destroyed old upper colour.  The other new colour on each side is
genuinely new.  In the rectangular case, all two new colours on each side
are genuinely new.

#### Proof

The vertices `A'` and `B'` are at Johnson distance one or two.  In the
distance-two case their intersection is `K` and their symmetric difference
is the four-set `{a,b,c,d}`.  A common middle-rank neighbour must select one
element from each of the two opposite difference pairs; besides `A`, the
three possibilities are exactly (2.2b).

In the distance-one case, the common neighbours of two adjacent Johnson
vertices are precisely the lower clique on their intersection together with
the upper clique inside their union.  This gives items 2--3.  Substitution
in the four edge intersections and unions gives the final colour statement.
For example, the two chorded choices in (2.2b) reuse one of the two old
intersections and one of the two old unions, while the rectangular choice
gives the four distinct colours displayed in (3.4)--(3.5).  The adjacent
case is identical after interchanging lower and upper. ∎

### Corollary 2.1 -- every rainbow splice moves holes

If the old pair is two-sided rainbow at depth one, every colour-safe
two-cycle switch requires at least one current rank-`(m-1)` hole and at
least one current rank-`(m+1)` hole.  A rectangular switch requires two of
each.

Thus a switch does not create or destroy the depth-one defect; it moves at
least one hole on each side.  This is true even for the chorded switches
not counted by the rectangular ambient graph below.

Fix `1<=q<=H`.  On the two old cycles, exactly `q` cyclic depth-`q` windows
cross `e` and exactly `q` cross `f`.  Let

\[
 \mathcal O_q^-,\ \mathcal O_q^+
\]

be these `2q` old lower and upper colours.  After the switch, let

\[
 \mathcal N_q^-,\ \mathcal N_q^+
\]

be the `2q` new lower and upper shadows crossing the two new edges.  Let
`R_q^-` and `R_q^+` be all retained colours of the full cycle packing, and
let

\[
 \mathcal H_q^\pm
 =\binom{[2m]}{m\pm q}\setminus
   (R_q^\pm\sqcup\mathcal O_q^\pm)
\tag{2.3}
\]

be the old holes.

### Theorem 2.1 -- multidepth-safe splice and exact colour criterion

Assume both old cycles have length greater than `2H`.  The switch (2.1)
merges them into a cycle which

* has all lower and upper shadows through depth `H` of the correct rank;
* has no internal coordinate zero-run or one-run of length at most `H`; and
* remains globally rainbow at every signed depth `q<=H`

if the following two conditions hold.

1. The new transition word is `H`-separated and both new edges satisfy the
   `H`-seam condition.
2. For every `q<=H`, each of `mathcal N_q^-` and `mathcal N_q^+` has size
   `2q` and

   \[
   \mathcal N_q^\pm\cap R_q^\pm=\varnothing.
   \tag{2.4}
   \]

Condition (2.4) is equivalently

\[
 \mathcal N_q^\pm
 \subseteq \mathcal H_q^\pm\cup\mathcal O_q^\pm.
\tag{2.5}
\]

The number of used colours, and hence the number of holes, is unchanged at
every signed depth.

Conversely, among splices whose new shadows have the correct ranks and are
internally distinct, preservation of global rainbowness is equivalent to
(2.4).

#### Proof

Only windows crossing one of the two deleted edges can change.  All other
windows and colours form `R_q^\pm`.  By Lemma 1.1, `H`-separation gives the
correct ranks and excludes short runs.  The `H`-seam condition and Lemma
1.2 give distinct new windows at each individual seam; the explicit
cardinality premise also excludes a collision between the two seams.  Thus
(2.4) is precisely the condition
that no new colour collides with a retained colour.  Since `2q` old colours
are removed and `2q` new colours are inserted on each side, the used-colour
and hole counts are invariant.  The converse follows by reading the same
ledger backwards. ∎

This theorem is stable under iteration: after each splice, recompute the
two local transition neighbourhoods and the current hole sets, and apply
the same criterion.

---

## 3. Rectangular switches and the depth-one hole obstruction

There is a particularly numerous induced-square subclass of (2.2).  Write
one old edge as

\[
 A=L\cup\{a\},\qquad A'=L\cup\{b\},
\tag{3.1}
\]

where `|L|=m-1` and `a,b` lie outside `L`.  Choose

\[
 c\in L,qquad d\notin L\cup\{a,b\},
\tag{3.2}
\]

and put

\[
 L'=L-\{c\}+\{d\},
\qquad
 B=L'\cup\{b\},\qquad B'=L'\cup\{a\}.
\tag{3.3}
\]

The old edges `(A,A')`, `(B,B')` and the cross edges `(A,B')`, `(B,A')`
form an induced Johnson four-cycle.  Call this a **rectangular switch**.

The old depth-one colours are

\[
 \begin{array}{c|c|c}
 &\text{lower}&\text{upper}\\ \hline
 e&L&L\cup\{a,b\}\\
 f&L-c+d&(L-c+d)\cup\{a,b\},
 \end{array}
\tag{3.4}
\]

whereas the new colours are

\[
 \begin{array}{c|c|c}
 &\text{lower}&\text{upper}\\ \hline
 (A,B')&L-c+a&L\cup\{a,d\}\\
 (B,A')&L-c+b&L\cup\{b,d\}.
 \end{array}
\tag{3.5}
\]

All four lower colours in (3.4)--(3.5) are distinct, and all four upper
colours are distinct.

### Corollary 3.1 -- four compulsory holes for a rectangular splice

In a globally two-sided-rainbow packing, a rectangular switch can be colour
safe at depth one only if

\[
 L-c+a,\ L-c+b\in\mathcal H_1^-,
 \qquad
 L+a+d,\ L+b+d\in\mathcal H_1^+.
\tag{3.6}
\]

Thus none of the two new lower or two new upper colours can be paid for by
one of the colours destroyed by the switch.

For a fixed used edge `e=(L,{a,b})`, define

\[
 \begin{aligned}
 C_e&=\{c\in L:L-c+a,L-c+b\in\mathcal H_1^-\},\\
 D_e&=\{d\notin L\cup\{a,b\}:L+a+d,L+b+d\in\mathcal H_1^+\}.
 \end{aligned}
\tag{3.7}
\]

If the middle cycles are vertex-disjoint, the number of depth-one-safe
rectangular switch incidences at `e` is at most

\[
 |C_e|\,|D_e|.
\tag{3.8}
\]

Indeed, `(c,d)` determines the opposite Johnson edge (3.3), and a
vertex-disjoint cycle packing contains that edge at most once.

Equation (3.8) is a genuine local obstruction.  A scalar bound on the
number of holes does not ensure either `C_e` or `D_e` is nonempty.  For
example, the Johnson graph on rank-`(m-1)` sets has an independent set of
size `Omega(N_1/m)`: label the `2m` coordinates by distinct residues modulo
a prime `p` with `2m<p<4m`, colour a set by the sum of its labels modulo
`p`, and take a largest colour class.  Adjacent sets receive different
colours.  A lower-hole family of that exponential size contains no adjacent
pair at all and hence makes every `C_e` empty.

Therefore an estimate on the *number* of uncovered colours cannot by itself
give a positive local safe-switch degree.  It is compatible with a fixed
used edge having `C_e=0` or `D_e=0`; and at deficits of order `N_1/m`, the
independent-set example makes every `C_e` zero simultaneously.  To obtain a
large switch forest from the particular strip matching, one needs a
paired-hole distribution theorem or a hole-moving absorber.

---

## 4. The ambient rectangular-switch multigraph is dense

Let `mathfrak C_(m,ell)` be the complete family of cyclic-strip middle
cycles

\[
 T_t=C\cup I_\gamma(t,\ell)
\]

from Section 2 of `RAINBOW_MULTIDEPTH_STRIP_MATCHING_20260724.md`.  Assume
`ell>=3`.

The number of such cycles is

\[
 |\mathfrak C_{m,\ell}|
 =\frac{(2m)!}{4\ell\,(m-\ell)!^2}.
\tag{4.1}
\]

Every fixed Johnson edge lies in exactly

\[
 D_E
 =\left(\frac{(m-1)!}{(m-\ell)!}\right)^2
\tag{4.2}
\]

members of `mathfrak C_(m,ell)`.  This follows by double-counting
cycle-edge incidences, since a cycle has `2ell` edges and `J(2m,m)` has
`Wm^2/2` edges.

Define an **ambient** multigraph on `mathfrak C_(m,ell)` by putting one
incidence between two cycles for every rectangularly switchable pair of one
edge from each.  At this stage the two cycles are allowed to meet at other
middle vertices; the vertex-disjoint subgraph is treated in Theorem 5.2.

### Theorem 4.1 -- exact ambient degree and multiplicity

The rectangular-switch incidence multigraph is regular of degree

\[
 \boxed{
 \Delta_\square
 =2\ell(m-1)^2D_E.}
\tag{4.3}
\]

It has no loops, and two fixed cycles support at most

\[
 \boxed{4\ell}
\tag{4.4}
\]

parallel switch incidences.

#### Proof

Fix a cycle and one of its `2ell` edges `(L,{a,b})`.  Formula (3.2) gives
exactly `(m-1)^2` opposite Johnson edges.  Each is contained in `D_E` strip
cycles, proving (4.3).

A strip cycle uses each of its `ell` antipodal coordinate pairs on exactly
two opposite Johnson edges.  The other edge in the same cycle with exchange
pair `{a,b}` has lower colour at Johnson distance `ell-1` from `L`; since
`ell>=3`, it is not one of (3.3).  Hence there are no loops.

Two cycles share at most `ell` antipodal coordinate pairs.  For each shared
pair there are at most two choices of an edge in either cycle, hence at most
four incidences.  This gives (4.4). ∎

The dense degree (4.3) concerns geometric switchability in the complete
strip family.  It concerns neither colour safety inside one selected
matching nor, yet, vertex-disjointness of the partner cycles.

---

## 5. Almost every ambient rectangular switch is run-safe

For an edge `e` in a strip cycle `Gamma`, let

\[
 \Lambda_H(\Gamma,e)
\]

be the set of coordinates occurring in transition labels of the `H` edges
immediately before or after `e`, excluding `e` itself.

Assume

\[
 \ell>2H.
\tag{5.1}
\]

Then these `2H` neighbouring strip edges have pairwise disjoint labels, and

\[
 |\Lambda_H(\Gamma,e)|=4H.
\tag{5.2}
\]

Call a rectangular incidence **strongly `H`-run-safe** if

* its new exchange pair `{c,d}` avoids both old neighbourhoods; and
* the two old neighbourhood label sets are disjoint.

This condition is stronger than necessary, but it gives the `H`-seam
condition at both new edges and makes the new transition word
`H`-separated.

### Theorem 5.1 -- run-safe minimum degree

Uniformly for `H^2=o(m)` and `ell>2H`, every vertex of the ambient switch
multigraph has at least

\[
 \boxed{
 \left(1-O\!\left(\frac{H^2}{m}\right)\right)
 \Delta_\square}
\tag{5.3}
\]

strongly `H`-run-safe incidences.  The maximum parallel multiplicity remains
at most `4ell`.

#### Proof

Fix `Gamma,e=(L,{a,b})`.  First choose `(c,d)` as in (3.2).  At most `4H`
members of either choice class occur in `Lambda_H(Gamma,e)`, so the fraction
of pairs rejected at this stage is at most

\[
 \frac{8H}{m-1}.
\tag{5.4}
\]

Fix a surviving opposite edge `f`.  Choose uniformly one of the `D_E` strip
cycles through `f`.  The stabilizer of `f` is transitive on the `m-1`
members of its lower colour and separately on the `m-1` coordinates outside
its upper colour.  In the two-sided `H`-neighbourhood of `f`, exactly `2H`
coordinates come from each class.  Hence any fixed eligible coordinate is
present with probability `2H/(m-1)`.

The forbidden set `Lambda_H(Gamma,e) union {c,d}` has at most `4H+2`
coordinates.  A union bound therefore rejects at most

\[
 \frac{(4H+2)2H}{m-1}
 =O\!\left(\frac{H^2}{m}\right)
\tag{5.5}
\]

of the `D_E` cycles through `f`.  Combining (5.4)--(5.5) proves (5.3).
The multiplicity bound is inherited from Theorem 4.1. ∎

Theorem 5.1 is still ambient: its partner cycle can meet the fixed cycle
away from the switched edges.  The following estimate removes those
incidences.

### Theorem 5.2 -- vertex-disjoint run-safe degree

If

\[
 H^2+\ell^2=o(m),\qquad \ell>2H,
\tag{5.6}
\]

then every strip cycle has at least

\[
 \boxed{
 \left(1-O\!\left(\frac{H^2+\ell^2}{m}\right)\right)
 \Delta_\square}
\tag{5.7}
\]

strongly `H`-run-safe incidences whose partner cycle is vertex-disjoint
from it.

#### Proof

Fix an opposite Johnson edge

\[
 f=\{L+a,L+b\},
\]

and put

\[
 O=[2m]\setminus(L\cup\{a,b\}).
\]

The stabilizer of `f` is

\[
 (\mathfrak S_L\times\mathfrak S_O)\rtimes\langle(a\ b)\rangle.
\]

Every orbit of this stabilizer on middle sets, other than the endpoint orbit
`{L+a,L+b}` and its complementary orbit `{O+a,O+b}`, has size at least
`m-1`: its size is a product of binomial coefficients from the two
`(m-1)`-element classes, with a possible factor two.

For a middle set `X` in such an orbit `\mathcal O`, double counting cycles
through `f` and their vertices in `\mathcal O` gives

\[
 |\mathcal O|\,c_f(X)
 \le 2\ell D_E.
\]

Hence a uniformly chosen strip cycle through `f` contains `X` with
probability at most `2\ell/(m-1)`.

Under the strong run-safety condition, neither endpoint of `f` lies in the
fixed cycle: such an endpoint is adjacent to a switched endpoint and, in a
cyclic-interval Johnson cycle, would have to be its other cycle neighbour,
putting the new label `{c,d}` in the first forbidden transition
neighbourhood.  A complementary endpoint cannot occur in a strip cycle
through `f`, since that cycle has a nonempty core contained in every one of
its vertices.  A union bound over the `2ell` vertices of the fixed cycle
therefore rejects at most

\[
 \frac{4\ell^2}{m-1}
\tag{5.8}
\]

of the cycles through `f`.  Combining (5.8) with Theorem 5.1 proves (5.7).
∎

Every incidence counted in (5.7) genuinely merges two vertex-disjoint
cycles, creates no coordinate zero-run or one-run of length at most `H`,
and gives correct-rank new depth-`q` shadows.  The crossing depth-`q`
windows at either individual seam are injective.  It need not be globally
rainbow: the hole conditions (2.4), already nontrivial in (3.6), remain
indispensable.

---

## 6. Exact saving from a safe splice forest

Suppose a strip matching supplies `p` globally multidepth-rainbow cycles,
and perform `s` successive splices satisfying Theorem 2.1, always between
distinct current components.  The result has `p-s` cycles, the same total
number of used colours at every signed depth, and no short runs.

Cut one edge of each remaining cycle.  At depth `q`, exactly `q(p-s)` lower
and `q(p-s)` upper cyclic windows are lost.  Therefore the independent-cut
term

\[
 pH(H+1)
\]

is replaced exactly by

\[
 (p-s)H(H+1).
\tag{6.1}
\]

Including the endpoint-capped erosion overhead, the gate charge becomes

\[
 U_m+(p-s)(H^2+2H),
\tag{6.2}
\]

where `U_m` is the original unmatched band-vertex count.

Thus it is enough to find a state-dependent colour-safe switch forest with

\[
 p-s=o(W/H^2).
\tag{6.3}
\]

Equivalently, relative to a hypothetical single final cycle, every merge
which is attempted but cannot be made colour safe leaves one extra final
component and has the exact terminal charge

\[
 \boxed{H^2+2H.}
\tag{6.4}
\]

More generally, after `r` rejected merges which are not replaced by other
accepted forest edges, the excess independent-cut charge is exactly
`r(H^2+2H)`.  There is no hidden factorability surcharge: this is the sum of
the endpoint cap `H` and the two lost-window sums
`2(1+...+H)`.

### Theorem 6.1 -- exact soft-splice collision charge

Perfect colour safety is sufficient but not necessary for improving the
erosion ledger.  Consider one geometrically safe merge in an arbitrary
current state.  Let `R_q^pm` be the set of distinct colours of all windows
not crossing the two deleted edges, `O_q^pm` the set of distinct colours of
the old crossing windows, and `N_q^pm` the set of distinct colours of the
new crossing windows.  No disjointness is assumed.  Define

\[
 \kappa_q^\pm
 =|R_q^\pm\cup\mathcal O_q^\pm|
  -|R_q^\pm\cup\mathcal N_q^\pm|.
\tag{6.5}
\]

Thus `kappa_q^pm` is the exact increase in the missing-colour count; it can
be negative if the splice gains distinct colours.  When the current state
is globally rainbow, it reduces to

\[
 \kappa_q^\pm
 =2q-|\mathcal N_q^\pm\setminus R_q^\pm|.
\tag{6.5a}
\]

The exact change in the standard conservative
endpoint-capped ledger (which charges `q` lost windows per signed depth and
final component) is

\[
 \boxed{
 \Delta G
 =\sum_{q=1}^{H}(\kappa_q^-+\kappa_q^+)
  -(H^2+2H).}
\tag{6.6}
\]

In particular, the splice is non-worsening whenever

\[
 \sum_{q=1}^{H}(\kappa_q^-+\kappa_q^+)
 \le H^2+2H.
\tag{6.7}
\]

#### Proof

Before the switch the distinct cyclic colours at signed depth `q` are
`R_q^pm union O_q^pm`; afterwards they are
`R_q^pm union N_q^pm`.  Hence the cyclic missing count increases by exactly
`kappa_q^pm`, with no rainbowness premise.  Merging
two components reduces the later path cut loss by

\[
 2\sum_{q=1}^{H}q=H(H+1)
\]

and reduces the endpoint-cap term by `H`.  Subtracting these savings gives
(6.6). ∎

Formula (6.6) also supplies an exact charge for a rejected splice.  Rejecting
it leaves the full `H^2+2H` component charge; accepting it replaces that
charge by its state-dependent collision loss.  Therefore a useful switch
forest may be sought under a total collision budget, rather than under the
strong zero-collision condition (2.4).  Because (6.5) is the difference of
the actual distinct-colour counts before and after each switch, these
charges telescope under an arbitrary sequence of accepted splices.

Theorems 4.1, 5.1, and 5.2 show that geometric and run constraints do not
prevent such a forest in the current regime
`H^2+ell^2=o(m)`.  Corollary 3.1 shows precisely why the
current ABKV strip matching does not yet provide it: its scalar defect
ledger contains no paired-hole or hole-transport information.

---

## 7. Resulting research gate

The safe-splicing problem is reduced to the following finite exchange
statement.

> **Paired-hole switch-forest lemma.**  Choose the near-perfect strip
> matching, or modify it with an absorber, so that the state-dependent graph
> of switches satisfying (2.4) contains a forest which merges all but
> `o(W/H^2)` cycle components.

An initially dense *geometric* switch graph is already proved above.  What
is missing is either

1. a distribution theorem giving the paired holes in (3.6) and their
   multidepth analogues, or
2. an absorber which moves the current holes along the exchange graph while
   successively merging components.

This is strictly narrower than asking for a new OR factor or a new shadow
matching: factorability follows from the endpoint-capped erosion word once
the colour-safe switch forest is constructed.

---

## 8. Chorded switches are four-state hole rotors

Every nonrectangular one-hole switch in Proposition 2.0, including the
apparently adjacent-clique cases after reparametrization, consumes one lower
and one upper hole.  Its ambient transport graph can be classified exactly.

Let `mathcal X` be the set of compatible signed hole pairs `(F,G)` with

\[
 |F|=m-1,\qquad |G|=m+1,
 \qquad |F\cap G|=m-2.
\tag{8.1}
\]

For such a pair put

\[
 K=F\cap G,qquad S=F\cup G.
\tag{8.2}
\]

Then `|S|=m+2`, and there is a unique four-set

\[
 Q=S\setminus K
\]

and a unique `x in Q` such that

\[
 (F,G)=(K+x,\ K+(Q\setminus\{x\})).
\tag{8.3}
\]

Join two vertices of `mathcal X` when one nonrectangular one-hole switch
moves the first hole pair to the second, without imposing membership in a
particular selected cycle packing.

### Theorem 8.1 -- ambient chorded transport components

The ambient chorded hole-pair graph is the disjoint union

\[
 \boxed{
 \binom{2m}{m-2}\binom{m+2}{4}
 \text{ copies of }K_4.}
\tag{8.4}
\]

The component indexed by `(K,Q)` consists of

\[
 v_x=(K+x,\ K+(Q\setminus\{x\})),
 \qquad x\in Q.
\tag{8.5}
\]

It has degree `3`, diameter `1`, and every one of its six graph edges has
exactly two chorded Johnson-four-cycle witnesses.

#### Proof

Write `Q={a,b,c,d}`.  The chorded switch already computed in Proposition
2.0 has the hole transport

\[
 (K+a,\ K+b+c+d)
 \longmapsto
 (K+d,\ K+a+b+c).
\tag{8.6}
\]

Thus it changes the distinguished element of `Q` from `a` to `d`, while
fixing both `K` and `S=K+Q`.  Conversely, for any two distinct `a,d in Q`,
choose one of the two remaining elements, say `c`, as the reused lower
colour.  The old middle edges are

\[
 (K+a+c,\ K+b+c),
 \qquad
 (K+c+d,\ K+a+d),
\tag{8.7}
\]

where `b` is the fourth element.  Replacing them by the cross edges consumes
the two holes on the left of (8.6) and leaves the two holes on the right.
Choosing `b` rather than `c` as the reused lower colour gives the second
witness.  These are the only choices, by the distance-two list (2.2b).
The adjacent-clique descriptions in items 2--3 of Proposition 2.0 become
one of these same two witnesses after taking `K=F intersect G` and
`Q=(F union G) setminus K`; they do not add a third transport edge or
change the fiber.

Hence every pair `v_a,v_d` in one `(K,Q)` fiber is adjacent, with witness
multiplicity two.  A chorded move preserves `K=F intersect G` and
`S=F union G`, so no edge joins different fibers.  Finally, (8.2)--(8.3)
recover `(K,Q,x)` uniquely from `(F,G)`, proving both the component count
and all asserted graph parameters. ∎

### Corollary 8.2 -- chorded transport alone is not global routing

Repeated chorded distance-two switches can rotate a compatible hole pair
among four states, but cannot change either its intersection `K` or its
union `S`.  In particular, their ambient graph has no component larger than
four, regardless of `m`.

This is a local obstruction, not a nonexistence theorem for safe splicing.
Rectangular two-hole moves change the fiber invariants, and longer absorbers
may do so as well.

### 8.1 Ambient witnesses versus selected-cycle liftability

Theorem 8.1 is an ambient Johnson-graph statement.  To realize the move
`v_a -> v_d` inside the selected cyclic-strip packing, at least one of the
two witnesses (8.7) must satisfy all of the following additional conditions.

1. Its two old Johnson edges must occur in two distinct current cycle
   components, with the required pairing of their four middle vertices.
2. The two new cross edges must satisfy the `H`-seam condition, or the
   weaker geometric conditions being charged in Theorem 6.1.
3. At every depth `2<=q<=H`, its new crossing shadows must obey the desired
   hole/collision budget.

Even exact middle ownership does not imply item 1: it owns vertices, not
the two prescribed edge pairings.  The dense ambient strip-switch estimate
of Theorem 5.1 does not imply it either, because it averages over all strip
cycles through an opposite edge rather than the cycles retained by the
matching.

Consequently the chorded move reduces paired-hole routing to a concrete
**lift problem**: choose the strip matching so that enough of the two ambient
witnesses per `K_4` edge survive as cross-component, multidepth-geometric
switches.  Without that lift, the `K_4` rotor classification by itself does
not merge any selected components.

---

## 9. Cut first: the exact boundary-signature circulation

A one-edge splice of two already cut paths is less restrictive than a
two-cycle switch.  It adds one seam and removes no existing path window.
The resulting boundary ledger has a natural directed-circulation form.

Let the `Gamma_i` be pairwise vertex-disjoint, `H`-run-valid oriented cycles
whose shadow colours are jointly globally rainbow through depth `H`.  Cut `Gamma_i`
between its tail vertex `T^i_{-1}` and head vertex `T^i_0`.  Indices before
`0` are read cyclically on the old cycle.  At depth `q`, define the lower
and upper cut signatures

\[
 \begin{aligned}
 \mathcal B_{i,q}^-
 &=\left\{
   \bigcap_{t=-r}^{q-r}T^i_t:1\le r\le q
   \right\},\\
 \mathcal B_{i,q}^+
 &=\left\{
   \bigcup_{t=-r}^{q-r}T^i_t:1\le r\le q
   \right\}.
 \end{aligned}
\tag{9.1}
\]

These are exactly the `q` lower and `q` upper cyclic colours lost by cutting
`Gamma_i`.

For two cut paths `i,j`, suppose the tail `T^i_{-1}` is Johnson-adjacent to
the head `T^j_0`.  Concatenating `i` to `j` creates the cross signatures

\[
 \begin{aligned}
 \mathcal X_{ij,q}^-
 &=\left\{
   \left(\bigcap_{t=-r}^{-1}T^i_t\right)
   \cap
   \left(\bigcap_{t=0}^{q-r}T^j_t\right)
   :1\le r\le q
   \right\},\\
 \mathcal X_{ij,q}^+
 &=\left\{
   \left(\bigcup_{t=-r}^{-1}T^i_t\right)
   \cup
   \left(\bigcup_{t=0}^{q-r}T^j_t\right)
   :1\le r\le q
   \right\}.
 \end{aligned}
\tag{9.2}
\]

Call the arc `i->j` **signature compatible through depth `H`** when it is
geometrically `H`-seam safe and

\[
 \boxed{
 \mathcal X_{ij,q}^-=\mathcal B_{i,q}^-,
 \qquad
 \mathcal X_{ij,q}^+=\mathcal B_{j,q}^+
 \quad(1\le q\le H).}
\tag{9.3}

Thus an arc consumes the lower boundary signature of its source and the
upper boundary signature of its target.

### Theorem 9.1 -- boundary-signature path-forest theorem

Assume every retained cut path has more than `2H` transitions, as in the
cyclic-strip application.  Let `F` be an acyclic directed graph on the `p`
cut cycles, with indegree and outdegree at most one, all of whose arcs
satisfy (9.3).  Concatenating along the arcs of `F` produces
`c=p-|E(F)|` vertex-disjoint Johnson paths which

* remain `H`-run-valid;
* retain global lower- and upper-shadow uniqueness through depth `H`; and
* have, at every depth `q`, exactly `cq` unfilled lower cut colours and
  `cq` unfilled upper cut colours, in addition to the holes already present
  before the cycles were cut.

Consequently, if `U_m` is the original cyclic-band defect, their
endpoint-capped erosion ledger is

\[
 \boxed{U_m+c(H^2+2H).}
\tag{9.4}
\]

#### Proof

The directed degree and acyclicity conditions make `F` a path forest, so
the concatenations are well-defined and leave `c` components.  Because
every retained old path has more than `2H` transitions, any block of at
most `H` transitions meets at most one installed seam.  Such a block either
lies in an old cut path or is governed by the geometric seam condition.
Thus the several seam checks do not interact, and they preserve run
validity and the correct shadow ranks.

Before any joins, the families `mathcal B_(i,q)^pm` are pairwise disjoint
holes, because the old cycles were globally rainbow.  By (9.3), every
outgoing arc from `i` fills precisely `mathcal B_(i,q)^-`, and every incoming
arc to `j` fills precisely `mathcal B_(j,q)^+`.  Outdegree and indegree at
most one prevent repeated use.  A directed path component has exactly one
sink, whose lower signature remains unfilled, and one source, whose upper
signature remains unfilled.  This proves the `cq` count on either side.

There are `c` endpoint caps, costing `cH`, and

\[
 2c\sum_{q=1}^{H}q=cH(H+1)
\]

unfilled signed boundary colours.  Their sum is (9.4). ∎

In particular, a directed Hamilton path reduces the old `p(H^2+2H)` cut
charge to only `H^2+2H`.  A directed cycle of compatible arcs is equally
useful after deleting any one of its arcs.

### Proposition 9.2 -- exact depth-one mixed-flag arc

Let the cut edge of component `i` have lower and upper colours

\[
 L_i=T^i_{-1}\cap T^i_0,
 \qquad
 U_i=T^i_{-1}\cup T^i_0.
\]

Then the depth-one part of (9.3) for an arc `i->j` is equivalent to

\[
 \boxed{
 T^i_{-1}\cap T^j_0=L_i,
 \qquad
 T^i_{-1}\cup T^j_0=U_j.}
\tag{9.5}

Equivalently, `L_i subset U_j` and the tail of `i` and head of `j` are the
two distinct middle sets in the interval `[L_i,U_j]` selected by the cross
edge.  The arc owns the mixed flag `(L_i,U_j)`.

Thus an internal component of the directed forest uses its upper cut colour
on its incoming arc and its lower cut colour on its outgoing arc.  This is
the exact endpoint-neutral circulation law at depth one.

### Proposition 9.3 -- ambient mixed-flag arc degree

Fix an oriented cut occurrence in a strip cycle, written

\[
 T_{-1}=L+a,\qquad T_0=L+b.
\tag{9.5a}
\]

There are exactly

\[
 \boxed{(m-1)^2D_E}
\tag{9.5b}
\]

ambient oriented strip-cut occurrences `j` whose endpoints are distinct
from both endpoints in (9.5a) and whose cross edge from `T_{-1}` to
`T^j_0` owns the mixed flag `(L,U_j)`.

Indeed, choose

\[
 d\notin L\cup\{a,b\},\qquad c\in L,
\]

and set

\[
 U_j=L+a+d,qquad
 T^j_0=L+d,qquad
 T^j_{-1}=L-c+a+d.
\tag{9.5c}
\]

There are `(m-1)^2` choices, and the target Johnson edge lies in `D_E`
strip cycles.  Conversely, (9.5) forces (9.5c).

When `ell>2H` and `H^2+ell^2=o(m)`, the same neighbourhood and stabilizer
estimates as in Theorems 5.1--5.2 leave

\[
 \left(1-O\!\left(\frac{H^2+\ell^2}{m}\right)\right)
 (m-1)^2D_E
\tag{9.5d}
\]

geometrically `H`-seam-safe, vertex-disjoint ambient arcs.  This remains an
ambient occurrence count: the particular strip matching may retain none of
those partner cycles, and (9.5d) says nothing about (9.3) at depths `q>=2`.

### Theorem 9.4 -- soft boundary-splice ledger

Signature equality is again stronger than necessary.  In an arbitrary
current path family, let `R_q^pm` be its set of distinct signed depth-`q`
colours, and let a geometrically valid arc `i->j` between two distinct
current components add the cross-signature set `X_(ij,q)^pm`.  Adding the
arc deletes no old window.  Therefore the exact change in the
endpoint-capped ledger is

\[
 \boxed{
 \Delta G
 =-H-
  \sum_{q=1}^{H}
  \left(
   |\mathcal X_{ij,q}^-\setminus R_q^-|
   +|\mathcal X_{ij,q}^+\setminus R_q^+|
  \right).}
\tag{9.6}
\]

In particular, every geometrically valid one-edge path splice is
non-worsening and saves at least the endpoint cap `H`; it saves the full
`H^2+2H` exactly when it fills `q` new colours on each side at every depth.
The formula telescopes under successive path splices when the current colour
sets are updated after every arc.

#### Proof

The component count drops by one, saving `H`.  At signed depth `q`, the
missing count drops by exactly the number of genuinely new distinct colours
in the cross signature, namely the corresponding set difference in (9.6).
Nothing is removed.  Summing gives the formula. ∎

The remaining multidepth construction can therefore be phrased more
economically than a two-cycle switch forest:

> Find a long directed path forest in the boundary graph whose arc `i->j`
> is the one-edge endpoint splice (9.2), maximizing the total number of new
> signed shadow colours.  Exact signature-compatible arcs (9.3) are ideal,
> but the soft objective (9.6) is sufficient.

At depth one this is a mixed lower/upper flag circulation.  At greater
depths, (9.3) is the precise lift condition; no separate factorability or
pin-survival premise remains once the resulting paths satisfy the erosion
run condition.
