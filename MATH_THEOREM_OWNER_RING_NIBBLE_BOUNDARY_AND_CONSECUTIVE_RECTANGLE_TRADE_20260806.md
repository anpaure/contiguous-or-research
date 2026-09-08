# Owner-ring nibble boundary and an exact consecutive-period rectangle trade

## Status

The owner-only antipodal-ring hypergraph has exceptionally small pair
codegree: for every admissible period its sharp normalized maximum is

\[
                         {2\over q(q-1)}.                \tag{0.1}
\]

This closes one isolated random bite uniformly in the growing period.  It
does **not** make a published variable-rank nibble give a near-perfect
matching.  Near-maximal periods fail the Kostochka--Rodl/Grable hypothesis
by a fixed constant; sublinear periods make the hypothesis tend to zero,
but residence forces period at least `2h=Theta(sqrt q)`, and the theorem's
leave exponent then tends to zero so quickly that its guaranteed uncovered
fraction is `1-o(1)`.

The q1-root shadow is an additional, exact obstruction: owner-disjoint
rings may repeat one root up to `floor(q/2)` times.  The root leave equals
the owner leave plus the complete root-collision excess.

There is nevertheless a useful integral move.  On a product of two tight
window cycles, `p+1` period-`p` rings and `p` period-`(p+1)` rings cover
exactly the same `p(p+1)` owners.  Their two q1-root palettes are simple and
disjoint.  This is a literal consecutive-period, owner-neutral root-shadow
absorber.  Turning a bank of these trades into an exact cover-down still
requires a named root-linkage theorem.

No computation or search is used.

## 1. Owner-ring hypergraph

Put

\[
 n=2q-1,\qquad W=\binom{2q-1}{q},\qquad s=q-h,          \tag{1.1}
\]

and let the ring period `p` satisfy

\[
                         2h\le p\le q+h-1.              \tag{1.2}
\]

An owner ring is specified by a core `K` of size `s`, a disjoint moving
set `F` of size `p`, and an unoriented cyclic order of `F`.  Its hyperedge
on the owner shore is

\[
 \mathcal O(K,F)=
   \{K\cup F[t,t+h):t\in\mathbb Z/p\mathbb Z\},        \tag{1.3}
\]

which contains `p` distinct rank-`q` owners.

### Proposition 1.1 (exact degree)

Every owner has degree

\[
 D_p
   =\binom qh\binom{q-1}{p-h}{h!(p-h)!\over2}
   ={(q)_h(q-1)_{p-h}\over2}.                          \tag{1.4}
\]

#### Proof

Fix an owner `O`.  Choose `K subset O` in `binom(q,h)` ways and choose the
remaining `p-h` moving labels outside `O` in `binom(q-1,p-h)` ways.  In a
cyclic order of `F`, contract the fixed `h`-set `O-K` to one block.  There
are `(p-h)!` oriented cyclic orders of the resulting objects and `h!`
internal orders; quotient by reversal.  This is (1.4). \(\square\)

### Proposition 1.2 (sharp adjacent-owner codegree)

If `O,O'` are Johnson adjacent, their codegree is

\[
 C_p
  =\binom{q-1}{s}\binom{q-2}{p-h-1}
       (h-1)!(p-h-1)!,                                 \tag{1.5}
\]

and therefore

\[
                         {C_p\over D_p}={2\over q(q-1)}.\tag{1.6}
\]

The complete owner-pair audit shows that (1.5) is the maximum codegree
among distinct owners.

#### Proof

Write `O=I+x,O'=I+y`, where `|I|=q-1`.  The core must be an `s`-subset of
`I`.  After it is chosen, the two residual `h`-sets overlap in `h-1`
labels and must be adjacent cyclic windows.  Order their common
`(h-1)`-set, put `x,y` at its two ends, contract the resulting path, and
order the remaining cyclic objects.  After quotienting reversal this gives
the factorial factor in (1.5); the second binomial chooses the remaining
moving labels.

Dividing by (1.4) gives

\[
 2\,{h\over q}\,{p-h\over q-1}\,{1\over h}\,{1\over p-h}
 ={2\over q(q-1)}.
\]

The maximum assertion is the exact owner-pair classification input; the
present calculation identifies its attaining row. \(\square\)

## 2. What a direct growing-rank nibble actually yields

Let

\[
                         \eta_p
  ={p\Delta_2\log W\over D_p}.                          \tag{2.1}
\]

