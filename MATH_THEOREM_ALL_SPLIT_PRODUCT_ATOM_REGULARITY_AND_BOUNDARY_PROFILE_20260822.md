# All-split product atoms: exact regularity and boundary-codegree profile

**Status (2026-08-22).**  Every statement through Theorem 4.1 below is
proved.  The result replaces the fixed-split volume question by one explicit
regular hypergraph on the whole middle layer.  Its atoms have size `b^2`, its
uniform fractional factor is exact, and its largest normalized pair
codegree is exactly `4/b^2`.  The only pairs attaining that bound are the two
Johnson boundary shells.

This is not yet an integral near-factor theorem.  Since the edge size is
`b^2`, the product of edge size and maximum normalized codegree is `4`, not
`o(1)`.  Thus a fixed-uniformity nibble theorem cannot simply be invoked
without a growing-uniformity argument.  Nor does a central matching by
itself prove common all-depth coverage.  The theorem does, however, show
that neither lack of product atoms nor a fixed-split `Theta(b^(-1/2))`
volume loss is a genuine obstruction.

## 1. The atom multihypergraph

Let

\[
                 b=2h+1\ge5,
\]

and let `Omega` be a set of size `2b`.  Write

\[
                 \mathcal V={\Omega\choose b}.
\]

An oriented cyclic order on a `b`-set is a permutation modulo cyclic
rotation; reversal is not identified.  If `alpha` is such an order, let
`I_alpha(i,s)` be its cyclic interval of length `s` starting at `i`.

For every `b`-set `A subset Omega`, put `B=Omega-A`.  For oriented cyclic
orders `alpha` on `A` and `beta` on `B`, define the product atom

\[
 E(A,\alpha,\beta)=
 \{I_\alpha(i,h)\mathbin\cup I_\beta(j,h+1):
                         (i,j)\in\mathbb Z_b^2\}.       \tag{1.1}
\]

We retain the triple `(A,alpha,beta)` as an edge label, so the resulting
object `mathcal H_b` is a multihypergraph.  Parallel labelled copies do not
affect the meaning of a matching.  The torus enumeration theorem gives a
literal cyclic singleton realization of every edge in (1.1), using the
alternating type word with `h` letters of type `A` and `h+1` of type `B`.

### Lemma 1.1 (atom size)

Every edge of `mathcal H_b` has exactly `b^2` vertices.

#### Proof

A proper nonempty cyclic interval in a cyclic order is determined by its
set when its length is fixed and is not `b/2`.  Hence the `b` length-`h`
intervals of `alpha` are distinct, as are the `b` length-`(h+1)` intervals
of `beta`.  Intersecting a union in (1.1) with `A` and `B` recovers its two
factors.  Thus the map `(i,j)` in (1.1) is injective.  \(\square\)

There are `(b-1)!` oriented cyclic orders on a fixed `b`-set.  Consequently
the number of labelled atoms is

\[
       |\mathcal E|={2b\choose b}((b-1)!)^2.          \tag{1.2}
\]

## 2. Exact degree and pair codegrees

For `S,T in mathcal V`, put

\[
       d(S,T)=|S-T|=|T-S|.
\]

Let `D` be the degree of one vertex, with labelled atom multiplicity, and
let `lambda_d` be the codegree of two distinct vertices at Johnson distance
`d`.

### Theorem 2.1 (exact regularity)

The multihypergraph `mathcal H_b` is `b^2`-uniform and regular of degree

\[
                         D=(b!)^2.                  \tag{2.1}
\]

#### Proof

The symmetric group on `Omega` is transitive on `mathcal V` and preserves
the labelled atom family, so all vertex degrees agree.  Double-counting
vertex-edge incidences and using (1.2) and Lemma 1.1 gives

\[
 D={|\mathcal E|b^2\over|\mathcal V|}
   =((b-1)!)^2b^2=(b!)^2.
\]

\(\square\)

### Lemma 2.2 (distance census inside one atom)

Fix `S` in an atom `E`.  The number `n_d` of other vertices `T in E` at
distance `d` from `S` is

\[
 n_0=1,
 \qquad
 n_d=4\min(d,b-d)\quad(1\le d\le b-1),
 \qquad
 n_b=0.                                             \tag{2.2}
\]

In particular

\[
                         \sum_{d=0}^b n_d=b^2.       \tag{2.3}
\]

#### Proof

Consider first the length-`h` interval deck of one cyclic `b`-set.  From a
fixed interval, there is one interval at distance zero and, for each
`1<=a<=h`, exactly two intervals at Johnson distance `a`, obtained by
shifting its start by `a` in either direction.  Because `b=2h+1`, these are
all `b` intervals.  The length-`(h+1)` deck has the same distance census by
taking complements inside its `b`-set.

Distances add across the disjoint blocks `A` and `B`.  Therefore `n_d` is
the convolution of

\[
                         t_0=1,\qquad t_a=2
                         \quad(1\le a\le h).
\]

If `1<=d<=h`, the two endpoint terms contribute `4` and the `d-1`
interior terms contribute `4(d-1)`, giving `n_d=4d`.  If
`h<d<=2h=b-1`, all `2h-d+1=b-d` feasible terms are interior and contribute
four each.  No sum of two local distances exceeds `2h`, proving (2.2).
Equation (2.3) also follows directly from the `b^2` choices in the atom.
\(\square\)

