# Gate B: exact first-blocker-cell collision amplification

**Date:** 2026-08-22  
**Status:** unconditional finite identity and bounded-bite pathwise necessary
condition.
This note does not prove the positive Gate-B tail.  It removes a scope gap
between the infinitesimal pair-potential calculation and a finite
isolated-edge bite: every realized bite admits an exact first-blocker-cell
factorization, with no independence, regularity, or small-marking
assumption.  On any trajectory with a fixed whole-bite deletion cap, a
capacity-sized Gate-B survivor floor can occur only if the actual stopped
trajectory accumulates logarithmic mass in one of two explicit nonlinear
statistics.
It does not transfer the complete-state \(O(r^{-2})\) estimate to a finite
stopped bite; instead it names exactly the two stopped statistics that such
a transfer would have to control.

## 1. Catalogue pair mass

Let \(\mathcal C\) be a finite nonempty catalogue of \(Z\) rows.  Every row
has exactly \(b\ge1\) distinct windows in a nonempty target set
\(\mathcal T\) of size \(N\).  For \(T\in\mathcal T\), put

\[
 X(T)=|\{F\in\mathcal C:T\in W(F)\}|,
 \qquad
 c(F,G)=|W(F)\cap W(G)|.                              \tag{1.1}
\]

The ordered pair mass and normalized collision multiplier are

\[
 S=\sum_TX(T)^2=\sum_{F,G\in\mathcal C}c(F,G),
 \qquad
 \mathcal K={NS\over b^2Z^2}.                        \tag{1.2}
\]

For a nonempty deletion cell
\(\varnothing\ne\mathcal B\subsetneq\mathcal C\), define

\[
 m=|\mathcal B|,
 \qquad
 Y(T)=|\{F\in\mathcal B:T\in W(F)\}|,               \tag{1.3}
\]

\[
 R_{\mathcal B}=\sum_TX(T)Y(T),
 \qquad
 Q_{\mathcal B}=\sum_TY(T)^2.                        \tag{1.4}
\]

Use the three dimensionless cell statistics

\[
 u={m\over Z},\qquad
 \omega={R_{\mathcal B}\over S},\qquad
 \chi={Q_{\mathcal B}\over S}.                      \tag{1.5}
\]

Because \(\mathcal B\ne\mathcal C\), one has \(0\le u<1\), and the
remaining catalogue is nonempty.

## 2. Exact nonlinear one-cell identity

### Theorem 2.1 (first-blocker-cell factor)

