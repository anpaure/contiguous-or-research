# Audit: what the PBBS all-depth theorem does to the entropy ledger

Date: 2026-07-26

## Verdict

The PBBS statement needed for the proposed calibration is genuinely an
**all-depth theorem**, not a fixed-depth extrapolation.  One and the same
canonically oriented centered Johnson (2)-factor has zero missing
correct-rank intersection targets at every depth

\[
                         1\le q\le m.
\]

Thus it includes every growing window (q\le H(m)\le m).  This rigorously
refutes the use of the independent-occupancy ``demand''

\[
                       \Theta(\sqrt m\,W)
\]

as a model-independent information bill for simultaneous shadows.  It
does **not** prove the corresponding cyclic-wreath theorem: the PBBS
Johnson components are not self-owned wreaths, and not every PBBS
(q)-window has the correct intersection rank.  Consequently the precise
conclusion is that the supply-versus-iid-occupancy ledger supplies no
entropy obstruction to the wreath theorem; a wreath-specific structural
obstruction is not excluded.

## 1. The exact PBBS object and its number of windows

Let (f) be the canonical PBBS permutation of the (m)-sets and put

\[
                              g=f^2.
\]

The undirected edges (Xg(X)) form the centered spanning Johnson
(2)-factor.  Give each component the orientation inherited from (g).
For a start (X), define its depth-(q) window and intersection by

\[
 (X,gX,\ldots,g^qX),\qquad
 \iota_q(X)=\bigcap_{t=0}^{q}g^tX.
\]

There are exactly (W=\binom{2m+1}{m}) oriented starts, hence exactly
(W) depth-(q) windows for every (q\).  There is no wrap/repetition
qualification hidden here.  A PBBS orbit has length (L=\ell(2m+1)),
and its step-two component has length

\[
                  {L\over\gcd(2,L)}\ge 2m+1>q.
\]

## 2. The theorem is uniform up to (q=m)

The audited global-maximum corridor theorem says that, for every

\[
 1\le q\le m,
 \qquad S\in\binom{[2m+1]}{m-q},
\]

there is a start (X) for which

\[
                            \iota_q(X)=S.
\]

Writing

\[
 \mu^{\rm corr}_{P,q}(S)
   =\#\{X:\iota_q(X)=S,\ |\iota_q(X)|=m-q\},
\]

the exact result is

\[
 \boxed{
  1\le \mu^{\rm corr}_{P,q}(S)
       \le \binom{2q+1}{q}
 }
 \qquad(1\le q\le m).
\]

In particular

\[
 \boxed{M^{\rm corr}_{P,q}=0\quad\hbox{for every }1\le q\le m}
\]

simultaneously for the same (2)-factor.  The upper bound becomes
exponential in (q), but that affects collision control, not support.

## 3. Comparison with wreath shadows

An exact wreath factor also has (W) starts at every depth: each of its
(C_m=W/(2m+1)) cyclic orders contributes (2m+1) starts.  Moreover,
for a wreath row,

\[
 \bigcap_{t=0}^{q} I_\pi(j+t,m)
\]

is automatically a rank-((m-q)) cyclic interval.  Thus both models use
one common trajectory structure and (W) starts to hit

\[
                         N_q=\binom{2m+1}{m-q}
\]

targets.

The word ``identical'' should nevertheless be qualified.  In the wreath
model all (W) windows have the correct rank.  In PBBS, some windows may
have intersection rank larger than (m-q); if (b_q) denotes their
number, then the all-depth theorem only implies

\[
                           b_q\le W-N_q.
\]

Therefore PBBS has between (N_q) and (W) valid balls, rather than
exactly (W).  This makes its support achievement no easier in the raw
occupancy budget, but it means the two occupancy experiments are not
literally the same probability space.

There is a second qualification: PBBS proves the lower/intersection
shadows.  Unlike a family of cyclic orders, its complement does not
automatically identify the corresponding upper/union shadow at every
depth.  This does not rescue the ledger, since the one-sided lower band
alone still has an iid demand of order \(\sqrt m\,W\).

## 4. The candidate-count comparison

The Johnson graph has

\[
 d=m(m+1),\qquad |E(J)|={Wd\over2}.
\]

A spanning (2)-factor has (W) edges, so the honest overcount

\[
 \#\{\hbox{Johnson (2)-factors}\}
 \le \binom{Wd/2}{W}
\]

gives

\[
 \log\#\{\hbox{Johnson (2)-factors}\}
 \le W\bigl(2\log m+O(1)\bigr).
\]

The catalogue count for (C_m) cyclic orders is

\[
 W\bigl(\log m-1+o(1)\bigr).
\]

Hence the sibling Johnson model has at most twice this leading
logarithmic catalogue entropy, yet PBBS meets all one-sided depths through
(m).  An iid-occupancy union-bound heuristic charging
(\Theta(\sqrt m\,W)) nats would rule out this known object.  Its
independent-depth premise is therefore quantitatively false.

## 5. Exact scope of the refutation

What is refuted:

* the inference that (e^{O(W\log m)}) candidate objects cannot contain
  an all-depth support object because iid bins charge
  (e^{-\Theta(\sqrt m W)});
* a universal (O(\log m)) depth threshold derived only from that ledger;
* the claim that each depth necessarily consumes an essentially fresh
  (\Theta(W)) information bill.

What is not refuted:

* a theorem using a statewise invariant special to self-owned wreath
  packaging;
* a counting theorem proved specifically for cyclic-order factors rather
  than imported from iid occupancy;
* the residence/seam obstruction separating the PBBS (2)-factor from a
  literal wreath word;
* overload or balanced-multiplicity requirements.  The PBBS result is a
  support theorem and its cap \(\binom{2q+1}{q}\) is too large for a
  growing-window collision estimate.

The safe conclusion is therefore:

\[
 \boxed{
 \text{the entropy ledger is not an obstruction; cyclic packaging remains
 a combinatorial gate.}
 }
\]

