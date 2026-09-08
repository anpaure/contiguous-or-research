# Independent audit: canonical MSW degree-two cube energy

Date: 2026-07-25

Method: pure mathematics only. No finite search, computation, solver, web
search, or literature search is used.

## 0. Verdict

The exact fractional-rounding and one-flip local-descent theorem for the
canonical MSW degree-two cube is correct, including every factor of two.
With the doubled floor energy used below, the rounding toll is \(D_H/4\)
and the local-minimum gap is \(D_H\).  In the older half-energy
normalization, the two tolls are \(D_H/8\) and \(D_H/2\).

The remaining assertion \(\mathrm{FCE}_A\), an \(O(H\operatorname{Cat}_m)\)
upper bound for the fractional cube minimum, is sufficient for fixed-window
overload MWB and hence for the constant-one theorem.  It is unproved.

There is also an exact necessary condition which exposes the present
obstruction.  The entire degree-two cube changes only
\(4\operatorname{Cat}_{m-2}\) first-shadow target coordinates and at most
\(8\operatorname{Cat}_{m-2}\) target coordinates at any other depth.
Consequently \(\mathrm{FCE}_A\) forces the unchanged canonical MSW factor
itself to have only \(O_A(W/\sqrt m)\) missing first-shadow targets.  Thus
the cube cannot repair a macroscopic canonical first-shadow defect.  No
pure-mathematical lower bound contradicting this necessary condition is
currently proved.

## 1. Normalization

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=\operatorname{Cat}_m=\frac Wn,
\]

and, for \(1\le q\le H\le m-2\),

\[
 N_q=\binom n{m-q},\qquad
 W=c_qN_q+r_q,\qquad 0\le r_q<N_q.
\tag{1.1}
\]

For a real cyclic-order vector \(x\) of total column mass \(B\), let

\[
 \mu_q(x)=B_{m-q}x,
 \qquad a_q=\frac W{N_q},
 \qquad f_q(x)=\mu_q(x)-a_q\mathbf1.
\tag{1.2}
\]

Define

\[
 \beta_q=\frac{r_q(N_q-r_q)}{N_q}
\tag{1.3}
\]

and the doubled floor-corrected energy

\[
 \widetilde Q_q(x)
 =\sum_S(\mu_q(x,S)-c_q)(\mu_q(x,S)-c_q-1).
\tag{1.4}
\]

### Lemma 1.1 (exact centered form)

For every real \(x\) of the indicated total mass,

\[
 \boxed{
 \widetilde Q_q(x)=\|f_q(x)\|_2^2-\beta_q.}
\tag{1.5}
\]

If \(x=\mathbf1_F\) is an exact factor, then
\(Q_q(F):=\widetilde Q_q(\mathbf1_F)\) is a nonnegative integer, and it
vanishes exactly when every load is \(c_q\) or \(c_q+1\).

#### Proof

Write \(\theta=r_q/N_q\), so \(a_q=c_q+\theta\).  Since
\(\sum_S(\mu_q(S)-a_q)=0\), expansion gives

\[
\begin{aligned}
\sum_S(\mu_q-c_q)(\mu_q-c_q-1)
&=\sum_S(\mu_q-a_q)^2+N_q\theta(\theta-1)\\
&=\|f_q\|_2^2-\frac{r_q(N_q-r_q)}{N_q}.
\end{aligned}
\]

For integral loads, every scalar \((u-c_q)(u-c_q-1)\) is nonnegative
and vanishes precisely at the two consecutive integers \(c_q,c_q+1\).
\(\square\)

Put

\[
 \widetilde Q_H(x)=\sum_{q=1}^H\frac{\widetilde Q_q(x)}{c_q},
 \qquad Q_H(F)=\widetilde Q_H(\mathbf1_F),
 \qquad \Psi_H=\frac12Q_H.
\tag{1.6}
\]

For tuples of centered load vectors use the Hilbert product

\[
 \langle u,v\rangle_H
 =\sum_{q=1}^H\frac{\langle u_q,v_q\rangle}{c_q}.
\tag{1.7}
\]

## 2. The exact degree-two profiles

Let \(F_m\) be the canonical MSW exact factor and
\(\tau=(2\ 3)\).  The established component hierarchy gives

\[
 d=\operatorname{Cat}_{m-2}
\tag{2.1}
\]

