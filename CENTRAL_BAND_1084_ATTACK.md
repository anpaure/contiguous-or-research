# Attack on the `Gamma(2)<1.0843809493` central-band target

## 0. Verdict

Put

\[
 W_m=\binom{2m}{m},\qquad
 H=\lfloor2\sqrt m\rfloor.
\]

No construction currently in the handoff proves

\[
 \Gamma(2)<1.084380949299413.
\]

The fixed-depth, partial-block, quartet, and wreath results do not become
uniform at depth `H` by substituting `J=H` into their proofs.  The failure is
not only one of presentation.  This note proves a new quantitative
obstruction to the most tempting such substitution.

> **Fixed-frame trace obstruction.**  A cellwise middle-row construction
> based on one fixed perfect matching, even with repeated middle states and
> optimal literal repair, has asymptotic coefficient at least
> 
> \[
>  1+\delta_* = 1.247141309562646\ldots,
> \]
> 
> for the band `|r-m|<=2sqrt(m)`.  Here
> 
> \[
>  \delta_*=max_{0\le c\le2}
>  \left[e^{-c^2}\Phi(c/2)-\Phi(-3c/2)\right]
>  =0.247141309562647\ldots .
> \]

Here `Phi` and `phi` denote the standard normal distribution function and
density.

Thus constant-frame quartet cells, fixed-pair cube traces, and any literal
repair of them cannot reach the new `1.08438` target.  Pairing diffusion is
not optional: a successful construction must change its coordinate frame on
a positive-density set of sources or use genuinely cross-cell windows.

This is a scoped no-go theorem, not a lower bound for arbitrary OR words.
Sector-dependent quartet frames, nonlocal wreath switches, and a genuinely
growing vertically complete factor remain live.

## 1. The exact fixed-pair type distributions

Fix a perfect matching `P` of the `2m` coordinates.  For a set `S`, let

\[
 F(S)=\#\{e\in P:e\subseteq S\}
\]

be its number of full matching pairs.

The number of middle `m`-sets with type `g` is

\[
 V_g=\frac{m!}{g!^2(m-2g)!}\,2^{m-2g}.                 \tag{1.1}
\]

Indeed there are `g` full pairs, `g` empty pairs, and `m-2g` split pairs.
The number of rank-`m-q` sets with type `f` is

\[
 T_{f,q}=\frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.    \tag{1.2}
\]

Here there are `f` full pairs, `f+q` empty pairs, and `m-2f-q` split pairs.
Consequently

\[
 \sum_gV_g=W_m,
 \qquad
 \sum_fT_{f,q}=N_q:=\binom{2m}{m-q}.                \tag{1.3}
\]

These are exact identities.

## 2. What one fixed frame can expose

A `P`-cell is obtained by declaring every matching pair full, empty, or
split and allowing the orientations of the split pairs to vary.  Every
middle vertex in one cell has the same full-pair type.

Let a middle row be divided into `b_m` contiguous cell blocks.  Assume that
the row contains every middle set once and `R_m` additional repeated middle
states.  For a depth `q`, inspect the usual consecutive shadow windows

\[
 L_i^{(q)}=T_i\cap T_{i+1}\cap\cdots\cap T_{i+q}.     \tag{2.1}
\]

If (2.1) lies inside one `P`-cell block, then

\[
 F(L_i^{(q)})=F(T_i).                                \tag{2.2}
\]

All fixed full pairs survive the intersection; an oriented split pair can
never become full under intersection.  Notice that (2.2) does not require
the block order to be a cube-edge path.

Write `R_g` for the number of repeated row positions of type `g`.  There
are at most `V_g+R_g` internal starting slots of type `g`, so they can expose
at most

\[
 \min(T_{g,q},V_g+R_g)
\]

different rank-`m-q` targets of that type.  At most `qb_m` windows cross a
block boundary.  Hence the number `M_q` of missing lower targets satisfies

\[
 \boxed{
 M_q\ge
 N_q-\sum_g\min(T_{g,q},V_g)-R_m-qb_m.
 }                                                     \tag{2.3}
\]

The same bound holds above the middle by complementation.

For the natural cellwise architectures, `b_m=o(W_m/sqrt(m))`.  A traversal
using one block per fixed-pair cell has at most `3^m` blocks, and

\[
 \sqrt m\,3^m/W_m\longrightarrow0
\]

exponentially.  A wreath-scale factor has only `O(W_m/m)` components.  Thus
the boundary term in (2.3) is `o(W_m)` uniformly for `q=O(sqrt(m))`.

