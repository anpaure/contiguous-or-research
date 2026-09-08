# Final cross-audit: corrected six-slot `h=4` outer-gate theorem

**Date:** 2026-08-04  
**Method:** independent symbolic replay of the two corrected endpoint rows
and every downstream use of their strictness; no search, numerical
experiment, or computational construction.

**Corrected theorem:**
`MATH_THEOREM_SIX_SLOT_H4_OUTER_GATE_LOCAL_SIGN_AND_RESIDUAL_KKT_20260804.md`,
SHA256
`badc46480b85ef794e784ca2f62273aa6258cdf3dcfecbd915553102c6acd6af`.

**Corrected freeze manifest:**
`MATH_FREEZE_SIX_SLOT_H4_OUTER_GATE_LOCAL_SIGN_AND_RESIDUAL_KKT_20260804.sha256`,
SHA256
`837f42e3710c84272032b2627487fc9604e43f4597787b003ace220adf28f020`.

**Predecessor fail-closed audit:** SHA256
`5efa432687fbd7be14107ccdb1fded01ca6ec0db62db29ff681405d4f0742248`.

## 0. Verdict

**FINAL GO for the corrected successor bytes.**  The two false strict
endpoint statements identified by the predecessor audit are repaired in
their exact weak forms.  Every downstream strict gate inequality still has
an independent strict source.  The local sign interval, far-end obstruction,
continuity crossing, and residual KKT list retain their previous constants
and conclusions.

The predecessor SHA remains fail-closed and must not be cited as GO.

## 1. Corrected kernel sign at zero

With `w=At`, the exact factorization is

\[
 {-K'(At)\over2A}
 =\left(e^{-A^2(1-t)^2}+e^{-A^2(1+t)^2}\right)
  \left(\tanh{\pi t\over2}-t\right).
\tag{1.1}
\]

At `t=0`, the second factor is zero, so

\[
                         K'(0)=0.
\]

Thus the predecessor's strict left inequality at the included endpoint was
false, and the successor correctly states

\[
                         0\le-K'(w)<{3\over10}
 \qquad(0\le w\le A/2),
\tag{1.2}
\]

with strict positivity only for `w>0`.

For completeness, on `0<=t<=1/2`,

\[
 \operatorname{arctanh}(t)
 =\int_0^t{du\over1-u^2}
 \le{4t\over3}< {\pi t\over2}
 \qquad(t>0).
\]

Hence `tanh(pi t/2)>t` for `t>0`, proving the strict positive part.  On
`0<=t<=1/4`,

\[
 \tanh{\pi t\over2}-t
 <\left({\pi\over2}-1\right)t
 <{1\over7}<{1\over6},
\]

and the first factor in (1.1) is below one.  Since `A<8/9`, this gives

\[
                         -K'(At)<{2A\over6}<{8\over27}<{3\over10}.
\]

The authenticated quarter-to-half estimate supplies the remaining half
band.  The corrected sign row is therefore exact on its whole stated
interval.

## 2. Corrected diagonal displacement

For `q>=1` and `0<=w<=A/2`, the argument `qA+w` lies on the increasing
tail branch, so `K'(qA+w)>0`.  Therefore, wherever `F'(w)<0`,

\[
                         -F'(w)<-K'(w)<{3\over10}.
\]

Integrating only the negative part of `F'` gives

\[
                         F(s)-F(t)\le {3(t-s)\over10}
 \qquad(0\le s\le t\le A/2).
\tag{2.1}
\]

At `s=t`, equality is exactly `0=0`; this is why the weak sign is necessary.
If `s<t`, the displacement comparison is strict: either the train does not
drop, or the pointwise negative-slope bound is strict on the dropping set.

Independently,

\[
 F(s)-F(t)<{61\over1000}
\tag{2.2}
\]

because `F(s)<61/1000` and `F(t)>0`.  Thus the successor's separated pair
of inequalities (2.1)--(2.2) is exact.  Writing their minimum as one bound
is valid only weakly at a zero displacement.

## 3. Downstream strictness audit

### Active envelope

The moving loss is now at most `D(delta)`, not strictly below it.  However
the Jacobi reflection comparison immediately preceding it is strict:

\[
 F_\tau(b+\delta)+F_\tau(A-b)
 >F(b+\delta)-F(b)-\varepsilon.
\]

Therefore

\[
                         \mathcal H(\delta)
 >C(A+\delta)-D(\delta)-\varepsilon
\]

remains strict even at `delta=0`.

### Inactive envelope

The cap loss is strictly below `eta`, while the moving loss is at most
`D(delta)`.  Hence their maximum is at most
`max{eta,D(delta)}`; when equality can occur through the moving loss, the
preceding reflection comparison is again strict.  Consequently

\[
 \mathcal I(\delta)>-\varepsilon-max\{\eta,D(\delta)\}
\]

is unchanged.

### Singleton and half-period envelopes

Away from the half-band endpoint their displacement is nonzero, so the
displacement estimate is strict.  At the endpoint, strict train positivity
and strict reflection supply the needed sign.  The bounds for
`mathcal S` and `C((A+delta)/2)` therefore remain strict.

Adding the three envelopes gives exactly the same strict common gate
minorant as before.  In particular, strictness at the terminal point

\[
                         \delta_*={43849\over643260}
\]

does not rely on either corrected weak endpoint comparison.

## 4. Residual zero-shift row

The corrected equality `K'(0)=0` does not weaken the residual subtraction
claim.  At `w=0`,

\[
\begin{aligned}
 R_\tau(0)-T_\tau(0)
 &=-K'(0)+\sum_{q\ge1}(q-1)K'(q\tau)\\
 &=\sum_{q\ge2}(q-1)K'(q\tau)>0,
\end{aligned}
\]

because every tail derivative is strictly positive.  Thus the later
strict residual and KKT statements remain valid at the formerly delicate
endpoint.

## 5. Unchanged conclusions

The predecessor fail-closed audit already independently verified all rows
unrelated to the two endpoint strictness defects:

1. the ceiling-train concavity chord and its coefficient;
2. the switching point, two linear minorants, and exact positive interval;
3. both rational far-end Gaussian ledgers;
4. continuity of the relaxed gates;
5. the termwise residual identities; and
6. the complete smooth and nonsmooth KKT/subgradient candidate list.

The corrected theorem changes the two endpoint statements exactly as
replayed above and propagates “at most” through the two affected envelope
lines.  Each advertised strict conclusion survives for the independent
reasons in Sections 3--4.  Therefore the corrected successor proves:

\[
 \mathfrak G_{XY}(\delta)>0,
 \quad
 \mathfrak G_Z(\delta)>0
 \qquad(0\le\delta\le\delta_*),
\]

and

\[
 \mathfrak G_{XY}(A/2)<-{21\over2000},
 \qquad
 \mathfrak G_Z(A/2)<-{9\over2500},
\]

with the same residual KKT locus.

This remains a theorem about the two relaxed scalar gates.  It does not
prove complete physical six-slot `h=4` positivity or exhibit a nonpositive
physical table.

