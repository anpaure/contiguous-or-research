# Exact lower-rainbow context tilings inside one matching cube

Date: 2026-07-25

Method: explicit finite-group construction.

## 0. Outcome

Let `s=2^t` and fix a perfect matching `M` of a `2s`-element context set.
The middle `s`-sets which choose one endpoint from every pair of `M` form
an `s`-dimensional Boolean cube; modulo complementation they form a set of
size `2^(s-1)`.

There is an explicit family of

\[
                         \boxed{2^{s-1}/s}                         \tag{0.1}
\]

cyclic context orders such that

1. their folded middle packets partition all complementary pairs of
   transversals of `M`; and
2. all their cyclic `(s-1)`-intervals are distinct.

Thus the sharp two-rank context packing problem is solved exactly inside
each fixed matching cube.  Combining different matching cubes without
reusing their transversals remains the global gate.

For arbitrary `s`, exact factorization of a whole folded cube is
arithmetically impossible unless `s` is a power of two.  The same argument
with the least power of two `r>=s` nevertheless gives
`2^(s-1)/r >= 2^(s-2)/s` disjoint lower-rainbow cycles, covering more than
half of every folded matching cube.  This removes the power-of-two
restriction from all constant-density applications; see Theorem 3.2.

## 1. The folded cube

Write the pairs of `M` as

\[
                         P_i=\{x_i^0,x_i^1\},qquad i\in\mathbb Z_s.
\]

A vector `v in F_2^s` represents the transversal

\[
                         T(v)=\{x_i^{v_i}:i\in\mathbb Z_s\}.
\]

Complementation sends `v` to `v+1`, so the complementary transversal
pairs are the elements of

\[
                         G=\mathbb F_2^s/\langle\mathbf1\rangle.   \tag{1.1}
\]

For a starting vector `v`, define the context cyclic order

\[
 R_v=(x_0^{v_0},x_1^{v_1},\ldots,x_{s-1}^{v_{s-1}},
      x_0^{1-v_0},x_1^{1-v_1},\ldots,x_{s-1}^{1-v_{s-1}}).
                                                                    \tag{1.2}
\]

Moving the start of a length-`s` window one step flips exactly one pair.
Consequently the folded middle packet of `R_v` is

\[
 C+\bar v,
 \qquad
 C=\{\bar p_j:0\le j<s\}\subseteq G,
 \qquad
 p_j=e_0+\cdots+e_{j-1},                                         \tag{1.3}
\]

where bars denote classes modulo `1`.  The closing step flips coordinate
`s-1` and reaches `p_s=1=0` in `G`, so (1.3) is an `s`-cycle.

## 2. A kernel whose cosets are cut once by the prefix cycle

Choose any cyclic enumeration

\[
                         g_0,g_1,\ldots,g_{s-1}                   \tag{2.1}
\]

of the elements of `F_2^t`, and put `g_s=g_0`.  Define

\[
                         a_i=g_{i+1}+g_i.                         \tag{2.2}
\]

Because `sum_i a_i=0`, the linear map

\[
 \psi:G\longrightarrow\mathbb F_2^t,
 \qquad
 \psi(\bar e_i)=a_i                                             \tag{2.3}
\]

is well-defined.  Its values on the prefix cycle telescope:

\[
                         \psi(\bar p_j)=g_j+g_0.                  \tag{2.4}
\]

These are all `s=2^t` elements of the codomain.  Hence `psi` is surjective
and its restriction to `C` is bijective.  Put

\[
                         H=\ker\psi.                              \tag{2.5}
\]

Then

\[
                         |H|={|G|\over s}={2^{s-1}\over s}.       \tag{2.6}
\]

### Lemma 2.1

The translates `C+h`, `h in H`, partition `G`.

#### Proof

If `c+h=c'+h'`, applying `psi` gives `psi(c)=psi(c')`.  The restriction
of `psi` to `C` is injective, so `c=c'` and then `h=h'`.  Thus the
translates are disjoint.  Their total size is `|C||H|=|G|`, proving that
they cover.  \(\square\)

Taking one representative `v_h` of every `h in H`, Lemma 2.1 says that
the folded middle packets of the orders `R_(v_h)` partition all
complementary transversal pairs of `M`.

