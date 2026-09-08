# The volume seed controls every min-plus price at terminal depths five and six; the residue certificate breaks at seven

**Date:** 2026-08-07  
**Status:** unconditional all-price theorem for the terminal even
parent/child pair at depths five and six, proved without classifying either
min-plus fan.  An exact depth-seven calculation disproves the simple
residue-prefix certificate, but does not disprove the volume-seed
inequality itself.

## 1. Volume-normalized pair functional

For an even complete binomial state in dimension $n$, put

\[
 r={n\over2},\qquad t=r-D,\qquad
 V_{n,D}=D{n\choose r}-\sum_{j=1}^{r-1}{n\choose j}.
 \tag{1.1}
\]

Thus $V_{n,D}$ is the margin of the linear price $\psi(L)=L$.  Let
$M_{n,D}(\psi)$ denote the complete whole-job price margin.  For an even
parent $n$ and its central two-step child $n-2$, define

\[
 \lambda={V_{n,D}\over V_{n-2,D}},
 \qquad
 \mathcal L_{n,D}(\psi)
 =M_{n,D}(\psi)-\lambda M_{n-2,D}(\psi).
 \tag{1.2}
\]

The linear price is tight:

\[
                         \mathcal L_{n,D}(L)=0.
 \tag{1.3}
\]

If $P_1$ denotes the distance-one outer pair, the two-step identity gives

\[
 M_{n,D}=2M_{n-2,D}+M(P_1).
 \tag{1.4}
\]

Consequently (1.2) is exactly the weighted pair margin with outer-pair
weight one and central weight

\[
                         \rho^{\rm vol}=2-\lambda.
 \tag{1.5}
\]

The question is whether (1.3) is the worst covering price, namely whether
$\mathcal L_{n,D}(\psi)\ge0$ for every min-plus closure $\psi$.

## 2. A residue variation-diminishing lemma

Let a nonnegative closed piece table $p_1,\ldots,p_D$ have min-plus
closure $\psi$.  Choose $h$ minimizing $p_i/i$, and define

\[
                         \delta(L)=\psi(L)-{L\over h}p_h.
 \tag{2.1}
\]

Then

\[
 \delta(L)\ge0,\qquad
 \delta(L+h)\le\delta(L),\qquad
 \delta(jh)=0.
 \tag{2.2}
\]

The first inequality is the minimum-density lower bound for every
partition, the second follows by appending one size-$h$ piece, and the
third follows by using only size-$h$ pieces.

### Lemma 2.1 (residue-prefix certificate)

Let a finite signed sequence $(\mu_L)_{L\ge1}$ satisfy

\[
                         \sum_LL\mu_L=0.
 \tag{2.3}
\]

Assume that for every $1\le h\le D$, every nonzero residue
$1\le a<h$, and every $J\ge0$,

\[
 \boxed{
 \sum_{j=0}^{J}\mu_{a+jh}\ge0,}
 \tag{2.4}
\]

where coefficients beyond the support are zero.  Then every depth-$D$
min-plus closure satisfies

\[
                         \sum_L\mu_L\psi(L)\ge0.
 \tag{2.5}
\]

#### Proof

Choose a minimum-density $h$.  By (2.3), the linear part of (2.1)
cancels, so it is enough to prove
$\sum_L\mu_L\delta(L)\ge0$.  Multiples of $h$ contribute zero by
(2.2).  On a nonzero residue class, write

\[
 d_j=\delta(a+jh),\qquad
 S_J=\sum_{j=0}^{J}\mu_{a+jh}.
\]

The sequence $d_j$ is nonnegative and nonincreasing.  Finite summation by
parts gives

\[
 \sum_{j=0}^{N}\mu_{a+jh}d_j
 =\sum_{j=0}^{N-1}S_j(d_j-d_{j+1})+S_Nd_N\ge0.
 \tag{2.6}
\]

Sum over the nonzero residues. \(\square\)

This lemma is a variation-diminishing statement: one never enumerates
the shortest-path fan.  Only monotonicity of reduced costs along residue
classes is used.

## 3. Exact coefficient formula

Put

\[
 H_s^{(n)}={n\choose s}-{n\choose s-1},
 \qquad
 \widetilde H_1^{(n)}=n,
 \qquad
 \widetilde H_s^{(n)}=H_s^{(n)}\quad(s\ge2).
 \tag{3.1}
\]

For $1\le L\le t-1$, define

