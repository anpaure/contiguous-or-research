# Gate A conflict variance: companion energy, duplicate pair squares, and the microstep ledger

**Date:** 2026-08-22

**Status:** unconditional deterministic reduction and stopped summability
criterion.  The criterion is not yet a proof of Gate A.  It shows that the
existing sixth degree moment, used through a pointwise Cauchy bound, loses
one power of `r` after all microsteps.  The two observables sufficient for
the **conflict-variance contribution** are a signed companion-degree energy
and a skeleton-weighted pair-codegree square energy; other Gate-A inputs
remain separate.

## 1. Setup and normalization

Let `H` be a finite simple hypergraph whose vertices are split into shores
`V_sigma`.  Every edge contains exactly `k_sigma` vertices of shore
`sigma`; put

\[
 q=\sum_\sigma k_\sigma,\qquad Z=|E(H)|,\qquad
 n_\sigma=|V_\sigma|,\qquad z_\sigma={k_\sigma Z\over n_\sigma}.
                                                               \tag{1.1}
\]

All averages over `F` below are uniform over `E(H)`.  Fix a reference
shore `sigma_*`, write `z_*=z_(sigma_*)`, and put

\[
 R_\sigma={z_\sigma\over z_*},\qquad
 U_{p,\sigma}={1\over n_\sigma z_\sigma^p}
       \sum_{v\in V_\sigma}|d(v)-z_\sigma|^p.          \tag{1.2}
\]

Assume the two-shore cap

\[
                         d(v)\le Kz_\sigma
       \quad(v\in V_\sigma).                           \tag{1.3}
\]

At every checkpoint where the two shores are compared, assume also the
explicit fixed comparability condition

\[
 R^{-1}\le {z_\sigma\over z_*}\le R                 \tag{1.3a}
\]

for a constant `R>=1` independent of `r`.

In the punctured application, `k_M=k_L=2r`, `q=4r`, and we take
`z_*=z_M`.  In a matching-only residual, before any auxiliary unequal
purge, if `x=|L|/|L_0|`, equal removal from the two shores gives the exact
identities

\[
 { |M|\over|M_0|}={rx+2\over r+2},\qquad
 {z_L\over z_M}={|M|\over|L|}=1+{2\over rx}.          \tag{1.4}
\]

Thus, throughout `x>=r^(-alpha)` with any fixed `alpha<1`, the two shore
averages are `1+o(1)` comparable on the unpurged matching trajectory.  A
high-degree purge can delete unequal numbers of targets from the two
shores, so (1.4) must **not** be reused after such a purge.  At post-purge
checkpoints, (1.3a) is a separate stopped hypothesis, supplied in the
intended application by the paired-shore schedule.  Under (1.3a), no
hidden factor of `r` is lost by normalizing with `z_M` rather than `z_L`.

## 2. Exact conflict and duplicate identities

For an edge `F`, let

\[
 \Gamma(F)=\{G:G\cap F\ne\varnothing\},\qquad
 C_F=|\Gamma(F)|,\qquad
 A_F=\sum_{u\in F}d(u),                                \tag{2.1}
\]

and define its duplicate excess

\[
 \mathfrak E(F)=\sum_{G\in\Gamma(F)}(|G\cap F|-1).     \tag{2.2}
\]

The closed neighbourhood convention is important: `G=F` occurs in both
(2.1) and (2.2).  Double counting incidences gives

\[
                         \boxed{C_F=A_F-\mathfrak E(F).} \tag{2.3}
\]

There is a second exact form.  For `v notin F`, put

\[
 a_F(v)=|\{G:v\in G,\ G\cap F\ne\varnothing\}|,
 \qquad R_F=\sum_{v\notin F}a_F(v).                  \tag{2.4}
\]

Every member of `Gamma(F)` has `q` vertices, and its vertices split into
those in and outside `F`.  Hence

\[
                         \boxed{qC_F=A_F+R_F.}          \tag{2.5}
\]

Equation (2.5) explains why applying a range bound separately to all
external rows introduces a spurious factor `q`: their sum is already tied
to the conflict count.

For an unordered pair of distinct targets `P={u,v}`, write

\[
                         \lambda_P=d_H(P).             \tag{2.6}
\]

Remove the constant self-overlap from (2.2):

