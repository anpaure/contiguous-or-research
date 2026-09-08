# Independent audit: macroscopic-collar parity decorrelation

**Date:** 2026-08-03  
**Audited source:** `MATH_THEOREM_MACROSCOPIC_COLLAR_PARITY_DECORRELATION_20260803.md`  
**Audited source SHA-256:** `8e9e283811eb80016ee32eccf990f6ee12306172f1b209743c1db5a00e5ceecd`  
**Method:** independent symbolic proof replay; no finite search or numerical experiment.  
**Verdict:** **GO as stated.**  The truncation preserves the claimed uniform
target degrees and the normalized pair-codegree bounds, the far-tail estimate
is valid, and the adjacent-rank collar matching really is an exact
owner-indexed chain partition.  The source correctly leaves the joint
collar/residual construction and every later literal-chronology gate open.

## 1. Binomial and Gaussian estimates

Write (j=r-s).  The exact ratio is

\[
p_{r-j}=\frac{\binom{2r}{r-j}}{\binom{2r}{r}}
        =\prod_{i=0}^{j-1}\frac{r-i}{r+i+1}.
\]

For every factor,

\[
\log\frac{r-i}{r+i+1}
=\log\!\left(1-\frac{2i+1}{r+i+1}\right)
\le -\frac{2i+1}{r+i+1}.
\]

Since (r+i+1\le r+j) and
(sum_{i=0}^{j-1}(2i+1)=j^2), this gives

\[
p_{r-j}\le e^{-j^2/(r+j)}\le e^{-j^2/(2r)}.
\]

For (j=O(\sqrt{r\log r})), expansion of the same exact product gives

\[
\log p_{r-j}
=-\frac{j^2}{r}
 +O\!\left(\frac{j^2}{r^2}+\frac{j^4}{r^3}\right)
=-\frac{j^2}{r}+o(1).
\]

Therefore, at the inner boundary (j=a+1),
(p_{r-j}=e^{-c^2+o(1)}<1/2).  This makes every probability
(2p_s) in the parity law legal.  At the outer boundary
(b=\lceil\sqrt{6r\log r}\rceil), the same expansion gives
(p_{r-j}\ge r^{-7}) uniformly for (j\le b), for all sufficiently
large (r).  The coarser upper bound gives
(p_{r-j}\le r^{-3}) for (j>b).

The Riemann-sum estimate

\[
2\sum_{j\ge a}p_{r-j}
=\left(2\int_c^\infty e^{-x^2}\,dx+o(1)\right)\sqrt r
\]

is valid by the local expansion on bounded rescaled intervals and the
preceding Gaussian domination on the remaining tail.  Mills' inequality
gives

\[
2\int_c^\infty e^{-x^2}\,dx
\le \frac{e^{-c^2}}c
<\frac1{2c}<\frac{\sqrt\pi}{2}
\]

when (c>\sqrt{\log 2}).  Together with
(d=(\sqrt\pi/2+o(1))\sqrt r), the conditional mean of the selected-rank
count is at most (	heta d) for a fixed (	heta<1).

## 2. Parity marginals and capacity truncation

Conditional on a parity, the selected-rank indicators are independent with
probabilities (2p_s) on that parity.  Averaging the fair parity bit gives

\[
\Pr(s\in R_0)=\tfrac12(2p_s)=p_s.
\]

For a Poisson-binomial variable (X=|R_0|) with
(mathbb E X\le\theta d), the standard exponential Chernoff estimate is

\[
\Pr(X>d)
\le \exp\{-d(\log(1/\theta)-1+\theta)\}
\le e^{-\kappa\sqrt r}
\]

for some (kappa(c)>0).  Emptying the whole rank set on this event therefore
produces

\[
0\le p_s-q_s
=\Pr(s\in R_0,\,|R_0|>d)
\le e^{-\kappa\sqrt r}.
\]

Because (p_s\ge r^{-7}) throughout the retained band, this is
(o(p_s)) uniformly.  The exact uniform-order target-degree identity

\[
d_x(S)=\frac{q_s}{p_s},\qquad |S|=s,
\]

then yields (d_x(S)=1-o(1)) uniformly.  Also,

\[
\sum_{s\in\mathcal I}(p_s-q_s)
=\mathbb E\bigl[|R_0|\mathbf1_{\{|R_0|>d\}}\bigr]
\le b e^{-\kappa\sqrt r}=o(1).
\]

Multiplication by (W) converts this normalized loss into (o(W)) missing
named-target mass.  Truncation cannot enlarge an atom: every surviving atom
contains at most (d) target vertices and one owner, so (K\le d+1).

## 3. Complete pair-codegree replay

Let (S\subset U), with (|S|=s<t=|U|), and let
(eta_{s,t}=\Pr(s,t\in R)).  The exact named-target codegree is

\[
d_x(S,U)
=\eta_{s,t}
 \frac{\binom{2r-t}{r-t}}
      {\binom rt\binom ts}.
\]

