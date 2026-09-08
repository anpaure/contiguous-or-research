# Independent audit: complete-layer two-cut no-go and atomic histogram majorisation

**Date:** 2026-08-04

**Method:** independent symbolic replay; no computation, search, or solver

**Audited source:**
`MATH_THEOREM_COMPLETE_LAYER_BLOCK_TWO_CUT_NOGO_AND_ATOMIC_HISTOGRAM_MAJORISATION_20260804.md`

**Verdict:** **GO at the explicitly stated rank-histogram scope**, after two
nonmathematical clarifications were inserted into the source: the finite
demand sequence in Theorem 2.1 is zero-extended, and the triangular total
mass relation is an equality only in the active-boundary case
`Lambda>DW`.

## 1. Both-parity Gaussian normalization

Write `r=ceil(k/2)`, `W=binom(k,r)`, `D=d(k)` and `t_0=r-D`.
The defining scalar relation for `d(k)` gives

\[
 D=\sqrt{\frac{\pi k}{8}}+O(1),
 \qquad \frac{2D^2}{k}=\frac\pi4+o(1).
\tag{1.1}
\]

For every fixed `M`, the local central-binomial estimate gives, uniformly
for `0<=x<=M` and bounded integer perturbations `u`,

\[
 \frac{\binom{k}{r-xD+u}}{W}
 =\exp\!\left(-\frac{2x^2D^2}{k}\right)+o(1)
 =e^{-(\pi/4)x^2}+o(1).
\tag{1.2}
\]

For even `k`, `r=k/2` is the unique central rank.  For odd `k`, the
binomial maximum occurs at the two ranks straddling `k/2`, while the
chosen `r` differs from the mean by `1/2`.  This changes the displacement
in (1.2) by only `O(1)`, already absorbed by `u`.  Thus the exponent
`a=pi/4` and every subsequent limit are valid on both parities.

## 2. Replay of the two-cut no-go

The highest block has width `ell_1` and top rank `t_0-1`.  Because every
one of its `C_(t_0-1)` complete-layer flags is charged load `ell_1`, its
own suffix cut forces

\[
 C_{t_0-1}\le W-C_{t_0+\ell_1-1}.
\tag{2.1}
\]

Pass to a subsequence on which `ell_1/D -> alpha`.  The normalized
distances below the chosen central rank in the two terms of (2.1) are
respectively `1` and `1-alpha`.  Therefore

\[
 e^{-a}\le 1-e^{-a(1-\alpha)^2}.
\tag{2.2}
\]

Solving (2.2) gives

\[
 \alpha\le
 1-\sqrt{\frac{-\log(1-e^{-a})}{a}}=\alpha_*.
\tag{2.3}
\]

Since `a>log 2`, `e^{-a}<1/2`; hence the square root in (2.3) lies
strictly between zero and one and `0<alpha_*<1`.  Applying (2.3) to a
subsequence attaining the limsup proves
`limsup ell_1/D <= alpha_*` without assuming convergence of the original
sequence.

At the `q=1` cut the first two blocks contribute at least

\[
 C_{t_0-1}+C_{t_0-\ell_1-1}.
\tag{2.4}
\]

The second displacement is `1+ell_1/D`.  Monotonicity of the binomial
layers on the lower half, (1.2), and the limsup bound give

\[
 \frac{A_1}{W}\ge
 e^{-a}+e^{-a(1+\alpha_*)^2}+o(1).
\tag{2.5}
\]

Meanwhile `K_1/W=1-e^{-a}+o(1)`, so

\[
 \frac{A_1-K_1}{W}\ge
 2e^{-a}+e^{-a(1+\alpha_*)^2}-1+o(1).
\tag{2.6}
\]

The constant in (2.6) is strictly positive.  Direct rational interval
bounds from `3.1415<pi<3.1416` and the alternating exponential series
place it above `0.28`, so the source's weaker assertion `epsilon>0` is
certified without a numerical search.

Finally, `t_0/D -> infinity`, so a second residual block necessarily
exists for all sufficiently large `k`.  The top targets of the
complete-layer flags are distinct.  Removing one unit from the `q=1`
overload therefore omits at least one distinct named target, proving the
claimed `Omega(W)` weighted omission within this unsplit-block model.

