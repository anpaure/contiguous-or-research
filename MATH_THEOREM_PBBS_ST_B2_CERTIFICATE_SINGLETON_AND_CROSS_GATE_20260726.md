# Genuine PBBS \(B_2\) certificates are singletons: the exact cross-interlacing gate

Date: 2026-07-26

Method: pure mathematics only.  No profile envelope, independent marginal,
probabilistic surrogate, computation, or external input is used.

## 0. Outcome

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
 \qquad G=2H-1,qquad h=H+1.                    \tag{0.1}
\]

For a reduced root \(F\), let

\[
 a_H(F)=\mathbf1_{\{B_2(F)\le G\}}              \tag{0.2}
\]

be the literal second-predecessor-hit predicate.  The preceding
certificate theorem partitioned the active phases according to the current
particle \(a\), its predecessor \(b=a-1\), and the first two future
selection times

\[
 T_1<T_2                                           \tag{0.3}
\]

of \(b\).  It left two possible sources of short-lag degree: several
active phases in one terminal-hit certificate, or interlacing between
different certificates.

This note proves that the first source is impossible in genuine no-wrap
PBBS.

### Main theorem

Let \(F\in\mathcal D_d\) have \(k\) peaks, and assume

\[
 G<2(d+k)+1.                                      \tag{0.4}
\]

On every persistent-label augmentation of the reduced orbit, every
nonempty \(B_2\)-certificate cluster has exactly one phase:

\[
 \boxed{c_\gamma=1.}                             \tag{0.5}
\]

More strongly, if

\[
 e(t)=2t+B_2(\tau^tF)                            \tag{0.6}
\]

is the absolute first-return endpoint of the minimal peak expansion, then

\[
 \boxed{t\longmapsto e(t)
 \text{ is injective on the active phases in every no-wrap lift}.}       \tag{0.7}
\]

Condition (0.4) holds with room throughout the Pascal saddle

\[
 d=\frac m2+O(\sqrt{m\log m}),\qquad
 k=\frac m6+O(\sqrt{m\log m}),                   \tag{0.8}
\]

because \(d+k=(2/3+o(1))m\) while \(G=O(\sqrt m)\).

Consequently the exact certificate identities collapse to

\[
 \boxed{
 \mathscr I_H=0,qquad
 2\mathscr C_H=\mathscr X_H,qquad
 \Delta_H(t)=\xi_H(t).}                          \tag{0.9}
\]

Thus the statewise alternative asked for in the task is decided:

\[
 \boxed{
 \text{terminal clusters are not size-biased unbounded; they are
 identically singleton.}}                        \tag{0.10}
\]

Every possible divergence of the genuine reduced predecessor
autocorrelation must be cross-certificate interlacing.

At critical reduced active mass

\[
 \mathscr R_H\ge\kappa B_m/H,                    \tag{0.11}
\]

the exact remaining alternatives are now

\[
 \boxed{
 \begin{array}{ll}
 \text{bounded cross degree:}&
 \exists K,\delta>0:\
 \Pr_{\rm active}^{\rm Pascal}\{\xi_H\le K\}\ge\delta,\\[1mm]
 &\Longrightarrow\ \nu_{A\sqrt m}=\Omega(B_m\sqrt m);\\[3mm]
 \text{positive necessary branch:}&
 \xi_H\longrightarrow\infty
 \text{ in Pascal-weighted active probability.}
 \end{array}}                                    \tag{0.12}
\]

The first line follows from the established bounded-degree pullback; the
second is necessary if \(ST_A\) holds.  The theorem does **not** prove
which line holds in the global Pascal-weighted census.  That is no longer
a terminal-renewal question: it is exactly the cross-label four-hit
alignment problem.

There cannot be a universal statewise shortcut.  Two genuine PBBS
calibrations realize both cross regimes:

* the long-period calibrated singleton family in the Pascal saddle has
  \(\xi_H\le2\), but total weight only
  \((B_m/H)e^{-\Theta(\sqrt m)}\);
* the exact one-defect mountain rotor has \(\xi_H=\Theta(H)\) on almost
  every active phase, but its native-rank or lifted mass is subcritical for
  the Gaussian saddle.

Hence a proof of either line of (0.12) must be an aggregate
Pascal-weighted theorem.  Local PBBS legality permits both behaviors.

## 1. The equivariant minimal expansion

For a nonempty reduced root \(F\in\mathcal D_d\), let \(\Lambda F\) be
its unique minimal peak expansion.  It has rank

\[
 d+\operatorname {pk}(F)=d+k                         \tag{1.1}
\]

and no free inserted leaves.  Peak deletion semiconjugates the normalized
step-two PBBS map, and the minimal inverse fibre is a singleton.  Therefore

\[
 \boxed{\partial\Lambda F=F,
 \qquad\tau\Lambda F=\Lambda\tau F.}             \tag{1.2}
\]

At every phase, every transported free-slot coordinate of \(\Lambda F\)
is zero.  The exact predecessor theorem consequently gives

