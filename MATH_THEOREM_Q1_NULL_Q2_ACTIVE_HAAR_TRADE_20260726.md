# A complete physical `q=1`-null, `q=2`-active wreath trade

Date: 2026-07-26

Method: pure finite mathematics.  The displayed certificate is taken from
`NONLOCAL_HAAR_M4.md`; the complete lower/upper interpretation and the
minimal-dimension statement are proved here.

## 0. Outcome

There is a literal four-for-four trade of cyclic wreaths on nine
coordinates such that

1. both shores partition exactly the same `36` middle owners;
2. the complete multiset of physical depth-one lower intersections is the
   same on both shores;
3. the complete multiset of physical depth-one upper unions is the same on
   both shores; and
4. the depth-two lower-target multiset changes nontrivially.

Thus a finite depth-separating exact-factor trade already exists.  It is
the certified nonlocal `m=4` Haar edge.  No tensor, multiplicity, fractional
owner, or separate choice at different depths is used.

The ambient rank `m=4` is smallest possible.  At `m<=3` no equal-row-count
trade can have a nonzero depth-two effect after imposing exact middle and
depth-one neutrality.

The eight-owner cross-sector rectangle cannot itself have this property:
on its support every upper depth-one label determines its physical edge.
The `24`-owner pair-frame associator is an exact trade, but its displayed
first-shadow ledger is nonzero.  The four-for-four Haar edge is therefore
the first currently certified complete physical solution beyond those
local primitives.  Absolute minimality in the number of rows at `m=4` is
not claimed.

## 1. Physical shadow notation

Let `n=2m+1`.  For an omitted-label order

\[
                         q=(q_0,\ldots,q_{n-1}),
\]

put

\[
 I_i^{(r)}(q)=
 \{q_i,q_{i+2},\ldots,q_{i+2r-2}\},
 \qquad i\in Z_n,
\]

and

\[
                         B_re_q=\sum_{i\in Z_n}e_{I_i^{(r)}(q)}.
\]

The step-two order is a cyclic order because `gcd(2,n)=1`.  Its
middle owners are the `m`-intervals `I_i^(m)`.

Two consecutive middle owners have

\[
 I_i^{(m)}\cap I_{i+2}^{(m)}=I_{i+2}^{(m-1)},
 \qquad
 I_i^{(m)}\cup I_{i+2}^{(m)}=I_i^{(m+1)}.           \tag{1.1}
\]

Similarly, three consecutive middle owners have lower intersection
`I_(i+4)^(m-2)` and upper union `I_i^(m+2)`.  Therefore, for a signed row
trade `w`,

\[
 \begin{array}{c|c}
 \text{physical ledger}&\text{signed incidence}\ \hline
 \text{middle owners}&B_mw\\
 q=1\text{ lower intersections}&B_{m-1}w\\
 q=1\text{ upper unions}&B_{m+1}w\\
 q=2\text{ lower intersections}&B_{m-2}w\\
 q=2\text{ upper unions}&B_{m+2}w.
 \end{array}                                        \tag{1.2}
\]

### Lemma 1.1 (complement transfer)

Let `C_r` be the coordinate-complement bijection from rank `r` to rank
`n-r`.  Then

\[
                         B_{n-r}w=C_rB_rw.           \tag{1.3}
\]

#### Proof

The complement of `I_i^(r)` is the consecutive `(n-r)`-interval beginning
immediately after it in the same step-two cyclic order.  As `i` runs over
`Z_n`, this is merely a cyclic reindexing.  Apply the complement bijection
coordinatewise and sum. \(\square\)

Consequently exact middle ownership `B_mw=0` automatically gives
`B_(m+1)w=0`, and lower `q=1` neutrality `B_(m-1)w=0` automatically gives
upper `q=2` neutrality `B_(m+2)w=0`.

## 2. The four-for-four certificate

Set `m=4,n=9`.  Take the four negative orders

```text
1 8 6 7 4 5 3 9 2
1 9 8 6 7 4 5 2 3
1 5 3 9 8 6 7 2 4
1 7 3 9 4 5 8 2 6
```

and the four positive orders

```text
1 9 3 5 4 7 6 8 2
1 5 4 7 6 8 9 2 3
1 7 6 8 9 3 5 2 4
1 8 5 4 9 3 7 2 6
```

Write `N,P` for these row families and

\[
                         w={\bf1}_P-{\bf1}_N.        \tag{2.1}
\]

The direct finite certificate is

