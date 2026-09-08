# One-central rectangular greedy: annealed abundance and the quenched gate

**Status (2026-08-21).**  The statements below are proved.  They calibrate
the proposed one-central-resource greedy based on the rich rectangular
macro.  Annealed counting has enough entropy to reach a polynomially sparse
central residual, and length `Theta(n log n)` reaches the formal `Theta(1/n)`
scale.  This does **not** give a sequential selector: explicit dense
residuals contain no legal block at all.  The missing hypothesis is a
quenched tail-path expansion property, together with conditional (not merely
annealed) codegree control for the postponed graphic ranks.

## 1. A fixed common-transformation microblock family

Let

\[
 n=2m+1,
 \qquad H=\lceil\sqrt{n\log n}\rceil,
 \qquad W={n\choose m},
 \qquad K=\{m-H,\ldots,m+1+H\},
 \qquad f=m+H+2,
 \qquad d=n-f+1=m-H.                                 \tag{1.0}
\]

Fix a length `ell` common-transformation family `G_ell` from Theorem 8.1 of
`MATH_THEOREM_GLOBAL_PARITY_CYCLE_RESERVOIR_AND_FIFO_RECOMPOSITION_BARRIER_20260821.md`,
and use its `K`-simple, centrally chordless version.  Thus

\[
 |\mathcal G_\ell|
 \ge {(1-o(1))d^\ell\over n!}.                        \tag{1.1}
\]

For a fixed seed `pi` and `w in G_ell`, let

\[
 a=\ell-1,
 \qquad
 D_\pi^\circ(w)=\{C_m(\pi_t):1\le t\le a\}          \tag{1.2}
\]

be its retained central deck.  It is an `a`-set.  The omitted state
`pi_ell` is the branch-independent final checkpoint forced by the common
endpoint transformation.  It must be discarded: when common-endpoint
blocks are tiled, retaining this checkpoint would repeat an endpoint target
independently of the chosen branch and would preclude a full-deck matching.
For a residual family
`R subseteq binom([n],m)`, define the quenched feasible count

\[
 Z_\pi(\mathcal R)
 =|\{w\in\mathcal G_\ell:D_\pi^\circ(w)\subseteq\mathcal R\}|. \tag{1.3}
\]

A sequential central matching requires (1.3) to be positive for the
residuals it actually creates.  Averaging the seed or the residual does not
prove this.

## 2. Exact annealed count and its entropy threshold

### Proposition 2.1 (uniform-residual abundance)

Let `R` be uniformly random among the `r`-subsets of the central layer,
independently of the fixed seed.  Then

\[
 \mathbb E_{\mathcal R}Z_\pi(\mathcal R)
 =|\mathcal G_\ell|{{r\choose a}\over{W\choose a}}. \tag{2.1}
\]

If `rho=r/W`, `a^2=o(r)`, and (1.1) holds, then

\[
 \log\mathbb E Z_\pi(\mathcal R)
 \ge \ell\log d+a\log\rho-\log(n!)+o(1).            \tag{2.2}
\]

In particular, for fixed `C>1`, `ell=ceil(Cn)`, and
`rho=c_0 n^(-gamma)` with fixed `c_0>0`,

\[
 \log\mathbb E Z_\pi(\mathcal R)
 \ge
 [C(1-\gamma)-1]n\log n
 +Cn\log(c_0/2)+n-o(n\log n).                        \tag{2.3}
\]

Thus the expectation is superpolynomially large whenever
`gamma<1-1/C`.  If instead `ell=n log n+O(n)` and `rho=c_0/n`, then

\[
 \log\mathbb E Z_\pi(\mathcal R)
 \ge
 [\log(c_0/2)-1]n\log n+o(n\log n),                  \tag{2.4}
\]

which is exponentially positive on the `n log n` scale for `c_0>2e`.

#### Proof

Every retained deck in (1.2) has exactly `a` distinct targets.  A uniform
`r`-subset contains any fixed retained deck with probability
`binom(r,a)/binom(W,a)`, proving (2.1) by linearity.  Since
`a^2=o(r)`, the logarithm of this ratio is

\[
 a\log\rho+O(a^2/r)=a\log\rho+o(1).
\]

Combine this with (1.1), `log d=log n-log2-o(1)`, and
`log(n!)=n log n-n+o(n)`.  Substitution gives (2.2)--(2.4).  \(\square\)

The loss `log(n!)` is the entropy price of forcing one common endpoint
transformation.  With fixed `C`, it prevents the annealed calculation from
reaching density `Theta(1/n)`; taking `C` of order `log n` amortizes that
price.

There is a useful central-codegree refinement at this longer scale.  It
removes the all-distance caveat for the one rank which is to be matched.

### Proposition 2.2 (all-distance central codegree after antipode removal)

Suppose `ell` is polynomial in `n`.  The common-transformation family may
be chosen, without changing (1.1) by more than its `1-o(1)` factor, so that
no retained rank-`m` deck contains two disjoint targets.  Under a uniform
seed and any seed-independent branch law on this strengthened family,
every pair of distinct central targets satisfies

\[
 {\Pr(S,T\text{ both occur})
  \over \Pr(S\text{ occurs})}
 =O\!\left({a\over n^3}+{1\over n^2}\right).          \tag{2.5}
\]

In particular this is `O(n^(-2))` for `ell=Theta(n)` and
`O((log n)/n^2)` for `ell=Theta(n log n)`.

#### Proof

Two length-`m` occurrence windows at a temporal gap below `m` share an
occurrence and cannot be disjoint.  At a gap at least `m`, condition on the
earlier history.  There are exactly `m+1` rank-`m` targets disjoint from its
current target, and the history-free endpoint bound for each is at most

\[
 B_d={d!\over d^d},
\]

