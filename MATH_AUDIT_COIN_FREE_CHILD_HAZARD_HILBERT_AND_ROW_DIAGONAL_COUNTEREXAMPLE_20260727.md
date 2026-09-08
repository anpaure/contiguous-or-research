# Coin-free child hazards: exact references, active-mass drift, and the row-diagonal obstruction

Date: 2026-07-27

Method: pure mathematics only.  No computation, search, solver, or external
input is used.

## 0. Verdict

Let \({\cal H}_t\) be an induced \(r\)-uniform residual and give every
current edge rate

\[
                 \nu_t={1\over r\Delta_t},\qquad
                 \Delta_t=\max_x d_t(x).
\tag{0.1}
\]

There are no compensation-resource clocks in the coin-free process.  Fix an
active parent profile \(S\), put \(k=|S|\), \(b=r-k\), and let
\(T=S\cup\{a\}\) be a child.  The exact nonterminal child-link hazard is

\[
 h_T(t)={\nu_t\over d_t(T)}
 \sum_{F\supset T}
 \bigl|{\cal E}_t(F)\setminus{\cal E}_t(T)\bigr|.
\tag{0.2}
\]

Writing

\[
 J_t(A)=\sum_{x\in A}d_t(x)-|{\cal E}_t(A)|,
\tag{0.3}
\]

one has the exact decomposition

\[
 \boxed{
 {b-1\over r}-h_T(t)
 ={1\over r\Delta_t d_t(T)}
 \sum_{F\supset T}
 \left[
   \sum_{x\in F\setminus T}(\Delta_t-d_t(x))
   +J_t(F)-J_t(T)
 \right].}
\tag{0.4}
\]

Consequently the correct child-specific reference is

\[
 \boxed{
 R_T(t)=\exp\left[-\int_0^t h_T(s)\,ds\right]
 =u_t^{b-1}\exp\left[\int_0^t\epsilon_T(s)\,ds\right],
 \quad u_t=e^{-t/r},}
\tag{0.5}
\]

where \(\epsilon_T=(b-1)/r-h_T\ge0\).  In particular, only

\[
                         R_T(t)\ge u_t^{b-1}
\tag{0.6}
\]

is automatic.  The reverse comparison, which is needed to turn a crossing
at the natural reference \(d_0(T)u^{b-1}\) into a fixed displacement in the
child-normalized Hilbert coordinate, requires the additional integrated
degree-deficit estimate

\[
 \int_0^t {1\over r\Delta_s d_s(T)}
 \sum_{F\supset T}\sum_{x\in F\setminus T}
       (\Delta_s-d_s(x))\,ds=o(1).
\tag{ID}_T
\]

Whole-arm PSF does not contain this quantity.

There is a second independent failure.  With

\[
 p_a={d_0(S\cup\{a\})\over b\,d_0(S)},\qquad
 P_S(t)=\sum_a p_a I_a(t),
\tag{0.7}
\]

the edge-only process gives

\[
 \boxed{
 (\partial_t+{\cal L}_t){P_S\over u_t}
 ={1\over r\Delta_tu_t}
   \sum_a p_a I_a(t)(\Delta_t-d_t(a))\ge0.}
\tag{0.8}
\]

Thus \(P_S/u\) is a submartingale, not a martingale, unless every
\(p\)-supported live child resource has degree exactly \(\Delta_t\).  Its
lower drift is favorable, but a Freedman proof must use (0.8) and its
bracket; it cannot quote the compensated active-mass martingale.

Most decisively, even granting \(R_T=(1+o(1))u^{b-1}\), the required
active-mass lower bound (with exact balance at the initial state), and the
strongest possible distinct-row whole-arm PSF bound, the
centered Hilbert diagonal need not be \(O((rb)^{-1})\).  Section 5 gives an
explicit simple \(r\)-uniform catalogue for which

* every monitored child resource has degree \(\Delta\), so (0.8) is zero
  initially;
* every child reference differs from \(u^{b-1}\) at logarithmic derivative
  only \(O(1/\Delta)\);
* two distinct rows of the parent link have no common nonterminal edge, so
  the distinct-row PSF term is identically zero; but
* the generator of the exactly centered child variance at time zero is at
  least \((b-1)/(4r)=\Theta(1)\).

