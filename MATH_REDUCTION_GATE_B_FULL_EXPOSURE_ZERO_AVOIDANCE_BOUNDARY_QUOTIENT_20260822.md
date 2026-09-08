# Gate B: the full-exposure boundary quotient is exactly zero avoidance

**Date:** 2026-08-22

**Status.**  This note gives a nonperturbative all-module reduction for the
actual full-exposure columns.  On the unique-window boundary events, the
degree term and the entire one-blocker term have signed average zero.
Consequently the full-exposure profile is exactly the zero-hit profile.

For every `r>=5` and `2<=j<=r-2`, define the explicit avoidance residual
`rho^(0)_(r,j)` below.  Then

\[
 \boxed{\alpha^{(e)}_{r,j}\ge
 {\rho^{(0)}_{r,j}\over
  b\,k(k-1)\ell(\ell-1)}}.                                  \tag{0.1}
\]

Thus a uniform polynomial lower bound for `rho^(0)` closes the actual
full-exposure Hilbert scalar directly, without comparing `e` to `W_2` and
without a rank assumption.  After retaining the orbit-size factor, the
same result would automatically give a coordinatewise-polynomial inverse
at this fixed shallow rank.

## 1. Exposure and zero avoidance

Put

\[
 b=2r+1,\qquad k=r-2,\qquad \ell=b-k=r+3,
 \qquad X=\{I_r(t),I_{r-1}(t):t\in\mathbb Z_b\},              \tag{1.1}
\]

\[
 A=I_r(0),\qquad B=I_{r-1}(0),\qquad E_0=X-\{A,B\}.          \tag{1.2}
\]

Let `F` range over the complete punctured configuration catalogue.  For a
root `s`-set `S`, `s in {r,r-1}`, put

\[
 t_F=|F\cap E_0|,qquad
 d_s(S)=|\{F:S\in F_s\}|,                                    \tag{1.3}
\]

\[
 e_s(S)=\sum_{F:S\in F_s}(t_F-1)_+,
 \qquad
 Z_s(S)=|\{F:S\in F_s,\ F\cap E_0=\varnothing\}|.           \tag{1.4}
\]

Also define the one-blocker coefficient

\[
 W_{1,s}(S)=\sum_{T\in E_0}\deg(S,T)
            =\sum_{F:S\in F_s}t_F.                           \tag{1.5}
\]

The integer identity `(t-1)_+=t-1+1_(t=0)` gives pointwise

\[
                         \boxed{e_s=W_{1,s}-d_s+Z_s.}         \tag{1.6}
\]

Every rank-`s` target has the same complete-catalogue degree, so `d_s` is
a constant coefficient vector.

Fix `j` ordered distinguished coordinate pairs and use the harmonic lift

\[
 R_x(g)=\sum_{|S|=s}x(S)
 \prod_{i=1}^j
 (\mathbf1_{\{a_i\in gS\}}-\mathbf1_{\{b_i\in gS\}}).       \tag{1.7}
\]

All `L^2(S_b)` norms below use uniform probability measure.

## 2. Boundary events and signed profiles

For `t in Z_b`, put `K_t=I_k(t)`.  Let `B_t` be the event in which pair
one occupies the boundary edge `(t-1,t)`, pair two occupies
`(t+k-1,t+k)`, every remaining pair has one endpoint injectively in
`K_t-{t,t+k-1}` and one injectively in
`K_t^c-{t-1,t+k}`, and every pair may use either orientation.  Its size in
the uniform ordered-injection model is

\[
 |\mathcal B_t|=2^j(k-2)_{j-2}(\ell-2)_{j-2}.                \tag{2.1}
\]

Write `epsilon(z)=H_(k,j)(K_t)`.  The two adjacent boundary pairs make
`K_t` the unique splitting `k`-interval.  No interval of length `r` or
`r-1` splits them both.  Hence on `B_t`,

\[
 q(z)=\varepsilon(z),\qquad c_r(z)=c_{r-1}(z)=0.             \tag{2.2}
\]

For any coefficient vector `x` define its signed boundary profile by

\[
 \omega_x(t)={1\over|\mathcal B_t|}
              \sum_{z\in\mathcal B_t}\varepsilon(z)R_x(z). \tag{2.3}
\]

As in the unique-window proof, if `u_i` is the inside endpoint and `v_i`
the outside endpoint of pair `i`, orientation signs cancel exactly:

\[
 \varepsilon(z)H_{s,j}(gS)
 =\prod_i(\mathbf1_{\{u_i\in gS\}}-
          \mathbf1_{\{v_i\in gS\}}).                        \tag{2.4}
\]

