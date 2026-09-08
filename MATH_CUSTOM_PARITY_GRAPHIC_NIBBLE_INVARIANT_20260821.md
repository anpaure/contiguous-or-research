# A component-charge invariant for a custom one-central nibble

**Status (2026-08-21).**  The reductions and obstructions below are proved.
They do not construct the missing palette selection.  They give an exact
sequential quantity whose `o(W)` control would finish every rank postponed
after the one-central matching, and show why pair codegrees alone cannot
control that quantity.  The missing input is a high-order,
component-sensitive correlation theorem for whole queue-coherent path
bundles.

## 1. Ordered postponed-rank decks

Use the budget-normalized palette with `s` slots and common core length
`a`.  Let `B_ch` be the total number of discarded rank-incidences, with
`B_ch=0` if no observations are discarded.  Once a legal band-simple path
is chosen in slot `i`, its rank-`q`
deck, in temporal order, is

\[
 U_{i,q}=(B_{i,q,1},\ldots,B_{i,q,a}).                 \tag{1.1}
\]

The entries in (1.1) are distinct.  Add a private vertex `z_(i,q)` and
regard the deck as the augmented `a`-edge path

\[
 E_{i,q}:\quad
 z_{i,q}B_{i,q,1},\ B_{i,q,1}B_{i,q,2},\ldots,
 B_{i,q,a-1}B_{i,q,a}.                                \tag{1.2}
\]

All real edges after the private root edge lie in `J(n,q)`.  Write

\[
 r_{i,q}+h_{i,q}=a                                    \tag{1.3}
\]

for the real and dummy quotas.  As proved in
`MATH_CANDIDATE_CYCLOMATIC_HALL_GRAPHIC_ROUNDING_20260821.md`, if
`epsilon_q` is the minimum number of unmatched graphic-quota clones, then

\[
 \epsilon_q
 =\max_{I\subseteq[s]}
   \left(\beta_q(I)-\sum_{i\in I}h_{i,q}\right)_+,
 \qquad
 \epsilon_q\le\delta_q\le\epsilon_q+s.               \tag{1.4}
\]

Here `beta_q(I)` is the cyclomatic rank of the union of the unaugmented
temporal deck paths.  The private root edges are bridges and do not change
it.

## 2. Exact sequential cycle charge

Let `F` be any forest made from augmented edges of paths already selected
at rank `q`, and let `E` be a new augmented deck path.  Its private root is
new.  For every component `C` of `F` met by the real vertices of `E`, put

\[
 z_C=|V(E)\cap V(C)|,
 \qquad
 \kappa(E\mid F)=\sum_C(z_C-1)_+.                     \tag{2.1}
\]

Thus a first visit to an old component is free and every further visit to
the same component costs one.

### Lemma 2.1 (exact component charge)

The cyclomatic rank of `F union E` is exactly

\[
 \beta(F\cup E)=\kappa(E\mid F).                       \tag{2.2}
\]

Consequently one can delete exactly `kappa(E|F)` edges of `E` and retain a
forest containing all of `F`.

#### Proof

Let `z=sum_C z_C`, and let `c` be the number of old components met.  The
new path is a tree with `a` edges and `a+1` vertices.  On adjoining it, `z`
vertices are identified with old vertices and the `c` old components it
meets are joined into one.  Hence

\[
 \Delta(|E|-|V|+g)=a-(a+1-z)+(1-c)=z-c
 =\sum_C(z_C-1).
\]

This is (2.2), including the case `z=c=0`.  Extend the independent edge
set `F` greedily inside the graphic matroid using edges of `E`.  A maximal
extension omits exactly the rank excess in (2.2), and all omitted edges may
therefore be taken from `E`.  \(\square\)

Consider any ordering of the selected slots.  Starting with the empty
forest, after choosing path `i` at rank `q`, apply Lemma 2.1 and retain a
maximum subset of its augmented edges that preserves the forest.  Write

\[
 \kappa_{i,q}=\kappa(E_{i,q}\mid F_{i-1,q}),
 \qquad
 Z_q=\sum_{i=1}^s(\kappa_{i,q}-h_{i,q})_+.             \tag{2.3}
\]

### Theorem 2.2 (custom-nibble completion criterion)

For every rank `q`, the graphic quota deficiency obeys

\[
 \epsilon_q\le Z_q,
 \qquad
 \delta_q\le Z_q+s.                                   \tag{2.4}
\]

Therefore, if one common path per slot is selected so that

