# Coin-free child-hazard Hilbert process: exact reference inflation and the common-core square

Date: 2026-07-27

Method: pure mathematics only.

Scope: the proposed argument which removes compensation coins, gives every
child link its exact nonterminal hazard reference, centers the children of a
fixed parent with their static incidence weights, and invokes the stopped
whole-arm PSF estimate.

## 0. Verdict

Three parts of the proposal are exact.

1.  Every child link has a canonical predictable nonterminal hazard
    integrating factor.  Relative to that factor its live normalized count
    has zero predictable drift and only downward nonterminal jumps.
2.  For

    \[
       p_a={d_0(S\cup\{a\})\over b,d_0(S)},
       \qquad b=r-|S|,
    \]

    the active mass \(P=\sum_{a\ {m active}}p_a\) has favorable drift,
    and the exact parent--child incidence identity determines the weighted
    child mean.
3.  The exclusive-shore part of the child bracket is controlled by the
    already proved whole-arm PSF estimate.  Its integrated coefficient down
    to \(u=z\) is

    \[
             O\!\left({A_H\over mz}\right)
             =m^{-1/2+o(1)}
    \]

    at \(z=m^{-1/2}(\log m)^B\).

These facts do **not** prove \(o(W)\) triple-stop incidence.  There are two
independent missing terms.

First, if \(R_T\) is the exact coin-free child reference, then

\[
 \boxed{
 {R_T(t)\over d_0(T)u_t^{,b-1}}
 =\exp\!\left(\int_0^t
       \bigl(\mathfrak d_T(s)+\mathfrak c_T(s)\bigr)\,ds\right).}
 \tag{0.1}
\]

Here \(\mathfrak c_T\) is the familiar overlap deficit and
\(\mathfrak d_T\) is the average one-vertex degree deficit in the rows of
the \(T\)-link.  Pair spread controls \(\int\mathfrak c_T=o(1)\), but PSF
does not control \(\mathfrak d_T\).  Even the pointwise condition
\(d_t(x)\ge(1-\eta)\Delta_t\) gives only

\[
       \int_0^{r\log(1/z)}\mathfrak d_T(t)\,dt
       \le \eta r\log(1/z),                              \tag{0.2}
\]

so comparison by \(1+o(1)\) requires the much stronger scale
\(\eta=o((r\log(1/z))^{-1})\), or an incidence-averaged substitute.

Second, the exact child bracket contains the nonnegative common-core square

\[
 \boxed{
 \Theta_T(t)={1\over r}\sum_{x\notin T}{d_t(x)\over\Delta_t}
       \left({d_t(T\cup\{x\})\over d_t(T)}\right)^2.}
 \tag{0.3}
\]

Whole-arm PSF controls future edges meeting the two **exclusive** shores of
two rows.  It does not control an edge which hits a resource already common
to the two rows.  The latter events give (0.3).  A literal simple
\(r\)-uniform block configuration below has exclusive-shore PSF equal to
zero, active-mass jumps \(O((bG)^{-1})\), child references instantaneously
within \(O(G^{-1})\) of the standard reference, but centered Hilbert
generator \(\Theta(1)\).

Thus neither Doob nor Freedman can be invoked from PSF alone.  The exact
surviving positive statement is conditional: one needs both an integrated
reference-inflation estimate and an integrated common-core-square estimate.
The latter is a fourth-profile/pair-square condition, not a whole-arm PSF
condition.

No claim is made here that the block configuration is an induced residual of
the ordinary promotion-frame catalogue before all its geometric stops.  It
is a rigorous statewise counterexample to the proposed implication
``whole-arm PSF \(\Rightarrow\) centered child bracket'', and (0.1) is a
pathwise obstruction to the claimed reference comparison.  Excluding these
two mechanisms in the actual catalogue is exactly the remaining theorem.

## 1. Exact coin-free child reference

Let \({\cal H}_t\) be the current induced simple \(r\)-uniform hypergraph,
let

