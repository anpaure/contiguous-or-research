# Independent adversarial audit of `MIXED_CONJUGATE_RESOLUTION.md`

## 0. Verdict

The proved part of `MIXED_CONJUGATE_RESOLUTION.md` survives audit.

* The exponentially small large-cell exception is valid.
* Transporting a source radius through a coordinate conjugation is a
  legitimate chain-length label; it is not an assertion that the conjugated
  set retains its original fixed-order RSK shape.
* The one-point degree laws, singleton completion cost, and diagonal-orbit
  codegree formula are exact.
* The coarse target--target bound

  \[
       O\!\left(R e^{H^2/m+o(1)}/m\right)
  \]

  is valid.  In particular all distinct typed codegrees are `o(1)` under
  condition (5.7).
* The two-partition trade theorem is exact for whole-cell selections.

No integral resolution follows.  The fractional matching, small pair
codegrees, and two-partition rigidity do not prove the conjectural absorber
or an additive `o(W)` integrality gap.

Two presentation repairs were made directly in the source:

1. the polynomial prefactor in the `DU` lower-tail bound is now recorded as
   an `o(1)` in its exponential rate; and
2. the target--target orbit-size argument now states the exact continuation
   count and disposes explicitly of both one-continuation orbits.

## 1. Exponential large-cell tail

For one critical sequence of length `a`, the native last-`DU` partition has
dimension deficit distribution

\[
 \Pr(\delta=t)=2^{-t}\quad(1\le t<a),\qquad
 \Pr(\delta=a)=2^{1-a}.
\]

The last term combines the all-`UD` string and the string whose final `DU`
is in the first position.  Hence every exponential moment below `log 2` is
bounded uniformly in `a`.

Conditioned on one uncoloured odd-BK orbit, the orientation bits in distinct
critical sequences are disjoint and independent.  There are at most `d/2`
such sequences, so

\[
 \mathbb E e^{\theta\Delta}\le C_\theta^{d/2}.
\]

On the radius range `d<=m^(2/3)`, an orbit with at least `m/8` active
directions can have cell dimension below `ell=o(m)` only if
`Delta>m/9`.  Chernoff therefore gives

\[
 \Pr(\Delta>m/9)\le
 \exp(-\theta m/9+O(m^{2/3}))=e^{-\Omega(m)}.
\]

The other two exceptions are independently

\[
 W e^{-\Omega(m^{1/3})}
 \quad\text{and}\quad
 W e^{-\Omega(m)}
\]

from the RSK radius tail and the active-direction lower tail.  The first
dominates, proving

\[
 E\le W e^{-\Omega(m^{1/3})}.
\]

The original finite inequality in (1.6) omitted its harmless factor `m+1`.
It has been corrected to

\[
 \exp((\log4-c_0+o(1))m).
\]

This changes no theorem.  Multiplication by every
`H=exp(o(m^(1/3)))` still gives `HE=o(W)`.

## 2. Transported radius labels

A coordinate permutation generally changes the ordinary RSK shape of an
individual middle mask.  The construction does not use the conjugated
mask's new RSK shape.

Instead, a source block of radius `d` is a bundle of middle starts assigned
chain length `d`.  Coordinate permutation preserves:

* all set ranks;
* the cyclic Johnson geometry;
* every intersection and union relation; and
* local geodesicity through all certified depths.

Thus its image still supplies a valid nested segment through every
`q<=min(d,H)`.  Globally, the number of source middle vertices carrying
label `d` is `g_d`, and in the no-defect case it is exactly

\[
 a_d=N_d-N_{d+1},
\]

the forced number of radius-`d` chains in an SCD.  A new SCD is allowed to
assign these chain lengths to different middle masks.  Therefore transported
radius is legitimate.

What would be illegitimate is to claim that `rad(pi X)=rad(X)` in the
original fixed coordinate order.  The source makes no such claim.

## 3. Exact one-point degree law

Parallel conjugate occurrences are retained and each receives weight
`1/|G|`.  This avoids all stabilizer bookkeeping.

For any transitive typed class `Omega`, total weighted incidence divided by
`|Omega|` is the common degree.  The base system contains:

* `W-E` middle incidences;
* `g_d` radius-`d` middle incidences; and
* `G_q` incidences in each sign of depth `q`.

Therefore

\[
 \deg_x(X)=(W-E)/W,\qquad
 \deg_{x,d}(X)=g_d/W,\qquad
 \deg_x(S)=G_q/N_q.
\]

There is no hidden multiplicity inside one real block: for `q<ell`, its `R`
depth-`q` shadows are distinct in each typed class.  Different ranks and
signs are represented by separate vertex classes.

When `E=0`, telescoping `sum_(d>=q)a_d=N_q` makes every typed degree exactly
one.  This is an exact fractional perfect matching, not merely an
approximately regular weighting.

## 4. Singleton completion and repair cost

The block degree deficiencies are nonnegative because `g_d<=a_d` and hence
`G_q<=N_q`.  Giving every middle singleton weight `E/W` and every target
singleton at depth `q` weight `1-G_q/N_q` raises every degree to one.

The total singleton weight is exactly

\[
 E+2\sum_{q=1}^H(N_q-G_q)
 =E+2\sum_d e_d\min(d,H)
 \le(2H+1)E=o(W).
\]

