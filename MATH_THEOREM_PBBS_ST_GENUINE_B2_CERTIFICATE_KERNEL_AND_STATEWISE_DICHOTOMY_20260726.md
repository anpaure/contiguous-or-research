# The genuine PBBS \(B_2\)-certificate kernel and the statewise clustering dichotomy

Date: 2026-07-26

Method: pure mathematics only.  No profile envelope, independent marginal,
probabilistic surrogate, computation, or external input is used.

> **Correction (2026-07-26).**  The general certificate partition below is
> exact, but genuine no-wrap PBBS makes every nonempty terminal-hit
> certificate cluster a singleton.  Indeed the equivariant minimal peak
> expansion realizes the terminal-zero return at every reduced active
> phase.  If two phases shared their first two predecessor hits, their
> parent returns would have the same first-return endpoint, contradicting
> firstness for the earlier phase.  Thus, in the regime used here,
>
> \[
> c_\gamma=1,\qquad \mathscr I_H=0,
> \qquad \Delta_H(t)=\xi_H(t).
> \]
>
> The terminal-bunching branch discussed in Sections 0, 5, and 6 is
> therefore not a genuine PBBS alternative.  It remains a valid formal
> decomposition for an arbitrary marked renewal word, but PBBS occupies
> only its singleton-cluster face.  The complete proof and corrected
> implication boundary are in
> `MATH_THEOREM_PBBS_ST_B2_CERTIFICATE_SINGLETON_AND_CROSS_GATE_20260726.md`.

## 0. Result

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
 \qquad G=2H-1,\qquad h=H+1.                    \tag{0.1}
\]

For a reduced root \(F\), the genuine predecessor predicate is

\[
 a_H(F)=\mathbf1_{\{B_2(F)\le G\}}.             \tag{0.2}
\]

This note gives an exact two-time kernel for

\[
 a_H(F)a_H(\tau^uF),\qquad1\le u\le h,           \tag{0.3}
\]

using the actual selected-particle word.  It also gives a statewise
necessary-and-sufficient decomposition of bounded versus divergent
short-lag degree.

Work first on one persistent-label augmentation of a reduced PBBS orbit.
Let \({\cal U}\) be the one-step labelled PBBS map, let
\(\tau={\cal U}^2\), and let

\[
 x_t={\cal U}^{2t}x_0\qquad(t\in\mathbb Z/\ell\mathbb Z)       \tag{0.4}
\]

be one \(\tau\)-orbit.  Write \(\kappa_n\) for the persistent equality
particle selected at the one-step state \({\cal U}^nx_0\).  If the
current particle at quotient phase \(t\) is

\[
 a_t=\kappa_{2t},\qquad b_t=a_t-1,               \tag{0.5}
\]

let

\[
 T_1(t)<T_2(t)                                   \tag{0.6}
\]

be the first two selections of particle \(b_t\) strictly after time
\(2t\).  The exact predecessor theorem says

\[
 \boxed{a_H(x_t)=1\iff T_2(t)-2t\le G.}          \tag{0.7}
\]

Every active phase therefore has the unique **terminal-hit certificate**

\[
 \gamma(t)=\bigl(b_t,T_1(t),T_2(t)\bigr),        \tag{0.8}
\]

with hit times read modulo the period \(2\ell\).  Let

\[
 \Gamma_\gamma=\{t:a_H(x_t)=1,\ \gamma(t)=\gamma\},
 \qquad c_\gamma=|\Gamma_\gamma|.               \tag{0.9}
\]

These sets partition the genuine active phases.  More explicitly, if

\[
 \cdots<r_{b,i-1}<r_{b,i}<r_{b,i+1}<\cdots       \tag{0.10}
\]

are the one-step selection times of particle \(b\), then

\[
 \boxed{
 \Gamma_{b,i}=left\{t:
 \begin{array}{l}
 r_{b,i-1}<2t<r_{b,i},\quad \kappa_{2t}=b+1,\\
 r_{b,i+1}-2t\le G
 \end{array}\right\}.}
                                                               \tag{0.11}
\]