Using (d_x(U)=q_t/p_t) and (d_x(S)=q_s/p_s), the two exact normalized
forms are

\[
\frac{d_x(S,U)}{d_x(U)}
=\frac{\eta_{s,t}}{q_t\binom ts},
\qquad
\frac{d_x(S,U)}{d_x(S)}
=\frac{\eta_{s,t}}{q_s\binom{2r-s}{t-s}}.
\]

Before truncation, equal-parity ranks have
(eta^0_{s,t}=2p_sp_t), while opposite parities have zero joint mass;
truncation only decreases (eta).  Since (q_s=(1-o(1))p_s), the two
ratios are bounded by

\[
\frac{(2+o(1))p_s}{\binom ts},
\qquad
\frac{(2+o(1))p_t}{\binom{2r-s}{t-s}}.
\]

Nonzero codegree forces the positive rank gap (g=t-s) to be even, hence
(g\ge2).  On the retained band, (t\ge r-b\ge r/2) and
(g\le b-a<r/4) for large (r).  Both binomial denominators are therefore
at least their respective second binomial coefficients and are
(Omega(r^2)).  Dividing by the smaller endpoint degree is the maximum of
the preceding two ratios, so every target--target pair contributes
(O(r^{-2})).

For an owner (o_T) and a target (S\subset T), the exact codegree is

\[
d_x(o_T,S)=\frac{q_s}{\binom rs}
\le\frac{p_s}{\binom rs}
=\frac1{\binom{2r-s}{r-s}}.
\]

Here (a+1\le r-s\le b<r), so the denominator is at least
(inom r2) for large (r).  The owner degree is one and the target degree
is (1-o(1)), hence owner--target normalized codegree is also
(O(r^{-2})).  Distinct owners never coexist in an atom, and distinct
same-rank targets cannot coexist in a flag.  These exhaust all pair types.
Thus

\[
\rho_2=O(r^{-2}),\qquad
K^2\rho_2=O(r)O(r^{-2})=O(r^{-1})=o(1).
\]

In particular, the capacity truncation does not damage either conclusion:
it decreases every joint rank marginal, keeps all surviving target degrees
uniformly (1-o(1)), and enforces the asserted bound on (K).

For completeness, a (j)-rank same-parity flag has pre-cap marginal

\[
\tfrac12\prod_{i=1}^j(2p_{s_i})
=2^{j-1}\prod_{i=1}^j p_{s_i},
\]

and truncation only decreases it, exactly as recorded in the source.

## 4. Far-tail normalization

For every discarded rank (s<r-b), (j=r-s>b), so

\[
p_s\le e^{-b^2/(2r)}\le r^{-3}.
\]

There are fewer than (r) such nonempty ranks.  Hence

\[
\sum_{s<r-b}p_s\le r^{-2}=o(1),
\qquad
\sum_{s<r-b}\binom{2r}{s}
=W\sum_{s<r-b}p_s=o(W).
\]

This is a named-target count, not merely a probability under an unrelated
sampling measure.

## 5. Exact adjacent-rank collar chainization

Between ranks (s) and (s+1), every rank-(s) vertex has degree
(2r-s) and every rank-(s+1) vertex has degree (s+1).  Thus for every
family (X\subseteq\binom{[2r]}s),

\[
(2r-s)|X|\le(s+1)|N(X)|.
\]

For (s\le r-1), this implies (|N(X)|\ge|X|), so Hall gives a matching
saturating the entire lower shore.  Choose such a matching at each adjacent
pair from rank (r-a) through rank (r).

In the union of the upward-oriented matchings, each strict-lower collar
vertex has outdegree exactly one, every vertex has indegree at most one, and
rank strictly increases.  Consequently the components are vertex-disjoint
directed paths, not branching arborescences and not cycles.  Every collar
target belongs to exactly one path; its terminal rank-(r) owner is unique.
Adding singleton paths at unused rank-(r) owners yields exactly (W)
owner-indexed chains, each with at most one target in each of the (a)
collar ranks.

## 6. Composition boundary

The residual parity law is symmetric only before a collar path is assigned
to each owner.  A literal superposition would additionally require, for the
bottom (B_T) and collar load (ell_T),

\[
\max R_T\subseteq B_T,
\qquad |R_T|\le d-\ell_T.
\]

Neither independently constructed object enforces those inequalities.  The
source therefore correctly does **not** infer an integral residual matching,
an (o(W)) anchored chain deletion theorem, a suffix cocycle, interval
closure, upper coverage, or regeneration from the two marginal
constructions.  Pair-codegree subcriticality alone is also not promoted to a
growing-uniformity matching theorem.

## Final audit conclusion

No correction to the source theorem is required.  Its strongest positive
claim is a symmetric, capacity-truncated **fractional residual law** with
(o(W)) normalized defect and (K^2\rho_2=o(1)), plus a separate exact
collar chain partition.  Its strongest negative statement is equally
important: compatibility of those two objects remains an explicit open
premise.
