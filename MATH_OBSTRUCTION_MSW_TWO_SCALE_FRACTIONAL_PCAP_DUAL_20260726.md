# Two-scale MSW cube: the contracted suffix stars give a fractional PCap obstruction

Date: 2026-07-26

> **Scope correction (full-cube audit).**  This note proves an obstruction
> only for the deliberately restricted `L`-bit cube.  It does not obstruct
> a law on the full compatible cube, because that law may use
> `B=M_r+M_(r+1)-E_r` legal bits.  On the full cube the same cut has
> residual `D_r-3B`, positive only for
> `Cat_r/p>64/11+o(1)`.  See
> `MATH_AUDIT_MSW_FULL_TWO_SCALE_DUAL_AND_PRECEDING_SCALE_20260726.md`.

## 0. Outcome

The deliberately selected `L`-bit subcube in
`MATH_THEOREM_MSW_TWO_SCALE_COMPATIBLE_CUBE_20260726.md` does not have the
required product mean.

The persistent marked-gap suffix stars are not an integrality problem.
They expose a fractional capacity loss.  Every scale-`r` or scale-`r+1`
elementary switch has one distinguished suffix arm whose old and new
targets both have canonical load strictly larger than the cap `p` at every
common serviced depth `q>=r+1`.  On the overloaded-set dual, that arm has
coefficient zero.  After exact star contraction, one isolated switch can
therefore drain at most three units, not four.

The full cube is not additive at lower targets, but its failure of
additivity is sparse after summing depths.  A depth-`q` interaction occurs
only when two switched phases are the two boundaries of one window.  Along
one row, the retained size-`r+1` and size-`r+2` slabs have density
`O(1/r)`.  Hence, over `J` consecutive depths, the number of possible
two-boundary interactions is

\[
                         O(L(J/r+1)),                    \tag{0.1}
\]

where `L` is the number of tuned cube bits.  Each interaction changes a
bounded dual potential by at most two.

Take

\[
                         J=\lfloor r^{3/2}\rfloor,
 \qquad \mathcal Q=\{r+1,\ldots,r+J\}.                  \tag{0.2}
\]

The scalar tuning theorem gives

\[
 K_{q,p}(F_{MSW})-(W-N_q)\ge4L\qquad(q\in\mathcal Q),  \tag{0.3}
\]

with

\[
                         L=(1-o(1)){D_r\over4}
                         =\Theta(W/r^{3/2}).             \tag{0.4}
\]

For every product law on this exact `L`-bit cube, its mean histograms
`bar(mu)_q` satisfy

\[
 \boxed{
 \sum_{q\in\mathcal Q}
  \left(K_{q,p}(\bar\mu_q)-(W-N_q)\right)_+
 \ge(1-o(1))LJ=\Omega(W).}                              \tag{0.5}
\]

On this polylogarithmic subwindow the MWB weights are exactly one for all
sufficiently large `m`; consequently (0.5) is also an `Omega(W)` weighted
dual obstruction inside every fixed Gaussian window.

Thus the premise (5.4) of the two-scale Gaussian-rounding implication is
false.  The common suffix arms neutralize; the variable prefix arms and
the other suffix arm provide at most three isolated units, and the sparse
two-boundary commutators cannot coherently supply the missing unit at a
positive fraction of depths.

---

## 1. Exact contraction of a suffix star

Fix a scale `s in {r,r+1}`, an aligned size-`s+1` parent context `C`,
and a spectator `R in D_(s-1)`.  At a depth `q>=s`, the isolated column
has the four-arm form

\[
 a_{q,e}=\partial_e A_{q,C}+\partial_e B_{q,C}
          -\partial_e P^E_{q,C,R}
          -\partial_e P^O_{q,C,R},                     \tag{1.1}
\]

where

\[
                 \partial_eK
 =\mathbf e_{K\cup\{\gamma_e\}}
  -\mathbf e_{K\cup\{\beta_e\}}.                     \tag{1.2}
\]

