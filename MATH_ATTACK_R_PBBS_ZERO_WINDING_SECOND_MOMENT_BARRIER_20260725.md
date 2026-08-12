# PBBS zero-winding quotient returns: exact block rotation and the second-moment barrier

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, or web search
is used.

## 0. Verdict

Put

\[
 N=2m+1,
 \qquad
 B=\operatorname{Cat}_m,
 \qquad
 \Omega=\mathcal D_m.
\]

The even-time PBBS quotient map on Dyck words has the following literal
form.  Mark the first up-step which reaches the global maximum and write

\[
 D=P\,1\,R\,0\,S,                                      \tag{0.1}
\]

where the displayed zero is the first subsequent return to height zero.
Then

\[
 \boxed{\tau D=S\,1\,P\,0\,R},
 \qquad
 \boxed{d(D)=|S|+1}.                                  \tag{0.2}
\]

If an omitted coordinate has a zero-winding return after \(2s+1\) PBBS
steps, and \(D_h=\tau^hD\), then

\[
 \boxed{
   \sum_{h=0}^{s-1}d(D_h)=\delta(D_s),
   \qquad \delta(D_s)=|P_s|+1<N.}                    \tag{0.3}
\]

In fact the relevant first-passage variable is strictly decreasing, so a
zero-winding equality is automatically its first equality.  Thus zero
winding is an ordinary positive-integer first-passage equation, not merely a
congruence.

The literal word recursion gives more:

\[
 \boxed{s=\operatorname{ht}(D),\qquad d(D)=1.}       \tag{0.3a}
\]

Thus every zero-winding return is an equality case of the height-gap
theorem.  Combining this with the quotient edge budget proves the positive
but insufficient estimate

\[
 \boxed{
 \overline\nu^{(0)}_{\lceil A\sqrt m\rceil}
 =O_A\!\left(B\sqrt{\frac{\log m}{m}}\right),}       \tag{0.3b}
\]

where the superscript denotes zero winding only.  The required quotient
scale is \(o_A(B/N)\), so (0.3b) is still too large by
\(\Theta(\sqrt{m\log m})\).

The still stronger guess that the final descent must have length \(s\) is
false: for every \(t\ge0\),

\[
 D=(10)^t11100100
\]

has a zero-winding return at \(s=3\), height three, and final descent two.
Section 9 proves this symbolically and shows that \(\partial D=1100\), so
peak deletion does not repair the guess.

For an edge-disjoint quotient packing \(\mathcal P\), let \(E_I\) be the
\(s(I)\) consecutive quotient edges carrying the deficits in (0.3).  The
natural first- and second-moment ledgers are exactly

\[
 \sum_{I\in\mathcal P}\delta_I
 \le \sum_{D\in\Omega}d(D),                           \tag{0.4}
\]

and

\[
 \boxed{
 \sum_{I\in\mathcal P}{\delta_I^2\over s(I)}
 \le \sum_{D\in\Omega}d(D)^2.}                       \tag{0.5}
\]

The second inequality is Bessel's inequality for the normalized indicators
of the disjoint intervals.  Its centered version is

\[
 \boxed{
 \sum_{I\in\mathcal P}
 {\bigl(\delta_I-\mu s(I)\bigr)^2\over s(I)}
 \le \sum_{D\in\Omega}(d(D)-\mu)^2,}
 \qquad
 \mu={1\over B}\sum_D d(D).                         \tag{0.6}
\]

These estimates do **not** approach the residence gate.  In fact:

1. because \(d\ge1\), (0.4) is numerically weaker than the raw edge budget
   \(\sum_I s(I)\le B\);
2. the full Fourier-Bessel version, summed over all \(N\) spatial
   characters, collapses exactly to
   \[
      \sum_{I\in\mathcal P}{1\over s(I)}\le B,        \tag{0.7}
   \]
   which is again implied by the raw edge budget;
3. there is an absolute \(c>0\) such that, for all large \(m\),
   \[
   \sum_D d(D)\ge c\sqrt m\,B,
   \qquad
   \sum_D d(D)^2\ge c m^{3/2}B,
   \qquad
   \sum_D(d(D)-\mu)^2\ge c m^{3/2}B.                \tag{0.8}
   \]

Thus the scalar moments themselves carry macroscopic Catalan mass.  The
variance in (0.6) can control only intervals whose empirical deficit
\(\delta_I/s(I)\) is separated from \(\mu\); intervals near the mean are
completely invisible to it.

There is a second, independent square-root barrier.  For a fixed \(s\),
Fourier-Plancherel applied to the modular charge can bound one charge fibre
from collision information only at scale \(B/\sqrt N\), whereas the
quotient gate forced by fixed-window residence is \(o(B/N)\).  A proved
integer histogram construction shows that this square-root loss is sharp
for any argument using only the collision second moment.

Consequently the desired estimate

\[
 \nu_{\lceil A\sqrt m\rceil}(P_m)=o_A(B)              \tag{0.9}
\]

is not obtained.  What is proved is a precise no-go for the natural scalar
first moment, uncentered/centered Bessel, the all-character telescoping
bound, and charge-fibre collision second moment.  A successful proof must
use a signed higher correlation of the actual block rotation \(\tau\), or
a clustering theorem along its cycles; one-step deficit moments and
support orthogonality do not contain the missing \(1/N\) factor.

## 1. The quotient map as a literal block rotation

