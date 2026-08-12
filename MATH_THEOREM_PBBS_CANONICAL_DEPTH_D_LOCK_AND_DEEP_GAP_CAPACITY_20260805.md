# Canonical depth-`d` singleton locks force the deeper compiler into their complementary gaps

**Date:** 2026-08-05  
**Method:** exact rank monotonicity and interval counting; no computation  
**Status:** unconditional on the canonical maximal-antecedent face.  Using
the automatic depth-`d` fan cells as singleton witnesses locks one maximal
source letter for every rank-`r-d` target.  Every deeper target interval must
avoid all locked positions.  Its complete scalar capacity is therefore the
sum of the truncated triangular interval counts of the complementary gaps.

## 1. Set-up

Let `T` be a cyclic `d`-resident simple rank-`r` Johnson trace of length
`W`, and let

\[
                         P_p=\bigcap_{t=0}^{d}T_{p-t}           \tag{1.1}
\]

be its maximal antecedent.  Then

\[
                         |P_p|=r-d                             \tag{1.2}
\]

at every position, and

\[
                         \bigcup_{h=q}^{d}P_{i+h}
                         =\bigcap_{j=0}^{q}T_{i+j}              \tag{1.3}
\]

for `0<=q<=d`.

Assume the depth-`d` fan is complete.  For every rank-`r-d` target `S`,
choose one position `p(S)` with

\[
                         P_{p(S)}=S.                            \tag{1.4}
\]

Distinct targets choose distinct positions.  Put

\[
 L=\{p(S):|S|=r-d\},
 \qquad
 U=W-|L|=W-{k\choose r-d}.                                  \tag{1.5}
\]

Call `L` the canonical singleton-lock set.

## 2. Lock theorem

### Theorem 2.1 (deep intervals avoid every canonical lock)

Let `A` be any nonzero depth-`d` antecedent with `D^dA=T` (and hence
`A_p subseteq P_p`).  Suppose the
chosen canonical singleton witnesses are retained literally:

\[
                         A_{p(S)}=S=P_{p(S)}                    \tag{2.1}
\]

for every rank-`r-d` target `S`.  If a source interval `I` satisfies

\[
                         \left|\bigcup_{p\in I}A_p\right|<r-d, \tag{2.2}
\]

then

\[
                         I\cap L=\varnothing.                  \tag{2.3}
\]

#### Proof

If `p(S) in I`, then (2.1) gives

\[
 S=A_{p(S)}\subseteq\bigcup_{p\in I}A_p.
\]

The interval union therefore has rank at least `|S|=r-d`, contradicting
(2.2). `square`

Thus preserving the automatic bottom row of the top-`d` fan is not free:
it converts its selected source positions into hard separators for every
target of lower rank.

## 3. Exact gap capacity

Assume `L` is nonempty and write the cyclic complement as maximal gaps of
unlocked positions of lengths

\[
                         g_1,\ldots,g_c,
                         \qquad \sum_{a=1}^{c}g_a=U.            \tag{3.1}
\]

Every strict-lower source interval has length at most `d`.  Define

\[
 F_d(g)=\sum_{\ell=1}^{\min(d,g)}(g-\ell+1)
 =
 \begin{cases}
   {g(g+1)\over2},&g\le d,\\[2mm]
   dg-{d(d-1)\over2},&g\ge d.
 \end{cases}                                                  \tag{3.2}
\]

### Corollary 3.1 (exact scalar deep-capacity cut)

On the canonical-lock face, a necessary condition for compiling every target
of rank below `r-d` is

\[
 \boxed{
 \sum_{s=1}^{r-d-1}{k\choose s}
 \le
 \sum_{a=1}^{c}F_d(g_a).}                                    \tag{3.3}
\]

#### Proof

By Theorem 2.1, every such target witness is a length-at-most-`d` interval
contained in one unlocked gap.  A gap of length `g` contains exactly
`F_d(g)` such physical intervals.  Distinct exact target values require
distinct physical intervals, so summing over the gaps proves (3.3).
`square`

The function `F_d` is superadditive: joining two gaps creates all their old
intervals and possibly additional crossing intervals.  Hence (3.3) implies
the weaker distribution-free cut

\[
 \sum_{s=1}^{r-d-1}{k\choose s}\le F_d(U).                    \tag{3.4}
\]

The gap distribution contains genuinely more information than (3.4).
Isolated or evenly spread locks can destroy most of the short-interval bank
even when the total number `U` of unlocked positions is large.

### Corollary 3.2 (required long-gap scale)

Let

\[
                         G=\max_a g_a,
 \qquad
                         L_{<}=\sum_{s=1}^{r-d-1}{k\choose s}. \tag{3.5}
\]

Since `F_d(g)/g` is nondecreasing in `g`, (3.3) gives

\[
                         {L_<\over U}\le {F_d(G)\over G}.      \tag{3.6}
\]

In particular, when `G<=d`,

\[
                         G\ge {2L_<\over U}-1.                 \tag{3.7}
\]

Thus any asymptotic regime with `L_</U=Omega(d)` forces an unlocked gap of
length `Omega(d)`.  A canonical depth-`d` occurrence SDR cannot be chosen
without regard to its cyclic spacing.

