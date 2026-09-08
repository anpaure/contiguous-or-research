# Audit of all-depth wreath sprinkling

## Verdict

The all-depth sprinkling theorem is correct.  It is a cleaner finite
strengthening of the earlier outer-reservoir argument: each auxiliary cyclic
order is emitted as one singleton block of length `2n-2`, so it covers all
of its proper cyclic intervals at every rank and the full set.  No separate
tail cutoff or tail estimate is needed.

For an exact middle factor, structured shadow control is required only
through

\[
h=(1+o(1))\sqrt{m\log\log m}.
\]

This is the same sharp asymptotic threshold as the previously audited
independent-reservoir method, with simpler all-depth bookkeeping.

## 1. Literal blocks

The inner depth-`h` erosion block has `n+2h+1` entries and exposes every
cyclic interval of lengths `m-h,...,m+1+h` by consecutive unions.

For a cyclic order `x_0,...,x_(n-1)`, the all-depth block

\[
\{x_0\},\ldots,\{x_{n-1}\},
\{x_0\},\ldots,\{x_{n-3}\}
\]

has length `2n-2`.  Every proper cyclic interval, including a length-`n-1`
interval beginning at `x_(n-1)`, occurs contiguously.  The first `n`
entries have union `[n]`.  Thus the boundary ranks cause no off-by-one
problem: `q=m-1` pairs ranks one and `n-1`, while the full set is supplied
separately; the empty set is not required.

## 2. Exact finite inequality

Let `F` be an exact middle wreath factor, let

\[
N_q=\binom n{m-q},\qquad \mu_q=W/N_q,
\]

and take `T>=1` independent uniform cyclic orders.  A fixed proper `r`-set is a
cyclic interval with probability exactly `n/C(n,r)`.  Complementation pairs
the lower and upper holes.  Therefore some deterministic auxiliary family
leaves at most

\[
2\sum_{q=h+1}^{m-1}N_q(1-n/N_q)^T
\]

outer masks.  Appending them literally proves

\[
\begin{aligned}
\nu(2m+1)\le{}&W+(2h+1)W/n
 +2\sum_{q=1}^{h}M_q(F)\\
&+(2n-2)T
 +2\sum_{q=h+1}^{m-1}N_q(1-n/N_q)^T.
\end{aligned}
\tag{2.1}
\]

Since `mu_q` increases,

\[
\text{last sum}\le
\frac{2mW}{\mu_h}
 \exp(-(Tn/W)\mu_h).
\tag{2.2}
\]

The conditional-expectation potential in the submitted proof correctly
derandomizes the same `T` orders simultaneously across every outer depth.

## 3. Threshold

Let `a_m->infinity` with `log a_m=o(log log m)`, let `h_m` be the least
depth with

\[
\mu_{h_m}\ge3a_m\log m,
\]

and put `T_m=ceil((W/n)/a_m)`.  The exact ratio expansion is

\[
\log\mu_q
=\frac{q(q+1)}m+O(q^3/m^2)
\]

uniformly through `q=O(sqrt(m log m))`.  Hence

\[
h_m=(1+o(1))\sqrt{m\log\log m}.
\]

The auxiliary blocks cost at most `2W/a_m+o(W)`.  Moreover

\[
(T_mn/W)\mu_{h_m}\ge3\log m,
\]

so (2.2) is `o(W)`.  Thus

\[
\sum_{q=1}^{h_m}M_q(F_m)=o(W)
\]

is sufficient for coefficient one in odd dimension, and the trimmed lift
transfers it to even dimension.

## 4. Strongest combined form

Exact middle ownership and literal shallow-hole payment are both optional.
Combining all-depth sprinkling with the relaxed trace-pair repair gives the
following still weaker gate.  Let `P_m` be any `p_m` cyclic orders and let
`Phi_h(P_m,Z_m)` be the truncated complementary-trace occupancy from
`SOFT_TRACE_COMPRESSION_AND_SHALLOW_GATE_20260724.md`.  If

\[
p_m n=W+o(W),\qquad
\Phi_{h_m}(P_m,Z_m)=o(W),
\]

then the inner blocks, trace-pair repairs, `T_m` all-depth singleton blocks,
and their remaining literal holes form a universal word of length
`W+o(W)`.

This is now the weakest clean cyclic sufficient condition in the project.
