# Independent audit of quartet joint-face incidence

## 0. Verdict

`QUARTET_JOINT_FACE_INCIDENCE.md` is correct after separating three
different probability spaces which are easy to conflate:

1. the fraction of demands visible inside one fixed cell;
2. the incidence probability of one fixed nested pair under a random
   quartet frame; and
3. the joint incidence of lower and upper demands under the same frame.

The exact conclusions are:

* the random quartet frame at a fixed source is a uniform perfect matching;
* a fixed depth-`q` lower or upper nested pair is admissible with probability
  `p_m(q)=(1+o(1))2^{-q}` for `q=o(m)`;
* a fixed dimension-`m/2` cell separately has the smaller face fraction
  `2^{-q}exp(-q^2/(2m)+o(q^2/m))`;
* two disjoint same-side demands are asymptotically independent, while a
  lower and upper demand at one source have normalized codegree
  `exp(Theta(q^2/m))`;
* each deterministic wreath partition has exactly the same total incidence
  budget, forcing at least `(1+o(1))2^q` catalog members for universal
  depth-`q` coverage; and
* `O(m2^H)` random members suffice for all one-sided pairs through
  `H=o(m)`, up to the polynomial union-bound factor.

This is a useful joint theorem, but it is not a consecutive-window theorem.
An admissible face supplies directions; it does not place them consecutively
in any selected cycle.

## 1. Audit of the induced matching law

For even `m=2g`, a perfect matching has `m` edges.  A quartet resolution
induces that matching precisely by partitioning its edges into `g` unordered
pairs, one pair per quartet.  The number of preimages is

\[
 {m!\over2^g g!},                                    \tag{1.1}
\]

independent of the matching.  For odd `m=2g+1`, choose the leftover edge
and group the rest; this is again constant.  Thus the induced matching is
uniform.

This argument is pointwise in the source rank sector.  It remains valid
when the complete wreath frame function uses independent choices in every
sector.  It does not assert that frames at two different sources are
independent; that question is handled separately in Section 6 of the source
note.

## 2. Face equivalence and exact probability

Let `D=X\S`.  The cell face has intersection `S` if and only if the frame
edge incident with every `d in D` is split by `X`.  Since a split edge has
only one endpoint in `X`, distinct demanded coordinates automatically use
distinct free directions.  Therefore the event is exactly

\[
 P(D)\subseteq X^c.                                  \tag{2.1}
\]

There are `(m)_q` injections from `D` to `X^c`, followed by
`(2m-2q-1)!!` arbitrary residual matchings.  This verifies

\[
 p_m(q)={(m)_q(2m-2q-1)!!\over(2m-1)!!}.            \tag{2.2}
\]

Complementation gives the upper formula with no new assumption.

Writing every factor as

\[
 {m-i\over2(m-i)-1}
 ={1\over2}\left(1-{1\over2(m-i)}\right)^{-1}
\]

gives

\[
 \log(2^qp_m(q))
 ={1\over2}\log{m\over m-q}+O((m-q)^{-1}).          \tag{2.3}
\]

Hence `p_m(q)=(1+o(1))2^{-q}` uniformly for `q=o(m)`.

## 3. Audit of the Gaussian-scale distinction

In a fixed dimension-`d` cell, exactly `binom(d,q)` of the
`binom(m,q)` lower demands occur.  Expanding falling factorials verifies

\[
 \log{\binom dq\over\binom mq}
 =q\log(d/m)-{q(q-1)\over2}(d^{-1}-m^{-1})
  +O(q^3/m^2)                                        \tag{3.1}
\]

whenever `d` is bounded below linearly and `q=o(m)`.  At `d=m/2+O(1)`
this contains the factor `exp(-q^2/(2m)+o(q^2/m))`.

The source note correctly does not put that factor into the unconditional
probability.  Conditioning on a prescribed face removes `q` forced cross
edges and leaves a uniform matching on two sides of size `m-q`.  Thus

\[
 d\mid A=q+D_{m-q},
 \qquad E(d\mid A)=m/2+q/2+O(1).                    \tag{3.2}
\]

The incidence measure is dimension-size-biased.  This is the precise
reason the Gaussian cellwise depletion cancels from the factorial moment.

