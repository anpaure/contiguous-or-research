# Root-coded receiver banks plant in the PBBS owner factor

**Date:** 2026-08-05  
**Method:** hook action-angle coordinates, marked promoted-parent ports,
commuting clean `C6` switches, exact residual Hall deficiency, and odd
quotient/Tutte scope; no computation  
**Status:** unconditional owner/q1/q2 planting theorem for every fixed
root-coded hook bank after a bank-dependent positive ballast.  The
theorem also identifies the exact zero-ballast port obstruction, proper-cut
residue, and odd-extension residue.  An all-action rooted-bank theorem
remains open.

## 0. Outcome

The root-coded gap construction is not merely an abstract receiver
catalogue.  On every hook action sector whose angle mass exceeds the
vacancy-circle length by the size of the bank's cut-successor footprint
plus four, it is a literal family of PBBS angle tori.
Every elementary adjacent chip move has the selected q1/q2-neutral
clean-`C6` lift.  With at least one ballast chip in every vacancy bank, the
promoted parent's inserted `00` is its unique
adjacent-zero pair and therefore remembers the rooted child edge even
after the mark is forgotten.  Consequently a child matching uses
pairwise-disjoint three-component `C6` supports and can be switched
simultaneously inside the canonical PBBS two-factor.

Thus the **owner/q1 host row is closed** for this bank.  Two different rows
remain:

1. deleting the receiver endpoints must satisfy the residual matching
   cuts.  At even coordinate length these are exact Hall cuts; at odd
   length they are Tutte blossom cuts.

At zero uniform ballast the first assertion above can fail: the promoted
parent may contain several adjacent-zero pairs.  Then distinct rooted
edges still give distinct **marked** ports but may share an unmarked parent
component.  Port separation and q2-halo compatibility are genuine extra
premises on that boundary.

The hook vacancy circle always has odd length, so the actual hook
specialization lands on the second row.

## 1. The root code as a literal hook angle family

Let

\[
                         \ell=2h-1
\tag{1.1}
\]

be the hook vacancy-circle length.  For a 2-independent cut set
`H subset Z_ell`, put

\[
 u_H={\bf1}+\sum_{j\in H}(e_j-e_{j+1}).              \tag{1.2}
\]

Its entries belong to `{0,1,2}` and its total mass is `ell`.  More
generally, for an integer `c>=0`, put

\[
                         u_H^{(c)}=c{\bf1}+u_H.       \tag{1.3}
\]

This is a weak composition of mass

\[
                         b=(c+1)\ell.                \tag{1.4}
\]

Hence `[u_H^(c)]` is a literal angle torus of the hook action

\[
                         (h,1^b).                    \tag{1.5}
\]

If `a` is an admissible cut not in `H`, then

\[
 u_{H\cup\{a\}}^{(c)}
   =u_H^{(c)}+e_a-e_{a+1}.                           \tag{1.6}
\]

All petal endpoints, double-expansion receivers, and counter-circulation
states of the root-coded construction therefore belong to the same hook
angle graph.

### Lemma 1.1 (quotient faithfulness)

Suppose `H` has the protected marker block of the root-code theorem and
all inserted cuts lie in its workspace.  Then the necklace state
`[u_(H union S)^(c)]`, for `|S|<=2`, determines the ordered marker word and
the rooted cut set `H union S`.

In particular, the root-coded receiver vertices and rooted elementary
chip moves do not coalesce under the hook necklace quotient.

#### Proof

Subtracting the minimum digit `c` from (1.3) recovers the digits of
`u_(H union S)`.  In a 2-independent cut state, the coordinates equal to
two are exactly the cuts, so the cut set is recovered.  The two workspace
insertions leave the unique length-at-least-four marker run unchanged, as
in the persistent-root lemma.  A rotation equality must align marker
start and then is equality of the rooted cut sets. \(\square\)

The uniform ballast in (1.3) is important.  An arbitrary noninvariant
ballast word need not respect the quotient argument.

There is a rooted version for every sufficiently large mass, rather than
only the multiples in (1.4).  Reserve one coordinate `z` in a quiet part
of the gap word, away from every old or inserted cut and its successor.
For