For the optimal deadline

\[
                         d=\sqrt{\pi k/8}+O(1),                 \tag{3.8}
\]

the standard central local limit and binomial-tail estimates give

\[
 {1\over W}{k\choose r-d}\longrightarrow e^{-\pi/4},
 \qquad
 {L_<\over dW}\longrightarrow
 2\Phi\!\left(-\sqrt{\pi/2}\right),                           \tag{3.9}
\]

where `Phi` is the standard normal distribution function.  Consequently,
(3.7), with the case `G>d` already stronger, implies

\[
 \liminf_{k\to\infty}{G\over d}
 \ge
 {4\Phi(-\sqrt{\pi/2})\over1-e^{-\pi/4}}
 >0.77.                                                       \tag{3.10}
\]

Thus the canonical bottom-row locks must leave an unlocked arc containing
asymptotically more than `77%` of a deadline.  Merely spreading one witness
for each target around the cycle is incompatible with deep scalar capacity.

There is also an extensive, rather than merely extremal, consequence.  For
`0<alpha<=1`, let

\[
 U_{\ge\alpha d}=\sum_{a:\,g_a\ge\alpha d}g_a.                \tag{3.11}
\]

For a shorter gap,

\[
 {F_d(g_a)\over g_a}={g_a+1\over2}
 \le {\alpha d+1\over2},                                    \tag{3.12}
\]

whereas every gap has `F_d(g_a)/g_a<=d`.  Therefore (3.3) implies

\[
 {U_{\ge\alpha d}\over U}
 \ge
 \left(
 {L_</U-(\alpha d+1)/2\over d-(\alpha d+1)/2}
 \right)_+.                                                  \tag{3.13}
\]

Taking `alpha=1/2` in the optimal-deadline regime yields

\[
 \liminf_{k\to\infty}{U_{\ge d/2}\over U}
 \ge
 {4\over3}
 \left(
 {2\Phi(-\sqrt{\pi/2})\over1-e^{-\pi/4}}-{1\over4}
 \right)
 >0.18.                                                       \tag{3.14}
\]

So a positive fraction of all unlocked positions must lie in gaps of length
at least half a deadline.  One exceptional long gap cannot pay the total
deep-target interval count.

## 4. Exact lock-transversal criterion

For each rank-`r-d` target `S`, let

\[
                         O_S=\{p:P_p=S\}.                       \tag{4.1}
\]

The nonempty fibres `O_S` partition the source positions.  A canonical lock
set is exactly a choice of one representative from every fibre.

### Proposition 4.1 (prescribed free-bank criterion)

Let `R` be any prescribed set of source positions.  There is a canonical
lock set `L` disjoint from `R` if and only if

\[
                         O_S\not\subseteq R
                         \quad\hbox{for every }S.               \tag{4.2}
\]

#### Proof

Necessity is immediate.  Conversely, (4.2) permits choosing one position
from each nonempty set `O_S setminus R`.  Choices for different targets are
automatically distinct because their exact-value fibres are disjoint.
`square`

Thus lock placement has no hidden matching problem.  Its exact obstruction
is a fibre-transversal cut: a proposed free bank may not swallow every
occurrence of even one rank-`r-d` target.

### Corollary 4.2 (count-feasible protected free bank)

Suppose `R` is a union of disjoint cyclic intervals of lengths
`h_1,...,h_t`, separated by positions outside `R`, and

\[
                         O_S\not\subseteq R
                         \quad\hbox{for every }S,               \tag{4.3}
\]

\[
 \sum_{a=1}^{t}F_d(h_a)
 \ge
 \sum_{s=1}^{r-d-1}{k\choose s}.                             \tag{4.4}
\]

Then one can select the entire canonical depth-`d` singleton row while
leaving every position of `R` unlocked, and `R` alone contains at least as
many physical short intervals as there are deeper targets.

This is only scalar feasibility, not exact deep compilation.  But it
separates the next positive construction target cleanly: build a large
block-structured set `R` that is not a transversal of any complete
occurrence fibre, then solve the coordinate-value atlas inside `R`.

## 5. Exact scope

This theorem is a necessary cut, not a no-go theorem.

1. A construction may realize rank-`r-d` targets by noncanonical longer
   intervals instead of locking their maximal singleton cells.
2. Passing (3.3) counts physical intervals only; it does not assign their
   exact target values or satisfy the coordinate positive-hit cuts.
3. The theorem does not include typed suffix capacities.
4. On a linear opening, one uses the ordinary linear complementary gaps and
   adds the separately priced boundary collar.

Its role is to expose the first exact correlation between the automatic
top-`d` source row and the remaining deeper compiler: canonical occurrence
selection must simultaneously create enough long unlocked gaps.

## 6. Dependencies

The row identity and canonical source-cell lift are in

`MATH_THEOREM_PBBS_MAXIMAL_ANTECEDENT_INTERSECTION_SOURCE_ROW_IDENTITY_20260805.md`.

The fact that exact target values require distinct physical intervals is
Theorem 1.1 of

`MATH_THEOREM_PBBS_RIGID_ROTATION_FIXED_ANTECEDENT_COMPILER_AND_EXACT_CAP_CUT_20260805.md`.
