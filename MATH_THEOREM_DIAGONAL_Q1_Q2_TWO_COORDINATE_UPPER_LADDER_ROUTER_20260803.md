# A native q1/q2 upper ladder gives a two-coordinate terminal router

**Date:** 2026-08-03  
**Status:** exact conditional occurrence theorem.  No computation is used.
The theorem closes the **raw interval-address count** for one new nested
upper ticket type by using two different native interval-width banks.  It
does not by itself close the canonical folded-C8/two-cross-ray terminal
gate: that ticket has a different phase, role, and Boolean-incidence type.
The theorem assumes the second upper step is rank one and that one fixed
terminal state accepts the displayed paired occurrence type.  It does not
construct an all-dimensional carrier satisfying those hypotheses or a
type-conversion gadget from the canonical cross rays.

## 0. Result

Let indices lie in `Z_W`, let `2<=d<W-3`, and let

\[
                         A_0,\ldots,A_{W-1}\ne\varnothing
\]

be a cyclic literal word.  Assume the flat q1-exact diagonal identities

\[
 T_i=\bigcup_{h=i}^{i+d}A_h,qquad
 P_i=\bigcup_{h=i+1}^{i+d}A_h=T_i\cap T_{i+1},          \tag{0.1}
\]

with `|P_i|=r-1`, `|T_i|=r`, and with the two families enumerating their
two middle-level shores.

Put

\[
 R_i=T_i\cup T_{i+1},qquad
 U_i=R_i\cup A_{i+d+2}.                                 \tag{0.2}
\]

Assume additionally

\[
                         |R_i|=r+1,qquad |U_i|=r+2      \tag{0.3}
\]

for every `i`.  The first equality follows already from (0.1); the second is
the genuine q2-ladder hypothesis.

Give the four occurrences the cyclic interval addresses

\[
\begin{aligned}
 p_i&=[i+1,i+d]_W,\
 o_i&=[i,i+d]_W,\
 q_i&=[i,i+d+1]_W,\
 u_i&=[i,i+d+2]_W.
\end{aligned}                                            \tag{0.4}
\]

Then

\[
 p_i\subset o_i\subset q_i\subset u_i                 \tag{0.5}
\]

is simultaneously a chain of physical interval addresses and the Boolean
Hasse chain

\[
 P_i\subset T_i\subset R_i\subset U_i.                 \tag{0.6}
\]

The alternative q1 orientation gives

\[
 p_i\subset o_{i+1}\subset q_i\subset u_i,qquad
 P_i\subset T_{i+1}\subset R_i\subset U_i.             \tag{0.7}
\]

Consequently the `W` records

\[
 \mathcal B^0_i=(p_i,o_i,q_i,u_i),qquad
 \mathcal B^1_i=(p_i,o_{i+1},q_i,u_i)                   \tag{0.8}
\]

are, in either phase, pairwise occurrence-disjoint complete bundles.  Every
bundle has the two distinct terminal coordinates

\[
                         (q_i,u_i).                     \tag{0.9}
\]

Thus, if one fixed common-cap state accepts the complete **nested-upper**
paired type

\[
 (R_i\hbox{ at }q_i, U_i\hbox{ at }u_i)                \tag{0.10}
\]

for ticket `i`, the `W` bundles form an exact deterministic two-coordinate
terminal linkage with no additional physical cells.  On that accepted type
this directly avoids the `2W`-demand-versus-`W`-bank cut: the two terminal
banks have different interval widths and are disjoint.  No such acceptance
is inferred for the canonical cross-ray tickets.

## 1. Literal ladder identities

The q1 diamond identities give

\[
 P_i\cup A_i=T_i,qquad
 T_i\cup A_{i+d+1}=R_i.                                 \tag{1.1}
\]

By definition,

\[
                         R_i\cup A_{i+d+2}=U_i.          \tag{1.2}
\]

The ranks in (0.1) and (0.3) make every inclusion in (1.1)--(1.2) strict
of rank one.  Hence they are Boolean Hasse incidences.  Their interval
addresses are obtained by successively adding the left endpoint `i`, the
right endpoint `i+d+1`, and the right endpoint `i+d+2` to `p_i`, proving
(0.5)--(0.6).

For the second phase use

\[
 P_i\cup A_{i+d+1}=T_{i+1},qquad
 T_{i+1}\cup A_i=R_i,                                   \tag{1.3}
\]

