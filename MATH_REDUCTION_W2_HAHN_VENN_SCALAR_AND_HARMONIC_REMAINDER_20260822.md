# The exact `W_2` Hahn--Venn scalar and harmonic remainder bound

**Date:** 2026-08-22

**Status:** unconditional all-`r` Gram formula; an exact normalized `3 by 3`
scalar identity when the two residual `W_2` directions are independent,
with the dependent case obtained by deleting the redundant direction;
exact finite calibration through `r=9`; and an unconditional modulewise
bound for the higher-order remainder.  No uniform relative lower bound for
the new scalar is claimed.

## 1. Setup

Put

\[
 b=2r+1,\qquad k=r-2,\qquad N={b\choose k},\qquad
 p={b\over N},\qquad X_s={[b]\choose s}.
\]

On the position cycle `Z_b`, let `I_s(a)` be the cyclic interval of length
`s` starting at `a`.  The identity punctured configuration is the
layer-tagged family

\[
 E_0=\{(r,I_r(a)):1\le a\le b-1\}
 \mathbin{\dot\cup}
 \{(r-1,I_{r-1}(a)):1\le a\le b-1\}.
\]

A word `w in S_b` relabels these intervals and gives a configuration
`E(w)`.  To see injectivity directly, write
\(L_i=I_{r-1}(i)\) and \(M_i=I_r(i)\).  Containment among the retained
sets is exactly the alternating path
\[
 L_1,M_1,L_2,M_2,\ldots,L_{b-1},M_{b-1}.
\]
Its endpoint layers orient it, so every same-start pair is recovered.
Moreover
\(w(M_i)\setminus w(L_i)=\{w_{i+r-1}\}\) for \(1\le i\le b-1\).
These differences recover every word position except \(r-1\), and the
unique unused label recovers that last position.  Thus the configurations
and words are in bijection.  For layer-tagged targets `A_0,...,A_m`, let
`deg(A_0,...,A_m)` be the number of configurations containing every one of
them, with a repeated condition imposed only once.

For `s in {r,r-1}`, define

\[
 c_s(S)=\mathbf1_{\{(s,S)\in E_0\}},\qquad
 W_{2,s}(S)=\sum_{\{T,U\}\in{E_0\choose2}}\deg(S,T,U),       \tag{1.1}
\]

and let

\[
 q_k(S)=\mathbf1_{\{S=I_k(a)\text{ for some }a\in\mathbb Z_b\}}.          \tag{1.2}
\]

The goal is the module angle of the five coefficient vectors

\[
                         c_r,c_{r-1},W_{2,r},W_{2,r-1},q_k.                \tag{1.3}
\]

For later normalization, put

\[
 n_h={k\choose h}{b-k\choose k-h},
\]
\[
 E_j(h)=\sum_{a=0}^j(-1)^{j-a}{j\choose a}
 {k-j\choose h-a}{b-k-j\choose k-j-h+a},                 \tag{1.4}
\]

where invalid binomials are zero, and let `w_0=6`, `w_k=1`, and
`w_h=2` otherwise.  The relative-density cyclic-deck orbit factor is

\[
 \boxed{
 \Theta_{r,j}={N\over b}\sum_{h=0}^k{w_hE_j(h)\over n_h}.}               \tag{1.5}
\]

Here is the normalization explicitly.  For a uniform cyclic word `g`, let
`Q_T(g)` indicate that the `k`-set `T` is one of its `b` cyclic windows,
and put

\[
 (Sf)_T=\mathbb E_g[f(g)Q_T(g)].
\]

For fixed `T,U` with `|T cap U|=h`, the `b` choices of the first window
start and the `w_h` compatible relative starts are distributed uniformly
over the `N n_h` ordered labelled pairs with intersection `h`.  Hence

\[
 (SS^*)_{T,U}=\mathbb E_g[Q_T(g)Q_U(g)]
 ={b w_h\over N n_h}.                                \tag{1.6}
\]

Applying this kernel to the distinguished-pair harmonic gives the
standard-output squared Fisher singular value

\[
 \theta_{r,j}={b\over N}\sum_{h=0}^k{w_hE_j(h)\over n_h}.
\]

