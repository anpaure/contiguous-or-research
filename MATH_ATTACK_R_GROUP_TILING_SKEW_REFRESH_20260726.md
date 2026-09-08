# Skew-refresh rainbow-tile factors in the hypercube

## 1. Setup

Let (Q_h) have coordinate set (J), where (h) is a power of two.
An isometric (2h)-cycle has a first-half cyclic direction order
(pi), and a set (S\subseteq J), (1\leq |S|<h), is the direction
set of a consecutive segment if and only if it is a cyclic interval of
(pi).  For an isometric cycle factor (mathcal F), write

\[
 A_{mathcal F}(S)
 =\#\{C\in\mathcal F:S\text{ is a cyclic interval of }\pi_C\}.
\]

Put

\[
 N_h=\frac{2^{h-1}}h,
 \qquad
 U_h(q)=\frac{2^{h-1}}{\binom hq}
 \quad(1\le q<h).
\]

The quotient-tile formulation says that the factor is a literal tiling
of (mathbb F_2^h/\langle\mathbf1\rangle) by translated prefix-path
tiles.  All constructions below are integral tilings; no fractional
matching is used.

## 2. Fibrewise arbitrary-merge lemma

Let (L,R) be disjoint (d)-sets, with (d) a power of two.  Let
(mathcal F_R) be any isometric (2d)-cycle factor of (Q_R).  For
each **individual oriented cycle** (D\inmathcal F_R), choose an
isometric factor (mathcal H_D) of (Q_L).  These factors may depend
arbitrarily on (D).  For every (C\inmathcal H_D), choose a balanced
word

\[
 \sigma_{C,D}\in\{L,R\}^{2d},
 \qquad |\sigma_{C,D}|_L=|\sigma_{C,D}|_R=d,
\]

and a phase (	heta_{C,D}\in\mathbb Z_{2d}), and use the
arbitrary-merge torus factor on (V(C)\times V(D)).

### Lemma 2.1 (skew product is exact)

The union of all these torus factors is an isometric (4d)-cycle
factor of (Q_{L\sqcup R}).

### Proof

The right cycles (D) partition (V(Q_R)).  For a fixed (D), the
cycles (C\inmathcal H_D) partition (V(Q_L)).  Hence the products

\[
 V(C)\times V(D),
 \qquad D\inmathcal F_R,quad C\inmathcal H_D,
\]

are disjoint and partition (V(Q_{L\sqcup R})).  The arbitrary-merge
torus theorem partitions each such product into (d) isometric
(4d)-cycles.  Therefore their union is the claimed exact factor.
(square)

This differs essentially from a fixed product hierarchy: the complete
left factor, and in particular its direction order, is refreshed
separately over every right-cycle fibre.

## 3. One-step ledger

For every cyclic order (pi) of (L), there is an exact factor of
(Q_L) all of whose cycles have order (pi): coordinate-conjugate the
standard Hamming-code factor.  In Lemma 2.1, choose independently for
each (D) a uniform cyclic order (pi_D), and take this fixed-order
factor as (mathcal H_D).  Independently in every product torus, choose
(sigma_{C,D}) uniformly among balanced words and choose
(	heta_{C,D}) uniformly in (mathbb Z_{2d}).

Fix (S=S_L\sqcup S_R), and put

\[
 a=|S_L|,qquad b=|S_R|,qquad q=a+b.
\]

Assume (q<d).  Let

\[
 m=A_{mathcal F_R}(S_R).
\]

If (a>0), let (X_S) be the number of cycles (D) counted by (m)
for which (S_L) is an interval of (pi_D).  Then

\[
 X_S\sim\operatorname {Bin}\left(m,p_a\right),
 \qquad p_a=\frac d{\binom da}.                       \tag{3.1}
\]

For (a=0), put (X_S=m).  Conditional on all orders (pi_D), the
expected output count is