Thus (0.11) contains both terminal \(B_2\) thresholds literally: the
first future hit is \(r_{b,i}\), the second is \(r_{b,i+1}\), and no
independently transported event has been inserted.

The certificate clusters have the decisive geometric property

\[
 \boxed{\operatorname {diam}(\Gamma_\gamma)\le H-1.}          \tag{0.12}
\]

Indeed every \(2t\) in one cluster lies in the common interval

\[
 [T_2-G,T_1),                                    \tag{0.13}
\]

whose length is strictly smaller than \(G\).

Assume \(\ell>2h\); the complementary short-orbit sector has negligible
Pascal weight in the saddle.  Define the exact cluster-pair kernel

\[
 \boxed{
 {\cal K}_H(\gamma,\eta)
 =\sum_{u=1}^{h}
   |\Gamma_\gamma\cap(\Gamma_\eta-u)|.}          \tag{0.14}
\]

Then the orbit contribution to the genuine reduced two-time count is

\[
 \boxed{
 K_H({\cal O})=\sum_{\gamma,\eta}{\cal K}_H(\gamma,\eta).}    \tag{0.15}
\]

The diagonal entries are evaluated exactly:

\[
 \boxed{{\cal K}_H(\gamma,\gamma)=\binom{c_\gamma}{2}.}       \tag{0.16}
\]

Consequently

\[
 \boxed{
 K_H({\cal O})
 =\sum_\gamma\binom{c_\gamma}{2}+X_H({\cal O}),}             \tag{0.17}
\]

where the cross-certificate energy

\[
 X_H({\cal O})
 :=\sum_{\gamma\ne\eta}{\cal K}_H(\gamma,\eta)\ge0          \tag{0.18}
\]

is exact.  There is no cancellation between the two terms.

There is also a pointwise version.  For an active phase \(t\), put

\[
 \begin{aligned}
 \xi_H(t)=\sum_{u=1}^{h}\big(&a_H(x_{t+u})
       \mathbf1_{\{\gamma(t+u)\ne\gamma(t)\}}\\
   +&a_H(x_{t-u})
       \mathbf1_{\{\gamma(t-u)\ne\gamma(t)\}}\big).
 \end{aligned}                                   \tag{0.19}
\]

Its genuine two-sided reduced phase degree is exactly

\[
 \boxed{
 \Delta_H(t)=c_{\gamma(t)}-1+\xi_H(t).}          \tag{0.20}
\]

Equations (0.17) and (0.20) are the requested statewise
bounded/divergent theorem.  They show that there are exactly two possible
sources of divergence:

1. **terminal bunching:** the size-biased certificate size
   \(c_{\gamma(t)}\) diverges;
2. **cross-certificate interlacing:** phases in many distinct
   predecessor-hit certificates enter the same short-lag window, making
   \(\xi_H(t)\) diverge.

No third mechanism exists.

After summing all augmented orbits with their exact inverse-Pascal weights,
define

\[
 \mathscr I_H
 =\sum_{\cal O}w_{\cal O}\sum_\gamma
            c_\gamma(c_\gamma-1),               \tag{0.21}
\]

\[
 \mathscr X_H
 =2\sum_{\cal O}w_{\cal O}X_H({\cal O}),        \tag{0.22}
\]

where

\[
 w_{\cal O}=\frac1{2d+1}
 \binom{m+d-k}{2d}                               \tag{0.23}
\]

on an augmented rank-\(d\), peak-\(k\) orbit.  If
\(\mathscr R_H\) and \(\mathscr C_H\) are the genuine Pascal-weighted
reduced one- and two-time counts, then, after the negligible short-orbit
deletion,

\[
 \boxed{
 2\mathscr C_H=\mathscr I_H+\mathscr X_H,
 \qquad
 \mathscr R_H=\sum_{\cal O}w_{\cal O}\sum_\gamma c_\gamma.}   \tag{0.24}
\]

