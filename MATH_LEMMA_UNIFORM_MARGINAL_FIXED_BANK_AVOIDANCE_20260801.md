# Uniform common-basis marginals avoid every fixed subcritical bank

Date: 2026-08-01  
Status: unconditional probabilistic corollary, conditional only on the
existence of the stated uniform-marginal common-basis distribution (which
the strict-balanced-expansion theorem supplies on an SBE state).

## Lemma

Let `E` be a finite ground set and let `mathcal B` be a family of subsets of
`E`.  Suppose there is a probability distribution `mu` on `mathcal B` with
constant one-point marginals

\[
                         \Pr_{B\sim\mu}(e\in B)=p
                         \qquad(e\in E).               \tag{1}
\]

Then for every fixed `D subseteq E`, some `B in mathcal B` satisfies

\[
                         |B\cap D|\le\lfloor p|D|\rfloor. \tag{2}
\]

In particular,

\[
                              p|D|<1                    \tag{3}
\]

implies that some admissible `B` is completely disjoint from `D`.

### Proof

Linearity of expectation gives

\[
 \mathbb E_{B\sim\mu}|B\cap D|
   =\sum_{e\in D}\Pr(e\in B)=p|D|.                    \tag{4}
\]

At least one integer-valued outcome is at most the floor of its mean.  Under
(3) that outcome is zero.  No independence or negative dependence is used.
\(\square\)

## Strict-Catalan consequence

On a two-shore strict-balanced-expanding Catalan state, the common-basis
theorem supplies (1) with

\[
                  p={C\over N}={2(2n+1)\over n(n+2)}
                    =\Theta(n^{-1}).                   \tag{5}
\]

Therefore every bank `D` fixed **before** the common basis is selected, with

\[
                             |D|=O(\sqrt n),             \tag{6}
\]

is avoided completely for all sufficiently large `n`.  In particular a
fixed number of protected pivot collars, or any other independently fixed
`O(d)` damage bank with `d=Theta(sqrt(n))`, creates no puncture collision in
the common-basis row.

The quantifier is load-bearing.  The lemma does not apply when `D=D(B)` is
chosen adaptively from the selected basis, nor does it preserve uniform
marginals after conditioning, select a connector tree, impose head
injectivity, or establish source/cap compatibility.  It removes only the
collision between an independently fixed subcritical bank and the strict
common-basis punctures.