\[
 e_F=\mathfrak E(F)-(q-1),\qquad
 S_F=\sum_{P\in{F\choose2}}(\lambda_P-1).             \tag{2.7}
\]

Then, exactly,

\[
 S_F=\sum_{G\ne F}{|F\cap G|\choose2},\qquad
 e_F=\sum_{G\ne F}(|F\cap G|-1)_+,                   \tag{2.8}
\]

and therefore

\[
                         \boxed{0\le e_F\le S_F.}      \tag{2.9}
\]

Subtracting `q-1` in (2.7) is essential.  Without it, all codegree-one
pairs create a large artificial second moment even though the self term
has zero variance.

## 3. The punctured high/low pair-square energy

For a punctured configuration, call a target pair **high** if it is

1. a lower--middle containment pair; or
2. a disjoint middle--middle pair.

Inside every punctured configuration these pairs form, respectively, the
alternating containment path and the middle-disjointness path.  Thus every
edge contains exactly

\[
 h=(4r-1)+(2r-1)=6r-2                              \tag{3.1}
\]

high pairs.  Put

\[
 m={q\choose2}=8r^2-2r,\qquad
 \ell=m-h=8r^2-8r+2.                                \tag{3.2}
\]

This classification is intrinsic to the two target sets, so it remains
valid in every induced punctured residual.  Define

\[
 \Theta_H={1\over Zz_*^2}
   \sum_{P\ \mathrm{high}}\lambda_P(\lambda_P-1)^2,
 \qquad
 \Theta_L={1\over Zz_*^2}
   \sum_{P\ \mathrm{low}}\lambda_P(\lambda_P-1)^2.       \tag{3.3}
\]

### Lemma 3.1 (duplicate-square bound)

For every induced punctured residual,

\[
 \boxed{
 {\operatorname {Var}_F\mathfrak E(F)\over z_*^2}
 \le2\{h\Theta_H+\ell\Theta_L\}.}                    \tag{3.4}
\]

#### Proof

Write `S_F=S_F^H+S_F^L` according to (3.3).  Cauchy's inequality gives

\[
 (S_F^H)^2\le h\sum_{\substack{P\subset F\\P\ \mathrm{high}}}
                  (\lambda_P-1)^2,
 \qquad
 (S_F^L)^2\le \ell\sum_{\substack{P\subset F\\P\ \mathrm{low}}}
                  (\lambda_P-1)^2.                   \tag{3.5}
\]

Use `(x+y)^2<=2x^2+2y^2`, sum over `F`, and interchange `F,P`.
Every pair `P` is contained in exactly `lambda_P` current edges, so

\[
 {1\over Z}\sum_FS_F^2
 \le2z_*^2\{h\Theta_H+\ell\Theta_L\}.               \tag{3.6}
\]

Finally, subtracting the constant `q-1` does not change variance, and
(2.9) gives

\[
 \operatorname {Var}\mathfrak E
 =\operatorname {Var}e
 \le\mathbb E e_F^2\le\mathbb E S_F^2.
\]

This proves (3.4). `square`

The weights in (3.4) are the correct boundary-polymer weights.  In the
complete punctured hypergraph, the exact pair inventory gives

\[
 \Theta_H=O(1/r),\qquad \Theta_L=O(1/r^2),           \tag{3.7}
\]

because a high pair has codegree `O(D_M/r)`, a low pair has codegree
`O(D_M/r^2)`, and every edge contains `h=O(r)` and `ell=O(r^2)` pairs of
the two kinds.  Consequently the right side of (3.4) is `O(1)` at the
initial scale.  In fact transitivity makes the actual variance zero; (3.4)
is an intentionally positive majorant which can survive loss of
transitivity.

The current-scale propagation

\[
 \boxed{h\Theta_H+\ell\Theta_L=O(x^{-4})}             \tag{3.8}
\]

is the **pair-square gate** isolated by this note.  The power `x^-4` is
the nominal cost of conditioning on the two targets of each pair twice.
Neither (3.7) nor the boundary-codegree theorem by itself proves (3.8)
under the stopped adaptive law.

## 4. Companion-degree energy

Put

\[
 b_v=d(v)-z_{\operatorname {sh}(v)},\qquad
 a_0=\sum_\sigma k_\sigma z_\sigma,
\]

and define the centered companion energy

\[
 \Omega_A={1\over Zz_*^2}\sum_{F\in E(H)}(A_F-a_0)^2.
                                                               \tag{4.1}
\]

