# Literal low-target collars and a protected singleton bank

**Date:** 2026-08-06  
**Method:** explicit source factorization and stabilizer averaging; no
computation or search  
**Status:** unconditional local collar for every target of rank at most the
owner aperture, and a prospective protected packing for every target of
rank at most the deadline.
The explicitly audited braid and residual components of the rigid PBBS
rotation have no singleton source cells in the eventual central regime.
The untouched-component question is now closed positively by
`MATH_THEOREM_PBBS_HOOK_MOUNTAIN_NATIVE_SINGLETON_BANK_20260806.md`: one
native hook component contains all coordinate singleton tickets at once.
The prospective collars below remain useful for ranks `2,...,d`, but are
no longer needed for the singleton row.  They do not by themselves give
one resident antecedent for the completed factor or preserve the PBBS
whole-fan bank.

## 1. The audited rigid-rotation pieces fail the singleton row

Let the PBBS ground size be `2m+1`, and let `d` be the optimal deadline.
For all sufficiently large `m`,

\[
                         d+1<m-2.
\tag{1.1}
\]

The terminal rigid braid has positive owner-run lengths exactly

\[
                         m-1,\qquad m+1,
\tag{1.2}
\]

and every residual rigid-rotation component has every positive run of
length at least `m-2`.

### Proposition 1.1 (no singleton cell on the audited rigid pieces)

In the eventual range (1.1), the maximal depth-`d` antecedent of the
terminal braid and of every residual component created by the full rigid
rotation contains no singleton source letter.

#### Proof

A singleton `{x}` occurs in a depth-`d` antecedent if and only if `x` has
a positive owner run of length exactly `d+1`.  Equations (1.1)--(1.2) and
the residual lower bound show that no run has that length. \(\square\)

Thus the all-depth PBBS owner-intersection section does not by itself solve
the first literal compiler row on these components.  Its singleton
intersection paths are owner witnesses, not ordinary source singleton
cells.  Proposition 1.1 does not apply to untouched PBBS components; the
one-pile hook component cited above supplies the complete native singleton
bank there.

## 2. One explicit target collar

Fix a ground set `[k]`, owner rank `r`, and depth `d`.  Let

\[
                         \varnothing\ne S\subseteq[k],
                         \qquad s=|S|<r,
\tag{2.1}
\]

and assume

\[
                         r-s\ge d.
\tag{2.2}
\]

Also assume

\[
                         k\ge r+d+2,
\tag{2.2a}
\]

so that the exchanged labels and the two endpoint-screen labels below can
be chosen outside the rank-`r` set `K union S`.  Both hypotheses hold in
the eventual balanced central regime, uniformly for `1<=s<=d`.

Choose a set `K` disjoint from `S` of rank `r-s`, and an ordered partition

\[
                         K=C_1\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}C_d
\tag{2.3}

into nonempty blocks.  Choose `z_j in C_j` and fresh, pairwise distinct
labels `y_1,...,y_d` outside `K union S`, and put

\[
                         C'_j=(C_j-\{z_j\})\cup\{y_j\}.
\tag{2.4}
\]

Choose `u_-,u_+ in S` and fresh distinct `a,b` outside all preceding
sets.  Define the two rank-`s` screens

\[
                         E_-=(S-\{u_-\})\cup\{a\},
                         \qquad
                         E_+=(S-\{u_+\})\cup\{b\}.
\tag{2.5}
\]

For `s=1`, these are simply the singletons `{a}` and `{b}`.

Consider the literal source fragment

\[
 \boxed{
 W_S=(E_-,C_1,\ldots,C_d,S,C'_1,\ldots,C'_d,E_+).}
\tag{2.6}
\]

### Theorem 2.1 (literal low-target collar)

The consecutive length-`(d+1)` unions in (2.6) form the simple rank-`r`
Johnson path

\[
 K\cup E_-,
 \quad K_0\cup S,K_1\cup S,\ldots,K_d\cup S,
 \quad K_d\cup E_+,
\tag{2.7}
\]

where

\[
 K_j=(K-\{z_1,\ldots,z_j\})
          \cup\{y_1,\ldots,y_j\}.
\tag{2.8}
\]

All its immediate lower colours are distinct and all its immediate upper
colours are distinct.  The middle source letter is literally `S`.

When `S={x}`, the coordinate `x` has one positive owner run of length
exactly `d+1` inside the fragment, bounded on both sides by owners omitting
`x`.  Hence `{x}` is a legal singleton compiler cell.

#### Proof

