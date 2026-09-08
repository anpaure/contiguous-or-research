# Gate C: the exact multiroot grid and the two-root four-letter bridge

**Status (2026-08-22).** Every identity and implication below is proved.
For several marked value cuts, the common-time sign vector is not a single
threshold vector.  It is the coordinatewise product of a threshold in
marked-value order and a threshold in marked-position order.  Thus the
natural common walk has a two-dimensional grid of step types, rather than
the previously hoped-for one-dimensional Weyl-chamber alphabet.

For two roots, conditioning on their value and position separations reduces
the remaining random permutation exactly to a uniform word with four
prescribed letter multiplicities.  Joint goodness forces four explicit
one-sided meanders on the two value arcs.  This is a theorem-grade finite
reduction; the uniform multiroot moment bound is still open.

Throughout, `K` is odd.  All values and positions belong to `Z_K`, but
inequalities use their representatives in `{0,...,K-1}`.

## 1. Rooted signs

Let `sigma` be a permutation of `Z_K`, interpreted as the position of each
value.  For distinct values `a,v`, put

\[
 w_a(v)=(-1)^{((v-a)\bmod K)+((\sigma(v)-\sigma(a))\bmod K)}.       \tag{1.1}
\]

Thus `w_a(v)=+1` exactly when the two clockwise distances have the same
parity.  The cut `a` is *good* when, in the order
`a+1,...,a+K-1`, every prefix sum of the signs lies between zero and the
terminal sum.  Equivalently, every prefix and every suffix has nonnegative
sum.

For representatives `x,y in {0,...,K-1}`, oddness of `K` gives

\[
 (-1)^{(x-y)\bmod K}=(-1)^{x+y+\mathbf1_{x<y}}.          \tag{1.2}
\]

(The minus sign on `y` is immaterial modulo two.)

## 2. The exact multiroot grid

Fix distinct marked roots `a_1,...,a_j` and write

\[
 p_t=\sigma(a_t),\qquad c_t=(-1)^{a_t+p_t}.             \tag{2.1}
\]

For an unmarked value `v`, put `q=\sigma(v)` and
`z_v=(-1)^{v+q}`.

### Theorem 2.1 (two-threshold identity)

For every root `a_t` and every `v\ne a_t`,

\[
 \boxed{
 c_t w_{a_t}(v)
 =z_v(-1)^{\mathbf1_{v<a_t}}(-1)^{\mathbf1_{q<p_t}}.}  \tag{2.2}
\]

#### Proof

Apply (1.2) separately to the value and position distances in (1.1):

\[
 w_{a_t}(v)
 =(-1)^{v+a_t+\mathbf1_{v<a_t}}
  (-1)^{q+p_t+\mathbf1_{q<p_t}}.
\]

The factors independent of the two cuts are exactly `c_t z_v`.  This is
(2.2). \(\square\)

Order the marked roots once by value and once by position.  As `t` varies,
the first indicator in (2.2) is a threshold vector in value order, while
the second is a threshold vector in position order.  Consequently an
unmarked point in value cell `r` and position cell `s` has, up to the common
sign `z_v`, the Hadamard product of those two threshold vectors.  There are
at most

\[
                         2(j+1)^2                         \tag{2.3}
\]

signed step types.  Unless the two root orders coincide in a special way,
these are not the `2(j+1)` steps of a single threshold chain.  In
particular, taking first differences in only one root order does not turn
the general walk into an axis-step walk.

This is the precise obstruction to applying a one-chain
Karlin--McGregor/LGV estimate directly: roots also have different value
origins, and the value-wrap factor in (2.2) cannot be discarded.

## 3. Exact two-root normalization

Take roots `0` and `u`, where `1<=u<K`.  Translate all positions so that

\[
                    \sigma(0)=0,\qquad \sigma(u)=d,quad1\le d<K.       \tag{3.1}
\]

Let

\[
 I=\{1,...,u-1\},\qquad J=\{u+1,...,K-1\}.             \tag{3.2}
\]

For a remaining value `v`, write `q=\sigma(v)` and define

\[
 s(v)=w_0(v)=(-1)^{v+q},\qquad
 \eta(q)=\begin{cases}-1,&q<d,\\+1,&q>d,\end{cases}
 \qquad C=(-1)^{u+d}.                                  \tag{3.3}
\]

### Lemma 3.1 (two-root sign table)

For `v` different from `0,u`,

