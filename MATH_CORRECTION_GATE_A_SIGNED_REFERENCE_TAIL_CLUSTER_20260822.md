# Gate A correction: the signed reference-tail residual and its first punctured cluster

**Date:** 2026-08-22  
**Status:** exact signed reduction, fixed-carrier product-FKG theorem, and
exact finite punctured-slice obstruction; the asymptotic between-carrier
reference theorem remains open

## 0. Outcome

The normalized-hazard identity behind (G.168) is correct, but its last
one-sided relaxation is too lossy for the numerical Gate-A ledger.  If

\[
 X=\frac{d_v}{z_\sigma},\qquad
 U=\frac{R_v-J_v}{z_\sigma},\qquad
 Q=\frac{\overline D_m(v)}{z_\sigma},
\]

and \(\tau_\Psi\) is the carrier-Palm law tilted by an increasing
normalized-degree test \(\Psi(X)\), then the exact state-mixture identity is

\[
 \boxed{
 -\frac{\operatorname {Cov}(h_\gamma/Z,\Psi)}{\mathbb E\Psi}
 =\frac{k_\sigma}{n_\sigma}
 \left[-\Delta_\Psi X
       +m\Delta_\Psi^-U+\Delta_\Psi Q\right],}       \tag{0.1}
\]

where

\[
 \Delta_\Psi X=\mathbb E_{\tau_\Psi}X-\mathbb EX\ge0,
 \quad
 \Delta_\Psi^-U=\mathbb EU-\mathbb E_{\tau_\Psi}U,
 \quad
 \Delta_\Psi Q=\mathbb E_{\tau_\Psi}Q-\mathbb EQ. \tag{0.2}
\]

Consequently the sharp one-sided consequence is

\[
 \boxed{
 \frac{[-\operatorname {Cov}(h_\gamma/Z,\Psi)]_+}{\mathbb E\Psi}
 \le\frac{k_\sigma}{n_\sigma}
 \left[m\Delta_\Psi^-U+\Delta_\Psi Q\right]_+.}     \tag{0.3}
\]

Replacing \(\Delta_\Psi Q\) by
\(\mathbb E_{\tau_\Psi}Q\), as in (G.168), is formally valid because
\(Q\ge0\).  It is not a numerically faithful reference-law interface.

An exact \(r=3\) directed-punctured two-slice calculation proves all three
of the following simultaneously.

1. A universal favorable sign for \(U\) is false, even on a genuine
   uniform two-shore slice.
2. The absolute tilted duplicate load \(\mathbb E_{\tau_\Psi}Q\) can be
   between \(19\) and \(43\), far above the coefficient-one budget.
3. Its signed shift \(\Delta_\Psi Q\) cancels almost all of
   \(12\Delta_\Psi^-U\), and the favorable degree shift cancels the
   remainder.  The exact hazard covariance is favorable in both shores.

Thus the shortest reference and stopped interfaces must retain the signed
joint residual

\[
             12\Delta_\Psi^-U+\Delta_\Psi Q,         \tag{0.4}
\]

or, equivalently, retain the whole carrier hazard/avoidance profile.  A
separate small bound on \(\mathbb E_{\tau_\Psi}Q\) is not the right target.

## 1. Exact signed normalized-hazard identity

Let \(H\) be a finite simple hypergraph whose rows meet shore
\(V_\sigma\) in exactly \(k_\sigma\) targets.  Consider any mixture of
states having common shore sizes \(n_\sigma\).  The number of current rows
\(Z(H)\) may vary.  Put

\[
 z_\sigma(H)=\frac{k_\sigma Z(H)}{n_\sigma}.
\]

Fix a root \(v\in V_\sigma\), and choose an ordered \(m\)-carrier
\(\gamma=(v;F_1,\ldots,F_m)\) uniformly from the distinct current rows
through \(v\).  Let \(h_\gamma\) be the number of current rows meeting at
least one carrier row.  For a current row \(F\), define

\[
 C_F=|\{G:G\cap F\ne\varnothing\}|,
 \qquad
 \mathfrak E(F)=\sum_{G:G\cap F\ne\varnothing}(|F\cap G|-1).
                                                               \tag{1.1}
\]