\[
 \boxed{
 a_H(\tau^tF)=1
 \Longrightarrow
 \tau^t\Lambda F\text{ starts a genuine first return at time }
 B_2(\tau^tF).}                                  \tag{1.3}
\]

The no-wrap assumption (0.4) makes (1.3) literal on the common physical
lift; no congruence modulo the outer circumference is involved.

## 2. First-return endpoints cannot be shared

Follow the physical PBBS trajectory of \(D=\Lambda F\) on the universal
time line.  Let

\[
 \lambda_s                                         \tag{2.1}
\]

be the omitted physical coordinate at one-step time \(s\).  If quotient
phase \(t\) is active, (1.3) says

\[
 \lambda_{e(t)}=\lambda_{2t},
 \qquad
 \lambda_s\ne\lambda_{2t}
 \quad(2t<s<e(t)),                                \tag{2.2}
\]

where \(e(t)\) is (0.6).  The second assertion is firstness, not merely
endpoint equality.

### Lemma 2.1 (endpoint injection)

Equation (0.7) holds.

#### Proof

Suppose two distinct active phases have the same endpoint.  Lift their
start times to integers with

\[
 2t<2t'<e(t)=e(t')<2t+2(d+k)+1.                  \tag{2.3}
\]

The last inequality is the no-wrap choice supplied by (0.4).  Applying
(2.2) to both starts gives

