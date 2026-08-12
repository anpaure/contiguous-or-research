# Pair-radius reset colours: the exact adjacent-flag Hall obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad V_q=\binom{[n]}{m-q},\qquad
 N_q=|V_q|,\qquad W=\binom{2m}m,
\]

and

\[
 \lambda_q={W\over N_q}=c_q+\alpha_q,
 \qquad c_q=\lfloor\lambda_q\rfloor,
 \quad 0\le\alpha_q<1.                         \tag{0.1}
\]

The all-depth target tables of an \(H\)-memory circulation cannot be
chosen independently.  Before the de Bruijn overlap equations are even
visible, consecutive lower tables must be the two marginals of a
nonnegative flow on the consecutive-rank inclusion graph.

This gives an exact obstruction to using a compressed pair-radius family
as the **new** high-quota colour at a reset.  Suppose

\[
 c_{q-1}=K-1,\qquad c_q=K,\qquad K\ge2,             \tag{0.2}
\]

so every balanced parent load is at most \(K\), while the new high child
load is \(K+1\).  If \(D\subseteq V_q\) is the new high family, then every
fractional lower-flag realization necessarily satisfies

\[
                         (K+1)|D|\le K|\nabla D|,   \tag{0.3}
\]

where \(\nabla D\subseteq V_{q-1}\) is the upper shadow.  More robustly,
for arbitrary realized loads \(\mu_{q-1},\mu_q\),

\[
 \sum_{S\in D}(K+1-\mu_q(S))_+
 +\sum_{T\in\nabla D}(\mu_{q-1}(T)-K)_+
 \ge (K+1)|D|-K|\nabla D|.                       \tag{0.4}
\]

Fix a pairing of the \(2m\) coordinates and let \(d(S)\) count full
pairs.  For the low pair-radius family

\[
                         D_q(r)=\{S\in V_q:d(S)\le r\},        \tag{0.5}
\]

one has the exact shadow identity

\[
                         \nabla D_q(r)=D_{q-1}(r+1).            \tag{0.6}
\]

At Gaussian depth \(q=\Theta(\sqrt m)\), if the density of \(D_q(r)\)
is polynomially small but not exponentially small, then

\[
                         {|\nabla D_q(r)|\over|D_q(r)|}=1+o(1). \tag{0.7}
\]

Thus (0.3) fails for every fixed reset level \(K\).  The failure is
fractional, hence adding reset labels or bounded de Bruijn states cannot
repair it.

There is a dual cut for the old low-load fringe.  Immediately before the
reset, let

\[
 A=\{T:d(T)\le r_-\},\qquad E=V_{q-1}\setminus A,
\]

so \(A\) has load \(K\) and \(E\) has load \(K-1\).  Put

\[
                         C=\{S\in V_q:d(S)\ge r_-+1\}.          \tag{0.7a}
\]

At a polynomial upper-tail threshold, \(\nabla C=E\) and
\(|E|/|C|=1+o(1)\).  The flag Hall inequality would require

\[
                         K|C|\le(K-1)|E|,                       \tag{0.7b}
\]

which, for fixed \(K\), also fails by \((1-o_K(1))|E|\).  The two
cuts have disjoint low- and high-radius supports.  Consequently, at a
fixed-level Gaussian reset, a compressed pair-radius menu must pay
essentially the **entire reset fringe**

\[
 (1-\alpha_{q-1})N_{q-1}+\alpha_qN_q,                          \tag{0.7c}
\]

not merely the new bonus mass.

There is an explicit infinite Gaussian family.  For every fixed integer
\(K\ge2\), there are \(m_t\to\infty\) and reset depths
\(q=t=\Theta(\sqrt{m_t})\) such that

\[
 c_{t-1}=K-1,\qquad c_t=K,
 \qquad \alpha_t=\Theta_K(m_t^{-1/2}).             \tag{0.8}
\]

If the new high family is a pair-radius threshold of the prescribed
cardinality up to relative \(o(1)\), then

