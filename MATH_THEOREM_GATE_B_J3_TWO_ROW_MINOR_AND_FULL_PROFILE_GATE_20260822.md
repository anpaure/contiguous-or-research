# Gate B: the exact fixed-`j=3` local minor and the full-profile gate

**Date:** 2026-08-22

**Status.**  The fixed third harmonic level does not improve the decisive
two-row certificate from the preceding `j=2` analysis.  For every `r>=6`,
the `t=0,ell` minor of the sixteen-atom shore profile is explicitly rational,
has determinant at least `48/r^9`, and has least singular value

\[
             \boxed{\sigma_{\min}={147\over2r^5}
                    (1+O(r^{-1}))}.                         \tag{0.1}
\]

Thus its scale is again `Theta(r^-5)`.  Exact full-profile evaluations look
better because two other puncture rows occur on a larger scale, but this note
does not promote that observation to a uniform theorem.  The exact remaining
fixed-`j=3` lemma is a termwise asymptotic for those two rows, or an equivalent
full-Gram lower bound.  Consequently the current results do not justify
restricting five-vertex/relative polymer resummation to `j=2` alone.

## 1. Normalization

Use

\[
 b=2r+1,\qquad \ell=r+3,\qquad
 D_M=2r\,r!(r+1)!,\qquad A_3=(r-4)(r+1).            \tag{1.1}
\]

Here `A_3` is the unnormalised extra-pair injection denominator at `j=3`.
For the sixteen four-vertex atoms put

\[
 a_r={L_{r,3}(0)\over D_MA_3},\quad
 b_r={L_{r-1,3}(0)\over D_MA_3},\quad
 c_r={L_{r,3}(\ell)\over D_MA_3},\quad
 d_r={L_{r-1,3}(\ell)\over D_MA_3}.                \tag{1.2}
\]

The exact Venn coefficient formula is (2.1)--(2.3) of the `j=2` scale note,
with the remaining distinguished pair inserted through the signed injection
polynomial, where `K=r-4` and `L=r+1`,

\[
 La-Kc=(r+1)a-(r-4)c.                              \tag{1.3}
\]

after the two event pairs have been removed.  Dividing by
`K(r+1)=A_3` gives the signed average.  This leaves the same finite positional
Venn sum and produces the formulas below without enumerating root subsets.

## 2. Four exact rational rows

For every integer `r>=6`,

\[
 a_r={49r^6-523r^5+2733r^4-7695r^3+10796r^2-7196r+1296
 \over
 2r^3(r-4)(r-3)(r-2)^2(r-1)^2(r+1)^2},             \tag{2.1}
\]

\[
 b_r={147r^7-2002r^6+12376r^5-43364r^4+86273r^3
 -89142r^2+45000r-8640
 \over
 2r^3(r-4)(r-3)^2(r-2)^2(r-1)^2(r+1)^2},           \tag{2.2}
\]

\[
 c_r=-{4r^5-173r^4+820r^3-1385r^2+1084r-260
 \over
 6r^3(r-2)^2(r-1)^2(r+1)^2},                       \tag{2.3}
\]

\[
 d_r={155r^5-1233r^4+3401r^3-3813r^2+1982r-384
 \over
 2r^3(r-3)(r-2)^2(r-1)^2(r+1)^2}.                  \tag{2.4}
\]

Their determinant is

\[
 \boxed{
 a_rd_r-b_rc_r={P_3(r)\over
 6r^6(r-4)(r-3)^2(r-2)^4(r-1)^4(r+1)^4},}          \tag{2.5}
\]

where

\[
\begin{split}
P_3(r)={}&294r^{12}-5327r^{11}+45972r^{10}-227185r^9
+671640r^8-1273365r^7\\
&+2059524r^6-4190095r^5+8018970r^4-9937460r^3
+6936984r^2-2534976r+376704.                       \tag{2.6}
\end{split}
\]

Putting `u=r-6`, all coefficients of `P_3(u+6)` are positive:

\[
\begin{split}
(&294,15841,392934,5954555,61630890,460502523,
2552357106,10576238237,\\
&32463435360,71744047540,107879648688,98609942592,
41228317440).                                      \tag{2.7}
\end{split}
\]

More sharply,

\[
                         a_rd_r-b_rc_r\ge {48\over r^9}.     \tag{2.8}
\]

After placing (2.5) and `48/r^9` over a common denominator and substituting
`u=r-6`, the numerator coefficients, from degree twenty-one down to zero,
are

\[
\begin{split}
(&6,613,35868,1536527,49967196,1239779367,23741204580,
356465770937,4260564308766,\\
&41038029405988,321381974725992,2057446689488064,
10789715648915136,46290372112130688,\\
&161653064376469248,455182935615399168,1017864649871764992,
1765585155292111872,\\
&2289867377820493824,2089069897014337536,
1195334738227003392,322571705063178240),             \tag{2.9}
\end{split}
\]

which proves (2.8) without a numerical sign test.

## 3. Exact singular scale

Expanding (2.1)--(2.4) at infinity gives

\[
 a_r={49\over2r^5}+O(r^{-6}),\qquad
 b_r={147\over2r^5}+O(r^{-6}),                      \tag{3.1}
\]

\[
 c_r=-{2\over3r^4}+{157\over6r^5}+O(r^{-6}),\qquad
 d_r={155\over2r^5}+O(r^{-6}).                      \tag{3.2}
\]

Thus the larger singular value of
`B_(r,3)=((a_r,b_r),(c_r,d_r))` is
`(2/3)r^-4(1+O(1/r))`.  Since the product of the singular values is the
positive determinant, (2.5) yields

\[
 \boxed{
 \sigma_{\min}(B_{r,3})={147\over2r^5}
                         (1+O(r^{-1})).}             \tag{3.3}
\]

Crude factor bounds in (2.1)--(2.4), together with (2.8), also give an
explicit lower bound `c/r^5` for an absolute rational `c>0` and every
`r>=6`.  As before, adding the other profile rows can only increase the
least singular value.

## 4. Why the full-profile improvement is not yet a theorem

The exact evaluator shows that the two exceptional shifts `t=r+1,r+2`
are much larger than the minor above.  The observed leading form is

\[
 {L_{\bullet,3}(r+1)\over D_MA_3}\sim
 \left(-{2\over3r^3},{13\over2r^4}\right),\qquad
 {L_{\bullet,3}(r+2)\over D_MA_3}\sim
 \left(-{2\over3r^3},{17\over2r^4}\right).          \tag{4.1}
\]

If (4.1) is proved with uniform `O(r^-4),O(r^-5)` remainders, the determinant
of these two rows is `-4/(3r^7)+O(r^-8)`, and hence they certify

\[
                         \sigma_{\min}=\sqrt2\,r^{-4}
                         (1+O(r^{-1})).              \tag{4.2}
\]

This would explain the improved full-profile computations.  However, the
exact functions at these shifts contain additional factorial-ratio tails;
finite rational evaluation at growing `r` does not by itself prove (4.1).
The current exact Venn evaluator supplies the data but no published
termwise domination lemma that discards those tails uniformly.  Therefore
(4.1)--(4.2) are recorded as the next sharply specified lemma, not as a
claim proved by this note.

Even (4.2) remains two powers below the available absolute
`O(D_M/r^2)` remote dressing.  So a proof of the full sixteen-bank scale
would improve the local conditioning statement but would still not replace
shore-adapted relative polymer control.

## 5. Authentication

The exact checker is

`scratch/verify_gate_b_j3_two_row_minor_20260822.py`.

Its SHA-256 digest is

`e54f144d20b183a6b4f9dfd961a79ce5cb86cc5c7bf26ab943b9b43adaabeb95`.

It authenticates the frozen Venn/Hahn evaluator chain, verifies
(2.1)--(2.5) exactly for every `6<=r<=29`, and checks (2.8).  The checker is
a replay of the displayed algebra, not a premise of it.