\[
              \Delta_t=\max_x d_t(x),
              \qquad \nu_t={1\over r\Delta_t},           \tag{1.1}
\]

and use only selected-edge clocks, with no compensation-resource clocks.
Fix an active profile \(S\) of size \(k\), put \(b=r-k\), and fix a child

\[
                         T=T_a=S\cup\{a\}.               \tag{1.2}
\]

Write \({\cal F}_T(t)=\{F\in{cal H}_t:T\subseteq F\}\).  Events meeting
\(T\) are terminal for this coordinate and will remove it from the Hilbert
sum.  For an active row \(F\in{cal F}_T(t)\), its number of nonterminal
killers is

\[
 c_T(F;t)=\bigl|\{e\in{cal H}_t:
             e\cap T=\varnothing,
             \ e\cap(F\setminus T)\ne\varnothing\}\bigr|.  \tag{1.3}
\]

Define the average nonterminal hazard, with value zero when the link is
empty, by

\[
 h_T(t)={\nu_t\over d_t(T)}
             \sum_{F\in{cal F}_T(t)}c_T(F;t).            \tag{1.4}
\]

### Lemma 1.1 (canonical integrating factor)

Until terminal death of \(T\), let

\[
 R_T(t)=d_0(T)\exp\!\left(-\int_0^t h_T(s)\,ds\right),
 \qquad Z_T(t)={d_t(T)\over R_T(t)}.                     \tag{1.5}
\]

Then \(Z_T\), stopped just before terminal death and then removed from the
active coordinate set, has zero predictable nonterminal drift.  Every one
of its nonterminal jumps is nonpositive.

#### Proof

For a nonterminal selected edge \(e\), put

\[
 K_T(e;t)=\bigl|\{F\in{cal F}_T(t):
                         e\cap(F\setminus T)\ne\varnothing\}\bigr|.
 \tag{1.6}
\]

Reversing the row--killer sum gives

\[
 \nu_t\sum_{e:e\cap T=\varnothing}K_T(e;t)
 =\nu_t\sum_{F\in{cal F}_T(t)}c_T(F;t)
 =h_T(t)d_t(T).                                         \tag{1.7}
\]

Hence the nonterminal generator of \(d_t(T)\) is \(-h_Td_t(T)\).
The logarithmic derivative of \(R_T\) is also \(-h_T\), proving zero
drift for the ratio.  A selected edge only deletes rows, so its jump is
\(-K_T(e;t)/R_T(t)\le0\).  \(\square\)

This is the strongest drift cancellation available without adding coins.
It is child-specific: different children generally have different
references \(R_T\).

## 2. Exact comparison with \(u^{b-1}\)

For a resource set \(A\), put

\[
 {cal E}_t(A)=\{e:e\cap A\ne\varnothing\},
 \qquad
 J_t(A)=\sum_{x\in A}d_t(x)-|{cal E}_t(A)|.             \tag{2.1}
\]

The per-edge formula

\[
                J_t(A)=\sum_e(|e\cap A|-1)_+            \tag{2.2}
\]

shows that \(J_t(F)-J_t(T)\ge0\) whenever \(T\subseteq F\).

### Theorem 2.1 (reference-inflation identity)

For every live child \(T\),

\[
 {b-1\over r}-h_T=\mathfrak d_T+\mathfrak c_T,          \tag{2.3}
\]

where

\[
 \mathfrak d_T(t)=
 {1\over r,d_t(T)}
 \sum_{F\in{cal F}_T(t)}\sum_{x\in F\setminus T}
       \left(1-{d_t(x)\over\Delta_t}\right),           \tag{2.4}
\]

and

\[
 \mathfrak c_T(t)=
 {1\over r\Delta_t d_t(T)}
 \sum_{F\in{cal F}_T(t)}
       \bigl(J_t(F)-J_t(T)\bigr).                       \tag{2.5}
\]

Both terms are nonnegative, and (0.1) follows.