Use \(1\) for an up-step and \(0\) for a down-step.  For a Dyck word \(D\),
let its first step attaining its global maximum be the displayed \(1\) in

\[
 D=P\,1\,Q.
\]

Set

\[
 \delta(D)=|P|+1,
 \qquad
 \phi(D)=\overline Q\,0\,\overline P,                \tag{1.1}
\]

where the bar interchanges zero and one.

### Lemma 1.1 (one PBBS step)

The word \(\phi(D)\) is Dyck.  If \(u\in\mathbb Z_N\) is the coordinate of
the unmatched zero, one PBBS step is

\[
 (u,D)\longmapsto
 (u+\delta(D)\pmod N,\phi(D)).                       \tag{1.2}
\]

#### Proof

Let the marked up-step first reach height \(H\).  The old suffix \(Q\),
read from height \(H\), never rises above \(H\) and ends at height zero.
Therefore \(\overline Q\), read from zero, stays nonnegative and ends at
height \(H\).  The following zero lowers the height to \(H-1\).  Every
prefix of \(P\) has height at most \(H-1\), so \(\overline P\), read from
height \(H-1\), stays nonnegative and ends at zero.  Hence \(\phi(D)\) is
Dyck.

In the rooted cyclic word \(0D\), the PBBS parenthesis flip fixes the unique
unmatched zero and complements every bit of \(D\).  In
\(0\overline D\), the new unmatched zero is the complemented marked
up-step, at displacement \(|P|+1\).  Cutting immediately after it reads
\(\overline Q0\overline P\).  This proves (1.2). \(\square\)

Refine the marked factorization by taking the displayed zero to be the
first return to height zero after the marked step:

\[
 D=P\,1\,R\,0\,S.                                   \tag{1.3}
\]

The suffix \(S\) is Dyck.

### Theorem 1.2 (two-step block rotation)

For (1.3),

\[
 \boxed{
 \begin{aligned}
  \delta(D)&=|P|+1,\\
  \delta(\phi D)&=|R|+1,\\
  \tau D:=\phi^2D&=S\,1\,P\,0\,R.
 \end{aligned}}                                      \tag{1.4}
\]

Moreover, with \(d(D)=|S|+1\),

\[
 \delta(D)+\delta(\phi D)=N-d(D),                   \tag{1.5}
\]

and the even-time skew product is

\[
 \boxed{(u,D)\longmapsto(u-d(D)\pmod N,\tau D).}    \tag{1.6}
\]

#### Proof

Substitution in (1.1) gives

\[
 \phi D=\overline R\,1\,\overline S\,0\,\overline P.
\]

The word \(R\), read from height \(H\), stays between heights one and
\(H\) and ends at height one.  Hence \(\overline R\), read from zero,
stays between zero and \(H-1\) and ends at \(H-1\).  The displayed one is
therefore the first step of \(\phi D\) which reaches height \(H\).
The complemented Dyck word \(\overline S\), read from height \(H\), never
goes above \(H\); after the displayed zero, \(\overline P\) also remains
below \(H\).  Thus the displayed one is exactly the first maximum-reaching
step of \(\phi D\), and \(\delta(\phi D)=|R|+1\).

Applying (1.1) a second time gives

\[
 \phi^2D
 =\overline{\,\overline S0\overline P\,}\,0\,
   \overline{\overline R}
 =S1P0R.
\]

Finally,

\[
 |P|+1+|R|+1+|S|=2m=N-1,
\]

so (1.5) follows.  Reducing (1.5) modulo \(N\) in two applications of
(1.2) proves (1.6). \(\square\)

## 2. Zero winding and the exact Gaussian-window target

Put \(D_h=\tau^hD\), and factor every \(D_h\) as

\[
 D_h=P_h1R_h0S_h.
\]

After \(s\) even-time steps, (1.6) puts the spatial root at

\[
 u-\sum_{h=0}^{s-1}d(D_h)\pmod N.
\]

The following odd PBBS step moves it forward by \(\delta(D_s)\).

### Proposition 2.1 (zero-winding return equation)

An odd segment of length \(2s+1\) returns its omitted coordinate if and
only if, for one integer \(a\ge0\),

\[
 \sum_{h=0}^{s-1}d(D_h)=\delta(D_s)+aN.              \tag{2.1}
\]

It has zero winding exactly when \(a=0\).  In that case

\[
 \sum_{h=0}^{s-1}d(D_h)=\delta(D_s)<N,               \tag{2.2}
\]

and it is the first return exactly when

\[
 \sum_{h=0}^{j-1}d(D_h)\ne\delta(D_j)
 \qquad(0\le j<s).                                  \tag{2.3}
\]

#### Proof

The spatial displacement just computed is zero modulo \(N\) after the
final odd step precisely when the two sides of (2.1) are congruent.  The
left side is positive and \(1\le\delta(D_s)<N\).  Their difference is
strictly larger than \(-N\), so the congruent multiple is \(aN\) with
\(a\ge0\).  This proves (2.1).  When \(a=0\), positivity makes every proper
partial sum smaller than the final sum and hence smaller than \(N\).
Therefore every earlier modular equality is an ordinary equality, proving
(2.3). \(\square\)

There is a stronger sign statement which uses the second factorization in
each pair of PBBS steps.

### Theorem 2.2 (strict first-passage sign and the dual ledger)

Put

\[
 a_j=\delta(D_j),
 \qquad c_j=d(D_j),
 \qquad \widehat c_j=d(\phi D_j),
\]