One of the two fixed suffix arms is the hereditary marked arm.  Write its
old and new targets as

\[
                         S_{q,e}=A_{q,C}\beta_e,
 \qquad                   T_{q,e}=A_{q,C}\gamma_e.       \tag{1.3}
\]

All spectator choices in one parent packet use this same ordered target
pair.  Marked-gap-equivalent exterior contexts give the larger same-sign
stars counted in
`MATH_OBSTRUCTION_MSW_CROSS_PARENT_LAMBDA_GAUSSIAN_20260726.md`.

Contracting a star means retaining its two target rows and aggregating all
identical copies of the ordered arm.  It does not delete their mass and it
does not identify the two physical targets.  In the dual, the contraction
is represented by using one common weight on the two endpoint rows.

### Lemma 1.1 (hereditary cap saturation of the marked arm)

For every `e` of scale `s in {r,r+1}` and every `q>=s`,

\[
 \boxed{
 \mu_q^0(S_{q,e})>p,
 \qquad
 \mu_q^0(T_{q,e})>p.}                                  \tag{1.4}
\]

Here `mu^0` is the canonical MSW histogram.

#### Proof

At the matched depth `q=s`, the exact Catalan boundary profile gives old
load at least

\[
                         d_s=\operatorname {Cat}_s
\]

at `S_(s,e)` and old load at least

\[
                         c_s=\operatorname {Cat}_{s-1}
\]

at `T_(s,e)`.  For `s=r`, minimality of `r` and the exact Catalan quotient
give

\[
 \operatorname {Cat}_{r-1}
 ={\operatorname {Cat}_r(r+1)\over2(2r-1)}
 \ge {2p(r+1)\over2r-1}>p.                             \tag{1.5}
\]

For `s=r+1`, both `Cat_(r+1)` and `Cat_r` are at least `4p`.

At a larger depth, the window contains the complete local invisible block
and merely adjoins the target-forced exterior core.  The same
`Cat_s` fillings still give the old marked target, and the same
`Cat_(s-1)` boundary subclass still gives its mate.  Exterior collisions
can only increase these loads.  Thus the two lower bounds persist for
every `q>=s`, proving (1.4). \(\square\)

Let

\[
                         \Omega_q
 =\{S:\mu_q^0(S)>p\},
 \qquad \alpha_q=\mathbf1_{\Omega_q}.                  \tag{1.6}
\]

Lemma 1.1 says

\[
                         \alpha_q(S_{q,e})
                         =\alpha_q(T_{q,e})=1.           \tag{1.7}
\]

Therefore the contracted marked arm has exact dual coefficient zero:

\[
                         \alpha_q(S_{q,e})
                         -\alpha_q(T_{q,e})=0.           \tag{1.8}
\]

It neither drains nor refills the fixed overloaded-set potential.  Each
of the other three arms can decrease that potential by at most one.
Consequently every isolated retained switch obeys

\[
 \boxed{
                         \langle\alpha_q,a_{q,e}\rangle\ge-3.}          \tag{1.9}
\]

This is the exact four-arm weighted-dual effect of suffix-star
contraction.  No assumption about prefix-target injectivity is used.

---

## 2. The exact two-boundary interaction expansion

Fix a depth `q`.  In a physical row, a rectangle changes a target only
when its switched phase is one of the two boundary phases of the
depth-`q` window.  Hence one rooted window depends on at most the two
switch bits at its boundaries.

Let `G_q` be the multigraph on retained cube bits in which an edge records
one common row and one depth-`q` window whose two boundary phases are the
two switches.  For a configuration `X in {0,1}^L`, write
`E_q(X)` for the number of edges whose two endpoint bits are on.

### Lemma 2.1 (quadratic interaction remainder)

For every configuration,

\[
 \boxed{
 \left\langle\alpha_q,
  \mu_q^X-\mu_q^0-\sum_eX_ea_{q,e}
 \right\rangle
 \ge-2E_q(X).}                                         \tag{2.1}
\]

#### Proof

