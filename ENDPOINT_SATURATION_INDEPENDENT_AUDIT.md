# Independent audit: endpoint saturation and the near-perfect fixed-delay core

## Verdict

**PASS, with two presentation repairs and several important scope
qualifications.**

The endpoint-defect inequality, its zero-defect characterization, the
contiguous fixed-delay-core consequence, the rank-deficit inequality, and the
infinite-subsequence asymptotic argument are all mathematically valid.

The two repairs are:

1. Bounds such as `M-sigma` and `M-2 sigma` should be written with a positive
   part when they are used without first assuming `sigma<=M` or
   `2 sigma<=M`.
2. In the infinite-subsequence statement, the number of exceptional
   endpoints and spare short cells is

   \[
      O\!\left(\frac{W(k)}{\sqrt{k}}\right),
   \]

   not `O(sqrt(k) W(k))` if the displayed fraction in the source is read
   ambiguously.

Two short details should also be supplied in a final proof: eventual strict
monotonicity of `rho_m`, and a uniform `O(2^m)` upper bound on all noncentral
rank slacks when proving that the middle rank eventually maximizes `B(2m)`.
Both details are elementary and are proved below.

The result is useful but does not prove or disprove `nu(k)=B(k)`.  At `k=11`
it guarantees only a 93-window full-depth core.  At `k=14` it guarantees the
already known 3040-window fixed-delay core and strengthens that conclusion by
showing full recency depth at at least 3040 selected endpoints.

## 1. Setup and the standard interval band

Fix a rank `r`, put

\[
 M=\binom{k}{r},\qquad n=M+d,\qquad
 L=\sum_{s=1}^{r-1}\binom{k}{s},
\]

and

\[
 \sigma=dM+\binom{d+1}{2}-L.                    \tag{1.1}
\]

Choose one interval for every rank-`r` target.  Equal-rank targets are
incomparable, so the selected intervals are pairwise nonnested.  Their left
and right endpoints are consequently both distinct and occur in the same
order.  The usual order-statistic argument gives

\[
 I_i\subseteq[i,i+d]                              \tag{1.2}
\]

after ordering by left endpoint.  In particular, every selected rank-`r`
witness has length at most `d+1`, and every lower-rank target has a witness of
length at most `d`.

Choose one such short witness for each of the `L` lower targets.  The proof
below works for every such choice; it does not require a specially optimized
lower-witness assignment.

## 2. Audit of the right-endpoint defect inequality

Let `E_R` be the set of right endpoints of the selected rank-`r` intervals.
There are exactly `M` such endpoints.  For `b in E_R`, write the unique
selected central interval as

\[
 I_b=[a,b].
\]

At endpoint `b`, order the nonempty last-occurrence blocks from most recent
to oldest.  Let `j_b` be the number of blocks whose prefix union is the
rank-`r` value of `I_b`.  Finally put

\[
 c_b^R=\min(d,b).
\]

Let `q_b^R` be the number of chosen lower witnesses ending at `b`.  If
`b notin E_R`, the physical short-interval capacity gives simply

\[
 q_b^R\le c_b^R.                                 \tag{2.1}
\]

If `b in E_R`, a lower witness ending at `b` cannot begin before `a`, because
it would contain `I_b` and hence have rank at least `r`.  It cannot begin at
`a`, because that interval has the selected rank-`r` value.  It must therefore
be a proper suffix of `I_b`.

The distinct suffix unions ending at `b` are precisely the prefix unions of
the last-occurrence blocks.  Values strictly below the prefix union at depth
`j_b` occur at only the first `j_b-1` depths.  Hence

\[
 q_b^R\le j_b-1.                                 \tag{2.2}
\]

There is no hidden assumption here that the chosen central interval is a
minimal witness.  A redundant proper suffix may still have the same
rank-`r` value, but it cannot be one of the selected lower targets and so does
not increase (2.2).

Moreover,

\[
 j_b\le |I_b|\le d+1,
\]

because every last-occurrence block contributing to `I_b` has a distinct
last-occurrence position inside that interval.  If `b<=d`, the stronger
bound `j_b<=|I_b|<=b` holds.  Therefore

\[
 j_b-1\le c_b^R,                                 \tag{2.3}
\]

so all endpoint defects below are nonnegative.

Now

\[
 \sum_{b=1}^{M+d}c_b^R
   =dM+\binom{d+1}{2}=L+\sigma.                  \tag{2.4}
\]

Summing (2.1)--(2.2) and using `sum_b q_b^R=L` gives exactly

