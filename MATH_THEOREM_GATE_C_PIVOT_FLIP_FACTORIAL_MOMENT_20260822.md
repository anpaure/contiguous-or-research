# Gate C: pivot flips give all factorial moments of ballot cuts

**Status (2026-08-22).** Every assertion below is proved.  Let `G` be the
number of two-sided-ballot cuts of a uniform cyclic block order on odd
`K`.  Then, for every `j`,

\[
                 \boxed{\mathbb E(G)_j\le
                 \{2(H_e+H_{e+1})\}^j},\qquad K=2e+1.  \tag{0.1}
\]

Thus the previously open near-all-cut count is at most

\[
 \boxed{|\{\tau:G(\tau)\ge K-R\}|
 \le K^R\{2(H_e+H_{e+1})\}^{K}.}                       \tag{0.2}
\]

At the coefficient-one equal-block scale
`K=Theta(b/log b)` and `R=O(b/log^2 b)`, its logarithm is `o(b)`.  Hence
equal blocks supply only `exp(o(b))` high-overlap block orders, far below
the `4^b/poly(b)` local multiplicity scale.  This decisively rules out that
equal-block subroute; it does not rule out unequal/multiscale blocks or
construct the required Gate-C packing.

Throughout, `K=2e+1>=3`, and values and positions are represented by
`0,...,K-1`.

## 1. Ballot cuts and a threshold walk

Let `tau(p)` be the value at position `p`, and let
`sigma=tau^{-1}`.  For distinct values `a,v`, define

\[
 w_a(v)=(-1)^{((v-a)\bmod K)+((\sigma(v)-\sigma(a))\bmod K)}.       \tag{1.1}
\]

The cut `a` is *good* if, in the order

\[
                       a+1,a+2,\ldots,a+K-1,             \tag{1.2}
\]

every prefix sum of the signs lies between zero and the terminal sum.
Equivalently, every prefix and every suffix has nonnegative sum.

Put

\[
 c_v=(-1)^{v+\sigma(v)}.                                \tag{1.3}
\]

For each position threshold `p`, define a walk, indexed in linear value
order, by

\[
 X_p(v)=c_v(-1)^{\mathbf1_{\sigma(v)<p}},\qquad
 F_p(-1)=0,\qquad F_p(t)=\sum_{v=0}^tX_p(v).             \tag{1.4}
\]

At position `p`, let `a=tau(p)`.  Then `sigma(a)=p` and

\[
                         X_p(a)=c_a.                    \tag{1.5}
\]

Moving the threshold from `p` to `p+1` flips exactly this increment:

\[
 X_{p+1}(a)=-X_p(a),\qquad X_{p+1}(v)=X_p(v)\quad(v\ne a).         \tag{1.6}
\]

## 2. Good cuts can flip only pivot edges

Call an edge `a` a *positive pivot* of a walk `F` with increments `X`
when `X(a)=+1` and

\[
 F(t)\ge F(a-1)\quad(-1\le t\le a-1),\qquad
 F(t)\ge F(a)\quad(a\le t\le K-1).                    \tag{2.1}
\]

Call it a *negative pivot* when `X(a)=-1` and both inequalities reverse.

### Lemma 2.1 (pivot necessity)

If `a=tau(p)` is a good cut, then `a` is a positive pivot of `F_p` when
`c_a=+1`, and a negative pivot when `c_a=-1`.

#### Proof

For representatives `x,y`, oddness of `K` gives

\[
 (-1)^{(x-y)\bmod K}=(-1)^{x+y+\mathbf1_{x<y}}.         \tag{2.2}
\]

Since `sigma(a)=p`, (1.1), (1.3), and (1.4) give

\[
 w_a(v)=
 \begin{cases}
  c_aX_p(v),&v>a,\\
 -c_aX_p(v),&v<a.
 \end{cases}                                           \tag{2.3}
\]

Every prefix of (1.2) which remains in `a+1,...,K-1` is nonnegative.
Therefore

\[
 c_a\{F_p(t)-F_p(a)\}\ge0\qquad(a\le t\le K-1).       \tag{2.4}
\]

Every suffix of (1.2) which remains in `0,...,a-1` is also nonnegative.
For a suffix starting at `r`, this says

\[
 -c_a\{F_p(a-1)-F_p(r-1)\}\ge0
 \qquad(0\le r\le a).                                  \tag{2.5}
\]

Equations (2.4)--(2.5), together with
`F_p(a)-F_p(a-1)=X_p(a)=c_a`, are exactly the appropriate pivot
inequalities. \(\square\)

### Lemma 2.2 (at most two pivots)

Every walk with increments in `{+1,-1}` has at most one positive pivot and
at most one negative pivot.

#### Proof

Suppose `a<b` were positive pivots.  The right inequality at `a` and the
left inequality at `b` would give

