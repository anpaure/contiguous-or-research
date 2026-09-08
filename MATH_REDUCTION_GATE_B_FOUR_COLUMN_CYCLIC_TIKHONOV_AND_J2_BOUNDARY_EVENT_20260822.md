# A four-column cyclic Tikhonov bound and the `j=2` boundary-event quotient

**Date:** 2026-08-22

**Status.**  All Hilbert-space and `j=2` statements below are proved for
all parameters in their stated ranges.  They bypass the separate
`xi/delta` and dependent-module bookkeeping: one polynomial coercivity
bound for the cyclic differences of all four constraint columns gives a
polynomial compensated angle directly.  More specifically, the boundary
quotient proves the uniform polynomial bound

\[
                         \alpha^{(2)}_{r,2}\ge10^{-17}r^{-26}\qquad(r\ge5).
\]

Thus the formerly worst observed shallow module `j=2` is closed at the
complete `W_2` Hilbert level.  The modules `3<=j<=r-2` remain open.

## 1. Four-column cyclic Tikhonov lemma

Let `T` be a unitary operator of order `b` on a real Hilbert space and put

\[
 P={1\over b}\sum_{t=0}^{b-1}T^t.
\]

Thus `P` is the orthogonal projection onto the `T`-invariant subspace.  Let
`q` satisfy `Pq=q`, and let `v_1,...,v_m` be constraint columns.  Choose
positive scales `B_i` with `||v_i||<=B_i`, and define

\[
 D_{ij}=\langle (I-T)v_i,(I-T)v_j\rangle,
 \qquad
 \widetilde D_{ij}={D_{ij}\over B_iB_j},
 \qquad
 \lambda=\lambda_{\min}(\widetilde D).              \tag{1.1}
\]

### Theorem 1.1

If `lambda>0`, then

\[
 \boxed{
 {\operatorname {dist}(q,\operatorname {span}\{v_1,\ldots,v_m\})^2
  \over\|q\|^2}
 \ge {\mu\over m+\mu},
 \qquad \mu={\lambda\over2b}.}                     \tag{1.2}
\]

In particular, for the four Gate-B columns,

\[
 \boxed{\alpha^{(2)}_{r,j}\ge
 {\lambda_{r,j}/(2b)\over4+\lambda_{r,j}/(2b)}.}   \tag{1.3}
\]

This assertion includes modules on which the two conditioned `W_2`
columns are dependent; no rank-two determinant `xi` is used.

#### Proof

For `f=sum_i x_i v_i`, put

\[
                         X^2=\sum_i B_i^2x_i^2.
\]

The finite cyclic variance identity gives

\[
 \|(I-P)f\|^2={1\over2b}\sum_{t=0}^{b-1}\|f-T^tf\|^2
 \ge {1\over2b}\|f-Tf\|^2
 \ge\mu X^2.                                      \tag{1.4}
\]

Also

\[
 \|Pf\|\le\|f\|\le\sum_i|x_i|B_i\le\sqrt m\,X. \tag{1.5}
\]

Since `q` is invariant, the invariant and noninvariant pieces are
orthogonal.  If `Q=||q||`, then

\[
 \|q-f\|^2
 =\|q-Pf\|^2+\|(I-P)f\|^2
 \ge(Q-\sqrt m\,X)_+^2+\mu X^2.                  \tag{1.6}
\]

On `0<=X<=Q/sqrt(m)`, the right side is a quadratic with minimum
`mu Q^2/(m+mu)`; beyond that interval its second term is already at least
that value.  Taking the infimum over the original coefficients proves
(1.2). `square`

For Gate B one may take `B_i=||v_i||` when the column is nonzero.  More
convenient explicit upper scales are also allowed.  The exact remaining
lemma in this route is therefore

\[
 \lambda_{r,j}\ge r^{-C}
 \quad(2\le j\le r-2),                             \tag{1.7}
\]