It has the exact pair expansion

\[
 \boxed{
 Zz_*^2\Omega_A
 =\sum_vd(v)b_v^2+2\sum_{\{u,v\}}\lambda_{uv}b_ub_v.} \tag{4.2}
\]

Indeed, `A_F-a_0=sum_(v in F)b_v`; expanding its square and summing over
`F` proves (4.2).  The cross term is signed.  Replacing it by its absolute
value destroys the companion mixing which a stopped proof must preserve.

There is nevertheless an unconditional cap bound.

### Lemma 4.1 (sixth-mass cap bound)

Under (1.3),

\[
 \boxed{
 \Omega_A\le Kq\sum_\sigma k_\sigma R_\sigma^2U_{2,\sigma}
 \le Kq\sum_\sigma k_\sigma R_\sigma^2U_{6,\sigma}^{1/3}.} \tag{4.3}
\]

#### Proof

For every edge,

\[
 (A_F-a_0)^2=\left(\sum_{v\in F}b_v\right)^2
 \le q\sum_{v\in F}b_v^2.                            \tag{4.4}
\]

Averaging and using (1.3) gives

\[
 {1\over Z}\sum_F(A_F-a_0)^2
 \le {q\over Z}\sum_\sigma\sum_{v\in V_\sigma}d(v)b_v^2
 \le Kq\sum_\sigma k_\sigma z_\sigma^2U_{2,\sigma}. \tag{4.5}
\]

Divide by `z_*^2`.  The second inequality in (4.3) is the normalized
Lyapunov inequality `U_2<=U_6^(1/3)`. `square`

In the punctured case, fixed shore comparability turns (4.3) into

\[
                         \Omega_A
 \le C_{K,R}r^2(U_{6,M}^{1/3}+U_{6,L}^{1/3}).        \tag{4.6}
\]

The sharper current-scale target is

\[
                         \boxed{\Omega_A=O(x^{-4}).}  \tag{4.7}
\]

Equation (4.2) shows that (4.7) is a signed companion-pair decorrelation
statement.  It is strictly weaker than pointwise degree regularity and is
not a consequence of (4.3).

## 5. Conflict variance

Define

\[
                         V_C^*={\operatorname {Var}_FC_F\over z_*^2}.
                                                               \tag{5.1}
\]

### Theorem 5.1 (deterministic conflict-variance reduction)

Every capped induced punctured residual satisfies

\[
 \boxed{
 \sqrt{V_C^*}
 \le\sqrt{\Omega_A}
       +\sqrt{2\{h\Theta_H+\ell\Theta_L\}}.}          \tag{5.2}
\]

Consequently,

\[
 \boxed{
 V_C^*\le
 2Kq\sum_\sigma k_\sigma R_\sigma^2U_{6,\sigma}^{1/3}
 +4\{h\Theta_H+\ell\Theta_L\}.}                    \tag{5.3}
\]

#### Proof

By (2.3), `C=A-mathfrak E`.  The triangle inequality in `L^2(E(H))`
gives

\[
 \sqrt{\operatorname {Var}C}
 \le\sqrt{\operatorname {Var}A}
       +\sqrt{\operatorname {Var}\mathfrak E}.       \tag{5.4}
\]

The first variance is at most
`E(A_F-a_0)^2=z_*^2 Omega_A`; Lemma 3.1 bounds the second.  This proves
(5.2).  Square it using `(x+y)^2<=2x^2+2y^2` and apply (4.3) to obtain
(5.3). `square`

For the lower-shore normalization used in the protection theorem,

\[
 {\operatorname {Var}C_F\over z_L^2}={V_C^*\over R_L^2}. \tag{5.5}
\]

Thus (1.3a) makes (5.2)--(5.3) simultaneously valid on both punctured
shores with only a fixed `1+o(1)` change of constants.

For comparison, the cap alone gives

\[
 0\le\mathfrak E(F)\le A_F\le K\sum_\sigma k_\sigma z_\sigma,
                                                               \tag{5.6}
\]

and hence only `V_C^*=O_(K,R)(r^2)`.  That bound is enough for a total
`o(1)` protection error at a small stopping exponent, but not for the
`o(1/r)` shadow-purge budget.

## 6. What the centered row defect does and does not control

