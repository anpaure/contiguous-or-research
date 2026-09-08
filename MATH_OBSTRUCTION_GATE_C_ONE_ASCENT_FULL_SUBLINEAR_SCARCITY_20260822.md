# Gate C: one-ascent scarcity throughout the full sublinear-defect regime

**Status (2026-08-22).**  Every assertion below is proved.  The earlier
run bound `2^{b+O(1)} b^{O(K)}` was too crude near
`K=b/log b`: it discarded the factorial in the choice of odd internal
runs.  Exact coefficient extraction restores that factorial.

If `K=o(b)`, the number of one-ascent parity words with at most `K` odd
internal runs is
\[
                         2^{b+o(b)},                       \tag{0.1}
\]
not `4^{b-o(b)}`.  At the apparent threshold `K=c b/log b`, its natural
logarithm is exactly
\[
 b\log2+{cb\over\log b}
 \left(\log\log b-\log c+1-\tfrac12\log2\right)
 +O\left({b\over\log^2 b}+\log b\right).                 \tag{0.2}
\]
This is still `b log 2+o(b)`, exponentially below the
`2b log 2-O(log b)` required by a coefficient-one packing.

Consequently the entire one-ascent Hamilton family is insufficient for
every coefficient-one-compatible common loss `L=o(q)`, not merely for
`L=o(b^2/log b)`.  This applies to the *actual* intersection with the
Catalan-switched factor: the parity/odd-run test is a necessary condition,
so exact Dyck membership can only reduce the candidate set.

Throughout,
\[
 n=2b,\qquad m=n-1=2b-1,qquad
 h={b-1\over2},\qquad q=b(b-1),\qquad
 N=\binom{2b}{b-1}.                                      \tag{0.3}
\]
All logarithms in asymptotic formulas are natural.

## 1. Exact run generating function

For a binary word of length `m`, call its first and last runs endpoint
runs and all others internal runs.  Let `omega` be the number of
odd-length internal runs, and let `A_{m,j}` be the number of words with
`omega=j`.

Use the ordinary generating functions
\[
 E(z)={z\over1-z},\qquad
 V(z)={z^2\over1-z^2},\qquad
 O(z)={z\over1-z^2}                                      \tag{1.1}
\]
for a positive unrestricted endpoint run, a positive even internal run,
and a positive odd internal run.

### Lemma 1.1 (exact coefficient formula)

For every `j>=0`,
\[
 \sum_{m\ge1}A_{m,j}z^m
 =2E(z)\mathbf1_{j=0}
  +2E(z)^2{O(z)^j\over(1-V(z))^{j+1}}.                   \tag{1.2}
\]
The nonconstant summand simplifies to
\[
 G_j(z):={2z^{j+2}(1+z)\over1-z}(1-2z^2)^{-j-1}.          \tag{1.3}
\]

#### Proof

There are two constant words, represented by `2E(z)`, and they have no
internal run.  A nonconstant word is determined by its first bit and its
positive run lengths.  If it has `ell` internal runs, choose which `j`
are odd; summing over `ell>=j` gives
\[
 \sum_{\ell\ge j}\binom\ell j V^{\ell-j}O^j
 ={O^j\over(1-V)^{j+1}}.                                 \tag{1.4}
\]
Multiplication by the two endpoint-run factors and the two first-bit
choices proves (1.2).  Since
`1-V=(1-2z^2)/(1-z^2)`, direct cancellation gives (1.3).
\(\square\)

Put
\[
 R=R(m,j)=\left\lfloor{m-j-2\over2}\right\rfloor.        \tag{1.5}
\]

### Lemma 1.2 (sharp coefficient sandwich)

Whenever `R>=0`,
\[
 2^{R+1}\binom{R+j}{j}
 \le [z^m]G_j(z)
 \le 2^{R+3}\binom{R+j}{j}.                              \tag{1.6}
\]

#### Proof