\[
                         b\ge2\ell,
 \qquad                  s=b-2\ell,                  \tag{1.7}
\]

put

\[
 t_H^{(s)}
   =2{\bf1}+s e_z+\sum_{j\in H}(e_j-e_{j+1}).         \tag{1.8}
\]

This has mass `b` and every entry is positive.  When `s=0`, its cut
positions are exactly the entries equal to three and the marker roots the
necklace.  When `s=1`, `z` is the unique entry equal to three whose
successor is not one; every cut entry three is followed by its successor
entry one.  When `s>=2`, `z` is the unique entry at least four.  Thus in
all cases the necklace aligns `z` when necessary, then subtracts the known
ballast and recovers the rooted cut set.

Consequently Lemma 1.1 and all conclusions below hold for every hook mass
`b>=2ell`, using (1.8).  Formula (1.3) is the rotation-invariant special
case in which `b` is a multiple of `ell`.

For a fixed finite bank there is a substantially sharper ballast.  Let
`mathcal C` be the union of every cut coordinate which occurs in any hub,
petal endpoint, receiver, or counter-circulation state of the bank, and put

\[
                         Z=\mathcal C+1.              \tag{1.9}
\]

Choose a coordinate `z` outside `mathcal C union Z`; the root-code layout
may reserve one such quiet coordinate.  If

\[
                         b\ge\ell+|Z|+4,
 \qquad                  R=b-\ell-|Z|,               \tag{1.10}
\]

replace every state `u_S` in the bank by

\[
                         \widetilde u_S
   =u_S+{\bf1}_Z+R e_z.                               \tag{1.11}
\]

All states still have mass `b`, and every adjacent-chip difference is
unchanged because the same ballast is added everywhere.  Every zero of
`u_S` is the successor of a cut in `S subseteq mathcal C`, hence belongs
to `Z` and is raised to one.  Thus every `tilde u_S` is positive.  At `z`
the value is `1+R>=4`; away from `z` it is at most three.  The unique
maximum aligns `z`: a counter-circulation state can raise one nonroot
coordinate to at most four, whereas `z` has value `1+R>=5`.  After this
alignment, subtracting the known ballast recovers the rooted state.

Therefore the quotient-faithfulness and positive-predecessor conclusions
hold under the sharper fixed-bank threshold (1.10).  In particular, for a
fixed-size bank this is `b>=ell+O(1)`; for a growing bank its exact price is
the number of distinct possible cut-successor coordinates, not the number
of candidate packets.

## 2. Every rooted elementary move has a selected PBBS lift

The counter-circulation route between two shifted-cut endpoints is a path
of elementary adjacent chip moves

\[
                         x\longmapsto x-e_j+e_{j+1}. \tag{2.1}
\]

The PBBS hook angle-transfer theorem supplies, for every rooted edge
(2.1), a selected common-pivot clean `C6`.  It uses two child hook tori and
one leaf-promoted parent torus and preserves q1 and q2 on its isolated
halo.

The marked-parent theorem identifies its promoted port exactly by

\[
                         P01R,P10R\longmapsto P000R. \tag{2.2}
\]

Deleting the marked `00` recovers the rooted child edge.  Therefore
distinct rooted child edges give distinct marked parent ports, even when
several ports belong to one unmarked parent component.

### Lemma 2.1 (positive ballast makes the promoted parent self-marking)

Use (1.3) with `c>=1`, the rooted positive ballast (1.8), or the fixed-bank
ballast (1.11).  For every elementary move in a counter-circulation route,
write its child pair as

\[
                         [y+e_j],\qquad[y+e_{j+1}].   \tag{2.3}
\]

Then every entry of `y` is positive.  Consequently the promoted parent

\[
                         [\iota_j(y)]                 \tag{2.4}
\]

has exactly one adjacent pair of zero entries.  Its unmarked necklace
therefore determines the rooted child edge `(y,j)`.

#### Proof

Every state in the route is obtained from a baseline whose entries after
the cut derivative are at least one, by moving one or more distinguished
travelling chips.  In an elementary step the donated chip is precisely one
of those extra chips or one of the cut excesses.  Removing it returns that
coordinate to its underlying value, which is still at least one.  Thus `y`
is strictly positive.

