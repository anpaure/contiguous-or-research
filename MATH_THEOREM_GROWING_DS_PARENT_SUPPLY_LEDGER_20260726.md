# Growing \(D_s\) parent packets: exact Catalan ledger and the active-density gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. The ledger

Put

\[
 C_n=\operatorname {Cat}_n={1\over n+1}{2n\choose n},
 \qquad
 \theta={C_r\over p},
 \qquad
 \delta_\theta={1\over2}-{1\over\theta}
                 ={\theta-2\over2\theta}.
\tag{0.1}
\]

Here \(\mathcal D_n\) denotes the set of size-\(n\) Dyck fillings, so
\(|\mathcal D_n|=C_n\).

At the first fatal scale, \(r\) is minimal with \(C_r\ge4p\).  Hence

\[
 4\le\theta<16-{24\over r+1},
 \qquad
 {1\over4}\le\delta_\theta<{7\over16},
\tag{0.2}
\]

and the certified plateau defect in one aligned size-\(r\) context is

\[
                         D_r(\theta)=\delta_\theta C_r.
\tag{0.3}
\]

Consider literal size-\(s\) packets aligned with the two boundaries of
that parent, in the separated-boundary range \(2s\le r\).  Their exact
maximum row-disjoint packing number is

\[
 \boxed{N_{r,s}=2C_{r-s}-C_sC_{r-2s}.}
\tag{0.4}
\]

Normalize this by the fraction of the \(C_r\) root rows covered:

\[
                         \lambda_{r,s}={C_sN_{r,s}\over C_r}.
\tag{0.5}
\]

A complete \(D_s\) path packet has \(C_s\) rows and \(2s+1\) cyclic
starts.  For one complete joint integral choice, let

\[
\begin{aligned}
 \alpha_{r,s}
  &= {\text{number of row-start occurrences that move a physical target}
       \over N_{r,s}(2s+1)C_s},\\
 \gamma_{r,s}
  &= {\text{actual cap descent}
       \over\text{number of physical target-moving occurrences}},
\end{aligned}
\tag{0.6}
\]

with the second ratio defined to be zero if its denominator is zero.
Thus \(0\le\alpha_{r,s},\gamma_{r,s}\le1\).  Full carriers, unaffected
backgrounds, target collisions, and the common choice across all packets
are included before these quantities are evaluated.  In particular,
\(\alpha\gamma\) is an exact factorization of one joint gain, not a
product of marginal estimates.

Here and below, “cap descent” means the nonnegative decrease
\((\operatorname {PCap}_{\rm before}
  -\operatorname {PCap}_{\rm after})_+\).

Moving one occurrence lowers the cap hinge by at most one.  Therefore a
necessary scalar condition for repairing (0.3) is

\[
 \boxed{
 \lambda_{r,s}(2s+1)\alpha_{r,s}\gamma_{r,s}
       \ge\delta_\theta.}
\tag{0.7}
\]

Equivalently, the average genuine useful gain per retained packet must
satisfy

\[
 \boxed{
 G_{r,s}\ge G_{r,s}^{\rm req}
       :={\delta_\theta C_r\over N_{r,s}}
       ={\delta_\theta C_s\over\lambda_{r,s}}.}
\tag{0.8}
\]

For \(s=o(r)\), set \(a_s=C_s/4^s\).  The exact Catalan asymptotics give

\[
\begin{aligned}
 \lambda_{r,s}
 &=a_s(2-a_s)
   \left(1+O\left({s\over r}+{1\over r-2s}\right)\right),\\
 a_s
 &={1\over\sqrt\pi s^{3/2}}
       \left(1-{9\over8s}+O(s^{-2})\right).
\end{aligned}
\tag{0.9}
\]

Consequently a literal bank requires

\[
 G_{r,s}^{\rm req}
 ={\delta_\theta4^s\over2-a_s}
   \left(1+O\left({s\over r}+{1\over r-2s}\right)\right)
\tag{0.10}
\]

and

\[
 \boxed{
 \alpha_{r,s}\gamma_{r,s}
 \ge {\delta_\theta\over(2s+1)a_s(2-a_s)}(1+o(1))
 ={\delta_\theta\sqrt\pi\over4}\sqrt s\,(1+o(1)).}
\tag{0.11}
\]