For one window with boundary bits `x,y`, its target indicator is a
function on `{0,1}^2`.  Its exact Boolean expansion is its value at
`(0,0)`, the two isolated first differences, and the mixed second
difference

\[
 e_{T_{11}}-e_{T_{10}}-e_{T_{01}}+e_{T_{00}}.           \tag{2.2}
\]

Against a weight in `[0,1]`, (2.2) is at least `-2`.  Windows with at most
one switched boundary have zero mixed difference.  Sum (2.2) over the
active two-boundary windows.  There are exactly `E_q(X)` of them, counted
with their row/window multiplicities. \(\square\)

For independent bits with probabilities `x_e`, taking expectations gives

\[
 \left\langle\alpha_q,
  \bar\mu_q-\mu_q^0-\sum_ex_ea_{q,e}
 \right\rangle
 \ge-2\sum_{ef\in E(G_q)}x_ex_f.                       \tag{2.3}
\]

Thus the quotient dual has two terms:

1. at most three units of isolated prefix/remaining-suffix drain per bit;
2. at most two extra units per active opposite-boundary pair.

---

## 3. Summed interaction census for two adjacent scales

The retained switches in one physical row come from recursion nodes of
sizes `r+1` and `r+2`.

* Nodes of one size are disjoint.
* A size-`r+2` node contains at most one size-`r+1` node.
* The only pair whose affected phase-edge slabs overlap is the pattern
  `110010S <-> 101010S <-> 101100S`; one endpoint of every such pair was
  deleted in the compatible cube.

Consequently the switched phase centres in one row have the following
packing property: every cyclic phase interval of length `J<=m/2`
contains at most

\[
                         C_0(J/r+1)                     \tag{3.1}
\]

centres, for an absolute constant `C_0`.

### Lemma 3.1 (summed boundary-pair count)

For every interval `I` of `J` depths contained in `[r+1,m/2]`,

\[
 \boxed{
                         \sum_{q\in I}|E(G_q)|
                         \le C_1L(J/r+1)}               \tag{3.2}
\]

for an absolute constant `C_1`.

#### Proof

Fix one switch occurrence in one of its two rows.  An edge at a depth in
`I` requires the other switched phase to lie at one of the two directed
distances in `I`.  These two phase annuli have total length at most `2J`.
By (3.1), they contain `O(J/r+1)` retained centres.  Sum over the two rows
of every switch and divide by two for unordered pairs.  This proves
(3.2), with row multiplicity retained. \(\square\)

For a product law, `x_ex_f<=1`, so (3.2) also gives

\[
 \sum_{q\in I}\sum_{ef\in E(G_q)}x_ex_f
 \le C_1L(J/r+1).                                      \tag{3.3}
\]

This is where adjacent-scale compatibility matters.  Bounded degree at
one depth would give only `O(LJ)` after summation; recursive slab packing
saves the necessary factor `r`.

---

## 4. The explicit overloaded-set dual

Let the tuned compatible cube have `L` bits.  For a product law put

\[
                         s_x=\sum_ex_e\le L.             \tag{4.1}
\]

From (1.9), (2.3), and the definition of `alpha_q`,

\[
\begin{aligned}
 \langle\alpha_q,\bar\mu_q-p\mathbf1\rangle
 &\ge K_{q,p}(\mu_q^0)-3s_x
       -2\sum_{ef\in E(G_q)}x_ex_f.                    \tag{4.2}
\end{aligned}
\]

Since cap tail is the support function of the target-weight cube,

\[
                         K_{q,p}(\bar\mu_q)
 \ge\langle\alpha_q,\bar\mu_q-p\mathbf1\rangle.       \tag{4.3}
\]

Put `c_q=W-N_q`.  Scalar tuning gives

\[
                         K_{q,p}(\mu_q^0)-c_q\ge4L.     \tag{4.4}
\]

Therefore

\[
 \boxed{
 \left(K_{q,p}(\bar\mu_q)-c_q\right)_+
 \ge L+3(L-s_x)
       -2\sum_{ef\in E(G_q)}x_ex_f.}                   \tag{4.5}
\]

