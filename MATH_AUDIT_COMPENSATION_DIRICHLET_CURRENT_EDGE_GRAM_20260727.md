# Compensation Dirichlet energy under current-edge sampling

Date: 2026-07-27

Method: pure mathematics only.  No computation, search, solver,
independence heuristic, or web input is used.

## 0. Verdict

Fix a live physical pair profile \(S\) in the compensated
\(r\)-uniform residual and put

\[
                         b=r-2.
\tag{0.1}
\]

The compensation part of the centered child energy has an exact
pairwise Gram representation.  Its clock contributes the factor
\(1/r\), but current-edge sampling does **not** automatically contribute
another \(1/b\).

There are two exact reasons.

1. The centered Hilbert energy uses the static child weights
   \(p_a\), while sampling a current edge through \(S\) gives the
   current size-biased weights \(\pi_a\).  The Radon--Nikodym derivative
   is the current normalized child profile \(X_a\).  The exact Gram
   therefore contains the ratios \(X_a/X_{a'}\); it is not the
   unweighted physical theta kernel unless the child profiles are
   already flat.

2. Even in the flat case, the Dirichlet form is a harmonic current
   collision statistic: after expansion it contains \(B_{ay}^2/A_a\).
   The proved physical theta theorem bounds polynomial mixed-diagram
   numerators in the static catalogue.  It has no reciprocal current
   child-link denominator.  Static numerator control is not hereditary
   under restriction after division by \(A_a\).

The whole-arm PSF theorem does not bridge this gap.  It is an upper
bound on common future events of two displayed arms.  The compensation
Dirichlet form is largest when the child coin-decrement vectors are
orthogonal, precisely when common-event upper bounds are cheapest.

Consequently the existing theta and PSF theorems do not prove the
desired incidence-aggregate estimate

\[
 \boxed{
 Q_S^{\rm coin}\ \lesssim\ {L^C\over r(r-2)}.}
\tag{0.2}
\]

What they do isolate is the exact missing statement: a dynamic,
incidence-weighted conditional mixing bound for the child-to-coin
kernel under the independent current-child product law.  Formula
(CCM) below is the sharp version.  It is strictly different from PSF
and from the existing polynomial theta estimate.

This note does not construct an induced physical residual violating
(0.2).  It proves that the proposed deduction from the two stated
inputs is invalid and identifies the additional theorem which would
make it valid.

## 1. Static and current child laws

Let

\[
 N=d_t(S),\qquad
 A_a=d_t(S\cup\{a\}),\qquad
 B_{a y}=d_t(S\cup\{a,y\}),
\tag{1.1}
\]

where \(a,y\notin S\), \(a\ne y\), and a quantity is zero if its
profile is not live.  Double counting a current row through \(S\) and
one of its \(b\) remaining resources gives

\[
                         \sum_a A_a=bN.
\tag{1.2}
\]

Hence

\[
                         \pi_a={A_a\over bN}
\tag{1.3}
\]

is a probability law.  It has the following literal sampling
interpretation:

1. choose \(F\) uniformly from the current \(S\)-link;
2. choose \(A\) uniformly from \(F\setminus S\).

Then

\[
                         \Pr(A=a)=\pi_a.
\tag{1.4}
\]

The Hilbert energy in the stopped-profile argument instead uses

\[
 p_a={d_0(S\cup\{a\})\over b\,d_0(S)}.
\tag{1.5}
\]

Write

\[
 X_S={d_t(S)\over d_0(S)u^b},\qquad
 X_a={d_t(S\cup\{a\})
          \over d_0(S\cup\{a\})u^{b-1}}.
\tag{1.6}
\]

The exact parent--child identity is

\[
                         p_aX_a=uX_S\pi_a.
\tag{1.7}
\]

Thus current-edge sampling gives \(p\) only after the importance
weight \(uX_S/X_a\).  No lower profile stop presently bounds this
weight.

## 2. Exact coin decrement and centered variance

A compensation coin at \(y\) kills precisely the current rows in the
\((S,a)\)-link which also contain \(y\).  Its decrement in the
survival-normalized child coordinate is

\[
 h_y(a)
 ={B_{a y}\over d_0(S\cup\{a\})u^{b-1}}
 =X_a\vartheta_y(a),
\qquad
 \vartheta_y(a):={B_{a y}\over A_a}.
\tag{2.1}
\]

Set \(\vartheta_y(a)=0\) when \(A_a=0\), and also set
\(\vartheta_y(y)=0\).  The case \(a=y\) is a terminal coordinate
deletion and is favorable.  It is removed before centering.  Put

\[
 {\cal A}_y=\{a:A_a>0,\ a\ne y\},\qquad
 P_y=\sum_{a\in{\cal A}_y}p_a,
\tag{2.2}
\]

and

\[
 \bar h_y={1\over P_y}\sum_{a\in{\cal A}_y}p_ah_y(a).
\tag{2.3}
\]

The exact compensation carré-du-champ is

\[
 Q_S^{\rm coin}
 =\sum_y\chi_y
   \sum_{a\in{\cal A}_y}p_a\bigl(h_y(a)-\bar h_y\bigr)^2,
\tag{2.4}
\]

where

\[
                         0\le\chi_y\le {1\over r}.
\tag{2.5}
\]

For weights of total mass \(P\),

\[
 \sum_aw_a(f_a-\bar f)^2
 ={1\over2P}\sum_{a,a'}w_aw_{a'}(f_a-f_{a'})^2.
\tag{2.6}
\]

Applying (2.6) to every coin gives the requested exact
\((a,a')\)-form:

\[
 \boxed{
 Q_S^{\rm coin}
 ={1\over2}\sum_y{\chi_y\over P_y}
 \sum_{a,a'\in{\cal A}_y}
 p_ap_{a'}\bigl(h_y(a)-h_y(a')\bigr)^2.}
\tag{2.7}
\]

Equivalently, define the coin Gram kernel

\[
 G_y(a,a')=h_y(a)h_y(a').
\tag{2.8}
\]

Then (2.7) is diagonal mass minus Gram mass:

\[
 Q_S^{\rm coin}
 =\sum_y{\chi_y\over P_y}
 \left[
   P_y\sum_{a\in{\cal A}_y}p_aG_y(a,a)
   -\sum_{a,a'\in{\cal A}_y}p_ap_{a'}G_y(a,a')
 \right].
\tag{2.9}
\]

The off-diagonal term is subtracted.  An upper bound on it cannot
upper-bound the Dirichlet energy; a lower mixing bound would be useful.

## 3. Exact conversion to current-edge sampling

Substitute (1.7) and (2.1) into (2.7).  On positive child links,

\[
\begin{aligned}
 &p_ap_{a'}
   \bigl(X_a\vartheta_y(a)
          -X_{a'}\vartheta_y(a')\bigr)^2\\
 &\quad=(uX_S)^2\pi_a\pi_{a'}
 \left(
  \sqrt{X_a\over X_{a'}}\,\vartheta_y(a)
  -\sqrt{X_{a'}\over X_a}\,\vartheta_y(a')
 \right)^2.
\end{aligned}
\tag{3.1}
\]

Therefore

\[
 \boxed{
\begin{aligned}
 Q_S^{\rm coin}
 ={(uX_S)^2\over2r}
 \sum_y{\widehat\chi_y\over P_y}
 \sum_{a,a'\in{\cal A}_y}\pi_a\pi_{a'}
 \left(
  \sqrt{X_a\over X_{a'}}\,\vartheta_y(a)
  -\sqrt{X_{a'}\over X_a}\,\vartheta_y(a')
 \right)^2,
\end{aligned}}
\tag{3.2}
\]

where

\[
                         \widehat\chi_y=r\chi_y\in[0,1].
\tag{3.3}
\]

Formula (3.2) is the exact normalization.  It displays the \(1/r\)
from the coin clock and no other automatic small factor.

If \(X_a\) is constant on the active child shore, the square in (3.2)
reduces to

\[
                         \bigl(\vartheta_y(a)
                                  -\vartheta_y(a')\bigr)^2.
\tag{3.4}
\]

Without child-profile ratio control it is a multiplicatively twisted
theta form.  Thus even a theorem for the untwisted kernel would not
directly bound the actual static-weight energy.

## 4. Law of total variance

Continue with the current-edge experiment from Section 1.  For a
fixed \(y\), put

\[
 Z_y=\mathbf1_{\{y\in F\setminus(S\cup\{A\})\}}.
\tag{4.1}
\]

Conditional on \(A=a\),

\[
                         {\bf E}(Z_y\mid A=a)
                         =\vartheta_y(a).
\tag{4.2}
\]

The law of total variance gives

\[
 \boxed{
 \operatorname {Var}(Z_y)
 ={\bf E}_{A\sim\pi}
    [\vartheta_y(A)(1-\vartheta_y(A))]
  +\operatorname {Var}_{A\sim\pi}\vartheta_y(A).}
\tag{4.3}
\]

Since every row through \(S,y\) supplies \(b-1\) choices of
\(A\ne y\),

\[
 \bar\vartheta_y:=
 {\bf E}_{A\sim\pi}\vartheta_y(A)
 ={b-1\over b}{d_t(S\cup\{y\})\over N}.
\tag{4.4}
\]

Consequently

\[
\begin{aligned}
 {\cal G}_S
 &:=\sum_y\operatorname {Var}_{\pi}\vartheta_y(A)\\
 &={1\over bN}
   \sum_{a\ne y}{B_{a y}^2\over A_a}
  -{(b-1)^2\over b^2N^2}
   \sum_y d_t(S\cup\{y\})^2                              \tag{4.5}\\
 &={1\over2}\sum_{a,a'}\pi_a\pi_{a'}
   \sum_y\bigl(\vartheta_y(a)-\vartheta_y(a')\bigr)^2.
                                                                    \tag{4.6}
\end{aligned}
\]

The first term of (4.5) is a conditional collision probability:

\[
 {1\over bN}\sum_a{1\over A_a}
 \sum_{\substack{F,F'\supseteq S\cup\{a\}}}
 |(F\cap F')\setminus(S\cup\{a\})|.
\tag{4.7}
\]

The second term is its rank-one floor.  The desired extra factor is
exactly the assertion

\[
                         {\cal G}_S\le {L^C\over b}
\tag{4.8}
\]

in the appropriate marked-incidence aggregate, with the twisted
analogue required for (3.2).

Law of total variance does not prove (4.8).  It only identifies
\({\cal G}_S\) as the variation of the conditional inclusion law.
The visible \(b^{-2}\) in the pair average is canceled by the
\(b(b-1)\) ordered child pairs whenever the decrement vectors are
separated.

For example, take a uniform law on \(b\) children, choose distinct
external labels \(\phi(a)\ne a\), and let the nonconstant parts of the
decrement vectors be

\[
                         \vartheta_y(a)=\mathbf1_{\{y=\phi(a)\}}.
\tag{4.9}
\]

Adding a common decrement vector to every child does not change the
variance.  For the displayed nonconstant part one has

\[
                         {\cal G}_S=1-{1\over b},
\tag{4.10}
\]

not \(O(1/b)\).  This is an algebraic calibration of the form, not a
claim that (4.9) itself is an induced repaired-ring residual.

## 5. Comparison with the proved theta and PSF inputs

### 5.1 Harmonic-normalization mismatch for the theta kernel

After expanding the two coin decrements into current rows, the positive
diagonal in the untwisted energy is exactly (4.7):

\[
 {1\over bN}\sum_a{1\over A_a}
 \sum_{\substack{F,F'\supseteq S\cup\{a\}}}
 |(F\cap F')\setminus(S\cup\{a\})|.
\tag{5.1}
\]

The physical theta theorem controls the corresponding
equality-resolved polynomial diagram count before division by the
current link size \(A_a\).  The arbitrary-core extension of that
theorem remains polynomial: every physical row and column occurrence
has a nonnegative integral multiplicity.  Neither theorem contains the
harmonic weight \(1/A_a\).

This distinction is stable under restriction.  Deleting all but a
small, highly aligned part of one child link decreases every polynomial
theta numerator, but it can increase its ratio to \(A_a\).  Therefore
no static theta numerator inequality may simply be divided by the
current child degree.  Current-edge sampling makes the reciprocal
legitimate probabilistically—it is the conditional choice of
\(F,F'\) from the current \((S,a)\)-link—but does not make the
conditional collision small.

The literal internal-gap square is an important normalization audit,
although not a counterexample to the desired aggregate.  For a
distance-two pair \(S=\{X,Z\}\), its four midpoint children satisfy

\[
 {q_3(S\cup\{Y_{ij}\})\over q_2(S)}={1\over4},
\qquad
 p(Y_{ij}\mid S)={1\over4b}.
\tag{5.2}
\]

Thus the false pointwise estimate \(q_3/q_2=O(m^{-2})\) cannot supply
the missing denominator.  The current-child normalization does restore
one \(1/b\) for the complete four-child fibre; proving that this saving
survives all fibres and all harmonic collision ratios is exactly CCM,
not a consequence of the raw child-ratio table.

Finally, the theta theorem is an upper collision estimate.  Formula
(2.9) subtracts the off-diagonal Gram collision.  An upper bound on that
subtracted term cannot by itself upper-bound the Dirichlet energy; one
must control the positive harmonic diagonal (5.1), or prove a lower
mixing comparison with the rank-one floor.

### 5.2 Why whole-arm PSF does not supply the missing comparison

Whole-arm PSF controls, for displayed rows \(F,F'\), the number of
future selected edges meeting both exclusive shores.  It also proves
that formal compensation coin fibres disappear when one computes the
hazard of the complete physical union.

Neither statement bounds (4.7).  That expression counts literal shared
resources \(y\in F\cap F'\) inside two child links, divides by the
current child-link size \(A_a\), and then subtracts the independent
rank-one floor in (4.5).  A shared resource is not a future edge meeting
both exclusive shores.  Moreover, an upper bound on common future
events gives no lower control of the Gram term in (2.9).

An orthogonal family of coin-decrement vectors has no common-event
burden and therefore satisfies every such upper bound most easily,
while its Dirichlet energy is maximal.  Hence PSF does not supply the
harmonic collision-minus-floor estimate (4.5).

### 5.3 The exact missing incidence theorem

For marked pair-parent weights \(w_S\), define the twisted conditional
coin energy

\[
\begin{aligned}
 {\cal G}^{X,\chi}_S
 := {1\over2}\sum_y{\widehat\chi_y\over P_y}
 \sum_{a,a'\in{\cal A}_y}\pi_a\pi_{a'}
 \left(
  \sqrt{X_a\over X_{a'}}\,\vartheta_y(a)
  -\sqrt{X_{a'}\over X_a}\,\vartheta_y(a')
 \right)^2.
\end{aligned}
\tag{5.6}
\]

Then (3.2) is simply

\[
                         Q_S^{\rm coin}
 ={(uX_S)^2\over r}{\cal G}^{X,\chi}_S.
\tag{5.7}
\]

The required theorem is

\[
 \boxed{
 \sum_S w_S(uX_S)^2{\cal G}^{X,\chi}_S
 \le {L^C\over b}
       \sum_S w_S(uX_S)^2
       +o(W)
 \qquad(b=r-2).}
\tag{CCM}
\]

Here the sum is over actual marked pair-parent occurrences, so no
ambient-pair union bound is permitted.  Combining CCM with (5.7) gives

\[
 \sum_Sw_SQ_S^{\rm coin}
 \le {L^C\over r(r-2)}
       \sum_Sw_S(uX_S)^2+o(W/r),
\tag{5.8}
\]

which is exactly the missing compensation part of CHD.

CCM is a conditional mixing or normalized collision-minus-floor
theorem.  It is not a raw codegree bound.  It must either:

1. control the independent current-child product law, including all
   internal-gap fibres;
2. retain the reciprocal current-link normalization \(1/A_a\) in
   (4.5); and
3. control the child-profile twist \(X_a/X_{a'}\), or replace the
   static-weight energy by a dynamic energy and pay the resulting
   weight-motion generator.

None of these three statements is contained in the current physical
theta or whole-arm PSF theorem.

## 6. Surviving conclusion

The proposed route performs a useful exact reduction but does not close
the compensation Dirichlet term.

What is proved here is:

1. the exact centered pairwise coin Gram form (2.7);
2. the exact current-edge normalization (3.2);
3. the law-of-total-variance/collision-floor identity
   (4.3)--(4.7); and
4. the precise harmonic-normalization mismatch which prevents the
   existing theta and PSF bounds from yielding \(1/[r(r-2)]\).

The surviving positive gate is CCM.  A proof of CCM would close the
coin part of the centered Hilbert diagonal.  Without CCM, the only
unconditional factor supplied by the compensation clock is \(1/r\).