### Lemma 2.1 (one blocker vanishes)

For every central target `T`, every root shore `s`, every `j>=2`, and
every `t`,

\[
 \boxed{\omega_{S\mapsto\deg(S,T)}(t)=0.}                    \tag{2.5}
\]

#### Proof

Fix the positions of all distinguished endpoints.  If the endpoints at
one displayed event edge have the same membership in `T`, transpose those
two positions in the positional root set.  This fixes `T`, so equivariance
preserves `deg(S,T)`; it fixes all other distinguished positions and
reverses exactly one factor in (2.4).  Root sets therefore cancel in
pairs.

A nonzero contribution would require `T` to split both displayed adjacent
edges.  Those would then be the two boundaries of `T`, whose two arc
lengths would have to be `k` and `ell`.  But `|T|` is `r` or `r-1`, neither
`k=r-2` nor `ell=r+3`.  This is impossible. `square`

The harmonic lift of a constant coefficient vector is zero: swapping
`a_1,b_1` pairs the rank-`s` subsets and reverses their harmonic sign.
Summing (2.5) over `T in E_0` and using (1.6) therefore proves the exact
profile identity

\[
                         \boxed{\omega_{e_s}(t)=\omega_{Z_s}(t)}
 \quad(s\in\{r,r-1\},\ t\in\mathbb Z_b).                    \tag{2.6}
\]

This is stronger than merely saying that exposure and avoidance agree
after quotienting by the central span.

## 3. The full-exposure boundary quotient

Put

\[
 z_s(t)=\omega_{Z_s}(t),
 \qquad
 \rho^{(0)}_{r,j}={1\over b}\min_{x,y\in\mathbb R}
 \sum_{t\in\mathbb Z_b}(1-xz_r(t)-yz_{r-1}(t))^2.            \tag{3.1}
\]

Let `alpha^(e)_(r,j)` be the squared angle from the shallow current to the
span of `c_r,c_(r-1),e_r,e_(r-1)`.  The events `B_t` are disjoint because
pair one's unordered adjacent edge determines `t`.  Jensen's inequality,
(2.2), and (2.6) give

\[
 \operatorname {dist}(q,\operatorname {span}
  \{c_r,c_{r-1},e_r,e_{r-1}\})^2
 \ge {b|\mathcal B_t|\over(b)_{2j}}\rho^{(0)}_{r,j}.         \tag{3.2}
\]

For one fixed `k`-set,

\[
 \kappa_{k,j}={2^j(k)_j(\ell)_j\over(b)_{2j}},
 \qquad \|q\|_2^2\le b^2\kappa_{k,j}.                       \tag{3.3}
\]

Divide (3.2) by (3.3).  The factors for the last `j-2` pairs and the
`2^j` orientations cancel, proving (0.1).

The orbit witness also gives

\[
 \Theta_{r,j}\ge
 {N\over b^2k(k-1)\ell(\ell-1)},
 \qquad N={b\choose k}.                                      \tag{3.4}
\]

Consequently

\[
 \boxed{
 \alpha^{(e)}_{r,j}\Theta_{r,j}
 \ge {N\rho^{(0)}_{r,j}
          \over b^3[k(k-1)\ell(\ell-1)]^2}.}                 \tag{3.5}
\]

If `rho^(0)_(r,j)>=r^-C` uniformly, (3.5) has the form
`N r^(-C-11)`.  Since
`dim V_(b-j,j)<=N`, the normalized matrix-coefficient argument then gives
a coordinatewise-polynomial right inverse at rank `k`, in addition to the
Hilbert scalar.

## 4. Exact remaining object

The remaining full-exposure scalar is now a concrete two-profile question:

\[
 \boxed{\inf_{2\le j\le r-2}\rho^{(0)}_{r,j}\ge r^{-C}?}    \tag{4.1}
\]

It is a zero-avoidance partition-function problem for configurations
through a root, evaluated under the explicit signed injection polynomial
of the boundary event.  It is not implied by unsigned second or third
overlap moments.  No `W_2` singular-scale estimate or
rank-two/full-rank assumption is needed if (4.1) is proved directly.

The checker exhausts the complete `r=4` catalogue.  It verifies (1.6)
target by target, verifies that every one-blocker boundary profile is zero,
checks the exact equality of exposure and zero-avoidance profiles, and
finds

\[
 \rho^{(0)}_{4,2}
 ={2565702871466\over20425156452891}
 =0.1256148454\ldots .                                      \tag{4.2}
\]

This finite value is calibration only; it is not used to assert (4.1).