\[
 |D|=\Theta_K(W/\sqrt m),\qquad
 (K+1)|D|-K|\nabla D|=(1-o(1))|D|.                \tag{0.9}
\]

Consequently essentially every new compressed bonus unit must either be
dropped at the child rank or paid for by a parent cap violation.  This
survives the polynomial-size exact point-margin corrections from the
common-run theorem.

The obstruction is not a coefficient-one no-go in a fixed Gaussian
window: \(W/\sqrt m=o(W)\), and only \(O_A(1)\) fixed integer resets occur
for \(q\le A\sqrt m\).  A successful reset colour must be supported on
an expansion-rich family, or must charge the compressed old and new
fringes as exceptional.  Pair-radius compression can still be used inside
an epoch; it cannot itself supply either side of a fixed-level epoch
boundary.  No growing-\(K\) aggregate theorem is claimed: the
\(1+o(1)\) shadow expansion is multiplied by \(K\) in the Hall deficit.

The previously known finite obstructions have two different indexings:
the square-root obstruction is \(m=H=2\), while the balanced singleton
point-margin obstruction is \(m=3,H=2\).

## 1. The first projection: consecutive flag flow

Let \(\mu_q:V_q\to\mathbb R_{\ge0}\) be proposed lower target loads, all
having the same total \(W'\).  A fractional system of nested lower flags
with these marginals is a nonnegative measure on paths

\[
 L_0\supset L_1\supset\cdots\supset L_H,
 \qquad |L_q|=m-q,                                  \tag{1.1}
\]

whose marginal at rank \(q\) is \(\mu_q\).

### Theorem 1.1 (exact flag-flow criterion)

The tables \((\mu_q)_{q\le H}\) are the marginals of a fractional nested
flag system if and only if, for every \(q\ge1\), there is a nonnegative
flow

\[
 p_q(T,S)\qquad(S\subset T,\ |T\setminus S|=1)      \tag{1.2}
\]

with row marginal \(\mu_{q-1}\) and column marginal \(\mu_q\).
Equivalently, for every \({\cal A}\subseteq V_q\),

\[
 \boxed{\quad
 \sum_{S\in{\cal A}}\mu_q(S)
 \le \sum_{T\in\nabla{\cal A}}\mu_{q-1}(T).
 \quad}                                             \tag{1.3}
\]

If all tables are integral, the flag system can be chosen integral.

#### Proof

Every nested flag uses one inclusion edge between two consecutive ranks;
summing its weight gives (1.2).  Conversely, normalize the outgoing flow
from a positive-load node \(T\) to obtain a transition kernel
\(p_q(T,S)/\mu_{q-1}(T)\).  Starting with the measure \(\mu_0\) and
successively applying these kernels gives a measure on complete flags
with the prescribed marginals.

For one adjacent pair, (1.3) is exactly the max-flow/min-cut criterion in
the bipartite inclusion graph, with source capacities \(\mu_{q-1}(T)\)
and sink demands \(\mu_q(S)\).  This proves the equivalence.  With
integral margins the network has an integral feasible flow.  At an
internal node, match its incoming flow units to its outgoing flow units;
iterating this operation decomposes the integral layered flow into
integral unit flags. \(\square\)

Theorem 1.1 is only the one-sign Boolean-flag projection.  It omits the
upper flags, common middle owners, run vector, suffix overlap, and cycle
count.  Therefore failure of (1.3) is decisive, whereas satisfaction of
all its inequalities is not sufficient for an \(H\)-memory circulation.

## 2. Reset expansion and its robust form

Assume (0.2), and let \(D\subseteq V_q\) be prescribed to have load
\(K+1\).  Every balanced table on \(V_{q-1}\) has load at most \(K\).
Apply (1.3) with \({\cal A}=D\).  This gives (0.3).

For the robust statement, put

\[
 E_D=\sum_{S\in D}(K+1-\mu_q(S))_+,
 \qquad
 E_\nabla=\sum_{T\in\nabla D}(\mu_{q-1}(T)-K)_+.   \tag{2.1}
\]

Then

\[
 \sum_{S\in D}\mu_q(S)\ge(K+1)|D|-E_D,            \tag{2.2}
\]

while

\[
 \sum_{T\in\nabla D}\mu_{q-1}(T)
 \le K|\nabla D|+E_\nabla.                          \tag{2.3}
\]

Insert these estimates in (1.3).  Rearrangement proves (0.4).  In
particular, if

\[
                         |\nabla D|\le(1+\varepsilon)|D|,       \tag{2.4}
\]

then

\[
                         E_D+E_\nabla
 \ge \bigl(1-K\varepsilon\bigr)|D|.              \tag{2.5}
\]

This is stable under arbitrary changes outside \(D\) and \(\nabla D\).
It also permits overload at the parent rank, but charges it exactly.

## 3. Exact radial quotient

The obstruction above is one cut of a complete one-dimensional
description for pair-invariant tables.  Let

\[
 A_{q,d}=\#\{S\in V_q:d(S)=d\}
 ={m!\,2^{m-q-2d}\over
   d!\,(q+d)!\,(m-q-2d)!}.                       \tag{3.1}
\]

Suppose \(\mu_q(S)=u_{q,d(S)}\).  Put

\[
                         P_d=A_{q-1,d}u_{q-1,d},
 \qquad Q_d=A_{q,d}u_{q,d},                       \tag{3.2}
\]

padding nonexistent classes by zero.  A deletion either changes
\(d\) to \(d-1\), when a coordinate from a full pair is deleted, or
leaves \(d\) unchanged, when a singleton-pair coordinate is deleted.

### Proposition 3.1 (radial adjacent-flow criterion)

The two radial tables admit a fractional inclusion flow if and only if,
for every \(d\ge1\),

\[
 Y_d:=\sum_{i=0}^{d-1}(Q_i-P_i)                  \tag{3.3}
\]

satisfies

\[
                         0\le Y_d\le P_d,          \tag{3.4}
\]

with the zero-padded terminal equation implied by
\(\sum_dP_d=\sum_dQ_d\).

#### Proof

Let \(x_d\) be the total flow from parent class \(d\) to child class
\(d\), and let \(y_d\) be the flow from parent class \(d\) to child
class \(d-1\), with \(y_0=0\).  The marginal equations are

\[
                         P_d=x_d+y_d,
 \qquad Q_d=x_d+y_{d+1}.                          \tag{3.5}
\]

Thus

\[
                         y_{d+1}-y_d=Q_d-P_d,
\]

and consequently \(y_d=Y_d\).  Nonnegativity of \(x_d,y_d\) is exactly
(3.4).  At a parity endpoint where the unchanged-\(d\) edge type does
not exist, the zero-padded terminal equation forces \(x_d=0\), so no
extra condition has been omitted.

Conversely, (3.3)--(3.4) define nonnegative \(x_d=P_d-Y_d\) and
\(y_d=Y_d\).  Distribute each total uniformly over the corresponding
pair-wreath orbit of inclusion edges.  This gives a fractional flow with
the required per-set marginals.  Since the underlying bipartite network
is integral, integral per-set loads also admit an integral flow. \(\square\)

This quotient can test any proposed pair-radius/reset table exactly.  It
does not encode suffix overlap; it is the first necessary projection.

## 4. The pair-radius shadow is too small at a reset

For \(D_q(r)\) from (0.5), adding one coordinate either preserves \(d\)
or increases it by one.  Conversely, every parent with \(d\le r+1\) has
a deletion into a child with \(d\le r\).  Hence (0.6) holds exactly.

Write

\[
 F_q(r)={|D_q(r)|\over N_q},
 \qquad p_{q,d}={A_{q,d}\over N_q}.               \tag{4.1}
\]

Uniform deletion from rank \(q-1\) to rank \(q\) gives the exact identity

\[
 F_q(r)=F_{q-1}(r)
 +p_{q-1,r+1}{2(r+1)\over m-q+1}.                 \tag{4.2}
\]

Therefore

\[
 {|\nabla D_q(r)|\over|D_q(r)|}
 ={m+q\over m-q+1}
 {F_{q-1}(r)+p_{q-1,r+1}
  \over
  F_{q-1}(r)+{2(r+1)\over m-q+1}p_{q-1,r+1}}.     \tag{4.3}
\]

The adjacent atom ratio is

\[
 {p_{q,d+1}\over p_{q,d}}
 ={(m-q-2d)(m-q-2d-1)
   \over4(d+1)(q+d+1)}.                           \tag{4.4}
\]

It follows directly by multiplying these ratios away from the mode that,
uniformly for \(q=O(\sqrt m)\) and lower-tail probabilities between
\(m^{-C}\) and \(1/4\),

\[
 {p_{q-1,r+1}\over F_{q-1}(r)}
 =O_C\!\left(\sqrt{\frac{\log m}{m}}\right).      \tag{4.5}
\]

For completeness, a lower-tail probability at least \(m^{-C}\) places
the boundary at distance \(O_C(\sqrt{m\log m})\) below the mode: farther
away, the products in (4.4) give a smaller than polynomial tail.  Over
the preceding \(\Omega_C(\sqrt{m/\log m})\) atoms, (4.4) stays within a
fixed exponential factor of one, so their sum is
\(\Omega_C(\sqrt{m/\log m})\) times the boundary atom.  This proves
(4.5), with a change of the implicit constant.

Insert (4.5) into (4.3).  Since \(q=O(\sqrt m)\),

\[
 {|\nabla D_q(r)|\over|D_q(r)|}
 =1+O_C\!\left(\sqrt{\frac{\log m}{m}}\right).     \tag{4.6}
\]

For every fixed \(K\), (4.6) is eventually smaller than
\((K+1)/K\).  Equations (0.3)--(0.4) now prove the fractional and robust
pair-radius reset obstruction.

### Theorem 4.1 (the old fringe gives the dual Hall obstruction)

At a reset (0.2), suppose the prescribed parent table is

\[
 \nu_{q-1}(T)=
 \begin{cases}
 K,&d(T)\le r_-,\\
 K-1,&d(T)\ge r_-+1,
 \end{cases}                                                    \tag{4.7}
\]

and define

\[
 E=\{T\in V_{q-1}:d(T)\ge r_-+1\},\qquad
 C=\{S\in V_q:d(S)\ge r_-+1\}.                  \tag{4.8}
\]

Assume the boundary class \(d=r_-+1\) in \(V_{q-1}\) has a singleton
pair; equivalently,

\[
                         2(r_-+1)<m-q+1.                         \tag{4.9}
\]

Then

\[
                         \nabla C=E.                             \tag{4.10}
\]

If \(q=O(\sqrt m)\) and the upper-tail density of \(E\) lies between
\(m^{-C_0}\) and \(1/4\), for fixed \(C_0\), then

\[
                         {|E|\over|C|}
 =1+O_{C_0}\!\left(\sqrt{\frac{\log m}{m}}\right).              \tag{4.11}
\]

For arbitrary realized tables, put

\[
 E_C=\sum_{S\in C}(K-\mu_q(S))_+,
 \qquad
 E_E=\sum_{T\in E}(\mu_{q-1}(T)-(K-1))_+.        \tag{4.12}
\]

For fixed reset level \(K\),

\[
 E_C+E_E\ge K|C|-(K-1)|E|
                         =(1-o_K(1))|E|.           \tag{4.13}
\]

#### Proof

Adding a coordinate never decreases pair radius, so every parent of a
member of \(C\) lies in \(E\).  Conversely, a parent in \(E\) can delete
a singleton-pair coordinate and retain its radius.  Condition (4.9)
guarantees such a singleton even in the boundary class, proving (4.10).

Let \(G=1-F_{q-1}(r_-)\) and
\(p=p_{q-1,r_-+1}\).  Taking complements in (4.2) gives

\[
 { |E|\over N_{q-1}}=G,
 \qquad
 { |C|\over N_q}
 =G-{2(r_-+1)\over m-q+1}p.                    \tag{4.14}
\]

The upper-tail counterpart of (4.5), proved by reading the ratio products
(4.4) in the other direction, gives

\[
                         {p\over G}
 =O_{C_0}\!\left(\sqrt{\frac{\log m}{m}}\right).
\]

Together with \(N_{q-1}/N_q=(m+q)/(m-q+1)\), this proves (4.11).

Now apply the Hall inequality (1.3) to \(C\).  The analogues of
(2.2)--(2.3) give

\[
 K|C|-E_C
 \le\sum_{S\in C}\mu_q(S)
 \le\sum_{T\in E}\mu_{q-1}(T)
 \le(K-1)|E|+E_E.
\]

This is the first inequality in (4.13); (4.11) gives the last equality.
\(\square\)

At a genuine Gaussian pair-radius reset, the lower and upper quantile
thresholds satisfy \(r_++1\le r_-\) once both tail densities tend to zero
(their locations are on opposite sides of a mode with variance
\(\Theta(m)\)).  Thus the new low-radius family \(D\) and the old-fringe
descendant family \(C\) are disjoint, as are their parent shadows
\(\nabla D\) and \(E\).  Hence the robust inequalities (2.5) and (4.13)
may be added without double-counting a table entry.  Outside this
quantile regime, the disjointness condition \(r_++1\le r_-\) should be
stated explicitly.

Write

\[
 \varepsilon_q=K-\lambda_{q-1},\qquad
 \beta_q=\lambda_q-K.                             \tag{4.15}
\]

The prescribed old and new fringe sizes are

\[
                         \varepsilon_qN_{q-1},
 \qquad \beta_qN_q.                                \tag{4.16}
\]

If a desired tail density is smaller than \(m^{-C_0}\), omitting that
tail costs at most \(Wm^{-C_0}\).  Otherwise the threshold atom-to-tail
bound makes the closest pair-radius threshold have relative cardinal
error \(o(1)\).  Taking \(C_0=2\), uniformly at a fixed-level Gaussian
reset, the total robust Hall cost is therefore

\[
 (1-o(1))
 \bigl(\varepsilon_qN_{q-1}+\beta_qN_q\bigr).       \tag{4.17}
\]

The expression in parentheses is the exact reset fringe.  If

\[
 \delta_q={\lambda_q-\lambda_{q-1}\over\lambda_{q-1}}
 ={2q-1\over m-q+1},                               \tag{4.18}
\]

then direct substitution gives

\[
 {W\delta_q\over1+\delta_q}
 \le
 \varepsilon_qN_{q-1}+\beta_qN_q
 \le W\delta_q.                                   \tag{4.19}
\]

Thus the obstruction is independent of the arithmetic phase at which the
integer is crossed.

For fixed \(K\), equations (4.11) and (4.6) make both Hall-deficit
coefficients \(1-o(1)\), proving (4.17).  This conclusion cannot be
summed unchanged over growing reset levels.  Indeed the exact new-tail
coefficient is

\[
 1-K\left({|\nabla D|\over|D|}-1\right),           \tag{4.20}
\]

and the old-tail coefficient is

\[
 1-(K-1)\left({|E|\over|C|}-1\right).              \tag{4.21}
\]

Although each shadow expansion tends to one, multiplication by a growing
\(K\) need not tend to zero.  Thus a growing-window fringe sum requires
the additional quantitative hypotheses that the two displayed products
are \(o(1)\) (or at least are bounded below one by a fixed margin) at all
charged resets.  The ordinary one-level-reset assumption alone does not
prove this.  In particular, no linear critical-scale obstruction is
deduced here.

## 5. An infinite Gaussian reset sequence

Fix \(K\ge2\), put \(L=\log K\), and for real \(x>t\) define

\[
 \Lambda_t(x)
 =\prod_{i=1}^t{x+i\over x-t+i}.                  \tag{5.1}
\]

This is strictly decreasing from a value larger than \(K\) to one, so
there is a unique \(M_t\) with

\[
                         \Lambda_t(M_t)=K.          \tag{5.2}
\]

The elementary logarithmic expansion gives

\[
                         M_t={t^2\over L}+O_K(t).   \tag{5.3}
\]

Choose a fixed

\[
                         0<\eta<{2\over L}
\]

and put

\[
                         m_t=\lfloor M_t-\eta t\rfloor.         \tag{5.4}
\]

Differentiating (5.1),

\[
 -{d\over dx}\log\Lambda_t(x)
 =\sum_{i=1}^t{t\over(x-t+i)(x+i)}
 ={L^2\over t^2}+O_K(t^{-3})                  \tag{5.5}
\]

uniformly for \(x=M_t+O_K(t)\).  Integrating from \(m_t\) to
\(M_t\) gives

\[
 \log\Lambda_t(m_t)
 =L+{\eta L^2\over t}+O_K(t^{-2}).                \tag{5.6}
\]

Moreover

\[
 \log{\Lambda_t(m_t)\over\Lambda_{t-1}(m_t)}
 =\log{m_t+t\over m_t-t+1}
 ={2L\over t}+O_K(t^{-2}).                        \tag{5.7}
\]

The choice \(\eta<2/L\) and (5.6)--(5.7) imply, for all sufficiently
large \(t\),

\[
 K-1<\Lambda_{t-1}(m_t)<K<\Lambda_t(m_t)<K+1.      \tag{5.8}
\]

Thus depth \(t\) is a reset from floor \(K-1\) to floor \(K\).  Also

\[
 \alpha_t=\Lambda_t(m_t)-K
 ={K\eta L^2+o_K(1)\over t},                      \tag{5.9}
\]

and \(m_t=(1+o_K(1))t^2/L\).  Since
\(N_t=(1+o_K(1))W/K\), the prescribed new high mass is

\[
 \alpha_tN_t
 =(\eta L^2+o_K(1)){W\over t}
 =\Theta_K(W/\sqrt m).                            \tag{5.10}
\]

Choose the least pair-radius threshold whose density reaches
\(\alpha_t\).  Equations (4.4)--(4.5) show that its boundary atom is
\(o(\alpha_t)\), so

\[
                         |D|=(1+o(1))\alpha_tN_t.   \tag{5.11}
\]

Equations (4.6), (2.5), and (5.10) yield

\[
 E_D+E_\nabla
 \ge(1-o(1))|D|
 =\Theta_K(W/\sqrt m).                            \tag{5.12}
\]

This proves the infinite robust obstruction.

## 6. Exact boundary for the circulation attack

The following statements are proved.

1. Consecutive target tables of any fractional or integral memory
   circulation satisfy every flag Hall inequality (1.3).
2. Pair-invariant consecutive tables have the exact radial criterion
   (3.3)--(3.4).
3. At a quota reset, a new high family must expand by at least
   \((K+1)/K\) into the parent rank.
4. A polynomial-density low pair-radius tail expands by only \(1+o(1)\),
   and therefore cannot be the new high reset colour.
5. The old low-load high-radius fringe obeys the dual obstruction; the
   two disjoint cuts force essentially the whole reset fringe to change.
6. Infinitely many Gaussian resets force
   \(\Theta_K(W/\sqrt m)\) table changes for this prescribed menu.
7. A growing-level aggregate needs uniform control after multiplying the
   shadow-expansion errors by the reset level \(K\); one-level reset
   arithmetic alone does not supply it.

The following are not proved and must not be inferred.

1. There is no obstruction here to choosing expansion-rich old and new
   reset fringes.  A diffuse hash family may have a very large shadow.
2. The forced cost in (5.12) is \(o(W)\).  It does not refute an
   asymptotic near-balanced circulation or the coefficient-one theorem.
3. Passing all flag Hall inequalities does not solve the common-owner,
   two-sign, de Bruijn-overlap, integrality, or cycle-count constraints.
4. Pair-radius menus remain viable away from resets, where their
   compressed shadows are precisely what aligns forbidden rows.

Thus the minimal stable obstruction beyond the finite square/parity
examples is an adjacent-rank expansion requirement.  Reset colours do
not remove it; they must be designed around it.
