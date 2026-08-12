# Delcourt--Postle colourings do not force planted C6 off pairs to align

Date: 2026-07-31  
Status: exact catalogue count, exact conditional-reservation formulation,
and a list-colouring no-go.  The result rules out using the **unconditioned
full colouring, additive weights, or the published list-colouring corollary**
as a black box which co-colours a planted suspended-hex bank.  It does not
rule out precontracting a packet, precolouring a dedicated class, or choosing
the body and the absorber bank jointly by a new theorem.

## 0. Verdict

Let `G_Q` be one four-uniform punctured capacity-slot shore and let
`H_L` be its short-physical-cycle conflict system.  A suspended transparent
hex has an off phase `{x,y}` and target atom `t`; if one colour class contains
`x,y` and leaves all four resources of `t` free, the switch gains one atom.

The full Delcourt--Postle colouring does not force this event.

1. In the canonical unpunctured catalogue every atom is an endpoint of
   exactly

   \[
                         4n(n-2)                                      \tag{0.1}
   \]

   off pairs, but a colour class may contain **zero** of them.
2. For every pairwise-resource-disjoint planted packet bank and every list
   assignment in the Delcourt--Postle range, there exists a valid list
   colouring in which every planted off pair is bichromatic.  This follows
   by declaring the planted pairs themselves to be forbidden size-two
   configurations; their conflict hypergraph is only a matching and leaves
   every Delcourt--Postle hypothesis intact.
3. The exact conditional reservation encoding has one configuration
   `{x,y,e}` for every atom `e` meeting the target.  In the all-capacity-two
   host a fixed pair `{x,y}` belongs to exactly

   \[
                         4n(2n-1)=\Theta(D_0)                         \tag{0.2}
   \]

   such triples, where `D_0=2(n+1)(n+2)`.  Thus the direct encoding violates
   the power-saving `(3,2)`-codegree hypothesis.  This is not a removable
   counting slack: omitting even one of those triples permits that blocker
   to consume a target resource.
4. Additive weighting is blind to whether the two endpoints of a pair have
   the same colour.  Contracting a whole packet makes the equality literal,
   but ordinary colour averaging still falls short by order `P/n`; it gives
   another `P-o(P)` construction, not zero defect.

Therefore the full colouring remains useful as a distributed body/exchange
reservoir, but it does not perform the required correlated planting.  The
missing theorem must select a body and its off phases together (or work on a
contracted packet host with an exact finishing mechanism).

## 1. Exact canonical off-pair graph

Work first in the unpunctured canonical slot-`1` host on `[2n]`.  An atom is
an incidence

\[
                  A=(D,V),\qquad |D|=n,quad |V|=n+2,quad D\subset V. \tag{1.1}
\]

Put

\[
 M={2n\choose n}=P+C,qquad N={2n\choose {n+1}}={2n\choose {n-1}}. \tag{1.2}
\]

The atom set has order

\[
 |\mathcal A_n|=M{n\choose2}={N(n^2-1)\over2}.                    \tag{1.3}
\]

For a target `A=(D,V)`, write `V-D={p,q}`.  The suspended-hex theorem chooses

\[
 b\in D,\qquad c\notin V,\qquad (a,s)=(p,q)\text{ or }(q,p).     \tag{1.4}
\]

Thus it gives exactly `2n(n-2)` off pairs through `A`.

### Theorem 1.1 (regular simple catalogue graph)

Let `R_n` be the graph on `mathcal A_n` in which two atoms are adjacent when
they are the canonical off phase of a suspended hex.  Retain the target as
an edge label.  Then:

\[
 \deg_{R_n}(e)=4n(n-2)\quad(e\in\mathcal A_n),                    \tag{1.5}
\]

\[
 |E(R_n)|=2n(n-2)|\mathcal A_n|
          =n(n-2)N(n^2-1),                                      \tag{1.6}
\]

and every unordered off pair has exactly one target label.

#### Proof

If `e` occurs in the `e_a` role, choose the deleted core element in `n`
ways, orient the two extension elements in two ways, and choose the fourth
active element in `n-2` ways.  This gives `2n(n-2)` occurrences.  The
`e_c` role gives another `2n(n-2)`.

Conversely an off pair recovers the suspended hex uniquely.  Its two lower
sets meet in the `(n-1)`-set `K`; their two exceptional elements recover
`a,c`.  The upper set over `K+a` recovers `s`, and the upper set over `K+c`
then recovers `b`.  Hence the target `(K+b,K+a+b+s)` is unique.  Double
counting proves (1.6).  \(\square\)

The statement is for the canonical auxiliary slot choice used in the
suspended-hex theorem.  An atom with noncanonical auxiliary slots has degree
zero in this restricted graph; allowing every auxiliary slot lift enlarges
the catalogue but is unnecessary for the no-go below.

### Colour collision ledger

For a colouring `phi` and a colour `c`, define

\[
 z_c(\phi)=|\{xy\in E(R_n):\phi(x)=\phi(y)=c\}|.                  \tag{1.7}
\]