For a target \(u\in V_\tau\), put \(b_u=d_u-z_\tau\), and set

\[
 R_v=\frac1{d_v}\sum_{F\ni v}\sum_{u\in F-\{v\}}b_u,
 \qquad
 J_v=\frac1{d_v}\sum_{F\ni v}\mathfrak E(F).       \tag{1.2}
\]

If \(D_\gamma\) is the number of repetitions among the external conflict
rows met by the carrier, write

\[
 \overline D_m(v)=\mathbb E[D_\gamma\mid H,v].       \tag{1.3}
\]

The row identity

\[
 C_F=\sum_{u\in F}d_u-\mathfrak E(F)                 \tag{1.4}
\]

and inclusion--exclusion at multiplicity one give

\[
 \frac{\mathbb E[h_\gamma\mid H,v]}{Z(H)}
 =\frac{k_\sigma}{n_\sigma}
 \left\{m(c_\sigma-1)+X+mU-Q\right\},              \tag{1.5}
\]

where \(X,U,Q\) are as in Section 0 and

\[
 c_\sigma=\frac1{z_\sigma}\sum_\tau k_\tau z_\tau
 =\sum_\tau k_\tau
   \frac{k_\tau n_\sigma}{k_\sigma n_\tau}         \tag{1.6}
\]

is constant throughout the mixture.  Palmize by all labelled ordered
carriers.  Since \(\Psi\) is root-measurable, conditional averaging replaces
\(h_\gamma\) by the left side of (1.5).  Tilting by
\(\Psi/\mathbb E\Psi\), subtracting the untilted mean, and using
\(\operatorname {Cov}(X,\Psi)\ge0\) prove (0.1)--(0.3).

The distinction between (0.3) and the weaker bound

\[
 \frac{k_\sigma}{n_\sigma}
 \left[m(\Delta_\Psi^-U)_+
       +\mathbb E_{\tau_\Psi}Q\right]               \tag{1.7}
\]

is the main point of this note.

## 2. What product association proves exactly

Let the original target indicators be independent, with an arbitrary
retention probability in \((0,1]\) on each target.  Fix a labelled carrier
\(\gamma\) in the complete catalogue and condition on every target in its
carrier rows being retained.  The remaining unfixed indicators are still
independent.

Let \(d_v\) be the residual root degree, let \(h_\gamma\) be the residual
carrier hazard, and let \(c>0\) be deterministic.  Both

\[
             d_v,qquad h_\gamma
\]

are coordinatewise nondecreasing functions of the remaining target
indicators.  Hence Harris's inequality proves, for every nondecreasing
\(\psi\),

\[
 \boxed{
 \operatorname {Cov}\left(
 h_\gamma,\psi(d_v/c)
 \mathrel{\Big|}\gamma\text{ retained}\right)\ge0.} \tag{2.1}
\]

This is not yet the full carrier-Palm sign.  Let \(\pi_\gamma\) be the
deterministic survival-weighted distribution of the carrier label, and put

\[
 H_\gamma=\mathbb E[h_\gamma\mid\gamma\text{ retained}],
 \qquad
 P_\gamma=\mathbb E[\psi(d_v/c)mid\gamma\text{ retained}]. \tag{2.2}
\]

The law of total covariance gives the exact decomposition

\[
 \boxed{
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\psi(d_v/c))
 =\mathbb E_{\pi}\operatorname {Cov}(
     h_\gamma,\psi(d_v/c)\mid\gamma\text{ retained})
  +\operatorname {Cov}_{\pi}(H_\gamma,P_\gamma).}    \tag{2.3}
\]

The first term is nonnegative by (2.1).  The only possible product-law
reversal is the between-carrier Simpson term in (2.3).  Existing rooted
boundary polymers control fixed moments of the carrier-conditioned
environment, but they do not yet give a tail-mass-uniform bound on this
last covariance.

Two qualifications are essential.

* If \(c\) is replaced by the realized random average degree, the test need
  not be coordinatewise increasing.  That is the separate shadow-center
  transfer.
* A uniform exact-size slice is negatively dependent rather than product.
  Fixed-tuple de-Poissonization with exponentially small relative error does
  not automatically transfer a normalized tail ratio whose denominator can
  be much smaller.  Section 3 gives a literal example.