and define

\[
 Y_j=a_j-\sum_{h=0}^{j-1}c_h.                       \tag{2.4}
\]

Then

\[
 \boxed{Y_{j+1}-Y_j=-\widehat c_j<0}                \tag{2.5}
\]

and hence

\[
 \boxed{Y_j=a_0-\sum_{h=0}^{j-1}\widehat c_h.}      \tag{2.6}
\]

Consequently a zero-winding return at time \(s\) satisfies the two exact
positive ledgers

\[
 \boxed{
 \sum_{h=0}^{s-1}c_h=a_s,
 \qquad
 \sum_{h=0}^{s-1}\widehat c_h=a_0,}                 \tag{2.7}
\]

and

\[
 Y_0>Y_1>\cdots>Y_{s-1}>Y_s=0.                     \tag{2.8}
\]

In particular, every zero-winding equality is automatically a first return;
the separate inequalities in (2.3) need not be checked.

#### Proof

Write \(b_j=\delta(\phi D_j)\).  The two-step voltage identity (1.5),
first at \(D_j\) and then at \(\phi D_j\), gives

\[
 c_j=N-a_j-b_j,
 \qquad
 \widehat c_j=N-b_j-a_{j+1}.                        \tag{2.9}
\]

Therefore

\[
 Y_{j+1}-Y_j
 =a_{j+1}-a_j-c_j
 =a_{j+1}+b_j-N
 =-\widehat c_j.
\]

Every deficit is a positive odd integer, so the decrease is strict.  This
proves (2.5)-(2.6).  Zero winding says \(Y_s=0\), and (2.6) gives the second
identity in (2.7).  Strict decrease then gives (2.8), proving the final
claim. \(\square\)

The sign identity can be upgraded to a literal word statement.

### Theorem 2.3 (zero winding is exact height equality)

If \(D_0\) has a zero-winding return at time \(s\), then

\[
 \boxed{s=\operatorname{ht}(D_0),
 \qquad d(D_0)=1.}                                  \tag{2.10a}
\]

More precisely, if \(C_j=\sum_{h<j}d(D_h)\), then

\[
 \boxed{
 P_s=S_{s-1}1S_{s-2}1\cdots S_1 1S_0.}             \tag{2.10b}
\]

Thus every zero-winding gap is an equality case of the height-gap bound:

\[
 \boxed{2s+1=2\operatorname{ht}(D_0)+1.}            \tag{2.10c}
\]

#### Proof

By Theorem 2.2, \(C_j<a_j=|P_j|+1\) for \(j<s\).  For \(1\le j\le s\),
let \(A_j\) be the prefix of \(D_j\) of length \(C_j-1\).  Since

\[
 D_{j+1}=S_j1P_j0R_j,
 \qquad
 C_{j+1}=C_j+|S_j|+1,
\]

the prefix relation is

\[
 A_{j+1}=S_j1A_j.                                   \tag{2.11}
\]

The base case is \(A_1=S_0\).  At the zero-winding hit,
\(C_s=a_s=|P_s|+1\), so \(A_s=P_s\).  Iterating (2.11) proves (2.10b).

Every \(S_j\) is Dyck and hence has total height zero.  The right side of
(2.10b) contains exactly \(s-1\) displayed up-steps, so \(P_s\) ends at
height \(s-1\).  The marked next up-step is the first step reaching the
global height of \(D_s\); therefore

\[
 \operatorname{ht}(D_s)=s.                         \tag{2.12}
\]

The one-step proof in Lemma 1.1 also shows that \(\phi\) preserves global
height: the displayed step in \(\phi D\) reaches the old height, and every
other part remains at or below it.  Hence \(\tau=\phi^2\) preserves height,
and (2.12) gives \(\operatorname{ht}(D_0)=s\).

Finally, immediately before the terminal block \(S_0\) on the right side
of (2.10b), the path is already at height \(s-1\).  If \(S_0\) were
nonempty, its first step would reach height \(s\) before the marked step of
\(D_s\), contradicting the definition of that marked step.  Thus
\(S_0=\varnothing\), so \(d(D_0)=|S_0|+1=1\).  This proves (2.10a) and
(2.10c). \(\square\)

### Corollary 2.4 (direct height/edge split)

Let \(\mathcal P\) be an edge-disjoint zero-winding quotient family, and
let every member have \(s_I\le H\).  For every integer \(1\le L<H\),

\[
 \boxed{
 |\mathcal P|
 \le A_L(m)+{B\over L+1},}                          \tag{2.13a}
\]

where \(A_L(m)\) is the number of semilength-\(m\) Dyck paths of height at
most \(L\).  Consequently, uniformly for fixed \(A>0\) and
\(H=\lceil A\sqrt m\rceil\),

\[
 \boxed{
 |\mathcal P|=O_A\!\left(B\sqrt{\frac{\log m}{m}}\right).} \tag{2.13b}
\]

#### Proof

By Theorem 2.3, intervals with \(s_I\le L\) have distinct start roots of
height at most \(L\), so there are at most \(A_L(m)\) of them.  Every other
interval uses at least \(L+1\) of the pairwise disjoint deficit-carrying
quotient edges, so there are at most \(B/(L+1)\) of those.  This proves
(2.13a).

The path-graph spectral radius gives

