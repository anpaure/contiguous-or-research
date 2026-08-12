# Independent fail-closed audit of the monotone anchor-grid ray ledger

**Date:** 2026-08-04  
**Audited source:**
`MATH_LEMMA_APERY_MONOTONE_ANCHOR_GRID_RAY_LEDGER_20260804.md`  
**Audited SHA256:**
`8b696e0a2ec971924fb24b6b3cb7498ce4c8ba1164e3f7f21eef21ea9a256d07`

## Verdict

**FAIL CLOSED as written.**  The endpoint eligibility, adverse-theta
accounting below the quarter, and the priced-majorant formulation in
Section 4 are sound.  However, the second line of (1.1) assigns the raw
positive price `L-V_j` to every pair anchored at `t_j>=1/4`.  Past the
quarter the hypotheses guarantee only that the pair is strictly positive.
They do not guarantee an arbitrary positive margin `L-V_j` when both
endpoints lie past the quarter.

The exact repair is local:

\[
 f(X)-f(Y)+g(Y)>
 \begin{cases}
 \min\{0,L-V_j-\varepsilon\},&t_j<1/4,\\
 \min\{0,L-V_j\},&t_j\ge 1/4,
 \end{cases}
\tag{A.1}
\]

and every `p_i` in Theorem 2.1 must be the corresponding clipped price.
The global price may likewise be written
`min(0,L-V_*-epsilon)`; in the present application it is already negative.
With this repair, the all-period majorant (4.1)--(4.2), which already uses
`min{0,L-B(i/h)}`, is the correct proof-safe corollary.

## 1. Dependency and scope check

The audited bytes contain the newly required quarter-band monotonicity

\[
f'(x)<0\qquad(1/4\le x\le1/2).
\]

The lemma is explicitly scoped to honest exact-first-carry formal cyclic
Apéry clocks.  Its final scope paragraph does not claim overshoot, later
first crossing, finite shoulders, integral carrier rounding, common-cap
compilation, or an OR-word upper bound.  That scope is correct.

## 2. Strict anchor eligibility is correct

For reflected pair `i`, terminal-suffix maximality gives

\[
Y_i>{i\over h}.
\]

Thus every anchor satisfying `t_j<=i/h` also satisfies `Y_i>t_j`, including
the equality case `t_j=i/h`.  The strict endpoint convention in (2.1) is
therefore valid.

## 3. The below-quarter price is valid

Let `t_j<1/4` and `Y>t_j`.

* If `X<t_j`, then `f(X)>L`, monotonicity from `t_j` gives
  `f(Y)<f(t_j)<V_j`, and `g(Y)>-epsilon`.
* If `X>=t_j`, monotonicity gives `f(X)-f(Y)>=0`, while
  `g(Y)>-epsilon`.  Moreover `f(t_j)>L` and `f(t_j)<V_j`, so
  `L-V_j-epsilon<-epsilon`.

Hence the first line of (1.1) is valid for the stated anchors.  The same
argument validates the global price: the global upper bound includes
`f(0)>L`, so `V_*>L`.

## 4. Exact counterexample to the above-quarter raw price

Take the certified anchor

\[
t_j={2\over7},\qquad V_j={4083\over100000}.
\]

Its raw price in the second line of (1.1) is

\[
L-V_j
={5503\over125000}-{4083\over100000}
={1597\over500000}>0.
\tag{A.2}
\]

Now choose any `X=Y` with `2/7<Y<1/2`, for example `X=Y=1/3`.
This satisfies every pairwise hypothesis in Lemma 1.1.  The pair value is

\[
f(X)-f(Y)+g(Y)=g(Y).
\]

The certified theta rows give

\[
0<g(Y)<\varepsilon={1\over20000}={25\over500000}
<{1597\over500000}=L-V_j.
\]

Therefore the claimed strict lower bound by `L-V_j` is false.  The proof's
sentence "nonnegative compact difference and `g(Y)>0`" establishes only a
strict lower bound by zero.  This is exactly why the authenticated
period-twenty-one theorem uses an ordered-ray dichotomy and explicitly
does **not** charge `L-V_j` when the left endpoint has passed the quarter.

## 5. Correct two-case statement

For `t_j>=1/4` and `Y>t_j`:

* if `X<1/4`, then `f(X)>L`, `f(Y)<V_j`, and `g(Y)>0`, so the pair is
  greater than `L-V_j`;
* if `X>=1/4`, quarter-band decrease gives
  `f(X)-f(Y)>=0`, and `g(Y)>0`, so the pair is greater than zero.

The uniform lower bound is consequently

\[
\min\{0,L-V_j\},
\]

not `L-V_j`.  This establishes (A.1).

## 6. Finite-grid ledger after correction

With clipped prices, the proof of Theorem 2.1 is exact:

* `C>L` and `g(alpha)>-epsilon` give the base `L-epsilon`;
* strict anchor eligibility permits one clipped price for each reflected
  pair;
* the retained middle train is nonnegative (and in the authenticated
  Apéry setting strictly positive).

Thus

\[
E(s)>L-\varepsilon+\sum_i p_i+
\sum_r f(s_r/A)
\]

holds with `p_i` defined by (A.1).  A positive ray-only ledger remains a
sufficient condition; positive middle-train and overlap/theta credits may
still be added.

The period-twenty-one `2/7` improvement is not a blind grid price.  It is
available only in the branch `X_6<1/4`; in the complementary branch,
orderedness makes the entire far ray positive.  Section 3 correctly
mentions this distinction, but it does not repair the universally
quantified Lemma 1.1 or Theorem 2.1.

## 7. The priced majorant survives

Section 4 defines

\[
B(t)=\min\left(V_*+\varepsilon,
\inf_{j:t_j\le t}
\{V_j+\varepsilon\mathbf 1_{t_j<1/4}\}\right)
\]

and uses

\[
\min\{0,L-B(i/h)\}.
\]

For the finite anchor grid the infimum is a minimum.  Selecting an anchor
which realizes it and applying (A.1) gives exactly this clipped price.
Hence (4.2), or its augmentation by retained middle and overlap credits,
is indeed a sufficient one-dimensional all-period criterion.

It is only a sufficient criterion.  The lemma neither proves the required
uniform discrete/Riemann-sum inequality nor upgrades formal clocks to
physical words.  The source's scope statement correctly preserves both
limitations.

## Final disposition

The source SHA above must not be promoted as a theorem in its present
form.  Replace the two raw prices in Lemma 1.1 and Theorem 2.1 by their
clipped versions.  No change is needed to the priced-majorant formula
(4.1)--(4.2).  After that textual and algebraic correction, this audit
finds no further obstruction in the anchor-grid reduction.
