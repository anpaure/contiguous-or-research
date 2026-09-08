# Partial pair-flip blocks and a shallow-resolution/deep-covering split

This note refines the rank-balanced program using partial pair-flip blocks and
pure shadow coverage.  It proves three quantitative facts:

1. the middle-only partial-block hypergraph has relative pair codegree at most
   `2/m^2`, a substantial improvement over the earlier loose `O(1/m)` bound;
2. if a near-factor is pseudorandom at the natural Poisson scale, then depths
   beyond `Theta(sqrt(m log log m))` leave only `o(W)` total missing masks; and
3. this hybrid split does not reduce the first-order size of a one-stage
   all-shallow-ranks matching edge: almost all Boolean-lattice mass already
   lies inside the shallow structured core.

The remaining theorem is therefore precise.  One needs a pseudorandom
near-factor of the middle layer which is deliberately shadow-resolving in the
inner `Theta(sqrt(m log log m))` band and merely random-like outside it.

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \rho_q=N_q/W.                                      \tag{0.1}
\]

Use `H` for the final central-band depth and `ell` for the half-length of a
partial block.  We assume

\[
 H=o(\ell),\qquad \ell=o(m),\qquad R=2\ell.          \tag{0.2}
\]

For the eventual literal-tail application one may take, nonoptimally,

\[
 H=(1+\varepsilon)\sqrt{m\log m}                    \tag{0.3}
\]

and then choose `ell/H -> infinity` arbitrarily slowly.

## 1. Partial blocks

Choose a middle set `X`, ordered distinct elements

\[
 a_0,\ldots,a_{\ell-1}\in X,
 \qquad b_0,\ldots,b_{\ell-1}\notin X,
\]

and flip the pairs `a_i <-> b_i` first forward and then backward in the same
cyclic order.  The resulting cycle has `R=2ell` distinct middle states.  Its
unchanged core has size `m-ell`.  Every cyclic `q`-window with `q<ell` is
geodesic, and its `R` lower rank-`m-q` colours are distinct; the same is true
of its `R` upper rank-`m+q` colours.

There are, with parameter multiplicity,

\[
 E=W(m)_\ell^2                                           \tag{1.1}
\]

blocks.  Symmetry gives middle degree

\[
 D=R(m)_\ell^2                                           \tag{1.2}
\]

and full depth-`q` target degree

\[
 D_q=D/\rho_q.                                           \tag{1.3}
\]

Thus a selection of `t=W/R` blocks has natural mean occurrence

\[
 \lambda_q=tR/N_q=1/\rho_q                              \tag{1.4}
\]

for every target of either sign.  Crucially, (1.4) is independent of `ell`.
Shortening the blocks changes the matching geometry and seam cost, but not the
shadow redundancy available at a given rank.

## 2. Exact middle pair-codegree improvement

Let `H_ell` be the multihypergraph whose vertices are the middle `m`-sets and
whose edges are the `R` middle states of parameterized partial blocks.

### Lemma 1

`H_ell` is `R`-uniform and `D`-regular, and

\[
 \boxed{\frac{\Delta_2(H_\ell)}{D}\le\frac2{m^2}.}       \tag{2.1}
\]

#### Proof

Fix distinct middle sets `X,Y`, and let their Johnson distance be `d`.  If
`d>ell`, no partial block contains both.  Otherwise, two positions containing
`X,Y` must have cyclic separation `d` or `R-d`; there are at most `2R`
ordered position pairs.

For one such pair, the `d` elements of `X-Y` and the `d` elements of `Y-X`
must occupy the intervening transition positions.  Their orders contribute at
most `(d!)^2`.  The remaining active coordinates contribute

\[
 (m-d)_{\ell-d}^2
\]

choices.  Hence

\[
 \begin{aligned}
 d(X,Y)&\le2R(d!)^2(m-d)_{\ell-d}^2,\\
 \frac{d(X,Y)}D
 &\le2\left(\frac{d!}{(m)_d}\right)^2
   =\frac2{\binom md^2}\le\frac2{m^2}.
 \end{aligned}
\]

QED.

In particular,

\[
 R^2\Delta_2(H_\ell)/D=O(\ell^2/m^2)=o(1).         \tag{2.2}
\]

