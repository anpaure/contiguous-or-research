# Support-budget audit after the mutual-equality no-go

Date: 2026-07-26

Method: pure mathematics only.

## 1. Three support ledgers must be kept separate

There are three different quantities in the prime-cycle programme.

1. A frequency-zero mixed count `r=1+v` has **count support**

   \[
                    s_{\rm count}=|\{C:v_C\ne0\}|.
   \tag{1.1}
   \]

   The smallest linear stopping bound is `s_count=2p`; its equality case
   is the doubled/omitted affine `K_(p,p)` of Theorem 32.3.

2. A size-`p+2` singleton component may have an even cycle in its
   two-regular complement.  The smallest such direction has
   **complement-cycle length four**.  This is a row--necklace incidence
   statistic.

3. Given two actual wreath bases, the transition matrix has
   **endpoint-frame support**

   \[
       \|K(D,C)\|_F^2=p+2\nu_-\bigl(K(D,C)\bigr).
   \tag{1.2}
   \]

   This is a coordinate-pair statistic internal to the physical wreath
   packets.

The first two quantities are visible before physical phase completion.
The third is visible only after actual wreath rows have been assembled.
No identity in the count or complement-kernel equations assigns an upper
budget to (1.2).

## 2. The exact endpoint tax for an `r`-row trade

Let

\[
 \mathcal C=C_1\sqcup\cdots\sqcup C_r
 =D_1\sqcup\cdots\sqcup D_r=\mathcal D
\tag{2.1}
\]

be two wreath factorizations of the same `rp` distinct middle sets, and
put

\[
                         t_{ij}=|C_i\cap D_j|.
\tag{2.2}
\]

Theorem 17.9 of the affine-grid file gives

\[
 \boxed{
 X(\mathcal D,\mathcal C):=
 \sum_{i,j}\left(
 \nu_-\bigl(K(D_j,C_i)\bigr)-(p-t_{ij})
 \right)\ge\binom r2.}
\tag{2.3}
\]

The reverse-directed ledger satisfies the same bound.  Hence the combined
two-direction negative-entry tax is at least `r(r-1)`.

Therefore

\[
 \boxed{
 \sum_{i,j}\|K(D_j,C_i)\|_F^2
 \ge pr(3r-2)+r(r-1).}
\tag{2.4}
\]

Indeed, the cross baselines have

\[
 \sum_{i,j}(p-t_{ij})=pr^2-rp=pr(r-1),
\]

because `sum_(i,j)t_(ij)=rp`.  Substitution in (1.2) gives the baseline
`pr(3r-2)`, and (2.3) adds twice `binom(r,2)`.

For the `p`-by-`p` supported affine trade this is

\[
 \boxed{
 \sum_{i,j}\|K(D_j,C_i)\|_F^2
 \ge p^2(3p-2)+p(p-1).}
\tag{2.5}
\]

For a two-for-two wreath trade it is

\[
 \boxed{
 \sum_{i,j=1}^2\|K(D_j,C_i)\|_F^2\ge8p+2.}
\tag{2.6}
\]

Its reverse-directed cross ledger also has support at least `8p+2`, so
the bidirectional support is at least `16p+4`.

The additive terms in (2.5)--(2.6) are rigorous forced support, not an
entropy estimate.  Their sharpness as minima is not presently proved.

## 3. Projection to the smallest mixed-count circuit

Suppose the equality case of Theorem 32.3 is phase-completed **as a
supported move**: the `p` omitted rows are replaced by one extra translate
of each of the `p` doubled rows, and no count-neutral row participates.
The phase equations force the two `p`-row shores to factor the same
`p^2` physical sets.  Thus (2.5) applies.

What does not follow is an enlargement of (1.1).  The row-count vector is
still

\[
                         0^p\,2^p\,1^{T-2p},
\tag{3.1}
\]

so its count support remains exactly `2p`, independently of every
transition matrix in (2.5).  The zero-frequency equation

\[
                         B(r-\mathbf1)=0
\tag{3.2}
\]

sees only the `K_(p,p)` necklace incidences.  It contains no term equal
to, or bounding,

\[
             \sum_{i,j}\nu_-\bigl(K(D_j,C_i)\bigr).
\tag{3.3}
\]

Consequently the new endpoint tax does **not** exclude all mixed counts
of support `2p`.  It excludes only the all-cross endpoint-equality
realization and gives the exact lower bound (2.5) on every supported
physical realization.

