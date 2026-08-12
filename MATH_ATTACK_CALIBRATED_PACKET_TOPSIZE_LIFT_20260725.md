# A Pascal lift for calibrated top packets

Date: 2026-07-25

Pure mathematics only.

## 0. Result and boundary

Let \(X\) be an \(n\)-set.  For every \(M\)-set \(U\subset X\), choose one
directed cyclic order \(\pi_U\).  The chosen order supplies its \(M\) cyclic
intervals at every proper length.  This note gives a canonical fractional
lift from top size \(M\) to top size \(M+1\): for a child top \(T\), delete a
point \(z\in T\), use the already chosen order on \(T-z\), and insert \(z\)
in a cyclic gap.  Average equally over all \((M+1)M\) deletion-gap routes.

The lift has an exact profile recurrence.  If \(\varepsilon_r\) is the
normalized \(L^1\) error of the old length-\(r\) interval profile and
\(\chi_r\) is the normalized covariance between a length-\(r\) interval and
exclusion of a prescribed point by its parent top, then

\[
 \boxed{
 \varepsilon_r^+
 \le {M-r+1\over M+1}\varepsilon_r
       +{r\over M+1}(\varepsilon_{r-1}+\chi_{r-1}) .}
 \tag{0.1}
\]

No product of marginal estimates occurs in (0.1).  The covariance term is
an actual joint packet--boundary incidence.  Near the middle, its coefficient
is \(1-o(1)\).  Thus marginal near-transversality and marginal shallow-shadow
balance do **not** by themselves form an inductive invariant.

For \(n=2m\), \(M=m+H\), the middle and two shadow recurrences are

\[
 \varepsilon_{0}^{+,\mathrm{mid}}
 \le {H+1\over M+1}\varepsilon_0
      +{m\over M+1}(\varepsilon_1^-+\chi_{m-1}),
 \tag{0.2}
\]

\[
 \varepsilon_q^{+,-}
 \le {H+q+1\over M+1}\varepsilon_q^-
      +{m-q\over M+1}(\varepsilon_{q+1}^-+\chi_{m-q-1}),
 \tag{0.3}
\]

and, for \(q\ge1\),

\[
 \varepsilon_q^{+,+}
 \le {H-q+1\over M+1}\varepsilon_q^+
      +{m+q\over M+1}(\varepsilon_{q-1}^++\chi_{m+q-1}).
 \tag{0.4}
\]

Equations (0.2)--(0.4) prove a conditional one-step integral lifting theorem
once the joint covariance and the childwise correlated-rounding discrepancy
are \(o(1)\) in aggregate.  They also give a genuine partial theorem without
that rounding assumption: the canonical **fractional** lift preserves every
shallow profile satisfying those joint bounds.

More generally, let \(\varepsilon_{r,k}\) measure the joint profile of an
\(r\)-interval together with exclusion of a prescribed \(k\)-set by its
parent top.  The whole hierarchy obeys

\[
 \boxed{
 \varepsilon_{r,k}^+
 \le {M-r+1\over M+1}\varepsilon_{r,k}
     +{r\over M+1}\varepsilon_{r-1,k+1}.}
 \tag{0.4a}
\]

Thus \(t\) fractional lifts require correlations only through boundary order
\(t\), and the error at any one output rank is a convex combination of the
initial errors \(\varepsilon_{r-j,j}\), \(0\le j\le t\).

There is a separate obstruction to lifting directly from dimension \(2m\)
to \(2m+2\).  If two new points are added and the radius \(H\) is retained,
only

\[
 {2\binom{2m}{M}\over\binom{2m+2}{M+1}}
 ={1\over2}+O(H/m)                                      \tag{0.5}
\]

of the new top tags contain exactly one new point and hence have an old
\(M\)-top as a one-point deletion parent.  A direct ambient-dimension lift
must therefore couple old top sizes \(M-1,M,M+1\); a one-layer induction
misses asymptotically half the child tops.

## 1. Packet profiles and the missing joint statistic

Assume

\[
 2\le r\le M-1.                                         \tag{1.1}
\]

For \(A\in\binom Xr\), let

\[
 \mu_r(A)
 =\#\{U\in\tbinom XM:A\text{ is a cyclic }r
                  \text{-interval of }\pi_U\}.
 \tag{1.2}