The obstruction is the same-row death diagonal.  Doob controls it only at
the scalar \(A_3^{-1}\) scale; that is insufficient because converting
child \(p\)-mass to triple incidence multiplies by \(b\sim m\).

Therefore **the hazard integrating factor and whole-arm PSF alone do not
prove \(o(W)\) triple-stop incidence for the proposed coin-free Hilbert
process.**  They omit both the comparison with \(u^{b-1}\) and the
same-row diagonal.

There is, however, a catalogue-specific positive repair.  Section 3 proves
the edge-only active-mass lower stop from PPS by a direct quadratic-variation
calculation.  Section 4 proves that every compatible physical triple in the
ordinary promotion-frame catalogue has at least
\(\exp[m\log m-O(m)]\) initial frames.  Down to the square-root density this
makes the same-row diagonal exponentially small.  Thus, for the actual
ordinary catalogue, the sole new coin-free gate left by this audit is the
integrated degree-deficit part of \((\mathrm{ID})_T\).  The abstract example
in Section 5 proves that the factorial-floor input cannot be omitted or
replaced by distinct-row PSF.

## 1. Derivation of the exact child hazard

For a resource set \(A\), let

\[
                 {\cal E}_t(A)=\{g\in{\cal H}_t:g\cap A\ne\varnothing\}.
\]

Fix \(T\) and a current row \(F\supset T\).  A selected edge kills this
row nonterminally precisely when it avoids \(T\) and meets
\(F\setminus T\).  The family of such edges is

\[
                 {\cal E}_t(F)\setminus{\cal E}_t(T).
\tag{1.1}
\]

Reverse the event--row incidence sum.  If \(N_T=d_t(T)\), then the
nonterminal part of its generator is

\[
 \begin{aligned}
 {\cal L}^{\rm nt}_tN_T
 &=-\nu_t\sum_{F\supset T}
       |{\cal E}_t(F)\setminus{\cal E}_t(T)|\\
 &=-h_TN_T,
 \end{aligned}
\tag{1.2}
\]

which proves (0.2).  Terminal events meeting \(T\) send the stopped
coordinate to the cemetery and are favorable.

For every \(A\), (0.3) is equivalent to

\[
                         |{\cal E}_t(A)|
 =\sum_{x\in A}d_t(x)-J_t(A).
\tag{1.3}
\]

Since \(T\subset F\), subtracting (1.3) for \(T\) from that for \(F\)
gives

\[
 |{\cal E}_t(F)\setminus{\cal E}_t(T)|
 =\sum_{x\in F\setminus T}d_t(x)-[J_t(F)-J_t(T)].
\tag{1.4}
\]

There are \(b-1\) resources in \(F\setminus T\).  Substitute
\(d_t(x)=\Delta_t-(\Delta_t-d_t(x))\) into (1.4), average over
\(F\supset T\), and use \(\nu_t\Delta_t=1/r\).  This proves (0.4).
Both bracketed terms in (0.4) are nonnegative: the first by maximality of
\(\Delta_t\), and the second because

\[
 J_t(F)-J_t(T)
 =\sum_g\left[(|g\cap F|-1)_+-(|g\cap T|-1)_+\right]\ge0.
\]

Solving the scalar drift equation (1.2) proves (0.5).  Consequently

\[
 Z_T(t)={d_t(T)\over d_0(T)R_T(t)}
\tag{1.5}
\]

has zero predictable nonterminal drift; after terminal death is included
as absorption, it is a nonnegative local supermartingale.

## 2. Comparison with the compensated reference

This section distinguishes the two possible meanings of “coin-free.”

If compensation clocks

\[
                 \chi_t(x)={\Delta_t-d_t(x)\over r\Delta_t}
\tag{2.1}
\]

are actually present, their nonterminal contribution on \(F\setminus T\)
adds

\[
 {1\over r\Delta_t}\sum_{x\in F\setminus T}
       (\Delta_t-d_t(x))
\]

to the edge-only hazard.  It cancels the first sum in (0.4) exactly.  Thus
the compensated reference is

\[
 R_T^{\rm comp}(t)=u_t^{b-1}
 \exp\left[
 {1\over r}\int_0^t
 {1\over\Delta_sd_s(T)}
 \sum_{F\supset T}(J_s(F)-J_s(T))\,ds
 \right].
\tag{2.2}
\]