## 3. Exact socket conjugate sequence

At start rank `t`, a socket has capacity `c=t-t_0`.  The start
multiplicities are

\[
 h_{t_0}=C_{t_0},\qquad h_t=C_t-C_{t-1}\quad(t_0<t\le r).
\tag{3.1}
\]

They are nonnegative on the lower Boolean half and telescope to `C_r=W`.
For `1<=q<=D`, the number of sockets of capacity at least `q` is exactly

\[
 \sum_{t=t_0+q}^{r}(C_t-C_{t-1})
 =C_r-C_{t_0+q-1}
 =W-C_{t_0+q-1}=K_q.
\tag{3.2}
\]

This also checks both endpoints.  At `q=1` it excludes precisely the
capacity-zero sockets.  At `q=D` it counts starts at rank `r`; on odd
`k`, where the two central layers have equal size, this count is correctly
zero.

## 4. Exact Gale/max-flow criterion

Construct the standard network

\[
 \text{source}\longrightarrow\text{rank columns}
 \longrightarrow\text{sockets}\longrightarrow\text{sink},
\]

with source-column capacity `n_s`, unit column-socket capacities, and
socket-sink capacity `c_i`.  For a set `Q` of `p` columns, socket `i` can
accept at most `min(c_i,p)` units.  Eliminating the socket side of a cut
therefore gives the necessary and sufficient inequalities

\[
 \sum_{s\in Q}n_s\le\sum_i\min(c_i,p).
\tag{4.1}
\]

For fixed `p`, the largest left side is the sum of the `p` largest
demands.  Ferrers double counting and (3.2) give

\[
 \sum_i\min(c_i,p)
 =\sum_{q=1}^{\min(p,D)}|\{i:c_i\ge q\}|
 =\sum_{q=1}^{\min(p,D)}K_q.
\tag{4.2}
\]

These are all cuts, not merely necessary inequalities.  Integral
max-flow produces the required zero-one matrix.  The source now explicitly
zero-extends the finite decreasing demand list, so its notation `p>=1`
has no endpoint ambiguity.

## 5. The analytic one-crossing argument

Set

\[
 P(x)=e^{-a(1-x)^2}+e^{-a(1+x)^2}
 =2e^{-a(1+x^2)}\cosh(2ax).
\tag{5.1}
\]

Its derivative has the sign of

\[
 f(x)=\tanh(2ax)-x.
\tag{5.2}
\]

For `x>0`,

\[
 f'(x)=2a\operatorname{sech}^2(2ax)-1
\]

is strictly decreasing.  It starts positive, while `f(1)<0`; hence `f`
has exactly one positive zero.  Thus `P` first increases and then
decreases.  Since

\[
 P(0)=2e^{-a}<1,
 \qquad P(1)=1+e^{-4a}>1,
\tag{5.3}
\]

the decreasing branch remains above one all the way to its endpoint, and
`P` crosses level one exactly once, on its increasing branch.

Now let

\[
 H(\theta)=\theta-\int_0^\theta P(x)\,dx.
\tag{5.4}
\]

Then `H'=1-P` is first positive and then negative, so the minimum of `H`
on `[0,1]` occurs at an endpoint.  The endpoint values are

\[
 H(0)=0,
 \qquad
 H(1)=1-\int_0^2e^{-(\pi/4)u^2}\,du
 =1-\operatorname{erf}(\sqrt\pi)>0.
\tag{5.5}
\]

Therefore `H(theta)>0` for every `theta>0`.  Moreover,

\[
 \lim_{\theta\downarrow0}\frac{H(\theta)}\theta
 =1-2e^{-a}>0.
\tag{5.6}
\]

So `H(theta)/theta` extends to a positive continuous function on the
compact interval `[0,1]`.  This proves `max G(theta)<1` with a fixed
positive margin.

## 6. Uniform Riemann margin, including `p/D -> 0`

For `0<=j<D`, the two ranks in the discrete cut have normalized
displacements

