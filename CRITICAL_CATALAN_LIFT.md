# A critical Catalan defect lift is enough

## 1. Outcome

The contractive criterion in `CONTRACTIVE_DEFECT_LIFT.md` allows an additive
`O(H Cat_m)` error, and for that reason it needs an inherited defect
coefficient bounded by a constant strictly below four.  There is a different
regime which is useful for the exact ECO recursion.

Put

\[
 C_m=\operatorname {Cat}_m,\qquad
 W_m=\binom{2m+1}{m}=(2m+1)C_m .
\]

The Catalan ratio is

\[
 A_m:=\frac{C_{m+1}}{C_m}
      =\frac{2(2m+1)}{m+2}
      =4-\frac6{m+2}.                                \tag{1.1}
\]

Although `A_m` tends to four, it is still smaller than the width ratio by
the exact telescoping factor

\[
 \frac{A_mW_m}{W_{m+1}}=\frac{2m+1}{2m+3}.           \tag{1.2}
\]

Consequently a lift may inherit defects at the full Catalan child rate.  If
the number of defects which cannot be charged to an old defect is
sub-Catalan on average, normalized defect still tends to zero.

## 2. The critical recurrence theorem

Let `E_(m,H)(F)` be the total missing-shadow count through depth `H` of an
exact wreath factor on `2m+1` coordinates, as in
`CONTRACTIVE_DEFECT_LIFT.md`.

### Theorem 1 (critical Catalan lift)

Suppose that for every final dimension parameter `M`, every depth `H=o(M)`,
and every

\[
 j_0=j_0(M,H)\quad\hbox{with}\quad
 H=o(j_0),\qquad j_0=o(M),                            \tag{2.1}
\]

one can start with an arbitrary exact factor `F_(j_0)` and construct factors
`F_m`, `j_0<=m<=M`, satisfying

\[
 E_{m+1,H}(F_{m+1})
 \le \frac{C_{m+1}}{C_m}E_{m,H}(F_m)+B_{m,H}          \tag{2.2}
\]

for every `j_0<=m<M`.  If

\[
 \frac1M\sum_{m=j_0}^{M-1}\frac{B_{m,H}}{C_m}=o(1),  \tag{2.3}
\]

uniformly for the chosen final-parameter sequence, then

\[
 \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.       \tag{2.4}
\]

In particular, the pointwise condition

\[
 \max_{j_0\le m<M}\frac{B_{m,H}}{C_m}=o(1)           \tag{2.5}
\]

is sufficient.  Condition (2.3) is weaker: a sparse set of dimensions may
have Catalan-sized exceptional terms.

### Proof

Write

\[
 e_m=\frac{E_{m,H}(F_m)}{W_m}.
\]

Dividing (2.2) by `W_(m+1)` and using (1.2) gives

\[
 e_{m+1}\le
 \frac{2m+1}{2m+3}e_m+\frac{B_{m,H}}{W_{m+1}}.       \tag{2.6}
\]

The multiplicative factors telescope:

\[
 \prod_{r=s}^{M-1}\frac{2r+1}{2r+3}
       =\frac{2s+1}{2M+1}.                            \tag{2.7}
\]

Iteration of (2.6) therefore gives the exact estimate

\[
 \boxed{
 e_M\le
 \frac{2j_0+1}{2M+1}e_{j_0}
 +\frac1{2M+1}
       \sum_{m=j_0}^{M-1}\frac{B_{m,H}}{C_{m+1}} .}
                                                               \tag{2.8}
\]

Indeed, the factor following the error born at step `m` is
`(2m+3)/(2M+1)`, and
`W_(m+1)=(2m+3)C_(m+1)`.

The first term needs a little care because `H` is larger than `sqrt(M)` in
the tail application.  The useful dimension-free bound is not
`e_(j_0)=O(H)`, but the total-lattice bound

\[
 E_{j_0,H}\le 2^{2j_0+1},\qquad
 e_{j_0}=O(\sqrt {j_0}),                              \tag{2.9}
\]

by the central-binomial estimate.  It is therefore enough to choose

\[
                         j_0^{3/2}=o(M).              \tag{2.10}
\]

Since

\[
 \frac{C_m}{C_{m+1}}=\frac{m+2}{2(2m+1)}\le\frac12,
\]

condition (2.3) makes the second term in (2.8) `o(1)`.  Equations
(2.8)--(2.10) make the first term `o(1)`.  Hence

\[
                         E_{M,H}(F_M)=o(W_M).         \tag{2.11}
\]

Choose, for example,

\[
 H=\left\lceil\sqrt{M\log M}\right\rceil,
 \qquad j_0=\left\lceil M^{3/5}\right\rceil,        \tag{2.12}
\]

Then `H=o(j_0)`, `j_0=o(M)`, and
`j_0^(3/2)=o(M)`.  Any three-scale choice with these properties works.

The wreath linearization and truncated-tail argument from
`CONTRACTIVE_DEFECT_LIFT.md` now converts (2.11) into an OR word of length
`W_M+o(W_M)` in odd dimension `2M+1`.  The standard one-coordinate lift
has twice the length, while

\[
 \binom{2M+2}{M+1}=2\binom{2M+1}{M},
\]

so the same asymptotic ratio holds in even dimensions.  The Sperner lower
bound gives the reverse inequality and proves (2.4).  \(\square\)

## 3. A cleaner bounded-initial-defect version

If the construction at `j_0` is known to have `e_(j_0)=O(1)`, the auxiliary
condition (2.10) is unnecessary: (2.1) alone makes the first term of (2.8)
vanish.  More generally Theorem 1 only requires

\[
                    \frac{j_0}{M}e_{j_0}=o(1).        \tag{3.1}
\]

This is the exact initial condition and should be used instead of the
convenient sufficient choice in (2.10).

## 4. The ECO charging target

Every Dyck word of semilength `m+1` has a unique ECO parent, and

\[
 \sum_{w\in\mathcal D_m}(\ell(w)+1)=C_{m+1},         \tag{4.1}
\]

where `ell(w)` is the final-descent length.  The peak-insertion theorem in
`MSW_ECO_INSERTION_AUDIT.md` says that every child flip order is its parent
flip order with one adjacent two-letter block inserted, after a
path-dependent coordinate injection.

This suggests a weaker successor lemma than the fixed-coordinate paired
braid.

> **Critical ECO charging lemma.**  For every controlled depth `H=o(m)`,
> construct the next exact factor so that every missing new shadow can be
> charged either
>
> 1. to an old missing shadow, with total charge at most
>    `(C_(m+1)/C_m) E_(m,H)`; or
> 2. to an exceptional family of size `B_(m,H)`, where the exceptional
>    terms satisfy the Cesaro sub-Catalan condition (2.3).

Unlike the strict-contraction programme, this lemma does not require one
common inserted coordinate pair and does not require an inherited
coefficient bounded away from four.  Path-dependent ECO coordinates are
allowed.  What must be proved is that the genuinely new seam holes have
sub-Catalan *distinct target* count on average; counting a constant number
of raw seam windows per child is too crude and gives only `Theta(C_m)`.

Thus there are now two independent sufficient routes:

* a fixed-coordinate braid with inherited coefficient `a<4`, which may pay
  `O(HC_m)` additive repair; or
* a critical ECO lift at the full Catalan rate, whose uncharged distinct
  defect is `o(C_m)` on average.

The second criterion is quantitatively sharper and may exploit duplication
among the path-local seam targets which the first criterion deliberately
ignores.