\]

Every proper rank has the same total occurrence mass

\[
 L_M:=\sum_A\mu_r(A)=M\binom nM.                        \tag{1.3}
\]

Put

\[
 \bar\mu_r={L_M\over\binom nr},\qquad
 E_r=\sum_{A\in\binom Xr}|\mu_r(A)-\bar\mu_r|,
 \qquad
 \varepsilon_r={E_r\over L_M}.                         \tag{1.4}
\]

The statistic \(E_r\) measures the complete interval-occurrence profile,
not just its support.  At the middle rank, when \(L_M=(1-o(1))\binom nm\),
the condition \(E_m=o(L_M)\) implies both \(o(\binom nm)\) holes and
\(o(\binom nm)\) repeated-owner occurrences.

The lift needs a joint refinement of (1.2).  If
\(B\in\binom Xs\) and \(z\notin B\), define

\[
 \nu_s(B,z)
 =\#\{U\in\tbinom XM:B\text{ is an }s\text{-interval of }\pi_U,
                         \ z\notin U\}.                 \tag{1.5}
\]

The appropriate conditional density is

\[
 \alpha_s={n-M\over n-s}.                               \tag{1.6}
\]

Indeed, without making any randomness assumption,

\[
 \sum_{B,z\notin B}\nu_s(B,z)=(n-M)L_M,                \tag{1.7}
\]

because every interval occurrence has exactly \(n-M\) points outside its
parent top.  The average of \(\nu_s(B,z)\) over the
\(\binom ns(n-s)\) admissible pairs is therefore
\(\alpha_s\bar\mu_s\).

Define the top--point covariance defect

\[
 K_s=\sum_{B,z\notin B}
      |\nu_s(B,z)-\alpha_s\mu_s(B)|,
 \qquad
 \chi_s={K_s\over(n-M)L_M}.                             \tag{1.8}
\]

This is the additional induction variable.  It is not a product of a top
marginal and an interval marginal.  It directly counts their failure to
factor.

It will also be useful to center \(\nu\) at its global mean:

\[
 F_s=\sum_{B,z\notin B}
      |\nu_s(B,z)-\alpha_s\bar\mu_s|.                   \tag{1.9}
\]

The triangle inequality, followed by summation over the \(n-s\) possible
points \(z\), gives the exact useful bound

\[
 \begin{aligned}
 F_s
 &\le K_s+\alpha_s(n-s)E_s\\
 &=K_s+(n-M)E_s.
 \end{aligned}                                         \tag{1.10}
\]

Equivalently,

\[
 {F_s\over(n-M)L_M}\le\chi_s+\varepsilon_s.            \tag{1.11}
\]

There is no corresponding estimate with \(K_s\) omitted: the marginal
number \(\mu_s(B)=\sum_{U\supset B}\mathbf1_{\{B\text{ interval in }U\}}\)
does not determine how those occurrences are distributed between tops
containing and avoiding a given \(z\).

## 2. The canonical deletion--insertion lift

Fix a child top \(T\in\binom X{M+1}\).  A route consists of

\[
 z\in T,\qquad U=T-z,\qquad
 g\in\{\text{the }M\text{ cyclic gaps of }\pi_U\}.       \tag{2.1}
\]

Insert \(z\) in gap \(g\).  This gives a cyclic order
\(\operatorname{ins}_{g,z}(\pi_U)\) of \(T\).  Give every route weight

\[
 {1\over M(M+1)}.                                       \tag{2.2}
\]

Thus every child top has total packet weight one.  Coincident output orders,
if any, have their route weights added.

### Lemma 2.1 (cyclic gap audit)

Let \(A\) be a proper cyclic \(r\)-interval of an \(M\)-cycle.

1. Inserting a new point in exactly \(M-r+1\) of the \(M\) gaps leaves
   \(A\) a cyclic \(r\)-interval.
2. If \(B\) is a cyclic \((r-1)\)-interval, inserting a new point in exactly
   \(r\) gaps makes \(B\) together with the new point a cyclic
   \(r\)-interval.

#### Proof