\[
 F(b-1)\ge F(a)=F(a-1)+1,qquad F(a-1)\ge F(b-1),        \tag{2.6}
\]

a contradiction.  Reversing every sign proves the negative assertion.
\(\square\)

Thus, immediately before each flip (1.6), there are at most two values
which could possibly be good.

## 3. Conditioning on the parity-color fiber

Fix the full color vector `c=(c_v)`.  A value `v` may occupy exactly the
positions `p` satisfying

\[
                      (-1)^{v+p}=c_v.                  \tag{3.1}
\]

Conditional on a nonempty color fiber, a uniform order `tau` is obtained
by two independent uniform bijections: the values allowed at even
positions are bijected to the even positions, and likewise for odd
positions.

Reveal `tau(0),tau(1),...` in position order.  Just before position `p` is
revealed, the walk `F_p` is determined by the color vector and the revealed
history: (1.4) merely records which increments have already been flipped.
The next value is uniform among the values still eligible for the parity of
`p`.  Writing `p=2r` or `p=2r+1`, the sizes of these pools are

\[
 n_{2r}=e+1-r\quad(0\le r\le e),\qquad
 n_{2r+1}=e-r\quad(0\le r<e).                           \tag{3.2}
\]

Let `I_p` indicate that the value selected at position `p` is one of the
positive or negative pivots of `F_p`.  Lemma 2.2 and conditional uniformity
give, for every history in every nonempty color fiber,

\[
 \Pr(I_p=1\mid c,\tau(0),...,\tau(p-1))\le {2\over n_p}.             \tag{3.3}
\]

If `P=sum_p I_p`, Lemma 2.1 gives the pointwise domination

\[
                              G\le P.                   \tag{3.4}
\]

## 4. All falling factorial moments

We record the elementary adapted-indicator estimate used below.

### Lemma 4.1 (factorial hazard bound)

If adapted indicators `I_0,...,I_{K-1}` satisfy
`Pr(I_p=1 | history)<=q_p` for deterministic `q_p`, then, for every
`j>=1`,

\[
             \mathbb E\left(\sum_p I_p\right)_j
             \le\left(\sum_p q_p\right)^j.             \tag{4.1}
\]

#### Proof

Expand the falling factorial as the sum of products over ordered distinct
times.  After sorting any such times, iterated conditioning bounds its
expectation by the product of the corresponding `q_p`.  Summing, and then
allowing repeated times, is at most the full multinomial expansion on the
right of (4.1). \(\square\)

### Theorem 4.2 (uniform factorial moments)

For every `1<=j<=K`,

\[
 \boxed{\mathbb E(G)_j\le B_K^j,\qquad
 B_K=2(H_e+H_{e+1})\le4H_{e+1}.}                       \tag{4.2}
\]

#### Proof

Apply Lemma 4.1 conditionally on `c`, using (3.2)--(3.4):

\[
 \sum_{p=0}^{K-1}{2\over n_p}
 =2\sum_{r=1}^{e+1}{1\over r}+2\sum_{r=1}^e{1\over r}
 =B_K.                                                  \tag{4.3}
\]

Because falling factorials are increasing on nonnegative integers,
`(G)_j<=(P)_j`.  The bound is uniform in every nonempty color fiber, so
averaging over `c` proves (4.2). \(\square\)

The estimate is deliberately robust: it uses only the necessary
half-meander conditions in Lemma 2.1, not the remaining two halves of the
two-sided-ballot test.

## 5. Near-all-cut entropy

Let `0<=R<K` and

\[
                \mathcal B_{K,R}=\{\tau:G(\tau)\ge K-R\}.             \tag{5.1}
\]

Taking `j=K-R`, the falling-factorial Markov inequality and Theorem 4.2
give

\[
 { |\mathcal B_{K,R}|\over K!}
 \le {B_K^{K-R}\over(K-R)!}.                           \tag{5.2}
\]

Since `K!/(K-R)!<=K^R` and `B_K>=1`,

\[
 \boxed{|\mathcal B_{K,R}|\le K^R B_K^K,qquad
 \log|\mathcal B_{K,R}|=O(K\log\log K+R\log K).}       \tag{5.3}
\]

At `K=Theta(b/log b)` and `R=O(K^2/b)=O(b/log^2 b)`, both terms in the
last exponent are `o(b)`.  Hence

\[
                         |\mathcal B_{K,R}|=\exp(o(b)). \tag{5.4}
\]

The equal-block overlap theorem says that loss `O(bK)` requires precisely
`R=O(K^2/b)` failed cuts.  Formula (5.4) proves that this family cannot
provide the exponentially many macroscopically different near-tours
needed for a coefficient-one packing.

The companion checker
`scratch/verify_gate_c_pivot_flip_factorial_moment_20260822.py` verifies
the sign identity, good-cut pivot necessity, the two-pivot bound, the
color-fiber conditional law, and all displayed finite moment inequalities
through `K=9`.
