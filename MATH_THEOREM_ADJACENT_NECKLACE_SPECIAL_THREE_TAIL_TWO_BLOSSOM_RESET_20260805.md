# Adjacent necklaces: an exact three-tail reset for the special `q=3 mod 6` fibre

**Date:** 2026-08-05  
**Method:** one noncritical product gradient, two odd circulation blossoms,
and four explicit path-product matchings; no computation  
**Status:** unconditional local reset.  For every odd `q=3 mod 6`, the
special odd path can be saturated, except that `q=3` supplies the single
parity socket.  For `q>=21` the construction uses exactly two distinct
deleted-cut hub colours.  A global ordinary-sector selector must reserve
those two colour classes; robustness of that selector is not proved here.

## 1. Input and statement

Write

\[
                         q=6b+3.
\tag{1.1}
\]

The enlarged special macro fibre is the odd path

\[
 S_0-S_1-\cdots-S_{2b},
 \qquad
 S_r=(3^r,q-3r)\ (r<2b),\qquad S_{2b}=(3^{2b+1}).
\tag{1.2}
\]

The direct critical exits occur only at odd `r`.  Moreover, if an even
vertex `S_(2s)` is sent through the one-product ear of the capacity-two
theorem, the exit lies on the minority shore of the target odd product.
Thus neither a direct exit nor that one-product two-tail ear can saturate
the special path.

The construction below uses the smallest repair consistent with both
obstructions: one even special tail, followed by two circulation-blossom
tails.  Put

\[
                    2\le s\le b-1,
 \qquad             c=b-s\ge1.
\tag{1.3}
\]

Such an `s` exists exactly when `b>=3`, or `q>=21`.

### Theorem 1.1 (three-tail two-blossom reset)

For every `q=6b+3>=21` and every `s` satisfying (1.3), there is a finite
ambient adjacent-transfer subgraph with the following properties.

1. It meets the special path in exactly `S_(2s)`.
2. It uses one noncritical even-by-even product fibre and three ordinary
   critical macro fibres.
3. It contains two circulation blossoms with distinct deleted-cut hub
   necklace orbits.
4. After deleting `S_(2s)` from the special path, the union of the
   remaining special path and the entire reset subgraph has a perfect
   matching.

In particular the special `q=3 mod 6` path exports no socket for `q>=21`.

The two blossom hub colours are explicit.  They must be contracted in the
one-use hub partition matroid before an independent ordinary-sector
selection is made.

## 2. The even special tail and its noncritical product

Use the notation of the one-product-ear theorem.  The direct shift out of
`S_(2s)` enters the noncritical macro base

\[
             F=(A,B)=(6s+1,6c+2)
\tag{2.1}
\]

at

\[
                         x=(2s-1,0)
\tag{2.2}
\]

in the literal fibre

\[
                         P_{2s}\mathbin\square P_{2c}.
\tag{2.3}
\]

Choose the exit

\[
                         y=(2s-3,1).
\tag{2.4}
\]

Its coordinate parity is even, opposite to the odd parity of `x`.  The
boundary move which repairs the noncritical residues `(1,2)` sends `y` to

\[
 z=(2s-3,0,0)
\tag{2.5}
\]

in the critical macro fibre

\[
 T=(6s,4,6c-1)
   \cong P_{2s-1}\mathbin\square P_1\mathbin\square P_{2c-1}.
\tag{2.6}
\]

Thus `z` is on the minority shore of the odd-by-odd product, exactly as
predicted by the one-product-ear parity lock.

### Lemma 2.1

The graph `F-{x,y}` has a perfect matching.

#### Proof

Write `p=2s` and `r=2c`, and use coordinates
`0<=i<p`, `0<=j<r`.  For every `j>=2`, match

\[
                         (i,2h)(i,2h+1).
\tag{2.7}
\]

On columns zero and one, use `(i,0)(i,1)` for `i<=p-4`.  The four
remaining vertices are matched by

\[
 (p-3,0)(p-2,0),
 \qquad
 (p-2,1)(p-1,1).
\tag{2.8}
\]

The two omitted vertices are precisely `y=(p-3,1)` and `x=(p-1,0)`.
All displayed pairs are path-product edges. \(\square\)