At the hard endpoint \(\theta\uparrow16\),

\[
 \boxed{
 G_{r,s}^{\rm req}={7\over32}4^s(1+o(1)),
 \qquad
 \alpha_{r,s}\gamma_{r,s}
 \ge {7\sqrt\pi\over64}\sqrt s\,(1+o(1)).}
\tag{0.12}
\]

The second constant is \(7\sqrt\pi/64=0.19386\ldots\).  Since
\(\alpha\gamma\le1\), no literal separated-parent construction with
\(s=s(m)\to\infty\) can repair the plateau, even under perfect signs and
perfect physical carriers.  This is an occurrence-count and
one-Lipschitz cap obstruction, not an entropy argument.

For fixed \(s\) and \(r\to\infty\), the absolute all-start capacity is

\[
                         f_s=(2s+1)a_s(2-a_s).
\tag{0.13}
\]

The sequence \(f_s\) is strictly decreasing, and

\[
                         f_{25}>{7\over16}>f_{26}.
\tag{0.14}
\]

Thus, at the hard endpoint, the idealized literal bank has enough raw
mass only for \(s\le25\).  This is necessary, not sufficient: it credits
all \((2s+1)C_s\) starts as active and perfectly useful.

For a genuinely growing seed, the escape condition is instead

\[
 \boxed{
 \lambda^{\rm act}_{r,s}\gamma_{r,s}
       \ge{\delta_\theta\over2s+1},
 \qquad
 \lambda^{\rm act}_{r,s}:=\lambda_{r,s}\alpha_{r,s}.}
\tag{0.15}
\]

Hence active root density must be \(\Omega(1/s)\), up to carrier
efficiency.  Literal alignment supplies only

\[
                   \lambda_{r,s}^{\rm lit}
                   \sim {2\over\sqrt\pi s^{3/2}},
\tag{0.16}
\]

so its minimum required density amplification is

\[
 \boxed{
 A_{\min}(s,\theta)
 ={ \delta_\theta\sqrt\pi
    \over4\alpha_{r,s}\gamma_{r,s}}
       \sqrt s\,(1+o(1)).}
\tag{0.17}
\]

At \(\theta\uparrow16\), the leading factor is
\(7\sqrt\pi/(64\alpha\gamma)\).  Density \(c/s\), rather than full
root density, is already enough at the scalar level precisely when

\[
                         2c\alpha\gamma>\delta_\theta
\tag{0.18}
\]

with a strict margin for exceptional terms.  What remains is to realize
that density and gain in one legal joint physical library.

## 1. Exact Catalan asymptotics

Stirling's expansion gives

\[
 \boxed{
 C_n={4^n\over\sqrt\pi n^{3/2}}
 \left(1-{9\over8n}+{145\over128n^2}+O(n^{-3})\right).}
\tag{1.1}
\]

Indeed,

\[
 {2n\choose n}={4^n\over\sqrt{\pi n}}
 \left(1-{1\over8n}+{1\over128n^2}+O(n^{-3})\right)
\tag{1.2}
\]

and

\[
 {1\over n+1}={1\over n}
   \left(1-{1\over n}+{1\over n^2}+O(n^{-3})\right).
\tag{1.3}
\]

The Catalan recurrence also gives the exact finite ratio

\[
 \boxed{
 {C_{r-s}\over C_r}
 =\prod_{j=0}^{s-1}{r+1-j\over2(2r-2j-1)}.}
\tag{1.4}
\]

When \(r-s\to\infty\), division of the two instances of (1.1) yields

\[
 {C_{r-s}\over C_r}
 =4^{-s}\left({r\over r-s}\right)^{3/2}
 \left[
 1-{9\over8}\left({1\over r-s}-{1\over r}\right)
       +O((r-s)^{-2})
 \right].
\tag{1.5}
\]

The analogous formula holds with \(2s\) in place of \(s\).  In
particular, if \(s=o(r)\),

\[
 {C_{r-s}\over C_r}
 =4^{-s}\left(1+O\left({s\over r}+{1\over r-s}\right)\right).
\tag{1.6}
\]

The factor \(4^{-s}\) alone is not the obstruction: it cancels against
the \(4^s\) rows in a packet.  The decisive residual factor is the
\(s^{-3/2}\) in \(C_s/4^s\).