The first insertion may occur in any gap except the \(r-1\) internal gaps of
the block \(A\), leaving \(M-(r-1)=M-r+1\) choices.  For the second claim,
the insertion gap may be any of the \(r-2\) internal gaps of \(B\), or either
boundary gap, giving \(r\) choices.  The restrictions in (1.1) exclude the
empty and whole-cycle degeneracies. \(\square\)

Let \(\mu_r^+(A)\) be the resulting weighted number of child packets in which
\(A\) is a cyclic \(r\)-interval.  Its total mass is

\[
 L_{M+1}:=(M+1)\binom n{M+1}
          =(n-M)\binom nM
          ={n-M\over M}L_M.                            \tag{2.3}
\]

### Theorem 2.2 (exact profile-boundary identity)

For \(2\le r\le M-1\) and \(A\in\binom Xr\),

\[
 \boxed{
 \mu_r^+(A)
 ={(n-M)(M-r+1)\over M(M+1)}\mu_r(A)
 +{r\over M(M+1)}
       \sum_{z\in A}\nu_{r-1}(A-z,z).}
 \tag{2.4}
\]

#### Proof

Partition the routes producing \(A\) according as the inserted point \(z\)
lies outside or inside \(A\).

If \(z\notin A\), deletion of \(z\) shows that \(A\) was already an
\(r\)-interval in the parent order.  For every occurrence counted by
\(\mu_r(A)\), there are \(n-M\) choices of \(z\notin U\), and Lemma 2.1 gives
\(M-r+1\) admissible gaps.  Multiplication by (2.2) gives the first term.

If \(z\in A\), put \(B=A-z\).  The parent must omit \(z\), and \(B\) must be
an \((r-1)\)-interval in it.  These are precisely the occurrences counted by
\(\nu_{r-1}(B,z)\).  Lemma 2.1 gives \(r\) admissible gaps.  Sum over
\(z\in A\) and multiply by (2.2). \(\square\)

Write

\[
 \bar\mu_r^+={L_{M+1}\over\binom nr}.                   \tag{2.5}
\]

The constant profiles in (2.4) have the correct output mean.  Explicitly,
using

\[
 {\bar\mu_{r-1}\over\bar\mu_r}
 ={\binom nr\over\binom n{r-1}}
 ={n-r+1\over r},                                      \tag{2.6}
\]

one obtains

\[
 \begin{aligned}
 &{(n-M)(M-r+1)\over M(M+1)}\bar\mu_r\\
 &\quad+{r\over M(M+1)}\,r\alpha_{r-1}\bar\mu_{r-1}
 ={n-M\over M}\bar\mu_r
 =\bar\mu_r^+.
 \end{aligned}                                         \tag{2.7}
\]

Subtracting (2.7) from (2.4) is therefore an exact **joint** centered
identity; no independence substitution has been made.

### Corollary 2.3 (normalized error recurrence)

Let

\[
 \varepsilon_r^+
 ={1\over L_{M+1}}
   \sum_{A\in\binom Xr}|\mu_r^+(A)-\bar\mu_r^+|.
 \tag{2.8}
\]

Then

\[
 \boxed{
 \varepsilon_r^+
 \le {M-r+1\over M+1}\varepsilon_r
 +{r\over M+1}
       {F_{r-1}\over(n-M)L_M}.}
 \tag{2.9}
\]

Consequently,

\[
 \boxed{
 \varepsilon_r^+
 \le {M-r+1\over M+1}\varepsilon_r
 +{r\over M+1}(\varepsilon_{r-1}+\chi_{r-1}).}
 \tag{2.10}
\]

#### Proof

Apply the triangle inequality to the centered form of (2.4), then sum over
\(A\).  The correspondence

\[
 (A,z\in A)\longleftrightarrow(B=A-z,z\notin B)         \tag{2.11}
\]

is a bijection, so the second summed term is exactly \(F_{r-1}\).  Divide by
(2.3).  The two coefficients become

\[
 {M-r+1\over M+1},\qquad {r\over M+1},                 \tag{2.12}
\]

which add to one.  Finally use (1.11). \(\square\)

The second coefficient in (2.10) is \(1-o(1)\) when \(r\sim M\sim n/2\).
Thus \(\chi_{r-1}\) is not a lower-order technicality.  It is the leading
input to the lifted central profile.