\[
 \lambda_{2t}=\lambda_{e(t)}=\lambda_{2t'}.
\]

But \(2t'\) lies strictly between \(2t\) and the first return endpoint
\(e(t)\), contradicting the second part of (2.2).  Hence the endpoint map
is injective. \(\square\)

This argument uses one actual PBBS word and the exact first-return
property.  It is not a statement about a formal selected-label itinerary.

## 3. Certificate clusters are singleton

Work in the persistent equality-particle word of the reduced process.  An
active phase \(t\) has current particle

\[
 a=\kappa_{2t},\qquad b=a-1,                     \tag{3.1}
\]

and its certificate records the first two future \(b\)-hits
\(T_1(t),T_2(t)\).  By definition of \(B_2\),

\[
 e(t)=T_2(t)                                     \tag{3.2}
\]

when the same time origin is used for the minimal expansion.

If two active phases shared one certificate, they would have the same
second hit \(T_2\), hence the same endpoint (3.2).  Lemma 2.1 forbids
this.  This proves (0.5).

Equivalently, the exact marked-suffix occupancy

\[
 \#\left\{t:
 r_{b,i-1}<2t<r_{b,i},\quad
 \kappa_{2t}=b+1,\quad
 r_{b,i+1}-2t\le G\right\}                       \tag{3.3}
\]

is always at most one for an actual no-wrap PBBS selected-particle word.
This is a PBBS-specific restriction absent from arbitrary balanced cyclic
words.  It repairs the same-spectrum obstruction: those abstract words may
place several successor visits in one terminal suffix, but PBBS firstness
does not.

## 4. Collapse of the two-time kernel

Let \(\Gamma_\gamma\) be the certificate classes and

\[
 {\cal K}_H(\gamma,\eta)
 =\sum_{u=1}^{h}
 |\Gamma_\gamma\cap(\Gamma_\eta-u)|.             \tag{4.1}
\]

The exact reduced two-time count on one long augmented orbit is

\[
 K_H({\cal O})=\sum_{\gamma,\eta}
                   {\cal K}_H(\gamma,\eta).      \tag{4.2}
\]

By (0.5), every diagonal term is zero.  Thus

\[
 \boxed{
 K_H({\cal O})
 =\sum_{\gamma\ne\eta}{\cal K}_H(\gamma,\eta).} \tag{4.3}
\]

For an active phase \(t\), all its short-lag active neighbours belong to
different certificates, so

\[
 \boxed{
 \Delta_H(t)
 =\sum_{u=1}^{h}
  \bigl(a_H(\tau^{t+u}F)+a_H(\tau^{t-u}F)\bigr)
 =\xi_H(t).}                                     \tag{4.4}
\]

Now weight every augmented rank-\(d\), peak-\(k\) orbit by

\[
 w_{\cal O}
 ={1\over2d+1}\binom{m+d-k}{2d}.                \tag{4.5}
\]

After the negligible short-period deletion, summing (4.3)--(4.4) gives
(0.9).  In particular,

\[
 \boxed{
 {2\mathscr C_H\over\mathscr R_H}
 =\mathbb E_{\rm active}^{\rm Pascal}\xi_H.}    \tag{4.6}
\]

No same-predecessor renewal moment remains in (4.6).

## 5. The corrected statewise decision boundary

Assume the critical one-point lower bound (0.11).  For fixed \(K\), put

\[
 \mathscr L_{H,K}^{\rm cross}
 =\sum_{d,k}P_m(d,k)
   \#\{F:a_H(F)=1,\ \xi_H(F)\le K\}.             \tag{5.1}
\]

Because \(\xi_H=\Delta_H\), the established terminal-zero degree pullback
gives

\[
 \boxed{
 \overline\nu_H
 \ge {\left((3/4-o(1))\mathscr L_{H,K}^{\rm cross}
              -o(B_m/H)\right)_+\over K+1}.}     \tag{5.2}
\]

After the simple-return reduction and the \(N\)-fold deck lift,

\[
 \mathscr L_{H,K}^{\rm cross}=\Omega(B_m/H)
 \quad\Longrightarrow\quad
 \boxed{\nu_{A\sqrt m}=\Omega(B_m\sqrt m).}      \tag{5.3}
\]

Conversely, \(ST_A\) and (0.11) imply

\[
 \boxed{
 \forall K<\infty,\qquad
 \mathscr L_{H,K}^{\rm cross}=o(B_m/H),}         \tag{5.4}
\]

which is exactly

\[
 \xi_H\longrightarrow\infty                    \tag{5.5}
\]

in active Pascal-weighted probability.

Equations (5.2)--(5.5) are an exact equivalence boundary.  They do not
evaluate the cross term.  In particular, scalar divergence of
\(\mathscr C_H/\mathscr R_H\) remains weaker than (5.5), because a sparse
set of highly interlaced phases may carry the mean.

## 6. Actual PBBS calibrations show why no local conclusion remains

The singleton theorem removes one proposed local mechanism, but it does
not make cross interlacing universal.

### 6.1 Bounded cross degree at the saddle

The calibrated long-period singleton family has

\[
 d=\frac m2+O(\sqrt m),\qquad
 k=\frac m6+O(\sqrt m),\qquad
 \Delta_H\le2.                                   \tag{6.1}
\]

By (4.4), its actual cross degree satisfies

\[
 \boxed{\xi_H\le2.}                              \tag{6.2}
\]

Its complete Pascal mass is only

\[
 {B_m\over H}e^{-\Theta(\sqrt m)}.               \tag{6.3}
\]

Thus it is a genuine saddle calibration, but not the critical obstruction
required by (5.3).

### 6.2 Divergent cross degree

On the exact one-defect mountain rotor, all but one phase are active in a
cycle of length \(2h-1\).  Since certificate clusters are singleton,
its already computed degree

\[
 \Delta_H=\Theta(h)                               \tag{6.4}
\]

is entirely cross-certificate:

\[
 \boxed{\xi_H=\Theta(H).}                        \tag{6.5}
\]

This is genuine PBBS dynamics, but its native-rank or Gaussian lift has
subcritical global weight.

Therefore neither boundedness nor divergence of \(\xi_H\) is a statewise
law of PBBS.  Only an aggregate theorem on the long-period Pascal-saddle
orbits can decide (5.2) versus (5.4).

## 7. Exact remaining kernel

Every active phase now supplies one distinct first-return arc

\[
 I_t=[2t,e(t)]                                    \tag{7.1}
\]

in the physical omitted-label word of the minimal expansion.  The arcs
obey

\[
 \lambda_{e(t)}=\lambda_{2t},\qquad
 \lambda_s\ne\lambda_{2t}\quad(2t<s<e(t)),       \tag{7.2}
\]

and their right endpoints are distinct by Lemma 2.1.  The cross kernel is
therefore

\[
 \boxed{
 \mathscr X_H
 =\sum_{\cal O}w_{\cal O}
  \sum_{\substack{t\ne t'\\1\le|t-t'|_\ell\le h}}
  \mathbf1_{\{e(t)-2t\le G\}}
  \mathbf1_{\{e(t')-2t'\le G\}}.}               \tag{7.3}
\]

Here the endpoints \(e(t),e(t')\) are the actual next equal-label times
in one PBBS word, not independently chosen renewal variables.  Formula
(7.3) is the sole remaining reduced two-time statistic.

The endpoint injection gives only the sharp statewise cap

\[
 \xi_H(t)=O(H);                                   \tag{7.4}
\]

the dense rotor shows that this order is attainable.  It gives no
aggregate saving at the critical scale.

## 8. Final status

The exact statewise question is settled:

\[
 \boxed{c_\gamma=1\text{ for every genuine no-wrap PBBS certificate}.}
\]

Hence terminal-cluster divergence is impossible, and every positive
\(ST_A\) proof must establish cross-certificate divergence in probability.
Every negative proof may instead establish positive critical Pascal mass
with bounded \(\xi_H\), in which case (5.3) gives the required physical
packing obstruction.

What is not settled is the global alternative itself.  The actual PBBS
renewal word admits both bounded and divergent cross behavior on genuine
subfamilies, and the known bounded family loses
\(e^{-\Theta(\sqrt m)}\) mass.  Thus this note proves neither \(ST_A\) nor
its negation.  It proves that the only remaining unknown is (7.3), with no
terminal-bunching branch left to absorb the difficulty.
