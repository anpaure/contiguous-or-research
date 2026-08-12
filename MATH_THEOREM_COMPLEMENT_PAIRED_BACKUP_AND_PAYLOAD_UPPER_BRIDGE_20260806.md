# Complement-paired polynomial backups and the exact payload--upper bridge

**Date:** 2026-08-06  
**Method:** Boolean complementation, explicit Johnson geodesics, random
permutation packing, and literal derivative algebra; no computation or
search  
**Status:** unconditional polynomial paired-backup theorem and an exact
scope theorem for the bottom-to-PBBS interface.  A polynomial upper leave
can be repaired by paths which simultaneously restore the complementary
owner-intersection targets.  Payload thinning never changes the long
source deck when the owner chronology is fixed.  A local complement-closed
macro does not, however, export complements of the deep payload values.
The remaining bridge is one correlated PBBS-relative payload macroization,
not a terminal common cap.

## 1. Long source intervals are determined by the owner chronology

Let `A=(A_i)` be a cyclic source word and put

\[
                         T_i=\bigcup_{h=0}^{d}A_{i+h}.
\tag{1.1}
\]

No rank or residence assumption is needed in this section.

### Theorem 1.1 (long-deck rigidity)

For every `q>=0` for which the displayed cyclic interval is proper,

\[
 \boxed{
 \bigcup_{p=i}^{i+d+q}A_p
       =\bigcup_{j=0}^{q}T_{i+j}.}
\tag{1.2}
\]

Consequently, if `A` and `A'` have the same labelled owner chronology
`T`, then their occurrence-labelled OR values agree on every corresponding
source interval of width at least `d+1`.  Thinning source letters while
retaining `D^d A=T` can change the strict-lower deck, but cannot change any
owner-union witness.

#### Proof

The right side of (1.2) is

\[
 \bigcup_{j=0}^{q}\bigcup_{h=0}^{d}A_{i+j+h}.
\]

The sums `j+h` attain every integer from `0` through `d+q`, so this is the
left side.  Applying the identity to two antecedents of the same labelled
`T` proves the last assertion. \(\square\)

This is the exact positive interface for a bottom payload atlas.  Once the
atlas is installed by owner-invisible thinning **inside the same owner
chronology** as the protected upper paths, no upper target has to be
recompiled and no source homotopy is needed.

## 2. One upper path has an exact complementary lower path

Work in the balanced middle-level incidence graph on a ground set

\[
                         [n],\qquad n=2R-1,
\]

with lower shore `binom([n],R-1)` and owner shore
`binom([n],R)`.  Fix a proper upper target

\[
                         Z\in{[n]\choose R+s},
                         \qquad 2\le s\le R-2,
\tag{2.1}
\]

and put

\[
                         S=[n]\setminus Z,
                         \qquad |S|=R-s-1.
\tag{2.2}
\]

Choose a disjoint decomposition

\[
 Z=C\mathbin{\dot\cup}A\mathbin{\dot\cup}B,
 \qquad |C|=R-s,\qquad |A|=|B|=s,
\tag{2.3}
\]

with orders `A=(a_1,...,a_s)` and `B=(b_1,...,b_s)`.  Define

\[
 V_i=C\cup\{b_1,\ldots,b_i\}
          \cup\{a_{i+1},\ldots,a_s\},
 \qquad 0\le i\le s,
\tag{2.4}
\]

and the internal facets

\[
 L_i=V_i\cap V_{i+1}
    =C\cup\{b_1,\ldots,b_i\}
          \cup\{a_{i+2},\ldots,a_s\},
 \qquad 0\le i<s.
\tag{2.5}
\]

Choose `c in C` and add endpoint facets

\[
                         L_-=V_0-\{c\},
                         \qquad L_+=V_s-\{c\}.
\tag{2.6}
\]

### Theorem 2.1 (complement-paired whiskered geodesic)

The incidence path

\[
 L_- -V_0-L_0-V_1-\cdots-L_{s-1}-V_s-L_+
\tag{2.7}
\]

is simple and its owner union is `Z`.  Its complement is the simple
incidence path

\[
 \overline{L_-}-\overline{V_0}-\overline{L_0}
 -\overline{V_1}-\cdots-
 \overline{V_s}-\overline{L_+},
\tag{2.8}
\]

whose owner vertices are the rank-`R` sets

\[
 \overline{L_-},\overline{L_0},\ldots,
 \overline{L_{s-1}},\overline{L_+}
\]

