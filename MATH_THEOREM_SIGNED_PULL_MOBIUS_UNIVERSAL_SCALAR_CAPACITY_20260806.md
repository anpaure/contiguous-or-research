# Signed pull phases realize every scalar interval pattern at triangular depth

## Status

The one-polarity pull language consists exactly of downsets in the cyclic
interval poset, so an arbitrary dense cluster need not be one-phase
toggleable.  This note proves that the obstruction disappears at the
**scalar multiplicity** level when two phases are allowed.

For the shortest upper-rich ring, and all sufficiently large dimensions,
every zero-one pattern on the complete proper-interval bank has Möbius
positive and negative mass at most the available core size.  Hence every
such pattern is a difference of two legal pull phases.

This does not realize arbitrary named target substitutions: scalar
cancellation can pair different omitted coordinates.  The remaining gate is
literal coordinatewise cancellation plus the upper/residence/compiler
tickets.

## 1. Cyclic interval coordinates

Let the ring period be `L`, and let

\[
 \mathcal I=\{(i,\ell):i\in\mathbb Z/L\mathbb Z,
                         1\le\ell\le d\}
\tag{1.1}
\]

denote the nonempty cyclic intervals of length at most `d`.  Thus

\[
                         |\mathcal I|=Ld.                 \tag{1.2}
\]

Let

\[
                         z_{i,\ell}\in\{0,1\}             \tag{1.3}
\]

be an arbitrary scalar change pattern, and extend it by

\[
                         z_{i,d+1}=z_{i,d+2}=0.            \tag{1.4}
\]

The interval-poset Möbius coefficient at `(i,ell)` is

\[
 a_{i,\ell}
 =z_{i,\ell}-z_{i-1,\ell+1}-z_{i,\ell+1}
                   +z_{i-1,\ell+2}.                       \tag{1.5}
\]

This is formula (3.5) of
`MATH_THEOREM_PULL_RUN_TOGGLE_MOBIUS_AND_DENSE_CLUSTER_OBSTRUCTION_20260806.md`
in cyclic start/length coordinates.

Write

\[
 A^+=\sum_{i,\ell}(a_{i,\ell})_+,
 \qquad
 A^-=\sum_{i,\ell}(-a_{i,\ell})_+.                       \tag{1.6}
\]

These are exactly the numbers of one-run core coordinates required in the
positive and negative pull phases.

## 2. A universal total-variation bound

### Theorem 2.1 (signed Möbius mass)

Every zero-one pattern (1.3) satisfies

\[
 \boxed{
                         A^+\le Ld+{L\over2},
                         \qquad
                         A^-\le Ld+{L\over2}.}
\tag{2.1}
\]

#### Proof

For one cell put

\[
 p=z_{i,\ell}+z_{i-1,\ell+2},
 \qquad
 q=z_{i-1,\ell+1}+z_{i,\ell+1}.                          \tag{2.2}
\]

Then `a=p-q`, with `p,q in {0,1,2}`.  Directly,

\[
 (p-q)_+\le1+{p-q\over2},
 \qquad
 (q-p)_+\le1-{p-q\over2}.                               \tag{2.3}
\]

Indeed the only possible differences are `-2,-1,0,1,2`.

Let

\[
                         Z_\ell=\sum_i z_{i,\ell}.         \tag{2.4}
\]

Summing (1.5) first over the cyclic start gives

\[
 \sum_i a_{i,\ell}=Z_\ell-2Z_{\ell+1}+Z_{\ell+2}.        \tag{2.5}
\]

Summing over `ell=1,...,d` telescopes to

\[
                         \sum_{i,\ell}a_{i,\ell}=Z_1-Z_2. \tag{2.6}
\]

Since `0<=Z_1,Z_2<=L`, equations (2.3) and (2.6) give

\[
 \begin{aligned}
 A^+&\le Ld+\frac12(Z_1-Z_2)\le Ld+\frac L2,\\
 A^-&\le Ld-\frac12(Z_1-Z_2)\le Ld+\frac L2.
 \end{aligned}                                           \tag{2.7}
\]

This proves (2.1).  \(\square\)

The bound is of the correct order.  Alternating local zero-one patterns can
produce Möbius coefficients of magnitude two on a positive density of
cells, so no `o(Ld)` universal estimate is possible.

## 3. Exact two-phase scalar realization

Let the all-high source ring have core size `c`.  The exact signed pull
criterion says a profile is the difference of two legal one-run phases if

\[
                         A^+\le c,
                         \qquad A^-\le c.                 \tag{3.1}
\]

### Corollary 3.1 (universal scalar pull pair)

If

\[
                         Ld+{L\over2}\le c,               \tag{3.2}
\]

then every zero-one scalar pattern on `mathcal I` is the exact multiplicity
difference of two legal pull phases.

#### Proof