Then the only universal identity is

\[
 \sum_c z_c(\phi)
   =|\{xy\in E(R_n):\phi(x)=\phi(y)\}|.                          \tag{1.8}
\]

The right side has no positive colour-invariant lower bound.  For comparison
only, an independent uniform `q`-colouring would have

\[
 \mathbb E z_c={n(n-2)N(n^2-1)\over q^2}\sim {N\over4}           \tag{1.9}
\]

when `q~D_0~2n^2`.  This is not a legal-colouring theorem, and it counts
highly overlapping off pairs rather than a resource-private absorber bank.

For a planted bank of `T` pairwise-resource-disjoint packet supports, let
`z_c^B` count its co-coloured off pairs.  Exactly

\[
                 \sum_c z_c^B=Z_\phi,qquad 0\le Z_\phi\le T.    \tag{1.10}
\]

If equality were imposed by contraction, then `Z_phi=T` and averaging gives
only `max_c z_c^B>=T/q`.  Without contraction even the lower bound `1` is
false.

## 2. The exact conditional-reservation conflicts

Let a planted packet have off atoms `{x_i,y_i}` and target `t_i`.  For every
host atom `e` meeting one of the four literal resources of `t_i`, introduce
the three-configuration

\[
                             \{x_i,y_i,e\}.                       \tag{2.1}
\]

If both off atoms receive colour `c`, avoidance of (2.1) says exactly that
the colour-`c` class leaves every target resource unused.  If packet supports
are not resource-disjoint, one must additionally forbid

\[
                    \{x_i,y_i,x_j,y_j\}                           \tag{2.2}
\]

whenever `t_i,t_j` conflict.  For the resource-disjoint bank of the packet
packing theorem, (2.2) is empty.  Hence simultaneous activation of all
co-coloured pairs is a host matching precisely when (2.1) is imposed (with
the separate contracted-graphic test still required for physical
acyclicity).

### Proposition 2.1 (exact blocker count)

In the unpunctured all-capacity-two occurrence host, every ordinary literal
target is met by exactly

\[
                              4n(2n-1)                            \tag{2.3}
\]

occurrence atoms.

#### Proof

Let the target resources be lower `D`, upper `V`, and prescribed slots
`(x,i),(y,j)`.  Their four occurrence degrees are

\[
 4{n\choose2},\quad4{n+2\choose2},\quad2(n^2-1),\quad2(n^2-1).
                                                                    \tag{2.4}
\]

The six pair-intersection sizes are

\[
       4, 2(n-1), 2(n-1), 2(n+1), 2(n+1), 1.                \tag{2.5}
\]

The four triple intersections have sizes `2,2,1,1`, and the fourfold
intersection has size one.  Inclusion--exclusion gives

\[
 (8n^2+4n)-(8n+5)+6-1=4n(2n-1).                                \tag{2.6}
\]

\(\square\)

For a resource-disjoint bank, an arbitrary blocker atom belongs to at most
four configurations (2.1), because its four resources can meet at most four
disjoint target supports.  But the fixed pair `{x_i,y_i}` belongs to every
one of the `4n(2n-1)` configurations for its target.  Consequently

\[
 \Delta_3(H_{\rm res})=\Delta_{3,2}(H_{\rm res})=4n(2n-1)        \tag{2.7}
\]

in the ordinary symmetric host.

Since `D_0=2(n+1)(n+2)=Theta(n^2)`, (2.7) is `Theta(D_0)`, not
`D_0^(1-beta)` for any fixed `beta>0`.  Thus Corollary 1.17 cannot be applied
directly to the exact conditional-reservation system.  Sparsifying (2.1)
would make the conclusion unsound: every omitted blocker may receive the
off-pair colour and consume a required target resource.

Contracting `{x_i,y_i}` into an eight-resource off macro changes (2.1) into
a two-conflict, but does not cure the mixed codegree.  At a target resource
`v` outside the off macro, all `Theta(D_0)` atoms through `v` are conflict
neighbours of the macro.  Contracting the **entire twelve-resource packet
support** does cure this local exponent problem, because reservation is then
ordinary host disjointness.  Section 4 explains why that contraction still
does not give exact cover-down by colour averaging.

## 3. A list-colouring separation theorem

The equality failure is stronger than the absence of an averaging proof.

### Theorem 3.1 (every planted bank can be made wholly bichromatic)

Let `B={(x_i,y_i):i in[T]}` be the off pairs of any pairwise-resource-
disjoint planted suspended-hex bank in `G_Q`.  Let `L` be any edge-list
assignment satisfying the list-size hypothesis of the applicable
Delcourt--Postle corollary.  Then there is an `L`-colouring of

\[
                         L(G_Q)\cup H_L                            \tag{3.1}
\]

in which

\[
                         \phi(x_i)\ne\phi(y_i)\qquad(i\in[T]).    \tag{3.2}
\]