Before the profile pair-spread stop, the audited one-frame estimate gives

\[
                         J_s(F)\le {CA_2\Delta_s\over m u_s}.
\tag{2.3}
\]

Hence

\[
 0\le\log{R_T^{\rm comp}(t)\over u_t^{b-1}}
 \le\int_0^t{CA_2\over rmu_s}\,ds
 \le {CA_2\over mz}.
\tag{2.4}
\]

At \(z=m^{-1/2}(\log m)^B\), with \(B\) larger than the fixed
polylogarithmic loss, (2.4) is \(o(1)\).  Thus the child-reference
comparison is valid in the compensated process.  But the compensation
coin bracket remains and is not removed by an integrating factor.

In the literal edge-only process, (2.4) controls only the
\(J(F)-J(T)\) part.  If merely

\[
                         d_t(x)\ge(1-\delta_t)\Delta_t
\tag{2.5}
\]

on the displayed remainders, then (0.4) gives only

\[
 \log{R_T(t)\over u_t^{b-1}}
 \le {b-1\over r}\int_0^t\delta_s\,ds+{CA_2\over mz}.
\tag{2.6}
\]

Thus \(R_T=(1+o(1))u^{b-1}\) requires
\(\int_0^T\delta_sds=o(1)\), not just \(\sup_s\delta_s=o(1)\).
Over \(T=\Theta(r\log(1/z))\), a pointwise error
\(\delta=m^{-c}\), \(c<1\), allows an exponent
\(\Theta(m^{1-c}\log m)\).  PSF does not alter this arithmetic.

## 3. Active mass and weighted mean

At time zero every row through \(S\) contains exactly \(b\) extensions,
so

\[
 \sum_a d_0(Sa)=b\,d_0(S),\qquad
 p_a={d_0(Sa)\over b\,d_0(S)},\qquad
 \sum_ap_a=1.
\tag{3.1}
\]

Let \(I_a\) be the survival indicator of the physical resource \(a\).  In
the edge-only process its deletion rate is \(\nu_td_t(a)\).  Therefore

\[
 {\cal L}_tP_S=-\nu_t\sum_ap_aI_ad_t(a).
\tag{3.2}
\]

Since \(u'_t=-u_t/r\), (3.2) proves (0.8).  The exact individual survival
reference is

\[
 \sigma_a(t)=\exp\left[-\int_0^t\nu_sd_s(a)\,ds\right]\ge u_t,
\tag{3.3}
\]

and \(I_a/\sigma_a\) is a local martingale.  Hence

\[
                         \sum_ap_a{I_a\over\sigma_a}
\tag{3.4}
\]

is the corrected active-mass martingale.  It is not \(P_S/u\), and its
denominators do not match the exact child-incidence identity below.

The proposed weighted-mean estimate itself is correct.  The current
incidence identity is

\[
                         \sum_a d_t(Sa)=b\,d_t(S).
\tag{3.5}
\]

Using \(R_{Sa}\ge u^{b-1}\), (3.1), and (3.5),

\[
 \begin{aligned}
 \sum_{a:I_a=1}p_aZ_{Sa}
 &= {1\over b d_0(S)}
    \sum_a{d_t(Sa)\over R_{Sa}}\\
 &\le {d_t(S)\over d_0(S)u^{b-1}}
 =u_tX_S(t),
 \end{aligned}
\tag{3.6}
\]

where \(X_S=d_t(S)/(d_0(S)u^b)\).  Hence, on
\(P_S\ge c_0u\) and \(X_S\le A_2\), the current weighted mean of the
\(Z_{Sa}\)'s is at most \(A_2/c_0\).

The reference comparison is nevertheless indispensable.  The natural
child coordinate is

\[
 X_{Sa}={d_t(Sa)\over d_0(Sa)u^{b-1}}
       =\Phi_{Sa}Z_{Sa},\qquad
 \Phi_{Sa}={R_{Sa}\over u^{b-1}}.
\tag{3.7}
\]

Thus \(X_{Sa}\ge A_3\) implies only
\(Z_{Sa}\ge A_3/\Phi_{Sa}\).  No fixed centered-energy charge follows
from (3.6) unless \(\Phi_{Sa}\) is bounded at the required scale.

### 3.1 The edge-only active-mass lower stop is nevertheless cheap

For the ordinary promotion-frame catalogue, put

\[
                         q_2(a,a')={d_0(a,a')\over D_0}.
\]