independent \(j=0\) ownership components.  Their two sides each contain
two wreaths.  Orient the corresponding actual degree-two trades from the
\(F_m\)-side to the \(\tau F_m\)-side and call them \(g_R\),
\(R\in\mathcal D_{m-2}\).

The established universal four-letter profile says that, for each \(R\),

\[
 \|B_{m-1}g_R\|_2^2=4,
 \qquad
 \|B_{m-q}g_R\|_2^2=8\quad(2\le q\le H).
\tag{2.2}
\]

For completeness, in the universal notation with exceptional labels
\(\alpha,\beta,\gamma,\delta\), disjoint ordered lists \(E,O\), and

\[
 \partial K=e_{K\cup\{\gamma\}}-e_{K\cup\{\beta\}},
\]

one has, for \(2\le r\le m-1\),

\[
B_rg_R=
 \partial\operatorname{suf}_{r-1}O
 +\partial\operatorname{suf}_{r-1}E
 -\partial\operatorname{pre}_{r-1}E
 -\partial\operatorname{pre}_{r-1}O.
\tag{2.3}
\]

For \(2\le r\le m-2\), the four cores in (2.3) are distinct, giving
eight distinct coefficients of magnitude one.  At \(r=m-1\), the two
\(O\)-terms cancel and the remaining rectangle has four distinct
coefficients of magnitude one.  This proves (2.2).  No disjointness is
asserted between the profiles of different \(R\)'s.

Define

\[
 \alpha_H
 =\frac4{c_1}+8\sum_{q=2}^H\frac1{c_q},
 \qquad D_H=d\alpha_H.
\tag{2.4}
\]

Since \(c_q\ge1\),

\[
 \boxed{
 D_H\le(8H-4)\operatorname{Cat}_{m-2}
 =O(H\operatorname{Cat}_m).}
\tag{2.5}
\]

## 3. Exact fractional cube and Bernoulli rounding

For \(t=(t_R)_R\in[0,1]^d\), put

\[
 x(t)=\mathbf1_{F_m}+\sum_Rt_Rg_R.
\tag{3.1}
\]

The component column supports are disjoint.  On a component, (3.1) puts
coefficient \(1-t_R\) on its old side and \(t_R\) on its new side.
Therefore

\[
 x(t)\ge0,
 \qquad B_mx(t)=\mathbf1,
 \qquad \sum_Cx(t)_C=B.
\tag{3.2}
\]

If \(X_R\) are independent Bernoulli variables with
\(\mathbb P(X_R=1)=t_R\), then

\[
 F_X=F_m+\sum_RX_Rg_R
\tag{3.3}
\]

is a genuine exact factor for every outcome.

### Theorem 3.1 (lossless rounding identity)

For every \(t\in[0,1]^d\),

\[
 \boxed{
 \mathbb E Q_H(F_X)
 =\widetilde Q_H(x(t))
 +\alpha_H\sum_Rt_R(1-t_R).}
\tag{3.4}
\]

Consequently some exact cube vertex satisfies

\[
 \boxed{
 Q_H(F_X)\le\widetilde Q_H(x(t))+\frac{D_H}{4}.}
\tag{3.5}
\]

Equivalently, in the half-energy normalization,

\[
 \Psi_H(F_X)\le\widetilde\Psi_H(x(t))+\frac{D_H}{8}.
\tag{3.6}
\]

#### Proof

At depth \(q\), write \(\Delta_{q,R}=B_{m-q}g_R\).  Independence and
centering of \(X_R-t_R\) give

\[
\mathbb E\left\|
 f_q(x(t))+\sum_R(X_R-t_R)\Delta_{q,R}
\right\|_2^2
=\|f_q(x(t))\|_2^2
\sum_Rt_R(1-t_R)\|\Delta_{q,R}\|_2^2.
\]

Sum with weights \(1/c_q\), subtract the fixed \(\beta_q/c_q\), and use
(2.2).  This proves (3.4).  Since \(t_R(1-t_R)\le1/4\), the expectation is
at most the right side of (3.5), and some outcome is at most its
expectation. \(\square\)

Cross terms between distinct \(g_R\)'s are unrestricted.  They disappear
from the variance solely because the Bernoulli variables are independent;
no false orthogonality assumption is being used.

## 4. Exact local-descent theorem