### Theorem 2.4 (the full Pascal boundary hierarchy)

For \(k\ge0\), \(B\in\binom Xs\), and
\(Z\in\binom{X-B}k\), define

\[
 \nu_{s,k}(B,Z)
 =\#\{U\in\tbinom XM:
       B\text{ is an }s\text{-interval of }\pi_U,\
       U\cap Z=\varnothing\}.                           \tag{2.13}
\]

Thus \(\nu_{s,0}=\mu_s\) and \(\nu_{s,1}=\nu_s\).  Put

\[
 \alpha_{s,k}
 ={\binom{n-M}k\over\binom{n-s}k}.                     \tag{2.14}
\]

Every interval occurrence admits exactly \(\binom{n-M}k\) excluded
\(k\)-sets, so

\[
 \sum_{B,Z}\nu_{s,k}(B,Z)
 =\binom{n-M}kL_M.                                     \tag{2.15}
\]

Consequently \(\alpha_{s,k}\bar\mu_s\) is the global mean on the
\(\binom ns\binom{n-s}k\) admissible pairs.  Define

\[
 \varepsilon_{s,k}
 ={1\over\binom{n-M}kL_M}
  \sum_{B,Z}
  |\nu_{s,k}(B,Z)-\alpha_{s,k}\bar\mu_s|.               \tag{2.16}
\]

At the child level the same definition uses top size \(M+1\), hence
\(\binom{n-M-1}kL_{M+1}\) in the denominator.

For \(2\le r\le M-1\) and \(0\le k\le n-M-1\),

\[
 \boxed{
 \varepsilon_{r,k}^+
 \le {M-r+1\over M+1}\varepsilon_{r,k}
      +{r\over M+1}\varepsilon_{r-1,k+1}.}
 \tag{2.17}
\]

#### Proof

Fix \(A\in\binom Xr\) and \(Z\in\binom{X-A}k\).  In a lifted packet whose
child top avoids \(Z\), an inserted point outside \(A\) must also avoid
\(Z\).  For every parent occurrence counted by \(\nu_{r,k}(A,Z)\), there
are \(n-M-k\) possible inserted points and \(M-r+1\) gaps.  If the inserted
point is \(z\in A\), the parent top must avoid \(Z\cup\{z\}\).  The gap audit
therefore gives the exact identity

\[
 \begin{aligned}
 \nu_{r,k}^+(A,Z)
 &= {(n-M-k)(M-r+1)\over M(M+1)}\nu_{r,k}(A,Z)\\
 &\quad+{r\over M(M+1)}
   \sum_{z\in A}
   \nu_{r-1,k+1}(A-z,Z\cup\{z\}).
 \end{aligned}                                         \tag{2.18}
\]

The constant reference profiles in (2.18) map to the child constant
reference profile.  To verify this directly, put \(N=n-M\).  The first
constant term is

\[
 {(N-k)(M-r+1)\over M(M+1)}
 {\binom Nk\over\binom{n-r}k}\bar\mu_r.                 \tag{2.19}
\]

Using

\[
 {\bar\mu_{r-1}\over\bar\mu_r}={n-r+1\over r},
 \qquad
 (k+1)\binom N{k+1}=(N-k)\binom Nk,                    \tag{2.20}
\]

the second constant term is

\[
 {r(N-k)\over M(M+1)}
 {\binom Nk\over\binom{n-r}k}\bar\mu_r.                 \tag{2.21}
\]

Their sum is

\[
 {N-k\over M}{\binom Nk\over\binom{n-r}k}\bar\mu_r
 ={N\over M}
   {\binom{N-1}k\over\binom{n-r}k}\bar\mu_r,            \tag{2.22}
\]

which is \(\alpha_{r,k}^+\bar\mu_r^+\).

Subtract (2.22) from (2.18), apply the triangle inequality, and sum over
\((A,Z)\).  The first term sums to the old \(k\)-boundary error.  In the
second term, the map

\[
 (A,Z,z\in A)\longmapsto(B=A-z,Y=Z\cup\{z\})           \tag{2.23}
\]

maps onto every admissible \((B,Y)\), with \(|Y|=k+1\), exactly \(k+1\)
times, once for every choice of the marked point \(z\in Y\).  Finally use

