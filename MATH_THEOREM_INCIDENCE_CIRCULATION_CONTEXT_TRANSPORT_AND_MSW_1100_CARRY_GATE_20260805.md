# Incidence circulations transport across one Johnson context move

**Date:** 2026-08-05  
**Method:** exact signed incidence-chain identity; no computation  
**Status:** unconditional in the Boolean incidence-cycle lattice.  It gives
a uniform constant-size algebraic carry for the frozen two-hex MSW relay
across one `1100` renewal block.  Literal alternation, q2-halo closure, and
the component effect require one additional prepared-prism hypothesis and
are not claimed unconditionally.

## 0. Outcome

Let `Z` be any signed, degree-zero circulation in the Boolean incidence
graph between rank-`r` owners and rank-`(r+1)` colours.  Put the whole
circulation in a disjoint common context `S`.  If one Johnson move changes
the context

\[
                         S\longmapsto S-a+b,                       \tag{0.1}
\]

then the difference between the two contextual copies of `Z` is an exact
sum of incidence hexagons.  There is one transport hexagon for each signed
incidence in `Z`; all auxiliary rails cancel solely because `Z` has zero
boundary at every owner and every colour.

The frozen `T_0` repair relay consists of two incidence hexagons and twelve
distinct toggled incidences.  Therefore:

* one context exchange transports it using twelve hexagons;
* the two context exchanges of the canonical `1100 -> 1001 -> 0011`
  geodesic transport it using twenty-four hexagons.

For concatenated Dyck roots, the canonical MSW path presents a suffix
packet only after every prefix exchange has occurred.  Thus a packet on a
base word `X` appears naturally with the **down-set** `0011` of a preceding
`1100` block, whereas a repair of the positive-prefix obstruction needs the
**up-set** `1100`.  The identity in this note is the exact algebraic
conjugacy between those two placements.

This closes the cycle-lattice part of the proposed one-unit counter carry.
The remaining physical theorem is sharply isolated:

> Prepare the transport prism so that its hexagons can be swept in an
> alternating order, its two q2 halos cancel without losing an old target,
> and its auxiliary rails have the same component effect as conjugating the
> original relay.

Without that prepared-prism theorem, the chain identity alone is not a
valid rethreading of the canonical factor.

## 1. Boolean incidence notation

Let `B(Omega;r,r+1)` be the bipartite incidence graph whose left vertices
are rank-`r` owners and whose right vertices are rank-`(r+1)` colours.  Give
every edge the orientation owner-to-colour.

A signed incidence chain is

\[
                         Z=\sum_{e}\epsilon_e e,
 \qquad \epsilon_e\in\mathbb Z.                                  \tag{1.1}
\]

It is a circulation when its signed degree is zero at every owner and every
colour.  The alternating vector of any incidence hexagon is a circulation.
The sum of the two hexagons in the frozen `T_0` relay is therefore a
circulation.

Let the support coordinates of `Z` be disjoint from two context labels
`a,b`.  Fix a context `S` with `a in S`, `b notin S`, and write

\[
                         S'=S-a+b.                                \tag{1.2}
\]

For a base incidence

\[
                         e=(O,Q),\qquad Q=O+x,                     \tag{1.3}
\]

write

