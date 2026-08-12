# A common PBBS tag reservoir plants every synchronized height collar

**Date:** 2026-08-06  
**Method:** explicit coordinate calculus and missing-tag signatures; no
computation or search  
**Status:** unconditional **interior** resource-separation theorem for the
synchronized collars at all high PBBS heights.  It removes collisions among
the positive-time collar owners and collar lower colours.  It does not show
that all five collars can be attached to the literal height ladder: adjacent
heights have a load-bearing endpoint overlap, and some intercut arcs have
zero length.  Thus endpoint topology, full-collar domination, typed cap,
and antecedent-boundary regeneration remain separate.

## 1. The common reservoir

Use the explicit height-pentagon notation on the ground set
`{0,1,...,2r}`.  For `4 <= h < H`, the five head/tail owners have the
common rank-`r-2` core

\[
 G_h=[2r+1]\setminus(L_h\cup A_h),
\]

where

\[
 L_h=000\,1^{h-1}0^{h+1}(10)^{r-h-1}
\]

and

\[
 A_h=\{0,1,2,2h+1,2h+2\}.
\]

### Lemma 1.1 (literal form of the height core)

One has

\[
 \boxed{
 G_h=\{h+2,h+3,\ldots,2h\}
       \mathbin{\dot\cup}
       \{2h+4,2h+6,\ldots,2r\}.}
 \tag{1.1}
\]

Consequently

\[
 \boxed{
 J_H:=\{2H+2,2H+4,\ldots,2r\}
       \subseteq\bigcap_{h=4}^{H-1}G_h,}
 \qquad |J_H|=r-H.
 \tag{1.2}
\]

#### Proof

The initial three zeroes of `L_h` are precisely the first three members of
`A_h`.  The next block of zeroes occupies positions `h+2,...,2h+2`; its
last two positions are the other two members of `A_h`.  The zeroes in the
final alternating block are `2h+4,2h+6,...,2r`.  Removing `A_h` leaves
(1.1).  If `h <= H-1`, every even coordinate from `2H+2` onward belongs to
the final alternating-zero block in (1.1), proving (1.2).  The displayed
arithmetic progression has `r-H` members.  \(\square\)

The important point is quantitative: the number of high collars is
`Theta(H)`, whereas their common reservoir has size `r-H`.  In the
deadline range `H=O(sqrt(r))`, the common reservoir is much larger.

## 2. Global missing-tag construction

There are five synchronized incoming collar paths at each height.  Index
all paths by

\[
 \mathcal P=\{(h,i):4\le h<H,\ i\in\mathbb Z_5\},
 \qquad m:=|\mathcal P|=5(H-4).
 \tag{2.1}
\]

Fix a residence parameter `delta` with

\[
 5\le\delta\le r-6.
 \tag{2.2}
\]

Assume

\[
 \boxed{m\le r-H,
 \qquad m+\delta\le r+1.}
 \tag{2.3}
\]

Choose distinct tags

\[
 g_p\in J_H\qquad(p\in\mathcal P)
 \tag{2.4}
\]

and write `mathcal T={g_p:p in mathcal P}`.  For path `p=(h,i)`, choose

\[
 D_p\subseteq G_h,qquad |D_p|=\delta-2,
 \tag{2.5}
\]

so that

\[
 D_p\cap\mathcal T=\{g_p\}.
 \tag{2.6}
\]

This is possible because `mathcal T subseteq G_h` and

\[
 |G_h\setminus\mathcal T|=r-2-m\ge\delta-3.
\]

Put `K_p=G_h\setminus D_p`.  In the synchronized sliding-window collar,
order `D_p` with `g_p` first, then the three endpoint-screen labels, and
then the common ordering of the exterior set.  The owner states are those
of the corrected collar theorem:

\[
 S_p(t)=K_p\cup
 \{w_{p,t+1},\ldots,w_{p,t+\delta+1}\},
 \qquad 0\le t\le r+3.
 \tag{2.7}
\]

### Theorem 2.1 (global tag separation)

For every path `p`:

\[
 S_p(0)\cap\mathcal T=\mathcal T,
 \tag{2.8}
\]

while every positive-time owner satisfies

\[
 \boxed{S_p(t)\cap\mathcal T
       =\mathcal T\setminus\{g_p\}}
 \qquad(t\ge1).
 \tag{2.9}
\]

Every lower colour on path `p` has the same missing-tag signature:

\[
 \boxed{(S_p(t)\cap S_p(t+1))\cap\mathcal T
       =\mathcal T\setminus\{g_p\}.}
 \tag{2.10}
\]