\[
 \frac{r-(t_0-1-j)}D=1+\frac{j+1}{D},
 \qquad
 \frac{r-(t_0+j)}D=1-\frac jD.
\tag{6.1}
\]

The uniform estimate (1.2) applies across this entire band.

Consider any sequence `k -> infinity` and `1<=p<=D`.  If a subsequence
has `p/D -> theta>0`, division of the cut sum by `pW` gives the Riemann
average `G(theta)`.  The convergence is uniform when `theta` stays in a
compact subinterval of `(0,1]`.  If instead `p/D -> 0`, every
`j<=p-1` has `j/D -> 0` uniformly, and the same normalized average tends
to

\[
 2e^{-a}<1.
\tag{6.2}
\]

The positive compact margin in Section 5 and this small-`p` limit exclude
every countersequence to a uniform discrete margin.  Hence some absolute
`eta>0` satisfies

\[
 \sum_{j=0}^{p-1}
 \left(C_{t_0-1-j}+C_{t_0+j}\right)
 \le(1-\eta)pW
\]

simultaneously for all `1<=p<=D` and all sufficiently large `k`.

## 7. Completion of every majorisation cut

For sufficiently large `k`, `r-2D>0`, and the binomial layers are
strictly increasing throughout the residual range.  Since
`0<=n_s<=C_s`, the sum of the `p` largest residual demands is at most

\[
 \sum_{j=0}^{p-1}C_{t_0-1-j}.
\tag{7.1}
\]

For `p<=D`, the inequality in Section 6 rearranges to

\[
 \sum_{j=0}^{p-1}C_{t_0-1-j}
 \le pW-\sum_{j=0}^{p-1}C_{t_0+j}
 =\sum_{q=1}^{p}K_q.
\tag{7.2}
\]

For `p>D`, the right side of the Gale cut is the total capacity, so the
single scalar mass inequality suffices.  Once the matrix exists, a row
of actual load at least `q` necessarily lies in a socket of capacity at
least `q`; (3.2) therefore gives the claimed histogram inequality
`A_q<=K_q`.

## 8. Triangular residual mass identity

Let `Lambda=sum_(s=1)^(r-1) C_s`, let the boundary delete `b_s` targets
only in residual ranks `s<t_0`, and put `h=sum_s b_s=(Lambda-DW)_+`.
Then

\[
 \sum_{s<t_0}n_s
 =\Lambda-\sum_{s=t_0}^{r-1}C_s-h,
\tag{8.1}
\]

while (3.2) gives

\[
 \sum_{q=1}^{D}K_q
 =DW-\sum_{s=t_0}^{r-1}C_s.
\tag{8.2}
\]

Thus the required mass inequality is equivalent to
`Lambda-h<=DW`, which is automatic from the definition of `h`.  It is an
equality when `Lambda>DW`; when `Lambda<=DW`, `h=0` and the difference is
exactly the already available scalar slack.  No assumption about the
distribution of the `b_s`, beyond `0<=b_s<=C_s` and support in the
residual ranks, enters any proper Gale cut.

## 9. Scope and surviving theorem

The negative result applies only to contiguous residual blocks whose
complete top layer is unsplit and charged one common width.  It does not
exclude within-layer splitting, cross-SCD rechainization, or other global
flag constructions.

The positive result is exact but only at the rank-incidence level.  A row
of the Gale matrix is not yet a literal Boolean flag: its selected named
targets need not be nested, need not share one named rank-`r` owner, and
need not belong to one complete-layer orbit compatible with the existing
joint-start lift.  Accordingly the theorem proves neither an actual lower
deck nor `nu(k)<=B(k)+O(1)`.

The exact remaining lower-side task is therefore correctly stated as an
atomic-to-complete named nested-flag lift.  No aggregate suffix-capacity,
parity, Gaussian-rank, or integer rank-histogram obstruction survives.

## Final verdict

All requested components replay: both-parity scaling, the
`alpha_*`/`epsilon` no-go, exact socket conjugacy, Gale integrality, the
analytic `P/H` one-crossing proof, the uniform Riemann margin including
`p/D -> 0`, and the triangular residual identity.  The source is **GO at
its stated scope** after the two clarifying edits recorded above.