## 4. Audit of same-source codegrees

For two lower demands `D_1,D_2`, both occur exactly when their union is
matched outside.  Hence their codegree is `p_m(|D_1 union D_2|)`.  The same
holds for two upper demands.

If the demands are disjoint, sequential exposure gives

\[
 p_m(a+b)=p_m(a)p_{m-a}(b).                          \tag{4.1}
\]

Comparison of the products shows that the normalized codegree is
`1+o(1)` throughout `a+b=o(m)`.  With overlap `c`, the leading ratio is
`2^c`; this is shared incidence, not a failure of the formula.

For one lower demand of size `a` and one upper demand of size `b`, expose
the outside mates of the lower demand.  Their intersection `R` with the
upper demand is hypergeometric, and the remaining requirement has
probability `p_{m-a}(b-R)`.  This proves the exact mixed formula.

The bounds

\[
 2^{ab/m}\le E2^R\le(1+b/m)^a\le e^{ab/m}           \tag{4.2}
\]

follow respectively from Jensen and comparison of sampling without
replacement with independent Bernoulli sampling.  The harmless
`p_n(s)/2^{-s}=1+o(1)` factors then prove the normalized
`exp(Theta(ab/m))` codegree.  This positive correlation is caused by
direct edges which satisfy one lower and one upper demand simultaneously.

## 5. Audit of arbitrary-source dependence

For a fixed quartet decomposition, sources with distinct complete local-rank
vectors use independent sector-frame variables.  Their local success
probabilities therefore multiply.  Sources with equal rank vectors use the
same local choices, so intersections of their allowed matching sets replace
products.  Averaging those two branches over decompositions gives the exact
formula in Section 6 of the source note.

This dependence on the full rank-vector equality event is real.  One may
not replace the arbitrary two-source codegree by the product of its
one-source marginals.  Nor is source Johnson distance by itself enough
before the decomposition average is expanded into its coordinate-type
counts.

## 6. Audit of the catalog bounds

Every deterministic wreath frame has the canonical dimension histogram.
Summing `binom(d,q)` over that histogram gives

\[
 \sum_X\binom{d(X)}q
 =W\binom mq p_m(q).                                  \tag{6.1}
\]

Thus a catalog of `K` partitions has only `Kp_m(q)` incidences per nested
pair on average.  Universal multiplicity `L` forces
`K>=L/p_m(q)`.  This rules out constant catalogs at growing depth and
polynomial catalogs beyond logarithmic depth, independently of how the
catalog is constructed.

For the upper bound, independent catalog members give a binomial count for
each fixed pair.  The total number of lower and upper pairs through
`H=o(m)` has logarithm `Theta(m)`.  Taking

\[
 K=C_\epsilon m/p_m(H)=O_\epsilon(m2^H)             \tag{6.2}
\]

and applying Chernoff plus a union bound gives the claimed simultaneous
multiplicity.

The two-sided incidence identity with
`binom(d,a)binom(d,b)` is also correct.  It gives the catalog denominator
`J_m(a,b)` and retains an `exp(-Theta(ab/m))` saving in its reciprocal.
This is a codegree-scale correction, not a one-sided face penalty.

## 7. Scope boundary

The face event proves that a direction ordering *could* realize the target
inside its cube.  A constructed cycle factor would still need to:

* choose those directions in consecutive transitions;
* assign different targets to different windows;
* reconcile lower and upper assignments with their mixed codegrees;
* select cells from the catalog without overlapping middle vertices; and
* pay only `o(W)` seams and repairs.

No statement in the source note claims these missing steps.

## 8. Machine audit

`scratch/check_quartet_joint_face_incidence.py` independently enumerates:

* all perfect matchings through `m=5`;
* all quartet or quartet-plus-leftover structures and their local frames;
* the exact lower and upper probabilities for every depth;
* all same-source lower/lower codegrees;
* every same-source lower/upper size pair;
* the one-sided and mixed dimension-factorial moments; and
* representative arbitrary-two-source shared-sector and independent-sector
  branches.

All checks pass.  The finite checker validates the exact identities, not
the asymptotic catalog-to-cycle step, which remains open.

