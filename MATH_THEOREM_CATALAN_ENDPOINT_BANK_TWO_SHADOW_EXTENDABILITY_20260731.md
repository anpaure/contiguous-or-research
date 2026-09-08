# Catalan endpoint banks are universally two-shadow extendable

Date: 2026-07-31  
Status: complete theorem; the coupled common-bank/forest condition remains open

## 0. Verdict

Let

\[
        X_n=\binom{[2n]}n,\qquad K_n=\operatorname{Cat}_n
             ={1\over n+1}\binom{2n}n .
\]

For every `n>=3`, **every** family of at most `K_n` middle sets has an
injective choice of a two-step lower shadow, and also an injective choice of
a two-step upper shadow.  Equivalently, it is independent in both
transversal matroids

\[
 X_n\longleftrightarrow\binom{[2n]}{n-2},\qquad
 X_n\longleftrightarrow\binom{[2n]}{n+2}.
\]

The missing-tail and missing-head banks of any Catalan linear forest have
exactly `K_n` members.  Consequently each endpoint bank can always be
extended to either required diagonal saturating matching in the
two-coordinate recursion.  Thus **neither one-sided endpoint bank is a Hall
obstruction**.

This does not choose the same deleted child-atom set on both shores and does
not prove that the two diagonal supports and their attachments form a linear
forest.  The unresolved condition is precisely the synchronized common-bank
plus topology row, not one-sided shadow capacity.

## 1. Universal two-step shadow theorem

For a family `A` of `n`-sets, write

\[
 \partial_2 A=\{Y\in\tbinom{[2n]}{n-2}:Y\subseteq A
                    \text{ for some }A\in\mathcal A\}.
\]

### Theorem 1.1

For `n>=3` and every `A subset X_n` with `|A|<=K_n`, there is an injection

\[
       f_-:\mathcal A\longrightarrow\binom{[2n]}{n-2},
       \qquad f_-(A)\subset A.                         \tag{1.1}
\]

There is dually an injection

\[
       f_+:\mathcal A\longrightarrow\binom{[2n]}{n+2},
       \qquad A\subset f_+(A).                         \tag{1.2}
\]

### Proof

Assume first that `n>=4`.  The elementary comparison

\[
 {K_n\over\binom{2n-2}n}
 = {2(2n-1)\over(n+1)(n-1)}\le1                       \tag{1.3}
\]

is equivalent to `n^2-4n+1>=0`, which holds for `n>=4`.

Take any nonempty `B subset A` and write

\[
             |\mathcal B|=\binom xn
\]

for the unique real `x>=n`.  By (1.3), `x<=2n-2`.  The Lovasz form of the
Kruskal--Katona theorem gives

\[
        |\partial_2\mathcal B|\ge\binom{x}{n-2}.
\]

Moreover

\[
 {\binom{x}{n-2}\over\binom xn}
 ={n(n-1)\over(x-n+1)(x-n+2)}\ge1,                    \tag{1.4}
\]

because `x<=2n-2`.  Hence

\[
                 |\partial_2\mathcal B|\ge|\mathcal B|
\]

for every `B subset A`.  Hall's theorem proves (1.1).

For `n=3`, the two-step lower shadow is simply the union of a family of
triples.  If `t<=5` distinct triples had union of order below `t`, then they
would all lie in a set of order at most `t-1`, which contains fewer than
`t` triples for `1<=t<=5`.  Thus Hall again applies.  This covers
`K_3=5`.

Finally complementing every set turns (1.1) into (1.2).  `square`

### Corollary 1.2 (basis extension)

Let `T_-` and `T_+` be the two transversal matroids on `X_n` defined by
matchability into ranks `n-2` and `n+2`.  Both have rank

\[
             P_n=\binom{2n}{n-2}.
\]

Every family of at most `K_n` middle sets is independent in both matroids,
and therefore extends to a basis of each.

### Proof

Theorem 1.1 is exactly independence.  A maximal independent set in a
matroid extends to a basis; the full rank is `P_n` because a symmetric-chain
decomposition supplies a saturating matching between ranks `n-2` and `n`.
The upper statement is its complement dual.  `square`

## 2. Consequence for a Catalan linear forest

Let `F` be a Catalan linear matching at parameter `n`, oriented as a path
forest on `X_n`.  It has

\[
 N_n=\binom{2n}{n-1}
\]

edges on `M_n=binom(2n,n)` vertices and therefore

\[
 M_n-N_n=K_n                                                   \tag{2.1}
\]

components.  Let `E^-` be the vertices unused as tails and `E^+` the
vertices unused as heads.  Each path contributes one of each, so

\[
                     |E^-|=|E^+|=K_n.                         \tag{2.2}
\]

### Corollary 2.1 (no one-sided endpoint obstruction)

Each of `E^-` and `E^+` can be included in a rank-`P_n` basis of either
two-step transversal matroid.  In particular:

* `E^-` can be completed to a middle bank matched bijectively to all
  rank-`n+2` resources;
* `E^+` can be completed to a middle bank matched bijectively from all
  rank-`n-2` resources;
* the complements of those bases have the exact Catalan-collar order
  `M_n-P_n` and lie in the used tail/head banks respectively.

### Proof

Apply Corollary 1.2 and use (2.2).  Since `E^-` is precisely the complement
of the used-tail image, the complement of any basis containing `E^-` lies
inside the used-tail image; similarly for heads.  The cardinality statement
is immediate.  `square`

## 3. Exact remaining synchronization gate

Corollary 2.1 produces, in general, two different Catalan-size deletion
banks `Q^-` and `Q^+`.  The restricted five-sector recursion keeps the
central child atoms literally, and therefore asks for **one** atom set `Q`
whose tail image is the first deletion bank and whose head image is the
second.  Equivalently, `Q` must be a common basis of the two dual contracted
transversal matroids induced by the oriented child forest.

After that common basis is selected, the two diagonal matchings and all
cross attachments must still have a linear-forest physical support.
Therefore the exact unresolved statement is

\[
 \boxed{\text{common deletion basis}\quad+\quad
        \text{forest-compatible representatives}.}
\]

The theorem above removes every weaker explanation based on an isolated
endpoint bank having too small a two-step shadow.

## 4. Audit

The standard-library replay

```text
python3 scratch/audit_catalan_endpoint_bank_two_shadow_20260731.py
```

checks (1.3)--(1.4) exactly for `4<=n<=100`, exhausts every family of at
most five triples for `n=3`, and verifies Hall by explicit bipartite
matching.  It is an audit of the finite base and the exact arithmetic; the
all-`n` proof is Theorem 1.1.