#### Proof

Since \(T\subseteq F\),

\[
\begin{aligned}
 c_T(F;t)
 &=|{cal E}_t(F)|-|{cal E}_t(T)|\\
 &=\sum_{x\in F\setminus T}d_t(x)
       -\bigl(J_t(F)-J_t(T)\bigr).                      \tag{2.6}
\end{aligned}
\]

Insert (2.6) into (1.4).  Every row has exactly \(b-1\) resources
outside \(T\), so subtracting the result from \((b-1)/r\) gives
(2.3)--(2.5).  By \(d_t(x)\le\Delta_t\) and (2.2), both summands are
nonnegative.  Finally, with \(u_t=e^{-t/r}\),

\[
 {d\over dt}\log {R_T(t)\over d_0(T)u_t^{b-1}}
 ={b-1\over r}-h_T(t),                                  \tag{2.7}
\]

and integration proves (0.1).  \(\square\)

Before the pair-profile stop, the edge-local pair census gives

\[
              J_t(F)\le {C A_2\Delta_t\over m u_t}.     \tag{2.8}
\]

Consequently

\[
 \mathfrak c_T(t)\le {C A_2\over r m u_t},
 \qquad
 \int_0^{r\log(1/z)}\mathfrak c_T(t)\,dt
 \le {C A_2\over m}\left({1\over z}-1\right).          \tag{2.9}
\]

At \(z=m^{-1/2}(\log m)^B\), the last expression is \(o(1)\) for the
stated polylogarithmic thresholds.  This proves the desired comparison
for the collision part only.

In contrast, if every relevant row resource merely satisfies
\(d_t(x)\ge(1-\eta)\Delta_t\), then

\[
                     \mathfrak d_T(t)\le{(b-1)\eta\over r}
                     \le\eta.                           \tag{2.10}
\]

Integration gives (0.2).  Thus constant-factor or
\(m^{-c}\)-degree flatness with \(c<1\) is far from sufficient at the
full square-root-density horizon.

There is also a literal pathwise sharpness example.  Suppose, on an
interval with no selected event, every resource in every remainder row of
one child has degree \(\varepsilon\Delta\), the relevant killer families
are disjoint, and the maximum \(\Delta\) is attained elsewhere.  Then
\(\mathfrak c_T=0\), whole-arm exclusive-shore PSF is zero, and

\[
 h_T={\varepsilon(b-1)\over r},
 \qquad
 {R_T(t)\over d_0(T)u_t^{b-1}}
 =\exp\!\left({(1-\varepsilon)(b-1)t\over r}\right).    \tag{2.11}
\]

The no-event path has positive probability.  Hence no deterministic or
stopped pathwise comparison of \(R_T\) with \(d_0(T)u^{b-1}\) follows
from PSF.

## 3. Active mass and the exact weighted mean

The time-zero incidence identity is

\[
       \sum_{a\notin S}d_0(S\cup\{a\})=b,d_0(S),       \tag{3.1}
\]

so the weights

\[
                 p_a={d_0(S\cup\{a\})\over b,d_0(S)}  \tag{3.2}
\]

form a probability vector.  Let \({\cal A}_t\) be the extension resources
which are physically active, and put

\[
                         P_S(t)=\sum_{a\in{cal A}_t}p_a.\tag{3.3}
\]

For an edge \(e\) avoiding \(S\), write

\[
                         w_e(t)=\sum_{a\in e\cap{cal A}_t}p_a. \tag{3.4}
\]

### Lemma 3.1 (coin-free active mass)

In the coin-free process,

\[
             (\partial_t+{\cal L}_t){P_S\over u_t}\ge0.\tag{3.5}
\]

If \(w_e\le\omega\) on the stopped interval \(u\ge z\), then the
martingale part of \(P_S/u\) has jumps of magnitude at most \(\omega/z\)
and predictable quadratic variation at most

\[
                     {\omega\over2}(z^{-2}-1).           \tag{3.6}
\]