Apply Theorem 2.1 and the signed Möbius criterion.  Use one distinct core
coordinate for every unit of positive or negative coefficient, assigning
its omission run to the corresponding interval.  \(\square\)

For the shortest upper-rich ring,

\[
                         L=d+3,
                         \qquad c=r-d-1.                  \tag{3.3}
\]

Condition (3.2) becomes

\[
                         r\ge d^2+{9\over2}d+{5\over2}.   \tag{3.4}
\]

At the optimal triangular depth on `2r-1` coordinates,

\[
                         d^2=\left({\pi\over4}+o(1)\right)r.
\tag{3.5}
\]

Since `pi/4<1`, inequality (3.4) holds for all sufficiently large `r`.
Therefore:

### Theorem 3.2 (triangular-depth universal scalar clock)

For all sufficiently large `r`, every zero-one scalar pattern on all
proper intervals of a shortest upper-rich ring is a difference of two legal
one-run pull phases.

## 4. Exact limitation

Theorem 3.2 is not a literal named-target absorber.  If one positive phase
omits coordinate `x` and the negative phase omits coordinate `y`, equal
scalar omission counts do not imply equal set-valued interval unions.
Thus a cell with scalar difference zero may still change from a value
missing `y` to a value missing `x`.

The literal support nevertheless has a simple necessary property.  In
fact the property is not special to pull runs: it holds for every pair of
equal-length set words.

### Theorem 4.1 (universal singleton-rooted interval support)

Let

\[
                    A=(A_t)_{t\in\mathbb Z/L\mathbb Z},
                    \qquad B=(B_t)_{t\in\mathbb Z/L\mathbb Z}           \tag{4.1}
\]

be arbitrary cyclic set words on the same phase positions.  Let

\[
 \mathcal C=\{J\in\mathcal I:
       \bigcup_{t\in J}A_t\ne\bigcup_{t\in J}B_t\}.
\tag{4.2}
\]

Then every `J in mathcal C` contains a singleton interval belonging to
`mathcal C`:

\[
 \boxed{
 J\in\mathcal C
 \quad\Longrightarrow\quad
 \text{there is }t\in J\text{ with }\{t\}\in\mathcal C.}
\tag{4.3}
\]

#### Proof

If the two unions differ at `J`, then, after exchanging the words if
necessary, some coordinate `x` belongs to `union_(t in J) A_t` but not to
`union_(t in J) B_t`.  Choose `t in J` with `x in A_t`.  Then `x notin
B_t`, so `A_t ne B_t`.  Hence the singleton `{t}` lies in `mathcal C`.
\(\square\)

Put

\[
                         P=\{t:A_t\ne B_t\}.              \tag{4.4}
\]

### Corollary 4.2 (source-support transversal bound)

The changed source positions hit every changed interval:

\[
                         J\cap P\ne\varnothing
                         \qquad(J\in\mathcal C).          \tag{4.5}
\]

Consequently, if `tau(mathcal C)` is the minimum number of phase positions
meeting every interval in `mathcal C`, then

\[
                         \boxed{|P|\ge\tau(\mathcal C).}  \tag{4.6}
\]

In particular, `s` pairwise disjoint changed intervals force at least `s`
changed source letters.

#### Proof

Theorem 4.1 gives a changed singleton inside every `J`, and its phase lies
in `P`.  Thus `P` is a transversal.  The remaining assertions follow from
the definition of `tau`.  \(\square\)

### Corollary 4.3 (dense literal two-phase obstruction)

The family

\[
                         \mathcal C_{\ge2}
                          =\{J\in\mathcal I:|J|\ge2\}     \tag{4.4}
\]

is not the literal change support of any two pull phases, regardless of the
number of core coordinates.  Its density is

\[
                         {|\mathcal C_{\ge2}|\over|\mathcal I|}
                          ={d-1\over d}=1-o(1).            \tag{4.5}
\]

#### Proof

The family is nonempty for `d>=2` but contains no singleton, contradicting
Theorem 4.1.  Its size is `L(d-1)` out of `Ld`.  \(\square\)

Thus allowing signed phases closes scalar Möbius capacity but not arbitrary
literal support.  The obstruction applies to every equal-length
rethread—not merely to pull coordinates.  A literal dense-cluster
coalescer must prepare a singleton-rooted cluster, change enough physical
letters to hit its interval support, or use an insertion/deletion which
changes the interval-address correspondence.

The theorem closes precisely the following possible obstructions:

* insufficient total core capacity;
* a scalar Möbius-sign obstruction;
* the one-polarity downset obstruction after allowing two phases.

It leaves precisely:

1. pair positive and negative runs coordinatewise so all unwanted literal
   changes cancel;
2. assign the intended changed occurrences to the required named targets;
3. preserve owner, upper-provider, residence, topology, and compiler
   tickets under the same pairing.

Consequently the dense-cluster coagulation route is not blocked by scalar
rank arithmetic.  Its remaining obstruction is a labelled two-phase
transport theorem.