\[
 w_u(v)=
 \begin{cases}
 -C s(v)\eta(q),&v\in I,\\
  C s(v)\eta(q),&v\in J.
 \end{cases}                                           \tag{3.4}
\]

The sign of the edge between the two roots, as seen from either root, is
`C`.

#### Proof

Formula (2.2), or a direct expansion of the two clockwise distances, gives

\[
 w_u(v)=C s(v)(-1)^{\mathbf1_{v<u}+\mathbf1_{q<d}}.
\]

This is (3.4); setting `v=u` in the root-zero row gives the final claim.
\(\square\)

## 4. The exact four-letter law

Classify every available position

\[
 q\in\{1,...,K-1\}\setminus\{d\}                     \tag{4.1}
\]

by the two bits

\[
             \bigl(\mathbf1_{q<d},\ q\bmod2\bigr).     \tag{4.2}
\]

Let `n_{epsilon,r}` be the number of positions of type
`(epsilon,r)`.  Explicitly these are the cardinalities of the four sets

\[
 \{q:1\le q<d,\ q\equiv r\pmod2\},\qquad
 \{q:d<q<K,\ q\equiv r\pmod2\}.                       \tag{4.3}
\]

### Theorem 4.1 (uniform four-letter bridge)

Conditional on (3.1), the type word

\[
 \left(\mathbf1_{\sigma(v)<d},\ \sigma(v)\bmod2\right)_{
 v=1,...,K-1;\ v\ne u}                                \tag{4.4}
\]

is uniform among all words having the four multiplicities
`n_{epsilon,r}`.

#### Proof

Once a type word is fixed, the actual positions of each of its four types
can be assigned to the corresponding value slots in

\[
                      \prod_{\epsilon,r}n_{\epsilon,r}! \tag{4.5}
\]

ways.  This multiplicity is independent of the word.  Every normalized
permutation satisfying (3.1) occurs once. \(\square\)

Thus the exact two-root problem contains no hidden permutation weights: it
is a four-letter sampling-without-replacement problem.  The signs in each
letter are read from (3.3)--(3.4), with the deterministic parity of the
value slot `v`.

## 5. Four necessary meanders

For a word `x_1,...,x_m`, call it a forward meander when every prefix sum is
nonnegative, and a backward meander when every suffix sum is nonnegative.

### Proposition 5.1 (four-arc implication)

If both roots `0` and `u` are good, then all four statements hold:

1. `(s(v))_{v in I}` is a forward meander;
2. `(w_u(v))_{v in I}` is a backward meander;
3. `(w_u(v))_{v in J}` is a forward meander;
4. `(s(v))_{v in J}` is a backward meander.

#### Proof

The root-zero word is

\[
             I,\quad u,\quad J,                         \tag{5.1}
\]

in that order.  Its nonnegative prefixes include every prefix contained in
`I`, and its nonnegative suffixes include every suffix contained in `J`.
The root-`u` word is

\[
             J,\quad0,\quad I,                          \tag{5.2}
\]

so the analogous two consequences are a forward meander on `J` and a
backward meander on `I`. \(\square\)

Together, Theorem 4.1 and Proposition 5.1 reduce the second factorial
moment to an explicit four-letter bridge estimate.  A sufficient uniform
bound would be

\[
 \Pr(0,u\text{ both good}\mid\sigma(0)=0,\sigma(u)=d)
 \le {C\over\sqrt{u(K-u)d(K-d)}}.                       \tag{5.3}
\]

Indeed, summing the reciprocal square roots over `u,d` is bounded, after
the normalization by the uniform position `d`, and would give
`E(G)_2=O(1)`.  Bound (5.3) is **not proved here**.  Even its proof would
settle only the second moment; the live equal-block entropy gate needs the
corresponding high-multiroot estimate when `j=K-R`.

## 6. Exact remaining scope

The earlier single-root theorem is the `j=1` estimate and gives
`E G=O(1)`.  The present note supplies the correct joint state space.  What
remains is one of the following genuinely multiroot conclusions:

\[
 \mathbb E(G)_{K-R}\le C^K,                             \tag{6.1}
\]

or a direct count of orders with at least `K-R` good cuts of size
`C^K K^R`.  Such a result would rule out the equal-block Gate-C route at
the coefficient-one scale; it would not itself construct the required
coherent-tour packing.

The companion checker
`scratch/verify_gate_c_multiroot_grid_two_root_four_letter_20260822.py`
verifies (2.2), (3.4), the constant multiplicity in Theorem 4.1, and the
four-meander implication exhaustively in the stated finite ranges.