At an arbitrary cube vertex \(F\), orient \(h_R\) to be the applicable
flip away from the current side of component \(R\).  Thus
\(h_R\in\{g_R,-g_R\}\), and all independent combinations of these outward
flips are exact cube vertices.

### Theorem 4.1 (one-flip local-minimum gap)

If no applicable coordinate flip strictly decreases \(Q_H\) at \(F\),
then

\[
 \boxed{
 Q_H(F)\le
 \min_{t\in[0,1]^d}
 \widetilde Q_H\left(\mathbf1_F+\sum_Rt_Rh_R\right)
 +D_H.}
\tag{4.1}
\]

The fractional set on the right is the same whole cube as (3.1).
Equivalently,

\[
 \Psi_H(F)\le\min\widetilde\Psi_H+\frac{D_H}{2}.
\tag{4.2}
\]

If the reverse strict inequality to (4.1) holds at a vertex, an applicable
degree-two flip strictly decreases the energy.

#### Proof

Let \(f=(f_q(F))_{q\le H}\) and let \(\delta_R\) be the corresponding
tuple of load effects of \(h_R\).  The exact quadratic increment is

\[
 Q_H(F+h_R)-Q_H(F)
 =2\langle f,\delta_R\rangle_H+\|\delta_R\|_H^2
 =2\langle f,\delta_R\rangle_H+\alpha_H.
\tag{4.3}
\]

Local minimality therefore gives

\[
                2\langle f,\delta_R\rangle_H\ge-\alpha_H
\tag{4.4}
\]

for every \(R\).  For arbitrary \(t\in[0,1]^d\),

\[
\begin{aligned}
&\widetilde Q_H\left(\mathbf1_F+\sum_Rt_Rh_R\right)-Q_H(F)\\
&\qquad=
2\sum_Rt_R\langle f,\delta_R\rangle_H
+\left\|\sum_Rt_R\delta_R\right\|_H^2\\
&\qquad\ge-\alpha_H\sum_Rt_R\ge-D_H.
\end{aligned}
\tag{4.5}
\]

The squared norm, which contains every cross term, is retained as one
nonnegative quantity.  Taking the minimum proves (4.1). \(\square\)

Finite strict descent on the cube terminates at such a local minimum, but
(4.1) is useful at the constant-one scale only if the fractional minimum
itself is controlled.

## 5. The precise sufficient fractional theorem

For \(H_A=\lceil A\sqrt m\rceil\), consider:

### \(\mathrm{FCE}_A\) — UNPROVED

For every fixed \(A>0\), there is \(C_A<\infty\) such that

\[
 \boxed{
 \min_{t\in[0,1]^d}\widetilde Q_{H_A}(x(t))
 \le C_AH_A\operatorname{Cat}_m.}
\tag{5.1}
\]

### Theorem 5.1 (\(\mathrm{FCE}_A\) implies constant one)

If \(\mathrm{FCE}_A\) holds for every fixed \(A\), then the fixed-window
overload form of MWB holds, and hence

\[
                    \nu(k)\le(1+o(1))W(k).
\tag{5.2}
\]

#### Proof

Apply Theorem 3.1 to a fractional minimizer.  It gives an exact factor
\(F_A\) with

\[
 Q_{H_A}(F_A)
 \le C_AH_AB+\frac{D_{H_A}}4
 =O_A(H_AB).
\tag{5.3}
\]

For an integer load vector, the audited floor-overload inequality in the
present doubled normalization is

\[
                  2O_q(F_A)\le Q_q(F_A).
\tag{5.4}
\]

Therefore

\[
 \sum_{q\le H_A}\frac{O_q(F_A)}{c_q}
 \le\frac12Q_{H_A}(F_A)
 =O_A(H_AB)=o(W),
\tag{5.5}
\]

because

\[
 \frac{H_AB}{W}=\frac{H_A}{n}=O_A(m^{-1/2}).
\]

This is exactly the fixed-window overload statement for every fixed \(A\).
The audited diagonal equivalence gives overload MWB, and the simultaneous
integral deletion-flow reduction then gives (5.2).  This conclusion is
unlabelled overload MWB; it does not assert the stronger labelled
common-owner theorem. \(\square\)

The local-descent theorem gives the same conclusion under (5.1), with the
larger but still scale-correct additive toll \(D_H\).

## 6. Exact fixed-shadow obstruction to \(\mathrm{FCE}_A\)

Let

\[
 M_q=\#\left\{S\in\binom{[n]}{m-q}:
          \mu_q(F_m,S)=0\right\}