This removes the projective-plane-type numerical warning for the
**middle-only** packing more strongly than the previous `O(D/m)` estimate.
It still does not by itself invoke a theorem with growing uniformity: the
[classical Pippenger--Spencer statement](https://doi.org/10.1016/0097-3165(89)90074-5)
fixes the edge size before taking the asymptotic limit.  A quantitative nibble proof uniform under (2.2), or a
direct Boolean absorption, would settle Stage A for these partial blocks.

The one-stage decorated hypergraph is less favourable.  A prescribed middle
set and one of its rank-`m-1` facets co-occur with relative frequency of order
`1/m`, because the selected cycle uses two of the `m` lower facets incident
with that middle vertex.  Thus adding all shadow classes raises the worst
relative pair codegree back to order `1/m`.  This is another reason to pack
the middle layer first and treat shadow coverage as tracked statistics rather
than literal disjoint vertices in the same matching edge.

## 3. Pure random coverage and its threshold

For `t=W/R` independent uniform parameter blocks, a fixed target is absent
with probability

\[
 \left(1-\frac R{N_q}\right)^t
 =\exp\left(-\frac1{\rho_q}+o(1)\right).           \tag{3.1}
\]

An actual block factor is not independent, so (3.1) is presently a benchmark,
not a conclusion.  Abstract the required random-like property as follows:
for some constant `c>0`, a random near-factor `F` obeys

\[
 \mathbb E M_q^\epsilon(F)
 \le N_q\exp(-c/\rho_q)+o(W/H)                    \tag{3.2}
\]

for each sign and every depth in a specified outer range.

For `q=O(sqrt(m log m))`,

\[
 \log\frac1{\rho_q}
 =\frac{q^2}{m}+O\left(\frac qm+\frac{q^3}{m^2}\right)
 =\frac{q^2}{m}+o(1).                              \tag{3.3}
\]

Choose the transition depth `q_*` by

\[
 \frac c{\rho_{q_*}}\ge2\log H.                   \tag{3.4}
\]

Then

\[
 q_*=(1+o(1))\sqrt{m\log\log H}
     =(1+o(1))\sqrt{m\log\log m}.                 \tag{3.5}
\]

Since `rho_q` decreases with `q`, (3.2)--(3.4) give

\[
 \begin{aligned}
 \frac1W\sum_{q=q_*}^{H}\sum_\epsilon
       \mathbb E M_q^\epsilon
 &\le 2H e^{-2\log H}+o(1)\\
 &=O(1/H)+o(1)=o(1).                               \tag{3.6}
 \end{aligned}
\]

Markov's inequality then supplies one factor with `o(W)` total outer-band
omissions.  Thus the outer depths need only pseudorandom **coverage**, not
rank-balanced matchings or perfect rainbow behaviour.

By contrast, for `q=o(sqrt m)` one has `rho_q=1-o(1)` and the random missing
fraction is asymptotically constant.  The inner band cannot be repaired from
an unstructured random factor.

## 4. Exact multiscale sufficient theorem

The following formulation is sufficient for an asymptotically optimal OR
array.

### Tracked shadow-factor hypothesis

There is a (possibly random) family `F` of disjoint partial blocks such that:

1. its middle states miss `o(W)` middle sets and `|F|=W/R+o(W/R)`;
2. over both signs and all `q<q_*`, the total number of missing shadow targets
   is `o(W)`; and
3. for `q_*<=q<=H`, it satisfies (3.2), or directly has `o(W)` total missing
   targets.

Under this hypothesis, concatenate the block cycles.  Append the first `H`
states of each block and use the existing endpoint padding.  By `H=o(ell)`,
all cyclic windows through depth `H` are linearized and all coordinate runs
have the required length at cost

\[
 O(H|F|)=O(HW/\ell)=o(W).                         \tag{4.1}
\]

Append every missing middle or central-band mask literally.  Their total cost
is `o(W)`.  Finally, a binomial tail estimate gives

\[
 \frac1W\sum_{|r-m|>H}\binom{2m}{r}
 =O\left(\sqrt m\,e^{-H^2/m}\right)=o(1)          \tag{4.2}
\]

for the safe choice (0.3), so all masks outside the band may also be appended
literally.  Applying the maximal-factor identity to the padded middle row and
then appending the repairs yields a universal OR array of length `W+o(W)`.

Therefore the all-rank problem is reduced to the tracked shadow-factor
hypothesis.  No per-block shadow quotas and no nonwrapping cut CSP are needed.

## 5. Why the hybrid does not shrink a one-stage edge

Although (3.5) is much smaller than the final tail depth, it is already much
larger than the natural Gaussian width `sqrt m`.  Consequently

\[
 1+2\sum_{q<q_*}\rho_q=(\sqrt\pi+o(1))\sqrt m.     \tag{5.1}
\]

Thus a rank-balanced hyperedge which literally carries its proportional share
of every shallow target class has forced expected size

\[
 r_{\rm shallow}
 =R\left(1+2\sum_{q<q_*}\rho_q\right)
 =(2\sqrt\pi+o(1))\ell\sqrt m.                    \tag{5.2}
\]

This is asymptotically the same as carrying proportional shares of *all*
ranks.  The reason is simple: almost all `2^(2m)` Boolean masks already lie in
the interval `|r-m|<q_*`.

With `ell/H -> infinity` and the safe `H` from (0.3), (5.2) is at least

\[
 m\sqrt{\log m}\,\omega(1).                        \tag{5.3}
\]

The ambient parameter degree has

\[
 \log D=(2+o(1))\ell\log m,                        \tag{5.4}
\]

so the decorated edge size is much larger than `log D`.  Existing
fixed-uniformity matching theorems cannot be invoked by merely observing that
both quantities are finite or polynomial/exponential.

The hybrid split is still valuable, but for a different reason: it removes
outer layers from the **integral resolution** task and replaces them by
pseudorandom tracking.  It does not evade the intrinsic `Theta(ell sqrt m)`
amount of shallow Boolean information per block.

## 6. A plausible proof architecture

The quantitative ledger points to the following joint construction.

1. **Middle nibble.**  Use the unusually strong middle codegree (2.1) to
   obtain a near-factor of partial blocks.  The desired theorem should also
   make the matching pseudorandom with respect to the block-neighbourhood
   weights of outer shadow targets.
2. **Shallow steering.**  During the same nibble, bias or absorb blocks so
   that the total missing count over `q<q_*` is `o(W)`.  This is a covering
   constraint, not a disjoint-shadow matching constraint.  At the smallest
   depths it specializes to the already identified two-sided almost-rainbow
   resolution.
3. **Deep tracking.**  Prove (3.2) for `q>=q_*`.  Only an expectation bound on
   the *total* number of misses is needed; no union bound over exponentially
   many individual targets is required.
4. **Literal alteration.**  Append all remaining masks.  Equations (3.6),
   (4.1), and (4.2) make the total alteration `o(W)`.

[Recent quantitative nibble work](https://arxiv.org/abs/2511.11375) allows
pseudorandomness with respect to families of weight functions, which is
directionally relevant to Steps 1 and 3.  It cannot be quoted here without
auditing its dependence on the growing uniformity `R=2ell` and on the number
and complexity of the shadow weights.

## 7. Ledger

Proved here:

* the exact partial-block degree law (1.2)--(1.4);
* the middle relative pair-codegree bound `2/m^2`;
* the pure-coverage transition threshold
  `q_*=(1+o(1))sqrt(m log log m)` under the Poisson benchmark;
* the summed outer-repair bound `o(W)` under (3.2);
* the exact sufficient tracked-factor hypothesis; and
* the unavoidable shallow edge-size scale `Theta(ell sqrt m)`;
* the certification-depth distribution (8.2); and
* the exact typed fractional perfect matching of Theorem 2.

Not proved:

* a growing-uniformity near-factor theorem from (2.1);
* Poisson-like shadow tracking after conditioning on middle disjointness; or
* an `o(W)`-defect integral rounding of the typed shallow complex.

The principal gain is a cleaner target.  The final `sqrt(m log m)` band does
not have to be resolved integrally at every rank.  Only the inner
`sqrt(m log log m)` band needs deliberate multiscale coordination; beyond it,
random-like redundancy plus literal alteration is sufficient.

## 8. Certification-depth mixing: the clean joint hypergraph

There is a better way to combine the shallow integral task with deep pure
coverage.  Keep **every** physical block at the common long half-length

\[
 \ell=L H,\qquad L\longrightarrow\infty,\qquad LH=o(m). \tag{8.1}
\]

Thus every selected block physically supplies all depths through `H`, and the
outer target multiplicity remains the favourable `lambda_q=1/rho_q`.
Independently assign a block a **certification depth** `d` between `0` and
`q_*`.  A type-`d` block is required to be collision-free only in the middle
class and in the two shadow classes of depths `q<=d`; its deeper physical
windows are not vertices of the matching hyperedge.

Define

\[
 \begin{aligned}
 p_0&=1-\rho_1,\\
 p_d&=\rho_d-\rho_{d+1}\quad(1\le d<q_*),\\
 p_{q_*}&=\rho_{q_*}.
 \end{aligned}                                           \tag{8.2}
\]

Then

\[
 \sum_{d=0}^{q_*}p_d=1,
 \qquad \sum_{d=q}^{q_*}p_d=\rho_q\quad(1\le q\le q_*).
                                                               \tag{8.3}
\]

Let `D_M=R(m)_ell^2` be the middle degree of the common parameter-block
family.  For every parameter block `B` and label `d`, form the nonuniform edge

\[
 e(B,d)=\mathcal M(B)\cup
 \bigcup_{q=1}^{d}
 \bigl(\mathcal L_q(B)\cup\mathcal U_q(B)\bigr).       \tag{8.4}
\]

Its size is

\[
 |e(B,d)|=R(1+2d).                                     \tag{8.5}
\]

Give every type-`d` copy the fractional weight

\[
 x(B,d)=p_d/D_M.                                       \tag{8.6}
\]

### Theorem 2 (exact typed fractional matching)

The weights (8.6) give weighted degree exactly one to every middle vertex and
to every lower and upper target of depths `1,...,q_*`.

#### Proof

A middle vertex has degree `D_M` in every type, hence weighted degree

\[
 \sum_dp_d=1.
\]

A fixed depth-`q` target occurs in `D_M/rho_q` parameter blocks.  It belongs
to an edge copy precisely for labels `d>=q`, so its weighted degree is

\[
 \frac{D_M}{\rho_q}\sum_{d=q}^{q_*}\frac{p_d}{D_M}
 =\frac1{\rho_q}\sum_{d=q}^{q_*}p_d=1
\]

by (8.3).  QED.

The expected number of selected type-`d` blocks in this fractional solution
is

\[
 t_d=p_dW/R.                                           \tag{8.7}
\]

Thus the capacity equations are exact: the middle contribution sums to `W`,
and the number of certified depth-`q` slots of either sign is

\[
 \sum_{d=q}^{q_*}t_dR
 =W\sum_{d=q}^{q_*}p_d=W\rho_q=N_q.                   \tag{8.8}
\]

This realizes rank balancing by mixing **whole certification depths**, not by
independently deleting individual slots.  It preserves all undeclared outer
windows for random covering.

Indeed, for an undeclared target of any depth `q>q_*`, sum the fractional
weights over all labels of every physical block containing it.  The result is

\[
 \frac{D_M}{\rho_q}\sum_{d=0}^{q_*}\frac{p_d}{D_M}
 =\frac1{\rho_q}=\lambda_q.                         \tag{8.9}
\]

Thus the same fractional object has degree one on every certified shallow
vertex and exactly the desired Poisson mean on every unlabelled outer target.

If (8.6) could be rounded to a matching with total defect `o(W)`, its selected
blocks would simultaneously

* cover all but `o(W)` middle and shallow-shadow vertices, with certified
  shadow colours globally distinct; and
* retain every physical depth-`q` window for `q_*<q<=H`, to which the
  pseudorandom estimate (3.2) could be applied.

Every common block is linearized through depth `H` and factored at delay `H`.
The prefix plus factor overhead is `O(H)` per block, hence

\[
 O(HW/R)=O(W/L)=o(W).                                  \tag{8.10}
\]

Together with (3.6) and (4.2), the desired typed matching and outer tracking
would prove `nu(2m)=W+o(W)`.

There is a quantitative warning.  The number of shallow vertices is
`Theta(W sqrt m)`.  An ordinary assertion that a matching covers a
`1-o(1)` fraction of that typed hypergraph may leave `o(W sqrt m)` vertices,
which is far larger than the allowed `o(W)` repair budget.  The required
integral theorem must give **total defect `o(W)`**, equivalently relative
defect `o(1/sqrt m)` across the shallow complex.

Also, the largest typed edge has size

\[
 R(1+2q_*)=\Theta\bigl(\ell\sqrt{m\log\log m}\bigr),   \tag{8.11}
\]

while the fractional average edge size is

\[
 R\left(1+2\sum_{q=1}^{q_*}\rho_q\right)
 =(2\sqrt\pi+o(1))\ell\sqrt m.                       \tag{8.12}
\]

So Theorem 2 closes every density and divisibility equation but not the
integral rounding.  The precise successor theorem is now:

> Round the typed fractional matching (8.6) with total defect `o(W)`, while
> retaining Poisson-scale outer-shadow statistics of the unlabelled physical
> windows.

This single statement combines the formerly separate Stage A, shallow Hall,
and deep random-covering requirements without imposing unnecessary quotas on
the final OR sequence.

## 9. The certification law is exactly the SCD radius law

The differences in (8.2) have a canonical Boolean-lattice meaning:

\[
 Wp_d=N_d-N_{d+1}\quad(0\le d<q_*).               \tag{9.1}
\]

In every symmetric chain decomposition of `2^[2m]`, the number of chains with
minimum rank `m-d` and maximum rank `m+d` is exactly

\[
 \binom{2m}{m-d}-\binom{2m}{m-d-1}=N_d-N_{d+1}.    \tag{9.2}
\]

Every symmetric chain contains one middle set.  Hence `p_d` is precisely the
distribution of the half-length (radius) of the symmetric chain containing a
uniform middle set.  The truncated mass

\[
 Wp_{q_*}=W\rho_{q_*}=N_{q_*}                     \tag{9.3}
\]

is the number of chains reaching rank `m-q_*`, after all longer chains are
truncated to the central band.

The remaining bundle-size divisibility is asymptotically harmless.  For each
radius, group `floor(Wp_d/R)` full bundles and leave fewer than `R` chains.
Across all radii through `q_*`, the total number of band vertices in these
remainders is at most

\[
 \sum_{d=0}^{q_*}(R-1)(2d+1)=O(Rq_*^2)=o(W).       \tag{9.4}
\]

Thus no congruence condition on `R` can obstruct an `o(W)`-defect theorem.

The typed block edge has the same interpretation internally.  For a cyclic
block `X_0,...,X_(R-1)` and a start `t`, define

\[
 L_q(t)=\bigcap_{i=0}^{q}X_{t+i},
 \qquad U_q(t)=\bigcup_{i=0}^{q}X_{t+i}.            \tag{9.5}
\]

Geodesicity gives the saturated symmetric chain segment

\[
 L_d(t)\subset\cdots\subset L_1(t)\subset X_t
 \subset U_1(t)\subset\cdots\subset U_d(t).        \tag{9.6}
\]

For fixed `d`, the `R` segments (9.6), one for each cyclic start, are
vertex-disjoint: at each rank this is exactly the distinct-shadow property of
the pair-flip block, and different ranks cannot collide.  Therefore

\[
 e(B,d)=\bigsqcup_{t=0}^{R-1}\mathcal C_t^{(d)}      \tag{9.7}
\]

is a bundle of `R` disjoint radius-`d` symmetric chains.

The integral typed matching problem is consequently equivalent to a concrete
ordered-SCD problem:

> Decompose the central Boolean band into symmetric chains with the forced
> radius counts (9.2), and bundle chains of a common radius into pair-flip
> wreaths so that their middle members occur in cyclic order and their chain
> flags are the consecutive intersection/union flags (9.6).

Call such an object a **wreath-resolved symmetric chain decomposition**.  A
near wreath-resolved SCD with only `o(W)` uncovered band vertices is exactly
the `o(W)`-defect typed matching required in Section 8.

This reformulation supplies an integral scaffold absent from independent slot
decorations.  It also explains why the probabilities `p_d` telescope so
perfectly: they were the symmetric-chain radius counts all along.  The
remaining obstruction is compatibility between an SCD's middle-centred flags
and the pair-flip cyclic order, not rank capacity or divisibility.

## 10. Shift-compatible SCD normal form

The wreath condition can be stated directly on the middle members of an SCD.
For the chain centred at a middle set `X` and truncated radius `d(X)`, write

\[
 \begin{aligned}
 L_q(X)&=X\setminus\{r_0(X),\ldots,r_{q-1}(X)\},\\
 U_q(X)&=X\cup\{u_0(X),\ldots,u_{q-1}(X)\},
 \end{aligned}                                           \tag{10.1}
\]

where the `r_i` are the successive downward labels and the `u_i` the
successive upward labels of that symmetric chain.  Define the projected
Johnson move

\[
 f(X)=X\setminus\{r_0(X)\}\cup\{u_0(X)\}.          \tag{10.2}
\]

For positive truncated radius, the first necessary condition is that `f` be a
permutation of that radius class (or of all but the allowed repair set).
Radius-zero singleton chains require no projected edge.  This is already
stronger than merely decomposing the Boolean
lattice into symmetric chains: different chains can project to the same
middle set under (10.2).

The exact higher-shadow compatibility is the shift rule

\[
 \begin{aligned}
 r_i(f(X))&=r_{i+1}(X),\\
 u_i(f(X))&=u_{i+1}(X)
 \end{aligned}
 \qquad(0\le i<d(X)-1).                           \tag{10.3}
\]

Indeed, (10.2)--(10.3) imply inductively that

\[
 f^j(X)=X\setminus\{r_0,\ldots,r_{j-1}\}
          \cup\{u_0,\ldots,u_{j-1}\},             \tag{10.4}
\]

and therefore

\[
 \bigcap_{j=0}^{q}f^j(X)=L_q(X),
 \qquad
 \bigcup_{j=0}^{q}f^j(X)=U_q(X)                   \tag{10.5}
\]

for every `q<=d(X)`.  Conversely, if the consecutive shadows along the
`f`-orbit are the SCD members at every depth, comparing successive set
differences recovers (10.3).

Thus the integral core may be phrased without hypergraph terminology:

> Construct a symmetric chain decomposition whose middle projection `f` is a
> radius-preserving permutation and whose ordered chain labels obey the shift
> recurrence (10.3); then group the cycles of `f` into long locally geodesic
> wreaths.

At depth one, bijectivity of `f` is precisely the two-sided rainbow middle
projection already encountered in the Kneser/Johnson formulation.  Equation
(10.3) identifies the genuinely new all-depth demand: the SCD flags must form
a de Bruijn-type shift system along that projection.  This is a more concrete
mathematical target than arbitrary integral rounding of (8.6).

## 11. The standard Greene--Kleitman projection is a macroscopic distance away

For the standard Greene--Kleitman SCD, the map (10.2) lowers chain radius by
one at every non-singleton chain.  More sharply, its complete indegree law is

\[
 \#\{X:\deg^-f(X)=j\}=\binom{2m-j-1}{m-j}
 \qquad(0\le j\le m).
\]

Hence exactly `W/2` middle vertices lie in the image and asymptotically
`W/4` vertices have indegree at least two.  The former inference that a
maximum linear subforest retains only `W/2` edges is false: deleting a
vertex's outgoing edge can retain two incoming edges.  The exact replacement
is the rooted-tree DP in
`MATH_CORRECTION_GK_PROJECTION_LINEAR_SUBFOREST_TREE_DP_20260731.md`; its
finite retained-edge values for `m=3,...,7` are
`13,44,159,588,2188`, and no asymptotic edit bound is claimed from them.

Independently, all `W-Cat_m=(1-o(1))W` existing projection edges cross
from radius `d` to radius `d-1`, whereas (10.3) first requires a
radius-preserving map.  Consequently the shift-compatible object cannot be
obtained by an `o(W)` repair of the standard Greene--Kleitman projection.
This last conclusion uses radius drop, not the retracted linear-subforest
bound.  The full proofs are in `GK_PROJECTION_COUNTS.md` and the correction
note cited above.

## 12. Tail compression removes the outer Poisson stage

The multiscale program above originally left depths `q>q_*` uncertified and
asked the physical windows to cover them with Poisson-type statistics.  That
is no longer necessary.

The construction in `TRUNCATED_IDEAL_PRODUCT.md` covers, on `2m`
coordinates, every rank at most `m-H` and every rank at least `m+H` in length

\[
 O\!\left(
   \left(1+\frac{H^2}{m}\right)\binom{2m}{m-H}
 \right)                                                     \tag{12.1}
\]

whenever `sqrt(m)<=H=o(m^(2/3))`.  Choose

\[
                         H=\sqrt{m\omega(m)},
 \qquad                   \omega(m)\longrightarrow\infty        \tag{12.2}
\]

arbitrarily slowly.  Then (12.1) is `o(W)`.

Consequently one may set the certification cutoff itself equal to `H`, use
the exact radius law

\[
 p_0=1-\rho_1,
 \qquad p_d=\rho_d-\rho_{d+1}\ (d<H),
 \qquad p_H=\rho_H,                                      \tag{12.3}
\]

and require the typed matching to cover only the complete band through depth
`H`.  Every rank outside that band is supplied by the independent tail word.
There is no longer any need to preserve undeclared windows, prove (3.2), or
track Poisson outer-shadow statistics.

The remaining integral target is therefore cleaner:

> Round the radius-typed fractional matching through
> `H=sqrt(m) omega(1)` with **total** band defect `o(W)`.

This still demands relative defect `o(1/sqrt(m))` because the band has
`Theta(W sqrt(m))` members, but it eliminates the formerly separate deep
random-covering obstruction.
