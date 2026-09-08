# Gate B: uniform all-depth conditioning from two omitted-triple defects

**Date:** 2026-08-22

**Status.**  This note proves the uniform local theorem which was previously
open.  Let `A_(r,j)` be the full `(2r+1)`-by-two shore profile of the sixteen
four-vertex zero-avoidance atoms, divided by

\[
                  D_M(r-4)_{j-2}(r+1)_{j-2}.
\]

Then, for every `r>=9` and every `2<=j<=r-2`,

\[
                 \boxed{\sigma_{\min}(A_{r,j})\ge r^{-29}.} \tag{0.1}
\]

The proof uses two row differences.  Each difference is exactly the sum of
two omitted three-blocker path terms.  Their Hahn distributions are a common
quadratic plus at most two endpoint defects.  A Vandermonde calculation
turns this into a rational determinant.  After separating the parity of
`m=j-2`, its numerator factors into polynomials with strictly positive
coefficients.

This closes the conditioning of the complete sixteen-atom bank uniformly in
harmonic depth.  It does **not** yet transfer the result to the full
zero-avoidance exposure: the available remote estimate is an absolute
`O(D_M/r^2)` bound, whereas (0.1) requires a shore-adapted relative or
row-difference estimate.

## 1. Two exact puncture defects

Put

\[
 b=2r+1,\qquad K=r-4,\qquad L=r+1,
 \qquad m=j-2,qquad D_M=2r\,r!(r+1)!.              \tag{1.1}
\]

After multiplying cut labels by `-2 modulo b`, the local boundary graph is
the punctured Cayley graph on `Z_b` with steps `+/-1,+/-3`, and the two event
roots are `0,5`.  Let `L_(s,j)(t)`, `s in {r,r-1}`, be the signed profile of
the sixteen four-vertex atoms at event start `t`.  At `t=3` no local atom
uses either omitted target, so this row is the complete-bank value.

Define the two defects

\[
 C_{1,s,j}=L_{s,j}(3)-L_{s,j}(r+1),\qquad
 C_{2,s,j}=L_{s,j}(3)-L_{s,j}(r+2).                \tag{1.2}
\]

Write `(q,a)` for the cyclic interval of rank `q` and start `a`.  Comparing
the complete local bank with the punctured bank shows that the only deleted
inclusion--exclusion terms are the following four three-edge paths:

\[
\begin{array}{c|c|c}
 &\text{first path}&\text{second path}\\ \hline
C_1&\{(r-1,r),(r,0),(r,r+1)\}&
     \{(r-1,0),(r,r-1),(r,r+1)\}\\
C_2&\{(r-1,r+2),(r,0),(r,r)\}&
     \{(r-1,0),(r-1,r+2),(r,b-1)\}.
\end{array}                                                   \tag{1.3}
\]

Thus (1.2) contains no remote atom and no infinite cluster expansion.

## 2. Exact Hahn distributions

After the two displayed boundary pairs have been removed, a shore root has
`a` points in the inside pool and `c` in the outside pool.  The normalized
signed injection average for the remaining `m` pairs is

\[
 e_m(a,c)=
 \sum_{h=0}^m(-1)^{m-h}{m\choose h}
 { (a)_h\over(K)_h}
 { (c)_{m-h}\over(L)_{m-h}}.                       \tag{2.1}
\]

This is the boundary Hahn polynomial.  Formula (2.1) follows by deciding
which `h` pairs take their root endpoint from the inside pool, placing the
constrained endpoints first, and dividing by `(K)_m(L)_m`.  It is also an
average of products of numbers in `{-1,0,1}`, so

\[
                              |e_m(a,c)|\le1.        \tag{2.2}
\]

Let

\[
                         P(a)=(K+1-a)(a+1),\qquad0\le a\le K. \tag{2.3}
\]

For `i=1,2` and a shore `s`, let `G_(i,s)(a)` be the coefficient, divided by
`D_M`, of `e_m(a,s-2-a)` in the defect `C_(i,s,j)`.  Direct cellwise
bijection counting of the four triples in (1.3) gives