The first owner window in (2.6) is `K union E_-`.  The next is `K union S`;
the screens differ by the one swap `a -> u_-`.  As the start advances
through the primed blocks, the `j`-th owner replaces
`z_1,...,z_j` by `y_1,...,y_j`, giving (2.7)--(2.8).  The final step swaps
`u_+ -> b` and gives `K_d union E_+`.  Every owner has rank

\[
                         (r-s)+s=r,
\]

and every step is a nonloop Johnson step.

Internal owners are separated by the number and identities of the
`y`-labels.  The two endpoints contain respectively the private labels
`a,b`, so the path is simple.

On an internal edge, the lower colour is obtained by deleting
`z_j,y_j` from the corresponding upper colour; its ordered prefix of the
`y`-bank recovers `j`.  The first lower colour contains `K` and omits
`u_-`, while every internal lower colour contains all of `S`; the last
lower colour contains `K_d` and omits `u_+`.  The private endpoint labels
and the changed-core profile separate the two endpoint upper colours from
all internal upper colours and from one another.  Thus both immediate
palettes are simple.

The letter at the displayed middle position is `S`, so it is already a
width-one exact target occurrence.  If `S={x}`, no other letter in (2.6)
contains `x`: the screens are `{a},{b}` and both core banks are disjoint
from `x`.  A single source occurrence belongs to exactly `d+1`
consecutive owner windows, proving the final assertion. \(\square\)

The collar is clipped.  Coordinates in the two endpoint screens and in
the exchanged core banks export boundary ages to the exterior.  Only the
target coordinate in the singleton case has a completely closed local
run statement.

## 3. All singleton collars have a disjoint prospective packing

Specialize to the balanced central regime `k=2r-1`, with
`d=o(r)`.  For a fixed singleton target `{x}`, take the complete stabilizer
orbit of (2.6) over all allowed `K`, partitions, swaps, and endpoint labels.

### Theorem 3.1 (protected singleton collar bank)

For all sufficiently large `r`, one can choose one collar (2.6) for every
coordinate `x in[k]` so that

1. their owner vertices are pairwise distinct;
2. their immediate lower colours are pairwise distinct;
3. their immediate upper colours are pairwise distinct;
4. their union is an incidence path forest of size `O(kd)`; and
5. both all-occurrence exposures of this forest are below `r/3`.

Consequently the bank extends to a simple spanning middle-level
two-factor by the polynomial protected-factor theorem.

#### Proof

For one `x`, choose uniformly from its full stabilizer orbit.  Every
internal owner is then uniform on the rank-`r` owners containing `x`, and
the two endpoint owners are uniform on the corresponding endpoint-screen
orbit.  The immediate lower and upper resources have the analogous
stabilizer-uniform laws.  Every one of these resource orbits has size

\[
                         \exp(\Theta(r)),
\tag{3.1}
\]

uniformly because `d=o(r)`.  One collar uses `O(d)` resources.  After fewer
than `k` collars have been chosen, only `O(kd)` resources are forbidden.
The union bound inside the stabilizer orbit is therefore `o(1)`, so a
resource-disjoint next collar exists.  This proves items 1--4 by induction.

For completeness, choose at each induction step uniformly among the
remaining collars.  Fix a lower-star or upper-star exposure test.  A
collar can hit it at at most four owner/lower occurrences: nonconsecutive
vertices of the internal geodesic have intersection rank at most `r-2` or
the corresponding lower colours have union rank at least `r+1`, and the
two private endpoints add at most two more hits.  For each one of the
`O(d)` resource positions, stabilizer transitivity shows that the chance
of lying in the fixed star is a polynomial factor divided by one of the
exponential orbit sizes in (3.1).  Conditioning on avoidance of the
previous polynomial forbidden bank changes this by a factor `1+o(1)`.
Thus the collar's conditional hit probability is

\[
                         \exp(-\Theta(r)),
\tag{3.2}
\]

uniformly after the polynomial forbidden bank is removed.  The sum over
`k=2r-1` tasks is still exponential-small.  Exposure `r/4` needs at least
`r/16` hit collars, so the adapted binomial moment bound is

\[
                         \exp(-\Theta(r^2)).
\tag{3.3}
\]

There are only `exp(O(r))` stars.  A union bound gives package exposure at
most `r/4`; adding no pre-existing bank gives item 5 (and leaves room for
an `o(r)` protected base).  The polynomial protected-factor extension
theorem applies to the resulting path forest. \(\square\)