\[
 \mathbb E\bigl[A_{m out}(S)\mid(\pi_D)\bigr]
 =\kappa_{a,b}N_dX_S,                                \tag{3.2}
\]

where, when (a,b>0),

\[
 \kappa_{a,b}
 =\frac{2\binom da\binom db}{\binom{2d}{a+b}},       \tag{3.3}
\]

and, when exactly one of (a,b) is zero and the other is positive,

\[
 \kappa_{a,0}=\frac{2d\binom da}{\binom{2d}a},
 \qquad
 \kappa_{0,b}=\frac{2d\binom db}{\binom{2d}b}.       \tag{3.4}
\]

Indeed, (3.1) is the exact probability that a fixed (a)-set is a
cyclic interval in a uniform cyclic order.  Equations (3.2)--(3.4) are
the arbitrary-merge amplification formula, summed over the (N_d)
left cycles above each good right cycle.  Equivalently, for one good
product torus the expected number of output cycles containing (S) is
(kappa_{a,b}).

For (a,b>0), averaging also over the orders gives the exact identity

\[
 \mathbb E A_{m out}(S)
 =\frac{2^d\binom db}{\binom{2d}{a+b}}
 A_{mathcal F_R}(S_R).                              \tag{3.5}
\]

The same identity holds for (a=0<b).  If (b=0<a), then instead

\[
 \mathbb E A_{m out}(S)
 =\frac{2^{2d-1}}{\binom{2d}a}=U_{2d}(a),            \tag{3.6}
\]

independently of the right factor.  Consequently, if (b>0) and

\[
 A_{mathcal F_R}(S_R)\ge c,U_d(b),                 \tag{3.7}
\]

then

\[
 \mathbb E A_{m out}(S)\ge c,U_{2d}(q).           \tag{3.8}
\]

Thus the refresh is quota-neutral: it transports a lower uniform quota
on the inherited right restriction to the same lower uniform quota in
the doubled cube.

## 4. Simultaneous integral refresh

Fix (C>0).  For a factor on (Q_d), suppose a family
(mathscr A_d) of subsets has

\[
 A_{mathcal F_d}(B)\ge c_d U_d(|B|)
 \quad\text{for every nonempty }B\inmathscr A_d,    \tag{4.1}
\]

and every (B\inmathscr A_d) has (|B|\le C\sqrt d).
Define

\[
 \mathscr A_{2d}
 =\left\{A\sqcup B:
 B\inmathscr A_d\cup\{\varnothing\},
 |A|\le C\sqrt d, |B|\le C\sqrt d,
 A\sqcup B\ne\varnothing\right\}.                 \tag{4.2}
\]

### Lemma 4.1 (simultaneous refresh)

There is (d_*(C)) such that, whenever (d\ge d_*(C)) is a power of
two and (c_d\ge c_*>0), one can make all choices in the skew product
so that

\[
 A_{mathcal F_{2d}}(S)
 \ge c_d(1-\varepsilon_d)^2U_{2d}(|S|)
 \quad(S\inmathscr A_{2d}),                        \tag{4.3}
\]

where

\[
 \varepsilon_d=2^{-d/10}.                           \tag{4.4}
\]

### Proof

Increase (d_*(C)) so that (2C\sqrt d<d).  Hence the formulas in
Section 3 apply to every set in (4.2).

First expose the independent orders (pi_D).  For (a>0,b>0), the
mean in (3.1), using (4.1), obeys

\[
 \lambda_S
 \ge c_*\frac{2^{d-1}d}
 {\binom da\binom db}
 \ge c_*,2^{d-1}d^{,1-2C\sqrt d}.                 \tag{4.5}
\]

For (a>0,b=0), the same argument gives

\[
 \lambda_S=N_dp_a
 =\frac{2^{d-1}}{\binom da}
 \ge 2^{d-1}d^{-C\sqrt d}.                          \tag{4.6}
\]