## 3. The first exact directed-punctured slice cluster

This is the smallest parameter with a nonconstant twelve-carrier tail on a
relevant equal-decrement slice.  At \(r=2\), the shores have sizes \(10\)
and \(5\).  On every slice with sizes \((10-t,5-t)\), the cases \(t=0,1\)
have \(X=d/z_\sigma=1\) at every root supporting a twelve-carrier, while
the cases \(t\ge2\) have no such root.  Hence every normalized upper-tail
test is constant or zero.  The checker verifies this by exhausting all
\(2^{15}\) target sets before performing the \(r=3\) calculation below.

Take \(r=3\), so \(b=7\).  The middle targets are the \(35\) three-subsets
of \([7]\), and the lower targets are the \(21\) two-subsets.  For a
permutation \(w=(w_0,\ldots,w_6)\), define

\[
 E(w)=\{(\mathcal M,I_3^w(s)):s=1,\ldots,6\}
 \mathbin{\dot\cup}
 \{(\mathcal L,I_2^w(s)):s=1,\ldots,6\},            \tag{3.1}
\]

where \(I_j^w(s)=\{w_s,\ldots,w_{s+j-1}\}\) cyclically.  These are
exactly \(7!=5040\) distinct rows.

Let \(A\) be one uniformly missing middle target and \(B\) one uniformly
missing lower target, independently.  Retain every other target.  This is
the uniform two-shore slice with

\[
                         n_M=34,qquad n_L=20.        \tag{3.2}
\]

The state orbit is determined by

\[
                         j=|A\cap B|\in\{0,1,2\}.    \tag{3.3}
\]

The orbit sizes and residual row counts are

\[
\begin{array}{c|ccc}
j&0&1&2\\ \hline
\#\text{ states}&210&420&105\\
Z_j&3096&2856&3264.
\end{array}                                                \tag{3.4}
\]

Indeed, for a fixed three-set \(A\), the numbers of two-sets meeting it in
\(0,1,2\) points are \(6,12,3\).  Multiplication by \(35\) gives the first
row.  Inclusion--exclusion gives

\[
 Z_j=5040-864-1440+d(A,B),                           \tag{3.5}
\]

and the three pair codegrees are \(360,120,528\), respectively.

At every retained root use ordered twelve-carriers.  Let

\[
 \psi_{11/10}(X)=\left(\frac{(X-11/10)_+}{X}\right)^{12}. \tag{3.6}
\]

The carrier-Palm mass of a state-root pair is \((d_v)_{12}\).  Define
\(U,Q\) with the realized shore averages

\[
 z_M=\frac{6Z_j}{34},\qquad z_L=\frac{6Z_j}{20}.     \tag{3.7}
\]

For comparison, the deterministic slice centers are

\[
 \mathbb EZ=\frac{20880}{7},\qquad
 \bar z_M=\frac{62640}{119},\qquad
 \bar z_L=\frac{6264}{7}.                            \tag{3.8}
\]

Let \(\overline U\) denote the same companion statistic centered and
normalized by \(\bar z_M,\bar z_L\).

### Theorem 3.1 (exact local-cluster table)

For the slice (3.2), carrier order \(m=12\), and test (3.6), the following
table is obtained by exact rational arithmetic.

\[
\begin{array}{c|cc}
 &\mathcal M&\mathcal L\\ \hline
\mathbb EU-\mathbb E_\tau U
 &0.0424705562834&0.0625430965606\\
\mathbb E\overline U-\mathbb E_\tau\overline U
 &0.286441610310&0.180732947773\\
\mathbb EQ&42.5355632649&20.1048851331\\
\mathbb E_\tau Q&42.0940305875&19.4298938583\\
\Delta_\Psi Q&-0.441532677428&-0.674991274799\\
12\Delta_\Psi^-U+\Delta_\Psi Q
 &0.0681139979734&0.0755258839284\\
\Delta_\Psi X&0.0681140031163&0.0755258839860\\
-\Delta_\Psi X+12\Delta_\Psi^-U+\Delta_\Psi Q
 &-5.14287636\,10^{-9}&-5.75735133\,10^{-11}.
\end{array}                                                \tag{3.9}
\]

Every displayed sign is exact; the decimals only shorten the rational
numbers.  In particular,