or, after using the independently proved orbit lower bound, any weaker
bound for which `Theta_(r,j) lambda_(r,j)/b` is polynomially bounded below.

## 2. Exact `j=2` boundary states

Put

\[
 b=2r+1,\qquad k=r-2,\qquad \ell=b-k=r+3,
 \qquad r\ge4.
\]

On the position cycle let `I_s(u)` be the cyclic interval of length `s`
starting at `u`.  Fix two ordered distinguished label pairs
`(a_1,b_1),(a_2,b_2)` and put

\[
 H_s(A)=
 (\mathbf1_{\{a_1\in A\}}-\mathbf1_{\{b_1\in A\}})
 (\mathbf1_{\{a_2\in A\}}-\mathbf1_{\{b_2\in A\}}).         \tag{2.1}
\]

For a permutation `g`, the value of every harmonic lift depends only on
the ordered preimage tuple

\[
 (g^{-1}a_1,g^{-1}b_1,g^{-1}a_2,g^{-1}b_2).
\]

For each `t in Z_b`, define the boundary tuple

\[
 e_t=(t,t-1,t+k-1,t+k).                            \tag{2.2}
\]

The first pair straddles the left boundary of `I_k(t)` and the second
pair straddles its right boundary, with both positive endpoints inside.

Define the punctured central columns and the full shallow column by

\[
 c_s(g)=\sum_{u=1}^{b-1}H_s(gI_s(u)),\quad s\in\{r,r-1\},
 \qquad
 q(g)=\sum_{u=0}^{b-1}H_k(gI_k(u)).                \tag{2.3}
\]

### Lemma 2.1 (exact boundary values)

For every `t`,

\[
 \boxed{q(e_t)=1,\qquad c_r(e_t)=c_{r-1}(e_t)=0.}  \tag{2.4}
\]

#### Proof

An interval on the cycle splits both adjacent endpoint pairs in (2.2)
only if its two boundary edges are exactly the two displayed edges.  The
two arcs between those edges have lengths `k` and `ell`.  Since
`k!=ell`, the unique `k`-interval which splits both pairs is `I_k(t)`,
and its two factors in (2.1) are positive.  This proves `q(e_t)=1`.
Neither `r` nor `r-1` equals `k` or `ell`, so no interval of either central
length splits both pairs.  Every summand defining the two `c` columns is
therefore zero. `square`

For uniform `g`, the ordered four-preimage tuple is uniform on the
`(b)_4` injective tuples.  The `b` events in (2.2) are disjoint, so their
total probability is exactly `b/(b)_4`.

## 3. Exact two-profile quotient

Let `w_r,w_(r-1)` be the two `W_2` harmonic constraint columns.  Explicitly,
if

\[
 E_0=\{I_r(u),I_{r-1}(u):1\le u\le b-1\},
\]

`deg(S,T,U)` counts permutations whose image of `E_0` contains the three
displayed targets, and

\[
 W_{2,s}(S)=\sum_{\{T,U\}\in{E_0\choose2}}\deg(S,T,U),
 \qquad
 w_s(g)=\sum_{S\in{[b]\choose s}}W_{2,s}(S)H_s(gS),          \tag{3.1}
\]

then put

\[
 \omega_s(t)=w_s(e_t),\qquad s\in\{r,r-1\},                  \tag{3.2}
\]

and

\[
 \rho_r={1\over b}\min_{x,y\in\mathbb R}
 \sum_{t\in\mathbb Z_b}
 (1-x\omega_r(t)-y\omega_{r-1}(t))^2.             \tag{3.3}
\]

### Theorem 3.1 (boundary-event lower bound)

For the complete-state `j=2` angle,

\[
 \boxed{
 \alpha^{(2)}_{r,2}\ge
 {\rho_r\over4b\,k(k-1)\ell(\ell-1)}.}            \tag{3.4}
\]

Consequently any polynomial lower bound on `rho_r` proves a polynomial
angle at `j=2`.

#### Proof