The many-disjoint-list-colourings conclusion may likewise be chosen so that
every one of the returned colourings satisfies (3.2).

#### Proof

Add the pairs in `B` as size-two configurations.  They form a matching on
the atom set.  Therefore they add one to the maximum size-two configuration
degree and at most one to the mixed two-codegree; their common two-degree is
zero.  They change no higher configuration degree or codegree.  All
Delcourt--Postle hypotheses remain valid with the same asymptotic parameter.
Apply the list-colouring (or many-disjoint-list-colourings) corollary to
`H_L union B`.  Avoidance of each new two-configuration is exactly (3.2).
\(\square\)

Thus no admissible large-list assignment can make even one prescribed
off-pair equality unavoidable in all valid colourings.  In particular,
the list theorem cannot be used as an equality gadget by choosing highly
overlapping lists.

This is a black-box no-go, not a claim that no favourable colouring exists.
One may deliberately optimize over colourings for many equalities, but that
is a new correlated theorem not contained in Delcourt--Postle.

## 4. Additive weights and full-support contraction

Assigning linear weights to off endpoints cannot detect co-location.  For
example, putting weight `1/2` on each endpoint makes every planted pair
contribute total weight one whether it is monochromatic or bichromatic.
More generally, sums of the form

\[
                     \sum_{e\in M_c}w(e)                           \tag{4.1}
\]

are linear in individual atoms, whereas the gain variable
`1[phi(x_i)=phi(y_i)]` is quadratic.  The exact collision ledger (1.10) and
Theorem 3.1 show that ordinary largest-weight-class averaging has no positive
gain term to average.

There is one honest way to linearize the equality: replace a packet by one
twelve-resource macro edge containing all three lower, all three upper, and
all six literal slot resources of its two phases.  A selected macro can be
realized off and later switched on; host disjointness automatically reserves
its target.  For a resource-disjoint bank of `T` supports, the macros add at
most one to every host degree and satisfy

\[
                              T\le P/3,                            \tag{4.2}
\]

because each support uses three distinct upper resources.

Even granting a conflict-free colouring of the augmented host, the standard
colour average does not force a perfect activated class.  Give an ordinary
atom weight one and a macro weight three (its on-phase size).  Every colour
class has activated weight at most `P`.  Yet the fixed-`Q` edge ledger gives

\[
 |E(G_Q)|\le4P{n\choose2}
            =(D_0-8n-4)P.                                      \tag{4.3}
\]

Thus, even using the maximum bank in (4.2),

\[
             |E(G_Q)|+3T\le(D_0-8n-3)P.                         \tag{4.4}
\]

On the `q>=D_0` palette used in the standard corollary, the guaranteed
average activated weight is at most

\[
                    P-{(8n+3)P\over q}=P-\Theta(P/n).            \tag{4.5}
\]

The theorem's additional `D_0^(1-alpha)` colour slack only weakens this
average.  Hence full-support contraction is a sound way to **condition** a
packet, but the published colouring ledger still yields only a near-perfect
class.  It does not make the residual defect zero.  A colouring which happens
to use fewer colours may of course do better; (4.5) says precisely that this
is not forced by the Delcourt--Postle bound and additive averaging.

Precolouring every macro into one dedicated class and applying the matching
theorem to the resource-deleted remainder has the same scope: it produces a
planted `P-o(P)` body, with another `o(P)` unaligned leave.  Closing that
leave is exactly the correlated cover-down theorem, not a consequence of
the edge colouring.

## 5. Consequence for the Catalan programme

The full colouring supplies many near-forests and a useful exchange core.
It cannot, by itself, select one colour whose missing resources are exactly
the targets of co-coloured suspended hexes.  There are three independent
reasons:

1. equality of two disjoint atoms is not an avoidance constraint;
2. exact conditional reservation has linear, rather than power-saving,
   pair codegree before full-support contraction; and
3. after contraction, the colour-count ledger retains an order-`P/n`
   deficit.

The correct positive target is therefore a **body-conditioned packet
selection theorem**: choose a common basis, a physical bulk, and a set of
full-support packet macros jointly so that the residual body degree is
exactly the activated packet demand, and then verify the graphic/root and
downstream compiler rows.  This is strictly stronger than retaining all
Delcourt--Postle colour classes and strictly weaker than an absorber for an
arbitrary post hoc leave.

## 6. Independent finite audit

The script

```text
scratch/audit_catalan_dp_c6_colour_conditioning_20260731.py
```

enumerates `3<=n<=6` and verifies:

* `2n(n-2)` canonical packets per target;
* uniqueness of the target of every off pair;
* regular degree `4n(n-2)` of the canonical off-pair graph;
* equation (1.6); and
* the all-capacity-two blocker count `4n(2n-1)`.

Its retained output is

```text
scratch/catalan_dp_c6_colour_conditioning_20260731.audit.json
```

with status `PASS`.  The audit deliberately excludes puncture survival,
the analytic Delcourt--Postle hypotheses, and exact Catalan completion.