\[
 A_L(m)\le\left(2\cos{\pi\over L+2}\right)^{2m}
 \le4^m\exp\left(-{\pi^2m\over(L+2)^2}\right).      \tag{2.14}
\]

Take \(L=\lfloor(\pi/4)\sqrt{m/\log m}\rfloor\).  Then the first term in
(2.13a) is \(O(4^m m^{-8})=o(B/m)\), while the second is
\(O(B\sqrt{\log m/m})\).  For every fixed \(A>0\), this \(L\) is below
\(H\) for all sufficiently large \(m\), proving (2.13b). \(\square\)

Two immediate consequences of zero winding are

\[
 s\le\delta(D_s)<N,
 \qquad
 {1\over s}\sum_{h<s}d(D_h)={\delta(D_s)\over s}
 \le {N-1\over s}.                                  \tag{2.15}
\]

Thus for \(s\asymp\sqrt m\), the empirical deficit is only forced onto the
natural \(O(\sqrt m)\) scale.  Equation (2.15) contains no extra \(1/N\)
rarity.

Now let \(\mathcal P\) be an edge-disjoint family of nonwrapping quotient
return intervals.  Each quotient interval has all \(N\) spatial lifts, and
the lifts of an edge-disjoint quotient family are pairwise disjoint: above
each quotient edge, distinct spatial phases are distinct physical edges.
Consequently

\[
 \nu_H(P_m)\ge N|\mathcal P|.                       \tag{2.16}
\]

Therefore the fixed-window hypothesis

\[
 \nu_{\lceil A\sqrt m\rceil}(P_m)=o_A(B)            \tag{2.17}
\]

requires, on the long quotient cycles,

\[
 \boxed{|\mathcal P|=o_A(B/N).}                     \tag{2.18}
\]

This is the scale against which the moment estimates below must be judged.

## 3. Exact first, second, and centered ledgers

For \(I\in\mathcal P\), write \(s_I=s(I)\), list its deficit-carrying
edges as

\[
 E_I=\{D_I,\tau D_I,\ldots,\tau^{s_I-1}D_I\},
\]

and put \(\delta_I=\delta(\tau^{s_I}D_I)\).  Full interval
edge-disjointness implies that the sets \(E_I\) are pairwise disjoint.

### Proposition 3.1 (moment ledgers)

Every zero-winding packed family satisfies

\[
 \sum_I \delta_I\le M_1,\qquad
 \sum_I{\delta_I^2\over s_I}\le M_2,                \tag{3.1}
\]

where

\[
 M_1=\sum_{D\in\Omega} d(D),
 \qquad
 M_2=\sum_{D\in\Omega} d(D)^2.                     \tag{3.2}
\]

If \(\mu=M_1/B\) and

\[
 V=\sum_D (d(D)-\mu)^2,
\]

then

\[
 \sum_I{(\delta_I-\mu s_I)^2\over s_I}\le V.       \tag{3.3}
\]

#### Proof

Equation (2.2) and disjointness give

\[
 \sum_I \delta_I
 =\sum_I\sum_{D\in E_I} d(D)
 \le\sum_D d(D),
\]

which is the first inequality.

In \(\ell^2(\Omega)\), put

\[
 v_I={\mathbf1_{E_I}\over\sqrt{s_I}}.
\]

The vectors \(v_I\) are orthonormal.  Moreover,

\[
 \langle d,v_I\rangle={\delta_I\over\sqrt{s_I}}.
\]

Bessel's inequality proves the second inequality in (3.1).  Applying the
same argument to \(d-\mu\mathbf1\) gives

\[
 \langle d-\mu\mathbf1,v_I\rangle
 ={\delta_I-\mu s_I\over\sqrt{s_I}},
\]

and hence (3.3). \(\square\)

The first-passage theorem supplies the same ledgers at the initial endpoint.
Indeed, put

\[
 \widehat E_I=\{\phi D_I,\phi\tau D_I,
                  \ldots,\phi\tau^{s_I-1}D_I\}.
\]

Since \(\phi\) is a permutation and the \(E_I\)'s are disjoint, the
\(\widehat E_I\)'s are also disjoint.  The second identity in (2.7) and the
same proof give, with \(\alpha_I=\delta(D_I)\),

\[
 \sum_I \alpha_I\le M_1,
 \qquad
 \sum_I{\alpha_I^2\over s_I}\le M_2,
 \qquad
 \sum_I{(\alpha_I-\mu s_I)^2\over s_I}\le V.        \tag{3.4}
\]

Adding the two endpoint ledgers yields

\[
 \boxed{
 \sum_I(\alpha_I+\delta_I)\le2M_1,
 \qquad
 \sum_I{\alpha_I^2+\delta_I^2\over s_I}\le2M_2.}   \tag{3.5}
\]

Thus the exact first-passage sign doubles the available scalar information,
but it does not change its asymptotic moment scale.

The uncentered ledgers are already saturated at the formal level.  Since
\(d(D)\ge1\),

\[
 M_1\ge B,
 \qquad
 M_2\ge B.                                          \tag{3.6}
\]

Also \(\delta_I\ge s_I\).  Hence (3.1) gives only

\[
 \sum_I s_I\le M_1,
 \qquad
 \sum_I s_I\le M_2,                                \tag{3.7}
\]

whereas disjointness itself gives the stronger statement

\[
 \boxed{\sum_I s_I\le B.}                          \tag{3.8}
\]

The centered ledger has an exact and limited consequence.  For \(\eta>0\),
let