## 3. Gaussian evaluation of the lost capacity

Let

\[
 q=\lfloor c\sqrt m\rfloor
\]

for fixed `c>0`.  Both type distributions have variance
`(1/16+o(1))m`, while their means differ by

\[
 \frac{\mathbb E F(X_m)-\mathbb E F(X_{m-q})}{\sqrt m}
 \longrightarrow \frac c2.                           \tag{3.1}
\]

The local central limit theorem gives, uniformly for bounded `x`,

\[
 \begin{aligned}
 \frac{V_{\lfloor\mu_m+x\sqrt m\rfloor}}{W_m}
   &=\frac4{\sqrt{2\pi m}}e^{-8x^2}(1+o(1)),\\
 \frac{T_{\lfloor\mu_{m-q}+x\sqrt m\rfloor,q}}{N_q}
   &=\frac4{\sqrt{2\pi m}}e^{-8x^2}(1+o(1)),\\
 \frac{N_q}{W_m}&\longrightarrow e^{-c^2}.
 \end{aligned}                                       \tag{3.2}
\]

Use `x` relative to the lower-target mean.  The limiting middle density and
target density cross where

\[
 e^{-8(x-c/2)^2}=e^{-c^2}e^{-8x^2},
 \qquad x=c/8.                                       \tag{3.3}
\]

Below that threshold there are more targets than compatible middle slots.
Integrating the positive difference gives

\[
 \begin{aligned}
 \delta(c)
 &:=\lim_{m\to\infty}
 \frac{N_q-\sum_g\min(T_{g,q},V_g)}{W_m}\\
 &=e^{-c^2}\Phi(c/2)-\Phi(-3c/2).                   \tag{3.4}
 \end{aligned}
\]

The tails outside the uniform local-limit window are handled by the usual
Gaussian bound, so (3.4) is a limit of the complete exact sums, not only a
formal density comparison.

Differentiation gives

\[
 \delta'(c)=e^{-c^2}
 \left[-2c\Phi(c/2)+\tfrac12\phi(c/2)\right]
 +\tfrac32\phi(3c/2).                                \tag{3.5}
\]

Its unique maximizer on `[0,2]` is

\[
 c_*=0.613426084927899\ldots,
 \qquad
 \delta(c_*)=0.247141309562647\ldots .              \tag{3.6}
\]

The coarser single value `c=1` already gives

\[
 \delta(1)=e^{-1}\Phi(1/2)-\Phi(-3/2)
           =0.187567622575656\ldots,                 \tag{3.7}
\]

well above the available overhead `0.0843809493`.

## 4. Repeats and literal repairs cannot beat the constant

Suppose `R_m=epsilon_m W_m` repeated middle positions are inserted into the
cellwise trace.  Equation (2.3) and (3.4) give

\[
 M_q\ge(\delta(c)-\epsilon_m-o(1))W_m.              \tag{4.1}
\]

If every remaining missing mask is appended literally, the combined repeat
and repair cost is at least

\[
 R_m+M_q\ge(\delta(c)-o(1))W_m,                     \tag{4.2}
\]

unless `R_m` already exceeds that amount, in which case the same lower bound
is immediate.  Optimizing `c` proves

\[
 \boxed{
 L_{\rm fixed\ frame+literal}
 \ge(1.247141309562646-o(1))W_m.
 }                                                     \tag{4.3}
\]

This is more than the requested `1.0843809493`.  It also explains exactly
why the abstract quartet face resolver does not help a constant frame: every
target is available somewhere as a cube face, but the ordered trace has the
wrong full-pair type capacity.

There is also a quantitative escape toll.  Let

\[
 \epsilon_0=0.084380949299413\ldots
\]

be the entire overhead permitted by the proposed central-band coefficient.
If repeats plus literal repairs use at most `epsilon_0 W_m`, then (2.3) at
any fixed `c` forces

\[
 q b_m\ge(\delta(c)-\epsilon_0-o(1))W_m.
\]

Optimizing `(delta(c)-epsilon_0)/c` gives

\[
 c_{\rm seam}=0.350485\ldots .
\]

Thus any fixed-frame construction which hopes to escape through seams must
have

\[
 \boxed{
 b_m\ge(0.341806889960-o(1))\frac{W_m}{\sqrt m}.
 }                                                     \tag{4.4}
\]

Equivalently its average cellwise block length is at most about
`2.92563sqrt(m)`.  Wreath-scale blocks of length `Theta(m)` have too few
seams by a factor `Theta(sqrt(m))`.  This does not forbid deliberate
`Theta(W_m/sqrt(m))` frame changes; it proves that such mesoscopic switching
is necessary within this architecture.