The relative-density output is `p^(-1)S`, so its squared singular value is
`theta_(r,j)/p^2`, which is exactly (1.5).  This also fixes the convention:
`Theta` is a squared singular-value factor, not an unsquared norm factor.

## 2. A three-target Venn formula for `W_2`

For three subsets `A_0,A_1,A_2` and
`epsilon in {0,1}^3`, put

\[
 \nu_\epsilon(A_0,A_1,A_2)
 =\left|\bigcap_{i=0}^2 A_i^{\epsilon_i}\right|,
 \qquad A^1=A,\quad A^0=[b]\setminus A.                  \tag{2.1}
\]

For sizes `s_0,s_1,s_2`, define the positional signature multiplicity

\[
 \mathcal N_{s_0,s_1,s_2}(\nu)=
 \left|\left\{(a_0,a_1,a_2)\in[1,b-1]^3:
 \nu(I_{s_0}(a_0),I_{s_1}(a_1),I_{s_2}(a_2))=\nu
 \right\}\right|.                                          \tag{2.2}
\]

### Theorem 2.1 (exact Venn degree)

If `|A_i|=s_i`, then

\[
 \boxed{
 \deg(A_0,A_1,A_2)
 =\mathcal N_{s_0,s_1,s_2}(\nu(A_0,A_1,A_2))
  \prod_{\epsilon\in\{0,1\}^3}\nu_\epsilon(A_0,A_1,A_2)! .}             \tag{2.3}
\]

Consequently (1.1) is an explicit finite Venn sum involving only
`O(r^2)` base target pairs and the six positional tables corresponding to
`s_0 in {r,r-1}` and the three unordered size pairs
`{s_1,s_2} subseteq {r,r-1}`.

#### Proof

Fix a retained start triple.  A compatible word is precisely a bijection
from positions to labels which maps every positional Venn cell to the
corresponding labelled Venn cell.  It exists exactly when all eight cell
sizes agree, and then the cells can be bijected independently in
`product_epsilon nu_epsilon!` ways.  Summing over start triples proves
(2.3).  A proper target can occur at only one cyclic start in a word:
shifting a proper interval replaces one label by a distinct label.  Thus
no word is counted twice.  If two displayed targets coincide, the empty
off-diagonal Venn cells force their positional intervals to coincide as
well, so the repeated-condition convention is also respected. `square`

This formula removes the factorial catalogue: the tables in (2.2) use
only `(b-1)^3` start triples.

## 3. Boolean-zeta evaluation of every Hahn Gram entry

Fix `2<=j<=k` and choose disjoint distinguished pairs
`(a_i,b_i)`, `1<=i<=j`.  On `X_s`, put

\[
 H_s(A)=\prod_{i=1}^j
 (\mathbf1_{\{a_i\in A\}}-\mathbf1_{\{b_i\in A\}}),
 \qquad
 \mathcal R_{s,j}x(g)=\sum_{A\in X_s}x(A)H_s(gA).             \tag{3.1}
\]

All inner products and norms of these lifts use the uniform probability
measure on `S_b`.

For feasible `ell`, define

\[
 D_{s,t}(\ell)={b\choose s}{s\choose\ell}{b-s\choose t-\ell},            \tag{3.2}
\]

\[
 Z_{s,t,j}(\ell)=2^j\sum_{c=0}^j(-1)^{j-c}{j\choose c}
 {b-2j\choose
  \ell-c,\ s-j-\ell+c,\ t-j-\ell+c,\ b-s-t+\ell-c},                   \tag{3.3}
\]

where an invalid multinomial is zero, and put

\[
                         \zeta_{s,t,j}(\ell)
 ={Z_{s,t,j}(\ell)\over D_{s,t}(\ell)}.                  \tag{3.4}
\]

A uniform permutation sends a fixed pair of sets of intersection `ell`
uniformly over the `D_(s,t)(ell)` image pairs.  Splitting every
distinguished coordinate pair and recording whether the two images make
the same choice proves