For a shore center `z`, put `f_z(d)=(d-z)^6` and

\[
 \phi_z(d,a)
 =a\{f_z(d)-f_z(d-1)\}-\{f_z(d)-f_z(d-a)\}.          \tag{6.1}
\]

The centered row defect is

\[
 \mathfrak D_{z,\sigma}(H)
 =\sum_{v\in V_\sigma}\sum_{G\not\ni v}
        \phi_z(d(v),a_G(v)).                         \tag{6.2}
\]

The shifted second-difference formula gives

\[
 \phi_z(d,a)=\sum_{s=0}^{a-2}(a-1-s)P(d-z-s),        \tag{6.3}
\]

where

\[
 P(t)=t^6-2(t-1)^6+(t-2)^6
     =30(t-1)^4+30(t-1)^2+2.                         \tag{6.4}
\]

In particular,

\[
 \boxed{\phi_z(d,a)\ge(a)_2.}                       \tag{6.5}
\]

There is a useful stronger form.  Normalize the weights `a-1-s` in
(6.3) to a probability distribution on `0,...,a-2`.  Its variance is

\[
                         {(a-2)(a+1)\over18}.         \tag{6.6}
\]

Since the fourth moment about any point is at least the square of the
variance, (6.3)--(6.6) imply

\[
 \boxed{
 \phi_z(d,a)\ge(a)_2\left[1+{5\over108}
                 (a-2)^2(a+1)^2\right].}             \tag{6.7}
\]

The bracket is understood as irrelevant when `(a)_2=0`.

Let

\[
 Q_{2,\sigma}=\sum_{v\in V_\sigma}\sum_{G\not\ni v}(a_G(v))_2.
                                                               \tag{6.8}
\]

Equation (6.5) proves the unconditional comparison

\[
                         \boxed{Q_{2,\sigma}
                         \le\mathfrak D_{z,\sigma}.}   \tag{6.9}
\]

There is also an exact bridge to current pair codegrees.  Let

\[
 g(s)=(s)_2\left[1+{5\over108}(s-2)^2(s+1)^2\right]. \tag{6.10}
\]

Then

\[
 \boxed{
 \sum_{u\ne v}(d(u)-\lambda_{uv})g(\lambda_{uv})
 \le q\sum_\sigma\mathfrak D_{z_\sigma,\sigma}(H).} \tag{6.11}
\]

Indeed, for every edge `G` containing `u` but not `v`, all
`lambda_(uv)` edges through `u,v` meet `G`, so
`a_G(v)>=lambda_(uv)`.  There are `d(u)-lambda_(uv)` such `G`.
The integer function `g` is nondecreasing, and (6.7) bounds every row.
After summing over ordered `u,v`, each row `(v,G)` is used at most `q`
times, once for every `u in G`.  This proves (6.11).

Equation (6.11) is the sharp conclusion available from the centered
defect alone.  It controls a concentrated pair whenever the star of `u`
has many alternatives not containing `v`.  It degenerates for a
near-clone pair with `lambda_(uv)\approx d(u)`.  Moreover, converting its
sixth-power row weight to the cubic pair energies in (3.3) requires a
scale-sensitive interpolation.  Therefore (6.9)--(6.11) do **not** prove
the pair-square gate (3.8); claiming that implication would reintroduce a
missing near-clone/normalization hypothesis.

This failure has a literal finite witness.  Let `H={F,G}` consist of two
distinct `q`-edges with `t=|F cap G|>=2`.  For every external row
`(v,G)` or `(v,F)`, its occupancy is zero or one, so

\[
                         \mathfrak D_{z,\sigma}(H)=0          \tag{6.12}
\]

on every shore and at every center.  On the other hand, every pair
`P subset F cap G` has `lambda_P=2`, and hence

\[
 \sum_P\lambda_P(\lambda_P-1)^2
 \ge2{t\choose2}>0.                                      \tag{6.13}
\]

For a common target `u`, `d(u)=lambda_(uv)=2` for every other common
target `v`, so precisely the factor `d(u)-lambda_(uv)` in (6.11)
vanishes.  Thus no inequality which makes the pair-square energy vanish
with `mathfrak D` can hold for general induced residuals.  A positive
punctured theorem must use the stopped history, a priority rule, or an
additional current-scale near-clone estimate.