\[
 \binom Nk={N\over N-k}\binom{N-1}k,\qquad
 (k+1)\binom N{k+1}=N\binom{N-1}k,                    \tag{2.24}
\]

and \(L_{M+1}=NL_M/M\).  After division by
\(\binom{N-1}kL_{M+1}\), the two coefficients reduce to those in (2.17).
\(\square\)

For \(k=0\), (2.17) is the sharper form

\[
 \varepsilon_r^+
 \le {M-r+1\over M+1}\varepsilon_r
      +{r\over M+1}\varepsilon_{r-1,1},                \tag{2.25}
\]

where

\[
 \varepsilon_{r-1,1}
 ={F_{r-1}\over(n-M)L_M}
 \le\varepsilon_{r-1}+\chi_{r-1}.                     \tag{2.26}
\]

Thus Corollary 2.3 is exactly the first projection of the hierarchy.

Iterating (2.17) gives a particularly clean fixed-rank statement.  Every
coefficient at every branch is nonnegative, and the two outgoing
coefficients sum to one.  Therefore, whenever all indicated ranks are
proper,

\[
 \boxed{
 \varepsilon_{r,0}^{(t)}
 \le\max_{0\le j\le t}\varepsilon_{r-j,j}^{(0)}.}
 \tag{2.27}
\]

The actual expression is a convex combination, with weights obtained from
the two choices in (2.17).  Formula (2.27) is the exact inductive gain and
the exact obstruction: there is no error amplification at one rank, but
each lift consumes one further order of canonical top-boundary incidence.

## 3. Shallow-shadow form and aggregate recurrence

Now put

\[
 n=2m,\qquad M=m+H,\qquad H=o(m).                       \tag{3.1}
\]

Use the notation

\[
 \varepsilon_0=\varepsilon_m,\qquad
 \varepsilon_q^- =\varepsilon_{m-q},\qquad
 \varepsilon_q^+ =\varepsilon_{m+q}.                  \tag{3.2}
\]

Substitution in (2.10) gives (0.2)--(0.4).  Notice the direction of the
transport:

* the new middle profile is inherited principally from the old lower
  depth-one profile;
* the new lower depth \(q\) profile is inherited principally from old lower
  depth \(q+1\);
* the new upper depth \(q\) profile is inherited principally from old upper
  depth \(q-1\).

Thus one top-size lift consumes one additional lower shadow layer.  It does
not preserve a symmetric depth-\(Q\) invariant unless the input controls the
asymmetric interval of ranks

\[
 [m-Q-1,m+Q].                                          \tag{3.3}
\]

For any integer interval \([a,b]\subset[2,M-1]\), summing (2.10) gives

\[
 \begin{aligned}
 \sum_{r=a}^b\varepsilon_r^+
 &\le {a\over M+1}\varepsilon_{a-1}
      +{M-b+1\over M+1}\varepsilon_b\\
 &\quad+{M+2\over M+1}\sum_{r=a}^{b-1}\varepsilon_r
      +\sum_{r=a}^b {r\over M+1}\chi_{r-1}.
 \end{aligned}                                         \tag{3.4}
\]

In particular,

\[
 \boxed{
 \sum_{r=a}^b\varepsilon_r^+
 \le\left(1+{1\over M+1}\right)
       \sum_{r=a-1}^b\varepsilon_r
       +\sum_{s=a-1}^{b-1}\chi_s.}
 \tag{3.5}
\]

The factor in (3.5) is essentially lossless.  If the canonical fractional
lift is iterated \(t\) times, backward expansion of the output rank interval
by one lower rank at each step gives

\[
 \prod_{j=0}^{t-1}\left(1+{1\over M+j+1}\right)
 ={M+t+1\over M+1}.                                   \tag{3.6}
\]

Hence, for \(t=o(M)\), the deterministic amplification of aggregate profile
error is \(1+o(1)\).  More precisely, if
\(\mathcal K_j\) denotes the sum of the relevant \(\chi\)-errors at stage
\(j\), then the stage-\(t\) error on \([a,b]\) is at most

\[
 {M+t+1\over M+1}
 \left(
    \sum_{r=a-t}^b\varepsilon_r^{(0)}
    +\sum_{j=0}^{t-1}\mathcal K_j
 \right).                                             \tag{3.7}
\]

