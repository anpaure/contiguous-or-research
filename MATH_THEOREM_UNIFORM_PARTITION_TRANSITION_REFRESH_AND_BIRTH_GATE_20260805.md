# Uniform transition refinement exactly refreshes persistent colours

**Date:** 2026-08-05  
**Method:** pure mathematics; no search or solver  
**Status:** unconditional finite theorem.  Sparse deterministic transition
rules do not obstruct uniform colour refresh, provided the complete current
partition is exchangeable and the transition-count matrix is fixed.  The
only remaining asymmetry is the introduction of physically distinguished
newborn objects (the universal-dummy shore in the Boolean interface).

## 1. Uniform transition theorem

Let `Omega` be a finite set of size `m`.  Fix nonnegative integers

\[
 n_{ij}\qquad(1\le i\le a,\ 1\le j\le b)
\tag{1.1}
\]

with row sums `r_i` and column sums `c_j`:

\[
 \sum_j n_{ij}=r_i,
 \qquad
 \sum_i n_{ij}=c_j,
 \qquad
 \sum_i r_i=\sum_jc_j=m.
\tag{1.2}
\]

Zeros in the matrix are allowed and may encode forbidden state
transitions.

Choose a labelled partition

\[
 \Omega=A_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}A_a,
 \qquad |A_i|=r_i,
\tag{1.3}
\]

uniformly.  Conditional on this partition, independently for each `i`,
choose a uniform labelled refinement

\[
 A_i=A_{i1}\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}A_{ib},
 \qquad |A_{ij}|=n_{ij}.
\tag{1.4}
\]

Finally forget the old labels and put

\[
 B_j=\bigcup_iA_{ij}.
\tag{1.5}
\]

### Theorem 1.1 (exact transition refresh)

The output

\[
 \Omega=B_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}B_b,
 \qquad |B_j|=c_j,
\tag{1.6}
\]

is a uniform labelled partition with these column sizes.

In particular, neither the zero pattern of `(n_{ij})` nor the persistence
of the old state labels leaves any bias after the old labels are forgotten.

#### Proof

There is an equivalent one-stage experiment: choose a labelled array of
sets `(A_{ij})` partitioning `Omega`, with cell sizes `n_{ij}`, uniformly
among all such arrays.  Indeed, every first-stage partition `(A_i)` has

\[
 \prod_i {r_i!\over\prod_jn_{ij}!}
\tag{1.7}
\]

refinements, a number independent of the particular sets `A_i`; and every
refinement has the same conditional probability.

Now fix an output partition `(B_j)` of column sizes `(c_j)`.  The number of
arrays `(A_{ij})` with these column unions is

\[
 \prod_j {c_j!\over\prod_in_{ij}!},
\tag{1.8}
\]

again independent of the particular sets `B_j`.  Therefore every output
partition has the same probability.  This is exactly uniformity. `square`

## 2. Equivariance and transport by a random interface

### Corollary 2.1 (independence survives deterministic relabelling)

Let `phi:Omega->Omega'` be a bijection independent of the experiment in
Theorem 1.1.  Conditional on `phi`, the transported partition

\[
 \bigl(\phi(B_1),\ldots,\phi(B_b)\bigr)
\tag{2.1}
\]

is uniform on `Omega'` with sizes `(c_j)`.  In particular it is independent
of `phi`.

#### Proof

For each fixed bijection, transport is a bijection between the two finite
sets of labelled partitions.  Thus the conditional law is the same uniform
law for every value of `phi`. `square`

Apply this to the old part of a Boolean-interface perfect matching.  If the
old left shore is already uniformly partitioned into persistent states,
then any fixed state-transition count matrix may be sampled before the
matching; after forgetting the old states, the next persistent-state
partition of the old image set is uniform conditional on the whole
matching.  The random-refreshed-colour Chernoff theorem therefore applies
to every such transported class on the old image.

This is stronger than assuming a complete transition graph.  Countdown,
age, or residence automata may have an arbitrary sparse transition graph;
only the prescribed integer transition counts must be feasible.

## 3. The exact newborn asymmetry

The preceding argument is closed on a fixed population.  A square Boolean
interface instead has

* an old left shore `L` of size `m`;
* `N-m` universal dummies;
* a right shore `R` of size `N`;
* an old image `I subset R` and newborn complement `D=R\I`.

Conditional on the perfect matching, Theorem 1.1 and Corollary 2.1 give a
uniform transitioned partition of `I`.  They do **not** make the union with
a prescribed newborn partition of `D` uniform on all of `R`.  The set `D`
is random and Strong Rayleigh, but its members have a physically distinct
history: they did not exist on the preceding shore.

This boundary is exact.  If all newborns must receive one fixed state
`j_0`, then the next class `B_(j_0)` contains `D` deterministically once
the matching is fixed.  Unless `D` is empty or the state partition is
degenerate, the resulting full partition cannot be conditionally uniform
on `R`.

Thus persistent-state sparsity is not the refresh obstruction.  The only
new obstruction exposed by one Pascal interface is the interaction between
the random newborn set and the forced newborn state.

## 4. A sufficient newborn randomization criterion

Suppose, in addition, that conditional on the matching the elements of
`D` may be assigned to the new states by a uniform fixed-size partition
independent of the transitioned partition of `I`.  Fix numbers `d_j` and
`c_j` with

\[
 \sum_jd_j=|D|,
 \qquad
 \sum_jc_j=|I|.
\tag{4.1}
\]

This does not yet make the unions of the two partitions uniform on `R`:
they retain the deterministic intersection sizes `|B_j cap D|=d_j`.
However, every owner statistic splits into an old-image and a newborn
term.  The old-image term has the two-stage hypergeometric/Strong-Rayleigh
concentration already proved, and the newborn term has the same theorem
with `D` in place of `I`.  Hence every fixed finite family of linear owner
statistics has Chernoff concentration about its exact mean.

Consequently, an induction needs full exchangeability only if the next
matching theorem is invoked through a theorem requiring a globally uniform
colour partition.  If the next theorem is formulated for a bounded union
of independently refreshed Strong-Rayleigh cohorts, newborns may remain a
separate cohort.

This identifies the next proof target:

> **Cohort-stable coloured Boolean theorem.**  Prove the required
> one-interface owner concentration and exact rounding when each colour is
> a union of a bounded number of exchangeable Strong-Rayleigh cohorts, with
> geometric contraction of all inherited cohorts and insertion of one new
> newborn cohort.

If the number of cohorts can be merged or their total error can be
contracted without depending on their age, the colour-refresh obstruction
does not accumulate.

## 5. Consequence for the current programme

The multi-step refresh problem has therefore split into two parts:

1. **persistent histories:** solved exactly by Theorem 1.1 for every fixed
   feasible transition matrix, including sparse residence automata;
2. **births:** still open, but now isolated as a cohort-merging or
   cohort-stable concentration/rounding problem.

No claim is made here that physical OR-word roles may be arbitrarily
reassigned, or that the exact integral terminal compiler follows from
concentration alone.

## 6. Dependencies

1. `MATH_THEOREM_RANDOM_REFRESHED_COLOUR_BOOLEAN_MATCHING_CHERNOFF_20260805.md`;
2. `MATH_THEOREM_BOOLEAN_MATCHING_IMAGE_STRONG_RAYLEIGH_AND_COLORED_ASSIGNMENT_GATE_20260805.md`;
3. `MATH_THEOREM_COLORED_BOOLEAN_ONE_STEP_UNIFORM_FLOW_CONTRACTION_AND_EXACT_ROUNDING_GAP_20260805.md`.