There is a useful exact comparison with the partial-block method.  A cyclic
pair-flip block geodesic through `H=2sqrt(m)` has length strictly greater
than `4sqrt(m)`.  Even the shortest such frozen-frame blocks are therefore
too long to supply the seam density (4.4), before any matching or
factorization loss is counted.

## 5. Why the fixed-depth block proof is not uniform at `2sqrt(m)`

The fixed-depth theorem packages a cyclic pair-flip block of `R=2ell`
middle states together with all lower and upper shadows through depth `J`,
where `ell>J` is fixed before `m` tends to infinity.

At the present scale `J=2sqrt(m)`, balanced target occupancy forces one
decorated block to carry asymptotically

\[
 \begin{aligned}
 r_m
 &\ge R\left(1+2\sum_{q=1}^{J}\frac{N_q}{W_m}\right)\\
 &=(\sqrt\pi\,\operatorname{erf}(2)+o(1))R\sqrt m.
                                                               \tag{5.1}
 \end{aligned}
\]

Since `R>4sqrt(m)`, this is linear in `m` (indeed larger than
`7.05m+o(m)`).  Moreover, conditioned on a block containing a middle vertex
`X`, its two adjacent first shadows are two of the `m` facets of `X`.
Symmetry therefore gives a middle/facet relative codegree at least

\[
 \frac2m.                                             \tag{5.2}
\]

Thus the growing edge size and codegree sit at the projective-plane scale

\[
 r_m\frac{\Delta_2}{D}=\Theta(1),                   \tag{5.3}
\]

not in a regime obtained by making the fixed-uniformity
Pippenger--Frankl--Rodl proof quantitative.  Equations (5.1)--(5.3) do not
prove that the desired matching is false; they prove that the existing
fixed-`J` black box supplies no uniform theorem at this depth.  The
middle-only partial-block hypergraph avoids (5.2), but adding the tracked
shadow classes restores it, and shift closure remains unproved.

## 6. Quartet catalogs: faces are plentiful, ordered traces are not

The integral quartet resolver proves that every target is an abstract face
of some selected cell.  For one physical `d`-cube, however, the number of
lower depth-`q` faces is

\[
 \binom dq2^{d-q},
\]

whereas one cyclic order has only `2^d` starting windows.  Covering all local
faces by local cycles needs at least

\[
 \frac{\binom dq}{2^q}                              \tag{6.1}
\]

traces.  At the typical quartet-cell dimension `d=(1/2+o(1))m` and
`q=Theta(sqrt(m))`,

\[
 \log\frac{\binom dq}{2^q}
   =\left(\frac12+o(1)\right)q\log m.               \tag{6.2}
\]

Hence a constant or polynomial local catalog cannot turn abstract face
resolution into cellwise window resolution.  This is again scoped: a target
may be rerouted to a different cell, and sector-dependent frames can mix the
type statistic.  What (6.2) rules out is the direct strategy “resolve every
face, then choose a few cycle orders per cell.”

## 7. What remains genuinely capable of reaching `1.08438`

The audit leaves three live mechanisms.

1. **A growing vertically complete middle trace.**  One row of
   `W_m+o(W_m)` middle states whose consecutive intersections and unions are
   complete through `2sqrt(m)`, together with the run condition, would prove
   `Gamma(2)<=1`.
2. **Positive-density frame diffusion.**  The frame must vary with the
   source strongly enough to destroy the fixed statistic `F`; the quartet
   sector choices and balanced wreath switches provide finite evidence but
   no all-dimensional routing theorem.
3. **Cross-cell reuse.**  Windows crossing a positive-density family of cell
   boundaries could evade (2.2), but then they must be designed as part of
   one nonlocal braid.  Merely concatenating cell gadgets leaves only
   `o(W_m)` such windows and is covered by the theorem.

The `Q_9` fully vertical and optimally balanced wreath factors show that the
ordered requirement is finite-combinatorially consistent.  The failed rigid
`Q_9 -> Q_11` insertion and the exact fixed-frame bound (4.3) show why a
literal product or frozen-frame induction is insufficient.

The new conclusion is therefore sharper than “the central band is open”:

> Any proof of `Gamma(2)<1.0843809493` must use positive-density frame
> changes or positive-density cross-cell routing.  Fixed-frame cell traces,
> even optimally repeated and repaired, are quantitatively separated from
> the target by at least `0.16276036 W_m`.

The exact arithmetic and limiting constants are checked by
`scratch/check_central_band_1084.py`.