Therefore

\[
 \boxed{
 \frac{\mathscr C_H}{\mathscr R_H}=O(1)
 \iff
 \mathscr I_H=O(\mathscr R_H)
 \text{ and }
 \mathscr X_H=O(\mathscr R_H).}                 \tag{0.25}
\]

Likewise

\[
 \boxed{
 \frac{\mathscr C_H}{\mathscr R_H}\longrightarrow\infty
 \iff
 \frac{\mathscr I_H+\mathscr X_H}{\mathscr R_H}
       \longrightarrow\infty.}                 \tag{0.26}
\]

The statewise, rather than mean, positive requirement has the exact form

\[
 \boxed{
 \forall K<\infty,\quad
 \sum_{\cal O}w_{\cal O}
 \#\{t:a_H(x_t)=1,\ c_{\gamma(t)}-1+\xi_H(t)\le K\}
 =o(B_m/H).}                                     \tag{0.27}
\]

At critical active mass, failure of (0.27) for one fixed \(K\) gives a
physical \(\Omega(B_m\sqrt m)\) packing obstruction by the established
degree pullback.  Conversely, if \(ST_A\) holds, (0.27) is necessary.

The new structural conclusion is sharper.  Fix \(M<\infty\).  If a
positive critical mass lies in certificate clusters of size at most
\(M\), then \(ST_A\) can hold only if, on that mass,

\[
 \boxed{\xi_H(t)\longrightarrow\infty
 \quad\text{in Pascal-weighted probability}.}    \tag{0.28}
\]

Thus the only escape from terminal bunching is a literal interlacing of
unboundedly many **different** predecessor labels/hit pairs in almost every
Gaussian window.  This is the exact minimal remaining PBBS pattern.

The theorem does not decide whether the actual Pascal-saddle orbits exhibit
that interlacing.  It does reduce the genuine gate from an undifferentiated
autocorrelation to the two explicit nonnegative statistics
\(\mathscr I_H\) and \(\mathscr X_H\).

## 1. Exact two-hit certificates

Fix reduced rank \(d\) and put \(p=2d+1\).  Use persistent cyclic labels
\(\mathbb Z_p\) on the equality particles.  The augmented labelled PBBS
state space is conjugate to \(\binom{[p]}d\).  Let \({\cal U}\) denote
its one-step permutation, and let \(\kappa_n\) be the selected persistent
label at time \(n\).

Take one orbit of \({\cal U}^2\), of length \(\ell\).  The sequence
\(\kappa_n\) may be read on the universal cover \(n\in\mathbb Z\) and is
periodic with period \(2\ell\), whether or not that is its least period.

At quotient phase \(t\), the current selected label is \(a_t=\kappa_{2t}\).
Its immediate predecessor is \(b_t=a_t-1\).  List the positive future
selections of \(b_t\) after time \(2t\).  Their first two times are
\(T_1(t),T_2(t)\).

### Theorem 1.1 (literal \(B_2\) indicator)

Equation (0.7) holds.

#### Proof

By definition, \(B_1\) and \(B_2\) are the first and second positive
selection times of the immediate predecessor of the time-zero selected
particle.  Starting the same persistent-label process at time \(2t\),
those relative times are exactly

\[
 T_1(t)-2t,\qquad T_2(t)-2t.
\]

Therefore \(B_2\le G\) is exactly (0.7).  No outer slot or marginal event
appears. \(\square\)

Now fix a label \(b\), and list all of its selection times as in (0.10),
with

\[
 r_{b,i+q_b}=r_{b,i}+2\ell.                      \tag{1.1}
\]

If \(\kappa_{2t}=b+1\), there is a unique \(i\) for which

\[
 r_{b,i-1}<2t<r_{b,i}.                           \tag{1.2}
\]

The first two future \(b\)-hits are then \(r_{b,i}\) and
\(r_{b,i+1}\).  Theorem 1.1 makes the active condition

\[
 r_{b,i+1}-2t\le G.                              \tag{1.3}
\]

