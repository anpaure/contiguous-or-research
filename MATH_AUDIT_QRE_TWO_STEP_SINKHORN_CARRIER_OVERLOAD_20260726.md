# Audit of the QRE two-step Sinkhorn carrier overload

Date: 2026-07-26

Audited source:
`MATH_THEOREM_QRE_TWO_STEP_SINKHORN_CARRIER_OVERLOAD_20260726.md`.

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Verdict

The exact one-hit size-bias algebra, the forward carrier shift

\[
                         Z^\pm=L^\pm+A+o_B(1),
\]

the change-of-measure identities, and the fixed-frame obstruction all
pass.

The independent-rank lognormal row-load law is **conditional**, exactly as
the source's final boundary says.  Its displayed weighted Gaussian saddle
(WGS) is not proved by Section 3: that section identifies the saddle and
the only possible linear carrier term, but it does not provide the uniform
coefficient extraction needed to replace the exact sum by
\(\exp(A^2/2+AZ+o(1))\).  Likewise, the weaker reverse carrier transition
(RCT) is a valid sufficient lemma but is not completed there.

Thus the source proves an unconditional linear overload only for the legal
constant-in-rank fixed frame.  For independent rank matchings it gives a
sharp, credible reduction to RCT, not yet an unconditional no-go.

## 1. One-hit reverse and forward means

For source half-counts \((\alpha,\gamma)\), let

\[
 F\sim\operatorname{Hyp}(d,\gamma,\alpha),
 \qquad
 \operatorname{Var}F=
 {\alpha\gamma(d-\alpha)(d-\gamma)\over d^2(d-1)}.
\]

The number of split edges occupied on the \(A\)-side is \(\alpha-F\).
Size-biasing by this count gives

\[
 {\mathbb E[(F-\mathbb EF)(\alpha-F)]
        \over\mathbb E(\alpha-F)}
 =-{\operatorname{Var}F\over\alpha-\mathbb EF}
 =-{\gamma(d-\alpha)\over d(d-1)}.
\]

After including the exact change of the centered empty-edge mean, the
forward edit mean is

\[
 r_A={\gamma(\alpha-1)\over d(d-1)},
 \qquad
 r_C={\alpha(\gamma-1)\over d(d-1)}.
\]

Weighting by the two split shores gives \(1/4+o(1)\) uniformly on the
central core.  These formulas and their signs are correct.

In the reverse experiment, fix target half-counts \((a,c)\) and choose an
empty edge with its exact size bias \(z=d-a-c+F\).  Then

\[
 {\mathbb E[(F-ac/d)z]\over\mathbb Ez}
 ={\operatorname{Var}F\over(d-a)(d-c)/d}
 ={ac\over d(d-1)}={1\over4}+o(1).
\]

Thus the reverse local constant is also exactly \(1/4+o(1)\).

## 2. Forward carrier transition

Under a source column of the source-normalized kernel, one chooses a
uniform \(q\)-subset of the intrinsic split axes.  With
\(q=A\sqrt m+O(1)\), \(b=m/d+O(1)\), standard occupancy estimates give

\[
 \#\{j:\ell_j=1\}=q-O_{\mathbb P}(d),
 \qquad
 \#\{j:\ell_j\ge2\}=O_{\mathbb P}(d).
\]

The one-hit mean contributes

\[
 {4\over\sqrt m}(q/4+o(\sqrt m))=A+o(1).
\]

The conditional one-hit variance is
\(O(qd)\), which becomes \(O(d/\sqrt m)=o(1)\) after multiplication by
\(16/m\).  Multi-hit blocks contribute at most
\(O_{\mathbb P}(d^2/\sqrt m)=o(1)\) under \(d^2=o(\sqrt m)\).  Untouched
blocks agree literally in the target and source carriers.  Hence the
forward transition is correct on both signs.

## 3. Exact change of measure

Let

\[
 P(T,X)={B_{TX}\over G},
 \qquad
 \rho_G={N_q\over G},
 \qquad
 \widehat Q(T,X)={P(T,X)\over\rho_G\Lambda(T)}.
\]