\[
 \nu_{n,D}(L)=
 \mathbf1_{L\le D}H_{t+L}^{(n)}
 -\widetilde H_{t-L}^{(n)},
 \tag{3.2}
\]

and set it to zero outside that range.  The birth formula is

\[
                         M_{n,D}(\psi)
                         =\sum_L\nu_{n,D}(L)\psi(L).
 \tag{3.3}
\]

To avoid rational arithmetic, scale the coefficients of (1.2) by the
positive child volume:

\[
 \boxed{
 \widehat\mu_L=
 V_{n-2,D}\nu_{n,D}(L)
 -V_{n,D}\nu_{n-2,D}(L).}
 \tag{3.4}
\]

Then

\[
 V_{n-2,D}\mathcal L_{n,D}(\psi)
 =\sum_L\widehat\mu_L\psi(L),
 \qquad
 \sum_LL\widehat\mu_L=0.
 \tag{3.5}
\]

The tail signs have a short binomial proof.  For every admissible $s$,

\[
 \boxed{
 {H_s^{(n)}\over H_{s-1}^{(n-2)}}
 ={n(n-1)\over s(n+1-s)}.}
 \tag{3.6}
\]

This follows by substituting
$H_s^{(n)}={n\choose s}(n-2s+1)/(n-s+1)$; the factor
$n-2s+1$ cancels.

## 4. Terminal depth five

Take

\[
 D=5,\qquad n=76,\qquad n-2=74.
 \tag{4.1}
\]

The exact volume margins are

\[
 V_{74,5}=158985138106653726685,
 \qquad
 V_{76,5}=130481704855775740733.
 \tag{4.2}
\]

For the five exceptional short lengths, direct substitution in (3.4)
gives

\[
\begin{array}{c|r}
L&\widehat\mu_L\\ \hline
1& 21279569910196437387025065868478826962600\\
2& 34970060092946175659259439535875570177610\\
3& 35643542966207173624078631184458913199600\\
4& 21524456516363635750552331668676317892830\\
5&-5135642076097480036368412763710703568380
\end{array}
 \tag{4.3}
\]

Every later coefficient is negative.  Indeed, for $6\le L\le30$, put
$s=33-L$, so $3\le s\le27$.  Equation (3.6) gives

\[
 {H_s^{(76)}\over H_{s-1}^{(74)}}
 ={5700\over s(77-s)}
 \ge {38\over9}>1>
 {V_{76,5}\over V_{74,5}}.
 \tag{4.4}
\]

This is precisely $\widehat\mu_L<0$.  At $L=31$, the child uses the
modified rank-one birth, but

\[
 -H_2^{(76)}+{V_{76,5}\over V_{74,5}}\,74
 <-2774+74<0.
 \tag{4.4a}
\]

At $L=32$, only the parent rank-one birth remains, so the sign is again
negative.  Thus the entire
sign pattern is

\[
                         +,+,+,+,-,-,\ldots,-.
 \tag{4.5}
\]

For $2\le h\le5$, put

\[
 S_{h,a}=\sum_{j\ge0}\widehat\mu_{a+jh}
 \qquad(1\le a<h).
 \tag{4.6}
\]

The exact minima over the nonzero residues are

\[
\begin{array}{c|c|r}
h&\operatorname*{argmin}_{1\le a<h}S_{h,a}
 &\min_{1\le a<h}S_{h,a}\\ \hline
2&1&38738116195528698624305350254644306603854\\
3&2&23968193544076301328775646686731722430540\\
4&1&13371534233622582008566373238370120540489\\
5&1& 3931539206316370536210531459503236258980
\end{array}
 \tag{4.7}
\]

Every number is a direct binomial substitution in (3.4) and (4.6).
Because each nonzero residue sequence starts positive and then has only
negative terms, its prefix sums rise and then decrease to the positive
total in (4.7).  Hence every prefix is nonnegative.  Lemma 2.1 proves:

### Theorem 4.1 (all depth-five prices)

For every closed depth-five piece table and its complete min-plus closure,

\[
 \boxed{
 M_{76,5}(\psi)
 -{V_{76,5}\over V_{74,5}}M_{74,5}(\psi)\ge0.}
 \tag{4.8}
\]

Equivalently, the volume seed

\[
 \boxed{
 \rho^{\rm vol}_{5}
 =2-{V_{76,5}\over V_{74,5}}
 ={187488571357531712637\over158985138106653726685}}
 \tag{4.9}
\]

is the exact minimum central weight for a unit distance-one pair.  The
linear price is tight, so no smaller weight can work.  This controls every
depth-five fan ray without classifying the fan.