Therefore positive owners on different synchronized collar paths are
different, and lower colours on different paths are different.  They are
also different from every protected pentagon owner or pentagon lower
facet containing all global tags.  No assertion is made here about
collisions among the time-zero endpoints themselves.

#### Proof

Every selected tag lies in every `G_h`.  Equation (2.6) puts all tags
other than `g_p` in the fixed core `K_p`.  The tag `g_p` is the first
letter of the initial window, so it belongs to `S_p(0)` and leaves on the
first Johnson transition.  It cannot return: it lies in `G_h`, whereas
the later common exterior word lies in `[2r+1]\setminus G_h`.  This proves
(2.8)--(2.9).

The first lower colour is the intersection of the endpoint window and the
window after `g_p` leaves, so it omits `g_p`; every later state also omits
it.  All other tags remain in `K_p`.  This proves (2.10).

Distinct paths have distinct omitted tags, hence distinct signatures.
Every protected pentagon owner and lower facet at height `h` contains
`G_h`, and therefore contains all of `mathcal T`.  Such a resource cannot
equal a positive collar resource that omits one tag.  The endpoint
attachment at `S_p(0)` is the intended overlap, not a collision.  \(\square\)

Within one path, owner simplicity and lower-colour simplicity remain those
proved by the corrected sliding-window collar theorem.  Theorem 2.1 is
exactly the missing cross-path statement.

## 3. Deadline-scale consequence

### Corollary 3.1

If

\[
 H=O(\sqrt r),\qquad \delta=O(\sqrt r),
 \tag{3.1}
\]

then (2.3) holds for all sufficiently large `r`.  Hence all high-height
synchronized-collar interiors can be chosen simultaneously with no owner
or lower-colour collision.  This is an interior statement only.  If a
separate construction supplies degree-at-most-two acyclic endpoint
attachments, then the union is a protected incidence path forest; the tag
argument does not supply those attachments.

The finitely many low-height exceptional collars are not included in this
statement.  They may be retained as part of the bounded boundary state, or
handled by a separate protected-bank argument; no automatic disjointness
from an arbitrarily frozen low-height realization is claimed here.

Conditional on a valid endpoint attachment and on a full collar on every
positive-length intercut arc, the synchronized-current and
protected-extension theorems then give the one-cut occurrence bijection,
multi-cut full-union domination, exposures
`e=O(r^(3/2))`, `alpha,beta=O(sqrt(r))`, and extension to a spanning
two-factor.  Those attachment/intercut premises are not consequences of
the present theorem.

Indeed the literal ladder has a binding adjacent-height overlap.  For
`h>=5`, the common-deletion formula gives

\[
 g(Z_h^0)=Z_{h-1}^1,
 \qquad P_{h,0}=Q_{h-1,1}.
 \tag{3.2}
\]

After the simultaneous head shifts this owner already lies on rethread
edges from the two adjacent pentagons.  Adding an independent collar edge
there would create protected degree three unless it replaces or fuses with
one of those edges.  The same overlap creates a zero-length intercut arc,
so full-collar domination cannot simply be invoked there.  A shared/fused
adjacent-height collar is therefore still required.

## 4. Exact remaining scope

This theorem removes **interior cross-pentagon resource collisions** only.
It neither resolves the adjacent-height endpoint identity (3.2) nor proves
that an arbitrary frozen factor can be retrofitted.

The remaining correlated rows are:

* controlling the component structure of the completed two-factor beyond
  the already connected named height ladder;
* fusing the collars across the adjacent-height endpoint overlaps and
  zero-length intercut arcs;
* absorbing the clipped source-residence flags at the outer boundary;
* realizing the common histories in one depth-`delta` antecedent; and
* extending the occurrence bijection to the typed common-cap network.

Thus only the collar-interior collision row is closed.  The global upper
current still depends on the fused endpoint construction, and topology,
source history, and typed cap remain explicitly separate.

## 5. Dependencies

* `MATH_THEOREM_PBBS_AH_LADDER_PENTAGON_RETURN_20260805.md`;
* `MATH_THEOREM_PBBS_PENTAGON_THREE_SCREEN_COMMON_HISTORY_AND_UPPER_CURRENT_GATE_20260805.md`;
* `MATH_THEOREM_PBBS_SYNCHRONIZED_INCOMING_COLLAR_CANCELS_COMPLETE_UPPER_CURRENT_20260805.md`;
* `MATH_THEOREM_POLYNOMIAL_PROTECTED_FOREST_EXTENSION_FROM_TWO_EXPOSURES_20260805.md`;
* `MATH_AUDIT_PBBS_SYNCHRONIZED_COLLAR_AND_POLYNOMIAL_EXTENSION_20260806.md`.