and whose owner intersection is exactly `S`.  The two incidence paths are
resource-disjoint.

#### Proof

The `V_i` form the standard monotone Johnson geodesic, so their union is
`Z`.  Consecutive lower vertices in the sequence

\[
                         L_-,L_0,\ldots,L_{s-1},L_+
\tag{2.9}
\]

are distinct facets of the intervening owner.  At the first owner they
omit respectively `c` and `a_1`; at an internal owner `V_i` they omit
respectively `b_i` and `a_{i+1}`; at the last owner they omit respectively
`b_s` and `c`.  Hence the sequence (2.7) is an incidence path and

\[
                         L_-\cup L_0=V_0,
\]

\[
                         L_{i-1}\cup L_i=V_i
                         \quad(1\le i<s),
\]

\[
                         L_{s-1}\cup L_+=V_s.
\tag{2.10}
\]

It follows that

\[
 L_-\cup L_0\cup\cdots\cup L_{s-1}\cup L_+=Z.
\tag{2.11}
\]

Complementation reverses incidence and swaps the two middle shores.  Thus
(2.8) is an incidence path, and De Morgan's law with (2.11) gives

\[
 \bigcap_{L\in\{L_-,L_0,\ldots,L_{s-1},L_+\}}
       \overline L
 =\overline Z=S.
\tag{2.12}
\]

All displayed vertices in either path are distinct from their nonadjacent
mates: the ordered `A/B` profile recovers the index, while the endpoint
facets are the only ones missing `c`.  Finally every original vertex is a
subset of `Z`, whereas every complementary vertex contains the nonempty
set `S=[n]-Z`.  Equality across the two paths is impossible.  This proves
simplicity and resource disjointness. \(\square\)

The endpoint facets in (2.6) are load-bearing.  Complementing only the
internal edge facets need not give intersection `S`, because a coordinate
appearing only in an endpoint owner can be absent from every internal
facet.  The two whiskers make the union identity (2.11) exact.

## 3. Polynomially many paired packages pack simultaneously

Use the exposure convention for an incidence forest `P`:

\[
 \alpha(P)=\max_{x\in{[n]\choose R-1}}
      |\{U\in V(P)\cap{[n]\choose R}:x\subset U\}|,
\tag{3.1}
\]

\[
 \beta(P)=\max_{U\in{[n]\choose R}}
      |\{x\in V(P)\cap{[n]\choose R-1}:x\subset U\}|.
\tag{3.2}
\]

### Theorem 3.1 (polynomial complement-paired backup packing)

Let `P_0` be a protected incidence path forest with

\[
 |V(P_0)|=O(M),\qquad \alpha(P_0),\beta(P_0)=o(R).
\tag{3.3}
\]

For every `2<=s<=R-2`, let `D_s` be a family of proper upper targets of
rank `R+s`, with

\[
                         |D_s|\le M,
                         \qquad M=O(R^{3/2}).
\tag{3.4}
\]

For all sufficiently large `R`, one may choose for every target `Z` one
package consisting of (2.7) and (2.8) such that

1. all packages are mutually vertex-disjoint and avoid `P_0`;
2. their union with `P_0` is an incidence path forest;
3. every `Z` has a literal owner-union witness;
4. every `S=[n]-Z` has a literal owner-intersection witness;
5. the combined exposure is at most `R/3` on both shores; and
6. the total protected incidence size is `O(MR^2)`.

Consequently the entire paired bank extends to a simple spanning
two-factor by the polynomial protected-factor theorem.

#### Proof

Choose targets in increasing order of `s`.  Before a target in stratum
`s` is chosen, the used owner and lower-vertex banks have size at most

\[
                         C_0M(s+1)^2
\tag{3.5}
\]

for an absolute `C_0`: one package in stratum `t` has `O(t)` vertices on
each shore, and there are at most `M` targets at every preceding stratum.

Choose a uniformly random ordered decomposition (2.3), orders of `A,B`,
and a uniform `c in C`.  By symmetry every `V_i` is uniform among the
rank-`R` subsets of `Z`, and every member of (2.9) is uniform among the
rank-`(R-1)` subsets of `Z`.  A collision with the old owner bank can occur
either at a `V_i`, or when the complement of one of the `L`-vertices is an
old owner.  A collision with the old lower bank has the two symmetric
forms.  Hence, using (3.5), the collision probability is at most

