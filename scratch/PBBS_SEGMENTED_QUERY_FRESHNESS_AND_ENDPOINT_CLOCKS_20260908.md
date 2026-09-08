# Segmented deferred decisions and canonical endpoint clocks

2026-09-08. Pure finite proofs; no numerical calculation or search. This note gives an exact aggregate-query filtration, a large-cell geometric approximation, and a finite-query implementation of canonical endpoint-started clock words with an explicit no-wrap cutoff. It does not identify a fresh law for arbitrary reached roots, prove eligible-label abundance, or close the physical overlap gate.

Review status: the worktree root read the complete note and passed its audit of the exact variance, stopped density control, online coupling and cemetery convention, canonical original indices, reverse no-wrap grouping, and oracle query-count tightness on 2026-09-08.

The accepted inputs are:

- `PBBS_FINITE_ADAPTIVE_GAP_QUERY_FRESHNESS_20260908.md` and its underlying finite-layer incidence fibre;
- `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_finite_layer_zero_triangle_incidence_fibre.md`;
- `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md`, Sections 3–4;
- `/Users/amir.nuriyev/.codex/worktrees/e333/problem/research_round1/pbbs_original_array_shift_cocycles.md`, Sections 1–3.

## 1. Exact cell-query model

First consider finitely many independent uniform weak compositions. In one row, a labelled set `I` of size `n` carries nonnegative integers `(Z_i)_(i in I)` of known total `m`. Already fixed coordinates, including base-triangle zeros, are recorded separately.

Maintain a partition of the unrevealed labels into **cells**, each with its known total. A cell may be an interval of original labels or a more general labelled subset. The following observations are legal:

1. A cell-sum query chooses a cell `I` and a proper nonempty subset `A subset I`, using only the exposed environment, an independent seed, and the previous transcript. It reveals `sum_(i in A) Z_i`. Replace `I` by `A` and `I\A`, with the resulting known totals.
2. An individual query is the special case `A={i}`. Record that value and remove its singleton cell from the unrevealed system.
3. A query of a base coordinate, a previously observed coordinate, or a known singleton returns its already determined value. It is never resampled.

The selected subset and the decision to query or stop must be measurable before the new answer is supplied. An inverse-prefix location, reached-phase description, or first-passage index determined by unrevealed values is not a legal additional input merely because it can be named.

Ordinary prefix observations fit this model. With only prefix observations, their endpoints partition a row into intervals with known totals, and the next prefix splits one such interval. With other observations present, a prefix can be evaluated by querying its intersection with each currently intersected cell and adding the answers and known complete-cell totals. This may reveal more information than the original prefix total, which is allowed. For a bounded number of observations the number of cells and the resulting number of constituent sum queries remain bounded.

### Proposition 1: exact segmented deferred decisions

Conditional on any feasible legal transcript, every unrevealed cell is a uniform weak composition of its known total into its labelled coordinates. These cell vectors are conditionally independent, including cells in different rows.

**Proof.** This is true initially. At a sum query, the chosen cell and subset are fixed conditional on the past. If the cell has size `n`, total `m`, and `A` has size `k`, then conditioning its subtotal to equal `a` leaves independent uniform compositions of `a` into `A` and `m-a` into its complement: every pair of such compositions had the same original probability. Other cells are unaffected. A singleton observation is the same argument. Determined replies change no conditional distribution. Inducting also accounts for the information conveyed by the chosen indices and stopping rule, since these are functions of the existing transcript. `square`

Equivalently, a cell of size `n` and total `m` has the law of `n` independent geometric variables with any common parameter in `(0,1)`, conditioned on their sum being `m`. The geometric parameter cancels from this conditional law. This exact observation does not remove the conditioning on the cell total.

## 2. Exact subtotal law and variance

For a cell as above and `1<=k<n`, stars and bars gives

\[
 \Pr(X=a\mid\text{past})=
 \frac{\binom{a+k-1}{k-1}\binom{m-a+n-k-1}{n-k-1}}
      {\binom{m+n-1}{n-1}},\qquad 0\le a\le m,
 \tag{1}
\]

where `X=sum_(i in A)Z_i`. In particular,

\[
 \boxed{\mathbb E(X\mid\text{past})=\frac{km}{n},\qquad
 \operatorname{Var}(X\mid\text{past})=
 \frac{mk(n-k)(m+n)}{n^2(n+1)}.} \tag{2}
\]

Here is a derivation of the variance directly from the composition count. Symmetry gives `E Z_i=m/n`. The generating functions

\[
 \sum_{a\ge0}a(a-1)z^a=\frac{2z^2}{(1-z)^3},\qquad
 \sum_{a\ge0}az^a=\frac{z}{(1-z)^2}
\]