By (2.4), restriction to the boundary events deletes both central columns
and makes the target column identically one.  Hence

\[
 \operatorname {dist}(q,\operatorname {span}\{c_r,c_{r-1},w_r,w_{r-1}\})^2
 \ge {b\rho_r\over(b)_4}.                         \tag{3.5}
\]

For one fixed `k`-interval,

\[
 \kappa_{k,2}=\|H_k(gI_k(0))\|_2^2
 ={4(k)_2(\ell)_2\over(b)_4},                     \tag{3.6}
\]

because each distinguished pair chooses one endpoint inside and one
outside.  The triangle inequality in (2.3) gives
`||q||<=b sqrt(kappa_(k,2))`.  Divide (3.5) by this upper bound squared and
substitute (3.6), obtaining (3.4). `square`

There is a useful three-state certificate.  Put

\[
 u_t=(\omega_r(t),\omega_{r-1}(t)),\qquad
 K_r=|\det(u_0-u_3,u_1-u_3)|,
\]

and let

\[
 H_r=\max\{|\omega_s(t)|:s\in\{r,r-1\},\ t\in\{0,1,3\}\}.
\]

If `K_r>0`, the three-by-three matrix with rows `(1,u_0),(1,u_1),(1,u_3)`
has determinant of absolute value `K_r`.  The Schur-complement formula and
Hadamard's inequality give

\[
 \boxed{\rho_r\ge {K_r^2\over9bH_r^4}.}            \tag{3.7}
\]

Indeed, the squared distance of the first column from the other two on
these three rows is `K_r^2/det(U^T U)`, where `U` has rows `u_0,u_1,u_3`;
and `det(U^T U)<=9H_r^4`.  The full sum in (3.3) is no smaller.

## 4. Puncture localization and the exact local determinant

Let

\[
 X=\{I_r(u),I_{r-1}(u):u\in\mathbb Z_b\},\qquad
 A=I_r(0),\quad B=I_{r-1}(0),
\]

so `E_0=X-{A,B}`.  For two central targets `T,U`, let
`Phi_s(T,U;e_t)` denote their contribution to `omega_s(t)` in (3.1).
The complete pair catalogue `X` is invariant under cyclic translation, so
its profile is constant in `t`.  Passing from `X` to `E_0` subtracts the
pairs meeting `A` or `B`:

\[
 \omega_s(t)=\omega_s^X-
 \sum_{U\in X-\{A\}}\Phi_s(A,U;e_t)
 -\sum_{U\in X-\{B\}}\Phi_s(B,U;e_t)
 +\Phi_s(A,B;e_t).                                \tag{4.1}
\]

### Lemma 4.1 (exact six-state localization)

For every `r>=4`, the joint profile
`(omega_r(t),omega_(r-1)(t))` is constant off

\[
                         \boxed{\{0,1,2,r-1,r,r+3\}.}        \tag{4.2}
\]

#### Proof

Fix a missing target `M in {A,B}` and another central target `U`.  If the
two endpoints of either distinguished pair in `e_t` lie in the same cell
of the partition generated by `M,U`, swapping those endpoints preserves
the root-set count and reverses the harmonic sign.  Hence
`Phi_s(M,U;e_t)=0`.  A nonzero term therefore requires both boundary edges
of `I_k(t)` to be boundaries of `M` or `U`.  If neither is a boundary of
`M`, they would have to be the two boundaries of `U`; but the arcs between
them have lengths `k=r-2` and `r+3`, whereas `U` has length `r` or `r-1`.
Thus at least one displayed edge is a boundary of `M`.

The boundaries of `A` are `(-1,0)` and `(r-1,r)`, which give
`t in {0,r+3,r,2}`.  The boundaries of `B` are `(-1,0)` and
`(r-2,r-1)`, which give `t in {0,r+3,r-1,1}`.  Their union is (4.2), and
(4.1) proves the claim. `square`

For `r>=5`, `t=3` is outside (4.2).  Put

