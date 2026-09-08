# Audit of the random-covering and sprinkling claims

Put
\[
n=2m+1,\qquad W=\binom{n}{m},\qquad C_m=W/n,
\]
and let (M_r(\mathcal P)) be the number of (r)-sets which are not a cyclic
interval of any cyclic order in (\mathcal P). All logarithms below are
natural.

## 1. Exact interval probability

For (1\le r\le n-1), a fixed (A\in\binom{[n]}r) is an interval of a
uniform oriented cyclic order with probability
\[
\boxed{\Pr(A\text{ is an interval})=\frac{r!(n-r)!}{(n-1)!}
=\frac n{\binom nr}.}
\]
Indeed, contract (A) to one block, cyclically order the resulting
(n-r+1) objects, and linearly order the elements inside the block. The same
ratio holds if cyclic orders are identified up to reversal. The formula is
not to be used at (r=0,n); those two sets are automatically covered.

## 2. Theorem B is correct (and slightly sharpenable)

Let (k=\lceil \lambda_m C_m\rceil), and choose (k) independent uniform
cyclic orders. For any collection of ranks
(\mathcal R\subseteq\{1,\ldots,n-1\}),
\[
\begin{aligned}
\mathbb E\sum_{r\in\mathcal R}M_r
&=\sum_{r\in\mathcal R}\binom nr
 \left(1-\frac n{\binom nr}\right)^k\\
&\le \sum_{r\in\mathcal R}\binom nr
 \exp\!\left(-\frac{kn}{\binom nr}\right)\\
&\le e^{-\lambda_m}\sum_{r\in\mathcal R}\binom nr
\le 2^n e^{-\lambda_m},
\end{aligned}
\]
because (\binom nr\le W) and (C_m=W/n). Moreover
\[
\frac{2^n}{W}=(1+o(1))\sqrt{\pi m}.
\]
Consequently
\[
\lambda_m=\frac12\log m+\omega(1)
\]
already implies that the total number of uncovered sets in *any* band is
(o_{\mathbb P}(W)). In particular the note's choice
\(lambda_m=(\frac12+\varepsilon)\log m\) gives
\[
\mathbb E M_{\rm total}=O(m^{-\varepsilon}W),
\]
and hence, for example,
\[
\Pr\big(M_{\rm total}>m^{-\varepsilon/2}W\big)
=O(m^{-\varepsilon/2})=o(1).
\]

If “uniform random family” means sampling without replacement rather than an
i.i.d. multiset, the same upper bound holds: the hypergeometric miss
probability is at most the corresponding with-replacement probability.

Thus the probabilistic calculation and its constant (1/2) are correct.
It proves a covering statement with (\Theta(C_m\log m)) rows. It does not,
by itself, preserve an exact-middle-factor/disjointness condition if that is
part of a separate condition (A).

## 3. Exact binomial-ratio bound for sprinkling

For (0\le q\le m), write
\[
N_q=\binom{2m+1}{m-q},\qquad
\lambda_q=\frac W{N_q}.
\]
Then
\[
\lambda_q
=\prod_{i=1}^q\frac{m+1+i}{m+1-i}
\]
and, using
\(log((1+x)/(1-x))\ge2x\),
\[
\boxed{
\log\lambda_q\ge\frac{q(q+1)}{m+1}\ge\frac{q^2}{m}.
}
\]
The last inequality uses (q\le m). This verifies the exponent used in the
note.

Let
\[
q_0=\left\lceil\sqrt{2m\log\log m}\right\rceil,
\qquad \delta_m=\frac1{\log m},
\]
and add (k=\lceil\delta_m C_m\rceil) independent uniform cyclic orders to
an arbitrary initial family. For (q_0<q\le m-1), the expected number of
sets at rank (m-q) missed by the sprinkle is at most
\[
N_qe^{-\delta_m\lambda_q}.
\]
Since
\[
\delta_m\lambda_q
\ge\frac1{\log m}\exp(q_0^2/m)
\ge\log m,
\]
we obtain
\[
\sum_{q>q_0}\mathbb E M_{m-q}
\le \frac1m\sum_{r=1}^{m-q_0-1}\binom nr
\le\frac{2^{n-1}}m
=\left(\frac{\sqrt\pi}{2}+o(1)\right)\frac W{\sqrt m}
=o(W).
\]
Ranks (0,n) are automatic. Complementation gives exactly the same
deficiency at ranks (m-q) and (m+1+q). Thus the tail-sprinkling estimate
and its constants are correct.

## 4. Theorem C is missing an aggregate shallow-band hypothesis

The note assumes merely
\[
M_{m-q}(\mathcal Q)=o(W)\quad\text{for every }0\le q\le q_0.
\]
This does **not** imply
\[
\sum_{q=0}^{q_0}M_{m-q}(\mathcal Q)=o(W),
\]
because (q_0\to\infty). Even a uniform bound
\(\max_{q\le q_0}M_{m-q}=o(W)\) is insufficient: the unspecified (o(1))
may decay more slowly than (1/q_0). The extra sprinkle barely changes the
small-(q) deficiencies (its intensity there is only (1/\log m)), so it
does not repair this logical gap.

The exact corrected theorem is as follows.

> **Corrected band-shrinking theorem.** Suppose (\mathcal Q_m) has
> ( |\mathcal Q_m|=(1+o(1))C_m) (in particular,
> ((1-o(1))C_m) is allowed) and satisfies the aggregate condition
> \[
> \boxed{
> \sum_{q=0}^{q_0}M_{m-q}(\mathcal Q_m)=o(W).
> }
> \]
> Equivalently, the stronger pointwise condition
> \(max_{q\le q_0}M_{m-q}=o(W/q_0)\) suffices. After adjoining
> (\lceil C_m/\log m\rceil) independent uniform cyclic orders, with
> probability (1-o(1)) the resulting family has size
> ((1+o(1))C_m) and has (o(W)) uncovered sets in total over all ranks.

Proof: the shallow aggregate cannot increase; the estimate in Section 3
gives (o(W)) expected tail deficiency; Markov and complementation finish.

If the desired conclusion is only a separate per-rank statement
(M_{m-q}=o(W)), rather than an aggregate (o(W)) across the band, the
original pointwise hypothesis is enough. But all total-hole calculations in
the note, and the constant-one application, use the aggregate formulation,
for which the boxed condition is necessary in the reduction.

Finally, adjoining arbitrary cyclic orders preserves the row-count bound
((1+o(1))C_m) and can only improve coverage. It does **not** preserve an
exact middle ownership/factor condition. Any invocation of Theorem C in an
exact-factor formulation therefore needs an additional completion or
replacement argument.