and coefficient extraction against the other composition coordinates give

\[
 \mathbb E(Z_i)_2=\frac{2(m)_2}{n(n+1)},\qquad
 \mathbb E Z_iZ_j=\frac{(m)_2}{n(n+1)}\quad(i\ne j).
\]

Consequently `E(X)_2=k(k+1)(m)_2/[n(n+1)]`. Adding `EX` and subtracting `(EX)^2` proves (2). It includes `m=0`; the cases `k=0,n` are deterministic.

If `m/n<=C`, (2) immediately implies

\[
 \boxed{\Pr\left(\left|X/k-m/n\right|>\varepsilon
                  \mid\text{past}\right)
 \le\frac{C(1+C)}{k\varepsilon^2}.} \tag{3}
\]

The same estimate holds for the complementary cell with its own size. It remains valid when the chosen subset is adaptive, because its labels and size are already fixed conditional on the past.

## 3. Large-cell online freshness under actual incidence

Fix integers `S>=1`, `K>=0`, and `M>=0` before sending `r` to infinity. Work on the accepted safe base event `B_(r,S)`, and expose

\[
 E_r=(\text{full profile, all original rows }s\ge S,\text{ sampled offset }j).
\]

The exposed environment retains its **actual incidence marginal**. Conditional on each feasible environment, row `s<S` has its base-triangle coordinates fixed to zero and is otherwise a uniform composition of `ell_s` into

\[
 P_s=p_s-s-1
\]

free labelled coordinates. The accepted profile concentration gives, in actual incidence probability,

\[
 P_s\longrightarrow\infty,\qquad
 \frac{\ell_s}{P_s}\longrightarrow
 \rho_s=\frac1{(s+1)(s+3)},\qquad
 q_s=\frac{\rho_s}{1+\rho_s}=\frac1{(s+2)^2}.
 \tag{4}
\]

A query algorithm may depend on `r`, `E_r`, and its independent seed. It makes at most `K` nontrivial cell-sum queries and at most `M` new individual queries. Determined replies and repetitions may be omitted from its transcript. All queries obey Section 1.

Let `L_r` be a deterministic sequence tending to infinity. Stop the algorithm immediately before any new individual query whose current cell has fewer than `L_r` coordinates. This small-cell stop is a recorded outcome, not permission to replace a small-cell posterior by a geometric law. Sum queries may act on smaller cells, but such cells cannot later grow and hence cannot be used for a fresh large-cell query.

### Proposition 2: uniform large-cell approximation

For the preceding stopped algorithms, every new individual reply can be replaced online by a fresh geometric innovation of parameter `q_s`, with the total-variation distance between the full joint environment/transcript laws tending to zero. The bound is uniform over the legal algorithms with the displayed fixed `S,K,M` and `L_r`. Aggregate replies in the comparison process continue to use their exact current conditional composition kernels. They are not replaced by independent aggregates or given an unconditioned marginal.

If the probability of the small-cell stop is `o(1)` for a specified physical algorithm, the same conclusion holds for that algorithm without the extra stop. This probability is an additional hypothesis, not a conclusion for physical phase selection.

**Proof of density control.** Choose deterministic typical-profile tolerances `eta_r -> 0` such that outside a set of actual incidence probability `o(1)`, all initial densities differ from (4) by at most `eta_r`. All initial densities are then bounded by one common constant. There are at most `K+M` cell splits and at most twice as many newly created cells. Put `epsilon_r=L_r^(-1/4)`.

Track only cells of size at least `L_r`. Every ancestor of such a cell also has at least that size. On a history where its parent density stays in a fixed bounded interval, (3) shows that the probability a newly created large child's density differs from its parent's by more than `epsilon_r` is at most `C/(L_r epsilon_r^2)`. This estimate applies to singleton-query splits as well, by tracking their large remainder rather than the observed singleton. Small cells need no density estimate and cannot be ancestors of future large cells.

A stopped union bound over all splits proves that, except with probability

\[
 o(1)+O_{S,K,M}\bigl((L_r\varepsilon_r^2)^{-1}\bigr)=o(1),
 \tag{5}
\]

every large cell in row `s` has density within `eta_r+(K+M)epsilon_r` of `rho_s`. This argument uses conditional probabilities at current histories; it does not condition on future successful density control.

**Proof of individual approximation.** In a cell of size `n>=2`, total `m`, and at a specified unrevealed label, the exact marginal is

\[
 \Pr(Z=a\mid\text{past})=
 \frac{\binom{m-a+n-2}{n-2}}{\binom{m+n-1}{n-1}},
 \qquad 0\le a\le m. \tag{6}
\]