\[
 \mathbb E_g[H_s(gA)H_t(gB)]
 =\zeta_{s,t,j}(|A\cap B|).                            \tag{3.5}
\]

For a coefficient vector `x` on `X_s`, define its superset transform

\[
 D_i x(C)=\sum_{\substack{A\in X_s\\C\subseteq A}}x(A),
 \qquad |C|=i,                                       \tag{3.6}
\]

and, for `x` on `X_s` and `y` on `X_t`, put

\[
 U_i(x,y)=\sum_{C\in X_i}D_i x(C)D_i y(C).          \tag{3.7}
\]

Let the Newton coefficients of the Hahn kernel be

\[
 \beta_i^{s,t,j}
 =\Delta^i\zeta_{s,t,j}(0)
 =\sum_{h=0}^i(-1)^{i-h}{i\choose h}\zeta_{s,t,j}(h).       \tag{3.8}
\]

For the ranks in (1.3), intersection zero is feasible.  Put
`m=min(s,t)`.  Newton interpolation on the `m+1` possible intersection
values is therefore literal and needs no asymptotic or polynomial-degree
claim.

### Theorem 3.1 (exact Hahn--zeta Gram)

For arbitrary coefficient vectors `x,y` on any two ranks appearing in
(1.3),

\[
 \boxed{
 \left\langle\mathcal R_{s,j}x,\mathcal R_{t,j}y\right\rangle_{L^2(S_b)}
 =\sum_{i=0}^{\min(s,t)}\beta_i^{s,t,j}U_i(x,y).}   \tag{3.9}
\]

#### Proof

Newton interpolation and (3.8) give

\[
 \zeta_{s,t,j}(\ell)=\sum_{i=0}^{\min(s,t)}
 \beta_i^{s,t,j}{\ell\choose i}.                  \tag{3.10}
\]

Furthermore

\[
 {|A\cap B|\choose i}
 =\sum_{C\in X_i}\mathbf1_{\{C\subseteq A\}}
                       \mathbf1_{\{C\subseteq B\}}.         \tag{3.11}
\]

Insert (3.5) and (3.10), interchange the finite sums, and apply (3.11).
The result is exactly (3.9). `square`

Equations (2.3) and (3.9) are the promised all-`r` closed Hahn--Venn form.
They require no enumeration of `S_b`.  The usual Boolean-lattice zeta
transform evaluates every quantity (3.6)--(3.7) in `O(b2^b)` arithmetic
operations after the `W_2` vectors have been formed.

## 4. The five-vector angle reduces to one normalized `3 by 3` determinant

Let `v_1,...,v_5` be the five harmonic lifts in (3.1), in the order
(1.3), in the Hilbert space `L^2(S_b)` with uniform probability measure.
Whenever `v_5` is nonzero, define the second-order angle without reference
to coordinates by

\[
 \alpha^{(2)}_{r,j}
 ={\operatorname {dist}(v_5,\operatorname {span}\{v_1,v_2,v_3,v_4\})^2
   \over\|v_5\|_2^2}.                               \tag{4.1}
\]

Let `P_C` be orthogonal projection onto
`C=span{v_1,v_2}`, put

\[
 \bar w_1=(I-P_C)v_3,\qquad
 \bar w_2=(I-P_C)v_4,\qquad
 \bar q=(I-P_C)v_5,                                \tag{4.2}
\]

and let `H` be their `3 by 3` Gram matrix in this order.  These definitions
remain literal if the central vectors are dependent.  If
`G_(r,j)^(2)` denotes the `5 by 5` Gram matrix from (3.9), and its central
`2 by 2` block is invertible, then equivalently

\[
 H=G_{\{3,4,5\},\{3,4,5\}}
 -G_{\{3,4,5\},\{1,2\}}
  G_{\{1,2\},\{1,2\}}^{-1}
  G_{\{1,2\},\{3,4,5\}}.                          \tag{4.3}
\]

Thus `H` is the Gram matrix of `W_(2,r),W_(2,r-1),q_k` after orthogonal
projection away from the two central incidence vectors.  Write `H_W` for
its leading `2 by 2` block and define

