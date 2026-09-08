# Architecture-free endpoint chains and unit-scale vacancy

**Date:** 2026-08-03  
**Status:** unconditional necessary theorem for every universal nonzero OR
word.  No carrier, fixed derivative, Johnson adjacency, residence, or
cyclicity is assumed.  This is a static consequence, not an upper
construction.

## 0. Statement

Put

\[
 r=\left\lceil {k\over2}\right\rceil,
 \qquad W={k\choose r},
 \qquad
 \mathcal L=\{S\subseteq[k]:1\le |S|<r\},
 \qquad \Lambda=|\mathcal L|.
\]

Let

\[
 A=(A_1,\ldots,A_n)
\]

be any universal nonzero OR word and write

\[
 n=W+e.
\]

### Theorem 0.1

The strict lower ideal `mathcal L` has a partition into `n` (possibly
empty) inclusion chains

\[
 \mathcal L=C_1\mathbin{\dot\cup}\cdots
             \mathbin{\dot\cup}C_n
\]

such that

\[
                         |C_j|\le e                 \tag{0.1}
\]

for every `j`.

This partition is literal: every member of `C_j` is represented by an
interval of `A` ending at physical position `j`.

Let `d=d(k)` be least with

\[
 dW+{d+1\choose2}\ge\Lambda,
\]

and suppose `n=B(k)+C=W+d+C`, where `C>=0` is fixed.  Then the total number
of vacant positions in the endpoint-chain tableau is

\[
 \begin{aligned}
 V_C
   &:=(d+C)(W+d+C)-\Lambda\\
   &=(dW-\Lambda)+CW+(d+C)^2,                       \tag{0.2}
 \end{aligned}
\]

and minimality of `d` gives

\[
 -{d+1\choose2}\le dW-\Lambda
      <W-{d\choose2}.                                \tag{0.3}
\]

Consequently

\[
                         0\le V_C<(C+1)W+O_C(k),     \tag{0.4}
\]

and hence

\[
 {V_C\over W+d+C}<C+1+o(1).                         \tag{0.5}
\]

Thus a `B(k)+C` word forces an architecture-free lower-half chain
partition whose maximum chain size is `d+C=Theta(sqrt(k))` and whose
average vacancy is bounded by the unit-scale constant `C+1+o(1)`.

The chains are not asserted to be anchored at distinct middle owners, and
they need not satisfy the sliding suffix cocycle.  Those are strictly
additional gates.

## 1. Ordered middle witnesses

Choose one witnessing interval for each rank-`r` target.  Two different
rank-`r` target values are incomparable, so their chosen intervals cannot
contain one another.  Order them by their left endpoints:

\[
 I_t=[a_t,b_t],\qquad1\le t\le W.
\]

Both endpoint sequences are strictly increasing.  Since they are
increasing `W`-tuples in `[n]=[W+e]`,

\[
 t\le a_t,b_t\le t+e.                                \tag{1.1}
\]

### Lemma 1.1 (every long interval contains a middle witness)

Every interval `J=[a,b]` of length at least `e+1` contains one of the
selected middle-witness intervals.

### Proof

The length assumption and `b<=W+e` imply `a<=W`.  Apply (1.1) with
`t=a`:

\[
 a\le a_a\le b_a\le a+e\le b.
\]

Thus `I_a subseteq J`. `square`

In particular, the OR of any interval of length at least `e+1` contains a
rank-`r` set and therefore has rank at least `r`.

## 2. Endpoint chain partition

For every target `S in mathcal L`, choose one interval

\[
 J_S=[\ell_S,j_S]
\]

whose OR is `S`.  Lemma 1.1 implies

\[
                         |J_S|\le e.                 \tag{2.1}
\]

For each physical right endpoint `j`, put

\[
 C_j=\{S\in\mathcal L:j_S=j\}.                       \tag{2.2}
\]

These families partition `mathcal L`.  At fixed `j`, interval unions are
nested as the left endpoint moves left:

\[
 A_j\subseteq A_{j-1}\cup A_j\subseteq\cdots.
\]

Hence the distinct target values in `C_j` form an inclusion chain.  By
(2.1), only the `e` starts

\[
                         j-e+1,\ldots,j
\]

can occur, after clipping at the left boundary.  Therefore `|C_j|<=e`.
This proves Theorem 0.1.

## 3. Vacancy calculation

Equation (0.2) is direct.  The defining inequality for `d` gives the lower
bound in (0.3).  If `d>=1`, minimality also gives

\[
 (d-1)W+{d\choose2}<\Lambda,
\]

which rearranges to the strict upper bound in (0.3); the case `d=0` is
immediate.  Since `d=Theta(sqrt(k))`, substituting (0.3) into (0.2) proves
(0.4)--(0.5).

## 4. Exact scope

This theorem is a necessary static shadow of any near-optimal word.  It
proves none of the following.

1. The `W+d+C` endpoint chains are not reduced to `W` owner-anchored
   chains.
2. Their targets are not assigned to a complete central owner row.
3. Separate endpoint chains are not shown to satisfy one sliding suffix-OR
   recurrence.
4. No residence, upper-shadow, topology, common-cap, or regeneration
   statement is obtained.

Accordingly, the theorem does not prove `nu(k)<=B(k)+O(1)`.  It shows that
such a bound would already contain a unit-scale bounded-chain theorem in
every architecture, before the stronger owner and chronology constraints
are imposed.