The exact pair table gives, uniformly over distinct physical resources,

\[
                         q_2(a,a')\le {C\over m^2}.       \tag{3.8}
\]

Indeed owner--owner pairs have maximum ratio \(2/m^2\), top--owner pairs
are superpolynomially smaller in the Gaussian regime, and two distinct
tops have codegree zero.  Also

\[
                         \max_ap_a\le {1\over b},         \tag{3.9}
\]

because \(d_0(Sa)\le d_0(S)\).

Stop before PPS, so that

\[
 d_t(a,a')\le A_2u_t^{-1}q_2(a,a')\Delta_t
 \qquad(a\ne a').                                      \tag{3.10}
\]

For an edge \(g\), let \(w_g=\sum_{a\in g}p_aI_a\).  The predictable
bracket of the martingale part of \(P_S/u\) is

\[
 {d\langle M\rangle_t\over dt}
 ={\nu_t\over u_t^2}\sum_gw_g^2.                        \tag{3.11}
\]

Expanding the square, the repeated-resource diagonal obeys

\[
 \nu_t\sum_ap_a^2I_ad_t(a)
 \le {1\over r}\sum_ap_a^2
 \le {1\over rb}.                                      \tag{3.12}
\]

For the off-diagonal, (3.8)--(3.10) give

\[
 \begin{aligned}
 \nu_t\sum_{a\ne a'}p_ap_{a'}I_aI_{a'}d_t(a,a')
 &\le {A_2\over ru_t}
       \sum_{a\ne a'}p_ap_{a'}q_2(a,a')\\
 &\le {CA_2\over rm^2u_t}.
 \end{aligned}                                         \tag{3.13}
\]

Integrating (3.11)--(3.13), using \(dt=-r\,du/u\), gives

\[
 \boxed{
 \mathbb E\langle M\rangle_{T_*}
 \le {z^{-2}-1\over2b}
      +{CA_2(z^{-3}-1)\over3m^2}=o(1)}                  \tag{3.14}
\]

at \(z=m^{-1/2}(\log m)^B\), provided \(B\) dominates the fixed
polylogarithmic exponent in \(A_2\).

By (0.8),

\[
                         {P_S(t)\over u_t}=1+M_t+A_t,
 \qquad A_t\text{ nondecreasing}.                       \tag{3.15}
\]

Thus \(\inf_{t\le T_*}P_S/u_t<1/2\) implies
\(\inf_{t\le T_*}M_t<-1/2\).  The \(L^2\) maximal inequality and
(3.14) yield

\[
 \boxed{
 \Pr\left(\inf_{t\le T_*}{P_S(t)\over u_t}< {1\over2}\right)=o(1).}
\tag{3.16}
\]

The same proof after marking an owner/root incidence sums directly to
\(o(W)\) exceptional incidence.  No jump-envelope hypothesis is needed:
the square bracket already pays rare large jumps.  Hence the fact that
\(P/u\) is not a martingale is a correction to the proposed proof, but it
is not the surviving ordinary-catalogue obstruction.

## 4. What whole-arm PSF actually controls

For one child \(T\), define the nonterminal decrement made by an edge
\(g\) by

\[
 B_T(g)=|\{F\supset T:g\cap T=\varnothing,
                    \ g\cap(F\setminus T)\ne\varnothing\}|.
\tag{4.1}
\]

For rows \(F,F'\supset T\), put

\[
 C_T(F,F')=\{g:g\cap T=\varnothing,
                 \ g\cap(F\setminus T)\ne\varnothing,
                 \ g\cap(F'\setminus T)\ne\varnothing\}.
\tag{4.2}
\]

Double counting gives the exact square identity

\[
 \boxed{
 \sum_gB_T(g)^2
 =\sum_{F,F'\supset T}|C_T(F,F')|.}
\tag{4.3}
\]

Suppose whole-arm PSF gives, for distinct rows,

\[
                         |C_T(F,F')|\le\kappa_t\Delta_t
                         \qquad(F\ne F').
\tag{4.4}
\]

The diagonal in (4.3) is

\[
 \sum_{F\supset T}|C_T(F,F)|
 =\sum_{F\supset T}|{\cal E}(F)\setminus{\cal E}(T)|
 ={h_Td_t(T)\over\nu_t}.
\tag{4.5}
\]

Therefore

\[
 \boxed{
 \nu_t\sum_gB_T(g)^2
 \le h_Td_t(T)+{\kappa_t\over r}d_t(T)(d_t(T)-1).}
\tag{4.6}
\]

The second term is the distinct-row PSF gain.  The first is the
unavoidable same-row death bracket.

For the centered child energy, dropping the favorable centering
subtraction gives the upper bound

\[
 Q_S^E(t)
 \le {\cal R}_S(t)
 +{\kappa_t\over r}\sum_ap_a Z_{Sa}(t)^2,
\tag{4.7}
\]

where

\[
 \boxed{
 {\cal R}_S(t)=
 \sum_ap_a h_{Sa}(t)
 {d_t(Sa)\over[d_0(Sa)R_{Sa}(t)]^2}.}
\tag{RD-density}
\]

Before the parent and child stops, (3.6) makes the second term in (4.7)
of the required order when
\(\kappa_t=O(A_H/(mu_t))\).  Nothing in PSF bounds
\({\cal R}_S\).

### 4.1 The ordinary catalogue pays the row diagonal factorially

For the special ordinary promotion-frame catalogue, \({\cal R}_S\) is
nevertheless negligible for a pair parent.  This follows from a uniform
lower bound on every nonempty physical triple link.

Put \(M=m+H\).  An ordinary frame is a directed cyclic order on an
\(M\)-set \(U\), together with its top \(U\) and all \(M\) cyclic
rank-\(m\) windows.  Equivalently, every owner in that frame has complement
in \(U\) equal to a cyclic \(H\)-interval.

### Lemma 4.1 (uniform compatible-triple factorial floor)

If a set \(T\) of three distinct physical resources is contained in at
least one ordinary frame, then

\[
 \boxed{
 d_0(T)\ge {\lfloor M/6\rfloor!^6\over M}
          =\exp[M\log M-O(M)].}                         \tag{4.8}
\]

#### Proof

Fix one witness frame with top \(U\) and directed cyclic order \(\pi\).
There is at most one top resource in \(T\); let the other \(q\le3\)
resources be owners.  Their complements in \(U\) are fixed cyclic
intervals \(I_1,\ldots,I_q\).

The membership vector

\[
                         (\mathbf1_{x\in I_1},\ldots,
                           \mathbf1_{x\in I_q})
\]

changes around \(\pi\) only at the two boundary cuts of each interval.
Hence the cycle is partitioned into at most \(2q\le6\) consecutive cells
of sizes \(n_1,\ldots,n_c\).  Permute the labels arbitrarily inside every
cell.  Each set \(I_j\) remains the same cyclic interval, so all resources
of \(T\) remain in the resulting frame.  These permutations produce at
least

\[
                         {1\over M}\prod_{i=1}^c n_i!
\tag{4.9}
\]

distinct directed cyclic orders modulo rotation; the factor \(M\) is a
deliberately crude bound on rotational duplication.

Among all partitions of \(M\) into at most six nonnegative parts, the
product of the factorials is minimized after splitting into six parts and
balancing them.  Splitting one part \(n=a+b\) cannot increase the product,
because \(a!b!\le n!\).  If \(a\ge b+2\), replacing \((a,b)\) by
\((a-1,b+1)\) multiplies the product by \((b+1)/a<1\).  Thus

\[
                         \prod_i n_i!\ge\lfloor M/6\rfloor!^6.
\]

This proves (4.8). \(\square\)

For a pair parent, a child triple has survival exponent

\[
                         b-1=r-3=M-2.
\]

Since \(R_T\ge u^{M-2}\), Lemma 4.1 gives, uniformly for \(u\ge z\),

\[
 \begin{aligned}
 \log[d_0(T)R_T]
 &\ge M\log M-O(M)+(M-2)\log z\\
 &\ge \left({1\over2}-o(1)\right)m\log m              \tag{4.10}
 \end{aligned}
\]

at \(z=m^{-1/2}(\log m)^B\).  In particular, for all sufficiently large
\(m\),

\[
                         d_0(T)R_T\ge e^{m\log m/3}.     \tag{4.11}
\]

Before the natural triple stop, \(Z_T\le X_T\le A_3\), because
\(R_T\ge u^{M-2}\).  Also \(h_T\le1\).  Therefore (RD-density) and
\(\sum_ap_a=1\) imply the pointwise bound

\[
 \boxed{
                         {\cal R}_S(t)
 \le A_3e^{-m\log m/3}.}                                \tag{4.12}
\]

After integration for \(T_*=O(m\log m)\), summation over marked pair
incidences, and multiplication by every polylogarithmic top-strip
multiplicity, (4.12) is still \(o(W/b)\).  Thus (RD) is proved with
exponential room for the actual ordinary catalogue.  This proof uses the
literal cyclic-frame multiplicity; PSF alone cannot replace it, as the
next section shows.

## 5. A literal row-diagonal counterexample

Fix integers \(r>k\ge1\), put \(b=r-k\ge2\), and fix \(D\ge2\).
Let \(S\) be a \(k\)-set.  Choose pairwise disjoint \(b\)-sets
\(B_1,\ldots,B_D\), disjoint from \(S\), and insert the \(D\) central
edges

\[
                         F_i=S\cup B_i.                  \tag{5.1}
\]

For every \(x\in\bigcup_iB_i\), add \(D-1\) private \(r\)-edges which
contain \(x\), avoid \(S\cup(\bigcup_jB_j\setminus\{x\})\), and whose
other vertices are fresh and used in no other edge.  Finally, add a
reservoir vertex \(z\) and \(D\) reservoir edges through \(z\), using
fresh outside vertices and otherwise disjoint from the construction.
The resulting hypergraph is simple and has maximum degree \(D\).  Every vertex
\(x\in\bigcup_iB_i\) and every vertex of \(S\) has degree exactly \(D\).

The parent and child codegrees are

\[
 d_0(S)=D,qquad d_0(Sx)=1,qquad
 p_x={1\over bD}.                                       \tag{5.2}
\]

There are \(bD\) such children, so their \(p\)-mass is one.  For
\(T=Sx\), where \(x\in B_i\), its link consists only of \(F_i\).  The
nonterminal edges which kill that row are precisely the private edges at
the \(b-1\) other vertices of \(B_i\), and hence

\[
 h_{Sx}(0)={(b-1)(D-1)\over rD},qquad
 {b-1\over r}-h_{Sx}(0)={b-1\over rD}.                  \tag{5.3}
\]

Thus the reference defect is only \(O(D^{-1})\).  Also, two distinct
central rows have no edge avoiding \(S\) which meets both of their
outside shores.  The distinct-row common-event/PSF quantity is zero.

Initially all normalized child coordinates are one and their centered
variance is zero.  Select one private edge at a vertex \(x\in B_i\).
The coordinate \(Sx\) is terminal and is removed.  Each of the other
\(b-1\) child links \(Sy\), \(y\in B_i\setminus\{x\}\), loses its
unique row and changes from one to zero.  All other child coordinates
remain one.

Put

\[
 p={1\over bD},\qquad
 P'=1-p,qquad w=(b-1)p.
\]

After exact recentering on the remaining active mass, the variance made by
this jump is

\[
                         \Delta V={w(P'-w)\over P'}
 ={(b-1)/(bD)\over1-1/(bD)}\left(1-{1\over D}\right).
\tag{5.4}
\]

There are \(bD(D-1)\) private edges, each of rate \(1/(rD)\).  Therefore
the exact variance generator at time zero is

\[
 \boxed{
 ({\cal L}V)(0)
 ={(b-1)(D-1)^2\over
    rD^2(1-1/(bD))}
 \ge {b-1\over4r}.}
\tag{5.5}
\]

For \(b\asymp r\), this is bounded away from zero.  The desired centered
Hilbert estimate is \(O((rb)^{-1})\), smaller by order \(m^2\).

The example also verifies that failure of the active-mass martingale is not
responsible for (5.5): all \(p\)-supported child resources have degree
\(D=\Delta\), so the right side of (0.8) is zero at time zero.  Taking
\(D\to\infty\) also makes the logarithmic reference discrepancy in (5.3)
arbitrarily small.  What remains is exactly the row diagonal (4.5).

The construction can be run with the stipulated adaptive rate
\(1/(r\Delta_t)\).  At
\(t_*=r\log A_3/(b-1)\), an intact central row gives all its \(b\)
children natural normalized value \(A_3\).  The event that none of the
\(D\) central clocks, none of the \(D\) reservoir clocks, and none of the
\(b(D-1)\) private clocks attached to that row rings before \(t_*\)
ensures both \(\Delta_t=D\) throughout the interval and survival of the
row and its protected parent.  Its probability is

\[
 \exp\left[-t_*\left({2\over r}+{b(D-1)\over rD}\right)\right]
 =A_3^{-[2+b(D-1)/D]/(b-1)}
 =A_3^{-1-o(1)}.                                         \tag{5.6}
\]

One can retain the parent and active-mass stops in this calculation.
Condition on the event \({\cal C}\) that no central or reservoir clock
rings before \(t_*\).  Its probability is

\[
                         \Pr({\cal C})=e^{-2t_*/r}
                         =A_3^{-2/(b-1)}=1-o(1).          \tag{5.7}
\]

Given \({\cal C}\), the \(bD\) outside resources have independent
exponential lifetimes of rate

\[
                         \lambda_x={D-1\over rD}.
\tag{5.8}
\]

The lifetime of one complete group \(B_i\) is therefore exponential of
rate \(\lambda_B=b\lambda_x\), independently over \(i\).  Put

\[
 q_*:=e^{-\lambda_Bt_*}
 =A_3^{-b(D-1)/(D(b-1))}=A_3^{-1-o(1)}.                 \tag{5.9}
\]

At \(t_*\), the crossing \(p\)-mass is exactly
\(D^{-1}\operatorname {Bin}(D,q_*)\).  Choose, for instance,
\(D=A_3^3\).  Chernoff's inequality then gives

\[
 \text{crossing }p\text{-mass}=(1+o(1))q_*
                         =A_3^{-1-o(1)}                 \tag{5.10}
\]

with probability \(1-o(1)\), conditional on \({\cal C}\).

The parent link count, divided by \(De^{-\lambda_Bt}\), is a nonnegative
martingale.  Moreover

\[
 {e^{-\lambda_Bt}\over u_t^b}
 =e^{bt/(rD)}\le A_3^{b/[D(b-1)]}=1+o(1)
 \qquad(0\le t\le t_*).                                \tag{5.11}
\]

Thus Doob's inequality shows that the probability the natural parent
coordinate crosses any \(A_2\to\infty\) before \(t_*\) is at most
\((1+o(1))/A_2=o(1)\).  Similarly, the active outside-resource count is
a binomial death process of rate \(\lambda_x\), and

\[
                         {e^{-\lambda_xt}\over u_t}
 =e^{t/(rD)}=1+o(1).                                    \tag{5.12}
\]

A geometric grid in \(e^{-\lambda_xt}\), Chernoff's inequality at the
grid points, and monotonicity between consecutive points give
\(P_S(t)\ge u_t/2\) for all \(t\le t_*\) with probability \(1-o(1)\).
Indeed the smallest binomial mean on this interval is
\(bD e^{-\lambda_xt_*}=bD(1-o(1))\), so a fixed-factor failure has
probability \(\exp[-\Omega(bD)]\) at each of only
\(O(\log A_3)\) geometric grid points.

Consequently (5.10) occurs before both auxiliary stops with probability
\(1-o(1)\).  It is not \(O((bA_3^2)^{-1})\).  Multiplication by the exact
incidence factor \(bq_k(S)\) leaves order
\(bA_3^{-1-o(1)}q_k(S)\).  This is the scalar Doob scale and does not
close when \(A_3=m^{o(1)}\).

This is a counterexample for the abstract adaptive-rate edge-only process.
It is not asserted to be an induced residual of the ordinary-promotion-frame
catalogue.  Equation (5.5), however, is already
a statewise counterexample to the claimed deduction of the Hilbert
diagonal from active-mass balance and distinct-row PSF.

There is one further scope qualification.  The reservoir deliberately
keeps \(\Delta_t=D\).  Therefore the long-time crossing calculation need
not remain inside an additional stop of the form
\(\Delta_t\asymp D_0u_t^{r-1}\).  The time-zero generator identity (5.5)
does lie at the perfectly regular monitored-support state and is unaffected
by this qualification.  Thus (5.5) refutes the proposed *pointwise
derivation* of the Hilbert diagonal, while (5.10) is an abstract-process
triple-stop counterexample, not an ordinary-frame trajectory obstruction.

## 6. The exact surviving theorem

The active-mass lower stop is proved in Section 3.1, and the row-diagonal
trace is proved in Section 4.1.  Thus, after granting the edge-only version
of whole-arm PSF, the one genuinely new hypothesis is:

\[
 \boxed{
 \text{outside }o(W)\text{ marked incidence},\qquad
 \sup_{T,t}\int_0^t\epsilon_T(s)\,ds=o(1).}
\tag{ID}
\]

Here \(T\) ranges over child triples of retained pair parents and
\(\epsilon_T\) is the exact quantity in (0.4).

### Theorem 6.1 (conditional coin-free Hilbert closure)

Assume PPS, the parent upper stop \(X_S\le A_2\), the edge-only
distinct-row whole-arm bound

\[
                         \kappa_t\le {CA_H\over mu_t},   \tag{6.1}
\]

and (ID), down to \(z=m^{-1/2}(\log m)^B\).  Choose the polylogarithmic
thresholds so that

\[
                         A_3\ge8A_2,qquad
                         {A_HA_2\log(1/z)\over A_3}=o(1).
\tag{6.2}
\]

Then the total PFS\(_3\)-stopped marked incidence is \(o(W)\).

#### Proof

By (3.16), outside \(o(W)\) incidence one has \(P_S\ge u/2\) throughout.
Equation (3.6) then bounds the current weighted mean of the child
coordinates \(Z_{Sa}\) by \(2A_2\).  Hypothesis (ID) gives

\[
                         X_{Sa}=(1+o(1))Z_{Sa}.           \tag{6.3}
\]

Hence a natural triple crossing \(X_{Sa}=A_3\) has centered displacement
at least \(A_3/2\).  Quarantining that coordinate removes at least
\(p_aA_3^2/4\) centered energy; this is the exact weighted deletion
identity (the additional factor \(P/(P-p_a)\) is at least one).

Before crossing, \(Z_{Sa}\le X_{Sa}\le A_3\), and (3.6) gives

\[
                         \sum_ap_aZ_{Sa}^2
 \le A_3\sum_ap_aZ_{Sa}\le A_2A_3u.                    \tag{6.4}
\]

Equations (4.7), (6.1), and (6.4) bound the distinct-row energy rate by

\[
                         {CA_HA_2A_3\over rm}.           \tag{6.5}
\]

Its integral is at most

\[
                         {CA_HA_2A_3\log(1/z)\over m}.
\tag{6.6}
\]

The same-row integral is exponentially smaller by (4.12).  Optional
stopping and the crossing charge therefore give

\[
 \mathbb E\sum_{a\ {m crossing}}p_a
 \le {CA_HA_2\log(1/z)\over mA_3}+e^{-\Omega(m\log m)}
 =o(1/b),                                                \tag{6.7}
\]

using \(b\sim m\) and (6.2).  Finally,

\[
                         q_3(Sa)=bq_2(S)p_a
\]

converts (6.7) into \(o(q_2(S))\) triple incidence.  Summing the marked
pair-parent occurrences proves \(o(W)\). \(\square\)

In the compensated interpretation, (ID) follows from (2.4), and the
active-mass martingale is exact.  The new diagonal is then the
compensation-coin bracket in addition to the selected-edge terms above.
In the literal coin-free interpretation there is no coin bracket, and
Sections 3.1 and 4.1 close the other two proposed gaps; (ID) remains.

The whole-arm theorem currently on file was proved for the compensated
process.  Theorem 6.1 deliberately treats its edge-only analogue as a
hypothesis.  Importing the compensated theorem verbatim would be a second
error: removing coins also changes the displayed-arm survival hazard by
the degree-deficit term in (0.4).

This is the precise proved/conditional boundary.  Exact hazard centering
removes first-order child drift; it does not remove either heterogeneity of
the survival reference or the same-row carré-du-champ.  The latter is cheap
only because ordinary compatible triples have the factorial reserve (4.8).