## 2. Exact left-right packet overlap

A left-aligned packet is indexed by \(B\in\mathcal D_{r-s}\) and has
root rows

\[
                         \{TB:T\in\mathcal D_s\}.
\tag{2.1}
\]

A right-aligned packet is indexed by \(A\in\mathcal D_{r-s}\) and has
root rows

\[
                         \{AT:T\in\mathcal D_s\}.
\tag{2.2}
\]

Assume \(2s\le r\).  A row lying in both banks has the unique form

\[
                         T_iRT_j,
 \qquad
 T_i,T_j\in\mathcal D_s,\quad R\in\mathcal D_{r-2s}.
\tag{2.3}
\]

For fixed \(R\), the \(C_s\) left packets are indexed by \(RT_j\), the
\(C_s\) right packets by \(T_iR\), and every left packet meets every
right packet in the unique row \(T_iRT_j\).  Hence this conflict
component is \(K_{C_s,C_s}\).  Components belonging to distinct \(R\)'s
are disjoint.  A row-disjoint selection takes one complete shore from
each component, losing exactly \(C_s\) packets for each of the
\(C_{r-2s}\) middle fillings.  This proves (0.4).

This is the maximum independent literal bank.  If overlapping left and
right packets can be combined into a newly proved joint atom, its row
count and cap profile must be recomputed; (0.4) does not prohibit it.

To normalize (0.4), define

\[
\begin{aligned}
 \varepsilon_1
 &=-{9\over8}\left({1\over r-s}-{1\over r}\right)
      +O((r-s)^{-2}),\\
 \varepsilon_2
 &=-{9\over8}\left({1\over r-2s}-{1\over r}\right)
      +O((r-2s)^{-2}).
\end{aligned}
\tag{2.4}
\]

Then the two uses of (1.5) give

\[
 {N_{r,s}\over C_r}
 =4^{-s}\left[
 2\left({r\over r-s}\right)^{3/2}(1+\varepsilon_1)
 -a_s\left({r\over r-2s}\right)^{3/2}(1+\varepsilon_2)
 \right].
\tag{2.5}
\]

For \(s=o(r)\), this becomes

\[
 {N_{r,s}\over C_r}
 =4^{-s}(2-a_s)
  \left(1+O\left({s\over r}+{1\over r-2s}\right)\right),
\tag{2.6}
\]

which proves (0.9).

There is also a uniform growing-seed conclusion.  If \(s\to\infty\),
\(2s\le r\), and \(r-s\to\infty\), then, even before subtracting
overlaps,

\[
 \lambda_{r,s}
 \le {2C_sC_{r-s}\over C_r}
 =O(s^{-3/2})
\tag{2.7}
\]

uniformly for \(s/r\le1/2\).  Thus

\[
                         (2s+1)\lambda_{r,s}=O(s^{-1/2})=o(1).
\tag{2.8}
\]

This proves the growing-seed failure throughout the separated-boundary
range, not merely along \(s=o(r)\).  No conclusion is drawn for
\(s>r/2\): there the boundary slabs overlap geometrically and (2.3) is
not the correct joint decomposition.

## 3. The physical cap-descent bound

Move one occurrence from a physical target \(X\) to a physical target
\(Y\).  With all unaffected load included in \(u_X,u_Y\), the hinge
change is

\[
 [(u_X-1-p)_++(u_Y+1-p)_+]
       -[(u_X-p)_++(u_Y-p)_+]\ge-1.
\tag{3.1}
\]

The same one-Lipschitz bound survives the outer positive part in PCap.
Process all moved occurrences of one complete legal factor choice in any
order.  If \(A\) occurrences actually change their target, total cap
descent is at most \(A\), even if packets collide at physical targets.

For the row-disjoint literal bank, the number of available occurrences at
one serviced depth is at most

\[
                         L_{r,s}=N_{r,s}(2s+1)C_s.
\tag{3.2}
\]

If \(A_{r,s}\) of these move a target and the actual total descent is
\(G_{r,s}^{\rm tot}\), definitions (0.6) give the identity

\[
 G_{r,s}^{\rm tot}
 =N_{r,s}(2s+1)C_s\alpha_{r,s}\gamma_{r,s}.
\tag{3.3}
\]

Comparison with (0.3) proves (0.7).  This argument does not select
different signs at different targets or depths.