The promoted-parent formula inserts two consecutive zeros into `y` and
changes no old entry.  Since `y` has no zero, this is the unique adjacent
zero pair.  Locate and delete it to recover the rooted cyclic vector `y`
and its insertion cut `j`. \(\square\)

### Theorem 2.2 (PBBS owner/q1/q2 planting)

Let `F` be any finite selected bank of distinct rooted elementary edges
from the root-coded hook family with positive ballast—equivalently, use
(1.3) with `c>=1`, (1.8) with `b>=2ell`, or the fixed-bank construction
(1.11).  Assume no child angle torus is an endpoint of two edges of `F`.
For every edge choose its canonical selected clean-`C6` lift.

Then the three PBBS component roles of distinct `C6`s are pairwise
disjoint.  Simultaneously toggling all of them produces a spanning
owner/q1 two-factor.  The owner set and selected q1 and q2 multisets are
unchanged.

#### Proof

The two child occurrences belonging to different edges lie on distinct
child angle tori by the endpoint-matching hypothesis and Lemma 1.1.
Lemma 2.1 makes the **unmarked parent component** injective in the rooted
edge, so different `C6`s also have distinct parent components.  A parent
action has one fewer leaf than its children and therefore cannot coincide
with a child torus at this stage.  Thus the three old component roles of
one `C6` are disjoint from all roles of every other `C6`.

A clean `C6` replaces three disjoint old factor edges by three new edges
on exactly the same six owner endpoints.  Since the endpoint sets of the
different switches are disjoint, all toggles commute and their new edges
are also disjoint.  Every owner retains degree two.  The local selected
`C6` identity preserves the q1 rows.  Its complete q2 companion halo lies
on the same three old components.  The component triples are disjoint, so
the q2 halos are disjoint as well and the isolated q2 identities compose.
This preserves the global selected q1 and q2 multisets. \(\square\)

### Corollary 2.3 (root-coded fan bank)

Any root-coded passive-petal/receiver selection whose chosen elementary
edge set is a matching in child tori satisfies Theorem 2.2.

Thus no additional small-protected-factor theorem is needed merely to put
the rooted bank into the PBBS owner factor: the canonical PBBS factor
already contains all old edges, and the disjoint switches rethread it.

## 3. Exact zero-ballast host obstruction

When `c=0`, a predecessor `y` may already contain isolated zeros.  The
inserted `00` need not be the unique adjacent-zero pair after insertion,
and different rooted child edges may have the same unmarked promoted
parent with different marked ports.  Distinct marked ports can also be
adjacent edges of that parent cycle.  Thus the proof of Theorem 2.2 does
not extend to zero ballast.

The exact additional planting condition there is:

> **Rooted-bank halo condition.**  The chosen clean-`C6` lifts have
> pairwise disjoint q2 companion halos, or their overlaps are oriented in
> one of the proved consecutive-sibling telescoping patterns.

Root coding separates child angle tori and marked parent ports, but at zero
ballast it does not order those ports or the q2 companion occurrences on a
shared unmarked parent component.  It therefore does not prove this halo
condition.  Positive uniform ballast removes the issue by Lemma 2.1.

For general capacity-two macro sectors, rather than hook sectors, there is
an even earlier missing row: the capacity-two decomposition proves that
the token moves remain critical, but it does not supply the selected
q1/q2-neutral PBBS clean-`C6` lift for every background.  The hook lift is
the reason Theorem 2.2 is unconditional at the stated specialization.

## 4. Recheck of the even proper-cut Hall system

Now forget the hook parity and consider an even coordinate-length
capacity-two sector in which a root-coded bank has been planted.  Root
coding makes each endpoint diagonal graph a matching.

Let `G=(L,R;E)` be the ordinary bipartite sector graph.  For a left Hall
set `U`, put

\[
                         D=N_G(U).                    \tag{4.1}
\]

Discard every receiver job visible from `U`.  Among the remaining jobs,
let

\[
 h_B(U)=|\{j:A_j\cap U=\varnothing, B_j\subseteq D\}|. \tag{4.2}
\]