### Theorem 2.3 (complete pair-codegree profile)

For `1<=d<=b-1`,

\[
 {\lambda_d\over D}
   ={4\min(d,b-d)\over {b\choose d}^2},             \tag{2.4}
\]

while `lambda_b=0`.  Consequently

\[
       \max_{S\ne T}{\deg(S,T)\over D}
          ={4\over b^2},                            \tag{2.5}
\]

and equality holds precisely when `d(S,T)=1` or `b-1`.

#### Proof

The stabilizer of `S` in the symmetric group is transitive on the
`binom(b,d)^2` vertices at distance `d` from `S`.  Count triples `(E,T)` in
which `E` is a labelled atom containing `S` and `T in E` has distance `d`
from `S`.  Lemma 2.2 counts them as `D n_d`.  Counting first by `T` gives
`binom(b,d)^2 lambda_d`.  This proves (2.4), including `lambda_b=0`.

For `d=1,b-1`, (2.4) is `4/b^2`.  Put
`t=min(d,b-d)`.  If `2<=t<=h`, then

\[
 {b\choose d}={b\choose t}\ge {b\choose2}
                  ={b(b-1)\over2},
\]

and `t<=h=(b-1)/2` gives

\[
 {b\choose d}^2\ge b^2t.
\]

Thus (2.4) is at most `4/b^2`, with strict inequality for `b>=5` and
`t>=2`.  \(\square\)

## 3. Exact fractional factor and typical link overlap

### Corollary 3.1 (uniform fractional perfect matching)

Giving every labelled atom weight `1/D` is a fractional perfect matching:

\[
                  \sum_{E\ni S}{1\over D}=1
                  \qquad(S\in\mathcal V).           \tag{3.1}
\]

Its total weight is

\[
                         {1\over b^2}{2b\choose b}. \tag{3.2}
\]

#### Proof

Equation (3.1) is Theorem 2.1.  Summing it over vertices counts every atom
weight `b^2` times and gives (3.2).  \(\square\)

There is also a useful averaged form of the codegree calculation.  Choose
two labelled atoms `E,F` independently and uniformly among those containing
a fixed vertex `S`.  Then

\[
\begin{aligned}
 \mathbb E|(E\cap F)-\{S\}|
 &=\sum_{T\ne S}
      \left({\deg(S,T)\over D}\right)^2\\
 &=\sum_{d=1}^{b-1}{n_d^2\over {b\choose d}^2}
   ={32\over b^2}+O(b^{-3}).                       \tag{3.3}
\end{aligned}
\]

Indeed the shells `d=1,b-1` contribute exactly `32/b^2`.  For
`2<=t<=h`, pairing the shells `t,b-t` leaves

\[
 32\sum_{t=2}^h {t^2\over {b\choose t}^2}.
\]

The `t=2` summand is `O(b^{-4})`; for `t>=3`, monotonicity of binomial
coefficients through the middle and
`binom(b,t)>=binom(b,3)` give `O(b^{-3})` after summing `t^2`.
In particular

\[
 \Pr(E\cap F\ne\{S\})=O(b^{-2}).                  \tag{3.4}
\]

Equation (3.4) is an average statement.  It does not suppress the four
distance-one and four distance-`(b-1)` neighbours which occur in every
individual atom through `S`.

## 4. Exact consequence for the coefficient-one program

### Theorem 4.1 (all-split central packing reduction)

Let `H=H_b=o(b)`, put `f=b+H+2`, and assume `b>=3H+5`.  Suppose
`mathcal H_b` has a matching covering

\[
                  (1-o(1)){2b\choose b}             \tag{4.1}
\]

vertices.  Then the matched edges are
`(1+o(1))binom(2b,b)/b^2` genuine cyclic torus atoms.  They can be
serialized with `O(b)` legal connector positions per atom, hence with total

\[
                  O\left({1\over b}{2b\choose b}\right)=o\left({2b\choose b}\right)
                                                               \tag{4.2}
\]

connector length.  Thus they give a coefficient-one middle-layer covering.

#### Proof

Each matched edge covers `b^2` middle targets, so (4.1) gives the asserted
atom count.  Every edge has the physical torus realization described after
(1.1); its same-label spacing is at least `2b-2>=f`.  The displayed
hypothesis `b>=3H+5` is the near-half permutation-shift condition, so that
the diameter theorem joins arbitrary legal boundary histories in `O(b)`
emissions.  Multiplication by the atom count proves (4.2).  At each seam,
the connector positions and the `O(b)` middle-window starts straddling the
two cut boundaries contribute only `O(b)` charged targets.  Thus the same
estimate controls middle-layer damage.
\(\square\)

The hypothesis of Theorem 4.1 is deliberately left open.  The exact profile
(2.4) is stronger than generic `o(D)` codegree control, but it does not by
itself prove an integral matching when the edge size grows as `b^2`.
Moreover, even a proof of (4.1) would cover only the middle layer.  To obtain
a defective central covering one must choose the same physical atoms so
that their nearby-rank cyclic windows have aggregate `o(W)` holes.  Hence
the remaining product route has two cleanly separated requirements:

1. a quenched near-factor theorem for `mathcal H_b`; and
2. common all-depth control for the selected literal atoms.

No Baranyai--Katona factor is assumed in either the definition of
`mathcal H_b` or the regularity and codegree theorems above.
