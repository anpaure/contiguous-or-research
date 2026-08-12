# An explicit growing-dimensional transversal-face packing

## 1. Result and scope

For `1<=s<m`, let `F_(m,s)` be the hypergraph whose vertices are the middle
sets `binom([2m],m)` and whose edges are all `s`-dimensional matching faces

\[
 F(U,V;R)=\{U\cup X:X\text{ chooses one endpoint of every edge of }R\},
\tag{1.1}
\]

where `U,V` are disjoint `(m-s)`-sets and `R` is a perfect matching on the
remaining `2s` coordinates.

`TRANSVERSAL_CUBE_PACKING.md` proves the exact parameters

\[
 k_s=2^s,\qquad
 D_s=\binom ms^2s!,\qquad
 {\Delta_2\over D_s}={s\over m^2}.
\tag{1.2}
\]

Its fixed-`s` argument can be made quantitatively growing.  Fix
`0<alpha<1` and put

\[
 s=\left\lfloor\alpha\log_2\log m\right\rfloor.
\tag{1.3}
\]

For all sufficiently large `m` (so that `s>=1` and `k_s=2^s>4`),
`F_(m,s)` has a matching covering

\[
 \left(1-O\!\left(exp\{-c_\alpha(\log m)^{1-\alpha}\}\right)\right)
 \binom{2m}m
\tag{1.4}
\]

middle vertices, for some constant `c_alpha>0`.  All unmarked logarithms
below are natural; `log_2` is written explicitly.

This is an explicit `s(m)->infinity` theorem.  It is still only a
middle-layer packing.  Its dimension is `Theta(log log m)`, far below the
`omega(sqrt(m))` depth needed for negligible literal tails, and it carries
no radius or shadow ledger.

## 2. The growing-uniformity theorem

We use Corollary 1.5 of Alon--Bollobas--Kim--Vu, *Economical covers with
geometric applications*, in exactly the form audited directly from the
primary paper and in
`TYPED_MATCHING_QUANTITATIVE_AUDIT.md`:

> A `D`-regular `k`-uniform hypergraph with maximum pair codegree `C` has a
> matching whose uncovered fraction is
> 
> \[
> O\!\left(k\left({C\log(1+C)\over D}\right)^{1/(k-1)}\right),
> \tag{2.1}
> \]
> 
> provided
> 
> \[
> e^{2k}C=o(D/\log D).
> \tag{2.2}
> \]

Unlike fixed-uniformity nibble statements, this theorem genuinely permits
`k` to grow, subject to (2.2).

## 3. Verification of the hypothesis

Write `L=log m`.  From (1.3),

\[
 k_s=2^s\le L^\alpha=o(L).
\tag{3.1}
\]

Since `s=o(m)`, Stirling's formula gives

\[
 \log D_s
 =2\log\binom ms+\log(s!)
 =2s\log m-s\log s+O(s)
 =\Theta(s\log m).
\tag{3.2}
\]

Using (1.2), the left-to-right ratio in (2.2) is

\[
 e^{2k_s}{\Delta_2\over D_s}\log D_s
 =e^{2k_s}{s\over m^2}\log D_s.
\tag{3.3}
\]

Its logarithm is

\[
 2k_s-2\log m+O(\log s+\log\log D_s)
 =-2L+o(L),
\tag{3.4}
\]

which tends to minus infinity.  Thus (2.2) holds with a large margin.

## 4. Quantitative uncovered fraction

Because `Delta_2<=D_s` and `log(1+Delta_2)<=log(1+D_s)`, equations
(1.2)--(3.2) give

\[
 {\Delta_2\log(1+\Delta_2)\over D_s}
 \le {s\over m^2}\log(1+D_s)
 =\exp\{-2L+O(\log L)\}.
\tag{4.1}
\]

Substitute (4.1) into (2.1).  Since `k_s<=L^alpha` and the exponent in
(4.1) is negative,

\[
 \begin{aligned}
 \log\left[
 k_s\left({\Delta_2\log(1+\Delta_2)\over D_s}
       \right)^{1/(k_s-1)}
 \right]
 &\le O(\log L)-{2L-O(\log L)\over L^\alpha}\\
 &=-\Omega(L^{1-\alpha}).
 \end{aligned}
\tag{4.2}

This proves (1.4).

## 5. What the theorem changes

The earlier fixed-dimensional theorem yielded an unquantified diagonal
function `s(m)->infinity`.  The present calculation proves the explicit
range

\[
                     s=\alpha\log_2\log m,
\qquad 0<\alpha<1.
\tag{5.1}
\]

It also shows exactly why this theorem stops far short of the OR target.
At a polynomial depth `H`, the guaranteed error bound in (1.4) is not small
enough to imply `o(W/H)`, and the free dimension itself is only
`Theta(log log m)`.  Increasing `s` until
`2^s` is comparable with a power of `m` destroys the useful exponent in
(2.1); increasing it to `m-1` violates (2.2) by an `exp(2^m)` factor.

The result is therefore a quantitative middle-only face-packing theorem.
The matching conclusion alone does not certify a prescribed distribution of
active pair systems.  It is not a radius-resolved wreath construction or an
asymptotic OR upper bound.