This proves the cluster formula (0.11) and proves that its nonempty sets
partition the active phases.

The cluster size is consequently the exact marked-suffix occupancy

\[
 \boxed{
 c_{b,i}
 =\#\left\{t:
 \begin{array}{l}
 r_{b,i-1}<2t<r_{b,i},\quad\kappa_{2t}=b+1,\\
 2t\ge r_{b,i+1}-G
 \end{array}\right\}.}                          \tag{1.4}
\]

This is the even-phase version of the predecessor terminal-suffix formula.
It retains the missing successor-placement coordinate exactly.

### Lemma 1.2 (certificate diameter)

Equation (0.12) holds.

#### Proof

Every \(2t\in\Gamma_{b,i}\) satisfies

\[
 r_{b,i+1}-G\le2t<r_{b,i}.
\]

Since \(r_{b,i+1}>r_{b,i}\), the containing interval has length strictly
less than \(G=2H-1\).  The difference of two even integers in it is at
most \(2H-2\).  Dividing by two gives quotient diameter at most
\(H-1\). \(\square\)

## 2. The exact two-time convolution kernel

On \(\mathbb Z/\ell\mathbb Z\), write

\[
 A(t)=a_H(x_t).
\]

The orbit contribution to the reduced forward correlation is

\[
 K_H({\cal O})
 =\sum_{u=1}^{h}\sum_{t\in\mathbb Z/\ell\mathbb Z}
 A(t)A(t+u).                                     \tag{2.1}
\]

Since the certificate clusters partition \(\{t:A(t)=1\}\), expand both
indicators in (2.1):

\[
 A(t)=\sum_\gamma\mathbf1_{\Gamma_\gamma}(t).
\]

Interchanging the finite sums gives (0.14)--(0.15).

### Theorem 2.1 (diagonal certificate kernel)

If \(\ell>2h\), then (0.16)--(0.17) hold.

#### Proof

By Lemma 1.2, one may cut the orbit outside the interval containing one
cluster \(\Gamma_\gamma\); its linear diameter is at most \(H-1<h\).
Every unordered pair of distinct phases in that cluster has one positive
linear displacement in \(\{1,\ldots,h\}\).  The reverse cyclic
displacement is larger than \(h\), because \(\ell>2h\).  Thus every
unordered pair contributes exactly once to

\[
 \sum_{u=1}^{h}|\Gamma_\gamma\cap
                       (\Gamma_\gamma-u)|,
\]

proving (0.16).  Separate the terms \(\gamma=\eta\) and
\(\gamma\ne\eta\) in (0.15) to obtain (0.17). \(\square\)

The off-diagonal kernel is also completely explicit:

\[
 \boxed{
 {\cal K}_H((b,i),(c,j))
 =\sum_{u=1}^{h}
 \#\left\{t:
 \begin{array}{l}
 t\in\Gamma_{b,i},\\
 t+u\in\Gamma_{c,j}
 \end{array}\right\}.}                          \tag{2.2}
\]

Substituting (0.11) in both rows of (2.2) is an exact four-hit condition:
two consecutive hits of \(b\) certify the first phase, and two consecutive
hits of \(c\) certify the second.  The two marked successor conditions are
\(\kappa_{2t}=b+1\) and \(\kappa_{2t+2u}=c+1\).  Thus (2.2) is the full
two-time predecessor kernel requested in the task.  Its remaining datum is
the actual relative alignment of the \(b\)- and \(c\)-renewal blocks.

## 3. Pointwise degree identity

For an active phase \(t\), its two-sided active-phase degree is

\[
 \Delta_H(t)=\sum_{u=1}^{h}\bigl(A(t+u)+A(t-u)\bigr).         \tag{3.1}
\]

The condition \(\ell>2h\) ensures that the displayed neighbouring phases
are distinct and that no phase is counted in both directions.

