# Self-audit: global `1053/20000` price and period-26 closure

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_APERY_GLOBAL_1053_OVER_20000_AND_PERIOD26_COMPLETE_POSITIVITY_20260804.md`  
**Target SHA256:**
`c18c2744a87be8b41c42e956b9a750338c0abe5f6fb72b2cf669923644af39c5`  
**Verdict:** **SELF-AUDIT GO.**  This is not an independent audit.

## 1. Concavity

For

\[
Q(t)=\left({\pi^2t^2\over4}-{\pi\over2}\right)e^{-\pi t^2/4},
\]

the substitution `y=pi t^2/4` shows that `Q` increases up to `y=3/2`
and decreases afterward.  On `0<=x<=2/13`, the central term is therefore
largest at `2/13`, while every positive tail term is largest at its
smallest argument.  The rational endpoint certificates give

\[
Q(x)<-7/5,
\qquad Q(2-x)<1/2,
\qquad \sum_{j\ge3}Q(j-x)<1/20.
\]

Thus `J''<-17/20<-1/2` on the full interval.  No unproved location of a
critical point is used.

## 2. Tangent ledger

At `x=1/8`, the upper Gaussian ledger is

\[
{98781\over100000}
+{6324\over100000}
+{152\over100000}
+{1\over100000}
+{1\over1000000}
={1052581\over1000000}.
\]

The exact lower exponents obtained from `pi>333/106` are

\[
333/27136,
\quad74925/27136,
\quad176157/27136,
\quad320013/27136.
\]

The displayed finite Taylor degrees prove the four reciprocal comparisons;
the remaining tail starts beyond `506493/27136`.

For the derivative bracket, the lower positive ledger is

\[
{15\over8}{6321\over100000}
+{23\over8}{151\over100000}
+{31\over8}{7\over1000000},
\]

whereas the upper positive ledger, including its tail, is

\[
{15\over8}{6324\over100000}
+{23\over8}{152\over100000}
+{31\over8}{10\over1000000}
+{1\over1000000}.
\]

Against the corresponding lower and upper bounds on
`(1/8)e^{-pi/256}`, these give

\[
-1/1000<J'(1/8)<0.
\]

## 3. Global maximum

Since `J''<-1/2`, Taylor's theorem gives

\[
J(x)\le J(1/8)+J'(1/8)(x-1/8)-{1\over4}(x-1/8)^2.
\]

The final two terms have maximum `J'(1/8)^2<10^{-6}`.  Hence

\[
J(x)<{1052582\over1000000}.
\]

Jacobi completion adds at most `epsilon=50/10^6`, so

\[
f(x)<{52632\over1000000}
<{52650\over1000000}={1053\over20000}
\]

through `2/13`.  The authenticated decrease and `2/13` anchor close the
rest of `[0,1/2]`.

## 4. Residual repricing

The old and new global prices differ by

\[
{533\over10000}-{1053\over20000}
={13\over20000}={650\over1000000}.
\]

Exactly three far endpoints use that price, so both residual baselines gain
`1950/1000000`.  Consequently

\[
-1882+1950=68,
\qquad
-1648+1950=302.
\]

Replacing each old price slack by the new one preserves nonnegativity,
because the new estimate is global.  Therefore both residual chambers are
strictly positive, and the previously authenticated chamber exhaustion
proves complete formal period-26 positivity.

## 5. Scope

The conclusion is restricted to honest exact-first-carry formal period-26
clocks.  It makes no overshoot, shoulder, arbitrary-period, or OR-word
claim.  Both dependency hashes match the cited files.