Thus \(\omega=o(z^2)\) makes every fixed positive lower-mass deviation
exponentially unlikely by one-sided Freedman.

#### Proof

Only edges avoiding \(S\) are nonterminal.  Reversing the deletion sum,

\[
\begin{aligned}
 {\cal L}_tP_S
 &=-\nu_t\sum_{e:e\cap S=\varnothing}w_e\\
 &=-\nu_t\sum_{a\in{cal A}_t}p_a
       d_t^{\,\bar S}(a)
 \ge-{P_S\over r},                                      \tag{3.7}
\end{aligned}
\]

because \(d_t^{\,\bar S}(a)\le d_t(a)\le\Delta_t\).
Since \(\dot u=-u/r\), (3.5) follows.  Moreover

\[
 {d\langle M_P\rangle_t\over dt}
 ={\nu_t\over u_t^2}\sum_e w_e^2
 \le {\omega P_S\over r u_t^2}
 \le {\omega\over r u_t^2}.                             \tag{3.8}
\]

Using \(dt=-r\,du/u\) and \(P_S\le1\) gives (3.6).  The jump bound is
immediate.  Since the drift in (3.5) is favorable for a lower crossing,
one-sided Freedman applies to the negative martingale deviation.
\(\square\)

The stronger formerly quoted estimate \(\omega=O(L^C/(bm))\) used the
now-refuted unrestricted one-frame child bound.  The exact gap-two
configuration gives \(\omega\ge3/(4b)\).  This still satisfies
\(\omega=o(z^2)\) at
\(z=m^{-1/2}(\log m)^B\), but a uniform \(O(1/b)\) cap for every relevant
equality type must be stated separately; it is not PSF.

Now use the standard survival normalizations

\[
 X_S={d_t(S)\over d_0(S)u_t^b},
 \qquad
 X_a={d_t(S\cup\{a\})
             \over d_0(S\cup\{a\})u_t^{b-1}},          \tag{3.9}
\]

and write

\[
 \rho_a(t)={R_{T_a}(t)\over
                  d_0(T_a)u_t^{b-1}},
 \qquad X_a=\rho_a Z_a.                                \tag{3.10}
\]

The current incidence identity gives

\[
 \boxed{
       \sum_{a\in{cal A}_t}p_a\rho_a(t)Z_a(t)
       =\sum_ap_aX_a(t)=u_tX_S(t).}                     \tag{3.11}
\]

Since \(\rho_a\ge1\) by Theorem 2.1,

\[
        \bar Z_S(t):={\sum_{a\in{cal A}_t}p_aZ_a\over P_S(t)}
        \le {u_tX_S(t)\over P_S(t)}.                   \tag{3.12}
\]

In particular, on \(P_S\ge c_0u_t\) and \(X_S\le A_2\),

\[
                         \bar Z_S\le A_2/c_0.           \tag{3.13}
\]

This part of the proposed centering is correct.  Its limitation is also
exact: a standard triple stop says \(X_a=\rho_aZ_a\ge A_3\).  Without an
upper bound on \(\rho_a\), it gives no lower bound on the centered
displacement \(Z_a-\bar Z_S\).

## 4. Exact bracket decomposition

Center the live children at their current \(p\)-weighted mean:

\[
 V_S(t)=\sum_{a\in{cal A}_t}p_a
                  (Z_a(t)-\bar Z_S(t))^2.               \tag{4.1}
\]

Deleting any child coordinate is favorable.  Indeed, deleting a coordinate
of weight \(p\), value \(x\), from total active weight \(P\) changes the
centered sum by

\[
 V_{\rm old}-V_{\rm new}
 ={pP\over P-p}(x-\bar x)^2\ge0.                        \tag{4.2}
\]

After first deleting the coordinates contained in an event \(e\), let
\(B_e\) be the remaining coordinates and put