The witness separates the pair-square energy from the centered defect
alone.  It does not rule out a future joint inequality involving both
`Omega_A` and `mathfrak D`; no such inequality is proved here.

## 7. Stopped microstep audit

Let the coefficients `epsilon_j in (0,1]` be deterministic, and let the
actual marking probability in round `j` obey

\[
 p_j\le {C\epsilon_j\over r z_{M,j}}.                    \tag{7.1}
\]

The proof of the protection estimate is linear in `p_j`.  Retaining that
factor rather than absorbing it into a fixed constant gives

\[
 {p_j\over n_\sigma c_\sigma^6}(\mathcal P_{c,\sigma})_+
 \le {C\epsilon_j\over r}
 \left(U_{6,\sigma,j}
 +\sqrt{V_{C,\sigma,j}U_{6,\sigma,j}}\right).          \tag{7.2}
\]

For the lower shore, (1.3a) gives
`p_j z_(L,j)<=C epsilon_j/r`; for the middle shore this is immediate.
The elevated shadow centers satisfy `c_sigma=Theta(z_sigma)` with fixed
constants.  Hence (7.2) has one and the same constant on both shores.

Suppose that on the stopped good trajectory the lower-density clock
satisfies

\[
 x_{j+1}\le x_j,\qquad
 \log{x_j\over x_{j+1}}\ge c_0{\epsilon_j\over r},
 \qquad x_j\ge x_{\mathrm{stop}}:=r^{-\alpha}
 \quad(j<J),                                           \tag{7.3}
\]

for fixed `c_0>0`; the process stops at the first subsequent crossing of
`x_stop`.  The standard constant-size bite has
`epsilon_j=Theta(1)`.  The Taylor-safe construction has a polynomially
small `epsilon_j=epsilon_r` and `Theta(r log r/epsilon_r)` rounds; the
shadow Taylor remainder requires
`epsilon_r=o((r^2 log r)^-1)`.  This restriction does not alter the
weighted density integral below.
For every fixed `b>0`, comparison with the density integral gives

\[
 \boxed{
 \sum_{j<J}{\epsilon_j\over r}r^{-a}x_j^{-b}
 =O(r^{-a}x_{\mathrm{stop}}^{-b}).}                    \tag{7.4}
\]

Indeed `epsilon_j/r` is at most a fixed multiple of
`log(x_j/x_(j+1))`.  Summing the monotone function `x^-b` over those
logarithmic intervals proves (7.4), with the possible final crossing term
bounded directly by `r^-a x_stop^-b`.  An auxiliary purge only makes the
density drop larger and therefore cannot invalidate this upper bound; no
upper bound on the one-step density loss is being assumed.  Thus the extra
`epsilon_r^-1` microsteps cancel exactly against the `epsilon_r` in
(7.2); omitting either factor gives the wrong ledger.

Assume the stopped sixth-moment envelope already proved for the product
and exact-slice reference laws,

\[
 \mathcal U_j:=U_{6,M,j}+U_{6,L,j}
 \le C\{r^{-3}x_j^{-9}+r^{-4}x_j^{-21}
          +r^{-4}x_j^{-18}+r^{-5}x_j^{-45}\}
          +e^{-\Omega(r)}.                            \tag{7.5}
\]

The statement needed here is its stopped adaptive analogue; (7.5) is not
asserted merely from the reference calculation.

### Theorem 7.1 (fine quadratic gates are sufficient)

If, on the stopped trajectory,

\[
 \boxed{
 \Omega_{A,j}+h\Theta_{H,j}+\ell\Theta_{L,j}
 \le Cx_j^{-4}}                                      \tag{7.6}
\]

and (7.5) hold, then, for every fixed

\[
                         \boxed{\alpha<3/49},          \tag{7.7}
\]

\[
 \boxed{
 \sum_{j<J}\sum_{\sigma=M,L}{\epsilon_j\over r}
 \left(U_{6,\sigma,j}
       +\sqrt{V_{C,\sigma,j}U_{6,\sigma,j}}\right)
 =o(1/r).}                                            \tag{7.8}
\]

Here `V_(C,sigma)=Var_F(C_F)/z_(sigma)^2`; (1.3a) makes it comparable to
`V_C^*`.

#### Proof

Theorem 5.1 and (7.6) give `V_(C,sigma)=O(x_j^-4)` on both shores.
Thus the summand in (7.8) is at most a fixed multiple of

