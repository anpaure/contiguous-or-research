# Independent audit: promotion-ring same-block triple lower bound

Date: 2026-07-26

Audited source:
`MATH_THEOREM_PROMOTION_RING_R2_BLOCK_FLOOR_AND_GLOBAL_LATENT_OVERLAP_20260726.md`.

Method: independent hand verification; no computation or external search.

## 0. Verdict

The same-block triple theorem is correct under its exact hypotheses:

1. one fixed partition of the roots into blocks of size at most \(B\);
2. arbitrary dependence inside a block and independence between blocks;
3. balanced compatible-pair marginal \(p=M/\binom MH\); and
4. calibrated \(H\), so \(Rp=1+o(1)\).

Its exact asymptotic conclusion is

\[
 \boxed{
  B-1\ge(1-o(1))
  {L(R-1)\over\binom{m+\tau}{\tau}},}
\tag{0.1}
\]

where

\[
 R=\binom mH,\qquad L=\binom{m+H}{H},
\]

and \(H^2/(m\tau)=o(1)\).  For
\(\tau=\lceil(\log m)^2\rceil\), this gives

\[
                         B\ge R^{2-o(1)}.
\tag{0.2}
\]

The converse \((e^{-1}-o(1))W\) hole floor is valid in the stated
little-\(o\) regime

\[
 B=o\!\left({LR\over\binom{m+\tau}{\tau}}\right).
\tag{0.3}
\]

It is not proved merely from a fixed-factor inequality below the threshold.

## 1. Root-pair multiplicity

Let \(A,A'\in\binom{[2m]}{m-H}\) be distinct roots and put

\[
                         t=m-|A\cup A'|.
\tag{1.1}
\]

If both roots lie in a middle target \(D\), then \(|A\cup A'|=m-t\).
There are \(m+t\) coordinates outside this union, and \(D\) is obtained
by adjoining exactly \(t\) of them.  Therefore the number of common
middle targets is exactly

\[
                         \boxed{\binom{m+t}{t}.}
\tag{1.2}
\]

There is no missing orientation factor and no factor of two: the roots
are an unordered pair on both sides of the final triple count.

## 2. High-overlap root pairs are globally negligible

Inside a fixed target write

\[
                         A=D\setminus I,qquad
                         A'=D\setminus I',
\]

with \(I,I'\in\binom DH\).  Then \(t=|I\cap I'|\).  For a uniform
ordered pair of distinct roots,

\[
 \mathbb Et
 ={RH^2/m-H\over R-1}
 \le {R\over R-1}{H^2\over m}.
\tag{2.1}
\]

Thus

\[
 \Pr(t>\tau)
 =O\!\left({H^2\over m\tau}\right)=o(1).
\tag{2.2}
\]

This deletion must be made globally: over all targets, the total number
of \(t>\tau\) root-pair incidences is \(o(W R^2)\).  It is not legitimate
to assume separately that the dominant block of every target contains a
typical pair distribution.  The source proof uses the correct global
subtraction.

## 3. Dominant-block implication

For a target \(D\), let

\[
 r_j(D)=|\mathcal B_j\cap\mathcal R(D)|,
 \qquad \mu_j(D)=p r_j(D).
\]

If \(\max_jr_j(D)\le(1-\varepsilon)R\), calibration gives
\(\max_j\mu_j(D)\le1-\varepsilon/2\) eventually.  Markov inside each
block and independence between blocks give

\[
 \Pr(D\text{ missed})
 \ge\prod_j(1-\mu_j(D))
 \ge e^{-2\theta/\varepsilon}.
\tag{3.1}
\]

If some \(\mu_j(D)\ge1\), then

\[
 r_j(D)\ge p^{-1}=R/\theta=(1-o(1))R.
\]

Therefore expected \(o(W)\) holes force, for all but \(o(W)\) targets,
one block containing \((1-o(1))R\) roots.  A diagonal
\(\varepsilon_m\downarrow0\) justifies the displayed \(o(1)\) uniformly
on a \(1-o(1)\) target set.

## 4. Triple double count

After selecting one dominant block for every nonexceptional target and
discarding all globally exceptional \(t>\tau\) pairs, the lower count is

\[
                         (1-o(1))W\binom R2.
\tag{4.1}
\]

By (1.2), every remaining same-block root pair is counted for at most
\(\binom{m+\tau}{\tau}\) targets.  Hence

\[
 (1-o(1))W\binom R2
 \le
 \binom{m+\tau}{\tau}
 \sum_j\binom{|\mathcal B_j|}{2}.
\tag{4.2}
\]

Since the blocks partition the \(N_H\) roots,

\[
 \sum_j\binom{|\mathcal B_j|}{2}
 \le{(B-1)N_H\over2}.
\tag{4.3}
\]

Using \(W/N_H=L/R\) in (4.2)--(4.3) proves (0.1).

## 5. Converse audit

Let

\[
 Q={1\over WR^2}\sum_D\sum_jr_j(D)^2.
\]

The same low-/high-overlap split gives

\[
 Q\le {H^2\over m\tau}
 +{B\binom{m+\tau}{\tau}\over LR}.
\tag{5.1}
\]

Under (0.3), \(Q=o(1)\).  Hence, for almost every target,

\[
 \max_jr_j(D)/R=o(1).
\]

Thus \(\max_j\mu_j(D)=o(1)\), while
\(\sum_j\mu_j(D)=\theta=1+o(1)\).  Therefore

\[
 \prod_j(1-\mu_j(D))
 =\exp(-\theta-o(1))=e^{-1}-o(1),
\]

which proves the audited converse.

## 6. Asymptotic audit

At the calibrated height,

\[
 \log R=left({1\over2}+o(1)\right)
          \sqrt m(\log m)^{3/2},
 \qquad L=(1+o(1))mR.
\]

For \(\tau=\lceil(\log m)^2\rceil\),

\[
 \log\binom{m+\tau}{\tau}=O((\log m)^3)=o(\log R).
\]

Thus (0.1) has logarithm

\[
 \log B\ge2\log R-o(\log R)
 =(1+o(1))\sqrt m(\log m)^{3/2}.
\]

## 7. Scope

The theorem is a block-independence obstruction, not a latent-support
obstruction.  A deterministic good design, if one exists, has support one;
its common coordinate orbit has at most \((2m)!=\exp(o(R))\) states and
uniform root-frame marginals.  Therefore the \(R^{2-o(1)}\) conclusion
cannot be transferred to one unrestricted global latent variable.

The deterministic residue of the double count is exactly the weighted
overlap-capacity inequality \(\Phi_\tau\) stated in Section 6 of the
source theorem.
