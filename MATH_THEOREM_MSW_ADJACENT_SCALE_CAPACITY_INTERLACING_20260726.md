# Exact Catalan capacity interlacing for the recursive MSW parent trades

Date: 2026-07-26

## 0. Outcome

The Catalan jump `Cat_r/Cat_(r-1)~4` creates a genuine obstruction for
one fixed parent scale: depending on where the cap `p` lies between two
successive Catalan numbers, the certified plateau demand is between one
and `7/4+o(1)` times that scale's entire four-arm capacity.  Varying to
one neighboring scale does not remove a constant overshoot.

Two adjacent scales have enough **raw scalar capacity in every case**.
More precisely, if `r` is minimal with `Cat_r>=4p`, then the union of the
scale-`r` and scale-`r+1` catalogues contains strictly more switches than
one quarter of the certified cap tail.  Therefore an arbitrary subcatalogue
can be cardinality-tuned so that

\[
 4L\le K_{q,p}(F_{MSW})-(W-N_q)                          \tag{0.1}
\]

simultaneously throughout the whole phase-critical window
`q<=O(p^(1/4))`.  For that tuned count, the aggregate scalar saturation
defect is identically zero.

This settles the **arithmetic** overshoot/undershoot audit.  It does not
construct a joint exact Boolean cube from two scales.  The same-scale cube
theorem uses disjoint equal-size recursion slabs; adjacent-size slabs can
be nested, and no cross-scale commutation theorem is presently proved.
Thus the remaining interlacing gate is physical compatibility, not
Catalan constants.

---

## 1. Exact demand and one-scale supply

Put

\[
 H_{m,r}={1\over2}\binom{2(m-r)}{m-r},\qquad
 d_r=\operatorname {Cat}_r,                              \tag{1.1}
\]

and let

\[
 M_r=H_{m,r+1}\operatorname {Cat}_{r-1}                 \tag{1.2}
\]

be the number of elementary switches in the literal scale-`r` parent
family.  The growing-cutoff boundary theorem gives, for every `q>=r`,

\[
 K_{q,p}(F_{MSW})ge
 D_r:=H_{m,r}(d_r/2-p)                                   \tag{1.3}
\]

whenever `d_r>=4p`.

The exact capacity ratio is

\[
 \rho_{m,r}:={M_r\over H_{m,r}d_r}
 ={(m-r)(r+1)\over
   4(2(m-r)-1)(2r-1)}.                                  \tag{1.4}
\]

Write `t=d_r/p`.  The fraction of the entire scale-`r` catalogue needed
to match the certified demand is

\[
\boxed{
 a_{m,r}(t):={D_r\over4M_r}
 ={1/2-1/t\over4\rho_{m,r}}.}                           \tag{1.5}
\]

Since both factors in (1.4) exceed their limiting halves,

\[
                         \rho_{m,r}>{1\over16}.          \tag{1.6}
\]

Minimality of `r` gives

\[
                         4\le t<16.                      \tag{1.7}
\]

Consequently

\[
\boxed{
 {1\over16\rho_{m,r}}
 \le a_{m,r}(t)
 <{7\over64\rho_{m,r}}<{7\over4}.}                     \tag{1.8}
\]

The lower endpoint is slightly below one because `rho_(m,r)>1/16`.
The exact one-scale feasibility threshold is

\[
\boxed{
 t\le t^*_{m,r}:={1\over1/2-4\rho_{m,r}}.}              \tag{1.9}
\]

For `r=o(m)`,

\[
 t^*_{m,r}=4+{6\over r}
             +O(r^{-2}+r/m).                            \tag{1.10}
\]

Thus one scale works only when the Catalan overshoot above `4p` is within
relative `O(1/r)` of the lower endpoint.  A generic constant overshoot
leaves a constant fraction of the plateau untreated at every serviced
depth.

### Proof of (1.10)

Expanding (1.4),

\[
 \rho_{m,r}={1\over16}
 \left(1+{3\over2r}
       +O(r^{-2}+m^{-1})\right),                         \tag{1.11}
\]

and substitution into (1.9) gives (1.10).  \(\square\)

---

## 2. Exact adjacent-scale supply

The ratio of the next catalogue to the current one is

\[
\boxed{
 \sigma_{m,r}:={M_{r+1}\over M_r}
 ={(m-r-1)(2r-1)\over
   (2(m-r-1)-1)(r+1)}.}                                 \tag{2.1}
\]

For `r>=5`,

\[
                         \sigma_{m,r}>{3\over4}.         \tag{2.2}
\]

Indeed, putting `k=m-r-1`, inequality (2.2) is equivalent to

\[
 4k(2r-1)>3(2k-1)(r+1),
\]

whose left side minus right side is

\[
                         2k(r-5)+3(r+1)>0.               \tag{2.3}
\]

Combining (1.8) and (2.2) gives the exact strict inequality

\[
\boxed{
 {D_r\over4}<M_r+M_{r+1}\qquad(r>=5).}                  \tag{2.4}
\]

Thus two adjacent catalogues always have enough raw switches, even at the
largest possible Catalan overshoot `t<16`.

Notice also

\[
 \sigma_{m,r}=1-{3\over2r}
                 +O(r^{-2}+r/m),                        \tag{2.5}
\]

so replacing scale `r` by a single adjacent scale does not cure a
constant overshoot.  The gain comes from combining the two supplies.