The middle term is an equality; the displayed source uses the equivalent
double sum.  A typed singleton corresponds to one literal-mask repair, so
unit cost is a valid upper-bound accounting convention.

This is only a **fractional** repair cost.  It does not imply that an
integral matching has comparable cost.  The source explicitly preserves
this distinction.

## 5. Exact orbit codegree formula

For a diagonal `G`-orbit `O` of ordered typed pairs and a fixed
`(u,v) in O`, every base ordered pair in `O` is carried to `(u,v)` by exactly
`|G|/|O|` permutations.  Multiplying by `1/|G|` and summing gives

\[
 \codeg_x(u,v)=\frac1{|O|}\sum_B c_O(B).
\]

This remains exact in the presence of stabilizers and repeated decorated
edges because occurrences, rather than distinct edge sets, are weighted.

For two middle vertices at Johnson distance `r`,

\[
 |O|=W\binom mr^2.
\]

There are `(W-E)/R` base blocks and at most `R(R-1)` ordered distinct middle
pairs per block.  Hence

\[
 \codeg_x(u,v)\le\frac{R-1}{\binom mr^2}.
\]

For a middle vertex and a depth-`q` target, the stabilizer of the middle set
has at least `binom(m,q)` images of the target.  At most `R^2` ordered pairs
of the two prescribed typed classes occur in one block, giving

\[
 \codeg_x(u,v)\le R/\binom mq\le R/m.
\]

These bounds are accepted.

## 6. Target--target codegrees

This was the most delicate part of the audit.

Fix target ranks `k,l in [m-H,m+H]`.  The diagonal orbit of an ordered pair
with intersection size `a` has, from a fixed first target, exactly

\[
 K(k,l,a)=\binom{k}{a}\binom{2m-k}{l-a}             \tag{6.1}
\]

continuations.

The only cases with `K=1` are:

1. `k=l=a`, the same-set diagonal orbit; and
2. `a=0,k+l=2m`, the complementary orbit.

Case 1 cannot contain two distinct vertices of one typed class.  Two
different target classes do not have equal ranks, so it does not reappear
across types.  Case 2 has zero base numerator: every two target vertices in
one partial pair-flip block contain the block's fixed selected core of size
at least `m-ell>0`, and therefore cannot be complements.

In every remaining feasible orbit, at least one nontrivial binomial factor
in (6.1) is at least `m-H=Omega(m)`.  Thus `K=Omega(m)` uniformly over all
typed target pairs which can co-occur.

For two fixed target classes, one block contributes at most `R^2` ordered
pairs, so all base blocks contribute at most `WR`.  The first target layer
has size at least `N_H`, giving

\[
 \codeg_x(u,v)
 \le O\!\left(\frac{WR}{N_Hm}\right)
 =O\!\left(\frac{R e^{H^2/m+o(1)}}m\right).
\]

The estimate `W/N_H=e^(H^2/m+o(1))` is uniform for
`H=o(m^(2/3))`.  Therefore condition

\[
 R e^{H^2/m}=o(m)
\]

makes every distinct target--target codegree `o(1)`.  Together with the
middle--middle and middle--target bounds, this proves the claimed maximum
over all distinct typed pairs.

No counterexample orbit survives the common-core test.  The source was
patched to include (6.1) and the two exceptional cases explicitly.

## 7. Parameter quantifiers

With `R=m^(3/4+o(1))` and `H=sqrt(m omega(m))`, condition (5.7) becomes

\[
 m^{-1/4+o(1)}e^{\omega(m)}\to0.
\]

Every `omega=o(log m)` satisfies this.  The additional requirements
`H<ell=R/2=o(m)` and `H=o(m^(2/3))` also hold for such a sufficiently slow
`omega`.

The phrase "such as `omega=o(log m)`" is therefore correct.  It would be
false for an unrestricted `omega=Theta(log m)` without controlling its
constant.

## 8. Two-partition trade rigidity

For partitions `P,Q` of a finite middle set, let binary variables select
their whole cells.  Every original vertex gives one overlap edge `PQ` and
the exact-cover equation

\[
 x_P+y_Q=1.
\]

Along a connected component these equations force every left variable to
one common bit and every right variable to its complement.  Conversely both
componentwise choices are valid.  The theorem is exact even with parallel
overlap edges.

Its scope is whole-cell, zero-defect trades between two partitions.  It does
not rule out:

* trades using parts of cells;
* three or more conjugate systems;
* repair singletons or temporarily uncovered vertices; or
* genuine multi-block absorbers.

The source states these escapes and does not overextend the theorem.

## 9. Final status

| claim | audit status |
|---|---|
| exponential large-cell tail | accepted after harmless `o(1)` repair |
| transported radius ledger | accepted |
| exact typed one-point degrees | accepted |
| fractional singleton cost `o(W)` | accepted; fractional only |
| exact orbit codegree formula | accepted |
| middle--middle and middle--target bounds | accepted |
| coarse target--target bound (5.6) | accepted after explicit orbit repair |
| all distinct typed codegrees `o(1)` under (5.7) | accepted |
| two-partition component rigidity | accepted with whole-cell scope |
| integral matching of repair cost `o(W)` | open conjecture |

The note therefore makes genuine general progress: it removes every
one-point fractional and pair-codegree obstruction in the mixed-conjugate
reservoir.  The remaining gap is still the advertised correlated integral
resolution, not a hidden error in the fractional laws.

