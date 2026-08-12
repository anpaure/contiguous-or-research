# Multiscale bottom-up component routing: exact supply, PCap demand, and physical-bin collapse

## 0. Verdict

Let

\[
 s=\min\{t:\operatorname{Cat}_t\ge p\},\qquad
 \alpha=\frac{\operatorname{Cat}_s}{p}.
\]

Then

\[
 1\le\alpha<4-\frac6{s+1},
\]

and the fatal scale \(r=\min\{t:\operatorname{Cat}_t\ge4p\}\) is either
\(s+1\) or \(s+2\).

At every scale \(t\), the bounded \(s_1\)-overlay components have three
different quantitative ledgers:

\[
\begin{array}{c|c}
\text{quantity per parent}&\text{asymptotic fraction of }\operatorname{Cat}_t\\ \hline
\text{number of selectable components}&1/12\\
\text{rows on their old shore}&3/8\\
\text{marked source-target mass actually transported}&1/8.
\end{array}                                             \tag{0.1}
\]

There are

\[
 H_{m,t+1}=\frac12\binom{2(m-t-1)}{m-t-1}
\]

aligned size-\(t+1\) parent contexts.  Thus the marked supply at scale
\(t\) is

\[
 S_t^{\rm mark}
 =\left(\frac1{128\sqrt\pi}+o(1)\right)
   \frac W{t^{3/2}},                                    \tag{0.2}
\]

whereas the certified plateau demand is

\[
 D_t^{\rm plat}
 =\left(\frac1{4\sqrt\pi}+o(1)\right)
   \left(\frac12-\frac1{\beta_t}\right)_+
   \frac W{t^{3/2}},
 \qquad
 \beta_t=\frac{\operatorname{Cat}_t}{p}.                \tag{0.3}
\]

At \(\beta_t=4\), marked supply is only \(1/8\) of demand.  Even crediting
every switched row with one perfect unit gives only \(3/8\) of demand.

More decisively, all the marked components at a fixed parent scale have
the same physical direction:

\[
              \operatorname{Cat}_j(e_3-e_2).
\]

Their intermediate labels are exactly refilled.  Every sequence of
even-pair coordinate-component switches preserves

\[
             \mu(2)+\mu(3)
             =\operatorname{Cat}_t+\operatorname{Cat}_{t-1}. \tag{0.4}
\]

Hence its unavoidable two-bin PCap is

\[
 \boxed{
 \bigl(\operatorname{Cat}_t+\operatorname{Cat}_{t-1}-2p\bigr)_+.} \tag{0.5}
\]

At the fatal scale \(\beta_t\ge4\), this is positive of order
\(\operatorname{Cat}_t\).  No number of component stages reduces it.

Bottom-up wrapping does not multiply target labels.  Port preservation
forces all coordinates of a completed child hole to disappear from the
next full-window intersection; only the new parent coordinate survives.
Thus four formal boundary labels at one scale are not four persistent
physical bins at the next.  For the distinguished parent target, the
coordinate-component move class has two physical bins, \(\{2,3\}\), not
\(4^h\).  It cannot accumulate sixteen physical targets without leaving
that move class and supplying a new parent-scale port factor whose
**full-window** target profile already has at least sixteen classes.

## 1. Catalan chronology from the \(p\)-scale

The exact Catalan ratios are

\[
 g_t:=\frac{\operatorname{Cat}_{t+1}}{\operatorname{Cat}_t}
      =\frac{2(2t+1)}{t+2}
      =4-\frac6{t+2},                                   \tag{1.1}
\]

and

\[
 q_t:=\frac{\operatorname{Cat}_{t-1}}{\operatorname{Cat}_t}
      =\frac{t+1}{2(2t-1)}
      =\frac14+O(t^{-1}).                               \tag{1.2}
\]

Minimality of \(s\) gives

\[
 \operatorname{Cat}_{s-1}<p\le\operatorname{Cat}_s,
\]

so

\[
 1\le\alpha
 <\frac{\operatorname{Cat}_s}{\operatorname{Cat}_{s-1}}
 =4-\frac6{s+1}.                                       \tag{1.3}
\]

For \(\ell\ge0\), put

\[
 \beta_{s+\ell}
 =\frac{\operatorname{Cat}_{s+\ell}}p
 =\alpha\prod_{u=s}^{s+\ell-1}g_u.                     \tag{1.4}
\]

Because \(\alpha<4\), the fatal scale is larger than \(s\).  Moreover
\(g_sg_{s+1}>4\) for all sufficiently large \(s\), so

\[
 r=
 \begin{cases}
 s+1,&\alpha g_s\ge4,\\
 s+2,&\alpha g_s<4.
 \end{cases}                                            \tag{1.5}
\]