When the displayed right side is negative, replacing it by its positive
part only strengthens the assertion; after summation below its total
negative correction is already `o(LJ)`.

Equation (4.2) is the requested explicit `alpha`-potential.  The
contracted common suffix arm contributes zero, all isolated variable
prefix action is contained in the coefficient `3s_x`, and every possible
nonadditive escape is displayed as one quadratic boundary-pair term.

---

## 5. An `Omega(W)` fractional PCap lower bound

Take

\[
                         J=\lfloor r^{3/2}\rfloor,
 \qquad H=r+J,
 \qquad I=\{r+1,\ldots,H\}.                             \tag{5.1}
\]

At the fatal scale `r=Theta(log p)`,

\[
 {W-N_H\over W}=O(H^2/m)=o(r^{-3/2}).                  \tag{5.2}
\]

Hence `c_H=o(D_r)`, and the tuning in the two-scale cube may take

\[
                         L=\left\lfloor{D_r-c_H\over4}\right\rfloor
                         =(1-o(1)){D_r\over4}.           \tag{5.3}
\]

Sum (4.5), use (3.3), and discard the nonnegative term `3J(L-s_x)`:

\[
\begin{aligned}
 \sum_{q\in I}
  \left(K_{q,p}(\bar\mu_q)-c_q\right)_+
 &\ge LJ-2C_1L(J/r+1)\\
 &=(1-O(1/r))LJ.                                        \tag{5.4}
\end{aligned}
\]

Now write `t=Cat_r/p in [4,16)`.  The exact plateau normalization gives

\[
 {D_r\over W}
 =\left({t-2\over8t\sqrt\pi}+o(1)\right)r^{-3/2}.       \tag{5.5}
\]

Since `J=(1+o(1))r^(3/2)`, (5.3)--(5.5) yield

\[
 \boxed{
 \sum_{q\in I}
  \left(K_{q,p}(\bar\mu_q)-(W-N_q)\right)_+
 \ge\left({t-2\over32t\sqrt\pi}+o(1)\right)W
 \ge\left({1\over64\sqrt\pi}+o(1)\right)W.}          \tag{5.6}
\]

This holds for every product probability vector, including deterministic
corners.

For `q<=H=o(sqrt(m))`, the MWB ratio satisfies `W/N_q=1+o(1)`, so its
integer quota is one and its reciprocal weight is exactly one for all
sufficiently large `m`.  Thus (5.6) is also a weighted obstruction on the
initial part of every window `q<=A sqrt(m)`.

---

## 6. Interpretation

The two-scale scalar proof allocated four units of possible relief to
every bit.  The exact suffix-star contraction shows that one of those
four units is unavailable throughout the hereditary plateau: it merely
moves mass between two targets already above cap.  The three remaining
isolated arms cannot meet the tuned four-units-per-bit demand.

Two-boundary nonadditivity is the only possible source of an extra unit.
The exact Boolean expansion shows that this source is quadratic in pairs
of switched boundaries.  Recursive packing supplies only
`O(LJ/r)` such pairs over `J` consecutive depths, whereas closing the
deficit would require `Theta(LJ)`.

Therefore this particular cardinality-tuned subcube is fractionally
blocked before rounding.  A different product bias inside the same
`L` variables cannot repair it, but this says nothing about laws using
the additional variables of the full compatible cube.  In particular it
does not close a bounded scale menu.

Possible escapes from this restricted cube include

1. using the remaining legal bits of the full compatible cube;
2. adding orientations whose distinguished suffix arm lands below cap;
3. using nonlocal trades with four genuinely external arms; or
4. choosing a larger-scale packet whose useful boundary interactions have
   density `Theta(1)` across the serviced depth band.

Merely contracting the existing same-sign stars identifies the correct
dual loss.  For the full adjacent-scale cube it closes fractional PCap
only in the high-overshoot regime where `D_r-3B` remains positive after
the two-boundary error.