### Theorem 4.1 (exact proper-cut residue for a private bank)

For a root-coded bank, the residual endpoint-list deficiency on the `B`
shore is exactly `h_B(U)`.  Hence the complete left-shore augmented Hall
system is

\[
 \boxed{
 h_B(U)\le |N_G(U)|-|U|
 \qquad(U\subseteq L).}                              \tag{4.3}
\]

The right-shore system is the symmetric inequality with `A,B` exchanged.

#### Proof

The full `B` endpoint graph is a matching.  After deleting `D`, a retained
job has a two-element list, a singleton list, or the empty list.  Different
jobs use disjoint endpoint vertices.  The first two cases admit disjoint
representatives independently; every empty list contributes exactly one
unit of deficiency.  Those empty lists are precisely (4.2).  Substitute
this exact deficiency into the augmented Hall formula. \(\square\)

Thus root coding solves the empty-shore bicycle obstruction:
`h_B(emptyset)=0`.  It does **not** automatically prove the proper cuts
(4.3).

There is a useful sufficient expansion certificate.  Let `J_*` be the
jobs counted by (4.2), put

\[
 X=\bigcup_{j\in J_*}A_j,
 \qquad
 E_*=N_G(X)\setminus D.                              \tag{4.4}
\]

Both-shore privacy gives

\[
 |X|=\sum_{j\in J_*}|A_j|,
 \qquad X\cap U=\varnothing.                          \tag{4.5}
\]

Hall applied to `U union X` yields

\[
 |D|-|U|\ge |X|-|E_*|.                               \tag{4.6}
\]

Consequently (4.3) follows whenever

\[
                         |E_*|\le |X|-h_B(U).         \tag{4.7}
\]

When no fixed deletion has removed an `A` option, `|X|=2h_B(U)` and (4.7)
becomes `|E_*|<=h_B(U)`: on average, the opposite diagonal of every trapped
square may expose at most one ordinary neighbour outside the original Hall
neighbourhood.  Root markers alone do not imply this condition.

## 5. Odd quotient and blossom scope

The hook vacancy length (1.1) is odd.  Every stabilizer of a hook
background is therefore odd, while the selected rooted states themselves
have trivial stabilizer by Lemma 1.1.

### Proposition 5.1 (endpoint safety descends)

The occurrence endpoint graphs of a root-coded bank are matchings.  Their
images in every odd rotational quotient are again pseudoforests; in fact
the marker prevents any cross-fan endpoint identification, so they remain
matchings on the selected bank.

#### Proof

Marker alignment proves injectivity of the selected endpoint orbits.  The
general odd-group quotient theorem also shows that a tree/unicycle
pseudoforest cannot acquire a bicycle under an odd rotation action.  Here
the stronger marker injection gives the matching conclusion directly.
\(\square\)

This does not turn the odd sector into a Hall problem.  After adding job
terminals and the possible parity socket, protected extension is exactly

\[
 o(\widehat G-S)\le |S|
 \qquad\hbox{for every }S\subseteq V(\widehat G),     \tag{5.1}
\]

where `o` counts odd components.  These are the Tutte blossom cuts.
Root coding removes endpoint coalescence from (5.1), but an ordinary odd
component of the residual PBBS angle graph can still violate it.

Nor does semiregular strict-Hall descent settle (5.1): strict Hall is a
bipartite proper-cut statement, whereas an odd blossom can survive with no
endpoint collision at all.

## 6. Exact integrated frontier

For the rooted hook bank, the remaining implication chain is now

```text
root-coded hubs and workspace petals
  -> literal quotient-private hook angle tori
  -> selected clean-C6 lifts
  -> simultaneous owner/q1 PBBS rethread       [proved]
  -> q2 halo-disjointness or telescoping        [open]
  -> even: trapped-square cuts (4.3),
     odd: Tutte blossom cuts (5.1)              [open]
  -> cross-level receiver regeneration          [open].
```

The root code therefore eliminates the former three-matroid endpoint
selector and its empty-shore bicycle loss on an actual PBBS family.  The
exact host obstruction is no longer owner-factor extension.  It is the
combination of physical q2 halo compatibility with the residual
Hall/Tutte matching cuts.
