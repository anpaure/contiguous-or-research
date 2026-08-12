# AD22 audit: carrier chunks and the multi-swap cube

## 0. Outcome

Two new positive objects have enough static capacity to matter at leading
order:

1. stationary carrier-rotor chunks with \(\ell\) distinct middle owners;
2. the \(K=L^2=(1-o(1))M\) rank-isolated cells in the positive multi-swap
   cube.

Neither object, by itself, supplies the low-variance mean-reverting exchange
kernel required by AD22.  The obstruction is an exact pointwise
fluctuation--dissipation identity, not a weakness of a concentration bound.

For one carrier chunk, exact mean reversion at rate \(\alpha\) forces
\[
\boxed{
\mathbb E\|z\|_2^2
=2\alpha\ell(1-\ell/B),
\qquad B=\binom Mm.
}
\tag{0.1}
\]
Thus bounded variance forces \(\alpha=O(1/\ell)\).  Selecting one of
\(R\asymp W/\ell\) chunks uniformly gives global rate
\(\kappa=\alpha/R\).  The AD22-scale rate \(\kappa\asymp1/R\) therefore
costs variance \(\Theta(\ell)\), while bounded variance gives only
\(\kappa=O(1/W)\).

For a positive cube of \(K\) independently selectable, support-disjoint
rectangle cells, exact reversion of every cell coefficient at rate
\(\alpha\) forces
\[
\boxed{
\mathbb E\|z\|_2^2=2\alpha K.
}
\tag{0.2}
\]
At the coefficient-one capacity \(K\asymp M\), constant per-top reversion
therefore has variance \(\Theta(M)\), reproducing the independent-packet
barrier.  Bounded variance reduces the rate to \(O(1/M)\).

The outer-product \(L\)-by-\(L\) grid obeys the same identity.  Its natural
one-sign heat bath has
\[
\alpha=1/L,
\qquad
\mathbb E\|z\|_2^2=8L
\tag{0.3}
\]
in the direct sum of hard rows.  It has bounded variance in each individual
row, but after a uniform choice among the \(p=N_H\) tops its mean-reversion
rate is only \(1/(pL)\), a factor \(L\) below AD22.

Consequently the new capacity cannot be converted into AD22 merely by a
local heat bath, fair bit resampling, or independent chunk resampling.  A
successful kernel must couple different carriers/tops so that their
\(\Theta(\ell)\) or \(\Theta(M)\) individual fluctuations cancel in the
aggregate while their mean drift adds.  This is exactly the global negative
covariance missing from the current construction.

## 1. A pointwise incidence-vector identity