\[
 \delta_{a,e}={K_{T_a}(e;t)\over R_{T_a}(t)},
 \qquad
 \delta_{e}^{\circ}=\delta_e-
       {\langle\delta_e,{\bf1}\rangle_{p;B_e}\over
        \langle{\bf1},{\bf1}\rangle_{p;B_e}}{\bf1}.    \tag{4.3}
\]

Lemma 1.1 and polarization give

\[
        (\partial_t+{\cal L}_t)V_S
        \le Q_S,
 \qquad
 Q_S=\nu_t\sum_e
          \|\delta_e^{\circ}\|_{L^2(p;B_e)}^2.         \tag{4.4}
\]

The point is not the centering algebra, which is valid, but the size of
\(Q_S\).

Fix one child \(T\), abbreviate \(K(e)=K_T(e;t)\), and for two rows
\(F,F'\in{\cal F}_T(t)\) put

\[
 I=(F\cap F')\setminus T,
 \quad A=(F\setminus F')\setminus T,
 \quad B=(F'\setminus F)\setminus T.                   \tag{4.5}
\]

An edge avoiding \(T\) which kills both rows either meets \(I\), or, if it
avoids \(I\), meets both \(A\) and \(B\).  Therefore

\[
\begin{aligned}
 \nu_t\sum_eK(e)^2
 &\le {b-1\over r}d_t(T)
   +{1\over r\Delta_t}\sum_{x\notin T}
                  d_t(x)d_t(T\cup\{x\})^2\\
 &\hspace{16mm}
   +{C A_H\over r m u_t}d_t(T)^2.                       \tag{4.6}
\end{aligned}
\]

#### Proof of (4.6)

Use \(K^2=K+(K)_2\).  For the first term,

\[
 \sum_eK(e)=\sum_{F\in{\cal F}_T}c_T(F)
 \le(b-1)\Delta_t d_t(T).                               \tag{4.7}
\]

For ordered distinct rows, the common-intersection part is at most

\[
 \sum_{F\ne F'}\sum_{x\in(F\cap F')\setminus T}d_t(x)
 =\sum_{x\notin T}d_t(x)(d_t(Tx))_2
 \le\sum_xd_t(x)d_t(Tx)^2.                              \tag{4.8}
\]

The remaining common killers meet the two exclusive shores.  Whole-arm
PSF gives at most \(C A_H\Delta_t/(m u_t)\) of them for each ordered row
pair.  There are at most \(d_t(T)^2\) ordered pairs.  Multiplication by
\(\nu_t=(r\Delta_t)^{-1}\) proves (4.6).  \(\square\)

After division by \(R_T^2\), (4.6) becomes

\[
 {d\langle Z_T\rangle_t\over dt}
 \le {b-1\over r}{Z_T\over R_T}
       +\Theta_T(t)Z_T^2
       +{C A_H\over r m u_t}Z_T^2,                      \tag{4.9}
\]

with \(\Theta_T\) exactly as in (0.3).  This displays the three pieces:

1. the one-row diagonal;
2. the shared-common-resource square \(\Theta_T\); and
3. the exclusive-shore PSF term.

Only the third is controlled by whole-arm PSF.  The trivial incidence
identity

\[
       \sum_{x\notin T}d_t(Tx)=(b-1)d_t(T)              \tag{4.10}
\]

gives merely \(0\le\Theta_T\le(b-1)/r\le1\).  Thus the omitted term can
be order one.

This does not contradict the statement that PSF is stable under equality
resolution.  When a common resource \(x\) is equality-resolved into the
protected prefix, the relevant prefix becomes \(T\cup\{x\}\), and an event
through \(x\) is then terminal.  Summing those refined pieces back into the
unrefined \(T\)-link produces exactly the square
\(d_t(Tx)^2\) in (4.6).  Equality resolution identifies the next-profile
term; it does not bound it.

The comparison with the compensated process is exact and explains why
removing coins does not remove this obstruction.  A selected edge through
\(x\) has total clock rate \(d_t(x)/(r\Delta_t)\), while the compensation
clock at \(x\) has rate

\[
                  {\Delta_t-d_t(x)\over r\Delta_t}.
\]

Both events delete every row in the \(Tx\)-link.  Their combined coefficient
is exactly \(1/r\), so compensation replaces (0.3) by

\[
             \Theta_T^{\rm comp}(t)
             ={1\over r}\sum_{x\notin T}
                \left({d_t(Tx)\over d_t(T)}\right)^2.   \tag{4.11}
\]

Coins cancel the degree-deficit term in the reference identity, but they
complete rather than cancel the common-core square.  Coin-free evolution
retains the factor \(d_t(x)/\Delta_t\); on high-degree resources, where the
standard reference comparison is plausible, this factor is already
\(1-o(1)\).  Thus the two omissions cannot be traded against each other.

Centering cannot remove it universally.  Formula (4.4) subtracts only the
constant child direction.  A common resource can affect one child block
and not another, producing a genuine contrast.  The next section gives an
exact simple configuration.

## 5. A zero-PSF block with order-one centered generator

Fix integers \(G\ge2\), \(L\ge1\), and \(b\ge3\), put \(r=k+b\), and
fix a \(k\)-set \(S\).  For \(1\le j\le G\), choose pairwise disjoint
cores

\[
                         C_j,\qquad |C_j|=b-1,           \tag{5.1}
\]

and fresh resources \(v_{j,1},\ldots,v_{j,L}\).  The displayed rows are

\[
                  F_{j,\ell}=S\cup C_j\cup\{v_{j,\ell}\}.
                                                                    \tag{5.2}
\]

They are \(r\)-sets.  Put \(\Delta=GL\).  Complete the hypergraph as
follows.

* For every \(x\in C_j\), add \(\Delta-L\) edges containing \(x\) and
  otherwise private padding resources.
* For every \(v_{j,\ell}\), add \(\Delta-1\) edges containing
  \(v_{j,\ell}\) and otherwise private padding resources.
* All padding resources and all padding sets are mutually disjoint and
  disjoint from the displayed rows.

Then every member of every \(C_j\), every \(v_{j,\ell}\), and every
member of \(S\) has degree exactly \(\Delta\); padding resources have
degree one.  Hence the maximum degree is \(\Delta\).  The construction is
simple.

For the parent \(S\),

\[
 d_0(S)=GL=\Delta.                                      \tag{5.3}
\]

Every core child \(T_{j,x}=S\cup\{x\}\), \(x\in C_j\), has degree
\(L\), while every variable child \(S\cup\{v_{j,\ell}\}\) has degree
one.  Thus

\[
 p_x={1\over bG}\quad(x\in C_j),
 \qquad
 p_{v_{j,\ell}}={1\over bGL},                           \tag{5.4}
\]

and each block has total \(p\)-mass exactly \(1/G\).

Consider one padding edge through \(x\in C_j\).  It avoids \(S\), removes
the coordinate \(x\), and deletes every displayed row in block \(j\).
At time zero all normalized child values equal one.  After removing the
coordinate \(x\), every other child in block \(j\) jumps from one to zero,
while all children in the other blocks remain one.  The remaining block
mass is

\[
 q={1\over G}-{1\over bG}={b-1\over bG},                \tag{5.5}
\]

and the total remaining active mass is \(P'=1-1/(bG)\).  Hence the exact
new centered variance is

\[
 V_{j,x}={q(P'-q)\over P'}
 ={\frac{b-1}{bG}\left(1-\frac1G\right)
       \over1-\frac1{bG}}.                              \tag{5.6}
\]

Every one of the \(\Delta-L=\Delta(1-1/G)\) padding edges through \(x\)
has clock rate \((r\Delta)^{-1}\).  Summing (5.6) over the
\(G(b-1)\) core resources gives the time-zero centered generator lower
bound

\[
\begin{aligned}
 (\partial_t+{\cal L}_t)V_S\big|_{t=0}
 &\ge G(b-1){1-1/G\over r}
       {\frac{b-1}{bG}\left(1-\frac1G\right)
        \over1-\frac1{bG}}\\
 &= { (b-1)^2\over br}
       { (1-1/G)^2\over1-1/(bG)}
 =\Theta(1)                                             \tag{5.7}
\end{aligned}
\]

whenever \(b/r\) is bounded away from zero and \(G\ge2\) is fixed or
tends to infinity.

On the other hand, the exclusive-shore common-event count is exactly zero.
Two rows in the same block have exclusive shores
\(\{v_{j,\ell}\}\) and \(\{v_{j,\ell'}\}\), and no padding edge meets
both.  Their common core is \(C_j\), which is precisely the term omitted
by exclusive-shore PSF.  Rows in different blocks have disjoint outside
resources and private padding families.  Displayed rows themselves meet
\(S\), so they are terminal and do not enter the nonterminal count.
Therefore

\[
             C_t^{\rm exclusive}(F,F')=\varnothing
             \quad\hbox{for every displayed row pair}.  \tag{5.8}
\]

The active-mass jump of one such event is only \(p_x=1/(bG)\).  Finally,
for a core child \(T_{j,x}\), the exact initial nonterminal hazard is

\[
 h_{T_{j,x}}(0)
 ={(b-2)(1-1/G)+(1-1/\Delta)\over r}.                   \tag{5.9}
\]

Thus its instantaneous reference deficit is

\[
 {b-1\over r}-h_{T_{j,x}}(0)
 ={b-2\over rG}+{1\over r\Delta}=O(G^{-1}),             \tag{5.10}
\]

while the centered generator (5.7) remains order one as \(G\to\infty\).
This separates the common-core obstruction from both the active-mass and
reference-comparison issues.

The same calculation appears directly in (0.3): for a core child,

\[
 \Theta_{T_{j,x}}(0)
 \ge {1\over r}\sum_{y\in C_j\setminus\{x\}}1
 ={b-2\over r}=\Theta(1).                               \tag{5.11}
\]

This proves that no statewise inequality

\[
                   Q_S\le {L^C\over rb}\times
                   \hbox{(current Hilbert mass)}         \tag{5.12}
\]

can follow from whole-arm PSF, even with arbitrarily small active-mass
jumps and arbitrarily accurate instantaneous child references.

## 6. Exact Doob/Freedman accounting

It is useful to state what would work if the two missing terms were supplied.
Stop a child while \(Z_T\le K\).  By (4.9), its predictable bracket is at
most

\[
 K^2\Gamma_T+K\Xi_T,                                   \tag{6.1}
\]

where

\[
\begin{aligned}
 \Gamma_T
 &=\int_0^{\tau}
       \left(\Theta_T(t)+{C A_H\over r m u_t}\right)dt,\\
 \Xi_T
 &=\int_0^{\tau}{b-1\over rR_T(t)}dt.                  \tag{6.2}
\end{aligned}
\]

All jumps of the martingale \(Z_T\) are nonpositive.  The one-sided
Freedman inequality for martingales with jumps bounded above by zero gives,
for \(K\ge2\),

\[
 \Pr\!\left(\sup_{t\le\tau}Z_T(t)\ge K\right)
 \le
 \exp\!\left[-{c\over \Gamma_T+\Xi_T/K}\right].       \tag{6.3}
\]

The statement is understood after replacing deterministic bounds in
(6.2) by stops; the stopped process is bounded and hence is a true
martingale.  Equation (6.3) follows from the usual exponential
supermartingale proof, using
\(e^x-1-x\le x^2/2\) for \(x\le0\).

The total static child incidence above one parent is

\[
             \sum_a q_{k+1}(S\cup\{a\})=bq_k(S).        \tag{6.4}
\]

Therefore, allowing a polynomial marked-monitor multiplicity \(M_m\), a
uniform bound

\[
 \Gamma_T+\Xi_T/K=o\!\left({1\over\log(bM_m)}\right)   \tag{6.5}
\]

makes the stopped child incidence \(o(q_k(S))\).  The PSF contribution to
\(\Gamma_T\) is

\[
 \int_0^{r\log(1/z)}{C A_H\over r m u_t}dt
 ={C A_H\over m}\left({1\over z}-1\right)
 =m^{-1/2+o(1)},                                        \tag{6.6}
\]

which is much smaller than \(1/\log m\).  Thus Freedman would close the
exclusive-shore sector with enormous margin.  What prevents (6.5) is
\(\int\Theta_T\), not PSF.

For comparison, a second-moment/Doob energy alone is weaker.  Suppose the
reference ratios are \(e^{o(1)}\), the parent is below \(A_2\), and the
active mass is at least \(c_0u\).  Then (3.13) and Gronwall applied only to
the PSF part give the centered-energy budget

\[
             O\!\left({A_HA_2^2\over mz}\right).        \tag{6.7}
\]

A child standard crossing at level \(A_3\ge4A_2/c_0\) costs
\(\Omega(p_aA_3^2)\).  Multiplying the resulting \(p\)-mass by
\(bq_2(S)\), the best conclusion from (6.7) is

\[
 {\hbox{triple stopped mass above }S\over q_2(S)}
 \le
 C{A_HA_2^2\over zA_3^2}.                              \tag{6.8}
\]

At \(z=m^{-1/2}(\log m)^B\), polylogarithmic
\(A_3/A_2\) does not make (6.8) vanish.  Thus plain Doob/second moment is
quantitatively insufficient even after deleting the common-core term;
one needs the one-sided Freedman gain or the stronger centered-diagonal
scale \(O((rb)^{-1})\).

## 7. Precise surviving theorem

The coin-free proposal becomes valid under the following three additional
statements, none of which follows from whole-arm PSF.

1. **Reference inflation.**  Outside \(o(W)\) marked incidence,

   \[
      \sup_{T,t\le T_z}\int_0^t\mathfrak d_T(s)ds=o(1).
                                                               \tag{RI}
   \]

   Together with (2.9), this makes
   \(R_T=(1+o(1))d_0(T)u^{b-1}\).

2. **Active-frame mass.**  For each monitored parent,

   \[
      \sup_{e:t\le T_z}\sum_{a\in e}p_a=o(z^2),        \tag{AM}
   \]

   or an incidence-averaged replacement strong enough for Lemma 3.1.

3. **Common-core square.**  Uniformly in the stopped marked incidence,

   \[
      \int_0^{T_z}{1\over r}\sum_{x\notin T}
        {d_t(x)\over\Delta_t}
        \left({d_t(Tx)\over d_t(T)}\right)^2dt
      =o\!\left({1\over\log m}\right).               \tag{CCS}
   \]

   A direct incidence-weighted version of (CCS) is sufficient and is
   probably the natural target; a pointwise version is stronger than needed.

Under (RI), (AM), (CCS), the large-initial-link bound making \(\Xi_T=o(1/\log
m)\), and the already proved PSF, equations (3.6), (6.3), and (6.4) prove
\(o(W)\) triple-stop incidence.  Conversely, Sections 2 and 5 show that
(RI) and (CCS) cannot be deleted from this proof architecture.

The exact conditional boundary is therefore

\[
 \boxed{
 \begin{array}{c}
 \text{coin-free exact hazards remove first-order drift, but}\\
 \text{they do not compare to the standard profile reference without (RI),}\\
 \text{and whole-arm PSF does not control the shared-core square (CCS).}
 \end{array}}
\]

Proving an incidence-averaged (CCS) theorem for the actual ordinary-frame
trajectory, together with the degree-deficit integral (RI), would complete
this Hilbert/Freedman route.  Without them, the claimed \(o(W)\) conclusion
is not proved.