Equation (3.7) is a genuine stable recurrence, but only for the strengthened
joint invariant.  Ordinary shadow-profile errors alone leave the
\(\mathcal K_j\)'s uncontrolled.

## 4. The scalar calibration horizon

Even perfect profile transport cannot overcome loss of total owner mass.
Let

\[
 L_j=(M+j)\binom n{M+j}.                               \tag{4.1}
\]

Then

\[
 {L_{j+1}\over L_j}={n-M-j\over M+j}.                  \tag{4.2}
\]

For \(n=2m\), \(M=m+H\),

\[
 {L_t\over L_0}
 =\prod_{j=0}^{t-1}{m-H-j\over m+H+j}.                 \tag{4.3}
\]

If \(H+t=o(m)\), Taylor expansion gives

\[
 \log{L_t\over L_0}
 =-{2Ht+t(t-1)\over m}
  +O\!\left({t(H+t)^3\over m^3}\right).               \tag{4.4}
\]

Consequently, a calibrated starting mass

\[
 L_0=(1-o(1))\binom{2m}m                              \tag{4.5}
\]

remains \((1-o(1))\binom{2m}m\) through \(t\) top-size lifts whenever

\[
 Ht+t^2=o(m).                                          \tag{4.6}
\]

For the calibrated value \(H\asymp\sqrt{m\log m}\), this permits

\[
 t=o\!\left(\sqrt{m/\log m}\right),                  \tag{4.7}
\]

but not a macroscopic run of top-size induction.  In particular, one step
has

\[
 L_1=L_0{m-H\over m+H}
     =L_0\left(1-O(H/m)\right),                        \tag{4.8}
\]

so it does preserve calibrated owner capacity.

## 5. Conditional integral lifting theorem

The construction in Section 2 is fractional at each child top.  An integral
lift chooses one deletion-gap route for every
\(T\in\binom X{M+1}\).  Let \(\widetilde\mu_r^+\) be its interval profile and
put

\[
 \delta_r={1\over L_{M+1}}
 \sum_{A\in\binom Xr}|\widetilde\mu_r^+(A)-\mu_r^+(A)|.
 \tag{5.1}
\]

This is a correlated-rounding discrepancy.  Independent choices are not
being asserted to make it small.

### Theorem 5.1 (one-step calibrated lift, conditional form)

Suppose \(n=2m\), \(M=m+H\), \(H=o(m)\), and

\[
 L_M\le W,\qquad L_M=(1-o(1))W,\qquad
 W=\binom{2m}m.                                         \tag{5.2}
\]

Let \(Q\le H-1\).  Assume

\[
 \sum_{r=m-Q-1}^{m+Q}\varepsilon_r=o(1),               \tag{5.3}
\]

\[
 \sum_{s=m-Q-1}^{m+Q-1}\chi_s=o(1),                   \tag{5.4}
\]

and that one deletion-gap route can be selected at every child top so that

\[
 \sum_{r=m-Q}^{m+Q}\delta_r=o(1).                      \tag{5.5}
\]

Then the integral child packet system has

\[
 \sum_{r=m-Q}^{m+Q}{1\over L_{M+1}}
 \sum_{A\in\binom Xr}
 |\widetilde\mu_r^+(A)-\bar\mu_r^+|=o(1).              \tag{5.6}
\]

In particular, its middle owner collision is \(o(W)\), and the total number
of uncovered targets over all ranks \(m-Q,\ldots,m+Q\) is \(o(W)\).

#### Proof

The triangle inequality adds \(\delta_r\) to (2.10).  Sum over the output
band and apply (3.5), (5.3), (5.4), and (5.5), proving (5.6).

By (4.8) and (5.2), \(L_{M+1}=(1-o(1))W\).  Also
\(\binom{2m}r\le W\), so every output mean
\(\bar\mu_r^+=L_{M+1}/\binom{2m}r\) is at least \(1-o(1)\).  Every uncovered
target contributes \(\bar\mu_r^+\) to the corresponding \(L^1\) error.
Thus their aggregate number is \(o(W)\).

