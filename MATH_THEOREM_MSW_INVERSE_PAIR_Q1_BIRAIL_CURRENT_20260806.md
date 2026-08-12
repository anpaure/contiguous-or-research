# Native MSW inverse pairs give an exact q1 birail current

## Status

The canonical same-phase incidence `C6` cannot be used as a masked collar
inside the native Mütze--Standke--Wiechert wreath factor.  There is,
however, a different native move which is exact on both central shores.

Two inverse separated-double swaps preserve the complete rank-`m` window
palette.  Consequently they preserve both the rank-`m` root shore and the
complementary rank-`(m+1)` owner shore.  Every input and output component is
a shortest wreath, so residence is automatic.  The complete signed effect
on rank-`(m+2)` immediate-upper colours is only one four-term `2 x 2`
birail rectangle.

This is an exact all-parameter local theorem.  It does not assert that the
resulting q1 rectangles span every desired upper defect, preserve deeper
upper witnesses, or join the wreath components.

No computation or search is used.

## 1. The inverse two-row trade

Put

\[
                         N=2m+1,\qquad m\ge2.          \tag{1.1}
\]

Let `a,b,c,d` be distinct labels and let

\[
 X=(x_1,\ldots,x_{m-2}),\qquad
 Y=(y_1,\ldots,y_{m-1})                              \tag{1.2}
\]

be disjoint ordered banks, also disjoint from `a,b,c,d`.  Consider the two
old cyclic coordinate orders

\[
 \begin{aligned}
 r_0&=(a,b,X,c,d,Y),\\
 r_1&=(b,d,X,a,c,Y),                                 \tag{1.3}
 \end{aligned}
\]

and the two new orders obtained by swapping the two displayed adjacent
pairs in each row:

\[
 \begin{aligned}
 r'_0&=(b,a,X,d,c,Y),\\
 r'_1&=(d,b,X,c,a,Y).                                \tag{1.4}
 \end{aligned}
\]

For a cyclic order `r`, write `E_t(r)` for the multiset of its cyclic
length-`t` interval sets.

### Theorem 1.1 (exact central palette equality)

The paired trade satisfies

\[
       E_m(r_0)\mathbin{\dot\cup}E_m(r_1)
       =E_m(r'_0)\mathbin{\dot\cup}E_m(r'_1).         \tag{1.5}
\]

Consequently it also satisfies

\[
       E_{m+1}(r_0)\mathbin{\dot\cup}E_{m+1}(r_1)
       =E_{m+1}(r'_0)\mathbin{\dot\cup}E_{m+1}(r'_1).
                                                               \tag{1.6}
\]

#### Proof

For the first row, the only old-only length-`m` intervals are

\[
       Y+a,\qquad X+b+c,\qquad Y+d,                  \tag{1.7}
\]

and the only new-only intervals are

\[
       Y+b,\qquad X+a+d,\qquad Y+c.                  \tag{1.8}
\]

For the second row, (1.8) are exactly the old-only intervals and (1.7)
are exactly the new-only intervals.  Every other length-`m` interval is
unchanged.  The signed currents therefore cancel, proving (1.5).

On a cyclic ground of size `2m+1`, complementation is a bijection from
cyclic length-`m` intervals to cyclic length-`(m+1)` intervals.  Applying
it to (1.5) proves (1.6).  \(\square\)

Thus, in the middle-levels lift, the paired substitution is exact on the
rank-`m` roots and the rank-`(m+1)` owners.

## 2. The q1 current collapses to one rectangle

Put

\[
 Y^- =\{y_1,\ldots,y_{m-2}\},\qquad
 Y^+ =\{y_2,\ldots,y_{m-1}\}.                       \tag{2.1}
\]

For a set `S`, write `[S]` for its basis vector in the signed palette
space.

### Theorem 2.1 (exact lower-neighbour current)

The complete signed change of the length-`(m-1)` interval palette is

\[
 \boxed{
 \begin{aligned}
 \Delta_{m-1}
    ={}&[Y^-+a]+[Y^++d]\\
      &-[Y^-+d]-[Y^++a].                             \tag{2.2}
 \end{aligned}}
\]

In particular all effects involving the long bank `X` cancel, as do the
two intermediate endpoint labels `b,c`.

#### Proof

In `r_0 -> r'_0`, the old-only length-`(m-1)` intervals are

\[
 X+b,\quad X+c,\quad Y^-+d,\quad Y^++a,              \tag{2.3}
\]

and the new-only intervals are

\[
 X+a,\quad X+d,\quad Y^-+c,\quad Y^++b.              \tag{2.4}
\]

Indeed, a length-`(m-1)` cyclic interval changes only when it contains
exactly one member of one of the swapped adjacent pairs.  Reading the four
boundary starts gives (2.3)--(2.4).