Delete \(\mathcal B\), and let \(Z',S',\mathcal K'\) denote the resulting
quantities.  Then

\[
 \boxed{
 {\mathcal K'\over\mathcal K}
 =1+{\chi+2(u-\omega)-u^2\over(1-u)^2}.}             \tag{2.1}
\]

In particular, the cell increases the collision multiplier exactly when

\[
 \boxed{\chi+2(u-\omega)>u^2.}                       \tag{2.2}
\]

The two positive mechanisms in (2.1) have literal pair interpretations.
Put

\[
 W_F=\sum_{T\in W(F)}X(T).
\]

Then

\[
 R_{\mathcal B}=\sum_{F\in\mathcal B}W_F,
 \qquad
 Q_{\mathcal B}=\sum_{F,G\in\mathcal B}c(F,G),      \tag{2.3}
\]

and

\[
 u-\omega
 =u\left(1-{\operatorname {avg}_{F\in\mathcal B}W_F
                    \over\operatorname {avg}_{F\in\mathcal C}W_F}
       \right).                                      \tag{2.4}
\]

Thus \(\chi\) is the within-cell shallow pair mass, while
\((u-\omega)_+\) records deletion biased toward rows carrying below-average
shallow pair-endpoint mass.

#### Proof

After deletion, \(X'(T)=X(T)-Y(T)\), and hence

\[
 S'=\sum_T(X(T)-Y(T))^2
   =S-2R_{\mathcal B}+Q_{\mathcal B}
   =S(1-2\omega+\chi).                               \tag{2.5}
\]

Also \(Z'=Z(1-u)\).  Substitution in (1.2) gives

\[
 {\mathcal K'\over\mathcal K}
 ={1-2\omega+\chi\over(1-u)^2}.
\]

Subtract \((1-u)^2=1-2u+u^2\) from the numerator to obtain
(2.1), and (2.2) follows because the denominator is positive.

For (2.3), interchange the sums over \(T\) and rows.  Finally
\(\sum_FW_F=S\), so

\[
 \omega={m\over Z}
 {R_{\mathcal B}/m\over S/Z},
\]

which is (2.4). \(\square\)

The term \(-u^2\) is material: when \(\omega=u\), the cell amplifies
\(\mathcal K\) only if \(\chi>u^2\).  It must not be dropped when a finite
bite has \(u=\Theta(1)\).

There is an equivalent escort form which is useful for comparison with the
stopped Palm dynamics.  Define

\[
 \pi(T)={X(T)\over bZ},\qquad
 \rho(T)={X(T)^2\over S},\qquad
 y(T)=\begin{cases}Y(T)/X(T),&X(T)>0,\\0,&X(T)=0.
       \end{cases}                                  \tag{2.6}
\]

Then \(\pi\) and \(\rho\) are probability laws and direct summation gives

\[
 u=\mathbb E_\pi y,\qquad
 \omega=\mathbb E_\rho y,\qquad
 \chi=\mathbb E_\rho y^2,\qquad
 \pi'(T)=\pi(T){1-y(T)\over1-u}.                   \tag{2.7}
\]

Consequently

\[
 {\mathcal K'\over\mathcal K}
 =\mathbb E_\rho\left({1-y\over1-u}\right)^2.       \tag{2.8}
\]

If \(L(T)=N\pi(T)\), then

\[
 \boxed{\omega-u={\operatorname {Cov}_\pi(L,y)\over\mathcal K}.} \tag{2.9}
\]

Indeed \(\rho=\pi L/\mathcal K\) and
\(\mathbb E_\pi L=\mathcal K\).  Hence the positive term
\((u-\omega)_+\) is exactly a rich-get-richer effect: targets already
carrying large Palm mass receive a smaller deletion fraction.

Thus (2.1) is the exact finite-cell version of the escort collision
transport identity; (2.3)--(2.4) additionally identify its two terms as
literal row-pair statistics.

## 3. Pathwise logarithmic gate

Consider an arbitrary nested deletion sequence

\[
 \mathcal C_0\supset\mathcal C_1\supset\cdots
 \supset\mathcal C_t\ne\varnothing,                 \tag{3.1}
\]

where \(\mathcal C_{i+1}=\mathcal C_i-\mathcal B_i\).  Compute
\(u_i,\omega_i,\chi_i\) in the current catalogue \(\mathcal C_i\), and
write \(\mathcal K_i\) for its collision multiplier.

### Theorem 3.1 (finite adaptive-amplification budget)

The exact product formula is

\[
 \boxed{
 {\mathcal K_t\over\mathcal K_0}
 =\prod_{i<t}
 \left(1+{\chi_i+2(u_i-\omega_i)-u_i^2
                  \over(1-u_i)^2}\right).}          \tag{3.2}
\]

If \(u_i\le\varepsilon<1\) for every cell, then

\[
 \boxed{
 \log {\mathcal K_t\over\mathcal K_0}
 \le {1\over(1-\varepsilon)^2}
 \sum_{i<t}\left\{\chi_i+2(u_i-\omega_i)_+\right\}.} \tag{3.3}
\]

Consequently, whenever \(\mathcal K_t\ge c/x\) and
\(\mathcal K_0=1\),

\[
 \boxed{
 \sum_{i<t}\left\{\chi_i+2(u_i-\omega_i)_+\right\}
 \ge(1-\varepsilon)^2
       \left(\log{1\over x}+\log c\right).}         \tag{3.4}
\]

In particular at least one of

\[
 \sum_{i<t}\chi_i,
 \qquad
 2\sum_{i<t}(u_i-\omega_i)_+                        \tag{3.5}
\]

is at least one half of the right side of (3.4).

#### Proof

Iterating Theorem 2.1 proves (3.2).  Let the fraction in its \(i\)-th
factor be \(g_i\).  It is greater than \(-1\), because both collision
multipliers are positive.  If \(g_i\le0\), then
\(\log(1+g_i)\le0\).  If \(g_i>0\), then

\[
 \log(1+g_i)\le g_i
 \le {\chi_i+2(u_i-\omega_i)_+\over(1-u_i)^2}
 \le {\chi_i+2(u_i-\omega_i)_+\over(1-\varepsilon)^2}. \tag{3.6}
\]

Sum (3.6) to obtain (3.3).  Substitution of
\(\mathcal K_t\ge c/x\), followed by the pigeonhole principle, proves
(3.4)--(3.5). \(\square\)

## 4. Application to an isolated-edge bite

Give the accepted rows in one realized isolated-edge bite any deterministic
order \(H_1,\ldots,H_s\), and let \(\Gamma[H]\) denote the closed conflict
neighbourhood.  Define the first-blocker cells

\[
 \mathcal B_i=\Gamma[H_i]-\bigcup_{a<i}\Gamma[H_a]. \tag{4.1}
\]

The cells are disjoint and their union is exactly the deleted catalogue.
Accepted rows are pairwise nonconflicting.  Hence \(H_i\) survives the
earlier cells, and its closed neighbourhood in the catalogue remaining
before cell \(i\) is exactly \(\mathcal B_i\).  Applying the cells
successively is therefore the literal realized bite, so (2.1) and (3.2)
apply without replacing the accepted set by independent blockers.

There is no denominator loss when a whole-bite bound is converted to
cellwise bounds, provided the unused deletion budget is retained.  Suppose
the whole bite deletes at most a \(\delta\)-fraction of its starting
catalogue, where \(0\le\delta<1\).  If \(Z_0\) is the starting size,
\(P_i\) rows were deleted before cell \(i\), and that cell has size \(m_i\),
then \(P_i+m_i\le\delta Z_0\).  Hence

\[
 u_i={m_i\over Z_0-P_i}
 \le{\delta Z_0-P_i\over Z_0-P_i}
 \le\delta.                                         \tag{4.2}
\]

Thus Theorem 3.1 applies with \(\varepsilon=\delta\).
For the good-trajectory bite bound \(\delta\le1/8\), this gives

\[
 u_i\le {1\over8},\qquad
 \log {\mathcal K_{\rm out}\over\mathcal K_{\rm in}}
 \le {64\over49}\sum_{i\text{ in bite}}
       \{\chi_i+2(u_i-\omega_i)_+\}.               \tag{4.3}
\]

For a full neighbourhood cell one has

\[
 Q_{\Gamma[H]}
 =\sum_T|\Gamma[H]\cap\mathcal S(T)|^2,             \tag{4.4}
\]

where \(\mathcal S(T)\) is the current external star of \(T\).  A
first-blocker cell is a subset of \(\Gamma[H]\), so its raw
\(Q\)-mass is no larger than (4.4).  At the complete punctured catalogue,
summing (4.4) over \(H\), normalizing by \(S\), and using target
transitivity gives exactly the complete-state common-blocker scalar
\(I_q\).  This explains why the complete-state tangent sees
\(pI_q=O(r^{-2})\), while (3.3) identifies the additional nonlinear
statistics which still require control after adaptive stopping.

## 5. Exact remaining Gate-B interface

For clarity, the collision forcing used here is elementary.  If
\(g\ge c_0xA\) targets satisfy
\(\pi_t(T)\ge1/(K_{\rm cov}xA)\), and \(N/A\ge c_1>0\), then

\[
 \mathcal K_t=N\sum_T\pi_t(T)^2
 \ge {Ng\over K_{\rm cov}^2x^2A^2}
 \ge {c_0c_1\over K_{\rm cov}^2x}.                 \tag{5.1}
\]

Thus the capacity-sized survivor floor forces
\(\mathcal K_t=\Omega(1/x)\).  On any realized stopped trajectory whose
whole bites each delete at most one eighth of their bite-start catalogue,
(4.2) permits \(\varepsilon=1/8\) in (3.4).  Thus, without any independence
or regularity assumption, that trajectory obeys the pathwise dichotomy:

1. **cell collision:** first-blocker cells accumulate
   \(\Omega(\log(1/x))\) normalized shallow pair mass \(\sum\chi_i\); or
2. **nonregular deletion bias:** cells repeatedly delete below-average
   pair endpoints, with
   \(\sum(u_i-\omega_i)_+=\Omega(\log(1/x))\).

This is strictly stronger than an infinitesimal complete-state calculation
and does not assert that either alternative occurs.  To prove the positive
Gate-B tail one must still align the resulting collision mass with terminal
holes.  Conversely, an \(o(\log(1/x))\) stopped upper bound for both sums
would rigorously rule out the full-survivor route and force the
hole-dependent or long-flag-arc alternative.

The finite identities and inequalities are independently checked by
`scratch/verify_gate_b_first_blocker_cell_collision_dichotomy_20260822.py`.
