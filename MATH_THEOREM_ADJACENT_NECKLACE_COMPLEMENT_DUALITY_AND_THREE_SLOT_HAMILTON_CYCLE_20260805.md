# Adjacent-transfer necklaces: complement duality and the complete three-slot Hamilton theorem

**Date:** 2026-08-05  
**Method:** pure mathematics; binary run complementation and nested boundary
cycles  
**Status:** unconditional.  This proves the near-perfect matching theorem
for `min(q,b)<=3`.  It does not prove the uniform theorem for arbitrary
`q,b`.

## 1. The graph

For positive integers `q,b`, let

\[
 {cal N}_{q,b}
 =\{(x_0,\ldots,x_{q-1})\in\mathbb Z_{\ge0}^{q}:
          \sum_i x_i=b\}/C_q,
\]

and let `G_(q,b)` join two cyclic compositions when one unit is moved
between cyclically adjacent coordinates.

Equivalently, encode

\[
 (x_0,\ldots,x_{q-1})
 \longmapsto
 0,1^{x_0}0,1^{x_1}\cdots0,1^{x_{q-1}}.       \tag{1.1}
\]

The image is a binary necklace with `q` zeroes and `b` ones, and a unit
move is exactly a cyclic adjacent interchange `01 <-> 10`.

## 2. Complement duality

### Theorem 2.1

For all positive `q,b`, binary complementation induces a graph
isomorphism

\[
                         \boxed{G_{q,b}\cong G_{b,q}.}       \tag{2.1}
\]

### Proof

Complementation sends a binary necklace with `q` zeroes and `b` ones to
one with `b` zeroes and `q` ones.  It commutes with cyclic rotation and
sends every cyclic adjacent interchange `01 <-> 10` to another such
interchange.  Applying the separator encoding (1.1) to the complemented
necklace gives a cyclic weak composition of `q` into `b` parts.  The two
maps are inverse. \(\square\)

Thus any theorem for a fixed number of slots is simultaneously a theorem
for a fixed chip mass.

### Theorem 2.2 (order parity for odd slot count)

If `q` is odd, then

\[
 |\mathcal N_{q,b}|\equiv {q+b-1\choose b}\pmod2.   \tag{2.2}
\]

Equivalently, by Lucas' theorem, the order is odd precisely when addition
of `b` and `q-1` has no binary carry:

\[
                         b\mathbin{\&}(q-1)=0.       \tag{2.3}
\]

### Proof

Burnside's lemma gives

\[
 |\mathcal N_{q,b}|
 ={1\over q}\sum_{d\mid\gcd(q,b)}
 \varphi(d){(q+b)/d-1\choose q/d-1}.                \tag{2.4}
\]

Indeed, a rotation whose cycles have length `d` fixes a composition only
when `d|b`, and then the values on its `q/d` cycles form a weak
composition of `b/d`; there are `varphi(d)` rotations of this cycle type.

Every divisor of odd `q` is odd.  For `d>1`, `varphi(d)` is even, while
division by odd `q` does not change parity.  Modulo two only `d=1`
survives in (2.4), proving (2.2).  Lucas' theorem gives (2.3).
\(\square\)

Thus a uniform near-perfect theorem, if true, must leave exactly the
single parity socket in (2.3) and none otherwise.

## 3. Exact layers for three slots

Fix `b>=1`.  For a cyclic triple `x`, put

\[
             m(x)=\min(x_0,x_1,x_2),\qquad
             s(x)=b-3m(x).                         \tag{3.1}
\]

The possible positive values of `s` are

\[
                 b,b-3,b-6,\ldots,                 \tag{3.2}
\]

down to `1`, `2`, or `3`; when `3|b` there is in addition the central
constant triple.

For `s>0`, define

\[
 v_i^{(s)}=[(0,i,s-i)]\qquad(0\le i\le s),          \tag{3.3}
\]

where brackets mean cyclic rotation class.  We have

\[
                 v_0^{(s)}=v_s^{(s)},               \tag{3.4}
\]

and the vertices

\[
                 v_0^{(s)},v_1^{(s)},\ldots,
                 v_{s-1}^{(s)}                      \tag{3.5}
\]

are otherwise distinct.

### Lemma 3.1 (layer cycle)

The vertices of (3.5) are exactly the triples with minimum `m` and
residual sum `s=b-3m`.  The edges

\[
 v_0^{(s)}v_1^{(s)},v_1^{(s)}v_2^{(s)},\ldots,
 v_{s-1}^{(s)}v_0^{(s)}                              \tag{3.6}
\]