\[
 d_t=u_t-u_3=(d_{t,M},d_{t,L}).                  \tag{4.3}
\]

Only the following local pairs contribute to `d_0,d_1`:

\[
\begin{array}{c|c|c}
t&\text{missing target }M&\text{possible }U\\ \hline
0&A,B&I_r(k),I_r(b-2),I_{r-1}(k),I_{r-1}(b-1)\\
1&B&I_r(1),I_r(r+2),I_{r-1}(1),I_{r-1}(r+3).
\end{array}                                                        \tag{4.4}
\]

Here is a compact exact audit of the resulting Venn calculation.  For a
fixed pair `T,U`, let its four labelled cells have sizes `n_i`.  If a root
has `m_i` elements in cell `i`, let `N(m)` be the number of retained
positional start triples with that signature.  Conditional on the counts
`m_i`, independently choose a uniform `m_i`-subset in every cell and let
`eta_e(m,n)` be the expectation of the product (2.1).  Explicitly, for two
distinct displayed points in cells `i,j`,

\[
 R_{ij}=\begin{cases}
 m_im_j/(n_in_j),&i\ne j,\\
 m_i(m_i-1)/(n_i(n_i-1)),&i=j,
 \end{cases}                                                    \tag{4.5}
\]

with the evident zero convention, and `eta_e` is the signed four-term
combination `R_ac-R_ad-R_bc+R_bd`.  The binomial choices of the root set
cancel its Venn factorials exactly, giving

\[
 \boxed{\Phi_s(T,U;e)=
 \left(\prod_i n_i!\right)\sum_m N(m)\eta_e(m,n).}             \tag{4.6}
\]

This is a finite cyclic-start sum, not an asymptotic approximation.
Substitution of the twelve pairs in (4.4) into (4.6), followed only by
collecting falling factorials, gives the following formulas.  Write

\[
\begin{aligned}
 P_0(r)&={1\over3}(2r^7-4r^6-12r^5+54r^4-270r^3
                    +549r^2-98r-176),\\
 P_1(r)&={1\over3}(2r^7-4r^6-24r^5+81r^4-267r^3
                    +687r^2-386r-8),\\
 P_2(r)&={1\over3}(2r^6-4r^5+16r^3-218r^2+567r-318),\\
 P_3(r)&={1\over6}(4r^5-4r^4-16r^3+13r^2-396r+1128),
\end{aligned}                                                   \tag{4.7}
\]

and

\[
\begin{aligned}
 Q_0(r)&=r^3(r+1)(r-1)^2(r-2)^2,\\
 Q_2(r)&=r^3(r+1)(r-1)^2(r-2),\\
 Q_3(r)&=r^3(r+1)(r-1)(r-2).
\end{aligned}                                                   \tag{4.8}
\]

Then, with `D_M=2r r!(r+1)!`,

\[
 \boxed{
 {d_{0,M}\over D_M}={P_0\over Q_0},\quad
 {d_{0,L}\over D_M}={P_1\over Q_0},\quad
 {d_{1,M}\over D_M}={P_2\over Q_2},\quad
 {d_{1,L}\over D_M}={P_3\over Q_3}.}             \tag{4.9}
\]

Equations (4.4)--(4.6) are also a short independent derivation recipe for
every coefficient in (4.7); no interpolation premise is being used.

### Theorem 4.2 (uniform `j=2` noncancellation)

For every `r>=5`,

\[
 \boxed{K_r\ge {D_M^2\over14000r^4}.}             \tag{4.10}
\]

#### Proof

Since `K_r=|det(d_0,d_1)|`, (4.9) simplifies exactly to

\[
 {K_r\over D_M^2}=
 {N(r)\over r^6(r+1)^2(r-1)^4(r-2)^3},             \tag{4.11}
\]

where

\[
\begin{split}
 6N(r)={}&8r^{11}-54r^{10}+138r^9-28r^8-1210r^7+5092r^6\\
 &-6937r^5-10495r^4+19768r^3+58176r^2-131368r+64480.
                                                               \tag{4.12}
\end{split}
\]