\[
 C_1M(s+1)^2(2s+3)
 \left(
 {1\over {R+s\choose R}}+
 {1\over {R+s\choose R-1}}
 \right).
\tag{3.6}
\]

At `s=2` this is `O(M/R^2)=O(R^{-1/2})`; for every larger `s` it is
smaller after increasing the absolute constant.  Thus (3.6) is `o(1)`
uniformly, and an avoiding package always exists.  Selecting uniformly
from the avoiding packages gives the sequential random process used below.

Fix a lower vertex `x`.  The probability that an original owner `V_i`
contains `x` is bounded, after summing over the `s+1` positions, by

\[
                         {(s+1)^2\over {R+s\choose R}}.
\tag{3.7}
\]

A complementary owner `overline L` contains `x` exactly when
`L subseteq overline x`.  The rank-`R` set `overline x` has only `R`
rank-`(R-1)` facets, so the corresponding probability is at most

\[
                         {(s+2)R\over {R+s\choose R-1}}.
\tag{3.8}
\]

The same two bounds, in the opposite order, control the probability that
the package has a lower vertex contained in a fixed owner.  Conditioning
on the preceding avoidance changes them by the factor `1+o(1)`.

Summing (3.7)--(3.8) over at most `M` targets in every stratum gives

\[
 \mu_\alpha,\mu_\beta
 \le(1+o(1))M\sum_{s=2}^{R-2}
 \left(
 {(s+1)^2\over {R+s\choose R}}+
 {(s+2)R\over {R+s\choose R-1}}
 \right)
 =O(M/R^2)=o(1).
\tag{3.9}
\]

One package contributes at most four units to either exposure.  For the
original geodesic this is the usual fact that nonconsecutive `V`-vertices
intersect in rank at most `R-2`, and nonconsecutive `L`-vertices have union
rank at least `R+1`.  The complementary half has the same statement.  Thus
exposure `R/4` requires at least `R/16` package hits.  The adapted
exponential-moment bound gives, for one fixed star,

\[
 \Pr(\text{package exposure}\ge R/4)
 \le\left({16e\,o(1)\over R}\right)^{R/16}
 =\exp(-\Omega(R\log R)).
\tag{3.10}
\]

There are fewer than `2^(2R)` stars on either shore.  A union bound and
(3.3) give simultaneous total exposures at most `R/3` for all large `R`.

Each package has `4s+4` incidence edges.  Summing over `M` targets in each
stratum gives `O(MR^2)` edges.  The selected objects are disjoint paths,
so their union with `P_0` is a path forest.  The polynomial protected-factor
theorem now gives the simple spanning two-factor.  The target identities
are Theorem 2.1. \(\square\)

The constant-per-stratum hypothesis in Theorem 3.1 is stronger than the
inverse-fan application needs.  The same orbit proof handles the linearly
growing rank profile produced by a polynomial puncture bank.

### Theorem 3.2 (inverse-fan profile packing)

Let `p=O(R^(3/2))`, let `P_0` be a protected incidence path forest with

\[
 |V(P_0)|=O(p),\qquad \alpha(P_0),\beta(P_0)=o(R),
\tag{3.11}
\]

and suppose that

\[
                         |\mathcal D_s|\le p s
             \qquad(2\le s\le R-2).
\tag{3.12}
\]

Then all targets in all the `D_s` admit mutually vertex-disjoint paired
packages of Theorem 2.1 which avoid `P_0`, have combined exposure at most
`R/3` on both shores, and have total protected incidence size

\[
                         O(pR^3).
\tag{3.13}
\]

Consequently their union with `P_0` extends to a simple spanning
middle-level two-factor.

#### Proof

Before processing a target in stratum `s`, the number of previously used
vertices on either shore is at most

\[
 O(p)+\sum_{t=2}^{s-1}O(t)|\mathcal D_t|
 =O\!\left(p\sum_{t=1}^{s}t^2\right)
 =O(ps^3).
\tag{3.14}
\]

Repeating the collision calculation (3.6), now with (3.14), bounds the
failure probability for one random package by

\[
 Cp s^3(2s+3)
 \left(
 {1\over {R+s\choose R}}+
 {1\over {R+s\choose R-1}}
 \right).
\tag{3.15}
\]

At `s=2` this is `O(p/R^2)=O(R^(-1/2))`.  The elementary consecutive-ratio
comparison for the two binomial denominators shows that, after enlarging
the absolute constant for the first few `s`, every later term is no
larger.  Hence (3.15) is `o(1)` uniformly, so sequential avoidance works.