If a packet's formal signed histogram has positive mass \(B_s\), its
physical useful gain is at most \(B_s\).  Carrier identifications can
cancel signed cells; negative mass can land below the residual hinge; and
positive mass can create overload elsewhere.  Hence every proposed local
profile must at least satisfy

\[
 \boxed{
 B_s\ge {\delta_\theta C_r\over N_{r,s}}
       ={\delta_\theta4^s\over2-a_s}(1+o(1)).}
\tag{3.4}
\]

This is only a necessary carrier-gain threshold.  Formal positive mass
above it is not a physical sign theorem.

## 4. Exact fixed-seed threshold

For fixed \(s\), let \(r\to\infty\).  The all-start normalized supply is
\(f_s\) from (0.13).  Since

\[
                         {a_{s+1}\over a_s}
                         ={2s+1\over2s+4},
\tag{4.1}
\]

one has

\[
 {f_{s+1}\over f_s}
 ={2s+3\over2s+4}{2-a_{s+1}\over2-a_s}<1.
\tag{4.2}
\]

Indeed, the last inequality is equivalent to

\[
                         2>a_s{8s+13\over2s+4},
\tag{4.3}
\]

which follows from \(a_s\le a_1=1/4\) and
\((8s+13)/(2s+4)<4\).  Thus \(f_s\) is strictly decreasing.

The hard-endpoint crossing is exact:

\[
\begin{aligned}
 16\cdot51\,C_{25}(2\cdot4^{25}-C_{25})
     &>7\cdot4^{50},\\
 16\cdot53\,C_{26}(2\cdot4^{26}-C_{26})
     &<7\cdot4^{52},
\end{aligned}
\tag{4.4}
\]

where

\[
 C_{25}=4861946401452,
 \qquad
 C_{26}=18367353072152.
\tag{4.5}
\]

These are precisely \(f_{25}>7/16>f_{26}\), proving (0.14).
For a fixed overshoot \(\theta\), the exact largest seed not excluded by
raw mass is

\[
 s_{\max}(\theta)
 =\max\{s:(2s+1)a_s(2-a_s)\ge\delta_\theta\}.
\tag{4.6}
\]

Moreover

\[
 f_s={4\over\sqrt{\pi s}}
       \left(1-{5\over8s}+O(s^{-3/2})\right).
\tag{4.7}
\]

Solving its leading term gives the useful approximation
\(s_{\max}\approx16/(\pi\delta_\theta^2)\); (4.6), not this
approximation, is authoritative in the present fixed range
\(1/4\le\delta_\theta<7/16\).

Thus literal alignment creates an upper, not a lower, seed-size gate.  A
separate geometric demand that \(s(m)\to\infty\) must be paired with a
density amplification outside the literal bank.

## 5. Minimum seed, density, and gain for an amplified atlas

Now let a legal atlas have \(N_{r,s}^*\) independently selectable
size-\(s\) atoms and put

\[
                         \lambda_{r,s}^*
                         ={C_sN_{r,s}^*\over C_r}.
\tag{5.1}
\]

Let \(\alpha^*,\gamma^*\) have the joint physical meanings in (0.6).
The three equivalent necessary thresholds are

\[
 \boxed{
\begin{aligned}
 \lambda_{r,s}^*
 &\ge {\delta_\theta\over(2s+1)\alpha^*\gamma^*},\\
 \alpha^*\gamma^*
 &\ge {\delta_\theta\over(2s+1)\lambda_{r,s}^*},\\
 G_{r,s}^*
 &\ge {\delta_\theta C_s\over\lambda_{r,s}^*}.
\end{aligned}}
\tag{5.2}
\]

These inequalities give the exact supply/demand ledger once an atlas and
its physical gain are specified.

Three regimes follow.

1. Literal alignment has
   \(\lambda^*\sim2/(\sqrt\pi s^{3/2})\), so it requires
   \(\alpha^*\gamma^*\sim(\delta_\theta\sqrt\pi/4)\sqrt s\).

2. Critical sparse suspension with \(\lambda^*\sim c/s\) has enough
   scalar mass exactly when

   \[
                         2c\alpha^*\gamma^*>\delta_\theta
   \tag{5.3}
   \]

   with a strict margin.  At the hard endpoint this is
   \(c\alpha^*\gamma^*>7/32\).