Put `x=r-4`.  Direct binomial expansion gives

\[
\begin{split}
 6N(x+4)={}&8x^{11}+298x^{10}+5018x^9+50540x^8+338502x^7\\
 &+1582220x^6+5263911x^5+12471117x^4+20632488x^3\\
 &+22656960x^2+14751576x+4249152.                 \tag{4.13}
\end{split}
\]

Every coefficient is positive.  Moreover
`N(r)>=(x^11+4^11)/6>=r^11/(6*2^10)>r^11/7000`, where the middle inequality
uses `(x+4)^11<=2^10(x^11+4^11)`.  The denominator of (4.11) is at most
`(25/16)r^15<2r^15`.  Equation (4.10) follows. `square`

The case `r=4` is positive by the displayed exact finite value below.

## 5. A completely explicit polynomial `j=2` angle

There are `|E_0|=4r` base central targets.  Every pair degree is at most

\[
 D_L={r+2\over r}D_M\le {3\over2}D_M.
\]

Therefore, writing `M_2=sum_{\{T,U\}}deg(T,U)`,

\[
 M_2\le {4r\choose2}D_L<12r^2D_M.                \tag{5.1}
\]

Every configuration contains `2r` rank-`s` targets on a fixed central
shore, so double counting gives

\[
 \|W_{2,s}\|_1=2rM_2<24r^3D_M.                  \tag{5.2}
\]

Since the harmonic kernel has absolute value at most one, (5.2) gives
`H_r<=24r^3D_M`.  Combining (3.7), (4.10), `b<=3r`, and then (3.4) gives
for `r>=5`

\[
 \rho_r\ge {1\over2\cdot10^{15}r^{21}},
 \qquad
 \boxed{\alpha^{(2)}_{r,2}\ge {1\over10^{17}r^{26}}}.        \tag{5.3}
\]

The constants are deliberately crude; only a uniform polynomial matters.

## 6. Exact finite calibration

The exact Hahn--Venn checker gives:

| `r` | rank of the two restricted profiles | augmented rank with `1` | `rho_r` | `r^4 K_r/D_M^2` |
|---:|---:|---:|---:|---:|
| 4 | 2 | 3 | .0569582 | 4.27278 |
| 5 | 2 | 3 | .0550590 | 2.19698 |
| 6 | 2 | 3 | .0537548 | 1.93179 |
| 7 | 2 | 3 | .0520087 | 1.78529 |
| 8 | 2 | 3 | .0498339 | 1.69422 |
| 9 | 2 | 3 | .0475378 | 1.63269 |

For `4<=r<=9`, the restriction has rank two and adjoining the constant
raises the rank to three.  The six-exception count agrees with Lemma 4.1.
For `5<=r<=9`, if the common value is `A` and `d_t=u_t-A`, the additional
exact identity `d_0=d_1+d_2` holds; that identity is not needed above.

The exact checker independently replays the local formulas through `r=35`
and again at `r=40,50`.  In the smaller displayed range `7<=r<=16`,
the values of `r^4K_r/D_M^2` decrease from
`1.785288...` to `1.467278...` and remain positive, consistently approaching
the leading constant `4/3` in (4.11)--(4.12).

## 7. What has and has not been closed

Theorem 1.1 removes a logical nuisance from Gate B: proving a cyclic
difference bound for all four constraints simultaneously automatically
handles rank-two and dependent `W_2` modules.  Theorem 3.1 reduces the
observed worst shallow module `j=2` to two one-dimensional cyclic profiles.
Theorem 4.2 and (5.3) close that module uniformly at the complete `W_2`
Hilbert level.

Still open are:

1. the corresponding uniform argument for `3<=j<=r-2`;
2. transfer from `W_2` to full exposure, delocalized inversion, stopped
   stability, and hole-aligned accumulated gain.