## 3. The lower colours are automatically rainbow

Fix one `(s-1)`-set `S` which occurs as a cyclic interval in some `R_v`.
Relative to `M`, the set `S` chooses one endpoint from `s-1` matched pairs
and misses one pair `P_i={x_i^0,x_i^1}` completely.  It therefore
determines the folded cube edge

\[
 \left\{
   \overline{S\cup\{x_i^0\}},
   \overline{S\cup\{x_i^1\}}
 \right\}.                                                       \tag{3.1}
\]

These are the two adjacent folded middle vertices on either side of that
lower interval.  Hence two context cycles containing the same lower colour
`S` would share both endpoints of (3.1).

### Theorem 3.1 (exact matching-cube context factor)

The orders `R_(v_h)`, `h in H`, have pairwise disjoint folded middle
packets and pairwise disjoint `(s-1)`-interval packets.  They number
`2^(s-1)/s`.

#### Proof

Middle disjointness is Lemma 2.1.  If two orders shared a lower colour,
(3.1) would force their folded cycles to share middle vertices, a
contradiction.  Proper cyclic intervals inside one order are distinct, so
there is no internal repetition either.  Equation (2.6) gives the count.
\(\square\)

### Theorem 3.2 (arbitrary-dimension partial context factor)

The power-of-two hypothesis is unnecessary for the constant-density
application.  For every integer `s>=2`, every perfect matching on a
`2s`-element context set has a family of

\[
 \boxed{
 {2^{s-1}\over r},
 \qquad r=2^{\lceil\log_2s\rceil},}
 \tag{3.2}
\]

cyclic context orders with pairwise disjoint folded middle packets and
pairwise disjoint `(s-1)`-interval packets.  In particular its size is at
least `2^(s-2)/s`, and its folded middle packets cover the fraction

\[
                         {s\over r}>{1\over2}                  \tag{3.3}
\]

of the matching cube.

#### Proof

Put `t=ceil(log_2 s)` and choose distinct elements

\[
                         g_0,\ldots,g_{s-1}\in\mathbb F_2^t
\]

whose affine differences from `g_0` span `F_2^t`; this is possible since
`s<=2^t` and `t+1<=s` for `s>=2`.  Put `g_s=g_0` and again define

\[
                         a_i=g_{i+1}+g_i,
 \qquad
                         \psi(\bar e_i)=a_i.
\]

The identity `sum_i a_i=0` makes `psi` well defined, and

\[
                         \psi(\bar p_j)=g_j+g_0
\]

shows simultaneously that `psi` is surjective and that its restriction to
the prefix cycle `C` is injective.  Hence, for `H=ker psi`, the translates
`C+h`, `h in H`, are pairwise disjoint.  They need not cover `G`, but

\[
                         |H|={2^{s-1}\over2^t}={2^{s-1}\over r}.
\]

The lower-rainbow proof of Theorem 3.1 used only middle disjointness and
therefore applies verbatim.  Finally `s<=r<2s`, proving (3.3). \(\square\)

## 4. Relation to the global context gate

A fixed matching cube contains only `2^(s-1)` of the

\[
                         {1\over2}\binom{2s}s
\]

folded middle vertices.  Different perfect matchings have intersecting
transversal cubes: if `M union M'` has `c` alternating components, they
have `2^(c-1)` common folded transversals.  Thus Theorem 3.1 cannot simply
be united over all `M`.

It nevertheless supplies an exact internal factorization for every cube.
The remaining global problem can be stated without cyclic-order geometry:

> Select partial kernel-translate factors from the matching cubes so that
> their folded transversal vertices are disjoint and their lower colours
> are disjoint, with total size `Omega(binomial(2s,s)/s)`.

The incidence is highly regular: every middle `s`-set is a transversal of
exactly `s!` perfect matchings.  A lower `(s-1)`-set is compatible with
`binom(s+1,2)(s-1)!` matchings before the inner cycle-edge selection.  This
is the precise next layer for a nibble, algebraic resolution, or recursive
cube packing; the within-cube cycle construction itself is now exact.