1. its retained rank-`m` decks are pairwise disjoint, and
2. `sum_(q in K\setminus\{m\}) Z_q=o(W)`,
3. `W-sa=o(W)`, `|K|s=o(W)`, and the discarded-incidence charge
   `B_ch=o(W)`,

then

\[
 \sum_{q\in K\setminus\{m\}}\delta_q=o(W),             \tag{2.5}
\]

and the coefficient-one DCC follows from the one-central reduction.

#### Proof

Lemma 2.1 retains `a-kappa_(i,q)` independent augmented edges from block
`i`.  The block has `r_(i,q)=a-h_(i,q)` graphic clones, so at most

\[
 (r_{i,q}-(a-\kappa_{i,q}))_+
   =(\kappa_{i,q}-h_{i,q})_+
\]

of them remain unmatched.  The union of all retained edges is a forest,
so summing these shortfalls gives the first inequality in (2.4).  Equation
(1.4) gives the second.  Finally `|K|s=o(W)` for the palette parameters,
and (2.5) follows.  \(\square\)

At the postponed middle rank all `h_(i,m+1)=0`.  The charge is zero exactly
when the new deck visits every old forest component at most once.  This is
the precise graphic acceptance rule.  It permits tree-like target reuse;
only repeated visits to one already connected component create charge.

## 3. The component susceptibility that a semi-random proof must control

Let a canonical band-simple rank-`q` deck be denoted by `U`, let
`M_q={n\choose q}`, and define its conditional pair kernel

\[
 K_q(S,T)=\Pr(T\in U\mid S\in U)\qquad(S\ne T).       \tag{3.1}
\]

Relabeling symmetry gives `Pr(S in U)=a/M_q`, and the kernel is symmetric.
For a fixed forest `F`, let its nontrivial target-vertex components be
`C` and define

\[
 \mathcal S_q(F)
 = {1\over 2M_q}\sum_C\sum_{\substack{S,T\in C\\S\ne T}}K_q(S,T).
                                                               \tag{3.2}
\]

### Lemma 3.1 (susceptibility bound)

For an independent canonical deck,

\[
 \mathbb E\,\kappa(E(U)\mid F)\le a\,\mathcal S_q(F). \tag{3.3}
\]

#### Proof

If `Z_C=|U\cap C|`, then
`(Z_C-1)_+\le {Z_C\choose2}`.  Hence

\[
\begin{aligned}
 \mathbb E\kappa
 &\le\sum_C\sum_{\{S,T\}\subseteq C}
       \Pr(S,T\in U)\\
 &= {a\over2M_q}\sum_C\sum_{S\ne T\in C}K_q(S,T),
\end{aligned}
\]

which is (3.3).  \(\square\)

For an arbitrary seed-independent branch law inside one
common-transformation fiber, after the seed is uniformized, relabeling
symmetry alone does **not** give an all-distance bound
`max_(S ne T)K_q(S,T)=O(n^(-2))`.  Already at the central rank `q=m`, if
`j` is Johnson distance and `N_j={m\choose j}{m+1\choose j}`, it gives only
the distance-profile estimate

\[
 K_m(S,T)\le {a-1\over N_j}\quad(2\le j\le m),       \tag{3.4}
\]

while central chordlessness gives

\[
 K_m(S,T)={2(a-1)\over a\,m(m+1)}=O(n^{-2})
 \quad(j=1).                                         \tag{3.5}
\]

Indeed, a deck contains at most `{a\choose2}` distance-`j` pairs, and
there are `M_mN_j/2` such unordered target pairs.  The denominator `N_j`
is only `m+1` at the antipodal distance `j=m`; hence (3.4) permits a much
larger far-pair codegree.  The same issue occurs at the extreme available
distances of other ranks.  By contrast, the original uniformly random
free-core law of the fixed-endpoint palette does have maximum middle-rank
kernel `O(n^(-2))`, by its history-conditioned return bound.  That stronger
law is not inherited by an arbitrary common-transformation fiber and is not
known after coverage conditioning.  No uniform all-distance `O(n^(-2))`
statement for every postponed rank of the live conditioned process is
currently proved.

For the **matched central rank only**, one may strengthen the support by
discarding every word whose deck contains an antipodal (`j=m`) pair.  The
discarded fraction is `exp(-n/2+o(n))` for polynomial `a`.  On that
antipode-free, centrally chordless support, (3.4)--(3.5) imply

\[
 \max_{S\ne T}K_m(S,T)
 =O\!\left({a\over n^3}+{1\over n^2}\right).         \tag{3.6}
\]