because `m>=d`.  A union bound over retained time pairs shows that the
fraction of generator words having a disjoint retained-deck pair is at most

\[
 {a\choose2}(m+1)B_d=e^{-n/2+o(n)}.                   \tag{2.6}
\]

Exclude these words together with the simplicity and chord failures before
the position-permutation pigeonhole argument.  The surviving largest fiber
still satisfies (1.1).

Let `j` be the Johnson distance of `S,T`.  For `j=1`, chordlessness gives
the exact normalized value
`2(a-1)/(a m(m+1))=(8+o(1))/n^2`.  For
`2<=j<=m-1`, relabeling transitivity and the trivial bound of
`binom(a,2)` distance-`j` pairs in one retained deck give normalized joint
occurrence at most

\[
 {2{a\choose2}
  \over a {m\choose j}{m+1\choose j}}
 =O(a/n^3),                                           \tag{2.7}
\]

because the smallest denominator in this range is
`{m\choose m-1}{m+1\choose m-1}=Theta(n^3)`.  The case
`j=m` is absent by construction.  This proves (2.5).  \(\square\)

Proposition 2.2 is still annealed over the seed and branch law.  It gives a
genuine favorable pair scale for the one-central matching hypergraph when
seeds are palette variables, but it does not survive arbitrary conditioning
on a reached residual.

## 3. Dense residuals can still contain no legal block

Annealed abundance cannot be turned into a cardinality-only extension
lemma.

### Theorem 3.1 (dictator-star residual obstruction)

Fix a letter `x` and put

\[
 \mathcal R_x=\{S\in{[n]\choose m}:x\in S\}.          \tag{3.1}
\]

Then

\[
 |\mathcal R_x|={m\over n}W=(1/2+o(1))W,              \tag{3.2}
\]

but no legal tail-MTF trajectory can have more than `m` consecutive
rank-`m` observations all lying in `R_x`.  Consequently, whenever `a>m`,

\[
 Z_\pi(\mathcal R_x)=0                                \tag{3.3}
\]

for every seed, regardless of the size or entropy of the
common-transformation family.

#### Proof

At rank `m<f`, `C_m(pi_t)` is the set of letters in the last `m` access
occurrences.  One occurrence of `x` therefore makes exactly the next `m`
rank-`m` windows contain `x`.  Consecutive occurrences of `x` are separated
by at least `f>m`, so these length-`m` coverage intervals are disjoint and
have a nonempty gap between them.  A consecutive run of windows containing
`x` has length at most `m`.  This proves (3.3), and (3.2) is elementary.
\(\square\)

There is also a sharp obstruction at the formal `1/n` scale which is not a
dictator star.  Identify the letters with `Z/nZ` and, for `c in Z/nZ`, put

\[
 \mathcal I_c=
 \left\{S\in{[n]\choose m}:\sum_{x\in S}x=c\pmod n\right\}. \tag{3.4}
\]

### Proposition 3.2 (balanced independent residual at density `1/n`)

Every `I_c` has size exactly `W/n`, and it is an independent set of the
Johnson graph `J(n,m)`.  Hence it contains no legal rank-`m` trace of length
two.

#### Proof

Translation by `u` sends the sum class `c` to `c+mu`.  Since
`gcd(m,n)=gcd(m,2m+1)=1`, translations act transitively on the `n` sum
classes, so they have equal size `W/n`.  Johnson-adjacent sets replace one
residue `y` by a distinct residue `x`; their sums differ by the nonzero
residue `x-y`.  They cannot lie in one class.  \(\square\)

Theorem 3.1 shows that even density, exact relabeling-averaged marginals,
and enormous branch entropy do not give a quenched extension.  Proposition
3.2 shows that stopping with `Theta(W/n)` uncovered central targets is in
general the correct cardinality scale; fortunately that leave is already
`o(W)`.

## 4. What a rigorous sequential theorem would have to say

Let `R_i` be the actual unused central targets before microblock `i`.  A
positive rectangular greedy needs a **reachable-residual** assertion such
as

\[
 Z_{\pi_i}(\mathcal R_i)>0                             \tag{4.1}
\]

until `|R_i|=o(W)`.  More quantitatively, a semi-random proof needs a lower
bound on (1.3) stable under the conditioning used to keep earlier central
decks disjoint.  Theorems 8.1 and 8.5 provide only the annealed statement
obtained after a uniform seed relabeling; (3.3) proves that no bound of the
form (4.1) follows from `|R_i|` alone.

The same distinction is essential for the postponed graphic ranks.  An
unconditioned law may satisfy

\[
 \Pr(S,T\in U_{i,q})=O\!\left({a\over M_qn^2}\right), \tag{4.2}
\]

but after conditioning on `D_(pi_i)^circ(w) subseteq R_i` its pair probabilities
can increase by the reciprocal of an exponentially small feasibility
probability.  Annealed codegrees therefore do not imply the conditional
bound (3.9) in
`MATH_CUSTOM_PARITY_GRAPHIC_NIBBLE_INVARIANT_20260821.md`.

Combining the proved reductions, the following three quenched invariants
would be sufficient:

1. the reached central residuals obey (4.1), and the selected branch keeps
   the rank-`m` decks disjoint;
2. conditional postponed-rank pair probabilities retain the scale (4.2);
3. every postponed-rank forest has component square mass
   `sum_C |C|^2=O(M_q a)`.

For linear microblocks, items 2--3 give total graphic cycle charge
`O(W|K|/n)=o(W)` by Corollary 3.2 of the component-charge note, while item 1
gives the single central matching.  Proving these properties for the
**reachable** residual process, or finding a global augmentation which
restores them, is the exact surviving positive attack.  The rectangular
macro removes endpoint and entropy obstructions, but it does not prove any
of the three quenched assertions.