There is more slack in a general completion.  Rows with `r_C=1` may move
to nonzero phases while remaining invisible in (3.2).  Such count-neutral
phase carriers can join the ownership component containing the `2p`
exceptional rows.  The isolated `p`-by-`p` orthogonal-grid description
then need not survive at all.  Hence Corollary 17.8 cannot, without an
additional carrier-elimination theorem, force even one extra member of
`supp(r-1)`.

The exact conclusion of this projection is therefore

\[
 \boxed{
 \begin{gathered}
 s_{\rm count}=2p\text{ remains arithmetically possible};\\
 \text{a supported completion pays endpoint-frame support at least }p(p-1)\\
 \text{above the formal all-cross baseline.}
 \end{gathered}}
\tag{3.4}
\]

## 4. Projection to the size-`p+2` length-four direction

A legal length-four direction in a size-`p+2` singleton component gives
two conjugate inverse two-for-two wreath trades:

\[
 \mathcal R_-\longleftrightarrow\mathcal S_- ,
 \qquad
 \mathcal R_+\longleftrightarrow\mathcal S_+ .
\tag{4.1}
\]

Apply (2.6) to either trade.  Each pays at least

\[
                         1
\tag{4.2}
\]

extra negative entry, equivalently two extra Frobenius-support positions,
beyond its common-cell baselines.  The two conjugate trades together pay
at least two extra negative entries, or four Frobenius-support positions,
when their ledgers are counted separately.

This does not lengthen the complement cycle.  Its length is still four:
the matrix identity

\[
                         Q=I+P
\tag{4.3}
\]

and the alternating kernel vector depend only on the four missing
row--necklace incidences.  The endpoint-frame support in (2.6) does not
occur in (4.3).  Nor does it bound the odd-graph cut number `k` in the
multi-cut normal form; a relation between those two invariants has not
been proved.

Thus the precise length-four verdict is

\[
 \boxed{
 \begin{gathered}
 \text{forced extra modular complement length}=0,\\
 \text{forced extra endpoint-frame support}\ge2\text{ per two-for-two trade.}
 \end{gathered}}
\tag{4.4}
\]

The second inequality is a genuine geometric tax, but the existing
modular circuit has unrestricted capacity to pay it.

There is a simple reason: by the product-support identity, the cross tax
is exactly the directed same-shore tax

\[
 \sum_{i\ne\ell}
 \left(\nu_-\bigl(K(C_\ell,C_i)\bigr)-p\right).
\tag{4.5}
\]

This quantity is already present in the chosen base wreath packets before
the phase move is performed.  Neither the mixed-count circuit nor the
length-four complement circuit spends a resource to create it.  The
physical reassembly merely exposes the same pre-existing endpoint
complexity on the cross transitions.

## 5. The missing bridge theorem

To turn (2.5) into a larger mixed-count support, one would need an
upper-budget theorem of one of the following forms.

1. **Supported form.**  Every supported phase completion of a count
   circuit on `s` base rows satisfies

   \[
      \sum_{i,j}\|K(D_j,C_i)\|_F^2
      \le \mathcal B(s,p),
   \]

   with `mathcal B(2p,p)<p^2(3p-2)+p(p-1)`.

2. **Carrier form.**  Endpoint excess `E` forces at least `f(E,p)`
   count-neutral phase carriers, and those carriers must be charged to the
   physical circuit support used by the lift.

3. **Length-four form.**  Endpoint excess in (2.6) forces an increase of
   the odd-graph multi-cut number or of the complement-cycle length.

None of these implications is present in the current ledger.  In
particular, (2.5) is not itself a contradiction: it is a lower bound on a
quantity for which the phase-completion problem currently has no upper
bound.

## 6. Exact status

Proved:

* the universal resolution tax (2.3)--(2.4);
* the `p`-row affine tax `p(p-1)` in (2.5);
* the two-row tax `2` in (2.6);
* no enlargement of count support or complement-cycle length follows
  from these taxes under the presently available equations.

Still open:

* whether the lower bounds in (2.4) are sharp for actual wreath trades;
* whether a supported `2p` mixed count with nonminimal endpoint support
  exists;
* whether count-neutral phase carriers can complete such a mixed count;
* any bridge from endpoint-frame excess to modular circuit length.