\[
 e_S=(S\cup O,S\cup Q),\qquad
 e_{S'}=(S'\cup O,S'\cup Q).                                     \tag{1.4}
\]

All unions below are disjoint unions of the context and base coordinates.

## 2. The transport hexagon

Put

\[
                         K=(S-a)\cup O.                            \tag{2.1}

\]

The three active labels `a,b,x` give the incidence hexagon with owners

\[
                         K+a,\quad K+b,\quad K+x                  \tag{2.2}

\]

and colours

\[
                         K+ab,\quad K+ax,\quad K+bx.              \tag{2.3}

\]

Its signed alternating vector, in cyclic order, is

\[
\begin{aligned}
 H_e={}&[K+a,K+ax]-[K+x,K+ax]+[K+x,K+bx]\\
      &-[K+b,K+bx]+[K+b,K+ab]-[K+a,K+ab].                         \tag{2.4}
\end{aligned}

\]

The first edge is `e_S` and the fourth edge is `-e_(S')`.

For later cancellation, name

\[
\begin{aligned}
 f_{Q,a}&=[K+x,K+ax],& f_{Q,b}&=[K+x,K+bx],\\
 g_{O,a}&=[K+a,K+ab],& g_{O,b}&=[K+b,K+ab].                       \tag{2.5}
\end{aligned}

\]

Then (2.4) rearranges to

\[
 e_{S'}-e_S
   =-H_e+(f_{Q,b}-f_{Q,a})+(g_{O,b}-g_{O,a}).                    \tag{2.6}
\]

The important separation is exact: the `f` rail depends only on the base
colour `Q`, and the `g` rail depends only on the base owner `O`.

## 3. Context-transport theorem

### Theorem 3.1

If `Z` is a signed incidence circulation, then

\[
 \boxed{
                         Z_{S'}-Z_S
                           =-\sum_e\epsilon_e H_e.}               \tag{3.1}
\]

In particular, two contextual copies of the same circulation differ by an
integer sum of incidence hexagons.

#### Proof

Multiply (2.6) by `epsilon_e` and sum over base incidences.  The coefficient
of the rail difference `f_(Q,b)-f_(Q,a)` is

\[
                         \sum_{e\ni Q}\epsilon_e,                 \tag{3.2}

\]

which is zero because `Z` has zero signed degree at `Q`.  The coefficient
of `g_(O,b)-g_(O,a)` is similarly

\[
                         \sum_{e\ni O}\epsilon_e=0.               \tag{3.3}

\]

Every auxiliary rail cancels, leaving (3.1).  \(\square\)

### Corollary 3.2 (path transport)

Let

\[
                         S_0,S_1,\ldots,S_t                       \tag{3.4}

\]

be any Johnson path on disjoint context coordinates.  Then `Z_(S_t)-Z_(S_0)`
is a sum of exactly `t |supp Z|` signed transport hexagons before identical
hexagons or zero coefficients are coalesced.

This is obtained by applying Theorem 3.1 to every context edge and
telescoping.

## 4. The exact `1100` carry count

The canonical complementary geodesic of the Dyck root `1100` is

```text
                         1100 -> 1001 -> 0011.
```

It has two Johnson context moves.  Let `Z_0` be the signed circulation of
the frozen two-hex `T_0` relay.  Its two incidence hexagons have disjoint
edge supports, so

\[
                         |\operatorname {supp}Z_0|=12.            \tag{4.1}

\]

Corollary 3.2 gives

\[
 \boxed{
          (Z_0)_{1100}-(Z_0)_{0011}
             \text{ is a sum of at most }24
             \text{ transport hexagons}.}                        \tag{4.2}

\]

The bound is uniform: it does not depend on the ambient semilength, a Dyck
suffix, or the ordinal gap of the missing chamber.

## 5. Why this is the required counter conjugacy

For Dyck roots `W,X,V`, the MSW insertion and deletion orders concatenate.
During the `X` portion of the canonical path rooted at `W X V`, all
coordinates of `W` have already been exchanged and no coordinate of `V`
has yet been exchanged.  Consequently every owner, colour, and turn in the
`X` portion has the two-sided constant context

\[
                         D(W)\cup U(V),                            \tag{5.1}

\]

where `D(W)` is the down-step set of `W` and `U(V)` the up-step set of `V`.

For `W=1100`, the natural prefix context in (5.1) is `0011`.  The missing
renewal family of the chamber theorem instead carries the positive prefix
`1100`.  Formula (4.2) is exactly the cycle-lattice move taking the relay
from the natural late-phase context to the desired early-phase context.

Reversing (4.2) removes one `1100` counter unit; iterating it transports a
relay across an arbitrary number of low renewals without increasing word
length.  A reflected construction gives the analogous high-renewal carry.
Thus the chamber grammar requires only one uniform algebraic macro schema,
not infinitely many unrelated circulation identities.

## 6. The literal prepared-prism gate

An integer cycle identity is weaker than a sequence of valid factor
switches.  To promote (3.1) to a literal repair, one must prove all of the
following in one host:

1. **Alternating sweep.**  Plant the complementary rail phases of Lemma 6.1
   below, including the one shared-colour phase compatibility of the
   two-hex relay.
2. **Turn-faithful boundaries.**  The other selected colour at every
   affected boundary owner gives the contextual copy of the base q2 turn.
3. **Topology.**  The swept prism conjugates, rather than destroys, the
   `-4` component effect of the two-hex relay.
4. **Protection.**  The auxiliary owners and colours avoid the protected
   stem bank and every previously planted prism.

These properties do not follow from `\partial Z=0`.  A common unit suffix
bottleneck or a nonalternating face can obstruct them even though (3.1)
holds integrally.

The alternation row itself has an exact one-bit form.

### Lemma 6.1 (alternating annulus sweep)

Let `Z` be one simple alternating incidence cycle.  Assume that, before any
switch, the two contextual boundary copies `Z_S,Z_(S')` have identical edge
statuses.  First toggle `Z_S`.  For every base owner or colour `v` on the
cycle, the transport construction supplies two rail incidences, one on the
`a` side and one on the `b` side.

There is a choice of complementary rail phases--exactly one of the two rail
incidences selected at each `v`--for which the transport hexagons can then
be toggled successively around the cycle.  After the last face:

1. every rail incidence has returned to its initial status;
2. the `S` boundary has returned to its original status;
3. the `S'` boundary has been toggled by `Z_(S')`.

Thus the relay has literally moved from one boundary of the annulus to the
other.

#### Proof

For a base edge `e=(O,Q)`, let `s_e` be the status of `e_S` after `Z_S`
has been toggled.  The status of `e_(S')` is then `1-s_e`.  Reading the six
edges in (2.4), its transport hexagon is alternating exactly when

\[
\begin{array}{c|cccccc}
\text{edge}&e_S&f_{Q,a}&f_{Q,b}&e_{S'}&g_{O,b}&g_{O,a}\\ \hline
\text{status}&s_e&1-s_e&s_e&1-s_e&s_e&1-s_e.
\end{array}                                                       \tag{6.1}
\]

Choose a starting edge of the base cycle and assign the two rail phases at
its endpoints according to (6.1).  Assign the phase at each successive new
vertex according to the next edge.  Toggling the current face flips both
rails at the shared vertex.  Since edge statuses alternate around the base
cycle, this is exactly the phase required by the next face.  At the final
face, evenness of the bipartite cycle gives the required phase at the
starting vertex.  Every vertex belongs to two consecutive faces, so both of
its rails are flipped twice and restored.  The three boundary conclusions
follow directly.  \(\square\)

Every signed zero-one circulation decomposes into alternating simple
cycles.  Edge-disjoint cycles can be swept independently.  If cycles share
vertices, a completed sweep restores the shared rails; the only additional
compatibility is that the next cycle admit the already planted initial
phase at each shared vertex.  A simple alternating cycle permits either
prescribed phase at one named vertex: start with the appropriate one of its
two incident edges.  The frozen relay's two cycles share only one q1 colour,
so both sweeps can always use the same planted phase there.  No additional
Hall condition occurs in this two-cycle annulus.

### Corollary 6.2 (turn-faithful carry)

In addition to Lemma 6.1, suppose the two boundary copies are locally
turn-isomorphic: the untouched second selected colour at every affected
owner is the same contextual copy of the corresponding base colour.  Then
the final q2 signed change is exactly the common-context copy of the base
relay change at `S'`.

Consequently, if the base relay is closed--every deleted q2 target retains
another occurrence--then the carried relay is also closed.  Intermediate
annulus states need not have a complete q2 palette.

#### Proof

The annulus sweep restores every interior rail and the old boundary, so its
final incidence difference is exactly `Z_(S')`.  At an affected owner, a
q2 turn is the union of the toggled colour and its untouched selected mate.
The turn-isomorphism hypothesis therefore tensors every old and new base
turn by the common context `S'`.  The base multiplicity inequalities carry
over verbatim.  \(\square\)

This removes q2-halo control from the list of dynamic requirements: only
the two terminal boundary copies must be turn-isomorphic.  The unresolved
host theorem is now static--plant the two boundary phases, the complementary
rail bits, and the required component incidence in one protected factor.

The unchanged canonical product does not supply those phases.

### Lemma 6.3 (canonical `1100` phase failure)

Use the first canonical context move

```text
                         1100 -> 1001.
```

For a balanced base owner word `O`, the two owner-side rail incidences are
complementary--exactly one is selected by the canonical q1 factor--if and
only if

\[
                         U_{-1}(O)=1.                              \tag{6.2}
\]

Among the six owners toggled by the frozen two-hex relay, the values of
`U_(-1)` are

\[
\begin{array}{c|c}
O&U_{-1}(O)\\ \hline
101010001101&2\\
100011001101&3\\
100010001111&1\\
101011000101&2\\
101001010101&4\\
101001001101&3.
\end{array}                                                       \tag{6.3}
\]

Hence five of the six owner rails fail the complementary-phase condition.
The literal carry cannot be performed inside the unchanged canonical
product factor.

#### Proof

The q1 colour joining the two context owners has prefix `1101`; its two
context facets delete positions two and four.  For any endpoint-height-two
word `Y`, the canonical selected owner pair is obtained by taking the
`U_1(Y)`-th and `(U_1(Y)+1)`-st up-steps touching line one.  In `Y=1101O`,
the prefix touching steps have ranks one, two, and three, at positions one,
two, and four, while

\[
                         U_1(Y)=2+U_{-1}(O).                       \tag{6.4}

\]

Exactly one of ranks two and three is selected if and only if the right
side of (6.4) is three, proving (6.2).  Reading the six displayed balanced
paths gives (6.3) directly.  \(\square\)

The other possible first moves out of `1100` do not repair this particular
host.  If the added context bit is position three, the colour prefix is
`1110`; exactly one context rail can be selected only when
`U_(-1)(O)<=1`.  If the added bit is position four, the two choices require
respectively `U_(-1)(O)<=1` or `U_(-1)(O)=1`.  The five rows larger than one
in (6.3) remain obstructed.

Thus the prepared-prism theorem genuinely requires a palette-preserving
rethread of the context rails; it is not hidden in a different ordering of
the two canonical `1100` exchanges.

There are nevertheless two exact pieces of protection already built into
the schema.  If a common Dyck suffix `V` is retained, every transport face
has the same suffix projection `U(V)`; faces belonging to distinct suffixes
are therefore support-disjoint.  Also, all context and relay exchanges
occur before the suffix phase, so the reverse suffix-side stem is untouched
whenever its requested depth lies wholly inside `V`.

## 7. Conditional induction

### Proposition 7.1

Assume the prepared-prism gate of Section 6 for one low renewal and its
reflected high-renewal version.  Then the frozen two-hex `T_0` relay extends
recursively through every word generated from `T_0` by the one-counter
renewal productions of the chamber theorem.  Each renewal changes only the
number of internal rethreading hexagons; it adds no word position.

If, in addition, different critical chambers can be assigned disjoint
suffix/context prisms, all targets in those grammar cylinders can be
repaired simultaneously without loss of prior q2 coverage.

#### Proof

Use the frozen relay at the terminal minimal chamber.  Reverse one context
transport for each low renewal and the reflected transport for each high
renewal.  The alternating-sweep assumption makes every algebraic identity a
literal switch sequence.  Turn-faithfulness preserves the closed q2 ledger
at every induction step, topology preserves the component change, and
protection retains the stem.  Induction on the renewal length proves the
claim.  \(\square\)

## 8. Scope

Theorem 3.1 and the count (4.2) are unconditional.  Proposition 7.1 is
conditional.  In particular, this note does not claim that the canonical
MSW factor already contains the required transport prism, that all missing
targets are repaired, or that arbitrary upper widths and the lower compiler
survive the rethread.