In `r_1 -> r'_1`, the old-only intervals are

\[
 X+d,\quad X+a,\quad Y^-+c,\quad Y^++b,              \tag{2.5}
\]

and the new-only intervals are

\[
 X+b,\quad X+c,\quad Y^-+a,\quad Y^++d.              \tag{2.6}
\]

Adding the two signed currents cancels (2.3) against the `X` part of
(2.6), and cancels (2.4) against the corresponding part of (2.5).  The
four uncancelled terms are exactly (2.2).  \(\square\)

Let a bar denote complement in the `N`-coordinate ground.

### Corollary 2.2 (exact immediate-upper birail current)

In the central lift with roots of rank `m` and owners of rank `m+1`, the
complete rank-`(m+2)` immediate-upper current is

\[
 \boxed{
 \Delta_{\rm up,1}
   =[\overline{Y^-+a}]+[\overline{Y^++d}]
    -[\overline{Y^-+d}]-[\overline{Y^++a}].}          \tag{2.7}
\]

#### Proof

For every cyclic order on `2m+1` labels, complementation bijects its
length-`(m-1)` intervals with its length-`(m+2)` intervals.  Consecutive
rank-`(m+1)` owners have precisely those length-`(m+2)` unions.  Apply
complementation to (2.2).  \(\square\)

Equation (2.7) is a literal `2 x 2` switch: labels `a,d` exchange between
the two ordered boundary profiles `Y^-,Y^+`.  It is rank one as a signed
matrix current and has zero row and column marginals.

## 3. The abstract q1 current lattice is generated

Put `k=m-1`, and let `Lambda_k` be the integer lattice

\[
 \Lambda_k=
 \left\{z\in\mathbb Z^{\binom{[N]}k}:
       \sum_{S\ni x}z_S=0\quad\hbox{for every }x\in[N]\right\}.
                                                               \tag{3.1}
\]

The total-sum equation is automatic, because summing the equations in
(3.1) gives `k sum_S z_S=0`.

For a `(k-2)`-set `Z` and four distinct labels `r,s,a,d` outside `Z`, put

\[
 \square(Z;r,s\mid a,d)
   =[Z+r+a]+[Z+s+d]-[Z+r+d]-[Z+s+a].                 \tag{3.2}
\]

### Theorem 3.1 (all coordinate-balanced q1 currents are square-generated)

For `m>=3`, the lattice `Lambda_(m-1)` is generated over the integers by
the currents (3.2).  Moreover every generator (3.2) is the
length-`(m-1)` current of one inverse-pair move in a coordinate conjugate
of the canonical MSW factor.

#### Proof

Represent a nonnegative multiset of `k`-sets by a zero-one matrix: its rows
are the characteristic vectors of the sets.  Two such matrices have the
same column sums exactly when their multiset difference belongs to
`Lambda_k`.  The standard alternating-cycle proof for binary matrices with
fixed margins transforms one matrix into the other by `2 x 2` switches.
At the set level one switch is a symmetric exchange

\[
 [A]+[B]-[A-a+b]-[B-b+a],                            \tag{3.3}
\]

where `a in A-B` and `b in B-A`.  Applying this to the positive and
negative parts of an arbitrary `z in Lambda_k` shows that symmetric
exchanges generate `Lambda_k`.

It remains to decompose (3.3) into the local squares (3.2).  Put

\[
 H=A-a,\qquad H'=B-b.
\]

Both are `(k-1)`-sets avoiding `a,b`.  The Johnson graph on the
`(k-1)`-subsets of `[N]-{a,b}` is connected.  Choose a path

\[
 H=H_0,H_1,\ldots,H_t=H'.                            \tag{3.4}
\]

If `H_i=Z_i+r_i` and `H_(i+1)=Z_i+s_i`, then

\[
 \begin{aligned}
 &[H_i+a]-[H_i+b]-[H_{i+1}+a]+[H_{i+1}+b]\\
 &\hspace{35mm}=\square(Z_i;r_i,s_i\mid a,b).        \tag{3.5}
 \end{aligned}
\]

Summing (3.5) along (3.4) telescopes to (3.3).  This proves the lattice
statement.

For physical realization, write an arbitrary generator as (3.2), choose
the ordered bank `Y=(r,Z,s)`, and partition the remaining `m` coordinates
as the ordered `(m-2)`-bank `X` and two labels `b,c`.  Equations
(1.3)--(1.4) then realize precisely (3.2), up to sign.  One canonical MSW
inverse pair has exactly these ordered roles; a coordinate permutation
sends its complete exact factor and the pair to the prescribed labels.
Thus every square occurs in a coordinate conjugate of a native MSW factor.
\(\square\)