\[
 \mathcal P_\eta=
 \left\{I:\left|{\delta_I\over s_I}-\mu\right|\ge\eta\right\}.
\]

Then (3.3) gives

\[
 \boxed{\sum_{I\in\mathcal P_\eta}s_I\le {V\over\eta^2}.} \tag{3.9}
\]

It says nothing at all about the complementary, near-mean family.  Any use
of (3.9) on all zero-winding intervals therefore needs a new dynamical
statement excluding empirical means close to \(\mu\).  Such a statement is
not a moment consequence.

## 4. The all-character Fourier-Bessel bound collapses exactly

The preceding Bessel inequality is the small-frequency form of a seemingly
stronger family.  Fix

\[
 \zeta=e^{2\pi i/N},
 \qquad 1\le k<N.
\]

For one interval \(I\), put

\[
 x_0=0,
 \qquad
 x_h=\sum_{j=0}^{h-1}d(\tau^jD_I)
 \qquad(1\le h\le s_I).
\]

Zero winding says \(x_{s_I}=\delta_I\).  Telescoping gives

\[
 \zeta^{k\delta_I}-1
 =\sum_{h=0}^{s_I-1}
   \zeta^{kx_h}\bigl(\zeta^{k d(\tau^hD_I)}-1\bigr). \tag{4.1}
\]

### Proposition 4.1 (character Bessel and exact collapse)

For every \(1\le k<N\),

\[
 \sum_{I\in\mathcal P}
 {\left|\zeta^{k\delta_I}-1\right|^2\over s_I}
 \le
 \sum_{D\in\Omega}\left|\zeta^{kd(D)}-1\right|^2.  \tag{4.2}
\]

Summing (4.2) over all \(k\) gives exactly

\[
 \boxed{\sum_{I\in\mathcal P}{1\over s_I}\le B.}    \tag{4.3}
\]

#### Proof

On the support \(E_I\), define

\[
 w_{I,k}(\tau^hD_I)=\zeta^{-kx_h}.
\]

The vectors \(w_{I,k}/\sqrt{s_I}\) are orthonormal because their supports
are disjoint.  Their inner products with the global vector

\[
 g_k(D)=\zeta^{kd(D)}-1
\]

are the telescoping sums (4.1).  Bessel's inequality proves (4.2).

For every integer \(a\) with \(0<a<N\), character orthogonality gives

\[
 \sum_{k=0}^{N-1}|\zeta^{ka}-1|^2=2N.               \tag{4.4}
\]

Both \(d(D)\) and \(\delta_I\) lie strictly between zero and \(N\).
Summing (4.2), using (4.4) on both sides, and cancelling \(2N\) proves
(4.3). \(\square\)

But (4.3) is implied by the raw edge budget (3.8), because
\(1/s_I\le s_I\).  Thus using every spatial character does not recover
even one new power of \(m\); it collapses to a weaker consequence of
packedness.  This is an exact orthogonality no-go, not an asymptotic
estimate.

## 5. The actual deficit moments contain macroscopic Catalan mass

The weakness above is not caused by a crude estimate of \(M_1,M_2,V\).
The PBBS deficit itself has large moments.  We prove this using only Dyck
path counting.

There is first an exact coefficient formula.  Let \(C_h(z)\) count Dyck
paths of height at most \(h\):

\[
 C_{-1}(z)=0,
 \qquad C_0(z)=1,
 \qquad C_h(z)={1\over1-zC_{h-1}(z)}.
\]

Let \(b_{m,j}\) be the number of \(D\in\mathcal D_m\) with
\(d(D)=2j+1\), and put

\[
 \mathcal B(x,y)=
 \sum_{m\ge1}\sum_{0\le j<m}b_{m,j}x^{m-j}y^j.
\]

### Proposition 5.1 (exact marginal-moment series)

One has

\[
 \boxed{
 \mathcal B(x,y)=
 \sum_{h\ge1}
 xC_{h-1}(x)\bigl(C_{h-1}(x)-C_{h-2}(x)\bigr)C_h(y).} \tag{5.0a}
\]

If \(L_y=2y\partial_y+1\), then for every integer \(q\ge0\),

\[
 \boxed{
 \sum_{m\ge1}\left(\sum_{D\in\mathcal D_m}d(D)^q\right)z^m
 =\left.(L_y^q\mathcal B(x,y))\right|_{x=y=z}.}      \tag{5.0b}
\]

In particular, (5.0b) with \(q=1,2\) is an exact formula for \(M_1,M_2\).

#### Proof

Decompose a nonempty Dyck path into primitive components, and let \(h\) be
its global height.  The components preceding the first component of height
\(h\) form an arbitrary Dyck path of height at most \(h-1\), counted by
\(C_{h-1}(x)\).  The distinguished primitive component is \(1E0\), where
\(E\) has exact height \(h-1\), and is counted by

\[
 x\bigl(C_{h-1}(x)-C_{h-2}(x)\bigr).
\]

The suffix after it is an arbitrary Dyck path of height at most \(h\),
counted by \(C_h(y)\).  This proves (5.0a).  On the monomial
\(x^{m-j}y^j\), the operator \(L_y\) acts by multiplication by \(2j+1\).
Applying it \(q\) times, then setting \(x=y=z\), proves (5.0b). \(\square\)

For \(h,n\ge0\), let

\[
 A_h(n)=\#\{D\in\mathcal D_n:\operatorname{ht}(D)\le h\}.
\]