followed by (1.2).  This proves (0.7).

As in the one-coordinate interval-diamond theorem, the displayed source
letters are semantic labels of the Hasse incidences.  Overlap of source
positions by different interval witnesses is not a capacity collision.

## 2. Capacity audit

Fix either phase.  Across different indices `i`, the port addresses `p_i`
are distinct, the owner addresses are distinct, the q1 upper addresses
`q_i` are distinct, and the q2 upper addresses `u_i` are distinct.  These
four address families also have four different lengths, so an address in
one family cannot equal an address in another.

Therefore the bundles in (0.8) are pairwise disjoint in every finite
occurrence coordinate.  The two terminals of one bundle are different
addresses because

\[
                         |q_i|=d+2,qquad |u_i|=d+3.     \tag{2.1}
\]

Notice that distinctness is address-level; the values `R_i` or `U_i` need
not be globally distinct for the terminal capacity statement.

If the owner occurrence is reserved as a semantic witness and unavailable
as a residual transit capacity, contract each chain in (0.8) to the complete
canonical record

\[
 \beta_i=(p_i;q_i,u_i;P_i,T_i,T_{i+1},R_i,U_i,
                    A_i,A_{i+d+1},A_{i+d+2}).           \tag{2.2}
\]

Its finite terminal coordinates remain `(q_i,u_i)`, and the records are
still pairwise disjoint.  The internal data in (2.2) are declarative parts
of one conjunctive route, not separately selectable atoms.

## 3. Direct joint-routing formulation

Let `I=Z_W` be the logical ticket set for this nested-upper system.  For
every `i`, give ticket `i` the single deterministic representative `beta_i`
of (2.2).  If the fixed cap, guard, and occurrence state accepts (0.10),
these `W` representatives are simultaneously legal and capacity-disjoint.
Hence this joint two-coordinate independence system has rank

\[
                         r(I)=W.                        \tag{3.1}
\]

No product-of-marginals inference is used.  The paired occurrence relation
is the deterministic graph

\[
                         i\longmapsto(q_i,u_i),          \tag{3.2}
\]

already materialized in one word.  Thus (3.1) is stronger than checking two
separate marginal Rado ranks and then assuming product closure.

Equation (3.1) is not a rank statement about the canonical two-cross-ray
Rado systems unless a separate theorem places `beta_i` in their complete
typed occurrence menus and in their legal paired relation.  Merely having
two distinct addresses does not provide that identification.

Any transported background must still avoid or be contracted away from the
two displayed terminal banks.  That is an additional hypothesis on the
complete state, not a consequence of the ladder.

## 4. Scope and the new target

This theorem proves:

* two distinct native `W`-element terminal banks;
* one deterministic paired occurrence for every ticket;
* pairwise-disjoint complete routes in either q1 phase;
* a reserved-owner bundle contraction; and
* zero additional word length for the two-coordinate terminal bank.

It does not prove:

* an all-dimensional q1-exact carrier;
* the q2 rank-one condition `|U_i|=r+2` at every seam;
* acceptance of `(R_i,U_i)` by the canonical two cross-ray ticket type;
* compatibility with transported background, lower flags, residence, or
  regeneration; or
* an additive-constant upper bound for `nu(k)`.

### Exact type boundary

For `1<=j<d`, a canonical folded-C8 antidiagonal ticket has value pair

\[
 \bigl(C\cup F[1,j],\ C\cup F[j+1,d]\bigr),             \tag{4.1}
\]

up to its fixed active labels.  Its two coordinates are separately
addressed, normally lie in opposite phases, and are incomparable: their
intersection is `C` and their union is `C union F`.  Their symmetric
difference contains all `d` filler labels.

By contrast, (0.10) is a same-phase nested Hasse pair

\[
                         R_i\subset U_i,\qquad
                         |U_i-R_i|=1.                       \tag{4.2}
\]

Therefore no identification preserving phase, ray role, Boolean
intersection/union type, or address incidence can map the canonical ticket
to (0.10) for `d>=2`.  A cap state may define a genuinely new accepted
nested-upper ticket, or an additional conversion gadget may be proved, but
neither follows from the ladder identities.

The raw address-supply target has therefore sharpened from

\[
 \text{find two copies of one }W\text{-socket bank}
\]

to

\[
 \boxed{\text{construct a type-preserving conversion/acceptance theorem
 from the canonical cross rays to the native nested upper pair, in one
 cap state}.}
\]
