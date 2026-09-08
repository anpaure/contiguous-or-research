# Gate B: vertical flag concentration and the joint entropy barrier

**Date:** 2026-08-22  
**Status:** unconditional finite reduction.  A fractional cover of mass
`O(x Cat_r)` must put positive mass on rows which are hole-dense at a
positive fraction of all capacity-forcing depths simultaneously.  Under
the usual per-depth `O(xA)` hole upper bound, those rows have uniform-row
probability `O(x)`, so every successful cover law has likelihood ratio
`Omega(1/x)` and relative entropy `Omega(log(1/x))`.  This is necessary,
not a construction of the cover.

## 1. Setup

Fix an integer `r>=2` and put

\[
 b=2r+1,\qquad A={b\choose r},\qquad
 L={b\choose {r-1}}={r\over r+2}A,\qquad B={A\over b}.
\tag{1.1}
\]

Let `P` be a matching of directed punctured rows, and define `x` by

\[
                         2r|P|=(1-x)L.             \tag{1.2}
\]

Assume `0<x<=1`; the zero-residual case needs no cover-down.

At depth `q`, let `H_q^-` and `H_q^+` be the lower and upper tagged hole
sets in ranks `r-q` and `r+1+q`, and put

\[
 B_q={b\choose {r-q}}={b\choose {r+1+q}},\qquad
 \delta_q=[B_q-(1-x)L]_+ .                         \tag{1.3}
\]

Occurrence conservation gives

\[
                 |H_q^-|+|H_q^+|\ge 2\delta_q.    \tag{1.4}
\]

Fix an integer `1<=Q<=r-1`.  Let a nonempty set `H'` be obtained from the tagged union of these hole
sets by omitting `e` exceptional targets.  For a full directed cyclic row
`C`, define