Thus (3.6) is `O(n^(-2))` when `a=Theta(n)`, and
`O((log n)/n^2)` when `a=Theta(n log n)`.  This statement is annealed over
a uniform seed and any seed-independent branch law; it must not be used
after arbitrary residual conditioning.

If one *assumes* a uniform conditional kernel bound `K_q=O(n^(-2))` for
a postponed rank, Lemma 3.1 yields

\[
 \mathbb E\kappa
 \le O\!\left({a\over M_qn^2}\sum_C|C|^2\right).     \tag{3.7}
\]

This scalar estimate cannot close Theorem 2.2.  Even if previously chosen
length-`a` paths never merge, at core volume `\Theta(W)` their components
have square mass `\Theta(Wa)`.  Summing (3.7) over `\Theta(W/a)` later block
choices gives only `O(Wa/n^2)`, which is not `o(W)` for the required
`a>>n^3`.  The failure is in the estimate, not a lower bound on the true
charge: most pairs of vertices in one legal path have much smaller joint
probability than the worst Johnson-adjacent pair.

Thus a successful semi-random proof needs a distance- and chronology-
sensitive strengthening of the full profile (3.4), or directly an invariant of the form

\[
 \sum_{i,\,q\in K\setminus\{m\}}
 a\,\mathcal S_q(F_{i-1,q})=o(W),                    \tag{3.8}
\]

under the conditional law used to choose the next rank-`m`-compatible path.
Equation (3.8), together with concentration or a conditional-expectation
choice, would imply the cycle-charge target.  Maximum pair codegree does
not imply (3.8), because it forgets which target pairs have already become
connected.

The benefit of the new common-transformation backbone is visible in the
following precise conditional statement.  It permits microblocks of length
`a=Theta(n)` without paying a separate bridge per microblock.

### Corollary 3.2 (a sufficient linear-microblock nibble invariant)

Use the linear-checkpoint normalization, so
`W-sa=o(W)`, `|K|s=o(W)`, and
`B_ch<=|K|s=o(W)`.  Suppose a sequential common-path selection with
`a=Theta(n)` has the
following properties at every step, conditional on its complete past.

1. Its next-path law is supported on choices preserving the required
   rank-`m` resource packing.
2. At every `q in K\setminus\{m\}` and for all distinct rank-`q` targets,

   \[
   \Pr(S,T\in U_{i,q}\mid\text{past})
      \le {C\Lambda_n a\over M_qn^2}.                  \tag{3.9}
\]

   Here `Lambda_n>=1` is uniform in `i,q`; the original stated hypothesis
   is the special case `Lambda_n=1`.

3. The maintained rank-`q` forest has target components satisfying

   \[
   \sum_C|C|^2\le C'M_qa.                              \tag{3.10}
\]

Then one realization of the selection has

\[
 \sum_{i=1}^s\sum_{q\in K\setminus\{m\}}\kappa_{i,q}
 =O\!\left({W|K|\Lambda_n\over n}\right)=o(W),       \tag{3.11}
\]

provided `|K|Lambda_n=o(n)`.

In particular it satisfies Theorem 2.2, even before using the dummy
allowances.

#### Proof

As in Lemma 3.1, (3.9)--(3.10) give, conditionally at each step and rank,

\[
 \mathbb E(\kappa_{i,q}\mid\text{past})
 \le {C\Lambda_na\over M_qn^2}\sum_C { |C|\choose2}
 =O(\Lambda_na^2/n^2)=O(\Lambda_n).                  \tag{3.12}
\]

There are `s=O(W/a)=O(W/n)` microblocks and
`|K|=O(sqrt(n log n))` band ranks.  Summing conditional expectations
gives the first bound in (3.11), and it is `o(W)` under the displayed
condition.  Some outcome is no larger
than its expectation.  Since `(kappa-h)_+<=kappa`, Theorem 2.2 applies.
\(\square\)

Corollary 3.2 is not yet an existence proof: neither (3.9) after conditioning
on the evolving rank-`m` packing nor the component-square invariant (3.10) has
been established.  It isolates them as two quantitative assertions that
would suffice.  For the old bridge-separated palette, where `a>>n^3`, the
same calculation gives only `O(W|K|a/n^2)` and is useless; linear checkpoint
spacing is essential.  Proposition 2.2 of the quenched-gate note verifies
the annealed kernel scale only for the antipode-free **central matched**
rank.  It supplies no part of hypothesis (3.9) for the postponed graphic
ranks, and it supplies no quenched bound after conditioning on the evolving
packing.  Thus Corollary 3.2 remains logically valid but wholly conditional
at exactly the two advertised gates.

## 4. Exact second-order blindness in one continuation fan

