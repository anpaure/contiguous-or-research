# Packing transversal cubes of perfect matchings

## 1. Verdict

Let

\[
 \mathcal V_m=\binom{[2m]}m,
 \qquad W=|\mathcal V_m|=\binom{2m}m.
\]

For a perfect matching `P` of `[2m]`, let

\[
 C(P)=\{S\in\mathcal V_m:|S\cap e|=1\text{ for every }e\in P\}.
\tag{1.1}
\]

The proposed packing of the full cubes `C(P)` is impossible in the
strongest possible sense:

> **Any two transversal cubes intersect.  Hence a vertex-disjoint family
> contains at most one full cube.**

If `c(P,Q)` is the number of alternating-cycle components of the coloured
multigraph `P union Q`, then the exact intersection is

\[
                         |C(P)\cap C(Q)|=2^{c(P,Q)}. \tag{1.2}
\]

Thus the maximum covered fraction is only

\[
 {2^m\over W}
 =\left(\sqrt{\pi m}+o(\sqrt m)\right)2^{-m}=o(1). \tag{1.3}
\]

There is, however, a rigorous subdivided replacement.  For every fixed
`s`, the middle layer has a packing by `s`-dimensional faces of matching
cubes which covers `W-o(W)` vertices.  By diagonalizing the fixed-`s`
theorem, one obtains some function `s(m)->infinity` and a packing by
`s(m)`-cubes covering `W-o(W)`.  No quantitative growth rate for `s(m)` is
obtained.

This is a middle-layer packing theorem only.  It has no RSK-radius ledger,
no global shadow injectivity, and no shift-compatible ordering.

## 2. Exact parameters of the full-cube hypergraph

Let `H_m` be the hypergraph with vertex set `V_m` and one edge `C(P)` for
every perfect matching `P`.

### Proposition 1 (vertices, edges, degrees, and pair codegrees)

`H_m` has

\[
 |V(H_m)|=W,
 \qquad |E(H_m)|=(2m-1)!!={ (2m)!\over2^m m!},
 \qquad |C(P)|=2^m.                                  \tag{2.1}
\]

Every middle set has degree

\[
                              D=m!.                 \tag{2.2}
\]

For `S,T in V_m`, put `a=|S intersection T|`.  Their codegree is

\[
                    d(S,T)=a!(m-a)!={m!\over\binom ma}. \tag{2.3}
\]

In particular, complementary vertices are incidence twins:

\[
                       d(S,S^c)=D.                  \tag{2.4}
\]

#### Proof

The first line is standard counting.  A perfect matching makes `S` a
transversal exactly when every edge crosses the cut `(S,S^c)`.  Such a
matching is a bijection from `S` to `S^c`, giving `m!` choices.

For two sets, partition the ground set into

\[
 A=S\cap T,\quad B=S\setminus T,\quad
 C=T\setminus S,\quad D_0=[2m]\setminus(S\cup T).
\]

Their sizes are `a,m-a,m-a,a`.  An edge crosses both cuts precisely when it
joins `A` to `D_0` or `B` to `C`.  Choose the two bijections independently,
giving `a!(m-a)!`.  QED.

### Proposition 2 (all higher codegrees)

For middle sets `S_1,...,S_j`, give a coordinate `x` its membership
signature

\[
 \sigma(x)=(1_{x\in S_1},\ldots,1_{x\in S_j})
     \in\{0,1\}^j,
\]

and let `n_sigma` be the number of coordinates with signature `sigma`.
Then their common degree is zero unless

\[
                         n_\sigma=n_{\bar\sigma}
                         \quad\text{for every }\sigma. \tag{2.5}
\]

When (2.5) holds, it is exactly

\[
 \prod_{\{\sigma,\bar\sigma\}} n_\sigma!,          \tag{2.6}
\]

where the product takes one representative of each complementary signature
pair.

#### Proof

A matching crosses every cut `S_i` iff each of its edges joins complementary
signatures.  Thus the two signature classes must have equal sizes.  For
each unordered complementary pair, choose an arbitrary bijection between
its two classes.  The choices for different pairs are independent.  QED.

## 3. Exact intersection classification

Colour the edges of `P` red and the edges of `Q` blue.  The multigraph
`P union Q` is two-regular and decomposes into even alternating cycles;
a common edge is regarded as a two-cycle with one edge of each colour.
Let the number of components be `c(P,Q)`.

### Theorem 3 (alternating-cycle intersection law)

\[
                         |C(P)\cap C(Q)|=2^{c(P,Q)}. \tag{3.1}
\]

#### Proof

On one alternating cycle, a set which is a transversal of both matchings
must alternate selected and unselected vertices.  There are exactly two
phases.  Choices on distinct components are independent.  QED.