\[
                         B_4w=0,\qquad B_3w=0,       \tag{2.2}
\]

and

\[
 \boxed{
 B_2w=-e_{13}+e_{23}+e_{14}-e_{24}
       +e_{15}-e_{25}-e_{19}+e_{29}\ne0.}           \tag{2.3}
\]

Every shore consists of four pairwise middle-disjoint wreaths.  Hence
each shore contains `4*9=36` distinct middle owners, and (2.2) says that
the two owner sets are identical.  The replacement is therefore an exact
zero-one owner partition trade.

Moreover the bipartite ownership overlap between the four negative and
four positive rows is connected.  In the certified construction it is one
interaction component for the final coordinate transposition `(1 2)`.
Thus the four-for-four exchange is a single legal component switch, not a
formal sum whose summands require incompatible completions.

For reference, both shores have the following common ten-row completion:

```text
1 4 6 9 7 8 5 3 2
1 6 5 7 3 9 8 4 2
1 3 8 6 7 5 9 4 2
1 4 6 2 8 9 5 7 3
1 4 6 5 2 9 7 8 3
1 5 4 2 6 9 7 8 3
1 8 6 7 5 9 2 3 4
1 8 7 9 4 2 5 3 6
1 7 2 3 5 9 8 4 6
1 8 7 9 2 3 4 5 6
```

Thus adjoining `N` or `P` gives an exact fourteen-wreath factor of the
entire middle layer `binom([9],4)`.

### Theorem 2.1 (complete physical depth separation)

The trade (2.1) preserves both complete physical signed depth-one shadow
multisets and changes the lower depth-two multiset.  Explicitly,

\[
 \boxed{
 B_3w=B_5w=0,
 \qquad
 B_2w\ne0.}                                         \tag{2.4}
\]

Its upper depth-two change is zero:

\[
                         B_6w=0.                     \tag{2.5}
\]

#### Proof

The lower depth-one assertion is the second equality in (2.2).  Exact
middle ownership is the first.  Lemma 1.1 gives

\[
 B_5w=C_4B_4w=0,
 \qquad
 B_6w=C_3B_3w=0.
\]

Equation (2.3) proves the nonzero lower depth-two action.  By (1.1)--(1.2)
these are exactly the physical intersection and union ledgers, including
every cyclic seam. \(\square\)

### 2.1 Hand audit of the rank-two signs

The last two signs in (2.3) are essential.  For transparency, the nine
rank-two intervals of each printed order, written as unordered pairs, are

\[
\begin{array}{c|l}
N_1&16,78,46,57,34,59,23,19,28\\
N_2&18,69,78,46,57,24,35,12,39\\
N_3&13,59,38,69,78,26,47,12,45\\
N_4&13,79,34,59,48,25,68,12,67\\ \hline
P_1&13,59,34,57,46,78,26,18,29\\
P_2&14,57,46,78,69,28,39,12,35\\
P_3&16,78,69,38,59,23,45,12,47\\
P_4&15,48,59,34,79,23,67,12,68.
\end{array}                                           \tag{2.6}
\]

Canceling the common entries in (2.6) leaves precisely

\[
                         -13+14+15-19+23-24-25+29.
\]

In particular every coordinate degree is zero, as it must be for an
equal-row-count trade:

\[
\begin{array}{c|rrrrrr}
x&1&2&3&4&5&9\\ \hline
\deg_x(B_2w)&-1+1+1-1&1-1-1+1&-1+1&1-1&1-1&-1+1.
\end{array}                                           \tag{2.7}
\]

Thus the alternative transcription with `+e_19-e_29` is impossible; the
certificate and (2.3) have `-e_19+e_29`.

The support effect in (2.3) is two elementary rectangles with common
axis `{1,2}`.  The important point is that their first-shadow boundary
terms have already been closed inside one genuine exact-factor component;
they are not three separately completed signed relations.

## 3. Why the eight-owner rectangle cannot solve the problem

Use the six-coordinate rectangle notation

\[
 P=\{t,e\},\qquad A=\{a,b,c,d\},\qquad
 \Omega=\{\{p,z\}:p\in P,z\in A\}.
\]

The induced Johnson graph on `Omega` is the rook graph `K_2 square K_4`.
Every one of its physical edges is of one of the forms