The theorem is prospective: it constructs a simple factor containing the
collars.  It does not assert that this factor differs from the canonical
PBBS factor in only `O(kd)` edges, nor that the rest of the fixed PBBS
whole-fan section survives.  Those are rethreading rather than packing
statements.

## 4. The complete subdeadline atlas packs prospectively

Theorem 2.1 applies without change to every target

\[
                         1\le |S|\le d.
\]

The number of all such targets is

\[
 \sum_{s=1}^{d}{k\choose s}
 =\exp(O(d\log k))
 =\exp(o(k))
\tag{4.1}
\]

in the central regime.  Thus there is ample owner count for one literal
collar per low target.  In fact the exposure argument also survives on
this scale.

### Theorem 4.1 (subdeadline protected collar atlas)

In the balanced central regime, for all sufficiently large `r`, one can
choose one collar for every nonempty target `S` with `|S|<=d` so that all
owner, immediate-lower, and immediate-upper resources are separately
pairwise distinct and both all-occurrence exposures are below `r/3`.
Their union extends to a simple spanning middle-level two-factor.

#### Proof

Put

\[
 N_d=\sum_{s=1}^{d}{k\choose s}=\exp(o(r)).
\tag{4.2}
\]

Uniformly for `s<=d=o(r)`, every resource position of an `S`-collar has a
stabilizer orbit of size `exp(Theta(r))`: fixing `S`, or one endpoint
screen of the same sublinear rank, removes only `o(r)` coordinates from a
central binomial orbit.  One collar has `O(d)` resources.  After fewer than
`N_d` choices, the forbidden resource bank has size

\[
                         O(dN_d)=\exp(o(r)).
\tag{4.3}
\]

The collision probability of a random next collar is therefore
`exp(-Theta(r))`, uniformly in the target.  Sequential avoidance gives the
three pairwise-disjoint resource banks.

Fix one lower or upper star.  The geodesic argument from Theorem 3.1 still
bounds one collar's contribution by four.  Its conditional probability of
hitting the star is `exp(-Theta(r))`; conditioning on (4.3) changes this by
`1+o(1)`.  Summed over all `N_d=exp(o(r))` targets, the expected number of
hit collars remains `exp(-Theta(r))`.  The adapted binomial-moment bound
therefore gives

\[
 \Pr(\text{one fixed exposure}\ge r/4)
                         =\exp(-\Omega(r^2)).
\tag{4.4}
\]

There are only `exp(O(r))` stars, so a union bound gives simultaneous
exposure at most `r/4`, and hence below `r/3`.

The protected incidence size is

\[
                         e=O(dN_d)=\exp(o(r)).
\tag{4.5}
\]

In the exact protected-factor criterion, exposure at most `r/3` gives
`D_alpha,D_beta>=2r/3-O(1)` and therefore

\[
 K(D_\alpha),K(D_\beta)=\exp(\Theta(r)),
 \qquad M_r(e)=O(re)=\exp(o(r)).
\]

The criterion applies for all sufficiently large `r`, completing the
path forest to a spanning two-factor. \(\square\)

This is still prospective.  The completion need not retain the fixed PBBS
whole-fan section.  The unresolved relative-rethread row is therefore not
an exposure or owner-capacity problem, even for the complete shallow atlas.

## 5. Consequence and remaining gate

The first necessary row of the relative payload atlas now has an exact
answer.

* The audited braid/residual rigid-rotation pieces fail it: they have no
  minimum-length runs.  No global no-go for untouched PBBS components is
  asserted.
* One prescribed singleton is installed by the explicit source collar
  (2.6).
* All `k` singleton collars coexist in a polynomial protected simple factor.

To use this inside the full construction one must prove a **PBBS-relative
collar rethread**: install the collar bank while puncturing only a controlled
set of whole-fan section edges, repair that named puncture leave by the
complement-paired backup bank, and fuse the collar source histories with
the remaining resident components.  For ranks `2,...,d`, either extend the
same relative packing to the subexponential family (4.1), or use multi-
target block charts instead of one collar per target.

This is a literal programmable-segment formulation.  It does not invoke a
terminal common cap.

## 6. Scope

Proved here:

* canonical singleton failure on the rigid factor;
* an explicit source/owner/q1 collar for every target of rank at most `d`;
* exact run length `d+1` for the singleton screen; and
* a prospective polynomial protected bank for all singleton targets.

Not proved here:

* a palette-preserving rethread of the canonical PBBS factor through these
  collars;
* zero-gap scheduling in the exterior;
* the complete low-rank subexponential packing;
* the middle/deep payload atlas;
* upper-safe opening; or
* `nu(k)<=B(k)+O(1)`.