Write
\[
 (1-2z^2)^{-j-1}
 =\sum_{r\ge0}\binom{r+j}{j}2^rz^{2r}.                   \tag{1.7}
\]
The coefficient of `z^s` in `(1+z)/(1-z)` is one for `s=0` and two for
`s>=1`.  Thus `[z^m]G_j` lies between twice the last term
`2^R binom(R+j,j)` and four times the sum of all terms through `R`.
Successive terms grow by a factor
\[
 2{r+j+1\over r+1}\ge2,
\]
so their sum is at most twice the last term.  This proves (1.6).
\(\square\)

The missing factorial is now visible: the coefficient is, within a
constant factor,
\[
                         2^R\binom{R+j}{j},               \tag{1.8}
\]
rather than `2^R m^j`.

## 2. Uniform sublinear asymptotics

Let
\[
                         A_m(\le K)=\sum_{0\le j\le K}A_{m,j}. \tag{2.1}
\]

### Theorem 2.1 (full sublinear scarcity)

For every integer sequence `K=K_m=o(m)`, with `K>=0`,
\[
 \boxed{\log A_m(\le K)={m\over2}\log2+o(m).}             \tag{2.2}
\]
More precisely, if `K->infinity` and `K=o(m)`, then
\[
 \log A_m(\le K)
 ={m\over2}\log2
 +K\left(\log{m\over2K}+1-\tfrac12\log2\right)
 +O\left({K^2\over m}+\log m\right).                    \tag{2.3}
\]

#### Proof

For the coarse uniform statement, Lemma 1.2 and
`binom(x,j)<=(ex/j)^j` give, uniformly for `j<=K`,
\[
 \log A_{m,j}
 \le {m\over2}\log2
 +K\log{e(m+K)\over K}+O(1)                              \tag{2.4}
\]
(with `j=0` handled directly).  If `epsilon=K/m->0`, the second term is
at most
\[
 m\epsilon\bigl(\log(1/\epsilon)+O(1)\bigr)=o(m).        \tag{2.5}
\]
Summing at most `m` terms costs only `O(log m)`.  Conversely the `j=0`
term in Lemma 1.2 is `2^{m/2-O(1)}`.  This proves (2.2).

For (2.3), set `T_j=2^{R(m,j)}binom(R(m,j)+j,j)`.  When
`j<=K=o(m)`, increasing `j` either leaves `R` fixed, multiplying `T_j`
by `(R+j+1)/(j+1)`, or decreases `R` by one, multiplying by
`R/[2(j+1)]`.  Both factors exceed one for all sufficiently large `m`.
Thus Lemma 1.2 makes the sum in (2.1) equal to `T_K` up to a factor
polynomial in `m`.

Now
\[
 R(m,K)={m-K\over2}+O(1),\qquad
 R(m,K)+K={m+K\over2}+O(1).                              \tag{2.6}
\]
Stirling's formula, uniformly for `K=o(m)`, gives
\[
 \log\binom{R+K}{K}
 =K\log{m\over2K}+K+O(K^2/m+\log m).                    \tag{2.7}
\]
Combining (2.6), (2.7), and `R log2` proves (2.3).
\(\square\)

### Corollary 2.2 (the `b/log b` rate)

Let `m=2b-1` and
\[
                         K={cb\over\log b}+O(1),\qquad c>0. \tag{2.8}
\]
Then
\[
 \log A_m(\le K)
 =b\log2+{cb\over\log b}
 \left(\log\log b-\log c+1-\tfrac12\log2\right)
 +O\left({b\over\log^2b}+\log b\right).                \tag{2.9}
\]

#### Proof

Substitute (2.8) into (2.3); replacing `m/2` by `b` changes only `O(1)`.
\(\square\)

In particular, the entropy correction in (2.9) is `o(b)`.  The crude
factor `b^{O(K)}` suggested an order-`b` correction because it omitted
the `K!` encoded by the binomial coefficient in (1.8).

## 3. Actual one-ascent factor intersections