Let \(\Omega\) be a finite target set of size \(B\).  Let
\(v\in\{0,1\}^{\Omega}\) have exactly \(\ell\) ones, and put
\[
\bar v=\frac\ell B\mathbf1.
\]
Suppose a random legal successor \(v'\), also of weight \(\ell\), satisfies
the exact conditional mean-reversion identity
\[
\mathbb E(v'-v\mid v)=-\alpha(v-\bar v).
\tag{1.1}
\]

### Lemma 1.1

For every current state \(v\),
\[
\boxed{
\mathbb E(\|v'-v\|_2^2\mid v)
=2\alpha\ell(1-\ell/B).
}
\tag{1.2}
\]

### Proof

For a coordinate \(x\) currently occupied by \(v\), the increment is
either zero or minus one.  Equation (1.1) therefore gives
\[
\Pr(v'_x=0\mid v)=\alpha(1-\ell/B).
\]
Summing over the \(\ell\) occupied coordinates, the expected number of
removed targets is
\[
\alpha\ell(1-\ell/B).
\]
Since \(v'\) and \(v\) have equal weight, the number of additions equals
the number of removals.  The squared Euclidean increment is their symmetric
difference size, twice the number of removals. \(\square\)

This is pointwise.  It assumes neither reversibility nor a stationary
distribution.

There is also a useful stationary form.  If a Markov kernel with stationary
law \(\pi\) has observable \(X\), mean \(b=\mathbb E_\pi X\), and drift
\[
\mathbb E(X'-X\mid X)=-\alpha(X-b),
\]
then stationarity and expansion of \(\|X'-b\|_2^2\) give
\[
\boxed{
\mathbb E_\pi\|X'-X\|_2^2
=2\alpha\mathbb E_\pi\|X-b\|_2^2.
}
\tag{1.3}
\]

## 2. Application to stationary carrier chunks

Fix one carrier copy and restrict to the repetition-free stationary
\(\ell\)-walks from
`TRP_OWNER_PATH_CODEGREE_AUDIT_20260725.md`.  Their owner incidence vectors
have weight \(\ell\).  Coordinate symmetry gives the exact barycenter
\[
\bar v_U=\frac\ell B\mathbf1_{\binom Um}.
\tag{2.1}
\]

Any legal single-chunk kernel satisfying
\[
\mathbb E(v'-v\mid v)=-\alpha(v-\bar v_U)
\tag{2.2}
\]
therefore obeys (0.1).  Since \(B\) is superpolynomially larger than
\(\ell\),
\[
\mathbb E\|v'-v\|_2^2=(2+o(1))\alpha\ell.
\tag{2.3}
\]

Now use \(R\) labelled carrier copies, where
\[
R=K_0N_H=(1+o(1))W/\ell.
\tag{2.4}
\]
Choose one copy uniformly and apply the single-copy kernel.  Summing the
carrier barycenters gives the constant global owner mean, so the global load
drift is
\[
\mathbb E(z\mid h)=-\frac\alpha R(h-\bar h\mathbf1).
\tag{2.5}
\]
Thus
\[
\kappa=\frac\alpha R.
\tag{2.6}
\]

The AD22 analogue asks for \(\kappa\ge c/R\), which requires
\(\alpha\ge c\).  Equation (2.3) then forces row variance
\[
\sigma^2=\Omega(\ell).
\tag{2.7}
\]
Conversely, \(\sigma^2=O(1)\) forces
\[
\alpha=O(1/\ell),
\qquad
\kappa=O(1/(R\ell))=O(1/W).
\tag{2.8}
\]
The stopping ratio remains
\[
\frac{\sigma^2}{\kappa}=\Theta(R\ell)=\Theta(W)
\tag{2.9}
\]
throughout this interpolation.  Independent full resampling is the endpoint
\(\alpha=1\), with exact variance
\[
2\ell(1-\ell/B).
\]

This does not rule out a coupled update of many carrier copies.  It proves
what such a coupling must accomplish: removals and additions from different
chunks must cancel on common global owner coordinates.  Without those
negative cross-copy covariance terms, summing (2.3) reproduces the same
\(\Theta(W)\) floor.

The owner near-matching supplied by the proposed chunk hypergraph would
create precisely such global dependence, but the degree/codegree calculation
does not itself construct an exchange kernel on near-matchings.  Alternating
cycles would be needed, and no bounded-length alternating-cycle supply has
yet been proved for this path hypergraph.

The same obstruction applies to every flag row, even before proving that
the row is support-simple.  Let \(p_r\) be the integer occurrence vector of
one \(\ell\)-chunk at rank \(r=m\pm q\).  It has total mass \(\ell\), and
under the uniform stationary chunk law its mean is
\[
\bar p_r=\frac\ell{\binom Mr}\mathbf1.
\]
Since every nonnegative integer vector of mass \(\ell\) has squared norm at
least \(\ell\),
\[
\mathbb E\|p_r-\bar p_r\|_2^2
\ge \ell-\frac{\ell^2}{\binom Mr}=(1-o(1))\ell.
\tag{2.10}
\]
Therefore any kernel which preserves this uniform stationary law and has
exact row drift \(-\alpha(p_r-\bar p_r)\) satisfies, by (1.3),
\[
\mathbb E\|p'_r-p_r\|_2^2
\ge(2-o(1))\alpha\ell.
\tag{2.11}
\]
Thus flag repetitions cannot improve the local variance/drift ratio.

## 3. Independent support-disjoint rectangle bits

Let \(\rho_1,\ldots,\rho_K\) be pairwise support-disjoint elementary
rectangles, so
\[
\|\rho_j\|_2^2=4,
\qquad
\langle\rho_i,\rho_j\rangle=0\quad(i\ne j).
\tag{3.1}
\]
Write a positive cube as
\[
x(E)=x_0+\sum_{j=1}^K E_j\rho_j,
\qquad E\in\{0,1\}^K.
\tag{3.2}
\]
Suppose a legal cube kernel mean-reverts every bit toward its fair mean:
\[
\mathbb E(E'_j-E_j\mid E)
=-\alpha(E_j-\tfrac12)
\qquad(1\le j\le K).
\tag{3.3}
\]

### Lemma 3.1

At every cube vertex,
\[
\boxed{
\mathbb E\|x(E')-x(E)\|_2^2=2\alpha K.
}
\tag{3.4}
\]

### Proof

If \(E_j=0\), (3.3) says that the bit turns on with probability
\(\alpha/2\); if \(E_j=1\), it turns off with the same probability.  Thus
the expected number of changed bits is \(\alpha K/2\).  Orthogonality in
(3.1) makes the squared load increment four times the number of changed
bits. \(\square\)

For the positive multi-swap cube,
\[
K=L^2=(1-o(1))M.
\tag{3.5}
\]
Hence an order-one per-top mean-reversion rate has variance \(\Theta(M)\),
not \(O(1)\) and not \(o(M)\).  A one-bit heat bath has
\[
\alpha=1/K,
\qquad
\mathbb E\|z\|_2^2=2,
\tag{3.6}
\]
but after choosing one of the \(p\) tops its global rate is only
\[
\kappa=1/(pK),
\]
again giving stopping ratio \(\Theta(pK)=\Theta(W)\).

The chronology obstruction in the multi-swap note is additional: arbitrary
vertices of this static cube are not all realizable with coefficient-one
path cost.  Lemma 3.1 shows that even if this physical issue were removed,
the fair local cube heat bath would still miss the AD22 variance/drift
ratio.

Truncating the collar from radius \(H\) to radius \(Q\) does not remove the
chronology obstruction.  The path inequality from the multi-swap audit
becomes
\[
N\ge F+(2L-F)(Q-6L+1),
\tag{3.7}
\]
where \(F\) is the number of promotion paths containing the \(2L\) marked
ports.  Here \(L\asymp\sqrt M\) and \(Q/L\to\infty\).  Keeping
\(N=M+O(Q)\) forces
\[
F\ge2L-O(M/Q)=\Theta(L).
\]
Initializing \(\Theta(L)\) radius-\(Q\) paths costs \(\Omega(LQ)\) per top,
and hence
\[
\Omega(LQ N_H)
=\Omega\!\left(W\frac{Q}{\sqrt m}\right)
=\omega(W)
\tag{3.8}
\]
globally.  Thus the independent cell cube is blocked both dynamically and
by its variance/drift ratio.  The cheaper outer-product deployment avoids
the path count but loses independent cell control.

The later rectangular port cube has dimensions
\[
p_0\asymp Q,
\qquad t_0\asymp M/Q,
\qquad p_0t_0\asymp M.
\]
It reduces the forced fragment count to \(\Theta(t_0)=\Theta(M/Q)\).
With a radius-\(Q\) truncation, however, those initializations still cost
\[
\Theta(t_0Q)=\Theta(M)
\]
per top, hence \(\Theta(W)\) globally.  This is better than the full-radius
\(H\) cost, but it remains a positive leading-constant toll rather than
\(o(W)\).  Thus neither known independent-cell geometry is compatible with
coefficient one after truncation.

## 4. The outer-product grid

The physically cheaper complementary-segment construction has cell signs
\[
c_{ij}=u_iv_j,
\qquad 1\le i,j\le L,
\tag{4.1}
\]
and pairwise support-disjoint rectangle vectors \(\rho_{ij}\).  Put
\[
x(u,v)=x_0+\sum_{i,j}c_{ij}\rho_{ij}.
\tag{4.2}
\]

There is a pointwise identity for every kernel on this rank-one sign
manifold.  If
\[
\mathbb E(c'_{ij}-c_{ij}\mid u,v)=-\alpha c_{ij}
\qquad\text{for every }(i,j),
\tag{4.2a}
\]
then, because \(c'_{ij},c_{ij}\in\{-1,+1\}\), each cell changes sign with
probability exactly \(\alpha/2\).  The rectangle supports are disjoint, and
a changed coefficient contributes squared norm
\(4\|\rho_{ij}\|_2^2=16\).  Hence every such kernel satisfies
\[
\boxed{
\mathbb E\|x'-x\|_2^2=8\alpha L^2.
}
\tag{4.2b}
\]
Thus order-one coefficient reversion is incompatible with total vertical
variance \(o(M)\), independently of how many row and column signs are
updated together.

Choose one of the \(2L\) signs uniformly and replace it by a fair sign.  A
fixed cell is affected when its row sign or column sign is selected, so
\[
\mathbb E(c'_{ij}-c_{ij}\mid u,v)=-\frac1L c_{ij}.
\tag{4.3}
\]
Thus the exact coefficient mean-reversion rate is
\[
\alpha=1/L.
\tag{4.4}
\]
With probability one half the chosen sign changes, in which case exactly
\(L\) cell coefficients change by magnitude two.  Therefore
\[
\boxed{
\mathbb E\|x'-x\|_2^2=8L.
}
\tag{4.5}
\]
This also follows from (1.3), since under fair signs
\[
\mathbb E\|x-\mathbb Ex\|_2^2=4L^2.
\]

After the top is chosen uniformly,
\[
\kappa=1/(pL),
\qquad
\sigma^2=8L,
\qquad
\frac{\sigma^2}{2\kappa}=4pL^2=(4+o(1))W.
\tag{4.6}
\]

There is a superficially favorable rowwise fact.  The \(L\) cells changed
by one sign occupy distinct isolated depths.  Hence the expected squared
increment in any fixed rank is \(O(1)\).  But its mean-reversion rate in
that rank is still only \(1/(pL)\).  Sequential AD22 descent would stop at
\(O(pL)\) per affected row, and summing the \(\Theta(L)\) active rows again
gives \(\Theta(pL^2)=\Theta(W)\).

More generally, a typical active depth contains \(K_q=\Theta(L)\) disjoint
cells.  Exact coefficient reversion at rowwise rate \(\alpha_q\) forces
row variance \(8\alpha_qK_q\).  Therefore bounded row variance itself
forces \(\alpha_q=O(1/L)\); the factor-\(L\) rate loss is not peculiar to
the one-sign implementation.

Resampling all signs in one top raises the per-top rate to order one, but
then (4.5) scales to \(\Theta(L^2)=\Theta(M)\).  Partial resampling
interpolates between these two endpoints without changing the
variance/drift ratio.

## 5. Exact capacity--variance tradeoff

The multi-swap construction needs \(K=\Theta(M)\) cells per top because
there are only
\[
p=(1+o(1))W/M
\]
tops and a coefficient-scale correction has total size \(\Theta(W)\).
Thus reducing \(K\) to make a local heat bath cheaper also reduces the
aggregate correction capacity to \(Kp=o(W)\).

Combining this with Lemma 3.1 gives the exact local tradeoff
\[
\boxed{
\text{aggregate capacity }Kp=\Theta(W)
\quad\Longrightarrow\quad
\frac{\text{variance}}{\text{per-top drift rate}}=\Theta(M).
}
\tag{5.1}
\]
The carrier chunks obey the identical relation with \(K\) replaced by
\(\ell\).

Therefore neither construction closes LVMR by an internal fair heat bath.
To obtain rate \(\kappa\asymp1/p\) with bounded row variance, a multi-top
exchange must cancel all but \(O(1)\) of the \(\Theta(M)\) individual
rectangle fluctuations.  In covariance language, if \(z_U\) are the
single-top increments, it must enforce
\[
\sum_{U\ne V}\mathbb E\langle z_U,z_V\rangle
=-\sum_U\mathbb E\|z_U\|_2^2+O(1)
\tag{5.2}
\]
in each treated row, while retaining the sum of their mean drifts.

This is almost complete anticorrelation, not a bounded-dependency
correction.  It agrees with the separate AD22 covariance obstruction:
successful rounding must be genuinely global.

## 6. Revised remaining gate

The useful successor statement is not another local cube or chunk heat
bath.  It is one of the following equivalent global objects.

1. A coupling of carrier-chunk resamplings whose marginal drift is the
   uniform heat-bath drift but whose global symmetric-difference size is
   \(O(1)\) per row.
2. A coupling of rectangle-cell flips across many tops in which almost all
   four-mask increments cancel pairwise, leaving the desired global drift.
3. A near-matching state space for the chunk hypergraph with a supply of
   bounded-length alternating exchanges whose projection on every hard row
   is mean reverting.

The exact owner codegrees \(O(m^{-2})\) make the third route more plausible,
but they do not count alternating cycles or prove the covariance (5.2).
That alternating-cycle/cancellation count is the next mathematical quantity
which must be computed.