Use the external matching edges `S_(2s)x` and `yz`, together with the
matching of Lemma 2.1.

## 3. Paying the minority exit with two majority tails

Suppress the singleton middle coordinate of `T`, and put

\[
 u=(2s-4,0),\qquad z=(2s-3,0),\qquad v=(2s-2,0).
\tag{3.1}
\]

These are three consecutive boundary vertices.  Their parities are
even, odd, even, respectively.

### Lemma 3.1

The graph `T-{u,z,v}` has a perfect matching.

#### Proof

The first path has odd order `2s-1` and the second has odd order `2c-1`.
On boundary column zero the deletion in (3.1) removes the final three
vertices.  Pair the remaining `2s-4` vertices consecutively.  The other
`2c-2` columns are paired as `(1,2),(3,4),...` independently in every
row. \(\square\)

The two majority vertices have literal shifted-cut neighbours.  In gap
words, the relevant local moves are

\[
 \begin{aligned}
 u:&\quad (3^{2s-4},12,4,6c-1)
       \longleftrightarrow
       (3^{2s-4},11,5,6c-1)=:u',\\
 v:&\quad (3^{2s-2},6,4,6c-1)
       \longleftrightarrow
       (3^{2s-2},5,5,6c-1)=:v'.
 \end{aligned}
\tag{3.2}
\]

Both new endpoints belong to the same critical macro fibre

\[
 U=(6s-1,5,6c-1)
   \cong P_{2s-1}\mathbin\square P_1\mathbin\square P_{2c-1},
\tag{3.3}
\]

at coordinates

\[
                         u'=(2s-4,0),
 \qquad                  v'=(2s-2,0).
\tag{3.4}
\]

Lift both shifted-cut edges in (3.2) by the odd circulation-blossom
theorem.  Their deleted-cut hubs are

\[
 \begin{aligned}
 h_u&=(3^{2s-4},16,6c-1),\\
h_v&=(3^{2s-2},10,6c-1).
\end{aligned}
\tag{3.5}
\]

They lie in the common critical macro fibre

\[
D=(6s+4,6c-1)
   \cong P_{2s+1}\mathbin\square P_{2c-1}
\tag{3.6}
\]

at coordinates `2s-4` and `2s-2` on its first factor.

### Lemma 3.2 (the two hub colours are distinct)

The necklace orbits of `h_u` and `h_v` are distinct.

#### Proof

The first word in (3.5) contains a part of size sixteen and no part of
size ten.  The second contains a part of size ten and no part of size
sixteen.  The remaining exceptional part `6c-1` is odd, and all other
parts are threes.  Hence no cyclic rotation identifies the two words.
\(\square\)

The two circulation blossoms are therefore hub-rainbow.  Their endpoint
levels differ by two: the first edge has `2s-1` gaps and the second has
`2s+1` gaps.  This causes no hidden cross-level collision.  A nonhub
circulation vertex coming from a `k`-gap cut state has either `k` or
`k-1` zero coordinates: the travelling chip can fill at most one old
zero, and it creates none.  The possible zero counts for levels `2s-1`
and `2s+1` are disjoint.  Together with fixed-level interior injectivity,
this proves that the two blossom interiors are disjoint, even after the
rotation quotient.  They are also disjoint from every cut and hub state
because a nonhub circulation state has the distinguished zero preceded by
one rather than two.

## 4. The two residual sockets cancel by one merge edge

Define the midpoint vertices

\[
 w_U=(2s-3,0)\in U,
 \qquad
w_D=(2s-3,0)\in D.
\tag{4.1}
\]

In literal gap words they are

\[
 \begin{aligned}
 w_U&=(3^{2s-3},8,5,6c-1),\\
w_D&=(3^{2s-3},13,6c-1).
\end{aligned}
\tag{4.2}
\]

Consequently

\[
                         w_U\longleftrightarrow w_D
\tag{4.3}
\]

is the literal cut deletion/insertion `8+5=13`.

### Lemma 4.1

Both

\[
 U-\{u',w_U,v'\}
 \quad\hbox{and}\quad
D-\{h_u,w_D,h_v\}
\tag{4.4}
\]