For `A subseteq [1,2b-1]` containing `2b-1`, define
\[
 H_A=(0,A^\downarrow,(A^c)^\downarrow).                  \tag{3.1}
\]
Its membership word `x_1...x_m` ends in one.  Let `omega(A)` count the
odd internal runs of this word.

Every odd internal zero-run is flanked by consecutive members of
`A^downarrow` whose difference is even, hence gives a same-parity edge of
`H_A`.  Every odd internal one-run gives the analogous edge inside
`(A^c)^downarrow`.  Distinct runs give distinct edges, so
\[
                         e_same(H_A)>=omega(A).           \tag{3.2}
\]

In the Catalan-switched factor every flag arc crosses coordinate parity,
while every Hamilton edge occurs in exactly `h` internal flags of one
coherent phase.  Therefore its actual intersection satisfies
\[
 M(H_A,delta)<=q-h e_same(H_A)<=q-h omega(A).             \tag{3.3}
\]

### Theorem 3.1 (actual-overlap scarcity for every `L=o(q)`)

For every `L=L_b=o(q)`, the number of phase-labelled one-ascent supports
with
\[
                         M(H_A,delta)>=q-L                \tag{3.4}
\]
is at most
\[
                         2^{b+o(b)}.                      \tag{3.5}
\]
The required number of supports for fixed-fraction central coverage is
\[
 {N\over q}=\Theta\left({4^b\over b^{5/2}}\right),        \tag{3.6}
\]
so the ratio of available candidates to the requirement is
`2^{-b+o(b)}`.

#### Proof

By (3.3), (3.4) forces
`omega(A)<=K=floor(L/h)=o(b)`.  Complementing a binary word preserves all
run lengths and swaps its final bit, so exactly half the words counted by
`A_m(<=K)` end in one.  Counting parameters rather than distinct cycles,
and multiplying by the two phases, only gives the upper bound
`A_m(<=K)=2^{b+o(b)}` from Theorem 2.1.  Finally Stirling's formula in
`N=binom(2b,b-1)` gives (3.6). \(\square\)

This is already a theorem about actual `D*` overlap.  Evaluating the exact
Dyck/first-return indicator cannot create a candidate that violates the
necessary parity inequality (3.3), so there is no hidden collection of
`4^b/poly(b)` actual high-overlap one-ascent tours at `K=b/log b` or at
any other sublinear `K`.

### Corollary 3.2 (nonuniform losses do not rescue the family)

Suppose a rankwise-disjoint collection of one-ascent partial supports is
contained in the Catalan-switched factor, has `Theta(N/q)` members, and
has total deletion `o(N)`.  Then such a collection cannot cover a fixed
positive fraction of that factor.

#### Proof

The average deletion is `o(q)`.  Choose `eta_b->0` so that all but `o(1)`
of the supports delete at most `eta_b q`; Markov's inequality supplies
such a sequence.  Each of these supports retains more than `q/2` flags
for large `b`, so two of them cannot be disjoint subsets of the same full
phase support.  They therefore require `Theta(N/q)` distinct phase
supports with loss `o(q)`, contradicting Theorem 3.1. \(\square\)

## 4. Scope

The one-ascent route is now closed throughout the entire sublinear
parity-defect regime.  Any common loss compatible with coefficient one
has `L=o(b^2)`, hence `K=L/h=o(b)`, and falls under Theorem 3.1.

This does not close Gate C.  General Hamilton cycles with `o(b)`
same-parity edges are factorially numerous, and the mesoscopic staircase
orbit reaches all relevant parity layers.  What remains is a non-one-ascent,
factor-adapted family with enough actual Dyck-compatible flags, followed
by an integral rankwise matching and the deeper symmetric-chain lift.

## 5. Finite audit

The companion checker
`scratch/verify_gate_c_one_ascent_full_sublinear_scarcity_20260822.py`
exhausts binary words through length 15, verifies the exact generating
function and coefficient sandwich, and checks the actual factor-overlap
implication for all one-ascent parameters at `b=3,5`.  It is confirmatory;
the general proof is above.