The other \(c_{\gamma(t)}-1\) members of its own certificate cluster all
lie within distance \(H-1\) by Lemma 1.2.  They therefore all occur in
(3.1).  Every remaining term in (3.1) belongs to a different certificate
and is counted by (0.19).  This proves (0.20).

Summing (0.20) over the active phases gives the finite identity

\[
 \sum_{t:A(t)=1}\Delta_H(t)
 =\sum_\gamma c_\gamma(c_\gamma-1)+2X_H({\cal O})
 =2K_H({\cal O}).                                \tag{3.2}
\]

The first equality is statewise; the second is the usual reversal of the
forward lag.  In particular, large scalar autocorrelation cannot cancel
between terminal bunching and cross-certificate interlacing.

There is a sharp certificate-compression consequence.  Put

\[
 R_{\cal O}=\sum_\gamma c_\gamma,
 \qquad
 q_{\cal O}=|\{\gamma:c_\gamma>0\}|.
\]

Cauchy--Schwarz gives

\[
 \boxed{
 \sum_\gamma\binom{c_\gamma}{2}
 \ge\frac12\left(\frac{R_{\cal O}^2}{q_{\cal O}}
                         -R_{\cal O}\right).}    \tag{3.3}
\]

Thus \(R_{\cal O}/q_{\cal O}\to\infty\) forces divergent mean degree
already inside the same-certificate term.  Equality in (3.3) occurs
exactly when the nonempty certificate clusters have equal sizes.  This is
a statewise statement on one actual PBBS orbit, not an averaged marginal.

## 4. Exact Pascal-weighted summation

For a reduced normalized root of rank \(d\), peak count \(k\), the exact
outer inverse-fibre weight is

\[
 P_m(d,k)=\binom{m+d-k}{2d}.                     \tag{4.1}
\]

It is constant along every augmented PBBS orbit.  Every normalized reduced
root has \(2d+1\) cyclic persistent-label augmentations.  Therefore the
correct orbit weight in the augmented trace is (0.23).

The exact trace formulas for the reduced process give

\[
 \mathscr R_H
 =\sum_{\cal O}w_{\cal O}
    \#\{t\in{\cal O}:A(t)=1\},                   \tag{4.2}
\]

\[
 \mathscr C_H
 =\sum_{\cal O}w_{\cal O}K_H({\cal O}).         \tag{4.3}
\]

Use the cluster partition in (4.2) and Theorem 2.1 in (4.3).  This proves
(0.24).

The already established Pascal short-period bound removes all augmented
\(\tau\)-orbits of length at most \(2h\) at total weight

\[
 o(B_m/H).                                       \tag{4.4}
\]

Hence (0.24) is exact up to an error negligible at the requested critical
scale.  No statement about a formal inverse tower is used.

Because \(\mathscr I_H,\mathscr X_H\ge0\), equation (0.24) immediately
proves (0.25)--(0.26).

## 5. Statewise bounded/divergent alternatives

Choose an active augmented phase with probability proportional to its
exact Pascal orbit weight.  Let

\[
 C_*=c_{\gamma(t)},\qquad X_*=\xi_H(t).           \tag{5.1}
\]

Equation (0.20) is the almost-sure identity

\[
 \boxed{\Delta_H=C_*-1+X_*.}                    \tag{5.2}
\]

It yields the following exact theorem.

### Theorem 5.1 (statewise dichotomy)

Assume \(\mathscr R_H\ge\kappa B_m/H\) along a subsequence.

1. If there are fixed \(K<\infty\) and \(\delta>0\) such that

   \[
   \Pr\{C_*-1+X_*\le K\mid a_H=1\}\ge\delta                 \tag{5.2a}
   \]

   along a subsequence, then that bounded-degree stratum has Pascal mass
   \(\Omega(B_m/H)\).  The degree pullback gives

   \[
   \overline\nu_H=\Omega(B_m/H),
   \qquad
   \nu_H=\Omega(B_m\sqrt m),                     \tag{5.3}
   \]

   so \(ST_A\) is false.