Consequently, for distinct `P,Q`,

\[
                         2\le |C(P)\cap C(Q)|\le2^{m-1}, \tag{3.2}
\]

while `P=Q` gives `2^m`.  Quotienting middle sets by complementation does
not help: the quotient edges still meet in `2^(c(P,Q)-1)` antipodal pairs.

### Corollary 4 (full-cube packing number)

The matching number of `H_m` is exactly one.  Therefore no nibble theorem
can produce a nontrivial full-cube packing; the obstruction is an actual
pairwise-intersection theorem, not a weak parameter estimate.

## 4. Exact intersection law for subdivided faces

An oriented face of `C(P)` is obtained by fixing the selected endpoint on a
set `I subseteq P` of matching edges.  Its codimension is `|I|`.

Every common transversal of `P,Q` is specified by one phase bit on each
alternating component of `P union Q`.  Fixing the orientation of one edge
specifies the phase of its component.

### Proposition 5 (phase-consistency criterion)

Let `F_P,F_Q` be oriented faces of `C(P),C(Q)`.  Pool their fixed-edge
constraints component by component in `P union Q`.

* If one component receives contradictory phase requirements, then
  `F_P intersection F_Q` is empty.
* Otherwise, if exactly `u` of the `c(P,Q)` components receive at least one
  constraint, then

  \[
                     |F_P\cap F_Q|=2^{c(P,Q)-u}.     \tag{4.1}
  \]

This identifies two different notions of a weakest subdivision.

1. A codimension-one face still intersects every full cube: its single
   constraint merely chooses one phase, leaving `2^(c-1)>=1` common
   transversals.  A face needs at least two suitably conflicting fixed
   orientations to be disjoint from a given full cube.
2. Two codimension-one faces can already be disjoint when their constraints
   impose opposite phases on the same component.  For example, the two
   opposite halves of one `C(P)` are disjoint.

Thus codimension one is the first **uniform** subdivision for which
pairwise-disjoint objects can exist, but it is not currently the first one
for which an almost-perfect packing theorem is available.

## 5. The `s`-face hypergraph

Fix `1<=s<m`, and put `r=m-s`.  A distinct `s`-dimensional matching face
has the canonical form

\[
 F(U,V;R)=\{U\cup X:X\text{ chooses one endpoint of every edge of }R\},
 \tag{5.1}
\]

where

* `U,V` are disjoint `r`-sets;
* `R` is a perfect matching on the remaining `2s` coordinates.

Every member includes `U`, excludes `V`, and has rank `m`.  The face has
`2^s` vertices.  It is a codimension-`r` face of any full matching obtained
by extending `R` with a bijection from `U` to `V`.  The extension is not
part of the distinct face data.

Let `F_(m,s)` be the simple hypergraph of all faces (5.1).

### Theorem 6 (exact face parameters)

`F_(m,s)` is `2^s`-uniform and exactly regular.  It has

\[
 |E(F_{m,s})|
 ={(2m)!\over (m-s)!^2\,2^s s!},                   \tag{5.2}
\]

and vertex degree

\[
 D_s=\binom ms^2s!.                                  \tag{5.3}
\]

For two middle sets at Johnson distance

\[
 j=|S\setminus T|=m-|S\cap T|,
\]

their codegree is zero for `j>s`, and for `0<=j<=s` is

\[
 d_s(j)=\binom{m-j}{s-j}^2j!(s-j)!.                 \tag{5.4}
\]

For distinct vertices,

\[
 {\Delta_2(F_{m,s})\over D_s}={s\over m^2}.          \tag{5.5}
\]

#### Proof

Count (5.1) by choosing ordered fixed sets `U,V` and then a matching on the
remaining coordinates, giving (5.2).  Alternatively, for a fixed middle
set `S`, choose the `s` varying coordinates in `S`, the `s` varying
coordinates in `S^c`, and a bijection between them.  This gives (5.3).

For `S,T` at distance `j`, a common face must fix `r` coordinates selected
by both and `r` coordinates excluded by both.  Choose these in
`binom(m-j,r)^2=binom(m-j,s-j)^2` ways.  Of the remaining coordinates, the
two symmetric-difference `j`-sets must be matched to each other, and the
remaining two `(s-j)`-sets must be matched to each other.  This gives
`j!(s-j)!` choices and proves (5.4).

Dividing by (5.3),

\[
 {d_s(j)\over D_s}
 ={\binom sj(j!)^2\over (m)_{\underline j}^2}.       \tag{5.6}
\]

For `j>=1`, divide (5.6) by its value `s/m^2` at `j=1`:

\[
 {d_s(j)/D_s\over s/m^2}
 ={(s-1)_{\underline{j-1}}j!
   \over (m-1)_{\underline{j-1}}^2}\le1.            \tag{5.7}
\]