\[
 a^{(0)}_{r,j}={H_{33}\over G_{55}},\qquad
 \delta_{r,j}={\det H_W\over H_{11}H_{22}},\qquad
 \xi_{r,j}={\det H\over H_{11}H_{22}H_{33}}.       \tag{4.4}
\]

The next formula concerns the case in which `bar w_1,bar w_2` are nonzero
and independent.  In a degenerate case, delete a dependent residual vector
and use the corresponding one-dimensional Schur complement; degeneracy
does not introduce an additional constraint direction.

### Theorem 4.1 (exact conditional determinant scalar)

If `H_W` is positive definite and `H_33>0`, then

\[
 \boxed{
 \alpha^{(2)}_{r,j}
 =a^{(0)}_{r,j}{\xi_{r,j}\over\delta_{r,j}},
 \qquad 0<a^{(0)}_{r,j}\le1,\quad
 0\le\xi_{r,j}\le\delta_{r,j}\le1.}             \tag{4.5}
\]

For one fixed module, the single scalar bound

\[
 \boxed{
 \Theta_{r,j}a^{(0)}_{r,j}\xi_{r,j}\ge r^{-C}}    \tag{4.6}
\]

implies its required `W_2` lower bound.  If (4.6) holds with one absolute
`C`, uniformly for every `2<=j<=r-2` and all sufficiently large `r`, then
it is sufficient for the full infimum in H.47.

#### Proof

Successive orthogonal projection first removes the central span and then
the two residual `W_2` vectors.  The residual squared norm of `q_k` after
the first projection is `H_33`, giving the factor `a^(0)`; orthogonal
projection and the hypothesis `H_33>0` give `0<a^(0)<=1`.  The standard
Schur-complement identity gives

\[
 {\operatorname {dist}(\bar q,\operatorname {span}(\bar w_1,\bar w_2))^2
  \over H_{33}}
 ={\det H\over H_{33}\det H_W}
 ={\xi\over\delta}.                                \tag{4.7}
\]

Here every vector has already been projected by `I-P_C`.  This proves the
equality in (4.5).  After diagonal normalization, `H` is a
correlation matrix.  Hadamard's inequality gives `delta<=1`, and taking a
Schur complement inside this correlation matrix gives
`0<=xi/delta<=1`, hence `xi<=delta`.  Equation (4.6) now implies
`Theta alpha^(2)>=r^(-C)` because division by `delta<=1` can only increase
the left side. `square`

For clarity, all dependent cases have the following exact
coordinate-free reduction.  Let

\[
 W=\operatorname {span}\{\bar w_1,\bar w_2\},\qquad d=\dim W,
\]

and choose any basis \(u_1,\ldots,u_d\) from the nonzero independent
residual directions.  Put

\[
 A=(\langle u_a,u_b\rangle)_{a,b=1}^d,\qquad
 z=(\langle u_a,\bar q\rangle)_{a=1}^d.
\]

Then, with the parenthesis below interpreted as one when \(d=0\),

\[
 \boxed{
 \alpha^{(2)}_{r,j}
 ={H_{33}\over G_{55}}
 \left(1-{z^{\mathsf T}A^{-1}z\over H_{33}}\right).}       \tag{4.8}
\]

For \(d=1\), the parenthesis is
\(1-|\langle u_1,\bar q\rangle|^2/(\|u_1\|^2H_{33})\).  For \(d=2\),
(4.8) is (4.5).  The value is independent of the chosen basis because the
quadratic term is the squared norm of the projection of \(\bar q\) onto
\(W\).  If \(H_{33}=0\), then \(v_5\) already lies in the central span and
\(\alpha^{(2)}=0\).  If \(G_{55}=0\), the module has no shallow-current signal at
all, so its orbit-scale product is zero rather than a case in which
(4.1) is defined.  Thus no nonsingularity hypothesis is hidden in the
definition of the angle; only the normalized determinant notation
`xi/delta` requires rank two.

Thus the first exact asymptotic obstruction is no longer a factorial
catalogue or an unspecified five-vector determinant.  It is the normalized
conditional volume `xi_(r,j)` in (4.4), together with the explicit central
factor `a^(0)` and orbit factor `Theta`.  A small `delta` is not itself an
obstruction: it appears in the denominator of (4.5).