\[
 \boxed{
 \sum_{b\in E_R}\bigl(c_b^R-(j_b-1)\bigr)\le\sigma.
 }                                                \tag{2.5}
\]

Thus Theorem 1 in the proposed argument is correct.

### Zero-defect characterization

If `b<=d`, then

\[
 c_b^R-(j_b-1)\ge b-(b-1)=1.
\]

If `b>=d+1`, zero defect is equivalent to `j_b=d+1`.  The bounds
`j_b<=|I_b|<=d+1` then force

\[
 |I_b|=d+1,\qquad I_b=[b-d,b].                   \tag{2.6}
\]

Consequently at least `[M-sigma]_+` selected rank-`r` intervals have maximum
physical length and maximum last-occurrence depth.  When `sigma<=M`, this is
the stated `M-sigma` conclusion.

## 3. Symmetric left-endpoint saturation

There is a completely symmetric theorem which is useful to record
explicitly.

Let `E_L` be the selected rank-`r` left endpoints.  For `a in E_L`, let
`f_a` be the number of distinct first-occurrence blocks, read from left to
right, needed to reach the chosen rank-`r` target.  Put

\[
 c_a^L=\min(d,n-a+1).
\]

Grouping the same chosen lower witnesses by left endpoint gives

\[
 \boxed{
 \sum_{a\in E_L}\bigl(c_a^L-(f_a-1)\bigr)\le\sigma.
 }                                                \tag{3.1}
\]

Indeed, every lower witness beginning at a selected central left endpoint
must be a proper prefix of that central interval, and there are at most
`f_a-1` strict prefix-union values below it.  The total left short-cell
capacity is again `L+sigma`.

A zero left defect occurs exactly when

\[
 a\le n-d,qquad f_a=d+1,qquad I_a=[a,a+d].      \tag{3.2}
\]

Intersecting the right-zero and left-zero families on the common set of `M`
selected rank-`r` intervals yields:

