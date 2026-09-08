# Product-SCD rectangles: endpoint matchings for every `q=o(b)` and the exact shift gate

**Status (2026-08-21).** Every theorem below is proved.  For each upper
offset `q=o(b)`, the clustered color-capacitated tokenwise containment graph
has a matching of size

\[
 {2b\choose b+q}
 -O\left({W_b\over\sqrt b}+{qW_b\over b}
          +e^{-\Omega(b)}W_b\right)
 ={2b\choose b+q}-o(W_b),                          \tag{0.1}
\]

where `W_b=binom(2b,b)`.  The construction uses **every** product
symmetric-chain rectangle whose two chain bottoms differ: it takes shift
`0` when the `A`-chain bottom is larger and shift `q` when the `B`-chain
bottom is larger.  Only equal-bottom chain pairs are discarded.  When
`q=o(sqrt b)`, (0.1) is `(1-o(1))W_b` because the target rank itself then
has that size.

For every remaining rectangle, all target-saturating **constant shifts**
are characterized exactly.  Their aggregate choice problem is a
multiple-choice interval packing matrix.  Already at `(b,q)=(5,2)` that
matrix contains an explicit determinant-`2` minor, so the most immediate
total-unimodularity shortcut fails.  This finite minor is not a no-go for a
near-perfect solution of the dense full problem.

All results here are in the tokenwise orbit relaxation.  The graph theorem
is unconditional; interpreting its color capacities as physical product
occurrence-token counts remains conditional on the requisite growing-rank
tight-cycle factors.  The theorem does not realize the selected containments
by common cyclic orders.  The estimate (0.1) is useful for one fixed or
slowly growing offset; summing this particular loss bound over
`1<=q<=Q` is `o(W_b)` for `Q=o(sqrt b)`, but not in the full DCC regime.

## 1. Product-chain rectangle geometry at general offset

Let `A,B` be disjoint `b`-sets, let `b=2h+1` be odd, and fix symmetric
chain decompositions on both Boolean lattices.  As usual, put

\[
 c_d={b\choose d}-{b\choose d-1},
 \qquad 0\le d\le h,                               \tag{1.1}
\]

so there are `c_d` chains with bottom rank `d`.

Fix an `A`-chain with bottom `a` and a `B`-chain with bottom `c`.  On their
Cartesian product, the rank-`b` source diagonal has local `A`-ranks

\[
 R_{a,c}=[d,b-d],\qquad d=\max(a,c).                \tag{1.2}
\]

At upper offset `q`, the target diagonal has local `A`-ranks

\[
 S_{a,c}^{(q)}=[L_{a,c},U_{a,c}],                  \tag{1.3}
\]

where

\[
 L_{a,c}=\max(a,c+q),
 \qquad
 U_{a,c}=\min(b-a,b-c+q).                          \tag{1.4}
\]

Write `[x]_+=max(x,0)`.  The exact number of targets in the rectangle is

\[
 N_{a,c}^{(q)}=[U_{a,c}-L_{a,c}+1]_+.              \tag{1.5}
\]

### Proposition 1.1 (exact interval containment matrix)

A source of local `A`-rank `r` is contained in a target of local `A`-rank
`s` exactly when

\[
 r\in R_{a,c},\qquad s\in S_{a,c}^{(q)},
 \qquad 0\le s-r\le q.                             \tag{1.6}
\]

Thus the rectangle incidence graph is convex in both ordered shores.

Assume `N_(a,c)^(q)>0`.  For an integer `z`, the constant-shift map

\[
 s\longmapsto r=s-z                              \tag{1.7}
\]

matches every target in the rectangle if and only if

\[
 z\in K_{a,c}^{(q)}=
 \left[
   \min(q,\max(0,c-a)),
   \max(0,\min(q,q+c-a))
 \right].                                           \tag{1.8}
\]

Every such map is a target-saturating containment matching and all of its
edges have phase color `z`.

#### Proof

Along a symmetric chain, containment is the rank order.  A source
`(X_r,Y_(b-r))` lies below a target `(X_s,Y_(b+q-s))` precisely when
`r<=s` and `b-r<=b+q-s`, which is (1.6).

The map (1.7) is a bijection from the target interval to an interval of
sources.  It is valid exactly when

\[
 L_{a,c}-z\ge d,qquad U_{a,c}-z\le b-d,qquad 0\le z\le q.
\]

Substitution from (1.4), separately for `a>=c` and `a<=c`, reduces these
bounds to (1.8).  \(\square\)

Two extreme cases will be used below.  If `a-c>=q`, then
`K_(a,c)={0}`, the source and target shores have equal size, and the unique
perfect matching adds only `B`.  If `c-a>=q`, then `K_(a,c)={q}` and the
unique perfect matching adds only `A`.  If `|a-c|<q`, the target shore is
of size
`max(0,|R_(a,c)|-(q-|a-c|))`; when it is nonempty, (1.8) contains
`q-|a-c|+1` constant shifts.