There is also a local obstruction to any invariant that records only
single-rank densities and pair intersections.  Fix a state
`pi=(p_1,...,p_n)` and let `D={p_f,...,p_n}` be its `d` eligible letters.
For `k<f` and `x in D`,

\[
 \Phi_k(x)=C_k(T_x\pi)=\{x,p_1,\ldots,p_{k-1}\}.       \tag{4.1}
\]

The map `Phi_k` is injective.  Given residual target families `R_k`, put

\[
 Y_k=\{x\in D:\Phi_k(x)\in R_k\}.                     \tag{4.2}
\]

The number of generators whose next observation is residual at every rank
in a set `R` is exactly `|\bigcap_{k\in R}Y_k|`.

### Theorem 4.1 (pairwise-indistinguishable fans)

Let `t>=2`, put `r=2^t-1`, and choose any `r` distinct ranks below `f`.
There are two systems of residual families having the same global
cardinalities and satisfying, inside the continuation fan,

\[
 |Y_k|=b2^{t-1},\qquad
 |Y_k\cap Y_l|=b2^{t-2}\quad(k\ne l),                 \tag{4.3}
\]

where `b=floor(d/2^t)`, but for which respectively

\[
 \left|\bigcap_kY_k\right|=b,
 \qquad
 \left|\bigcap_kY_k\right|=0.                        \tag{4.4}
\]

The at most `d-b2^t` unused eligible letters belong to none of the `Y_k`
in either system.

#### Proof

Index the chosen ranks by the nonzero vectors `u\in\mathbb F_2^t`.  Identify
`b2^t` eligible letters with pairs
`(z,j)\in\mathbb F_2^t\times[b]`.  In the
first system put `(z,j) in Y_u` when `u dot z=0`; in the second put it in
`Y_u` when `u dot z=1`.

Every nonzero linear form is balanced.  Two distinct nonzero vectors over
`\mathbb F_2` are linearly independent, so every prescribed pair of dot products
has `2^(t-2)` solutions.  This proves (4.3) for both systems.  In the first
system the common intersection consists exactly of the copies of `z=0`.
In the second it is empty: if two independent forms both take value one,
their nonzero sum takes value zero.

Finally, by injectivity of (4.1), prescribe these memberships on the fan
targets.  The two systems already have identical cardinalities there; if a
larger common global cardinality is desired, pad both identically outside
the fan whenever such targets are available.  \(\square\)

Thus, in the intended regime `r<d`, exact one- and two-rank fan statistics
can coexist with either `Theta(d/r)` legal continuations or none.  Favorable
pair-codegree data are second-order and cannot, without an
additional structural invariant, certify even one next move.

For comparison, if the sets `Y_k` are independently Bernoulli with density
`eta`, then

\[
 \left|\bigcap_{k\in R}Y_k\right|
 \sim {\rm Bin}(d,\eta^{|R|}),
 \qquad
 \Pr\!\left(\bigcap_kY_k\ne\varnothing\right)
 \le d\eta^{|R|}.                                     \tag{4.5}
\]

For `R=K\setminus\{m\}`, `|R|=\Theta(\sqrt{n\log n})`.
Rankwise-independent residuals
therefore lose all fully clean generators after used density only

\[
 (1+o(1)){\log d\over |R|}
   =\Theta\!\left(\sqrt{{\log n\over n}}\right).       \tag{4.6}
\]

This last calculation applies only to a pointwise algorithm demanding a
clean observation at every chosen rank.  Deferred real/dummy decoration
can be more flexible.  It nevertheless proves that a useful custom nibble
must deliberately create high-order alignment rather than preserve
rankwise-independent residuals.

## 5. Surviving theorem

The exact iterative target is now:

> Choose the rank-`m`-matching paths while maintaining forests `F_(i,q)` so that
> the cumulative excess repeated-component charge
> `sum_(i,\,q in K\setminus\{m\})(kappa_(i,q)-h_(i,q))_+` is `o(W)`.

Tree-like overlap is free up to the sublinear boundary term, dummy quota
pays the first allowed cycle charges, and only the excess in (2.3) matters.
Postponed-rank pair data are consistent with this target but do not prove it:
the required state
variable is the component susceptibility (3.2), an all-order property of
the previously selected path bundles.  The proved fiber rigidity rules out
only a post hoc opposite-central repair after the retained rank-`m` decks
are frozen; it does not settle all postponed ranks.  A successful proof must
either preserve (3.8), equivalently establish (3.9)--(3.10), during the common
selection or use global augmentations that revise previously chosen paths.