### Lemma 5.2 (two height populations on comparable sizes)

There are absolute constants \(\kappa,c_0>0\) such that, for all
sufficiently large \(m\), if

\[
 L=\lfloor\kappa\sqrt m\rfloor
\]

and \(m/3\le n\le2m/3\), then

\[
 A_{L-1}(n)\ge c_0\operatorname{Cat}_n,
 \qquad
 \operatorname{Cat}_n-A_{L-1}(n)
 \ge {1\over2}\operatorname{Cat}_n.                \tag{5.1}
\]

#### Proof

Dyck paths of height at most \(h\) are length-\(2n\) returns to zero in
the path graph on \(\{0,1,\ldots,h\}\).  Diagonalizing that graph gives

\[
 A_h(n)=
 {2\over h+2}\sum_{j=1}^{h+1}
 \sin^2{j\pi\over h+2}
 \left(2\cos{j\pi\over h+2}\right)^{2n}.           \tag{5.2}
\]

All summands are nonnegative.  Put \(q=L+1\) and keep the two terms
\(j=1,q-1\).  The elementary inequalities

\[
 \sin x\ge {2x\over\pi}\quad(0\le x\le\pi/2),
 \qquad
 \cos x\ge e^{-x^2}\quad(0\le x\le1)
\]

give

\[
 A_{L-1}(n)
 \ge c_\kappa {4^n\over m^{3/2}}.                  \tag{5.3}
\]

The standard Stirling bounds

\[
 c{4^n\over(n+1)^{3/2}}
 \le\operatorname{Cat}_n
 \le C{4^n\over(n+1)^{3/2}}                        \tag{5.4}
\]

and \(n\asymp m\) turn (5.3) into the first inequality of (5.1), with
some \(c_0=c_0(\kappa)>0\).

For the reverse estimate, pair the terms \(j\) and \(q-j\) in (5.2).
For \(1\le j\le q/2\),

\[
 \sin{j\pi\over q}\le {\pi j\over q},
 \qquad
 \left|\cos{j\pi\over q}\right|
 \le e^{-2j^2/q^2}.
\]

Therefore

\[
 A_{L-1}(n)
 \le {C4^n\over q^3}
      \sum_{j\ge1}j^2e^{-4nj^2/q^2}
 \le {C4^n\over m^{3/2}}
      \kappa^{-3}e^{-c/\kappa^2}.                  \tag{5.5}
\]

Choose the fixed \(\kappa>0\) sufficiently small that the last constant,
after division by the lower Stirling bound in (5.4), is at most \(1/2\).
This proves the second inequality. \(\square\)

### Lemma 5.3 (many macroscopic deficits)

There is an absolute \(c_1>0\) such that, for all large \(m\),

\[
 \#\left\{D\in\mathcal D_m:d(D)\ge {2m\over3}\right\}
 \ge c_1{B\over\sqrt m}.                            \tag{5.6}
\]

#### Proof

Let

\[
 \lceil m/3\rceil\le j\le\lfloor m/2\rfloor,
 \qquad n=m-j-1.
\]

Choose

\[
 E\in\mathcal D_n,
 \quad \operatorname{ht}(E)\ge L,
 \qquad
 S\in\mathcal D_j,
 \quad \operatorname{ht}(S)\le L-1,
\]

and form

\[
 D=1E0S.                                             \tag{5.7}
\]

The first primitive component \(1E0\) has height at least \(L+1\), while
the suffix \(S\) has height at most \(L-1\).  Hence the first primitive
component is the one which first attains the global maximum.  In (0.1),
the suffix is exactly \(S\), so

\[
 d(D)=2j+1\ge {2m\over3}.                            \tag{5.8}
\]

The first-return decomposition makes (5.7) injective.  Lemma 5.2 gives at
least

\[
 {c_0\over2}\operatorname{Cat}_{m-j-1}
                  \operatorname{Cat}_j              \tag{5.9}
\]

choices for each \(j\).  Since both indices in (5.9) are comparable to
\(m\), the Stirling bounds (5.4) give

\[
 \operatorname{Cat}_{m-j-1}\operatorname{Cat}_j
 \ge c{B\over m^{3/2}}.                             \tag{5.10}
\]

There are \(\Theta(m)\) allowed, disjoint values of \(j\).  Summing
(5.9)-(5.10) proves (5.6). \(\square\)

### Theorem 5.4 (first moment, second moment, and variance lower bounds)

There is an absolute \(c>0\) such that

\[
 \boxed{
 M_1\ge c\sqrt m\,B,
 \qquad
 M_2\ge c m^{3/2}B,
 \qquad
 V\ge c m^{3/2}B.}                                  \tag{5.11}
\]

#### Proof

The first two statements follow immediately from Lemma 5.3 by summing
\(d\) and \(d^2\) on the set in (5.6).

For the variance, every primitive Dyck path \(D=1E0\) has \(S=\varnothing\)
in (0.1), and hence \(d(D)=1\).  There are \(\operatorname{Cat}_{m-1}\)
such paths, and

\[
 {\operatorname{Cat}_{m-1}\over\operatorname{Cat}_m}
 ={m+1\over2(2m-1)}\ge {1\over4}.                   \tag{5.12}
\]

Thus at least \(B/4\) values of \(d\) equal one, while Lemma 5.3 supplies
at least \(c_1B/\sqrt m\) values at least \(2m/3\).  For arbitrary real
numbers \(x_D\) with mean \(\bar x\),