3. Root-dense suspension with \(\lambda^*\to\lambda_0>0\) needs only

   \[
   \alpha^*\gamma^*
      \ge{\delta_\theta\over(2s+1)\lambda_0},
   \qquad
   G_{r,s}^*\ge{\delta_\theta\over\lambda_0}C_s.
   \tag{5.4}
   \]

Thus root density is more than scalar capacity requires.  The critical
scale is active density times carrier efficiency of order \(1/s\).
More generally, if
\(\lambda^*\alpha^*\gamma^*\asymp s^{-\beta}\), a growing seed is
scalar-feasible for \(\beta<1\), constant-critical for \(\beta=1\), and
fails by occurrence conservation for \(\beta>1\).

If a construction has normalized exceptional loss \(\varepsilon_m\), its
exact minimum admissible seed is

\[
 s_{\min}(m)
 =\min\left\{s:
 2s\le r,\quad
 (2s+1)\lambda_{r,s}^*\alpha_{r,s}^*\gamma_{r,s}^*
       \ge\delta_\theta+\varepsilon_m
 \right\}.
\tag{5.5}
\]

There is no construction-independent numerical \(s_{\min}\): it depends
on the proved density and physical gain.  For a root-dense lower bound
\(\lambda^*\ge\lambda_0\) and joint efficiency
\(\alpha^*\gamma^*\ge\eta_m\), (5.5) is guaranteed by

\[
 s\ge {1\over2}
       \left({\delta_\theta+\varepsilon_m\over\lambda_0\eta_m}-1\right).
\tag{5.6}
\]

For critical density \(c/s\) with a fixed strict margin in (5.3), scalar
capacity imposes no growth rate beyond \(s(m)\to\infty\) and
\(2s(m)\le r(m)\); the actual minimum is then set by the atlas's geometric
error term.

By contrast, literal alignment has the asymptotic upper gate

\[
 s\lesssim
 \left({4\alpha\gamma\over\delta_\theta\sqrt\pi}\right)^2,
\tag{5.7}
\]

so it cannot support any \(s(m)\to\infty\).

## 6. Full-dimensional and hereditary PCap ledger

The number of aligned size-\(r\) contexts in semilength \(m\) is

\[
                     H_{m,r}={1\over2}{2(m-r)\choose m-r}.
\tag{6.1}
\]

With \(W={2m+1\choose m}\), Catalan and central-binomial asymptotics give,
uniformly for \(r=o(m)\),

\[
 \boxed{
 {H_{m,r}C_r\over W}
 ={1\over4\sqrt\pi r^{3/2}}
 \left(1+O\left({1\over r}+{r\over m}\right)\right).}
\tag{6.2}
\]

Thus the certified one-depth defect is

\[
 H_{m,r}D_r(\theta)
 ={\delta_\theta\over4\sqrt\pi}
 {W\over r^{3/2}}
 \left(1+O\left({1\over r}+{r\over m}\right)\right).
\tag{6.3}
\]

The literal all-start supply at that depth is at most

\[
 H_{m,r}C_rf_s
 =\left({1\over\pi}+o(1)\right)
 {W\over r^{3/2}\sqrt s},
\tag{6.4}
\]

when \(s=o(r)\).  Its supply/demand ratio is therefore

\[
 {4\over\delta_\theta\sqrt{\pi s}}(1+o(1)),
\tag{6.5}
\]

which is \(64/(7\sqrt{\pi s})(1+o(1))\) at the hard endpoint.

For the hereditary version, let \(I\) be a set of serviced depths and
let \(d_q\) be the certified defect per aligned context at depth \(q\).
Let \(G_I\) be the actual total cap gain, across all \(H_{m,r}\) contexts
and all \(q\in I\), of one common legal integral packet choice.  Necessarily

\[
                         G_I\ge H_{m,r}\sum_{q\in I}d_q.
\tag{6.6}
\]

Let \(A_I\) be the total number of physical target-moving occurrences of
that same choice, and define

\[
\begin{aligned}
 \bar\alpha_I
 &= {A_I\over
 H_{m,r}N_{r,s}(2s+1)C_s|I|},\\
 \Gamma_I
 &=\begin{cases}G_I/A_I,&A_I>0,\\0,&A_I=0,\end{cases}\\
 \bar\delta_I
 &= {1\over |I|C_r}\sum_{q\in I}d_q.
\end{aligned}
\tag{6.7}
\]