\[
 s_q(C)=\sum_{u\in\mathbb Z_b}
 \left({\bf1}_{I_{r-q}^C(u)\in H'}+
       {\bf1}_{I_{r+1+q}^C(u)\in H'}\right).       \tag{1.5}
\]

Thus `0<=s_q(C)<=2b`.  Let `Omega` be any candidate family of such rows.
A fractional cover of `H'` is a vector `y_C>=0` satisfying

\[
 \sum_{C\in\Omega:T\in C}y_C\ge1\quad(T\in H'),
 \qquad 0<t=\sum_{C\in\Omega}y_C.                  \tag{1.6}
\]

Duplicate labelled copies may be coalesced before applying the statements
below.

## 2. Exact vertical concentration theorem

Define the normalized cover law `mu(C)=y_C/t` and

\[
 z_q(C)={s_q(C)\over2b},\qquad
 \eta={\left[2\sum_{q=1}^Q\delta_q-e\right]_+
             \over 2bQt}.                         \tag{2.1}
\]

### Theorem 2.1

Every fractional cover (1.6) satisfies

\[
 \boxed{\mathbb E_\mu {1\over Q}\sum_{q=1}^Qz_q(C)\ge\eta.}
                                                            \tag{2.2}
\]

For `0<=theta<eta`, put

\[
 R_\theta(C)={1\over Q}
   |\{q:s_q(C)\ge2\theta b\}|,
 \qquad c_\theta={\eta-\theta\over1-\theta}.      \tag{2.3}
\]

Then

\[
 \boxed{\mathbb E_\mu R_\theta\ge c_\theta}       \tag{2.4}
\]

and, for every `0<=rho<c_theta`,

\[
 \boxed{\mu\{C:R_\theta(C)\ge\rho\}
       \ge {c_\theta-\rho\over1-\rho}.}           \tag{2.5}
\]

#### Proof

Reverse the two finite sums in the cover constraints:

\[
 \sum_Cy_C\sum_{q=1}^Qs_q(C)
 =\sum_{T\in H'}\sum_{C:T\in C}y_C
 \ge |H'|
 \ge2\sum_{q=1}^Q\delta_q-e.                      \tag{2.6}
\]

Divide by `2bQt`, using nonnegativity when the last member of (2.6) is
negative; this proves (2.2).  For a fixed row, every depth outside
the set in (2.3) has `z_q<theta`, while every other depth has `z_q<=1`.
Consequently

\[
 {1\over Q}\sum_qz_q(C)
 \le\theta+(1-\theta)R_\theta(C).                 \tag{2.7}
\]

Taking expectations and using (2.2) proves (2.4).  If
`p=mu{R_theta>=rho}`, then `0<=R_theta<=1` gives

\[
 c_\theta\le\mathbb E_\mu R_\theta
 \le \rho(1-p)+p.
\]

Rearrangement proves (2.5).  \(\square\)

The following converse form is often more convenient.  If every candidate
row obeys `R_theta(C)<=rho` and
`theta+(1-theta)rho>0`, then (2.6)--(2.7) give

\[
 \boxed{
 {t\over xB}\ge
 {\left[2\sum_{q\le Q}\delta_q-e\right]_+
  \over2xAQ\{\theta+(1-\theta)\rho\}}.}           \tag{2.8}
\]

Thus a candidate family in which both `theta=o(1)` and `rho=o(1)` cannot
support a cover of mass `O(xB)` in the capacity-forcing range below.

## 3. Capacity-forcing constants

Assume `rx>=64` and

\[
                  Q=\left\lfloor{\sqrt{rx}\over4}\right\rfloor.
                                                            \tag{3.1}
\]

For every `q<=Q`, the elementary product estimate

\[
 {B_q\over L}\ge1-{(q-1)(q+2)\over r}
\]

gives

\[
 \delta_q\ge L\left(x-{(q-1)(q+2)\over r}\right).          \tag{3.2}
\]

The right side is positive: the coarser estimate from `rx>=64` is
`(q-1)(q+2)/r<=x/8`.  More importantly, summation loses only the average
quadratic defect, since

\[
 \sum_{q=1}^Q(q-1)(q+2)={Q(Q-1)(Q+4)\over3}.                \tag{3.3}
\]

Hence, if `K>0` and `t<=KxB`, (2.2) holds with

\[
 \eta\ge\eta_0:={L\over KA}
 \left(1-{(Q-1)(Q+4)\over3rx}\right)
 -{e\over2KxAQ}.                                  \tag{3.4}
\]

Take `theta=eta_0/2`, and put

\[
 c_0={\eta_0\over2-\eta_0},\qquad \rho_0={c_0\over2}.
                                                            \tag{3.5}
\]

Whenever `eta_0>0`, at least `c_0/(2-c_0)` of the cover mass lies on rows
which have at least `rho_0 Q` distinct depths satisfying

\[
                         s_q(C)\ge\eta_0 b.        \tag{3.6}
\]

In the live fixed-power regime `x=r^{-alpha}`, `0<alpha<1/3`, one has
`xQ->infinity` and `Q/sqrt(rx)->1/4`.  Thus, for fixed `K` and
`e=o(A)`, equations (3.4)--(3.6) become

\[
 \eta_0={47\over48K}+o(1),\qquad
 \rho_0={47\over2(96K-47)}+o(1),                 \tag{3.7}
\]

and the cover mass on these vertically rich rows is at least

\[
                         {47\over192K-141}+o(1).   \tag{3.8}
\]

For example, at the sharp constant `K=1`, the symmetric threshold above
puts mass `47/51-o(1)` on rows having at least `47Q/98-o(Q)` depths with
at least `47b/48-o(b)` tagged hole windows.  The free threshold in
Theorem 2.1 gives stronger density if desired: taking `theta=3/4` and
`rho=11/24` puts mass at least `11/13-o(1)` on rows having at least
`11Q/24` depths with at least `3b/2` tagged hole windows.

There is also a sharp first-depth benchmark.  With no depth-one
exceptions, `B_1=L`, so a cover of both depth-one shores has

\[
                         t\ge{xL\over b}={L\over A}xB.       \tag{3.9}
\]

If `epsilon>=0` and `t<=(1+epsilon)xL/b`, then

\[
 \mathbb E_\mu{s_1(C)\over2b}\ge{1\over1+\epsilon}.
                                                            \tag{3.10}
\]

Consequently, for every `a>0`, all but at most
`epsilon/(a(1+epsilon))` of the cover mass lies on rows with
`s_1(C)>=2b(1-a)`.  Near the optimal mass, almost every weighted row is
therefore almost entirely supported on depth-one holes.

## 4. Uniform-row rarity and entropy

Let `U` be the uniform law on all labelled directed cyclic rows.  A fixed
rank-`k` target occurs in a `U`-row with probability

\[
                              {b\over {b\choose k}},          \tag{4.1}
\]

because every row has exactly `b` distinct rank-`k` windows and the action
on targets is transitive.  Suppose, in addition, that for constants
`C_*` and `c_*>0`,

\[
 |H_q^-|+|H_q^+|\le C_*xA,\qquad B_q\ge c_*A
 \quad(1\le q\le Q).                              \tag{4.2}
\]

Then

\[
 \mathbb E_U {1\over Q}\sum_qz_q(C)
 \le {C_*x\over2c_*}.                             \tag{4.3}
\]

If `E_(theta,rho)={C:R_theta(C)>=rho}`, every row in this event has
average normalized score at least `theta rho`; Markov's inequality and
(4.3) give the exact bound

\[
 \boxed{U(E_{\theta,\rho})
       \le {C_*x\over2c_*\theta\rho}.}            \tag{4.4}
\]

Apply this with `theta=eta_0/2` and `rho=rho_0`.  For fixed `K`, the event
has `U`-probability `O(x)` but, by (3.8), positive `mu`-probability.  If
`D=d\mu/dU`, then

\[
 \|D\|_\infty\ge{\mu(E_{\theta,\rho})
                         \over U(E_{\theta,\rho})}
                         =\Omega(1/x).             \tag{4.5}
\]

Cauchy--Schwarz on the same event gives the joint row-collision bound

\[
 \boxed{\mathbb E_U D^2
 \ge {\mu(E_{\theta,\rho})^2\over U(E_{\theta,\rho})}
 =\Omega(1/x).}                                    \tag{4.6}
\]

Binary data processing for relative entropy also gives

\[
 \boxed{D_{\rm KL}(\mu\Vert U)=\Omega(\log(1/x)).} \tag{4.7}
\]

Indeed, if `mu(E)>=d_0>0` and `U(E)<=C_0x`, the two-atom projection has
relative entropy at least
`d_0 log(1/(C_0x))-H_2(d_0)`.

## 5. Consequence for the live Gate B

The required `Omega(1/x)` enrichment is not merely a separate
single-depth effect.  A successful positive cover must create one common
row law with a positive-weight tail of rows that are simultaneously rich
at `Omega(Q)` nested depths.  The zero-avoidance identities and the local,
remote-shore, and Venn-gap estimates control fixed harmonic profiles; by
themselves they do not produce the vertical event (3.6), its positive
mass (3.8), or the entropy accumulation (4.7).

Thus a sufficient next theorem may be stated more concretely as a
**vertical survivor-tail theorem**: construct one positive stopped-bank
law which (i) assigns positive mass to the vertically rich event and (ii)
still gives every nonexceptional hole incidence at least `Omega(1/(xB))`.
Conversely, proving that every legal candidate row is vertically poor in
the sense of (2.8) would rule out the fractional-cover branch and force
continued descent or the long-arc alternative.