\[
\begin{array}{c|c}
G_{1,r}(a)&q_1P(a)+u_1\mathbf1_{a=K}\\
G_{2,r}(a)&q_2P(a)+u_2\mathbf1_{a=K}\\
G_{1,r-1}(a)&q_1P(a)+v_1\mathbf1_{a=K}\\
G_{2,r-1}(a)&q_2P(a)+w_2\mathbf1_{a=K-1}
                         +v_2\mathbf1_{a=K}.
\end{array}                                                   \tag{2.4}
\]

The seven coefficients are

\[
 q_1={4(r+2)(2r-3)\over
 r^3(r-3)(r-2)(r-1)(r+1)},                                  \tag{2.5}
\]

\[
 u_1=-{2r-3\over r^3(r-1)(r+1)},                            \tag{2.6}
\]

\[
 q_2={2(4r^2+6r-15)\over
 r^3(r-3)(r-2)(r-1)(r+1)},                                  \tag{2.7}
\]

\[
 u_2=-{4r-5\over r^3(r-1)(r+1)},                            \tag{2.8}
\]

\[
 v_1=-{(r+4)(4r^2-13r+8)\over
 2r^3(r-2)(r-1)(r+1)},                                      \tag{2.9}
\]

\[
 w_2=-{(r-4)(4r-5)\over r^3(r-2)(r-1)(r+1)},               \tag{2.10}
\]

\[
 v_2=-{4r^3+3r^2-36r+30\over
 2r^3(r-2)(r-1)(r+1)}.                                     \tag{2.11}
\]

Here is a self-contained audit of the finite calculation.  For an ordered
blocker triple `J`, form its eight Boolean cells `C_eta`.  If a positional
root has `u_eta` points in cell `eta`, the compatible words contribute

\[
 N_{s,J}(u)\prod_\eta u_\eta!\,(|C_\eta|-u_\eta)!           \tag{2.12}
\]

times the signed boundary choice sum.  The four label-cell size vectors in
(1.3), in the displayed blocker order, are permutations of

\[
\begin{split}
 &(0,1,r,0,2,r-2,0,0),\\
 &(0,r-1,2,0,2,0,r-2,0),\\
 &(3,0,r-2,0,0,r-1,1,0).                         \tag{2.13}
\end{split}
\]

The first two types have `2b-6` retained positional blocker tuples and the
last has `2b-5`.  Insert their four boundary marks, sum (2.12) over the
`2r` retained root starts, and divide by `D_M`.  For `0<=a<K` the result is
the common quadratic in (2.4); the only root starts lost at the puncture are
`a=K-1,K`, giving (2.6), (2.8)--(2.11).  Cancelling the factorials in
(2.12) gives exactly (2.5)--(2.11).  This proves (2.4) for symbolic `r`; no
finite interpolation is used.

Consequently, after division by `D_M(K)_m(L)_m`, the two defect rows are
obtained by summing (2.4) against (2.1).

## 3. Closing the quadratic Hahn sum

Define

\[
 S_d=\sum_{a=0}^KP(a)e_m(a,K+d-a),\qquad d\in\{1,2\}.       \tag{3.1}
\]

Also put

\[
 E_1=e_m(K,1),\quad E_2=e_m(K,2),\quad
 E_{12}=e_m(K-1,2).                                        \tag{3.2}
\]

The endpoint values simplify to

\[
 E_1={L-m\over L},\qquad
 E_2={(L-m)(L-m-1)\over L(L-1)},                            \tag{3.3}
\]

\[
 E_{12}={(L-m)(KL-Km-K-Lm+m^2-m)\over KL(L-1)}.             \tag{3.4}
\]

For auditability, the following formulas close (3.1) without a growing
sum.  Put

\[
 A=K-m,\qquad D=A+L+2,qquad
 U={1\over{K\choose m}},\qquad
 V={(-1)^m\over{L\choose m}}.                              \tag{3.5}
\]

Define

\[
 M_0={U(L+1)+V(K+1)\over D},                                \tag{3.6}
\]

\[
 M_1={-U(A+1)(L+1)+V(K+1)((m+1)(D+1)-(K+2))
       \over D(D+1)},                                       \tag{3.7}
\]

\[
\begin{split}
 M_2={}&U(L+1)(A+1)
 \left({2(A+2)\over D(D+1)(D+2)}-{1\over D(D+1)}\right)\\
 &+V(K+1)\left({(m+1)^2\over D}
 -{(2m+3)(K+2)\over D(D+1)}
 +{2(K+2)(K+3)\over D(D+1)(D+2)}\right).          \tag{3.8}
\end{split}
\]