Uniformly when `n>=L_r` and the density lies in the shrinking interval just proved, (6) converges in total variation to `(1-q_s)q_s^a`. For each fixed `a`, factorial cancellation gives this limit. The limiting masses sum to one, so finite-set truncation upgrades pointwise convergence to total variation. Uniformity follows by the same argument along any proposed violating sequence of parameters.

Couple the two processes with identical environments and seeds. At aggregate queries, use the same exact conditional subtotal draw while the histories agree. At an individual query, maximally couple (6) to a fresh geometric innovation. Determined replies and repetitions agree automatically. The chance of any discrepancy is at most the probability in (5) plus `M` times the uniform one-step total-variation error, which tends to zero. If an independent geometric proposal exceeds its cell's remaining total, the comparison process may enter a designated inconsistent-state cemetery; this is already part of the coupling error, because the actual reply cannot do so. This proves the proposition. `square`

### Online is different from posterior

The proposition describes sequential innovations relative to information already exposed at the time of each reply. It does not say that earlier innovations remain geometric after conditioning on later aggregate observations. For example, a later query can reveal a sum containing an earlier value; conditioning on that sum gives a conditioned-composition posterior. The comparison process preserves this dependence through its exact aggregate kernels.

Nor does the proposition authorize a first-passage boundary as a neutral query endpoint. An index defined by `F(j-1)<u<=F(j)` already reveals inequalities about the unrevealed prefix process. Those inequalities must be included in its conditional law or reconstructed through legal observations.

## 4. Canonical endpoint words: an explicit finite-query clock algorithm

The following proposition uses only individual gap queries. It is separate from Proposition 2 and does not require its large-cell hypothesis.

Fix `J>=1` and `S>=1` before sending `r` to infinity. Start at physical time zero of the canonical original root. Ask for at most `J` successive C/T clocks, where every next clock starts at the endpoint of the preceding clock. Their types may be chosen from the exposed environment, an independent seed, and previously computed answers. An arbitrary externally supplied reached phase is not an input.

Fix a physical cutoff `G_0`, known from the exposed data, satisfying

\[
 \boxed{G_0+1<\min_{0\le s<S}p_s.} \tag{7}
\]

The extra strict margin excludes the possible circumference-minus-one alternative for a C clock as well as a full-lap T return. In the Gaussian application, any fixed multiple of the short cutoff is far below these fixed-depth circumferences on the safe profile event.

### Proposition 3: exact cutoff computation with tight fresh-query count

There is a legal individual-gap algorithm which determines whether the requested endpoint-started concatenation finishes by `G_0`, and gives its actual successive endpoints up to the first failure. For fixed `J,S`, the number of fresh original gap coordinates requested by this algorithm is tight under the actual safe base-incidence law as `r -> infinity`.

This conclusion does not say that the clock durations themselves are tight, that the requested concatenation finishes by `G_0` with high probability, or that unrestricted wrapped clocks have been evaluated.

**Algorithm.** At every row `s<S`, maintain a counter `n_s`, initially zero. Process nodes depth-first and left-to-right, so each row's nodes are encountered chronologically. For a depth-`s` node:

1. Query the original coordinate `Z_(s,-n_s)` modulo `p_s`, then increment `n_s`. Known base values and repeated labels are reused.
2. If its type is C and the answer is `z`, expand it as `C T^(2z)`. If its type is T, expand it as `C T^(2z+1)`.
3. Recursively process those children in their displayed chronological order.

At depth `S`, the complete original `D_S` and its finite labelled orbit are functions of the exposed rows. Evaluate each leaf C/T clock on that one orbit, starting at the physical endpoint of the preceding leaf. No new randomness is exposed for these leaf evaluations. Sum the leaf durations to obtain the candidate parent duration. If the running candidate exceeds `G_0`, report failure at the cutoff; otherwise continue to the next requested outer clock. There is no reset between clocks or levels.

**Why the indices are legal.** The source's exact one-level partition is

\[
 C\mapsto CT^{2z},\qquad T\mapsto CT^{2z+1}.
 \tag{8}
\]

Every completed parent node has exactly one child C. At the next level, C moves the selected original physical label to its predecessor, while T returns to the same selected label. Hence completion of each parent node decreases that next-level original selected label by exactly one. All levels initially have selected label zero. Therefore the queried original coordinates in row `s` are precisely `0,-1,-2,...` in chronological order. This argument works for concatenations of endpoint-started C and T nodes; it does not require evaluation of a whole-row selection cocycle. The counters and every next queried index are known from the existing transcript.

**Why the cutoff answer is physical.** If the actual concatenation finishes by `G_0`, its entire horizon satisfies (7). The forward no-wrap clock partition therefore expands it exactly as (8) through depth `S`, with the same queried labels and the same chronological leaf orbit. It must agree with the algorithm's candidate.