Thus the proposed bottom-up construction has only one or two transitions
before it reaches the original fatal Catalan height.  Additional levels
move to heights approximately \(4^\ell\alpha p\); they do not create
extra phase capacity.

## 2. Exact parent-context normalization

Recall

\[
 H_{m,t}=\frac12\binom{2(m-t)}{m-t},
 \qquad
 W=\binom{2m+1}{m}.
\]

The exact consecutive ratio is

\[
 \frac{H_{m,t+1}}{H_{m,t}}
 =\frac{m-t}{2(2(m-t)-1)}
 =\frac14+o(1),                                         \tag{2.1}
\]

uniformly for \(t=O(\log p)=o(m)\).  Central-binomial and Catalan
asymptotics give

\[
 \frac{H_{m,t}\operatorname{Cat}_t}{W}
 =\left(\frac1{4\sqrt\pi}+o(1)\right)t^{-3/2},           \tag{2.2}
\]

and therefore

\[
 \frac{H_{m,t+1}\operatorname{Cat}_t}{W}
 =\left(\frac1{16\sqrt\pi}+o(1)\right)t^{-3/2}.          \tag{2.3}
\]

The factor \(1/4\) in (2.1) is essential: a parent-scale packet bank is
being compared with a child-hole plateau bank.

## 3. The three different \(s_1\)-component supplies

For the boundary coordinate swap \(s_1=(2\,3)\), the exact component law
at local scale \(t\) is

\[
 k_j=\operatorname{Cat}_j+\operatorname{Cat}_{j+1},
 \qquad
 n_j=\operatorname{Cat}_{t-j-2}.                        \tag{3.1}
\]

Choose \(J=J(t)\to\infty\) slowly enough that \(k_J=o(p)\).  The number of
bounded components is

\[
 N_t(J)=\sum_{j\le J}n_j
       =\left(\frac1{12}+o(1)\right)\operatorname{Cat}_t. \tag{3.2}
\]

Their total row support is

\[
\begin{aligned}
 V_t(J)
 &=\sum_{j\le J}k_jn_j\\
 &=\left(\frac38+o(1)\right)\operatorname{Cat}_t.        \tag{3.3}
\end{aligned}
\]

These are the usual \(1/12\) and \(3/8\) constants.

For the distinguished parent-window target, however, one component has
two arms.  Its \(\operatorname{Cat}_j\) child-fibre rows move

\[
                         2\longrightarrow z_j,
\]

while \(\operatorname{Cat}_j\) auxiliary rows move

\[
                         z_j\longrightarrow3.
\]

All other rows keep target \(z_j\).  Hence \(z_j\) is exactly refilled and
the signed marked ledger is

\[
                         \operatorname{Cat}_j(e_3-e_2). \tag{3.4}
\]

Summing (3.4) over the bounded components gives actual marked source mass

\[
\begin{aligned}
 M_t(J)
 &=\sum_{j\le J}
   \operatorname{Cat}_j\operatorname{Cat}_{t-j-2}\\
 &=\left(\frac18+o(1)\right)\operatorname{Cat}_t,        \tag{3.5}
\end{aligned}
\]

because

\[
 \sum_{j\ge0}\frac{\operatorname{Cat}_j}{4^{j+2}}
 =\frac1{16}C(1/4)=\frac18.                             \tag{3.6}
\]

Thus the \(3/8\) row mass is not \(3/8\) independent output mass.  Only
\(1/8\) leaves the source target, and every such unit enters the same
physical coordinate \(3\).

Multiplying by the parent contexts and using (2.3) gives

\[
\boxed{
\begin{aligned}
 S_t^{\rm mark}
 &=H_{m,t+1}M_t(J)
  =\left(\frac1{128\sqrt\pi}+o(1)\right)
     \frac W{t^{3/2}},\\
 S_t^{\rm row}
 &=H_{m,t+1}V_t(J)
  =\left(\frac3{128\sqrt\pi}+o(1)\right)
     \frac W{t^{3/2}}.
\end{aligned}}                                          \tag{3.7}
\]

The second line is an unrealistically generous bound which credits every
switched row with one useful unit.

## 4. Plateau demand at the same scale

At hole scale \(t\), the certified canonical plateau demand is

\[
 D_t^{\rm plat}
 =H_{m,t}\left(\frac{\operatorname{Cat}_t}{2}-p\right)_+
 =H_{m,t}\operatorname{Cat}_t
      \left(\frac12-\frac1{\beta_t}\right)_+.            \tag{4.1}
\]

By (2.2),

\[
 \boxed{
 \frac{D_t^{\rm plat}}W
 =\left(\frac1{4\sqrt\pi}+o(1)\right)
   \left(\frac12-\frac1{\beta_t}\right)_+
   t^{-3/2}.}                                           \tag{4.2}
\]