\[
 {\epsilon_j\over r}
 \{\mathcal U_j+x_j^{-2}\mathcal U_j^{1/2}\}.       \tag{7.9}
\]

For a monomial `r^-a x^-b` in (7.5), (7.4) bounds its direct
contribution by `O(r^-a x_stop^-b)`.  Its square-root contribution is

\[
 O\left(r^{-a/2}x_{\mathrm{stop}}^{-(b/2+2)}\right). \tag{7.10}
\]

The four exponent pairs `(a,b)` in (7.5) give

\[
\begin{array}{c|c|c}
(a,b)&\text{direct condition for }o(r^{-1})
     &\text{square-root condition for }o(r^{-1})\\ \hline
(3,9)&\alpha<2/9&\alpha<1/13\\
(4,21)&\alpha<1/7&\alpha<2/25\\
(4,18)&\alpha<1/6&\alpha<1/11\\
(5,45)&\alpha<4/45&\alpha<3/49.
\end{array}                                           \tag{7.11}
\]

The minimum is `3/49`, proving (7.8). `square`

The same conclusion has the stopped-expectation form actually used in
Gate A.  Let `mathcal G_j` be measurable at the current state.  Let
`xi_j` be a deterministic density-scale localization satisfying the
analogue of (7.3) with `xi` in place of `x`, and suppose
that `x_j=Theta(xi_j)` on `mathcal G_j`.  Replace (7.5)--(7.6) by

\[
 \mathbb E[\mathbf1_{\mathcal G_j}\mathcal U_j]
       \le \mathcal U_j^{\mathrm{ref}},\qquad
 \mathbb E\!\left[\mathbf1_{\mathcal G_j}
   \{\Omega_{A,j}+h\Theta_{H,j}+\ell\Theta_{L,j}\}\right]
       \le C\xi_j^{-4},                                    \tag{7.12}
\]

where `mathcal U_j^ref` is the right side of (7.5), with `xi_j` in place
of `x_j`.  The pointwise
Theorem 5.1 first gives

\[
 \mathbb E[\mathbf1_{\mathcal G_j}V_{C,\sigma,j}]
       \le C\xi_j^{-4}.                                    \tag{7.13}
\]

Cauchy's inequality, applied without conditioning on future cap
persistence, then gives

\[
 \mathbb E[\mathbf1_{\mathcal G_j}
       \sqrt{V_{C,\sigma,j}U_{6,\sigma,j}}]
 \le
 \sqrt{\mathbb E[\mathbf1_{\mathcal G_j}V_{C,\sigma,j}]
       \mathbb E[\mathbf1_{\mathcal G_j}U_{6,\sigma,j}]}.   \tag{7.14}
\]

Equations (7.4) and (7.10)--(7.11) therefore prove the expected analogue
of (7.8).  This is a stopped-event estimate, not probabilistic conditioning
on the event that the cap persists in all later rounds.

The existing collision telescope uses the stricter range `alpha<1/32`,
so (7.7) would not be the bottleneck.  In particular, proving (7.6) under
the stopped law would close the conflict-variance contribution to the
shadow theorem at the required `o(1/r)` scale.

### Proposition 7.2 (the `U_6`-only substitution misses one power)

Suppose only the cap estimate (4.6) is used for `Omega_A`, while the
pair-square part of (7.6) is granted.  Then Theorem 5.1 yields

\[
 V_C^*\le C\{r^2\mathcal U_j^{1/3}+x_j^{-4}\}.       \tag{7.15}
\]

The degree component of the protection bound is consequently
`C epsilon_j mathcal U_j^(2/3)` **per microstep**, without a remaining
`1/r` factor.
Summing all rounds gives `o(1)` for

\[
                         \alpha<7/90,                \tag{7.16}
\]

but not the required `o(1/r)`: already the first reference monomial
`U_6=O(r^-3x^-9)` contributes

\[
 \sum_{j<J}O(\epsilon_j\mathcal U_j^{2/3})
 =O(r^{-1}x_{\mathrm{stop}}^{-6}),                  \tag{7.17}
\]

which is not `o(1/r)` for any positive `alpha`.  At `alpha=0` it is only
`O(1/r)`, not a little-oh estimate.

#### Proof

Equation (7.15) and the protection factor `epsilon_j/r` give