\[
 \boxed{\mathbb EU-\mathbb E_\tau U>0}              \tag{3.10}
\]

on both shores, even after replacing the realized center by the
deterministic centers (3.8).  Nevertheless the last row of (3.9) is
negative on both shores, so the exact normalized carrier-hazard covariance
is favorable.

The untilted and tilted state-orbit masses make the responsible cluster
explicit:

\[
\begin{array}{c|ccc}
 &j=0&j=1&j=2\\ \hline
\mathcal M\text{ untilted}&.34064703&.39445798&.26489499\\
\mathcal M\text{ tilted}&.01302619&.98616429&.00080951\\
\mathcal L\text{ untilted}&.34331309&.38648427&.27020264\\
\mathcal L\text{ tilted}&.00385704&.99613294&.00001002.
\end{array}                                                \tag{3.11}
\]

Thus the first adverse \(U\)-cluster is the orbit in which the missing
middle and lower targets meet in exactly one coordinate.

#### Proof and exact certificate

For each of the three orbit representatives, enumerate the \(5040\)
permutations in (3.1), retain precisely those rows avoiding \(A,B\), and
compute

\[
 d_v=|\{F:v\in F\}|,qquad
 C_F=|\{G:F\cap G\ne\varnothing\}|,qquad
 \mathfrak E(F)=\sum_G(|F\cap G|-1)_+.              \tag{3.12}
\]

For every current row \(G\not\ni v\), put

\[
 a_G(v)=|\{F:v\in F,\ F\cap G\ne\varnothing\}|.   \tag{3.13}
\]

Sampling twelve carrier rows without replacement gives the exact duplicate
formula

\[
 \overline D_{12}(v)=
 \sum_{G\not\ni v}
 \left\{\frac{12a_G(v)}{d_v}-1
       +\frac{(d_v-a_G(v))_{12}}{(d_v)_{12}}\right\}. \tag{3.14}
\]

Equations (1.2), (3.7), and (3.14) determine \(U,Q,X\) at every root.
Multiply by the orbit count, the carrier mass \((d_v)_{12}\), and, for the
tilted columns, the rational weight (3.6).  Summing and dividing gives
(3.9)--(3.11).

The standard-library checker

`scratch/verify_gate_a_punctured_reference_local_cluster_20260822.py`

performs exactly these finite sums with `fractions.Fraction`.  It asserts
the catalogue size, orbit sizes, all three row counts, the centers (3.8),
both positive \(U\)-deficits, both positive shadow-center deficits, both
positive degree shifts, and both strictly negative exact brackets in the
last row of (3.9).  It uses no floating-point number in any assertion.
The decimals are produced only after all exact sign checks pass.

For literal self-containment, here are the exact sign certificates used in
(3.9).  For each labelled quantity \(Y\), reduce the rational number
obtained from (3.6)--(3.14) to \(Y=N_Y/D_Y\), where \(D_Y>0\).  The
following are the exact signed numerators \(N_Y\); hence every stated sign
can be checked by inspection, without treating a decimal or a program run
as a premise.

More explicitly, on either shore index the finitely many orbit-root atoms
by \(i\), let \(w_i\) be the orbit count times \((d_i)_{12}\), and put

\[
 B=\sum_iw_i,quad T=\sum_iw_i\Psi_i,quad
 B_Y=\sum_iw_iY_i,quad T_Y=\sum_iw_i\Psi_iY_i.     \tag{3.15}
\]

Here \(B,T>0\).  Thus the unreduced cross-product for a deficit is
\(B_YT-T_YB\), while that for a tilted-minus-untilted shift is
\(T_YB-B_YT\); its denominator is the positive integer \(BT\), after
clearing the already positive local rational denominators in
(3.7)--(3.14).  The integers below are those cross-products after their
common positive factors are cancelled.  Linear combinations use the same
positive common denominator.