Let `A_0=(m+1)M_0-M_1` and `A_1=(m+1)M_1-M_2`.  Then

\[
\begin{split}
 S_1={}&A_1\left[{K+2\choose m+1}
             +2{K+2\choose m+2}+{K+2\choose m+3}\right]\\
 &+A_0\left[{K+2\choose m+2}+{K+2\choose m+3}\right],      \tag{3.9}
\end{split}
\]

\[
\begin{split}
 S_2={}&A_1\left[{K+3\choose m+1}
             +2{K+3\choose m+2}+{K+3\choose m+3}\right]\\
 &+A_0\left[-{K+3\choose m+1}+{K+3\choose m+3}\right]
 +(K+3){(K+2)_m\over(K)_m}.                                \tag{3.10}
\end{split}
\]

To prove (3.9)--(3.10), write `h+q=m` in (2.1).  Since

\[
 (a)_h(K+d-a)_q=h!q!{a\choose h}{K+d-a\choose q},           \tag{3.11}
\]

Vandermonde's identity sums the quadratic weight over `0<=a<=K`.  For
`d=1`, the one omitted endpoint has weight zero.  For `d=2`, the two omitted
endpoints have weights zero and `-(K+3)`; the latter gives the last term in
(3.10).  Equivalently, the three alternating factorial moments are obtained
from

\[
 \sum_{q=0}^m(-1)^qy^q={1-(-y)^{m+1}\over1+y}               \tag{3.12}
\]

and its first two logarithmic derivatives, with `y=x/(1-x)`.  The resulting
beta integrals are (3.6)--(3.8).  This proves the closed formulas.

By (2.4), the exact normalized defect matrix is

\[
 B_{r,j}=\begin{pmatrix}
 q_1S_2+u_1E_2&q_1S_1+v_1E_1\\
 q_2S_2+u_2E_2&q_2S_1+w_2E_{12}+v_2E_1
 \end{pmatrix}.                                             \tag{3.13}
\]

## 4. The determinant never vanishes

Put

\[
 x=r-m-4\ge0.                                               \tag{4.1}
\]

Substitution of (2.5)--(3.10) into (3.13) gives

\[
 \boxed{\det B_{r,j}={(r-m)(r-m+1)^2\,\Phi_m(x)\over
 \mathcal D(r,m)},}                                         \tag{4.2}
\]

where

\[
\begin{split}
\mathcal D(r,m)={}&r^8(2r-m)(m+1)(m+2)(m+3)(r-2)(r-1)^2\\
&\hspace{15mm}\cdot(r+1)^4(2r-m-1)(2r-m+1).                 \tag{4.3}
\end{split}
\]

The numerator has four parity regimes.

For `m=0`,

\[
 \Phi_0(x)=2(x+4)^2(2x+7)(2x+9)H_0(x),                     \tag{4.4}
\]

\[
 H_0(x)=40x^4+485x^3+1977x^2+3308x+1950.                   \tag{4.5}
\]

For `m=2`,

\[
 \Phi_2(x)=4(x+5)(2x+9)(2x+11)H_2(x),                      \tag{4.6}
\]

\[
 H_2(x)=40x^5+1245x^4+13508x^3+67422x^2+158710x+143316.   \tag{4.7}
\]

For odd `m`,

\[
 \Phi_m(x)=-(m+1)(m+3)(m+2x+8)H_o(m,x),                    \tag{4.8}
\]

where

\[
\begin{split}
H_o={}&4m^8+(36x+119)m^7+(136x^2+912x+1467)m^6\\
&+(280x^3+2846x^2+9299x+9834)m^5\\
&+(340x^4+4628x^3+22901x^2+49207x+39053)m^4\\
&+(244x^5+4135x^4+27343x^3+88945x^2+143584x+92750)m^3\\
&+(96x^6+1924x^5+15810x^4+68904x^3+169743x^2
   +225672x+126443)m^2\\
&+(16x^7+364x^6+3544x^5+19526x^4+66867x^3
   +142873x^2+173845x+90190)m\\
&+8x^6+249x^5+2755x^4+14656x^3+40322x^2+54490x+27840.
                                                               \tag{4.9}
\end{split}
\]

Finally, if `m>=4` is even, put `y=m-4`.  Then