For one fixed lower or upper star, (3.7)--(3.8) and (3.12) give expected
package exposure

\[
 \begin{aligned}
 \mu
 &\le(1+o(1))p\sum_{s=2}^{R-2}s
 \left(
 {(s+1)^2\over {R+s\choose R}}+
 {(s+2)R\over {R+s\choose R-1}}
 \right)\\
 &=O(p/R^2)=o(1).
 \end{aligned}
\tag{3.16}
\]

The first term `s=2` dominates up to an absolute factor, again by the
consecutive-ratio comparison.  One package contributes at most four to a
star.  The exponential-moment and union-bound argument in (3.10) therefore
gives simultaneous package exposure at most `R/4` on both shores.
Together with (3.11), this is at most `R/3` for all large `R`.

Finally one stratum-`s` package has `O(s)` incidences, so

\[
 \sum_{s=2}^{R-2}O(s)|\mathcal D_s|
 \le O(p)\sum_{s=2}^{R-2}s^2
 =O(pR^3).
\]

This is polynomial.  The polynomial protected-factor theorem completes
the selected path forest. \(\square\)

## 4. PBBS polynomial-leave consequence

The fixed PBBS whole-fan section pairs every lower target `S` with the
proper upper target `[n]-S`.  Puncturing `p=O(R)` selected section edges
creates, after the already transported local rows are removed, at most
`O(R^3)` named paired casualties and at most `O(R^{3/2})` targets in one
upper excess-rank stratum.  Apply Theorem 3.1 with those upper targets.

### Corollary 4.1 (one bank repairs both sides of the polynomial puncture)

The unresolved PBBS whole-fan puncture leave has a polynomial protected
replacement forest in which

* every lost proper-upper value has a new union path;
* the same package has a complementary intersection path for the paired
  lower value;
* all paths are resource-disjoint, have sub-half exposure, and coexist in
  one simple spanning two-factor.

Thus the set-theoretic lower/upper occurrence repair of the polynomial
PBBS puncture is no longer a separate gate.  What remains at that bank is
source residence/history and fusion with the lower compiler, not owner or
target supply.

The conclusion is deliberately polynomial.  It does not select one such
package for every member of the exponentially large strict-lower ideal.
The fixed PBBS whole-fan bank remains the exponential baseline; the paired
packages repair only its named polynomial puncture leave.

### Corollary 4.2 (deadline-scale puncture bank)

Let `E_0` contain `p=O(R^(3/2))` selected section edges.  At upper excess
rank `s`, the exact inverse-fan enumeration gives at most `ps` distinct
named casualties.  Hence, against any additional protected forest of size
`O(p)` and exposure `o(R)`, Theorem 3.2 supplies one paired replacement
bank for the entire puncture leave.

In particular, a relative rethread which installs a deadline-scale
`O(Rd)=O(R^(3/2))` literal collar bank and changes only a constant number
of old selected incidences per collar incidence has no remaining
set-theoretic lower/upper backup obstruction.  Proving that **local-damage
relative rethread** is a separate hypothesis; a generic matching repair
whose Hamming radius is a higher polynomial is not covered by this
corollary.

## 5. Exact scope of complement-closed bottom supermacros

There is a useful even-dimensional identity and a sharp limitation.

Let `k=2r` and let `T_0,...,T_q` be rank-`r` owners.  Then their complements
are again rank-`r` owners and

\[
 \boxed{
 \bigcup_{j=0}^{q}\overline{T_j}
       =[k]\setminus\bigcap_{j=0}^{q}T_j.}
\tag{5.1}
\]

Hence an exact complement-reflected chronology turns an all-depth owner-
intersection bank into the complete paired upper bank.  At depths
`q<=d`, this automatically dualizes the canonical top-`d` fan of a
resident macro.

It does **not** dualize a deep value installed only by thinning payload
letters.  The thinning leaves the owners unchanged, so a value which was
not an owner intersection before thinning does not become one afterward.
There is also a rank-width obstruction: if `S` has rank `s<r-d`, then its
complement has rank `2r-s`, while a path of `ell` rank-`r` Johnson owners
has union rank at most `r+ell-1`.  Therefore any owner path witnessing
`[k]-S` has

