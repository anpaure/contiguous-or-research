# Shallow cyclic near-factors plus an `o(W)` reservoir

## Verdict

The exact reservoir argument is valid, and it combines with the relaxed
cyclic-family transfer to give a weaker sufficient theorem than either the
exact-factor WV lemma or the full-depth relaxed near-factor target.

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad N_q=\binom n{m-q}.
\]

No exact middle partition is required in the theorem below.

## 1. Exact damping inequality

Let `P` be a multiset of `p` cyclic orders.  For `q>=0`, let `M_q(P)` be
the number of rank-`m-q` masks absent from their length-`m-q` cyclic
intervals.  Fix integers

\[
0\le h<H<m,\qquad R\ge0.
\]

### Theorem 1 (relaxed defect damping)

There are `R` additional cyclic orders and a literal nonzero contiguous-OR
word of length at most

\[
\begin{aligned}
&p(n+2h+1)+R(n+2H+1)
 +2\sum_{q=0}^{h}M_q(P)\\
&\quad +2\left\lfloor
 \sum_{q=h+1}^{H}N_q\left(1-\frac n{N_q}\right)^R
 \right\rfloor
 +2\sum_{r=0}^{m-H-1}\binom nr-1.
\end{aligned}
\tag{1.1}
\]

If `P` is an exact middle factor, the `q=0` repair vanishes.  If the base
factor is emitted through depth `H`, the `N_q` in the reservoir term can be
replaced by its actual outer defects `M_q(P)`; (1.1) is the more economical
form and needs no information about those outer defects.

### Proof

For a cyclic order `pi` and depth `D`, emit

\[
I_\pi(0,m-D),\ldots,I_\pi(n-1,m-D),
I_\pi(0,m-D),\ldots,I_\pi(2D,m-D).
\]

This block has length `n+2D+1`.  The union of `t` consecutive entries,
for `1<=t<=2D+2`, is exactly

\[
I_\pi(j,m-D+t-1).
\]

Thus the `p` base blocks at depth `h` cover their lower and complementary
upper shadows through depth `h`; append the `2 sum_(q<=h) M_q(P)` missing
band masks.

Now choose `R` cyclic orders independently and uniformly, and emit their
depth-`H` blocks.  A fixed rank-`m-q` mask is a cyclic interval in one
uniform order with probability exactly `n/N_q`.  Hence the expected number
of masks, summed over `h<q<=H`, missed by every reservoir order is

\[
\sum_{q=h+1}^{H}N_q(1-n/N_q)^R.
\]

Some deterministic choice leaves at most the floor of this expectation.
Complementation shows that its upper holes are exactly the complements of
the lower holes, so twice this many literal repairs suffice.  Finally append
both outer tails; their exact nonempty size is

\[
2\sum_{r=0}^{m-H-1}\binom nr-1.
\]

Every displayed block is an actual word of nonempty masks and all witnesses
are internal contiguous intervals.  This proves (1.1).  `square`

## 2. The new shallow sufficient gate

Fix `epsilon>0`.  Let `gamma(m)->infinity` with
`gamma(m)=o(log log m)`, and put

\[
H=\left\lceil(1/2+\varepsilon)\sqrt{n\log n}\right\rceil,
\qquad
h=\left\lceil\sqrt{m(\log\log m+\gamma(m))}\right\rceil.
\tag{2.1}
\]

### Corollary 2 (shallow relaxed near-factor criterion)

It suffices to construct cyclic families `P_m` such that

\[
p_m n=W+o(W),\qquad
\sum_{q=0}^{h}M_q(P_m)=o(W).
\tag{2.2}
\]

Under (2.2),

\[
\nu(2m+1)=W+o(W),
\]

and the standard trimmed lift gives the same leading coefficient in even
dimensions.  For an exact middle factor, (2.2) reduces to shallow WV through
depth `(1+o(1))sqrt(m log log m)`.

### Proof

Set

\[
\eta=e^{-\gamma(m)/2},\qquad
R=\left\lceil\eta W/n\right\rceil.
\]

Then `eta=o(1)`, so the reservoir blocks cost `o(W)`.  Also

\[
\frac{W}{N_h}
 \ge \exp\!\left(\frac{h(h+1)}{m+h+1}\right)
 \ge \exp(\log\log m+\gamma(m)-o(1)).
\]

Since `N_q` decreases with `q`, uniformly for `h<q<=H`,

\[
(1-n/N_q)^R
 \le \exp(-Rn/N_q)
 \le \exp(-\eta W/N_h).
\]

The last exponent dominates `log m`, so

\[
\frac1W\sum_{q=h+1}^{H}
N_q(1-n/N_q)^R=o(1).
\]

The base block cost is

\[
p_m(n+2h+1)=W+o(W)
\]

because `h=o(n)`.  The shallow repair is `o(W)` by (2.2).  Finally,
Hoeffding and Stirling give

\[
\frac{2\sum_{r=0}^{m-H-1}\binom nr}{W}=o(1)
\]

at the value of `H` in (2.1).  Substitution in (1.1) proves the claim.
`square`

## 3. Exact scope

This theorem removes all need to control a factor or near-factor at depths

\[
\sqrt{m(\log\log m+\gamma(m))}<q
 \le (1/2+\varepsilon)\sqrt{(2m+1)\log(2m+1)}.
\]

It does **not** prove the shallow condition (2.2).  Independent reservoir
orders cannot push the threshold substantially below `sqrt(m log log m)`
at `o(W)` cost: at depth `q` their mean hit count is approximately
`eta W/N_q`, while summing the remaining holes requires that quantity to
dominate `log m`.

One typographical caution in raw derivations: the small binomial ratio is

\[
\binom{2m+1}{m-H}/\binom{2m+1}{m},
\]

not its reciprocal.