## 2. The unequal-bottom endpoint matching

Keep every chain pair with `a!=c`.  If `a>c`, use constant shift `z=0`;
if `c>a`, use constant shift `z=q`.  Both choices belong to the interval
(1.8), even when `|a-c|<q`.  Proposition 1.1 therefore matches every target
in every unequal-bottom rectangle.  Different chain pairs have disjoint
source and target vertices, so their union is a labelled containment
matching.  Equal-bottom rectangles are left unused.

The clustered endpoint color capacities at an admissible source split are

\[
 Q_{r,q,q}={r-q+1\over b}{b\choose r}^2,
 \qquad
 Q_{r,q,0}={b-r-q+1\over b}{b\choose r}^2,          \tag{2.1}
\]

while each interior color `1<=z<=q-1` has capacity
`2 binom(b,r)^2/b`.  The endpoint matching uses no interior color.

### Lemma 2.1 (endpoint overload is globally negligible)

For each source split and each of the two endpoint colors, the endpoint
matching exceeds the corresponding capacity in (2.1) by at most

\[
 {q-1\over b}{b\choose r}^2.                       \tag{2.2}
\]

Consequently, deleting at most

\[
 {2(q-1)\over b}W_b                                \tag{2.3}
\]

edges makes every color capacity valid.

#### Proof

Put `t=min(r,b-r)` and write

\[
 S_t={b\choose t},
 \qquad E_t=\sum_{d=0}^t c_d^2,
 \qquad F_t={S_t^2-E_t\over2}.                     \tag{2.4}
\]

The elementary induction

\[
 E_t\ge {b-2t\over b}S_t^2,
 \qquad F_t\le {t\over b}S_t^2                    \tag{2.5}
\]

is self-contained as follows.  It is equality at `t=0`.  Since
`S_(t-1)/S_t=t/(b-t+1)`, the induction hypothesis gives

\[
 {E_t\over S_t^2}
 \ge {b-2t+2\over b}
      \left({t\over b-t+1}\right)^2
    +\left(1-{t\over b-t+1}\right)^2
 ={b-2t\over b}+{2t\over b(b-t+1)}.
\]

Every selected shift-`0` edge at source split `r` comes from an ordered
chain pair `a>c` with both bottoms at most `t`; every selected shift-`q`
edge comes from a pair `c>a` with both bottoms at most `t`.  Each load is
therefore at most the full oriented off-diagonal count `F_t`.  By (2.5),
`F_t` respects both `q=1` endpoint capacities

\[
 {r\over b}{b\choose r}^2,
 \qquad {b-r\over b}{b\choose r}^2.                \tag{2.6}
\]

Each capacity in (2.1) is the corresponding quantity in (2.6) minus
`(q-1)binom(b,r)^2/b`, proving (2.2).  Delete arbitrary excess edges within
each source-profile/color class.  Since
`sum_r binom(b,r)^2=W_b`, their total number is bounded by (2.3).
Deletion preserves the matching property.  \(\square\)

## 3. Exact equal-bottom loss

Let

\[
 E_{b,q}=\sum_{d=0}^h c_d^2\max(0,b-2d-q+1)        \tag{3.1}
\]

be the exact number of rank-`(b+q)` targets in the discarded equal-bottom
rectangles.  The product-chain rectangles partition the target layer, so
before the capacity trimming in Lemma 2.1 the endpoint matching has exact
size

\[
 {2b\choose b+q}-E_{b,q}.                           \tag{3.2}
\]

### Lemma 3.1 (equal-bottom bound)

Put

\[
 D_{b,1}=\sum_{d=0}^h c_d^2(b-2d).
\]

Then

\[
 E_{b,q}\le D_{b,1}
 =O\left({W_b\over\sqrt b}\right).                \tag{3.3}
\]

#### Proof

The first inequality is termwise.  For completeness, write `b=2h+1` and
`d=h-k`.  Then

\[
 c_{h-k}={b\choose h-k}{2k+2\over h+k+2},
 \qquad
 {{b\choose h-k}\over{b\choose h}}
 \le e^{-k(k+1)/b}.                                 \tag{3.4}
\]

Consequently

\[
 D_{b,1}
 \le {16{b\choose h}^2\over b^2}
      \sum_{k\ge0}(2k+1)(k+1)^2e^{-2k(k+1)/b}
 =O\left({b\choose h}^2\right)
 =O\left({W_b\over\sqrt b}\right).                \tag{3.5}
\]

The ratio bound in (3.4) follows by writing it as
`prod_(j=0)^(k-1)(h-j)/(h+j+2)`; the last equality is the standard
central-binomial estimate.  \(\square\)

### Theorem 3.2 (general slowly growing offset)

Let `b` tend through odd primes and let `1<=q<=H=o(b)`.  Retain only the
genuine product payload interval