Whenever \(\beta_t>2\), the ideal supply ratios are

\[
 \boxed{
 \frac{S_t^{\rm mark}}{D_t^{\rm plat}}
 =\frac{\beta_t}{16(\beta_t-2)}+o(1),}                  \tag{4.3}
\]

and

\[
 \boxed{
 \frac{S_t^{\rm row}}{D_t^{\rm plat}}
 =\frac{3\beta_t}{16(\beta_t-2)}+o(1).}                 \tag{4.4}
\]

At \(\beta_t=4\), these are respectively \(1/8\) and \(3/8\).  As
\(\beta_t\uparrow16\), they decrease to \(1/14\) and \(3/14\).
Thus even the row-support fantasy has no same-scale constant surplus.

## 5. The invariant physical two-bin demand

The parent-window target \(2\) belongs to the two-point coordinate orbit

\[
                         \mathcal O=\{2,3\}
\]

under the even-pair automorphism group.  Every complete component switch
replaces rows by coordinate images.  Hence target-orbit mass is invariant
row by row and therefore globally:

\[
                         \mu_t(2)+\mu_t(3)
 =\operatorname{Cat}_t+\operatorname{Cat}_{t-1}.         \tag{5.1}
\]

The exact canonical loads are the two boundary Catalan counts

\[
                         \mu_t(2)=\operatorname{Cat}_t,
 \qquad
                         \mu_t(3)=\operatorname{Cat}_{t-1}. \tag{5.2}
\]

For any nonnegative loads on two bins with fixed total \(L\), their cap
tail is at least \((L-2p)_+\).  Therefore every factor reachable by any
number of even-pair coordinate-component stages satisfies, in one parent,

\[
 \boxed{
 K_{p,\mathcal O}
 \ge
 \bigl(\operatorname{Cat}_t+\operatorname{Cat}_{t-1}-2p\bigr)_+.} \tag{5.3}
\]

In normalized form this is

\[
 \operatorname{Cat}_t
 \left(1+q_t-\frac2{\beta_t}\right)_+.                  \tag{5.4}
\]

The necessary and sufficient numerical condition for the orbit even to
admit two loads at most \(p\) is

\[
 \beta_t\le\frac2{1+q_t}
 =\frac{4(2t-1)}{5t-1}
 =\frac85+O(t^{-1}).                                    \tag{5.5}
\]

Thus the bottom scale \(s\) is already impossible whenever
\(\alpha>8/5+o(1)\).  At the fatal scale \(\beta_t\ge4\), (5.5) fails by a
fixed factor.

Across aligned parents the unavoidable orbit tail is

\[
 R_t^{\rm orb}
 =H_{m,t+1}
   \bigl(\operatorname{Cat}_t+\operatorname{Cat}_{t-1}-2p\bigr)_+. \tag{5.6}
\]

Using (2.3),

\[
 \boxed{
 \frac{R_t^{\rm orb}}W
 =\left(\frac1{16\sqrt\pi}+o(1)\right)
   \left(1+q_t-\frac2{\beta_t}\right)_+
   t^{-3/2}.}                                           \tag{5.7}
\]

If physical target pairs from different parents collide, the lower bound
does not weaken: merging bins reduces available cap slots, and
\((x+y-p)_+\ge(x-p)_++(y-p)_+\).  Thus (5.6) is a valid optimistic lower
ledger for the coordinate-component move class.

At \(\beta_t\ge4\), both canonical loads in (5.2) exceed \(p\), since
\(q_t>1/4\).  Moving mass between \(2\) and \(3\) then preserves their
combined cap tail exactly.  The marked supply in (3.7) is transport, not
PCap reduction.

## 6. Multiscale sums

For a finite collection of scales \(\mathcal T\), suppose optimistically
that their parent-context banks and their serviced depth bands can be
treated disjointly.  Then

\[
 \boxed{
 \frac1W\sum_{t\in\mathcal T}S_t^{\rm mark}
 =\left(\frac1{128\sqrt\pi}+o(1)\right)
   \sum_{t\in\mathcal T}t^{-3/2},}                      \tag{6.1}
\]

while

\[
 \boxed{
 \frac1W\sum_{t\in\mathcal T}D_t^{\rm plat}
 =\left(\frac1{4\sqrt\pi}+o(1)\right)
   \sum_{t\in\mathcal T}
   \left(\frac12-\frac1{\beta_t}\right)_+t^{-3/2},}     \tag{6.2}
\]

and the invariant physical-orbit remainder is

\[
 \boxed{
 \frac1W\sum_{t\in\mathcal T}R_t^{\rm orb}
 =\left(\frac1{16\sqrt\pi}+o(1)\right)
   \sum_{t\in\mathcal T}
   \left(1+q_t-\frac2{\beta_t}\right)_+t^{-3/2}.}       \tag{6.3}
\]