Using (1.6) and

\[
                         \log W=(2\log2+o(1))q,         \tag{2.2}
\]

we obtain the exact scale

\[
                         \eta_p
   =(4\log2+o(1)){p\over q}.                            \tag{2.3}
\]

### Theorem 2.1 (published variable-rank nibble boundary)

The Grable--Kostochka--Rodl variable-rank theorem does not prove an
`o(W)` owner leave for any residence-compatible period in (1.2).

#### Proof

If `p/q` has a positive lower bound, (2.3) does not tend to zero, so the
theorem's hypothesis fails.

Suppose instead that `p=o(q)`.  The hypothesis now holds.  The theorem's
quantitative uncovered fraction has the form

\[
                \eta_p^{1/(2p-1+o(p))}.               \tag{2.4}
\]

Residence requires `p>=2h`, and at triangular depth
`h=Theta(sqrt q)`.  Since `eta_p>=q^{-1+o(1)}` throughout the admissible
range,

\[
 {\log(1/\eta_p)\over2p-1+o(p)}
       =O\!\left({\log q\over\sqrt q}\right)=o(1).     \tag{2.5}
\]

Thus (2.4) is `exp(-o(1))=1-o(1)`, not `o(1)`.  The published theorem may
select a nontrivial packing, but its asserted leave is asymptotically
almost the whole owner shore. \(\square\)

The fixed-uniformity Pippenger--Spencer theorem cannot be diagonalized in
`p`, and the current Gould--Kelly hierarchy also fixes `p` before sending
the degree to infinity.  Hence (2.4) is the strongest currently audited
direct variable-rank conclusion from the maximum codegree alone.

At the smallest legal period `p=2h`, the main expression in (2.4) is

\[
  \exp\!\left[-\Theta\!\left({\log q\over h}\right)\right]
   =1-\Theta\!\left({\log q\over\sqrt q}\right).       \tag{2.5a}
\]

Thus even its best residence-compatible calibration certifies only an
`O(W log q/sqrt q)`-scale covered set, not a near-factor.

### Proposition 2.2 (one isolated bite remains valid)

For any fixed `0<gamma<=1`, mark each ring independently with probability

\[
                         {\gamma\over pD_p}
\]

and retain it if it meets no other marked ring in an owner.  The retained
rings form an owner matching which covers

\[
       {\gamma e^{-\gamma}\over p}
       \left(1+O\!\left({1\over q}\right)\right)W      \tag{2.6}
\]

owners in expectation, and hence in some outcome.

#### Proof

For one ring, the normalized internal overlap parameter is bounded by

\[
 {1\over p}\binom p2{2\over q(q-1)}
       =O(p/q^2)=O(1/q).                                \tag{2.7}
\]

The growing-uniformity isolated-bite lemma therefore applies with edge
size `p`, degree `D_p`, and error `O(1/q)+D_p^{-1}`.  Equation (2.6) is its
coverage formula. \(\square\)

Iterating (2.6) for `Theta(p log q)` rounds would give a useful leave only
if the residual ring hypergraph regenerated its degrees and overlap
profile.  Time-zero regularity and (1.6) do not prove that hereditary
statement.

## 3. Exact root-shadow ledger

For a selected owner-ring matching `mathcal M`, let `mu(Q)` be the number
of selected rings whose width-`(h-1)` root row contains the rank-`(q-1)`
set `Q`.  Put

\[
 U_O=W-p|\mathcal M|,
 \qquad
 E_Q=\sum_Q(\mu(Q)-1)_+.                               \tag{3.1}
\]

### Theorem 3.1 (root leave equals owner leave plus collision excess)

The number of q1 roots not covered by `mathcal M` is exactly

\[
                         \boxed{U_Q=U_O+E_Q}.           \tag{3.2}
\]

Moreover

\[
                         \mu(Q)\le\left\lfloor{q\over2}\right\rfloor
                                                               \tag{3.3}
\]

for every root `Q`.

#### Proof

The selected rings contribute `p|mathcal M|` root occurrences.  Their
number of distinct values is

\[
 p|\mathcal M|-\sum_Q(\mu(Q)-1)_+=p|\mathcal M|-E_Q.
\]

Subtract from the `W` roots and use (3.1), proving (3.2).

Whenever a ring contains `Q` in its q1 row, the two owners adjacent to that
root are two distinct members of the `q`-element star