## 5. Terminal depth six

The identical certificate works one depth further.  Here

\[
 D=6,\quad n=106,\quad
 V_{104,6}=148723210992834427850437189877,
 \quad
 V_{106,6}=206593673676293574049897331849.
 \tag{5.1}
\]

The short coefficients have signs

\[
 \widehat\mu_1,\ldots,\widehat\mu_5>0,
 \qquad \widehat\mu_6<0.
 \tag{5.2}
\]

For a fully reproducible sign certificate, their smallest positive value
and the negative boundary value are

\[
\begin{aligned}
 \min_{1\le L\le5}\widehat\mu_L
 &=9807130586968231099301963248717358141831481512581042253076,\\
 \widehat\mu_6
 &=-4395742001457903783718562227997340648550876493635804192128.
\end{aligned}
 \tag{5.3}
\]

For $7\le L\le44$, formula (3.6), now with $3\le s\le40$, gives

\[
 {H_s^{(106)}\over H_{s-1}^{(104)}}
 ={11130\over s(107-s)}
 \ge {1113\over268}>4
 >{V_{106,6}\over V_{104,6}},
 \tag{5.4}
\]

so these tail coefficients are negative.  At $L=45$, the child uses the
modified rank-one birth, but

\[
 -H_2^{(106)}+{V_{106,6}\over V_{104,6}}\,104
 <-5459+2\cdot104<0.
 \tag{5.4a}
\]

At $L=46$, only the negative parent rank-one coefficient remains.  The
exact residue-total minima are

\[
\begin{array}{c|c|r}
h&\operatorname*{argmin}_{1\le a<h}S_{h,a}
 &\min_{1\le a<h}S_{h,a}\\ \hline
2&1&26927591468742280730801019951554008026363837799184573670994\\
3&1&17024188555070210006977391599221046729347936034437913988726\\
4&3&10522623372621323428962630405246754265955191766758182622749\\
5&1& 5217823620407741969433414604687771961097154239013781725431\\
6&1&  288797910418870941301352628519742514648648440072755385569
\end{array}
 \tag{5.5}
\]

The same one-sign-change argument verifies every residue prefix.
Therefore:

### Theorem 5.1 (all depth-six prices)

For every closed depth-six piece table and its complete min-plus closure,

\[
 \boxed{
 M_{106,6}(\psi)
 -{V_{106,6}\over V_{104,6}}M_{104,6}(\psi)\ge0.}
 \tag{5.6}
\]

Equivalently, the exact minimum unit-pair central weight is

\[
 \boxed{
 \rho^{\rm vol}_{6}
 =2-{V_{106,6}\over V_{104,6}}.}
 \tag{5.7}
\]

Again the volume ray is tight and controls every other min-plus price.

## 6. Exact break of this certificate at depth seven

The residue-prefix lemma is not an automatic all-depth proof.  At the
terminal depth-seven pair

\[
 D=7,\qquad n=142,
 \tag{6.1}
\]

the child and parent volumes are

\[
\begin{aligned}
 V_{140,7}&=6758985279718335862903013333535935437613,\\
 V_{142,7}&=7214609492569109394262920676290298581449.
\end{aligned}
 \tag{6.2}
\]

Form the scaled coefficients by (3.4).  On residue one modulo seven, the
second prefix is already negative:

\[
 \boxed{
 \widehat\mu_1+\widehat\mu_8
 =-2481935950726504473099989469441511843589071109953864598736332618889098521528400<0.}
 \tag{6.3}
\]

The complete residue-one total is also negative:

\[
 \sum_{j\ge0}\widehat\mu_{1+7j}
 =-3423325714954379686130249243233713709218759036643730386067200682046346277185673.
 \tag{6.4}
\]

Thus Lemma 2.1 cannot certify depth seven.  This is a failure of the
*proof mechanism*, not a counterexample to the volume seed: reduced costs
on different residues obey additional subadditivity relations, and those
relations may compensate the negative residue-one mass.  No depth-seven
price with negative volume-normalized margin is claimed.

## 7. Exact conclusion

The volume-seed principle survives the first two unclassified depths:
at terminal $D=5$ and $D=6$, it controls every covering price by a
one-dimensional residue variation argument, with no fan enumeration.
The first genuine new gate is now precise.  Starting at $D=7$, one must
use coupling between residue classes---equivalently, cyclic
subadditivity of the Apéry distance vector---rather than monotonicity
within each residue separately.
