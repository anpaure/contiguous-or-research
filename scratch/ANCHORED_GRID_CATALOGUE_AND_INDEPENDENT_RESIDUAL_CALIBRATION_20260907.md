# Anchored grid catalogue: a parameter calibration for residual placement

Date: 2026-09-07. Symbolic counting, no computation.

Consider the many-root grid of
`/Users/amir.nuriyev/.codex/worktrees/7796/problem/research_round1/MANY_ROOT_CROSSED_RAIL_GRID.md`.
Its parameters are b=4B, h>=2, K>=1, B>2Kh. Put

    ell=4Kh+1, t=4(2K+1), M=2t ell,
    R=(2K+1)^2, n_0=M-6R.

The template has n_0 distinct middle targets, including its complementary
branch. Its common oriented intersection F has size b-8Kh; the complement
G of its oriented union has the same size. Precisely16Kh coordinates
vary, in four ordered lists of length4Kh. The labels inside F and G have
no further role in the target support.

## Anchored catalogue bound

For any fixed b-subset T, the number of distinct coordinate-relabelled
grid supports containing T is at most

    n_0 (b)_(8Kh)^2 <= M b^(16Kh).                         (1)

Indeed choose which of the n_0 template targets is mapped to T. In that
role exactly8Kh active template labels belong to the target and8Kh do
not. Assign their distinct images, in order, from T and T^c. This gives
at most (b)_(8Kh)^2 choices. The remaining labels of T form F and those
of T^c form G, or vice versa for a complementary role. Their internal
permutations do not change the support. This also handles non-root roles;
anchoring only one preferred root would not bound all usable vertices.

## Independent residual statement

Retain each middle target independently with fixed probability rho in
(0,1), and let U be the retained family. Conditional on T being retained,
any fixed support from (1) lies wholly in U with probability rho^(n_0-1).
Thus

    P(T belongs to a wholly retained grid | T in U)
       <= min(1, M b^(16Kh) rho^(n_0-1)).                  (2)

If K/log b -> infinity, then the right side tends to zero. Indeed,
`n_0=(2K+1)((32h-12)K+2)>=52K^2h` for h>=2, while log M=O(log b),
using Kh<b/8. The logarithm of the nontrivial expression in (2) is

    O(log b)+16Kh log b+(n_0-1)log rho -> -infinity.

Consequently the expected number of retained targets lying in any wholly
retained grid is o(W), W=binom(2b,b). Markov's inequality gives o(W)
such targets with probability tending to one. Meanwhile |U|=(rho+o(1))W
by independence and the variance bound W rho(1-rho).

Therefore this independent residual cannot be near-completely packed by
whole grids with K/log b -> infinity, even if a few such grids exist.

## Scope

This is a calibration of one residual model, not a general grid-packing
obstruction. The vanishing bound applies to K/log b -> infinity, for
example K=(log b)^2 when Kh<b/8. It gives no obstruction when K grows
slowly, for example K=log log b, and neither proves availability at that
smaller scale nor excludes a structured
residual. It also does not apply unchanged when only part of a grid must
be new, old backup occurrences can be reused, or admissibility includes
controlled collisions. The exact within-grid gains and literal compiler
remain valid. A factorial count of all coordinate permutations would
overcount the unordered F/G labels and miss this anchored restriction.