\[
 {C\epsilon_j\over r}
 \{\mathcal U_j+\sqrt{V_C^*\mathcal U_j}\}
 \le C\left\{{\epsilon_j\mathcal U_j\over r}
       +\epsilon_j\mathcal U_j^{2/3}
       +{\epsilon_jx_j^{-2}\mathcal U_j^{1/2}\over r}\right\}.
                                                               \tag{7.18}
\]

There are `Theta(r/epsilon_r)` microsteps per unit logarithmic density
when `epsilon_j=epsilon_r`.  Applying (7.4) to the middle term gives, for
a monomial `(a,b)`,

\[
 O\left(r^{1-2a/3}x_{\mathrm{stop}}^{-2b/3}\right).  \tag{7.19}
\]

The four conditions for this to be `o(1)` are respectively
`alpha<1/6,5/42,5/36,7/90`; their minimum is (7.16).
Equation (7.17) is (7.19) for `(a,b)=(3,9)`. `square`

Thus a pointwise estimate is not enough: the number of microsteps must be
included.  The missing factor is precisely the companion decorrelation
(4.7), not another improvement of the elementary inequality
`U_2<=U_6^(1/3)`.

## 8. Exact remaining statement

This route reduces the conflict-variance part of Gate A to the following
two stopped quadratic estimates, uniformly until `x=r^-alpha`:

\[
 \boxed{
 \Omega_A=O(x^{-4}),\qquad
 h\Theta_H+\ell\Theta_L=O(x^{-4}).}                  \tag{8.1}
\]

They have distinct meanings.

* `Omega_A` is the signed covariance of degree deviations carried by one
  punctured configuration; replacing its signed pair term by absolute
  values loses the fatal factor `r`.
* `Theta_H,Theta_L` are current pair-codegree third energies with the
  exact one-dimensional/high and diffuse/low multiplicities supplied by
  the punctured boundary inventory.

The centered row defect gives the rigorous bridge (6.11), but does not
by itself imply either estimate in (8.1).  A stopped proof may establish
(8.1) directly, or establish an equivalent planted two-/three-carrier
comparison.  No full-state comparison is required.

The two gates in (8.1) do **not**, by themselves, preserve the maximum
degree cap.  Their exact role is only to make the signed protection term
in the elevated shadow-potential drift summable.  To invoke the shadow
purge telescope one must still supply, separately,

1. the stopped pre-purge centered-collision budget (and its already proved
   deterministic post-purge transfer);
2. the finite-microbite Taylor and realized-center errors at total
   `o(1/r)` scale;
3. the stopped sixth-moment envelope (7.5), the density clock (7.3), and
   the fixed two-shore cap/comparability hypotheses; and
4. the initial small shadow potential and the deterministic purge charge.

With those inputs, (7.8) supplies the missing protection part and the
shadow theorem yields `sum_j E[1_(mathcal G_j)rho_j]=o(1)` and cap failure
probability `o(1)`.  Without them, (8.1) is only a conflict-variance
reduction and must not be advertised as a standalone cap theorem.

There is one important microbite normalization in item 1.  The
post-purge defect transfer, on the fixed `rho<=rho_0<1` stopped event, has
an unnormalized additive charge
`C q rho n z^7`.  At the marking rate (7.1), its contribution to the next
bite is

\[
 {p_j\over nz^6}Cq\rho nz^7
 =O\left({\epsilon_jq\over r}\rho\right)=O(\epsilon_j\rho), \tag{8.2}
\]

because `q=4r` and the shore scales are comparable.  The purge itself
removes `Omega(rho/r)` shadow potential.  Hence (8.2) is absorbable when
`epsilon_j=o(1/r)`, in particular under the stronger Taylor-safe choice
following (7.3).  If one suppresses `epsilon_j` and uses only the coarse
published `O(rho)` version of the transfer, the shadow argument becomes
circular; the linear marking factor must be retained.

The companion verifier

`scratch/verify_gate_a_conflict_variance_reduction_20260822.py`

exhausts small two-shore uniform hypergraphs and checks (2.3), (2.5),
(2.8)--(2.9), (3.4), (4.2)--(4.3), (5.3), (6.5), (6.9), and (6.11), as
well as the rational exponent ledger (7.11), (7.16), and the microstep
cancellation (7.4).  It is a regression
test; every mathematical implication is proved above.