\[
                         \{Q+x:x\notin Q\}.             \tag{3.4}
\]

Different selected rings have disjoint owner rows, so their pairs in
(3.4) are disjoint.  At most `floor(q/2)` such pairs exist, proving
(3.3). \(\square\)

Thus an owner-perfect matching has a root-perfect shadow if and only if
`E_Q=0`.  Owner codegree alone controls neither `E_Q` nor its distribution.
The coupled owner/root packet hypergraph removes this ambiguity, but its
incident cross-codegree is of relative order `1/q`, not `1/q^2`; a direct
maximum-codegree growing-rank theorem is even farther from its useful
range.

## 4. An exact consecutive-period rectangle trade

For the two rectangle trades below assume `h>=2`.  (This is automatic in
the asymptotic triangular-depth regime.  At `h=1` the `(h-1)`-window
palettes collapse and the asserted simplicity is false.)

Assume

\[
             2h\le p\le {q+2h-2\over2}.               \tag{4.1}
\]

Choose pairwise disjoint sets

\[
 B,\quad X,\quad Y,\quad Z                           \tag{4.2}
\]

with

\[
 |B|=q-2h,\qquad |X|=p+1,\qquad |Y|=p,
 \qquad |Z|=q+2h-2p-2.                                \tag{4.3}
\]

Their sizes sum to `2q-1`.  Give `X` and `Y` cyclic orders and put

\[
 R_i=X[i,i+h)\quad(i\in\mathbb Z/(p+1)\mathbb Z),
 \qquad
 C_j=Y[j,j+h)\quad(j\in\mathbb Z/p\mathbb Z).         \tag{4.4}
\]

Define

\[
                         O_{ij}=B\cup R_i\cup C_j.     \tag{4.5}
\]

### Theorem 4.1 (owner-neutral rectangle absorber)

The `p(p+1)` owners in (4.5) are distinct and admit two exact ring
decompositions:

1. `p+1` row rings of period `p`, with row `i` having core `B union R_i`
   and moving cycle `Y`;
2. `p` column rings of period `p+1`, with column `j` having core
   `B union C_j` and moving cycle `X`.

Both modes are biresident at deadline `h-1` and use the same number of
source positions.

#### Proof

Every set in (4.5) has rank `(q-2h)+h+h=q`.  Its intersections with the
disjoint banks `X,Y` recover `(R_i,C_j)`, so all values are distinct.

For fixed `i`, the sets `C_j` are exactly the `h`-windows of the period-`p`
cycle `Y`; adjoining the fixed core `B union R_i` gives the row ring.  The
column assertion is symmetric.  The two total lengths are both
`p(p+1)`.  Since both periods are at least `2h`, every moving coordinate
has owner run at least `h` and gap at least `h`; core and unused
coordinates are constant. \(\square\)

### Theorem 4.2 (the two q1-root palettes are simple and disjoint)

The row mode has roots

\[
 Q^{\rm row}_{ij}
  =B\cup R_i\cup(C_j\cap C_{j+1}),                    \tag{4.6}
\]

and the column mode has roots

\[
 Q^{\rm col}_{ij}
  =B\cup(R_i\cap R_{i+1})\cup C_j.                    \tag{4.7}
\]

Each family consists of `p(p+1)` distinct rank-`(q-1)` sets, and the two
families are disjoint.  Their immediate-upper palettes are likewise
simple and disjoint.

#### Proof

Consecutive tight windows intersect in rank `h-1`.  Hence (4.6)--(4.7)
have rank `(q-2h)+h+(h-1)=q-1`.  The separate `X` and `Y` traces recover
the two indices, proving simplicity.

Every row root contains `h` elements of `X` and `h-1` of `Y`, while every
column root contains `h-1` of `X` and `h` of `Y`; they cannot coincide.

For immediate uppers replace the intersections in (4.6)--(4.7) by unions
of consecutive windows.  Row uppers have `(h,h+1)` elements on `(X,Y)`
and column uppers have `(h+1,h)`, giving the same simplicity and
disjointness argument. \(\square\)

Thus switching the rectangle changes no owner or source length and remains
biresident in both modes, but it does change the literal core/moving
residence pattern.  It exchanges one complete q1-root palette for a
disjoint palette of the same size.  It is an exact two-mode absorber for
root-shadow defects.
What remains is a packing/linkage theorem selecting disjoint rectangles so
that the desired missing roots occur in one mode and the roots surrendered
by the switch have alternative providers.