\[
 B\sum_D(x_D-\bar x)^2
 =\sum_{D<E}(x_D-x_E)^2.                             \tag{5.13}
\]

Keep only pairs with the first member in the \(d=1\) population and the
second in the population (5.6).  Equations (5.12)-(5.13) give

\[
 V\ge {1\over B}\,{B\over4}\,{c_1B\over\sqrt m}
       \left({2m\over3}-1\right)^2
 \ge c m^{3/2}B.
\]

This completes the proof. \(\square\)

Theorem 5.4 quantifies the saturation.  Even under the favorable additional
assumption that every selected endpoint has \(\delta_I\ge\varepsilon N\),
the numerical right sides supplied by (3.1) are no smaller than

\[
 {M_1\over\varepsilon N}\ge c_\varepsilon{B\over\sqrt m},
 \qquad
 {H M_2\over\varepsilon^2N^2}\ge c_{A,\varepsilon}B
 \quad(H=\lceil A\sqrt m\rceil).                    \tag{5.14}
\]

These are respectively factors \(\sqrt m\) and \(m\) above the quotient
scale \(B/N\).  Equation (5.14) is a statement about the value of the
particular moment upper bounds, not a lower bound on the true packing.

## 6. Charge-fibre second moments have an unavoidable square-root loss

For fixed \(s\), define the modular charge

\[
 c_s(D)\equiv
 \sum_{h=0}^{s-1}d(\tau^hD)-\delta(\tau^sD)\pmod N,
 \qquad c_s(D)\in\mathbb Z_N.                       \tag{6.1}
\]

Let

\[
 n_a=\#\{D\in\Omega:c_s(D)=a\},
 \qquad a\in\mathbb Z_N.
\]

The zero-winding starts are contained in the fibre \(a=0\); the latter may
also contain positive-winding starts.

### Proposition 6.1 (Plancherel barrier)

Put

\[
 F_k=\sum_{D\in\Omega}\zeta^{kc_s(D)}.
\]

Then

\[
 \sum_{k=0}^{N-1}|F_k|^2=N\sum_{a\in\mathbb Z_N}n_a^2. \tag{6.2}
\]

Consequently, even a collision estimate of the optimal equidistribution
order

\[
 \sum_a n_a^2\le C{B^2\over N}                     \tag{6.3}
\]

implies only

\[
 n_0\le\sqrt C,{B\over\sqrt N}.                    \tag{6.4}
\]

This loss is sharp from the information (6.3) alone: whenever
\(B\ge16N^2\), there are nonnegative integers \(n_a\) summing to \(B\)
such that

\[
 n_0\ge {B\over8\sqrt N},
 \qquad
 \sum_a n_a^2\le 2{B^2\over N}.                    \tag{6.5}
\]

#### Proof

Equation (6.2) is character orthogonality.  Equation (6.4) follows from
\(n_0^2\le\sum_a n_a^2\).

For sharpness, put

\[
 q=\left\lfloor{B\over N}\right\rfloor,
 \qquad
 t=\left\lfloor{B\over4\sqrt N}\right\rfloor,
 \qquad
 n_0=q+t.
\]

Distribute \(B-n_0\) as equally as possible among the other \(N-1\)
coordinates.  The assumption \(B\ge16N^2\) makes all coordinates
nonnegative and gives \(n_0\ge B/(8\sqrt N)\).  Relative to the mean
\(B/N\), the zero-coordinate deviation has magnitude at most \(t+1\),
and every other deviation has magnitude at most \(t/(N-1)+2\).  Since the
deviations sum to zero,

\[
 \sum_a n_a^2
 ={B^2\over N}+\sum_a\left(n_a-{B\over N}\right)^2
 \le {B^2\over N}+(t+1)^2
 +(N-1)\left({t\over N-1}+2\right)^2
 \le2{B^2\over N}.
\]

This proves (6.5). \(\square\)

Thus unsigned collision energy cannot locate the zero charge at the
\(B/N\) scale, let alone prove its depletion.  The sign of the deviation of
the zero fibre, or correlations between consecutive values of \(s\), must
enter.  This is distinct from the support-orthogonality collapse in Section
4, and the two obstructions persist simultaneously.

## 7. Audit of the level-three indexing