\tag{6.1}
\]

be the number of depth-\(q\) targets missed by the unchanged canonical MSW
factor.  Put

\[
 s_1=4,\qquad s_q=8\quad(q\ge2).
\tag{6.2}
\]

### Theorem 6.1 (the degree-two cube cannot repair a large missing shadow)

Every exact vertex \(F_X\) of the degree-two cube satisfies

\[
 \boxed{
 Q_H(F_X)\ge
 L_H:=\sum_{q=1}^H(c_q+1)(M_q-s_qd)_+.}
\tag{6.3}
\]

Every fractional cube point satisfies

\[
 \boxed{
 \widetilde Q_H(x(t))\ge L_H-\frac{D_H}{4}.}
\tag{6.4}
\]

Consequently \(\mathrm{FCE}_A\) requires

\[
 \boxed{
 \sum_{q=1}^{H_A}(c_q+1)(M_q-s_qd)_+
 \le C_AH_AB+\frac{D_{H_A}}4
 =O_A(H_AB).}
\tag{6.5}
\]

In particular, because \(c_1=1\),

\[
 \boxed{
 M_1\le4\operatorname{Cat}_{m-2}
 +\frac{C_AH_A\operatorname{Cat}_m}{2}
 +\frac{D_{H_A}}8
 =O_A\left(\frac W{\sqrt m}\right).}
\tag{6.6}
\]

#### Proof

Let

\[
 U_q=\bigcup_R\operatorname{supp}(B_{m-q}g_R).
\]

Equation (2.2), together with the fact that every nonzero profile
coefficient has magnitude one, gives

\[
                         |U_q|\le s_qd.
\tag{6.7}
\]

If \(S\notin U_q\), its load is unchanged throughout the whole real cube.
Thus every canonical missing target outside \(U_q\) is still missing at
every exact cube vertex.  There are at least \((M_q-s_qd)_+\) such targets.
At load zero, the depth-\(q\) summand in \(Q_q/c_q\) is

\[
 \frac{(0-c_q)(0-c_q-1)}{c_q}=c_q+1.
\]

All other integral summands are nonnegative, proving (6.3).

For a fractional point, use its Bernoulli rounding from Theorem 3.1.  Every
outcome obeys (6.3), so

\[
 L_H\le\mathbb EQ_H(F_X)
 =\widetilde Q_H(x(t))
  +\alpha_H\sum_Rt_R(1-t_R)
 \le\widetilde Q_H(x(t))+\frac{D_H}{4}.
\]

This proves (6.4).  Combining (6.4) with (5.1) gives (6.5).  Keeping only
the \(q=1\) term in (6.5) gives (6.6). \(\square\)

Theorem 6.1 is an actual-factor obstruction, not an abstract Gram-model
warning.  It says that this degree-two cube has only \(O(B)\) mutable target
coordinates per depth.  Therefore its scale-correct rounding theorem does
not by itself provide the required bulk correction.  Proving
\(M_1\gg B\sqrt m\), or the corresponding weighted multidepth violation of
(6.5), would refute \(\mathrm{FCE}_A\).  No such pure-mathematical estimate
is established here.

## 7. Adversarial audit

1. **The energy is doubled.**  The nonnegative integer energy in (1.4) is
   twice the older \(\frac12(u-c)(u-c-1)\) convention.  This accounts for
   every factor of two in Sections 3--5.

2. **Fractional energy may be negative.**  This is harmless.  The exact
   Bernoulli identity, not pointwise nonnegativity, supplies the rounding
   bound.

3. **No cross-profile orthogonality.**  Profiles for distinct components
   may overlap.  Independence proves Theorem 3.1; the full squared norm in
   (4.5) proves Theorem 4.1.

4. **Every rounded point is physical.**  Independent component choices are
   genuine exact factors by the ownership-cube theorem.  No signed or
   fractional endpoint is passed off as an exact factor.

5. **The sufficient conclusion is unlabelled.**  Small overload in each
   fixed window is the audited equivalent form of overload MWB.  It does
   not produce the stronger common labelled owner flow.

6. **The shadow condition is necessary, not yet contradictory.**  Equation
   (6.6) does not prove that the canonical first shadow violates the needed
   bound.  It identifies the additional canonical-shadow theorem which
   \(\mathrm{FCE}_A\) silently contains.