Then \(\widehat Q\) is a probability measure, its target marginal is
uniform, and

\[
                         \widehat Q_X(X)={C(X)\over N_q}.
\]

Therefore, for every source family \(\mathcal S\),

\[
 {1\over|\mathcal S|}\sum_{X\in\mathcal S}C(X)
 =\rho_G{\widehat Q_X(\mathcal S)\over P_X(\mathcal S)}.
\]

All normalizing constants pass.  If RCT holds, uniform targets give
\(Z\Rightarrow N(0,1)\), hence \(L\Rightarrow N(-A,1)\) under
\(\widehat Q\), while \(L\Rightarrow N(0,1)\) under \(P\).  The density
ratio on a short interval about \(\ell\) is then

\[
 e^{-A^2}{\phi(\ell+A)\over\phi(\ell)}
 =e^{-3A^2/2-A\ell}.
\]

It exceeds one on every bounded interval strictly below \(-3A/2\), giving
\(\sum_X(C(X)-1)_+=\Omega_A(W)\).  Thus RCT is indeed sufficient for the
claimed independent-frame aggregate no-go.

## 4. What remains in RCT

Conditionally on a fixed target, the exact posterior source weight is

\[
 {2^q\prod_j\binom{z_{j,a_j}}{a_j}
       \over\binom{S(\mathbf a)}q},
 \qquad \sum_ja_j=q.
\]

The factor \(\Lambda(T)^{-1}\) cancels from the conditional law.  The beta
identity

\[
 {1\over\binom Sq}=(S+1)\int_0^1x^q(1-x)^{S-q}\,dx
\]

is therefore the correct route to a product saddle.  The proposed local
tilt estimate is also of the right size: the derivative of
\(-\log\binom Sq\) is \(O(q/m)\), so tilting a local statistic of variance
\(O(d)\) changes its mean by \(O(d/\sqrt m)\).  Over \(q\) hits this gives
only \(O(d/\sqrt m)=o(1)\) after carrier normalization.

Two estimates still have to be proved uniformly under this posterior:

1. \(q-O_{\mathbb P}(d)\) one-hit blocks, \(O_{\mathbb P}(d)\) multi-hit
   blocks, and negligible hits of order at least three; and
2. conditional variance \(O(qd)\) for the sum of reverse edit scores,
   despite the global \(1/\binom{S(\mathbf a)}q\) coupling.

For a quenched conclusion, the resulting annealed estimates must also be
made uniform for all but \(o(W)\) targets in a typical independent rank
array.  The beta representation makes these statements plausible, but the
source note does not prove its local central bounds, saddle localization,
or quenched passage.

This is the exact smallest missing lemma for the independent-rank
two-step no-go.

## 5. Fixed-frame audit

For the constant-in-rank pair frame, an owner with \(f\) full and
\(s=m-2f\) split pairs satisfies

\[
 \Lambda_f={2^q\binom{f+q}q\over\binom sq},
 \qquad C(X)=\Lambda_f^{-1}.
\]

At \(q=A\sqrt m\), \(f=m/4+x\sqrt m\),

\[
                         \log\Lambda_f=3A^2+8Ax+o(1).
\]

Since \((f-m/4)/\sqrt m\Rightarrow N(0,1/16)\), the overload fraction
tends to \(\Phi(-3A/2)>0\).  This part is unconditional and exact.

## 6. Final boundary

Verified unconditionally:

1. all one-hit size-biased identities;
2. the forward carrier transition;
3. the exact change-of-measure reduction;
4. RCT \(\Rightarrow\Omega_A(W)\) aggregate overload; and
5. the fixed-frame overload theorem.

Not yet proved:

1. WGS;
2. RCT under the globally coupled posterior; or
3. an independent-rank aggregate overload theorem.

Accordingly, no independent-rank obstruction should be quoted without
the WGS/RCT qualifier.  The raw QRE and weighted allocation-score routes
remain open regardless: even a proved two-step overload would refute only
this particular source-normalized scaling, not every fractional flow.