Both lower bounds are (2^{d-o(d)}).  Chernoff's inequality gives

\[
 \Pr\bigl(X_S<(1-\varepsilon_d)\lambda_S\bigr)
 \le\exp\left(-\frac{\varepsilon_d^2\lambda_S}{2}\right).
                                                               \tag{4.7}
\]

The exponent in (4.7) is (2^{(4/5)d-o(d)}).  There are fewer than
(2^{2d}) possible (S).  A union bound therefore shows that, with
positive probability, every order count simultaneously has its stated
lower bound.

Fix such orders.  The contribution (Z_{C,D}(S)) of one product torus
to (A_{m out}(S)) lies in ([0,d]), and the variables belonging to
different tori are independent.  Equations (3.2)--(3.8) and the order
lower bounds show that the conditional mean (M_S) is at least

\[
 (1-\varepsilon_d)c_dU_{2d}(q)                      \tag{4.8}
\]

when (b>0), and at least
((1-\varepsilon_d)U_{2d}(q)) when (b=0).
Furthermore

\[
 U_{2d}(q)
 \ge 2^{2d-1}(2d)^{-2C\sqrt d}.                     \tag{4.9}
\]

There are at most (N_d^2) contributing tori.  Hoeffding's inequality,
using (N_d^2d^2=2^{2d-2}), gives

\[
 \Pr\bigl(A_{m out}(S)<(1-\varepsilon_d)M_Sigr)
 \le
 \exp\left(-\frac{2\varepsilon_d^2M_S^2}
 {N_d^2d^2}\right).                                 \tag{4.10}
\]

By (4.8)--(4.9), the exponent in (4.10) is
(2^{(9/5)d-o(d)}).  A second union bound over fewer than (2^{2d})
sets is therefore valid.  The resulting literal choices of orders,
balanced words, and phases satisfy (4.3). (square)

No independence remains in the final factor: randomness is used only
to prove that one deterministic collection of integral torus factors
exists.

## 5. Recursive factor and its sole structural defect

Fix (C>0).  Choose a sufficiently large power of two (d_0=d_0(C))
so that Lemma 4.1 applies and

\[
 \prod_{j\ge0}
 \left(1-2^{-2^jd_0/10}\right)^2\ge\frac12.         \tag{5.1}
\]

On a fixed (d_0)-set (K), take a fixed-order Hamming factor, with
cyclic order (pi_0).  Let (mathscr A_{d_0}) consist of the nonempty
cyclic intervals of (pi_0) of size at most (C\sqrt{d_0}).  Since
every such interval occurs in all (N_{d_0}) cycles and
(inom{d_0}q\ge d_0) for (1\le q<d_0),

\[
 A_{mathcal F_{d_0}}(S)=N_{d_0}\ge U_{d_0}(|S|).    \tag{5.2}
\]

Apply Lemma 4.1 recursively, always retaining the old factor as the
right child and refreshing a new left child.  For every

\[
 h=2^td_0
\]

this gives an exact isometric factor (mathcal F_h) such that

\[
 A_{mathcal F_h}(S)\ge\frac12U_h(|S|)>0
 \quad\text{for every }S\inmathscr A_h.             \tag{5.3}
\]

The recursively admissible family has a simple description.  There is
a nested right spine ending in the fixed core (K).  At every split of
a current (2d)-block into its new left (d)-block and inherited right
(d)-block, both intersection sizes are at most (C\sqrt d); at the
bottom, (S\cap K) is a cyclic interval of (pi_0).  There is no
direction-order restriction on any refreshed left block.

## 6. Gaussian-depth approximate covering

### Theorem 6.1 (exact factor, approximate simultaneous (q)-cover)

For every fixed (A>0), there is (r_0(A)) such that for every power
of two (h=2^r), (r\ge r_0(A)), there is an exact isometric
(2h)-cycle factor (mathcal F_h) with