\[
 \boxed{
 \text{at least }[M-2\sigma]_+
 \text{ witnesses have both full first- and full last-occurrence depth.}
 }                                                \tag{3.3}

For such a window every one of its `d+1` positions is the first occurrence,
within the window, of some target coordinate and the last occurrence, within
the window, of some (possibly different) target coordinate.

This does **not** force Johnson adjacency between consecutive central masks.
For example, with `d=1`, three pairwise disjoint nonempty blocks
`A_1,A_2,A_3` make both windows `[1,2]` and `[2,3]` full at both ends, while
the number of coordinates exchanged between their OR values is
`|A_1|=|A_3|`, which can be arbitrarily large.  The only immediate rank
obstruction is the already one-sided condition

\[
 r\ge d+1                                           \tag{3.4}
\]

whenever at least one zero-defect endpoint exists.

For `k=11`, (3.3) is vacuous because `M-2 sigma<0`.  For `k=14` it gives
`3432-2*392=2648` central witnesses with both depths full.

## 4. Contiguity of the maximum-length core

Order the selected rank-`r` intervals by left endpoint and write

\[
 I_i=[i+\alpha_i,i+\beta_i].
\]

The endpoint order gives

\[
 0\le\alpha_1\le\cdots\le\alpha_M\le d,
 \qquad
 0\le\beta_1\le\cdots\le\beta_M\le d,
 \qquad \alpha_i\le\beta_i.                     \tag{4.1}
\]

Length `d+1` is possible only at the state

\[
 (\alpha_i,\beta_i)=(0,d).                       \tag{4.2}
\]

The indices with `alpha_i=0` form an initial segment and those with
`beta_i=d` form a final segment.  Their intersection is therefore one
contiguous interval of indices.  By (2.5)--(2.6), it contains at least
`[M-sigma]_+` distinct rank-`r` masks.  Hence the claimed contiguous
fixed-delay core is correct.

Notice the exact novelty: the core-size statement was already obtainable
from the short-cell defect count, but (2.5) additionally proves full
last-occurrence depth at at least `M-sigma` selected endpoints.

## 5. Audit of the rank-deficit inequality

For the chosen lower witnesses let

\[
 D(k,r)=\sum_{s=1}^{r-1}(r-s)\binom{k}{s}.        \tag{5.1}
\]

At a fixed right endpoint, the `q_b^R` selected values form a strict
inclusion chain below rank `r`.  Their positive rank deficits are distinct
integers, so their sum is at least

\[
 1+\cdots+q_b^R=\binom{q_b^R+1}{2}.              \tag{5.2}
\]

Let `e_b=c_b^R-q_b^R`.  Then `e_b>=0` and

\[
 \sum_b e_b=\sigma.                              \tag{5.3}
\]

For `0<=q<=c<=d`,

\[
 \binom{c+1}{2}-\binom{q+1}{2}
   =\sum_{u=q+1}^{c}u\le d(c-q).                 \tag{5.4}
\]

Finally, the hockey-stick identity gives

\[
 \begin{aligned}
 \sum_{b=1}^{M+d}\binom{c_b^R+1}{2}
  &=M\binom{d+1}{2}+\sum_{u=1}^{d}\binom{u+1}{2}\\
  &=(M+1)\binom{d+1}{2}+\binom{d+1}{3}.
 \end{aligned}                                  \tag{5.5}
\]

Equations (5.2)--(5.5) prove

\[
 \boxed{
 D(k,r)\ge
 (M+1)\binom{d+1}{2}+\binom{d+1}{3}-d\sigma.
 }                                                \tag{5.6}
\]

Thus Theorem 3 is correct.  Calling it a “second-moment” strengthening is
descriptive rather than literal; it is a convex endpoint-chain/rank-deficit
bound.

For the two finite cases emphasized in the project:

* `k=11,r=6,d=3`: `D=1892`, while the right side is `1675`.
* `k=14,r=7,d=2`: `D=12005`, while the right side is `9516`.

So it gives no contradiction in either case.

## 6. Exact two-sided rank-depth refinement

The left and right chain information can be combined, but not by adding two
copies of (5.6) to one copy of `D`.

For an occupied lower-witness cell `x=[a,b]`, define

* `h_R(x)` to be the number of occupied cells `[a',b]` with `a'<=a`;
* `h_L(x)` to be the number of occupied cells `[a,b']` with `b'>=b`.

Every cell counted by `h_R(x)` is a same-right-endpoint interval containing
`x`; its target is a strict superset of the target at `x`.  All targets still
have rank below `r`.  Therefore the deficit of the label at `x` is at least
`h_R(x)`.  The same argument gives a lower bound `h_L(x)`.  Hence the exact
two-sided necessary condition is

\[
 \boxed{
 D(k,r)\ge\sum_{x\text{ occupied}}
             \max\{h_L(x),h_R(x)\}.
 }                                                \tag{6.1}
\]

This is a genuine data-dependent strengthening of either one-sided chain
bound.  It does not, by itself, give a new leading-order obstruction.

To make that limitation explicit, suppose `n` is large enough that the two
boundary triangles do not overlap.  In the complete `d`-band, a cell of
length `ell` has

\[
 \max(h_L,h_R)=d-\ell+1.
\]

Thus the complete-band value of the right side is

\[
 F_{n,d}=\sum_{\ell=1}^{d}(n-\ell+1)(d-\ell+1)
        =M\binom{d+1}{2}+\sum_{u=1}^{d}u^2.       \tag{6.2}
\]

It exceeds the one-sided baseline (5.5) by only

\[
 \binom{d+1}{3}.                                 \tag{6.3}
\]

Deleting one band cell decreases the functional in (6.1) by at most
`3d-2`: at most `d` for the removed cell and at most one for each of at most
`2d-2` other cells in its row and column.  Consequently the coarse scalar
corollary

\[
 D(k,r)\ge F_{n,d}-(3d-2)\sigma                  \tag{6.4}
\]

is valid.  Compared with (5.6), however, it is stronger only when

\[
 \binom{d+1}{3}>(2d-2)\sigma.                    \tag{6.5}
\]

That fails badly at `k=11` and `k=14`, and the guaranteed
`sigma=O(W/\sqrt{k})` on the infinite subsequence is still exponentially
larger than the polynomial bonus in (6.3).  A useful stronger obstruction
would therefore need actual information about the hole geometry or the pin
labels, not just left-right symmetry.

## 7. Audit of the central asymptotics

Take `k=2m`, `r=m`, and write

\[
 W_m=\binom{2m}{m}.
\]

Symmetry of the binomial coefficients gives exactly

\[
 L_m=\sum_{s=1}^{m-1}\binom{2m}{s}
    =\frac{4^m-W_m}{2}-1.                        \tag{7.1}
\]

Therefore

\[
 \rho_m:=\frac{L_m}{W_m}
 =\frac{4^m}{2W_m}-\frac12-\frac1{W_m}.          \tag{7.2}
\]

The standard central-binomial expansion

\[
 W_m=\frac{4^m}{\sqrt{\pi m}}
      \left(1-\frac1{8m}+\frac1{128m^2}
      +O(m^{-3})\right)
\]

then gives

\[
 \boxed{
 \rho_m=rac{\sqrt{\pi}}2\sqrt m-rac12
       +\frac{\sqrt\pi}{16\sqrt m}+O(m^{-3/2}).
 }                                                \tag{7.3}
\]

In particular,

\[
 \rho_{m+1}-\rho_m
   =\frac{\sqrt\pi}{4\sqrt m}+O(m^{-3/2})>0      \tag{7.4}
\]

for all sufficiently large `m`.  This supplies the monotonicity omitted in
the proposed proof.

Let `d_m` be the least integer satisfying

\[
 L_m\le d_mW_m+\binom{d_m+1}{2}.                 \tag{7.5}
\]

For each sufficiently large integer `q`, choose

\[
 m(q)=\max\{m:\rho_m<q\}.
\]

Then (7.4) implies

\[
 0<q-\rho_{m(q)}
   \le\rho_{m(q)+1}-\rho_{m(q)}=O(m^{-1/2}).     \tag{7.6}
\]

The value `d=q` is feasible in (7.5).  The value `q-1` is not feasible for
large `q`, because

\[
 \rho_m-\left(q-1+\frac{\binom q2}{W_m}\right)
  =1-O(m^{-1/2})-O(m/W_m)>0.                     \tag{7.7}
\]

Therefore `d_m=q`, and

\[
 \frac{\sigma_m}{W_m}
  =d_m-\rho_m+\frac{\binom{d_m+1}{2}}{W_m}
  =O(m^{-1/2}).                                  \tag{7.8}
\]

This proves the claimed infinite subsequence rigorously.

## 8. Why the middle rank really maximizes `B(2m)` eventually

For every noncentral rank `r`,

\[
 \binom{2m}{r}\le\binom{2m}{m-1}
 =W_m-\frac{W_m}{m+1}.                           \tag{8.1}
\]

For any rank, the quadratic term alone shows

\[
 \tau(2m,r)\le \left\lceil\sqrt{2L(2m,r)}\right\rceil
             =O(2^m),                            \tag{8.2}
\]

uniformly in `r`, because `L(2m,r)<4^m`.  On the other hand,

\[
 \frac{W_m}{m+1}=\Theta\!\left(\frac{4^m}{m^{3/2}}\right)
 \gg 2^m.                                       \tag{8.3}
\]

The middle-rank candidate is at least `W_m`; (8.1)--(8.3) show that every
other rank gives a strictly smaller value for all sufficiently large `m`.
Thus the middle rank is indeed the unique maximizer of `B(2m)` eventually.

Combining this fact with (2.5), (4.2), and (7.8) proves the conditional
near-perfect-core statement:

\[
 \text{core size}
   \ge W_m-O(W_m/\sqrt m)
   =(1-O(k^{-1/2}))W(k),                         \tag{8.4}
\]

with common delay

\[
 d\sim\frac{\sqrt\pi}{2}\sqrt m
       =\sqrt{\frac{\pi k}{8}}.                 \tag{8.5}
\]

The same `O(W(k)/sqrt(k))` quantity bounds the number of spare short cells
and the number of selected middle endpoints not proved to have full recency
depth.  By the symmetric refinement, at most twice that many witnesses fail
the simultaneous first-and-last-depth conclusion.

## 9. Finite significance and scope

The exact finite numbers are:

| case | `M` | `d` | `sigma` | guaranteed full-length/full-last-depth core | guaranteed both-depth core |
|---|---:|---:|---:|---:|---:|
| `k=11,r=6` | 462 | 3 | 369 | 93 | 0 |
| `k=14,r=7` | 3432 | 2 | 392 | 3040 | 2648 |

For `k=11`, this theorem does not explain or solve the difficult 369-window
short block of the canonical single-switch schedule.  For `k=14`, the core
size agrees with the earlier unrestricted forced-triple-core theorem; the
new information is full last-occurrence depth on at least those many selected
endpoints.

The asymptotic theorem is a meaningful rigidity statement: on infinitely
many even dimensions, equality forces an almost full fixed-delay growth
diagram.  It is still conditional on equality and supplies neither the
central ordering, the upper union shadows, nor coordinate pin survival.  The
rank-deficit inequalities leave a constant-factor margin, and the symmetric
endpoint theorem alone creates no Johnson-transition condition.  A proof or
disproof of the all-`k` conjecture still needs genuinely two-dimensional hole
geometry, interval-growth recurrence, or pinning information.

