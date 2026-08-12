# Common-state carousel fusion preserves owners but has unavoidable upper-seam current

**Date:** 2026-08-07  
**Status:** exact local fusion theorem and proof-safe obstruction.  A
common-state Euler splice preserves the owner multiset and the lower
immediate colour, and it merges components exactly as expected.  It does
not, in general, preserve the upper immediate palette or the complete
upper interval deck.  Without an independent alternative-witness bank,
its damage is linear in the number of fused components and cannot
telescope to (O(1)).

## 1. Carousel normal form

Fix a depth (d), and write (D=d+1).  Every component of the unified
rail queue has a permanent bank (B) and a cyclic order of distinct
toggle labels

\[
 x_0,x_1,\ldots,x_{N-1}.
\]

Its owner row is

\[
 O_t=B\cup\{x_{t-d},x_{t-d+1},\ldots,x_t\},
 \qquad t\in\mathbb Z_N .
\tag{1.1}
\]

Consequently the lower and upper immediate colours on
(O_tO_{t+1}) are

\[
 L_t=B\cup\{x_{t-d+1},\ldots,x_t\},
 \qquad
 U_t=B\cup\{x_{t-d},\ldots,x_{t+1}\}.
\tag{1.2}
\]

The same formulas apply to the ordinary, mixed and pure rail
components.  Their internal source intervals are simple; in particular,
within one component every proper upper interval has a unique occurrence.

The results below need only the window form (1.1), not the special
arithmetic of the unified family.

## 2. Excursions through one common state

Cut (c) cyclic owner rows at occurrences of one enhanced order-(d)
state.  This means that the cuts have the same permanent bank (B) and
the same ordered (d)-toggle context.  Put

\[
 \Sigma=B\cup\{s_1,\ldots,s_d\}.
\tag{2.1}
\]

For component (i), let the owner immediately before the cut and the
owner immediately after the cut be

\[
 E_i^- =\Sigma\cup\{\ell_i\},
 \qquad
E_i^+ =\Sigma\cup\{r_i\}.
\tag{2.2}
\]

Assume all outer labels lie outside (\Sigma), and for every proposed
new seam assume (\ell_i\ne r_{\sigma(i)}).  Pairwise distinct outer
labels are a convenient sufficient condition.

The old seam joins (E_i^-) to (E_i^+).  For a permutation
(\sigma\in S_c), instead join (E_i^-) to
(E_{\sigma(i)}^+).

### Theorem 2.1 (exact common-state re-pairing)

The re-pairing has the following properties.

1. It preserves the owner multiset exactly.
2. It preserves every owner transition away from the (c) selected
   seams.
3. Every new seam is a Johnson edge with lower immediate colour
   (\Sigma).
4. The component permutation of the rethreaded factor is (\sigma).
   In particular, all (c) excursions become one cycle exactly when
   (\sigma) is a (c)-cycle.
5. At the selected seams the old and new upper immediate colours are

   \[
   \boxed{
   \Sigma\cup\{\ell_i,r_i\}
   \quad\longmapsto\quad
   \Sigma\cup\{\ell_i,r_{\sigma(i)}\}.}
   \tag{2.3}
   \]

#### Proof

No owner is inserted or deleted, proving Item 1.  The interiors of the
opened excursions are unchanged, proving Item 2.  At a new seam the two
owners have intersection (\Sigma) and differ by deleting
(\ell_i) and inserting (r_{\sigma(i)}); hence the seam is a Johnson
edge and has lower colour (\Sigma).  Following an excursion indexed by
(i) next enters the excursion indexed by (sigma(i)), so the new
components are exactly the cycles of (sigma).  Taking the union of the
two endpoint owners gives (2.3).  \(\square\)

For (c=2), (2.3) is the exact rectangle

\[
 \begin{array}{c|cc}
   &r_1&r_2\\ \hline
 \ell_1&\Sigma+\ell_1+r_1&\Sigma+\ell_1+r_2\\
 \ell_2&\Sigma+\ell_2+r_1&\Sigma+\ell_2+r_2.
 \end{array}
\tag{2.4}
\]

Thus the two old diagonal colours are replaced by the two other
diagonal colours.  If the four outer labels are distinct and outside
(\Sigma), the old and new named values are disjoint.  The switch is
not upper-palette preserving.

### Corollary 2.2 (lower-rainbow incompatibility)

The common-state construction uses the same lower immediate colour
(\Sigma) at all (c) selected seams, both before and after fusion.
Consequently, for (c>1) it cannot occur inside a factor whose lower
immediate palette is globally simple, unless the formulation explicitly
allows several occurrence copies of the same lower colour.

This is an obstruction to applying the splice only after a literal
lower-rainbow factor has already been selected.

## 3. Exact residence test at the re-paired seams

Fix a coordinate (z), and fix a required minimum length (ho) for
every nonconstant (0)-block and (1)-block in the cyclic owner
incidence word of (z).  In the intended depth-(d) biresident use one
takes (ho=D=d+1).

For excursion (i), let

* (b_i^-(z)) be the incidence bit on its last owner and
  (b_i^+(z)) the incidence bit on its first owner;
* (s_i(z)) be the length of the constant suffix ending at the last
  owner;
* (p_i(z)) be the length of the constant prefix beginning at the first
  owner.

### Proposition 3.1 (necessary and sufficient seam condition)

Assume every block internal to the opened excursions already has length
at least (ho).  The re-paired chronology is (ho)-biresident if and
only if, at every new seam (i\to\sigma(i)), the following conditions
hold for every coordinate (z).

* If (b_i^-(z)=b_{sigma(i)}^+(z)), the new joined block has length

  \[
  s_i(z)+p_{sigma(i)}(z)\ge\rho,
  \tag{3.1}
  \]

  unless that bit is constant on the whole new cycle.