At the middle rank \(L_{M+1}\le W\), since \(M>m\) and the calibrated
starting mass is at most \(W\).  If \(h_0\) is the number of middle holes and
\(C_0\) the number of repeated middle occurrences, then

\[
 C_0=L_{M+1}-(W-h_0)\le h_0=o(W).                      \tag{5.7}
\]

This proves the last assertion. \(\square\)

The theorem isolates two distinct unsolved inputs:

1. propagation or construction of the joint covariance bounds (5.4);
2. a childwise correlated rounding satisfying (5.5).

Neither follows from marginal packet balance.  The canonical fractional
part, including the exact recurrence and its stable iteration, is fully
proved.

## 6. Why a direct \(2m\to2m+2\) one-layer lift cannot work

Add two new points \(a,b\) and retain the same depth \(H\).  The new middle
rank is \(m+1\), and the new top size is

\[
 M^+=(m+1)+H=M+1.                                      \tag{6.1}
\]

Partition the new tops \(T\in\binom{X\cup\{a,b\}}{M+1}\) by
\(j=|T\cap\{a,b\}|\).  The three class sizes are

\[
 \binom n{M+1},\qquad 2\binom nM,\qquad \binom n{M-1}.
 \tag{6.2}
\]

Only the middle class has the form \(U\cup\{a\}\) or \(U\cup\{b\}\) with
an old \(M\)-top \(U\).  Relative to \(\binom nM\), the total number of new
tops is

\[
 {n-M\over M+1}+2+{M\over n-M+1}.                      \tag{6.3}
\]

With \(n=2m\), \(M=m+H\), \(H=o(m)\), (6.3) is \(4+O(H/m)\).  Therefore the
one-new-point class has proportion

\[
 {2\over (n-M)/(M+1)+2+M/(n-M+1)}
 ={1\over2}+O(H/m),                                    \tag{6.4}
\]

which proves (0.5).

There is also an internal profile warning even on this middle class.  Insert
\(a\) into a cyclic order on an old \(M\)-top.  Among the \(M+1\) new middle
windows of length \(m+1\), exactly \(m+1\) contain \(a\) and exactly \(H\)
avoid it.  After deletion of \(a\), the first group becomes selected old
middle \(m\)-intervals, while the second group is made of old upper
depth-one \((m+1)\)-intervals.  Which intervals occur is determined by the
same insertion cut.  Thus even the liftable half of the top tags couples
owners to first shadows fibrewise; separate balance estimates cannot be
multiplied.

The other two top classes in (6.2) naturally call for old cyclic-order data
at top sizes \(M+1\) and \(M-1\), respectively.  Hence an ambient-dimension
induction must be triangular: three adjacent old top-size rows feed one new
row, together with compatible insertion cuts.  The top-size theorem above
provides one edge of that triangle, but not the full ambient lift.

## 7. Audit ledger

### Proved

1. The canonical deletion--insertion kernel has total weight one at every
   child top.
2. The exact joint profile identity is (2.4).
3. The exact normalized recurrence is (2.9); (2.10) follows from the
   explicitly defined covariance defect, not from independence.
4. The full \(k\)-boundary Pascal hierarchy is (2.17); after \(t\) lifts,
   every fixed-rank error is bounded by (2.27).
5. The middle/lower/upper shallow recurrences are (0.2)--(0.4).
6. Aggregate profile error amplifies by at most the telescoping factor
   \((M+t+1)/(M+1)\), apart from accumulated covariance errors.
7. Calibrated total owner mass survives \(t\) lifts throughout the
   asymptotic range \(Ht+t^2=o(m)\).
8. Under joint covariance and correlated-rounding hypotheses, Theorem 5.1
   gives an integral near-transversal with aggregate shallow-shadow holes
   \(o(W)\).
9. A direct one-layer \(2m\to2m+2\) lift addresses only
   \(1/2+o(1)\) of the new top tags.

### Not proved

1. Marginal shallow-shadow balance does not imply \(\chi_s=o(1)\).
2. No integral route selection with \(\sum_r\delta_r=o(1)\) is proved here.
3. No compatible three-top-size construction for the full ambient
   \(2m\to2m+2\) lift is proved.
4. Consequently, this note is a rigorous fractional lift and a conditional
   integral lift, not a proof of the calibrated top-packet near-factor.
