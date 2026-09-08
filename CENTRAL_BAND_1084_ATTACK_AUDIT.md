# Independent-style audit of `CENTRAL_BAND_1084_ATTACK.md`

## Verdict

The fixed-frame trace obstruction is correct with the scope stated in the
note.  It is a theorem about a middle-row architecture: one fixed coordinate
matching, cellwise contiguous blocks, `o(W/sqrt(m))` seams, and literal repair
of omitted shadows.  It is not a lower bound for arbitrary OR words or for
sector-dependent quartet frames.

The limiting deficit is

\[
 \delta(c)=e^{-c^2}\Phi(c/2)-\Phi(-3c/2),
\]

and its maximum on `[0,2]` is

\[
 \delta_*=0.247141309562647\ldots
\]

at `c=0.613426084927899...`.  Therefore the scoped architecture costs at
least `(1.247141309562646-o(1))W`, strictly above the requested
`1.084380949299413W` coefficient.

## 1. Exact type counts

For `m` matching pairs, a middle set with `g` full pairs must have `g` empty
pairs and `m-2g` split pairs.  Choosing the three pair classes and orienting
the split pairs gives

\[
 V_g=\frac{m!}{g!^2(m-2g)!}2^{m-2g}.
\]

A rank-`m-q` target with `f` full pairs has `f+q` empty pairs and
`m-2f-q` split pairs, giving

\[
 T_{f,q}=\frac{m!}{f!(f+q)!(m-2f-q)!}2^{m-2f-q}.
\]

The checker sums these integers exactly to `binom(2m,m)` and
`binom(2m,m-q)` respectively.  No independence assumption enters.

## 2. Capacity inequality

Inside one fixed-pair cell, full pairs occur in every vertex, empty pairs in
none, and split pairs in one orientation.  The intersection of any family of
cell vertices therefore has exactly the cell's fixed full pairs.  Thus every
internal depth-`q` shadow has the type of its starting middle slot.

With `R_g` repeated slots of type `g`, distinct targets of that type number
at most `min(T_{g,q},V_g+R_g)`.  Moving the repeats inside the minimum can
increase total coverage by at most `sum R_g=R`.  Only `q` starts on each side
of a block boundary can produce a crossing `(q+1)`-window, so the displayed
loss `qb` is generous.  This proves

\[
 M_q\ge N_q-\sum_g\min(T_{g,q},V_g)-R-qb.
\]

For one block per fixed-pair cell, `b<=3^m`; for wreath-scale blocks,
`b=O(W/m)`.  Either gives `qb=o(W)` at `q=O(sqrt(m))`.

## 3. Gaussian overlap calculation

For a uniformly random `k`-set, the number of full matching pairs has mean

\[
 \frac{k(k-1)}{2(2m-1)}
\]

and variance `(1/16+o(1))m` uniformly for `k=m-O(sqrt(m))`.  At
`q=c sqrt(m)`, the middle and lower-target means differ by
`(c/2+o(1))sqrt(m)`, while `N_q/W -> e^{-c^2}`.

In units `x sqrt(m)` relative to the target mean, the two local-limit
densities are

\[
 e^{-8(x-c/2)^2}quad\hbox{and}\quad
 e^{-c^2}e^{-8x^2}.
\]

They cross at `x=c/8`.  The unmatched target mass is therefore

\[
 e^{-c^2}\Phi(4(c/8))
 -\Phi(4(c/8-c/2))
 =e^{-c^2}\Phi(c/2)-\Phi(-3c/2).
\]

The exact finite sums in the checker converge to this expression.  For
example, near the maximizing scale their normalized deficits are
`0.23844, 0.24045, 0.24259, 0.24386` at `m=100,200,400,800`, approaching
`0.2471413`.

## 4. Optimization and repair accounting

Differentiating gives

\[
 \delta'(c)=e^{-c^2}
 [-2c\Phi(c/2)+\tfrac12\phi(c/2)]
 +\tfrac32\phi(3c/2).
\]

Bisection of its sign change, independently compared with a dense scan,
gives the stated optimizer and value.  The less optimized point `c=1`
already has `delta(1)=0.1875676226`, so the separation from `0.0843809493`
does not depend on delicate numerical optimization.

If `R` repeats are inserted, they can remove at most `R` holes at a fixed
depth.  Literal insertion of every remaining hole costs the remainder.
Thus repeats plus repairs cost at least `delta(c)W-o(W)`, proving the
coefficient floor.

If the total repeat-and-repair budget is the target
`epsilon_0 W=0.0843809493W`, the only remaining term in the exact capacity
inequality is the seam credit `qb`.  Maximizing the required seam density
over the available depths gives

\[
 b\ge\max_{0<c\le2}\frac{\delta(c)-\epsilon_0}{c}
        \frac W{\sqrt m}
   =(0.341806889960-o(1))\frac W{\sqrt m}.
\]

The maximum occurs at `c=0.350485...`.  Thus the claimed mesoscopic
switching toll follows directly; it is not an extra probabilistic heuristic.
Its reciprocal is `2.92563`: frozen pair-flip blocks longer than
`4sqrt(m)`, as required for depth-`2sqrt(m)` geodesicity, cannot provide
enough seams.

## 5. Fixed-depth and quartet audits

At `J=2sqrt(m)`, the Gaussian rank sum is

\[
 \sum_{q=1}^J\binom{2m}{m-q}/W
 =(\tfrac{\sqrt\pi}{2}\operatorname{erf}(2)+o(1))\sqrt m.
\]

Hence a proportionally decorated block has edge size
`(sqrt(pi) erf(2)+o(1))R sqrt(m)`.  Since local geodesicity requires
`R>4sqrt(m)`, this is greater than `7.05m+o(m)`.  A middle vertex and one
fixed facet have conditional co-occurrence at least `2/m`.  The product of
edge size and relative codegree stays bounded away from zero.  This verifies
that the fixed-uniformity matching theorem used in the fixed-depth proof has
not been made uniform merely by changing parameters.  It does not prove
nonexistence of a special matching.

For a `d`-cube, the ratio of all depth-`q` faces to the windows of one cyclic
trace is `binom(d,q)/2^q`.  At `d~m/2`, `q~sqrt(m)`, its logarithm is
`(1/2+o(1))q log m`.  Thus a polynomial per-cell catalog is insufficient for
cellwise face routing.  Cross-cell reassignment is deliberately outside that
claim.

## 6. Reproducibility

Run

```text
python3 scratch/check_central_band_1084.py
```

The script verifies the exact type totals, exact finite overlap deficits,
Gaussian constants, optimizer, comparison with `1.0843809493`, and the
exponential negligibility of fixed-cell seams.

The theorem leaves the correct live escape routes: positive-density frame
diffusion, positive-density cross-cell windows, or a genuinely growing
vertically complete middle trace.