```text
M.U_deficit =
+904231771741250389376210136034793803449875647884194265461944964946680871227633935442475058275389963817569289147535720311951579672603830897529073737769654030772906540240575908911136105162037876987
M.shadow_U_deficit =
+158643830038733178428228406482717042344140674431351460099427852320431942562488706024530490388058757379993702146852137930702764152120554641296742172587878552452204036255353536942083894095605955666391
M.Q_shift =
-4881070546058471135221339887507873018534265612708385636671846147240834863454530617967685368825652187793170223566896066403557507174870064388857514027131506265523414927986490798140578294240890925061
M.signed_residual =
+4894428206140578390797801240607974419247237256705361112841771123275148672264725368630284962786554313955949757290372241010915180103799732822353645203316197520400517847831134122987253346496743005077
M.degree_shift =
+271966711238256055413095387565589591888614393863342513108627050464679262988069591219189963594578303655954827366736374434931219126160746913986143343252264676665899844230439137253301569783
M.exact_bracket =
-369548696088891025002181168765074738414099621446297655065109076926091197522140444021633997253331327827994011889626516772044961512191328817310001108463819534089553615373744321807145596726523

L.U_deficit =
+2228692550519888215676357282676749501097188671293522905991203200742844231310578326625292666947596583410619040762828569303497
L.shadow_U_deficit =
+273748632318424532152289871947818418516014692191144713750938350911749887136402355772478511188145226206119208948656244302707
L.Q_shift =
-158689554020805098208513802479030428093171070083412398328380880609141048985345376056240516170179100664267918341138698648211001067
L.signed_residual =
+17756035203854451826583403590487829908693357022895810138942676793669928807513110062683904272062120844350791116054439183546856423
L.degree_shift =
+645402352187757643279190704033488691736942227726214350786382111939324075472366412901935688072813707925112141087878991235
L.exact_bracket =
-6767728329157648701416148372839704672930507719396591828803590472075279466674333527764849471129512968447662637369594351
```

The two entries \(\mathbb EQ\) and \(\mathbb E_\tau Q\) are strictly
positive directly from (3.14): every summand is nonnegative and the
enumeration contains external rows hit by at least two carrier choices.

## 4. Quantitative loss caused by the absolute duplicate charge

For the middle shore, the right side inside brackets in the relaxed bound
(1.7) is

\[
 12(0.0424705562834)+42.0940305875=42.6036772629.   \tag{4.1}
\]

For the lower shore it is

\[
 12(0.0625430965606)+19.4298938583=20.1804110170.   \tag{4.2}
\]

The signed residuals in (0.3) are only \(0.0681140\) and \(0.0755259\),
and the favorable degree shifts make the exact covariance nonpositive.
Thus (1.7) loses factors exceeding \(600\) and \(267\), respectively, and
changes a favorable exact sign into a large positive upper bound.

The phenomenon is not that the \(r=3\) residual has abnormally large
tail-only duplicates.  In the complete \(r=3\) catalogue, direct evaluation
of (3.14) gives

\[
 Q_M=45.1388890773,qquad Q_L=22.6833333350.         \tag{4.3}
\]

The duplicate load is a large common baseline.  Its *change under the tail
tilt*, not its absolute value, is the quantity participating in the exact
hazard covariance.

## 5. Consequences for the live proof architecture

The following claims should be retained.

1. The normalization identity (1.5), the exact covariance formula (0.1),
   and the pointwise typed-codegree theorem are correct.
2. A separate bound on \((\Delta_\Psi^-U)_+\) and
   \(\mathbb E_{\tau_\Psi}Q\) remains a valid sufficient condition.
3. Product Harris association proves the fixed-carrier term (2.1).

The following descriptions are too strong and should be weakened.

1. The statement that the *exact* remaining statistic after (G.168) is the
   tail-local \(U\)-deficit plus an absolute duplicate load should be
   replaced by the signed joint residual (0.4), or the unsplit carrier
   hazard/avoidance covariance.
2. The absolute duplicate estimate (G.170) should be described as an
   optional stronger route.  It is not the shortest numerical interface and
   can be grossly non-sharp even at the uniform reference law.
3. A product-law favorable sign cannot be transferred to exact slices by a
   fixed-tuple de-Poissonization statement alone.  A rare-tail-normalized
   cluster comparison is required.

No change to `MASTER_HANDOFF.md` is made here.  The precise recommended
replacement for its Gate-A sentence is:

> The shortest sequential input is a numerically adequate stopped bound on
> the signed joint residual
> \(12(\mathbb EU-\mathbb E_{\tau_\Psi}U)
> +\mathbb E_{\tau_\Psi}Q-\mathbb EQ\), equivalently on the unsplit
> normalized carrier-hazard/avoidance covariance, followed by the
> normalized-center and unequal-purge transfer.  Separate tail-local
> \(U\) and absolute-\(Q\) bounds are optional stronger hypotheses.

## 6. Exact asymptotic reference gate left open

The finite \(r=3\) slice does not disprove an asymptotic favorable or
\(o(1)\) bound at fixed \(a>1\).  It proves that such a theorem must retain
the connected missing-target cluster and the signed duplicate cancellation.

For independent retention with deterministic center, (2.3) isolates the
remaining reference theorem exactly:

\[
 \boxed{
 \frac{[-\operatorname {Cov}_{\pi}(H_\gamma,P_\gamma)]_+}
      {\mathbb E_\pi P_\gamma}
 =o(z_\sigma),}                                      \tag{6.1}
\]

uniformly for \(x\ge r^{-\alpha}\), the relevant fixed normalized tail
thresholds, and \(m=12\).  Equivalently one may prove the signed version of
(0.3) directly.  The necessary boundary object is a tail-decorated
carrier-union polymer: ordinary fixed moments and global \(L^2\) energies do
not control the denominator in (6.1).

For exact slices, the corresponding theorem must additionally sum the
finite-population connected cluster exemplified by \(|A\cap B|=1\), with
relative rather than additive error at the tail scale.  Only after this
reference theorem is proved should one attempt the stopped-law comparison.

There is a rigorous reason that the existing fixed-order flower estimates
do not already give this comparison.  Let \(c\ge m\) be an integer and

\[
                         f_c(d)=(d-c)_+^m.           \tag{6.2}
\]

Write its Newton expansion as

\[
 f_c(d)=\sum_{j=0}^d a_j{d\choose j},
 \qquad a_j=\Delta^jf_c(0).                         \tag{6.3}
\]

If \(A_m(z)=\sum_{q=0}^{m-1}\left\langle{m\atop q}\right\rangle z^q\)
is the Eulerian polynomial, then the standard power-sum generating function
and the binomial-transform identity give

\[
\begin{aligned}
 \sum_{d\ge0}f_c(d)z^d
 &=\frac{z^{c+1}A_m(z)}{(1-z)^{m+1}},\\
 \boxed{
 \sum_{j\ge0}a_jt^j
 =t^{c+1}(1+t)^{m-c-1}
     A_m\!\left(\frac{t}{1+t}\right)
 =\frac{t^{c+1}B_m(t)}{(1+t)^c},}                  \tag{6.4}
\end{aligned}
\]

where

\[
 B_m(t)=\sum_{q=0}^{m-1}
 \left\langle{m\atop q}\right\rangle
 t^q(1+t)^{m-1-q}.                                  \tag{6.5}
\]

For completeness, if \(F(z)=\sum_df_c(d)z^d\) and
\(A(t)=\sum_ja_jt^j\), then

\[
 F(z)=\frac1{1-z}A\!\left(\frac z{1-z}\right),
 \qquad
 A(t)=\frac1{1+t}F\!\left(\frac t{1+t}\right),     \tag{6.6}
\]

which proves (6.4).  Moreover

\[
                         B_m(-1)=(-1)^{m-1}\ne0.     \tag{6.7}
\]

Thus the pole at \(t=-1\) in (6.4) does not cancel.  The Newton series has
infinitely many nonzero coefficients (indeed they eventually alternate
with polynomial magnitude).  On a finite star of degree \(D\), its exact
truncation can require tuple orders growing all the way to \(D\), not merely
orders bounded in advance as \(r\to\infty\).

For \(m=12\) and the Gate-A threshold \(c=\Theta(z_\sigma)\), this proves:

\[
 \boxed{
 \text{fixed-order carrier/flower moments alone cannot algebraically
 reconstruct the exact normalized tail scalar.}}             \tag{6.8}
\]

This is not an impossibility theorem for a cluster expansion.  It says that
the successful expansion must be all-order or must control the truncated
tail function directly; a theorem through any fixed factorial order cannot
be promoted to the needed tail ratio by a finite Newton identity.