## 5. Exact finite calibration

The Hahn--Venn computation gives the following exact-rational values; only
decimals are printed here for readability.  The selected module is the top
defect-zero module `j=k=r-2`.

| `r` | `alpha^(2)` | `a^(0)` | `delta` | `xi` | `Theta alpha^(2)` |
|---:|---:|---:|---:|---:|---:|
| 4 | .172754 | .287968 | .174353 | .104595 | .691014 |
| 5 | .540662 | .604466 | .244490 | .218683 | 5.79280 |
| 6 | .601418 | .616893 | .166973 | .162784 | 28.3526 |
| 7 | .733484 | .739966 | .458251 | .454236 | 119.456 |
| 8 | .763429 | .766248 | .264740 | .263767 | 476.380 |
| 9 | .821210 | .822490 | .578735 | .577834 | 1852.59 |

At `r=4,5` the exact fractions agree with the independent factorial
catalogue certificates.  The values through `r=9` are exact computations,
not an asymptotic theorem.  They suggest that `xi/delta` tends to one in
the top regime, but the present note does not assert this.

## 6. An unconditional modulewise bound for the higher-order remainder

Put `D_M=2r r!(r+1)!`.  The full exposure satisfies
`e_s=W_(2,s)-R_s`, where `R_s>=0` and `||R_s||_1=O(D_M)`.  The latter
estimate follows self-containedly as
follows.  If `t_F=|F cap E_0|`, then

\[
 R_s(S)=\sum_{F:S\in F_s}
 { (t_F-1)(t_F-2)\over2}\mathbf1_{\{t_F\ge3\}},
 \qquad
 \|R_s\|_1\le2r\sum_F{t_F\choose3}.               \tag{6.1}
\]

We record the specialized boundary-codegree estimate used here rather
than hiding it behind an appeal to total mass.  Multiplication of the cut
circle by `-2 mod b` sends the boundary edges of retained `r`- and
`(r-1)`-intervals to step-one and step-three edges, respectively; the two
omitted starts delete one edge of each type.  This graph has maximum degree
four, and it is triangle-free for `b>=11`.

Fix a triple `J` of retained targets and let `v` be the number of its
distinct boundary cuts.  After anchoring the first interval start, a
second interval of either allowed length has at most four relative starts
with a prescribed intersection with the anchor.  A full three-target
Venn signature therefore has at most `(b-1)4^2` positional realizations.
For one realization let `V` be the product of the eight Venn-cell
factorials, and let `G=product_i g_i!`, where the positive elementary
boundary gaps have sizes `g_1,...,g_v`.

We claim `V<=8^2G`.  For the first interval, `V=G`.  On exposing another
interval, if its new cuts refine distinct old gaps, the product of the gap
binomial coefficients injects into the corresponding Venn-cell choice;
equivalently this is the appropriate summand of Vandermonde's identity,
so `V/G` cannot increase.  The same is true when one or both cuts were
already present.  If both new cuts lie in one old gap of size `g`, write
the three new pieces as `x,y,z`, with `y` between the cuts.  The first
choice factor `binom(g,y)` is paid by the Venn-cell split just described.
The segment of length `y` is the new interval or its complement, so
`y` belongs to `{r-1,r,r+1,r+2}`.  Every old gap after the first interval
has size at most `r+2`; hence `g-y<=3`, and the remaining factor is at most
`2^(g-y)<=8`.  There are only two further intervals, proving the claim.

Factorial log-convexity, moving mass from smaller gaps to a largest
nonsaturated gap, gives for `r>=6` (recall `v<=6`)

\[
 G\le(r+2)!(r-v+1)!.
\]

For completeness,
\((r)_m=m!{r\choose m}\ge(m/e)^m(r/m)^m=(r/e)^m\):
the binomial factor follows termwise, and
\(\log(m!)\ge\int_1^m\log x\,dx\ge m\log m-m\).
Taking \(m=v-1\), it follows that