The corrected display after Theorem 10.1 of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md` can be checked directly as
follows.  This also supplies a concrete zero-winding example for the dual
first-passage identity.

Use the notation of Theorem 8.2:

\[
 t=m-3,
\]

\[
 D_0=110100(10)^t,
 \quad
 D_1=1011(01)^t00,
 \quad
 D_2=(10)^t110010,
\]

with \(D_0\mapsto D_1\mapsto D_2\mapsto D_0\) under \(\phi\).  The gap-five
start used there is \(D_1\), so

\[
 \tau D_1=D_0,
 \qquad
 \tau^2D_1=D_2.
\]

The distinguished component of \(D_1\) ends at the final zero, hence
\(d(D_1)=1\).  In \(D_0\), the distinguished component is \(110100\) and
the terminal suffix is \((10)^t\), hence

\[
 d(D_0)=2t+1=N-6.
\]

Finally, the first maximum-reaching step of \(D_2\) is at position
\(2t+2=N-5\).  Therefore the correct identity is

\[
 \boxed{d(D_1)+d(\tau D_1)=1+(N-6)=N-5
       =\delta(\tau^2D_1).}                          \tag{7.1}
\]

This is zero winding for every \(m\ge3\).  The displayed numerical triple
\((1,3),4\) occurs only when \(t=1\), namely \(m=4\), after the appropriate
start indexing.

## 8. Exact remaining theorem

For \(H=\lceil A\sqrt m\rceil\), fixed-window residence needs the
edge-disjoint zero-winding quotient packing to be \(o_A(B/N)\), after the
negligible short quotient cycles are discarded.  The arguments above prove
the exact first-passage/height reduction (2.13b), but that estimate remains
larger than the target by \(\Theta(\sqrt{m\log m})\).  They also prove that
none of the following scalar refinements supplies the missing factor:

1. total deficit mass;
2. uncentered deficit Bessel energy;
3. the dual initial/terminal endpoint ledgers;
4. centered deficit variance without an empirical-mean separation theorem;
5. simultaneous use of all spatial characters through telescoping;
6. a collision second moment for the modular charge fibres.

The residual positive target can therefore be stated narrowly:

> Prove a signed, higher-order correlation or a cycle-clustering theorem
> for the literal rotation \(\tau(P1R0S)=S1P0R\), strong enough to show
> that the zero-winding solutions of (2.2)-(2.3) occupy quotient intervals
> with packing number \(o_A(B/N)\).

This report neither proves nor disproves that target.  It proves why the
natural first/second-moment and orthogonality implementations stop before
it.

## 9. Final descent need not realize the zero-winding height

The stronger proposed necessary condition

\[
 \operatorname{fd}(D)=s=\operatorname{ht}(D),      \tag{9.1}
\]

where \(\operatorname{fd}(D)\) is the length of the final descent, is
false.  There is a symbolic counterexample in every semilength at least
four.

### Theorem 9.1 (an all-dimensional final-descent obstruction)

For every \(t\ge0\), put

\[
 A_t=(10)^t,
 \qquad
 D^{(t)}=A_t11100100.                               \tag{9.2}
\]

Then \(D^{(t)}\) has semilength \(t+4\), and its next zero-winding return
has \(s=3\).  Nevertheless

\[
 \boxed{
 \operatorname{ht}(D^{(t)})=3,
 \qquad
 \operatorname{fd}(D^{(t)})=2.}                    \tag{9.3}
\]

Moreover, one round of peak deletion gives

\[
 \boxed{\partial D^{(t)}=1100.}                    \tag{9.4}
\]

Thus peak deletion of the exact equality chain does not force the deepest
branch to be the rightmost branch.

#### Proof

The prefix \(A_t\) is Dyck of height one.  The final primitive component
\(11100100\) has height three, first reached at its third step.  Hence the
canonical factorization of \(D_0=D^{(t)}\) is

\[
 P_0=A_t11,
 \qquad R_0=0010,
 \qquad S_0=\varnothing.                            \tag{9.5}
\]

Therefore

\[
 D_1=\tau D_0=1A_t1100010.
\]

Read \(A_t\) from height one.  It oscillates between heights one and two,
so the final displayed pair of up-steps first reaches height three.  The
canonical factorization is

\[
 P_1=1A_t1,
 \qquad R_1=00,
 \qquad S_1=10.                                     \tag{9.6}
\]

Consequently

\[
 D_2=\tau D_1=1011A_t1000.                          \tag{9.7}
\]

In (9.7), the first maximum-reaching step is always the fifth step: it is
the first step of \(A_t\) when \(t>0\), and the first step of the displayed
terminal \(1000\) when \(t=0\).  The path does not return to height zero
until its final step.  Thus

\[
 P_2=1011,
 \qquad S_2=\varnothing.                            \tag{9.8}
\]

The three even-time deficits are therefore

\[
 d(D_0),d(D_1),d(D_2)=1,3,1.                       \tag{9.9}
\]

Since \(S_2\) is empty,

\[
 D_3=\tau D_2=1P_2 0R_2=110110R_2.
\]

Its first global maximum is reached by the fifth step of the displayed
prefix \(11011\).  Indeed, \(R_2\), in its original position, ran from
height three to height one without exceeding height three; after the
rotation it is read from height two and cannot exceed height two.  Hence

\[
 \delta(D_3)=5=1+3+1.                              \tag{9.10}
\]

This is the zero-winding equation at \(s=3\).  At the two earlier times,

\[
 \delta(D_1)=2t+3>1,
 \qquad
 \delta(D_2)=5>1+3,
\]

so the return is consecutive; this also follows from Theorem 2.2.

The word in (9.2) visibly has height three and ends in exactly two zeros,
proving (9.3).  Finally, delete every peak.  Every prefix component \(10\)
vanishes, while

\[
 1^3 0^2 1^1 0^2
 \longmapsto
 1^2 0^1 1^0 0^1=1100.
\]

The reduced word \(1100\) is fixed by \(\tau\), has \(d=1\) and
\(\delta=2\), and hence has its own zero-winding return at \(s=2\).
Peak deletion has reduced the equality passage from height three to height
two, but it has not certified that the outer deepest branch was rightmost.
This proves (9.4) and the theorem. \(\square\)

Theorem 9.1 blocks the proposed final-descent enumeration.  The valid
necessary conditions remain those of Theorem 2.3: the first
maximum-attaining primitive component is terminal, and the return length is
the global height.  The global height need not be attained on the rightmost
tree branch.