For a bounded number of levels above \(s\), all \(t=(1+o(1))s\).  Hence
scale iteration adds supply and demand linearly in the number of levels;
there is no geometric supply amplification.  The factor \(4\) growth of
\(\operatorname{Cat}_t\) is cancelled by the factor \(1/4\) loss in the
number of parent contexts.

Equations (6.1)--(6.3) are favorable to the proposed scheme.  If context
banks or lower windows overlap, supplies cannot be summed independently
and must be grouped into joint atoms.  Plateau lower bounds from different
scales at the same depth likewise cannot simply be added; one may retain
the strongest one.  The pointwise orbit obstruction (5.3) needs no such
additivity.

On a protected depth interval of length \(L\), any plateau or orbit lower
bound which persists through that interval is multiplied by \(L\), up to
the negligible ambient correction \(W-N_q\).  Thus the same constant
deficit becomes a hereditary PCap deficit; changing scale does not dilute
it.

## 7. Why four-way labels do not become sixteen targets

A fibre of size \(d=\theta p\) requires at least

\[
                         b_{\min}=\left\lceil\frac d p\right\rceil
                         =\lceil\theta\rceil             \tag{7.0}
\]

physical bins if every bin is to have load at most \(p\).  Since
\(\theta<16\), the worst case requires sixteen bins.  Formal component or
boundary-profile labels count toward (7.0) only when they correspond to
distinct physical target sets in the same full-window histogram.

A component in layer \(j\) displays three local target names:

\[
                         2,\qquad z_j=2j+4,\qquad3.
\]

Its exact chronology is

\[
\begin{array}{c|c}
\text{mass}&\text{move}\\ \hline
\operatorname{Cat}_j&2\to z_j,\\
\operatorname{Cat}_j&z_j\to3,\\
\operatorname{Cat}_{j+1}-\operatorname{Cat}_j&z_j\to z_j.
\end{array}                                             \tag{7.1}
\]

Thus \(z_j\) is not an output bin: its incoming and outgoing masses are
equal.  Summing (7.1) leaves only
\(\operatorname{Cat}_j(e_3-e_2)\).  Varying \(j\), the suffix \(R\), or
the selected component creates many **labels** but no new physical
destination.

There is a second reset when scales are nested.  Let \(J_t\) be the
coordinate set of a completed size-\(t\) child hole.  Port preservation
fixes complementary boundary states

\[
                         O\cup P,\qquad
                         O\cup(J_t\setminus P).          \tag{7.2}
\]

Their intersection is exactly \(O\).  Every coordinate of \(J_t\),
including every target label created by a lower-scale routing stage, is
absent from one of the two ports.  Hence no child coordinate survives the
full child window when it is viewed from the next parent scale.

The next parent may introduce a new persistent coordinate and split it
between its two-point orbit, but it **replaces** the lower label rather
than adjoining an independent bit.  Consequently the physical-bin
recurrence for the distinguished full-window target is

\[
                         b_{t+1}\le2,                   \tag{7.3}
\]

not \(b_{t+1}=4b_t\) or even \(2b_t\).

The other boundary profiles of a local packet live at different window
cuts.  They are collateral histograms, not persistent state carried to the
next full-window target.  Counting them as four children of a routing node
conflates four signed profiles with four physical bins.

Therefore even six formal four-way stages do not produce sixteen physical
targets in the fatal fibre.  To obtain sixteen bins while preserving ports,
one needs a new size-\(t+1\) anchored factor whose **single full parent
window** already assigns its child roots to at least sixteen distinct
physical targets, each with load at most \(p\).  Such a factor may be
port-valid, but it is not generated by the coordinate-component hierarchy.

## 8. Final decision

The multiscale bottom-up proposal fails within the known coordinate
component move class.

* Catalan growth and parent-context decay cancel, so every scale supplies
  only \(\Theta(W/t^{3/2})\) marked mass.
* The \(3/8\) row-support constant hides the true \(1/8\) marked transport
  constant.
* All marked transport remains in the physical orbit \(\{2,3\}\), whose
  mass is invariant and whose PCap is already positive at the fatal scale.
* Port preservation erases lower-scale labels at the next full-hole
  boundary, so formal four-way labels do not multiply across scales.

Hence four-way labels cannot accumulate to sixteen effective physical
targets without introducing a genuinely new parent-scale port-transversal
factor which crosses the coordinate target-orbit invariant.  The required
object is not a deeper iteration of the existing \(s_i\)-component
switches; it is a one-scale physical target design with at least sixteen
full-window output classes and controlled collateral at every protected
depth.