are adjacent unit transfers.  Hence the layer contains a spanning cycle
`C_s` for `s>=3`; for `s=2` it is the edge `K_2`, and for `s=1` it is a
singleton.

### Proof

Subtracting the common minimum gives a nonnegative triple of sum `s`
with at least one zero.  If it has exactly one zero, rotating that zero
to the first coordinate gives a unique representative `(0,i,s-i)` with
`1<=i<=s-1`.  If it has two zeroes, all three rotations give the single
class `v_0=v_s`.  This proves the census.

Moving one unit between the last two coordinates sends `i` to `i+1` or
`i-1`, with the endpoint identification (3.4).  These are precisely the
edges in (3.6). \(\square\)

## 4. Two radial edges splice consecutive layers

Suppose `s>=4`, and let the common minimum in the outer layer be `m`.
In literal triples, the two moves

\[
\begin{aligned}
 (m,m+1,m+s-1)&\longleftrightarrow
 (m+1,m+1,m+s-2),\\
 (m,m+2,m+s-2)&\longleftrightarrow
 (m+1,m+2,m+s-3)
\end{aligned}                                       \tag{4.1}
\]

show, after subtracting `m+1` and rotating if necessary, that

\[
 v_1^{(s)}\sim v_0^{(s-3)},\qquad
 v_2^{(s)}\sim v_1^{(s-3)}.                         \tag{4.2}
\]

Both are single adjacent unit transfers.  The outer vertices
`v_1^(s),v_2^(s)` are consecutive on `C_s`, and the inner vertices
`v_0^(s-3),v_1^(s-3)` are consecutive on `C_(s-3)` whenever
`s-3>=3`.

Consequently, delete those two cycle edges and insert the two cross edges
(4.2).  This is the standard two-edge splice of two disjoint cycles into
one cycle on their union.

The three terminal cases need only one path insertion.

* If `s-3=1`, the inner layer is a singleton adjacent to both
  `v_1^(s)` and `v_2^(s)`; replace the outer edge
  `v_1^(s)v_2^(s)` by the resulting two-edge path.
* If `s-3=2`, the inner layer is the edge
  `v_0^(2)v_1^(2)`; replace the outer edge
  `v_1^(s)v_2^(s)` by the three-edge path through those two vertices.
* If `3|b`, the innermost nonconstant layer is `s=3`.  Its vertices
  `v_1^(3)` and `v_2^(3)` are adjacent to the central constant triple:
  in either orientation the move is `(m,m+1,m+2) -> (m+1,m+1,m+1)`.
  Replace the edge `v_1^(3)v_2^(3)` by the two-edge path through the
  constant triple.

All vertices mentioned in a splice are distinct except in the explicitly
handled singleton case.

## 5. Hamilton cycle and matching consequence

### Theorem 5.1 (three-slot Hamilton theorem)

For every `b>=3`, the graph `G_(3,b)` has a Hamilton cycle.  For `b=2`
it is `K_2`, and for `b=1` it is a singleton.

### Proof

Start with the innermost layer (and, when `3|b`, its central constant
triple), using the appropriate terminal construction in Section 4.  This
gives one cycle on all vertices at the innermost depth.  Process the
remaining values of `s` in increasing order, each time using (4.2) to
splice the next layer cycle into the accumulated cycle.  The layers
partition all cyclic triples by (3.1), so the final cycle is spanning.
The cases `b=1,2` follow directly from Lemma 3.1. \(\square\)

### Corollary 5.2

For every `b`, `G_(3,b)` has a matching covering all but at most one
vertex.  It is perfect exactly when its order is even.

By complement duality, the same is true for `G_(q,3)` for every `q`.
Together with the elementary mass-one singleton and mass-two path, this
proves the adjacent-necklace near-perfect matching conjecture whenever

\[
                         \min(q,b)\le3.              \tag{5.1}
\]

## 6. Scope and the surviving induction target

The proof exposes a useful subtractive-Euclidean geometry: subtracting
one from every coordinate removes mass `q`, and consecutive boundary
layers can be joined by two radial unit-transfer edges.  For three slots
the boundary quotient is literally a cycle, so the induction closes.

For general `q`, the analogous shell is the rotation quotient of the
boundary of a `(q-1)`-dimensional simplex lattice.  Complement duality and
the three-slot theorem do not prove that this higher-dimensional shell
has a Hamilton cycle or a near-perfect matching with two prescribed
radial sockets.  That protected shell statement is the exact remaining
Euclidean induction gate.