* If (b_i^-(z)\ne b_{sigma(i)}^+(z)), then

  \[
  s_i(z)\ge\rho,
  \qquad
  p_{sigma(i)}(z)\ge\rho.
  \tag{3.2}
  \]

#### Proof

Opening the components can change only the two boundary blocks of each
excursion.  Equal boundary bits concatenate those blocks, giving (3.1).
Unequal boundary bits leave them as two separate maximal blocks, giving
(3.2).  No other maximal block changes.  \(\square\)

In particular, a common order-(d) state is an owner/palette condition,
not by itself a full residence certificate.  Identical protected collars
of length at least (ho) on the relevant sides are a simple sufficient
condition.

## 4. Exact damage to longer upper occurrences

A source interval of length (j\ge D) is the union of

\[
 q=j-d
\tag{4.1}
\]

consecutive owners.  Hence it is represented by a (q)-vertex owner
path, containing (q-1=j-d-1) owner transitions.

Consider the (c) old excursions and a nontrivial (c)-cycle
(sigma).  Suppose

\[
 d+2\le j<\min_i N_i,
\tag{4.2}
\]

where (N_i) is the owner length of excursion (i).  This condition
ensures that a (q)-vertex path meets at most one selected
seam.

### Theorem 4.1 (upper occurrence-current formula)

At source length (j), common-state fusion deletes exactly

\[
 \boxed{c(j-d-1)}
\tag{4.3}
\]

old crossing occurrences and creates exactly the same number of new
crossing occurrences.  Every occurrence not crossing a selected seam is
unchanged.

#### Proof

At one cyclic seam, exactly (q-1) of the (q)-vertex paths cross the
seam: the seam can occupy any of the (q-1) transition positions of the
path.  There is one altered seam for each of the (c) excursions, and
(4.2) makes these occurrence families disjoint.  This gives
(c(q-1)=c(j-d-1)).  The re-pairing is a bijection on path positions, so
the same number of new paths is created.  Paths missing every selected
seam retain the same owner sequence and therefore the same union.
\(\square\)

For (j=d+2), Theorem 4.1 gives exactly (c) lost old upper-(q1)
occurrences, in agreement with (2.3).  For equal excursion length (N),
the total number of deleted proper upper occurrences over all eligible
lengths is

\[
 c\sum_{r=1}^{N-d-2}r
 =c\binom{N-d-1}{2}.
\tag{4.4}

This is (Theta(cN^2)) occurrence damage.

### Corollary 4.2 (named damage under private signatures)

Assume additionally that every old crossing interval has a named value
which occurs nowhere away from its own crossing occurrence.  This holds,
for example, when component-private signatures distinguish the crossing
intervals and each component has its simple proper interval deck.
Then the occurrence losses in (4.3) are genuine named-target losses.

In particular, any fusion of (c) components into one cycle loses at
least (c) named upper-(q1) targets.  No sequence of common-state
re-pairings can telescope this to (O(1)) damage as (c\to\infty).

#### Proof

Under the uniqueness hypothesis a deleted occurrence removes the only
witness of its value.  A final one-cycle re-pairing has no fixed excursion
seam, so all (c) old seams are changed.  Equation (4.3) at
(j=d+2) gives (c) lost named values.  The final loss depends only on
the final seam permutation, not on the sequence of intermediate
transpositions, so intermediate cancellation cannot reduce it.
\(\square\)

Sequential pairwise fusion can reduce a naive count of
(2(c-1)) altered seam occurrences to the (c) seam changes in the
final cyclic permutation.  That is a constant-factor saving, not
bounded total damage.

## 5. Why literal block insertion is not transparent

There is a second elementary fusion attempt: insert one opened source
cycle as a contiguous block at a cut of another.  If an old interval
crossed that cut, its new union is

\[
 \text{old value}\ \cup\ \text{(used universe of the inserted block)}.
\tag{5.1}
\]

Therefore that particular old value survives at the transported
crossing occurrence exactly when the inserted used universe is contained
in the old value.

For a maximal unified carousel the used universe has rank at least
(k-d), whereas the shortest protected upper values have rank (R+1).
In the central regime (d=o(k)) and (R\sim k/2), containment is
impossible.  Thus naive contiguous insertion is not upper-transparent at
the short upper rows.

This does not exclude recreation of the same named value elsewhere, but
it proves that block insertion does not preserve the old witnesses by
transport alone.

## 6. Exact boundary of the fusion problem

The common-state splice solves the purely topological Euler problem:

* the owner multiset is exact;
* internal owner edges and internal upper witnesses are untouched;
* the lower seam colour and Johnson legality are exact;
* residence has the explicit local test (3.1)--(3.2).

It does **not** solve integral Shadow--Braid fusion:

* a repeated common state already conflicts with a simple lower-(q1)
  palette;
* the upper-(q1) seam current is the nonzero rectangle (2.4);
* longer upper occurrence damage is (4.3);
* in the absence of alternative witnesses, final damage is at least
  linear in the number of components and cannot telescope to (O(1)).

Accordingly, a successful all-dimensional fusion theorem needs one of
the following genuinely additional structures.

1. A protected alternative-witness bank covering every old seam target.
2. An upper-transparent absorber whose own internal witnesses realize
   the deleted rectangle and every longer crossing ladder.
3. A correlated component selection in which the old-to-new seam values
   coincide globally and cancel as named targets, not merely as counts.
4. A construction born connected, avoiding post hoc fusion altogether.

The unified fractional component theorem remains valid.  The present
result identifies why its integral rounding cannot be completed by a
bare common-state Euler splice.