\[
 \Phi_m(x)=-(y+6)(2x+y+11)(2x+y+13)H_e(y,x),                \tag{4.10}
\]

where

\[
\begin{split}
H_e={}&(8y^2+48y+24)x^6
 +(44y^3+606y^2+2084y+651)x^5\\
&+(100y^4+2191y^3+15770y^2+38654y+10423)x^4\\
&+(120y^5+3632y^4+40713y^3+202416y^2+396813y+120432)x^3\\
&+(80y^6+3098y^5+47527y^4+362939y^3+1401929y^2
   +2359307y+852174)x^2\\
&+(28y^7+1322y^6+25825y^5+267951y^4+1569184y^3
   +5028592y^2+7582719y+3125836)x\\
&+4y^8+223y^7+5301y^6+69776y^5+551539y^4
   +2644354y^3+7324827y^2+10144976y+4525360.
                                                               \tag{4.11}
\end{split}
\]

Every coefficient in (4.5), (4.7), (4.9), and (4.11) is strictly positive.
Since `x,y>=0`, equations (4.2)--(4.11) prove that the determinant never
vanishes.  More quantitatively, its numerator is a nonzero integer.  Every
factor in (4.3) is positive and

\[
                         \mathcal D(r,m)\le512r^{21}         \tag{4.12}
\]

for `r>=9` and `0<=m<=r-4`.  As `r^3>=512`,

\[
                         \boxed{|\det B_{r,j}|\ge r^{-24}.} \tag{4.13}
\]

## 5. Uniform singular-value bound

The explicit coefficients (2.5)--(2.11) have absolute value at most one
for `r>=9`.  From (2.2)--(2.3),

\[
 |S_d|\le\sum_{a=0}^KP(a)\le r^3.                           \tag{5.1}
\]

Thus every entry of `B_(r,j)` has absolute value at most `2r^3`, and

\[
                         \|B_{r,j}\|_F\le4r^3.              \tag{5.2}
\]

The product of its singular values is the absolute determinant, so

\[
                         \sigma_{\min}(B_{r,j})
                         \ge {1\over4r^{27}}.                \tag{5.3}
\]

Let `T` act on the full profile by taking the two differences in (1.2).
Its row Gram matrix is

\[
                         TT^{\mathsf T}=\begin{pmatrix}2&1\\1&2\end{pmatrix},
 \qquad \|T\|=\sqrt3.                                      \tag{5.4}
\]

Since `B_(r,j)=T A_(r,j)`, equations (5.3)--(5.4) imply

\[
 \sigma_{\min}(A_{r,j})\ge {1\over4\sqrt3\,r^{27}}
                         \ge r^{-29},                        \tag{5.5}
\]

which proves (0.1).

## 6. Consequence and remaining gate

The sixteen-atom bank already has the exact affine three-profile identity

\[
                  L_{s,j}(0)+L_{s,j}(r+3)=L_{s,j}(3),        \tag{6.1}
\]

and therefore local best-constant residual at least `1/(3b)`.  The present
theorem adds a uniform polynomial inverse for its two shore columns.  Thus
there is no longer an open local harmonic-depth or local rank-two issue.

The remaining Gate-B scalar is a stability theorem for the actual
zero-avoidance profile.  An absolute perturbation of size `O(r^-2)` after
division by `D_M` can still overwhelm the deliberately crude `r^-29` local
inverse.  What is needed is one of:

1. a relative harmonic polymer estimate for the two shore columns;
2. an `r^-C` estimate directly on the two defect row differences of the
   remote dressing; or
3. a nonperturbative positivity argument for the full zero-avoidance
   determinant.

No conclusion about the full-exposure scalar is claimed here.

## 7. Authentication

The exact checker is

`scratch/verify_gate_b_uniform_allj_local_defect_conditioning_20260822.py`.

Its SHA-256 digest is

`5185c23f16dace0c5cdfceb69eb924fd5e59f74685bfcdaa5189423655411311`.

It authenticates the Venn/Hahn evaluator chain, verifies (2.4)--(2.11)
against the four omitted triples, checks the closed Vandermonde formulas,
replays the actual local rows, and verifies the determinant factorization,
parity positivity, and uniform lower bound.  Its finite replay confirms the
displayed identities; it is not used as the premise of the all-`r` proof.