\[
 I=[H+2,b-H-2].                                    \tag{3.6}
\]

There is a tokenwise containment matching respecting every clustered
color capacity and having size at least

\[
 {2b\choose b+q}
 -O\left({W_b\over\sqrt b}+{qW_b\over b}
          +e^{-\Omega(b)}W_b\right).               \tag{3.7}
\]

Thus it is within `o(W_b)` of the whole target rank for every `q=o(b)`.
If `q=o(sqrt b)`, its size is `(1-o(1))W_b`.

#### Proof

Start with the endpoint matching, delete every edge whose source split lies
outside `I`, and then delete the remaining overload from Lemma 2.1.  The
three losses--equal-bottom rectangles, inadmissible sources, and endpoint
overload--are bounded respectively by Lemma 3.1,

\[
 \sum_{r\notin I}{b\choose r}^2=e^{-\Omega(b)}W_b,
\]

and (2.3).

For prime `b`, all capacities in the genuine interval are integers and the
remaining edges inject into their occurrence-token sets.  Finally
`binom(2b,b+q)=(1-o(1))W_b` when `q=o(sqrt b)`.  \(\square\)

Summing (3.7) over `1<=q<=Q` gives the explicit aggregate error

\[
 O\left({QW_b\over\sqrt b}+{Q^2W_b\over b}
          +Qe^{-\Omega(b)}W_b\right).               \tag{3.8}
\]

Thus this particular endpoint construction has total `o(W_b)` loss for
`Q=o(sqrt b)`.  It does not reach the DCC regime
`H/sqrt(b)->infinity`.

## 4. Exact constant-shift transport and a non-TU minor

The discarded equal-bottom rectangles have all shifts `0,...,q` available,
so (3.3) is a construction loss, not a scalar obstruction.  The smallest
coherent aggregate problem
suggested by Proposition 1.1 has variables

\[
 x_{a,c,z},\qquad z\in K_{a,c}^{(q)},               \tag{4.1}
\]

where only nonempty target rectangles are included and `x_(a,c,z)` is the
number of the `c_ac_c` identical chain pairs that use the target-saturating
constant shift `z`.  Its constraints are

\[
 \sum_{z\in K_{a,c}^{(q)}}x_{a,c,z}\le c_ac_c       \tag{4.2}
\]

and

\[
 \sum_{\substack{a,c:\\L_{a,c}-z\le r\le U_{a,c}-z}}
 x_{a,c,z}\le Q_{r,q,z}.                            \tag{4.3}
\]

For fixed `z`, every column in (4.3) is an interval in `r`.  The supply
rows (4.2), however, couple choices across different `z` blocks.

### Proposition 4.1 (the natural shift matrix is not always TU)

At `(b,q)=(5,2)`, the zero-one coefficient matrix of (4.2)--(4.3) contains
the following determinant-`2` minor.  A column is written
`(a,c,z;lo,hi)`, where `[lo,hi]=[L_(a,c)-z,U_(a,c)-z]` is its source-rank
interval.  Take rows

\[
 (C_{1,1},P_{2,1},C_{3,0},C_{2,1},P_{0,0},C_{4,1})
\]

and columns

\[
\begin{array}{lll}
 (0,0,0;2,5),&(0,0,1;1,4),&(0,1,1;2,4),\\
 (2,1,0;3,3),&(2,1,1;2,2),&(1,0,1;1,3),
\end{array}
\]

where `P_(a,c)` is a supply row and `C_(r,z)` a color-capacity row.  The
minor is

\[
 \begin{pmatrix}
 0&1&0&0&0&1\\
 0&0&0&1&1&0\\
 1&0&0&1&0&0\\
 0&1&1&0&1&1\\
 1&1&0&0&0&0\\
 0&1&1&0&0&0
 \end{pmatrix},
 \qquad \det=2.                                     \tag{4.4}
\]

#### Proof

Formula (1.8) verifies that all six displayed columns exist, and their
intervals give exactly the incidences in (4.4).  Direct elimination gives
determinant `2`.  \(\square\)

This rules out automatic total unimodularity of the most literal
constant-shift transportation matrix.  It does not show an integrality gap
for the actual right-hand sides, does not include nonconstant matchings
inside a rectangle, and does not obstruct an `o(W_b)` rounding theorem.

## 5. Remaining exact gate

Theorem 3.2 comes within `o(W_b)` of the whole target rank for each
`q=o(b)` separately, and gives `(1-o(1))W_b` targets when `q=o(sqrt b)`.
To reach the full DCC band with **aggregate** `o(W_b)` loss, one must use
the equal-bottom rectangles and coordinate the small endpoint overloads
instead of discarding and trimming them independently at every offset.  The
next precise subproblem is to round (4.1)--(4.3), or its richer version
allowing nonconstant interval matchings, simultaneously over `q`, with total
loss `o(W_b)`.  After that, the still harder labelled-order coinstantiation
with the tight-cycle factors remains.