## 5. The dual rectangle fixes roots and switches owners

There is an exact companion trade on the other central shore.  Assume

\[
             2h\le p\le {q+2h-3\over2}.               \tag{5.1}
\]

Choose pairwise disjoint sets `B,X,Y,Z` with

\[
 |B|=q-2h+1,\qquad |X|=p+1,\qquad |Y|=p,
 \qquad |Z|=q+2h-2p-3.                                \tag{5.2}
\]

Give `X` and `Y` cyclic orders and use their `(h-1)`-windows

\[
 R_i=X[i,i+h-1),\qquad C_j=Y[j,j+h-1).                \tag{5.3}
\]

Define rank-`(q-1)` roots

\[
                         Q_{ij}=B\cup R_i\cup C_j.      \tag{5.4}
\]

### Theorem 5.1 (root-neutral rectangle absorber)

The `p(p+1)` roots in (5.4) are distinct and admit two exact ring
decompositions:

1. `p+1` row rings of period `p`, with row `i` having core
   `B union R_i` and moving cycle `Y`;
2. `p` column rings of period `p+1`, with column `j` having core
   `B union C_j` and moving cycle `X`.

The two modes use the same roots and total source length.  Their owner
palettes are

\[
 \begin{aligned}
 O^{\rm row}_{ij}
   &=B\cup R_i\cup(C_j\cup C_{j+1}),\\
 O^{\rm col}_{ij}
   &=B\cup(R_i\cup R_{i+1})\cup C_j.                  \tag{5.5}
 \end{aligned}
\]

Each owner palette is simple, and the two palettes are disjoint.  Their
immediate-upper palettes are likewise simple and disjoint.  Both modes are
biresident at deadline `h-1`.

#### Proof

The core of a row ring has size

\[
             (q-2h+1)+(h-1)=q-h,
\]

and adjoining the `(h-1)`-windows of `Y` gives exactly (5.4).  Consecutive
such windows have union of size `h`, giving the first line of (5.5).  The
column assertion is symmetric.  Intersecting with the disjoint banks
`X,Y` recovers `(i,j)`, so all roots in (5.4) are distinct.

A row owner has bank-size signature `(h-1,h)` on `(X,Y)`, whereas a
column owner has signature `(h,h-1)`.  This proves cross-mode disjointness;
the indices separately prove simplicity inside either mode.  Immediate
uppers have signatures `(h-1,h+1)` and `(h+1,h-1)`, so the same argument
applies.  Finally `p,p+1>=2h`, and every moving coordinate has owner run
and gap at least `h`; core and unused coordinates are constant.  Both
modes have total length `p(p+1)`. \(\square\)

### Corollary 5.2 (two-sided central mode basis)

Theorems 4.1 and 5.1 give complementary zero-length trades:

\[
 \begin{array}{c|cc}
 &\text{owner palette}&\text{root palette}\\ \hline
 \text{Theorem 4.1}&\text{fixed}&\text{switched disjointly}\\
 \text{Theorem 5.1}&\text{switched disjointly}&\text{fixed}.
 \end{array}                                           \tag{5.6}
\]

Thus neither central shore is intrinsically frozen in a prepared
rectangle.  This does not yet absorb an arbitrary paired leave: one switch
moves a complete `p(p+1)` palette.  A global proof still needs a spread
rectangle packing and a linkage/telescoping theorem expressing the actual
owner and root collision vectors in the integer span of the mode
differences while preserving upper and masked-port tickets.

## 6. Strongest proof-safe conclusion

The owner-only pair geometry proves an efficient first bite but no audited
black-box theorem turns it into a near-perfect residence-compatible cover.
The obstruction is quantitative, not merely the phrase “growing
uniformity”: every admissible period lies outside the useful leave range of
the strongest variable-rank pair-codegree theorem.

The two consecutive-period rectangles are genuine integral absorber
candidates.  They make the root correlation explicit while allowing either
central shore to move with the other held fixed.  The shortest remaining
theorem in this lane is therefore:

> construct a near-owner-factor together with a spread bank of disjoint
> consecutive-period rectangles whose owner and root modes absorb the
> complete paired collision/leave vector, while preserving the masked-port
> and upper-witness tickets.

No exact or bounded-leave cover-down is claimed here.