\[
 \max_{1\le q\le A\sqrt h}
 \frac{\#\{S\in\binom{[h]}q:A_{mathcal F_h}(S)=0\}}
 {\binom hq}=o_A(1).                                 \tag{6.1}
\]

More precisely, the factors can be chosen so that every recursively
admissible (S) has the positive lower quota (5.3).

### Proof

Choose (C>A/\sqrt2), and perform the construction of Section 5.
It remains only to count nonadmissible sets.

Let (S) be uniform in (inom{[h]}q), where (q\le A\sqrt h).
If (|S\cap K|\le1), then (S\cap K) is automatically a cyclic
interval.  Hence

\[
 \Pr(S\cap K\text{ is not an interval})
 \le
 \mathbb E\binom{|S\cap K|}{2}
 =\binom{d_0}{2}\frac{\binom q2}{\binom h2}
 =O_{A,d_0}(h^{-1}).                                 \tag{6.2}
\]

Consider one of the dyadic half-blocks of size (d) on the nested
right spine, where (d_0\le d\le h/2).  Its intersection size (X_d)
is hypergeometric, with

\[
 \mu_d=\mathbb EX_d=\frac{qd}{h}\le\frac{Ad}{\sqrt h},
 \qquad T_d=C\sqrt d.
\]

Thus

\[
 \frac{T_d}{\mu_d}
 \ge\frac CA\sqrt{\frac hd}
 \ge\frac{\sqrt2C}{A}>1.                            \tag{6.3}
\]

The hypergeometric Chernoff bound yields

\[
 \Pr(X_d\ge T_d)
 \le
 \exp\left[-T_d\left(
 \log\frac{T_d}{\mu_d}-1+\frac{\mu_d}{T_d}
 \right)\right].                                    \tag{6.4}
\]

For (ho_0=\sqrt2C/A>1), the bracket in (6.4) is at
least (c_{ho_0}log(T_d/\mu_d)), with
(c_{ho_0}>0).  Consequently

\[
 \Pr(X_d\ge T_d)
 \le
 \exp\left[-c_{ho_0}C\sqrt d
 \log\left(\frac CA\sqrt{\frac hd}\right)\right]. \tag{6.5}
\]

Along the dyadic spine there are only two relevant (d)-blocks at
each scale.  The exponent in (6.5), as a function of dyadic (d), is
bounded below by the smaller of a positive multiple of (sqrt h) and
a positive multiple of (sqrt{d_0}log(h/d_0)).  By taking the already
fixed (d_0(A)) larger if necessary, the union of (6.5) over all scales
is (o_A(1)).  Together with (6.2), this proves that a uniform
(q)-set is in (mathscr A_h) with probability (1-o_A(1)), uniformly
for (1\le q\le A\sqrt h).  Equation (5.3) then proves (6.1).
(square)

## 7. Scope and remaining gate

This theorem gives a positive answer to the inner direction-design
problem at Gaussian depth:

* the cycles form one literal exact vertex factor;
* every cycle is an isometric (2h)-cycle;
* one factor simultaneously covers (1-o_A(1)) of the (q)-subsets
  for every (q\le A\sqrt h);
* every covered (q)-set is the support of a genuinely consecutive
  direction block, not a fractional or separately labelled proxy;
* on the explicit recursively admissible family, the count is at least
  one half of the uniform mean (U_h(q)).

It evades the fixed-kernel obstruction because the left kernel/order is
chosen separately over each right-cycle fibre.  It evades the fixed
(Q_4)-leaf Gaussian obstruction because all finite-scale restrictions
except one fixed bottom core are refreshed away.  The sole structural
defect is that the intersection with this fixed core must be a cyclic
interval; at (q=O(\sqrt h)) that defect has density (O(h^{-1})).

This does **not** by itself finish the ambient constant-one theorem.
The remaining application must assign physical starting vertices and
control collisions of the corresponding monotone faces/OR segments.
The result closes only the exact-factor direction-support gate.