Then (6.6) requires the exact joint inequality

\[
 \boxed{
 \lambda_{r,s}(2s+1)\bar\alpha_I\Gamma_I
       \ge\bar\delta_I.}
\tag{6.8}
\]

Repetition through many hereditary depths does not repair a deficient
constant: demand and available row-start mass acquire the same factor
\(|I|\).  The packet state is common at every depth, so separately optimal
depthwise signs or carrier gains may not be added.  Only the joint
\(G_I\), and hence the joint \(\Gamma_I\), is legitimate.

For a strict-interior packet on the invisible hereditary source chain,
the physical carrier map sends every local state to the same exterior
target.  Then \(A_I=0\), and hence \(\bar\alpha_I=0\), irrespective of
the density of internal fringe packets.  Dense internal occurrence is
not active occurrence.  Positive supply must come from boundary-active
packets or from a separately proved joint atom transporting source load
to a boundary.

If exceptional backgrounds, crossing collisions, or unserviced source
incidences contribute an error \(E_{m,r}\), a strict repair needs

\[
 \lambda_{r,s}^*(2s+1)\bar\alpha_I\Gamma_I
 \ge \bar\delta_I+
 {E_{m,r}\over |I|H_{m,r}C_r}.
\tag{6.9}
\]

This is the quantitative target for a future joint packet theorem.  The
full carrier/background loss is inside \(\Gamma_I\); a count of nominal
packet states cannot replace it.

## 7. Check against the certified \(D_4\) constants

For \(s=4\), \(C_4=14\), and

\[
 \lim_{r\to\infty}{N_{r,4}\over C_r}={249\over32768},
 \qquad
 \lim_{r\to\infty}\lambda_{r,4}={1743\over16384}.
\tag{7.1}
\]

At \(\theta\uparrow16\), the required useful gain per packet is

\[
 \boxed{
 G_4^{\rm req}
 ={7/16\over249/32768}
 ={14336\over249}=57.574\ldots .}
\tag{7.2}
\]

The six-unit marked bridge and aggregate positive masses \(19\) and \(22\)
are therefore insufficient even before backgrounds.  The formal
start-resolved envelope \(60\) is above (7.2), but it must retain at least

\[
                         {14336/249\over60}
                         ={14336\over14940}
                         =0.95957\ldots
\tag{7.3}
\]

of its formal value after the complete joint carrier calculation.

In the all-start normalization, a \(D_4\) packet has
\(9\cdot14=126\) occurrences.  Condition (0.7) becomes

\[
                         \alpha\gamma
                         \ge {7168\over15687}
                         =0.4569\ldots .
\tag{7.4}
\]

The sixty-unit envelope supplies at most \(60/126=10/21\) in this
normalization, explaining its small scalar margin.  Thus a growing packet
must improve the active root density from \(s^{-3/2}\) to at least
\(s^{-1}\); merely enlarging the Catalan seed does not improve the ledger.

## 8. Exact remaining theorem

The scalar ledger leaves one precise constructive route.  For some
\(s=s(m)\to\infty\), \(2s\le r\), construct a product-compatible
parent atlas such that

1. its independently selectable boundary-active atoms have root density
   \(\lambda_{r,s}^*\ge(c+o(1))/s\);
2. one common integral choice across all protected depths has active
   fraction \(\bar\alpha_I\) and full physical carrier efficiency
   \(\Gamma_I\) satisfying

   \[
                         2c\bar\alpha_I\Gamma_I
                         >\sup_I\bar\delta_I;
   \tag{8.1}
   \]

3. all crossing collars, overlapping atoms, unaffected backgrounds, and
   exceptional incidences have total normalized loss smaller than the
   strict margin in (8.1).

Under these hypotheses, (6.9) beats the hereditary plateau/PCap defect.
Literal parent alignment fails the density requirement by the exact
Catalan ledger.  Strict-interior dense fringe suspension fails the
active-occurrence requirement on the hereditary source chain.  Neither
statement excludes a boundary-active dense suspension, a legal
overlapping multistate atom, or a packet with \(s>r/2\).  Those require
new geometry, not an entropy comparison.