have perfect matchings.

#### Proof

For `U`, the three deleted vertices are the final three positions on
boundary column zero of an odd-by-odd grid.  Pair the even initial segment
of that column consecutively and pair all remaining columns in consecutive
pairs.

For `D`, the deleted first-factor coordinates are

\[
                         2s-4,2s-3,2s-2.
\]

They split boundary column zero into segments of lengths `2s-4` and two,
both even.  Pair within those segments.  Again the other `2c-2` columns
come in consecutive pairs. \(\square\)

Use the edge (4.3), the two matchings in Lemma 4.1, and the perfect
matching inside each circulation blossom.  Together with Sections 2 and
3, every vertex of the reset is saturated.

Finally, deleting `S_(2s)` splits the special path into paths of orders
`2s` and `2b-2s`, both even.  Their alternating path matchings complete
the proof of Theorem 1.1.

## 5. Rotation and fibre disjointness

No hidden quotient choice occurs in the four path products.  Their macro
residue words are respectively

\[
 (1,2),\qquad(0,4,5),\qquad(5,5,5),\qquad(4,5)\pmod 6.
\tag{5.1}
\]

The first, second, and fourth have trivial cyclic stabilizer because their
residues distinguish all positions.  The third could have a nontrivial
stabilizer only if all three literal parts were equal.  But `s>=2` gives
`6s-1>5`, so this is impossible.  Thus every displayed product is the
literal product, not a nontrivial odd quotient.

The four macro bases in (5.1) are distinct, so their fibres are disjoint.
Section 3 proves disjointness of both circulation interiors from those
fibres and from each other.  Hence the matching is valid on necklace
orbits, not merely on pointed representatives.

## 6. Small special fibres

The remaining values are exact.

* `q=3`: the special fibre is the singleton `(3)`.  It is the one allowed
  parity socket.
* `q=9`: match `S_1S_2` in the special path and use the literal cut edge

  \[
                            (9)\longleftrightarrow(4,5).
  \tag{6.1}
  \]

  The ordinary macro fibre `(4,5)` is a singleton, so (6.1) closes both
  remaining vertices.
* `q=15`: the two-blossom construction in
  `MATH_THEOREM_ADJACENT_NECKLACE_ODD_CIRCULATION_BLOSSOM_LIFT_20260805.md`,
  Theorem 6.1, gives an exact perfect matching of the complete critical
  bank, including the special vertex.

Therefore the special fibre itself is no longer an open parity
obstruction for any odd `q`.

## 7. Exact global interface

The reset is local but it is not colour-free.  It contracts exactly the
two hub partition classes represented by `h_u,h_v`.  Other split blocks or
other merged sites can have the same unpointed hub colours, so it would be
incorrect to let an independently chosen ordinary-sector matching use
either class again.

Accordingly the remaining global theorem is the following robust version
of the ordinary hub-coloured ear problem.

> After deleting the three ordinary macro fibres `T,U,D` already rematched
> by the reset, and after contracting the two hub colours `h_u,h_v`, match
> all remaining ordinary capacity-two sectors modulo their odd rotational
> stabilizers by a one-use hub-coloured ear family, leaving at most one
> prescribed radial socket.

Theorem 1.1 proves the formerly missing `>=3`-tail reset.  It does not prove
this robust ordinary-sector selector.  In particular, the two explicit
hub colours must not be dismissed merely because they are distinct from
one another.

## 8. Scope

Proved:

1. an explicit even-special exit through the noncritical product fibre;
2. exact payment of its wrong-shore defect by two majority tails;
3. two vertex-disjoint odd circulation blossoms with distinct hub colours;
4. exact matchings of all four punctured path-product fibres;
5. literal cancellation of the final two sockets by `8+5=13`; and
6. complete treatment of `q=3 mod 6`, with only the forced `q=3` socket.

Not proved:

1. the robust ordinary-sector hub-coloured ear selector after the two hub
   colours are contracted;
2. simultaneous packing with all earlier ambient matching stages;
3. protection of an arbitrary PBBS physical halo; or
4. any universal-word upper bound.