\[
 \{pz,pz'\}
 \quad\text{or}\quad
 \{tz,ez\}.                                         \tag{3.1}
\]

Its upper-union label is respectively

\[
                         pzz'\quad\text{or}\quad tez.\tag{3.2}
\]

### Proposition 3.1 (upper-label rigidity on eight owners)

On `Omega`, the map

\[
 \{\text{physical Johnson edges}\}
 \longrightarrow { [6]\choose3},
 \qquad E\longmapsto\bigcup E
\]

is injective.  Consequently two cycle factors on `Omega` with the same
upper depth-one multiset have the same edge set and hence the same cycles.
They cannot have different depth-two shadows.

#### Proof

For a label `pzz'`, the only vertices of `Omega` contained in it are
`pz,pz'`; the third two-subset `zz'` is not in `Omega`.  For a label `tez`,
the only vertices are `tz,ez`; the third two-subset `te` is not in
`Omega`.  Thus (3.2) recovers the edge uniquely.

Equality of the upper-label multisets therefore gives equality of the
edge multisets.  A simple two-regular graph is determined by its edge set,
including its cycle decomposition and every consecutive deeper window.
\(\square\)

In particular the three matching resolutions of the eight-owner packet
have identical lower depth-one multisets but genuinely different upper
ones.  No commutator confined to that same eight-owner support can be
complete-`q=1`-null and deeper-active.

## 4. Relation to the `24`-owner associator

The `24`-owner pair-frame associator is an exact six-for-six owner trade,
but relative to its original pair frame its first-shadow type ledger is

\[
 \begin{array}{c|cc}
 &\text{old}&\text{new}\ \hline
 \text{lower}&16f_0+8f_1&24f_0\\
 \text{upper}&16f_1+8f_2&24f_1.
 \end{array}                                        \tag{4.1}
\]

Thus the primitive itself is not depth-one null.  It proves that pair
type is movable, while Theorem 2.1 proves that a bounded nonlocal
commutator can close the entire physical first-shadow boundary and retain
a deeper direction.

The two results are complementary: the associator is a transparent local
carrier; the Haar edge is the first certified closed depth separator.

## 5. Minimal ambient rank

### Proposition 5.1

No complete physical `q=1`-null, `q=2`-active equal-row-count wreath trade
exists for `m<=3`.  Hence `m=4` in Theorem 2.1 is minimal.

#### Proof

For `m<=2`, the lower depth-two layer is empty or rank zero and is
row-independent.  The complementary upper layer is likewise
row-independent: at `m=2,n=5` it is the complement of the singleton
ledger, and every cyclic order contains every singleton exactly once.

For `m=3,n=7`, every
cyclic order has each singleton exactly once among its length-one
intervals.  Therefore

\[
                         B_1e_q=\sum_{x\in[7]}e_{\{x\}}
\]

is independent of `q`.  Any trade with equally many positive and negative
rows has `B_1w=0`, so its lower depth-two effect is zero.

Its upper depth-two incidence is `B_5w=C_2B_2w` by Lemma 1.1.  Complete
lower depth-one neutrality at `m=3` is precisely `B_2w=0`, so the upper
depth-two effect also vanishes.  Thus no depth-two target changes.
\(\square\)

This proves minimality of the dimension, not of the four-row shore size.
A classification excluding two-for-two or three-for-three `m=4` trades
with (2.4) is not presently available.

There is nevertheless a universal support lower bound.  A one-for-one
trade is trivial: the family of middle intervals of one cyclic order
determines its unoriented cyclic order.  Indeed, two coordinates are
cyclically adjacent exactly when they occur together in the maximum
possible number `m-1` of its middle intervals.  Hence equality of two
middle supports gives the same row up to rotation and reversal, and all
shadow ledgers agree.  A nontrivial `m=4` trade therefore needs at least
two rows and at least `2n=18` middle owners per shore.  The certified
construction uses four rows and `36` owners, leaving only the two- and
three-row cases between the elementary lower bound and the positive
example.

## 6. Exact implication boundary

The finite existence question in the task is resolved positively by
Theorem 2.1.  The remaining difficulty is not discovering a seed trade;
it is a suspension theorem which embeds many copies in growing exact
factors while preserving the complete cyclic collars.

The direct port substitution of the printed `m=4` factors is obstructed:
after every relabeling/rooting, their selected Dyck roots cannot all be
made canonical endpoint ports.  Therefore a successful suspension must
reroute endpoints, add a bounded selector/collar, or reproduce the
preparatory commutator inside the parent context.  That is a separate
all-dimensional problem and does not weaken the finite theorem above.