For `m=2`, the coordinate-incidence map on singleton targets has zero
kernel, so the corresponding statement is vacuous.

### Corollary 3.2 (no static q1 lattice obstruction)

Every two exact shortest-wreath factors have q1-upper occurrence vectors
with the same coordinate marginals, and their difference lies in the
integer span of native inverse-pair currents.

#### Proof

Every wreath row contributes one occurrence of each coordinate to exactly
`m+2` of its `N` cyclic length-`(m+2)` intervals.  Every exact factor has
the same number of rows.  Hence all coordinate marginals agree.  Apply
Theorem 3.1 after complementation.  \(\square\)

This corollary is a lattice statement across the coordinate orbit of the
MSW move.  It does **not** put all required generators in one fixed factor,
make them row-disjoint, or give a serial path through exact factors.

## 4. Residence and native MSW supply

### Proposition 4.1 (residence is unchanged)

Every coordinate in every one of the four rows has one owner run of length
`m+1` and one owner gap of length `m`.  Hence both phases are positively
and negatively resident at every deadline at most `m-1`.

#### Proof

The owners of one row are the cyclic length-`(m+1)` intervals in a
permutation of `2m+1` labels.  A fixed label lies in exactly `m+1`
consecutive owners and outside exactly the remaining `m`.  This argument
is independent of the cyclic order.  \(\square\)

The canonical MSW flip-order recursion supplies the old pairs (1.3) for
every Dyck block replacement

\[
          u\circ1100\circ v
             \longleftrightarrow
          u\circ1010\circ v,                         \tag{3.1}
\]

including the two boundary families.  The exact indexed supply is

\[
                     (2m-1)\operatorname{Cat}_{m-2}. \tag{3.2}
\]

Moreover, choosing the first aligned `1100/1010` block gives a row-disjoint
involutive packet which covers a `1-o(1)` fraction of the canonical MSW
rows.  These supply statements are the all-parameter theorems in
`MATH_THEOREM_MSW_TRIPLE_CARRIER_COMPENSATION_20260727.md`; no finite audit
is needed for (3.1)--(3.2).

### Proposition 4.2 (the proved canonical family cannot span q1)

Let

\[
 R_m=(2m-1)\operatorname{Cat}_{m-2}                 \tag{4.1}
\]

be the proved indexed family (3.2).  For every `m>=3`, its linear span is
a proper subspace of the coordinate-balanced q1-current space.

#### Proof

The rank-`(m+2)` target shore has

\[
 T_m=\binom{2m+1}{m+2}=\binom{2m+1}{m-1}            \tag{4.2}
\]

coordinates.  The coordinate-incidence matrix has row rank `2m+1`: if a
linear combination of its coordinate rows vanishes on every
`(m+2)`-set, exchanging one coordinate in a target shows that all
coefficients are equal, and then that common coefficient is zero.  Hence
the balanced-current space has dimension

\[
                         T_m-(2m+1).                  \tag{4.3}
\]

On the other hand,

\[
 {T_m\over R_m}
   ={4(2m+1)(2m-3)\over(m+1)(m+2)}.                 \tag{4.4}

At `m=3`, (4.3) is `14` whereas `R_m=5`.  For `m>=4`, the ratio in
(4.4) is at least `6`, while `R_m>2m+1`; again
`T_m-(2m+1)>R_m`.  A family of `R_m` vectors cannot span a space of the
larger dimension (4.3). \(\square\)

This is a no-go only for the explicit canonical family (3.2).  The finite
censuses suggest that it is the complete pure inverse-pair catalogue, but
that classification is not an all-parameter theorem and is not used here.
Coordinate conjugates recover the full abstract lattice by Theorem 3.1;
the missing operation is precisely changing the ambient factor/slot.

## 5. Exact gain and remaining gate

The move proves, natively inside shortest wreath factors, all of the
following at once:

* exact rank-`m` root coverage;
* exact rank-`(m+1)` owner coverage;
* zero change in source length;
* strict positive and negative residence; and
* an occurrence-explicit four-term q1-upper current.

It therefore bypasses the native same-phase-`C6` obstruction for q1
palette adjustment.  The next exact question is no longer whether a native
central-preserving move exists.  It is the following birail span problem:

> Do the rectangles (2.7) from a row-disjoint MSW inverse-pair packet admit
> a bounded-defect integer combination which supplies every missing
> immediate-upper colour without withdrawing its last provider?

Even a positive answer would not yet prove `B(k)+O(1)`.  The paired swap
can change upper witnesses of widths at least two, and it does not reduce
the number of wreath components.  A complete proof still needs either a
deeper-width transparent compensation, or a protected witness linkage,
and a separate component connector/common-cap theorem.