\[
                         \ell\ge r-s+1>d+1.
\tag{5.2}

No one deadline-sized macro, nor its deadline-sized exact dual, can export
that witness.

There are two further resource warnings.

1. Pairing a **complete** owner factor with its complement doubles every
   owner.  A complement-closed supermacro factor must choose one
   representative from every complement pair and include its dual in the
   same selected superedge.
2. The depth-`d` lower projection of the complemented owner path is

   \[
      \bigcap_{h=0}^{d}\overline{T_{i+h}}
       =\overline{\bigcup_{h=0}^{d}T_{i+h}},
   \tag{5.3}
   \]

   not the set complement of the old rank-`(r-d)` lower state.  Its lower
   resource collisions must therefore be priced explicitly; ordinary
   owner complement closure does not preserve the old lower macro edge.

For odd `k=2R-1`, pointwise complement closure has the more basic rank
mismatch: a rank-`R` owner complements to rank `R-1`.  Theorem 2.1 is the
correct balanced-incidence replacement.  It adds endpoint facets and uses
two incidence paths; there is no same-shape one-path dual macro.

## 6. The strongest proof-safe bottom-to-PBBS bridge

Combine Theorem 1.1, Theorem 3.1, the PBBS whole-fan section, and terminal
compiler functoriality.

### Theorem 6.1 (protected payload overlay, sharpened form)

Suppose one owner chronology and one resident antecedent are constructed
with the following properties.

1. Outside a polynomial puncture bank, the chronology retains the fixed
   PBBS whole-fan section.
2. The puncture bank is repaired by the paired packages of Theorem 3.1.
3. Its rank-`(r-d)` projection has separated free blocks and an exact named
   payload atlas for every deeper strict-lower target, while the canonical
   top-`d` cells are retained outside those blocks.
4. Every later source rethread carries the selected lower cells by literal
   occurrence injections, and component fusion uses palette-safe common
   histories.
5. The final opening preserves one chosen occurrence of every named upper
   path.

Then the terminal word has every strict-lower, middle, and proper-upper
target.  No terminal two-coordinate common cap and no canonical deep
remote-block selector are needed.

#### Proof

The top-`d` cells together with the payload atlas give a literal matching
of every strict-lower target.  Item 4 and terminal compiler functoriality
transport that matching injectively to the final source word.

The unpunctured whole-fan section gives the exponential lower-intersection
and complementary upper-union baseline.  Theorem 3.1 repairs both named
shores of the polynomial puncture.  Payload thinning retains the same owner
chronology, so Theorem 1.1 says it cannot alter any of these upper owner-
union values.  Item 5 carries them through the linear opening.  The owner
factor supplies the middle layer.  Hence all nonempty targets occur.  The
terminal cap has no remaining target-coverage job. \(\square\)

## 7. Exact remaining gate

The theorem above identifies the strongest valid interface, but does not
construct it.  The missing statement is now:

> **PBBS-relative protected payload macroization.**  In the same resident
> owner factor which carries the whole-fan section and the polynomial paired
> repair bank, choose a rank-`(r-d)` duplicate-block projection, round its
> balanced `2/3` doublets without touching the protected incidence bank,
> and fill the free copies by a named interval-union atlas for every deep
> lower target.  Export palette-safe common-history ports and an upper-safe
> opening.

This is strictly sharper than either previous standalone gate.

* It is not the canonical PBBS remote selector: the deep values may be
  manufactured in the bottom free-copy payloads.
* It is not ordinary balanced-doublet rounding: the rounding is relative
  to an exponentially structured PBBS section and a polynomial paired
  bank.
* It is not a source homotopy between arbitrary owner factors.  Theorem
  1.1 is positive only after the two constructions share one labelled owner
  chronology; equality of the owner **set** does not suffice.
* It is not a terminal common-cap theorem: once the named payload atlas is
  present, compiler transport is functorial.

The local complement-closed supermacro does close the top-`d` dual rows,
but (5.2) proves that it cannot replace the all-depth PBBS baseline.  The
next proof must therefore build the payload macroization relative to that
baseline, rather than trying to reconstruct the baseline after an arbitrary
bottom rounding.

## 8. Dependencies and scope

Used as inputs:

* the fixed PBBS whole-fan and polynomial puncture-leave theorems;
* the polynomial protected-factor extension theorem;
* terminal compiler functoriality and common-history source fusion; and
* the exact bottom block payload criterion.

Not proved here:

* balanced-doublet integral rounding;
* the PBBS-relative payload atlas;
* a resident antecedent for the unprotected factor completion;
* upper-safe linear opening; or
* `nu(k)<=B(k)+O(1)`.