---

## 3. Cardinality tuning through the phase-critical window

Let `Q=[r,H]` and put

\[
                         c_q=W-N_q.                      \tag{3.1}
\]

The sequence `c_q` is increasing.  Assume

\[
                         c_H<D_r.                        \tag{3.2}
\]

Choose

\[
\boxed{
 L=\left\lfloor{D_r-c_H\over4}\right\rfloor.}          \tag{3.3}
\]

By (2.4), the union of the two adjacent catalogues contains at least `L`
switches.  For every `q in Q`, (1.3) and monotonicity give

\[
\begin{aligned}
 K_{q,p}(F_{MSW})-c_q
 &\ge D_r-c_q\\
 &\ge D_r-c_H\\
 &\ge4L.                                                 \tag{3.4}
\end{aligned}
\]

Therefore the scalar criticality defects of an `L`-bit tuned catalogue
obey

\[
\boxed{
 \sum_{q=r}^{H}
 \left(4L-[K_{q,p}(F_{MSW})-c_q]\right)_+=0.}           \tag{3.5}
\]

This is stronger than `o(W)`: after count tuning, the certified plateau
tail has no scalar undersupply at any serviced depth.

For the phase-capacity interval `H=O(p^(1/4))`, condition (3.2) holds with
room.  Indeed

\[
 {c_H\over W}=O(H^2/m)=O(p^{-1/2}),                     \tag{3.6}
\]

whereas

\[
 {D_r\over W}=\Theta(r^{-3/2}),qquad
 r=\Theta(\log p).                                      \tag{3.7}
\]

Hence `c_H=o(D_r)`, and

\[
             L=(1-o(1)){D_r\over4}.                     \tag{3.8}
\]

In particular the Catalan rounding of `r` and the forced duplicate budget
do not obstruct the saturation theorem on the entire `p^(1/4)` plateau
window.

---

## 4. One-scale lower bound and why varying one scale is insufficient

Suppose only the literal scale-`r` cube is used.  Every toggle lowers one
depth cap tail by at most four.  Hence, uniformly over `q in Q`,

\[
 \phi_q(F_x)
 \ge D_r-c_q-4M_r.                                      \tag{4.1}
\]

Summing gives

\[
\boxed{
 \sum_{q\in Q}\phi_q(F_x)
 \ge |Q|(D_r-4M_r)-\sum_{q\in Q}c_q.}                  \tag{4.2}
\]

If `a_(m,r)(t)>=1+epsilon`, `H=Theta(p^(1/4))`, and
`r=Theta(log p)`, then

\[
 |Q|(D_r-4M_r)
 =\Theta_\varepsilon
   \left({Wp^{1/4}\over(\log p)^{3/2}}\right),          \tag{4.3}
\]

while

\[
                 \sum_{q\le H}c_q
                 =O(WH^3/m)=O(Wp^{-1/4})=o(W).          \tag{4.4}
\]

Thus one scale fails by much more than `W` whenever its Catalan overshoot
is bounded away from the narrow threshold (1.9).

The same conclusion holds if one merely chooses **one** of `r-1,r,r+1`
at each depth: their catalogue sizes differ only by `1+O(1/r)`, while the
required factor in (1.5) can be any constant below `7/4`.  Adjacent
scales have to be combined, not alternated depth by depth.

---

## 5. The physical compatibility gate

Equation (3.5) is a scalar catalogue theorem, not yet an exact-factor
construction.  For one fixed scale, all switches form a Boolean cube
because equal-size recursion nodes in one row are disjoint and their phase
slabs do not interfere.  A size-`r+1` node and a size-`r+2` node can be
nested.  Their row pairs and switched slabs can therefore overlap, and
the same proof does not show that arbitrary choices from the two
catalogues commute.

Three possible upgrades would turn the scalar theorem into the Gaussian
rounding input.

1. A **cross-scale operadic commutation theorem** showing that the two
   local port replacements may be nested in either order.
2. A joint subcatalogue of size `L` from (3.3) whose middle supports form
   an exact Boolean cube.
3. Additional orientations at one scale giving at least
   `(7/4+o(1))M_r` compatible switches, avoiding cross-scale nesting.

No such theorem is currently recorded.  Row-disjoint thinning is far too
expensive: `M_r/(W/p)=Theta(p/r^(3/2))`, so restricting every row to one
switch loses the required order of magnitude.

There is a second, logically later caveat.  The lower bound (1.3) may be
strict because other canonical fibres also contribute to `K_(q,p)`.
This does not hurt scalar saturation, but it means a fractional/dynamic
drain theorem must remove the additional excess as well.  Formula (3.5)
proves only that Catalan arithmetic is no longer the obstruction.

---

## 6. Decision

The exact scalar audit is positive:

\[
 \boxed{
 \text{two adjacent scales eliminate all certified
 Catalan overshoot/undershoot at the count level.}}
\]

For one scale there is an explicit constant obstruction, determined by
(1.5) and (1.9).  For two scales the worst possible required factor is
strictly below `7/4`, while the exact available factor is strictly above
`7/4` for `r>=5`.

Therefore Gaussian-window rounding is not blocked by the Catalan jump.
Its next gate is a physical cross-scale cube (or same-scale extra
orientations), followed by the already isolated weighted four-arm drain
condition.