Conversely, if the candidate finishes by `G_0`, reverse the leaf grouping. Every group lies within the same horizon below the circumferences and their predecessor-return alternatives. Thus each use of (8) reverses to an actual parent clock. Repeating up the `S` levels reconstructs the requested actual outer concatenation with exactly the candidate endpoints. Consequently a candidate that exceeds `G_0` cannot conceal an actual concatenation finishing by `G_0`; otherwise the forward implication would make them equal. This is the same forward/reverse logic as in the accepted finite-layer fibre, now for a finite endpoint word.

**Why the fresh-query count is tight.** First run the same finite-depth genealogy against the original-coordinate geometric oracle, retaining the base zeros and reusing repeated values. In its infinite-label version, every node has finitely many children almost surely. A C node has `1+2z` children and a T node has `2+2z`; the mean fresh `z` at depth `s` is `q_s/(1-q_s)<=1/3`. A finite number of roots and a fixed number of generations therefore give a proper, almost surely finite tree. One may also bound its expected total node count by a constant depending only on `J,S`, using the conditional offspring bound `2+2/3` per node. Forced zeros and early cutoff stopping only decrease this bound.

For each fixed query cap `M`, all relevant circumferences tend to infinity. Before that cap the finite cyclic and infinite-label explorations agree, apart from a profile event of probability `o(1)`; no fresh index has wrapped around its row. Apply the accepted finite adaptive individual-query freshness theorem to this capped legal algorithm. It transfers the event of requesting another fresh value after the cap. Letting `r -> infinity` and then `M -> infinity`, the proper oracle-tree tail tends to zero. This proves tightness of the actual fresh-query count. Repetitions cannot create a hidden infinite traversal here: depth is fixed, every returned value is finite, and every outer word has at most `J` roots. `square`

The algorithm can evaluate a long candidate leaf clock using the entirely exposed depth-`S` orbit. Such computation costs no fresh upper-row queries; it is not a claim of a uniform running-time bound on orbit evaluation. The proposition concerns information/query complexity and cutoff correctness.

## 5. The unchanged arbitrary-phase physical gate

The canonical endpoint proposition does not automatically start a clock at an arbitrary interior offset, negative phase, or selected partner birth.

The literal shift source gives

\[
 \kappa_s(t)=\lambda_{s+1}(t)\pmod{p_s},\qquad
 Z^t_{s,j}=Z_{s,\kappa_s(t)+j}.
\]

Its bottom-up transport uses

\[
 C_s(j)=\sum_{k=1}^j(2Z_{s,k}+1+\epsilon_{s,k}),
\]

and signed visit counts `M_(s+1,j)(t)`, through

\[
 \lambda_s(t)=C_s(\lambda_{s+1}(t))
 +M_{s+1,\lambda_{s+1}(t)}(t)\pmod{n_s}.
\]

A predetermined phase `t` has one useful triangular property: the incoming-gap selector for row `s` depends only on strictly deeper rows. Conditioning on those **complete** deeper rows therefore causes no selection bias within row `s`. This observation does not give a bounded-query implementation of that complete conditioning or joint retrospective freshness after additional cocycle outputs are exposed.

To apply the segmented proposition to an actual shifted-phase exploration, the still-required interface is:

1. implement the needed prefix distances, original bit-transition counts, signed visit counts, and phase choices through a bounded number of legal cell-sum queries and a tight number of individual queries, without inserting a hidden trajectory or inverse-prefix oracle;
2. show that cells used for fresh individual replies have diverging size with high probability, or retain and account for their exact small-cell conditional laws instead;
3. retain every selection inequality and endpoint condition revealed by the procedure, rather than conditioning only on the final cell totals when that is not the full transcript.

Under neutral bounded splitting, Section 3 supplies the corresponding density control automatically. It does not establish the first or second physical requirement.

For illustration of why endpoint information matters, a uniform spatial point in a renewal arrangement selects intervals in proportion to their lengths. If a gap has `L=2Z+1+epsilon`, this would weight its geometric mass by `L`, not leave it geometric. Likewise, choosing a unit of composition mass makes a selected positive coordinate size-biased. These are cautionary examples, not an identification of the actual PBBS arrival distribution. The source's deeper-measurable selector is not automatically a length-biased selector; neither is an unimplemented arbitrary-phase oracle automatically neutral.

Accordingly, this note proves no new arrival process, no abundance of eligible original labels, no comparison of arbitrary shifted lifetimes with the sampled endpoint, and no occupied-support or coefficient-one conclusion. Those remain the physical gates identified in `PBBS_TOP_ZERO_ALL_SHORT_OVERLAP_REDUCTION_20260908.md`.