Indeed, each numerator factor is bounded by one of the two denominator
falling factorials when `j<=s<m`.  Thus the maximum is attained at `j=1`.
QED.

## 6. A rigorous near-packing after substantial subdivision

### Theorem 7 (fixed-dimensional face packing)

For every fixed `s>=1`, `F_(m,s)` has a matching covering

\[
                         (1-o(1))W                 \tag{6.1}
\]

middle vertices as `m->infinity`.

#### Proof

For fixed `s`, the uniformity `2^s` is fixed, `D_s->infinity`, every degree
is exactly `D_s`, and (5.5) gives

\[
                       \Delta_2/D_s=s/m^2=o(1).
\]

The standard Pippenger--Frankl--Rodl almost-perfect matching theorem for
fixed-uniformity nearly regular hypergraphs therefore applies.  QED.

### Corollary 8 (an unbounded but ineffective dimension)

There exists a function

\[
                         s(m)\longrightarrow\infty \tag{6.2}
\]

and matchings in `F_(m,s(m))` covering `W-o(W)` middle vertices.

#### Proof

For each integer `h`, apply Theorem 7 with fixed `s=h` and requested
uncovered fraction at most `1/h`.  Let `M_h` be a threshold after which this
holds, making the thresholds strictly increasing and imposing `M_h>=h`.
Define `s(m)` to be the
largest `h` with `M_h<=m`.  Then `s(m)->infinity`, while the uncovered
fraction is at most `1/s(m)=o(1)`.  QED.

This diagonal statement supplies no usable lower bound on `s(m)`.  It
cannot be substituted for a required depth such as
`Theta(sqrt(m log m))`.

## 7. Why codimension-one packing remains unresolved

The geometrically minimal uniform subdivision has `s=m-1`.  Its exact
parameters are

\[
 k=2^{m-1},\qquad D_{m-1}=m\,m!,\qquad
 {\Delta_2\over D_{m-1}}={m-1\over m^2}=\Theta(1/m). \tag{7.1}
\]

The small relative pair codegree does not license a classical nibble:

* Pippenger--Frankl--Rodl and Pippenger--Spencer fix `k` before taking the
  asymptotic limit;
* quantitative pseudorandom/conflict-free results in the present handoff
  likewise require fixed uniformity or a fixed power codegree saving;
* the growing-uniformity Alon--Bollobas--Kim--Vu condition includes
  `e^(2k)Delta_2=o(D/log D)`, whose left-to-right ratio here contains
  `e^(2^m)log(D)/m` and diverges overwhelmingly;
* pair-codegree data alone cannot imply a matching, as projective-plane
  hypergraphs have relative codegree tending to zero but matching number
  one.

No audited black box therefore proves an almost-perfect matching of the
half-face hypergraph.  Conversely, the full-cube alternating-cycle
obstruction no longer applies after orientation fixing, so the calculation
does not prove such a packing impossible.  This growing-dimensional case
remains open.

## 8. Does the subdivided packing solve shadow diversity?

No.  The fixed-`s` and diagonal packings are useful structural facts, but
they fall short in three independent ways.

1. **No radius ledger.**  A face is a physical middle-layer coordinate
   cube, but its vertices need not share one standard binary-RSK radius.
   The matching theorem does not allocate the exact counts
   `N_d-N_(d+1)` required at each radius.
2. **No shadow resolution.**  It controls disjoint middle vertices only.
   Lower and upper `q`-faces from different selected cubes may collide.
3. **No quantitative depth.**  The diagonal `s(m)` may grow arbitrarily
   slowly, whereas negligible literal tails require a prescribed growing
   band.

It also does not automatically prove useful diversity of the **active**
pair systems.  A codimension-`m-s` face remembers only its matching `R` on
the `2s` varying coordinates; the matching between fixed `U` and `V` is
invisible and can be chosen in `(m-s)!` ways.  Thus counting many full
matching extensions can exaggerate geometric diversity.

For codimension one, by contrast, almost every pair remains active, so a
hypothetical near-packing would genuinely mix near-complete pair systems.
That is exactly the quantitatively unresolved regime.

## 9. Finite audit

`scratch/check_transversal_cube_packing.py` independently enumerates all
perfect matchings through `m=5` and checks:

* the alternating-cycle intersection formula for every pair of matchings;
* every full-cube vertex degree and pair codegree;
* the number, degree, and complete pair-codegree table of every distinct
  `s`-face hypergraph, `1<=s<m`;
* the exact maximum ratio `Delta_2/D_s=s/m^2`.

At `m=5` it checks 945 matchings and 446,985 matching pairs.  The finite
calculation audits the formulae; the packing theorem itself is the
fixed-uniformity theorem applied to the proved parameters.