\[
 {G\over r!(r+1)!}
 \le {r+2\over(r)_{v-1}}
 \le3e^{v-1}r^{2-v}.                              \tag{6.2}
\]

The retained positional multiplicity, the bound `V<=64G`, and
`D_M=(b-1)r!(r+1)!` now give, after enlarging one absolute constant to
cover `4<=r<6`,

\[
                         {\deg(J)\over D_M}\le C^3r^{2-v}
 \qquad(|J|=3).                                    \tag{6.3}
\]

Three boundary edges with `v=4,5,6` incident cuts occur in
`O(r),O(r^2),O(r^3)` ways: by bounded degree and triangle-freeness these
are, respectively, a connected three-edge graph, an adjacent pair plus a
disjoint edge, and three disjoint edges.  Double-counting a configuration
together with three of its retained base targets gives

\[
 \sum_F{t_F\choose3}
 =\sum_{J\in{E_0\choose3}}\deg(J)=O(D_M/r)
\]

by (6.3), and (6.1) gives

\[
                              \|R_s\|_1=O(D_M).     \tag{6.4}
\]

The following estimate is genuinely modulewise.

### Theorem 6.1 (harmonic `L^1` to `L^2` transfer)

For any coefficient vector `x` on `X_s`,

\[
 \boxed{
 \|\mathcal R_{s,j}x\|_{L^2(S_b)}
 \le\sqrt{\kappa_{s,j}}\,\|x\|_1,
 \qquad
 \kappa_{s,j}={2^j{b-2j\choose s-j}\over{b\choose s}}.}     \tag{6.5}
\]

Consequently

\[
 \boxed{
 \|\mathcal R_{s,j}R_s\|_2
 =O(D_M\sqrt{\kappa_{s,j}}).}                     \tag{6.6}
\]

For fixed top defect `d`, with `j=k-d`, this becomes

\[
 \|\mathcal R_{r,k-d}R_r\|_2,
 \ \|\mathcal R_{r-1,k-d}R_{r-1}\|_2
 =O_d(D_M 2^{-r/2}r^{1/4}).                       \tag{6.7}
\]

#### Proof

For a uniform image of one fixed `s`-set, `H_s` is nonzero exactly when the
set chooses one coordinate from each distinguished pair.  There are
`2^j binom(b-2j,s-j)` such sets, proving

\[
                         \mathbb E_g H_s(gS)^2=\kappa_{s,j}. \tag{6.8}
\]

Minkowski's inequality applied to (3.1) gives

\[
 \|\mathcal R_{s,j}x\|_2
 \le\sum_S|x(S)|\,\|H_s(gS)\|_2
 =\sqrt\kappa\,\|x\|_1,
\]

which proves (6.5)--(6.6).  If `j=r-2-d`, then `b-2j=5+2d` and
`s-j` is `d+2` or `d+1`.  Finally
`binom(2r+1,r)=Theta(4^r/sqrt(r))`, giving (6.7). `square`

Equation (6.7) is exponentially stronger than the bare `L^1` statement in
absolute harmonic norm.  It is still not the required perturbation theorem:
the corresponding harmonic norms and conditioning of the `W_2` constraint
vectors may live on the same exponentially small scale.  No relative bound
is claimed.

## 7. Exact remaining gate and verifier

The immediate positive alternatives are now precise.  For `W_2`, either
prove (4.6) uniformly over the desired asymptotic module regime, or prove
the original product directly through a lower bound on
`Theta a^(0)xi/delta`.  For the full exposure, one must additionally
compare (6.6) with the smallest conditioned `W_2` harmonic singular scale
rather than with total mass.

The exact verifier is

```text
python3 scratch/research_w2_hahn_venn_exact_20260822.py 4
python3 scratch/research_w2_hahn_venn_exact_20260822.py 5
```

It constructs (2.2)--(2.3), verifies the Hahn/Newton kernel exactly,
evaluates (3.9) by exact rational arithmetic, checks
`alpha^(2)=a^(0)xi/delta`, and asserts all three independently certified
`r=4,5` fractions.  Arguments `6,...,9` reproduce the additional exact
finite calibration without factorial enumeration.