2. If \(ST_A\) is true, then (0.27) holds.  Equivalently,

   \[
   C_*+X_*\longrightarrow\infty                 \tag{5.4}
   \]

   in Pascal-weighted probability conditional on activity.

3. For every fixed \(M\), on the stratum \(C_*\le M\), conclusion
   (5.4) is equivalent to

   \[
   X_*\longrightarrow\infty.                    \tag{5.5}
   \]

   Thus any positive critical mass of bounded certificate size forces the
   cross-certificate interlacing law (0.28).

#### Proof

For item 1, (5.2a) and the assumed lower bound on \(\mathscr R_H\) give
critical Pascal mass on \(\{C_*-1+X_*\le K\}\).  Equation (5.2)
identifies this with a genuine
bounded \(\Delta_H\) stratum.  Apply the established terminal-zero degree
pullback and then the \(N\)-fold spatial deck lift to obtain (5.3).

Item 2 is the contrapositive, simultaneously for every fixed \(K\), and
is exactly (0.27).  On \(C_*\le M\), the difference between \(\Delta_H\)
and \(X_*\) is bounded by \(M-1\); this proves item 3. \(\square\)

There is also a mean version.  Under the active Palm law,

\[
 \mathbb E(C_*-1)=\frac{\mathscr I_H}{\mathscr R_H},
 \qquad
 \mathbb EX_*=\frac{\mathscr X_H}{\mathscr R_H}.              \tag{5.6}
\]

Thus bounded mean susceptibility is equivalent to both Palm means being
bounded.  Divergence of only their sum is not sufficient for \(ST_A\),
because it may be carried by a small exceptional mass; the probability
statement in Theorem 5.1 is the correct necessary condition.

## 6. What the theorem eliminates

The exact decomposition rules out several incomplete routes.

1. A two-hit marginal for one predecessor label controls only the cluster
   sizes \(c_\gamma\).  It does not control \(\mathscr X_H\).
2. A one-particle gap histogram determines the interval in (0.11) but not
   the marked successor placements \(\kappa_{2t}=b+1\).
3. Even every within-label terminal bunching moment can remain bounded
   while cross-certificate interlacing makes the degree diverge.
4. Conversely, large terminal clusters alone can make the scalar mean
   diverge on a sparse mass and still leave a critical bounded-degree
   sector.

The genuine positive route has therefore narrowed to one of two statements:

\[
 C_*\longrightarrow\infty
 \quad\text{in probability},                    \tag{6.1}
\]

or, on every nonnegligible bounded-\(C_*\) stratum,

\[
 X_*\longrightarrow\infty
 \quad\text{in probability}.                    \tag{6.2}
\]

The genuine negative route is equally exact: find fixed \(M,K\) and
critical Pascal mass satisfying

\[
 C_*\le M,\qquad X_*\le K.                      \tag{6.3}
\]

Equation (6.3), not a product of marginal estimates, gives the desired
bounded-degree obstruction.

## 7. Final boundary

Proved here:

1. the literal two-hit certificate (0.7)--(0.11);
2. the exact two-time convolution kernel (0.14)--(0.15), with both
   \(B_2\) predicates present;
3. the exact diagonal evaluation \(\binom{c_\gamma}{2}\);
4. the nonnegative same-certificate/cross-certificate decomposition
   (0.17);
5. the pointwise degree identity (0.20);
6. the Pascal-weighted identity (0.24); and
7. the statewise alternatives (0.27)--(0.28).

Not proved here:

1. critical abundance \(\mathscr R_H=\Omega(B_m/H)\);
2. boundedness of both \(\mathscr I_H\) and \(\mathscr X_H\);
3. probability divergence of terminal certificate sizes; or
4. probability divergence of cross-certificate interlacing on the
   bounded-size strata.

The smallest remaining asymptotic is now the marked cross-renewal kernel
\(\mathscr X_H\).  A proof must control the simultaneous alignment of
different persistent predecessor labels in (2.2).  Same-label renewal
data, scalar Kac sums, and terminal \(B_2\) marginals do not contain that
alignment.
