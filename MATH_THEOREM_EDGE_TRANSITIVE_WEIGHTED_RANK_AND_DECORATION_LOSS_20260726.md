# Edge-transitive weighted rank and the multidepth decoration loss

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or
independent rankwise rounding is used.

## 0. Verdict

For one genuinely route-transitive orbit, the weighted stable-set rank
inequality is equivalent, at the required scale, to an ordinary
near-perfect matching theorem.

Let every route contain \(R\) middle owners, let every owner have orbit
degree \(D\), and let \(\nu\) be the maximum number of pairwise compatible
routes. Then, for every nonnegative route weight \(w\),

\[
 \boxed{
 {1\over D}\sum_Rw_R
 \le {W\over R\nu}\,\alpha_w.}                            \tag{0.1}
\]

If a matching leaves \(L=W-R\nu\) owners, the factor in (0.1) is

\[
                         {W\over W-L}.
\]

Hence

\[
                         L=o(W/H)
\]

implies the full weighted rank estimate with relative error \(o(1/H)\).
Conversely, the unit weight shows that this leave bound is necessary for
that uniform orbit point. Thus no additional weighted obstruction exists
inside a truly transitive single orbit: the unweighted matching number is
the exact issue.

For a convex mixture of route orbits with owner-degree contributions
\(\theta_j\), a sufficient bound is

\[
 \boxed{
 w\cdot x
 \le\left(\sum_j{\theta_j\over\eta_j}\right)\alpha_w,
 \qquad
 \eta_j={R_j\nu_j\over W}.}                                \tag{0.2}
\]

Consequently a \(1-o(1/H)\) near-perfect matching in every positive-mass
orbit is sufficient. A matching of only the orbit's desired
\(\theta_j\)-fraction is not sufficient by this argument; the separate
losses add. Radius classes must therefore be synchronized in one composite
decorated factor, rather than rounded independently.

The known recursive strip factor gives the positive owner-only theorem.
For every power of two \(\ell=o(m)\), one fixed pair frame partitions all
middle owners with at least \(\ell\) split pairs into recursive
\(2\ell\)-necklaces. The exceptional fraction is \(e^{-\Omega(m)}\).
Every selected necklace is in the unrestricted coordinate orbit. Hence
the owner-conflict weighted rank inequality holds with exponentially small
relative error.

This does not survive naive multidepth decoration. If every necklace
advertises its \(R=2\ell\) distinct depth-\(q\) targets, any target-rainbow
route matching has at most \(N_q/R\) members. Therefore its owner coverage
fraction is at most

\[
                         {N_q\over W}.
\]

At \(q\sim a\sqrt m\), this tends to \(e^{-a^2}\), and the unit route
weight forces weighted-rank ratio at least

\[
                         {W\over N_q}\longrightarrow e^{a^2}. \tag{0.3}
\]

This is a genuine weighted obstruction to the unthinned decorated orbit.
It is independent of pair-frame mixing and of local shadow injectivity.

The correct escape is radius thinning: exactly \(N_q\) owner occurrences,
not all \(W\), may advertise depth \(q\) in the SCD normalization. The
known strip factors do not supply a radius-pure Catalan census, nor do they
control cross-cycle physical target collisions. Thus they certify the
owner part of the weighted inequality but not the decorated common-route
inequality.

The remaining theorem is now precise. Construct one approximate
radius-resolved, all-depth rainbow matching with owner leave \(o(W/H)\).
Once such a matching exists in each actual transitive composite class,
orbit symmetrization proves every weighted rank inequality automatically;
no separate weighted or iterative-rounding theorem is needed.

## 1. One transitive route orbit

Let \(\mathcal O\) be the set of middle owners, with

\[
                         |\mathcal O|=W.
\]

Let \(\mathscr E\) be a finite indexed route orbit. Assume:

1. every route \(E\in\mathscr E\) owns exactly \(R\) middle owners;
2. every owner belongs to exactly \(D\) indexed routes;
3. a group \(\Gamma\) acts transitively on \(\mathscr E\) and preserves
   the declared route-conflict relation.

The conflict relation may mean owner intersection only, or it may include
all decorated lower and upper target claims. Write \(G\) for the resulting
conflict graph on \(\mathscr E\), and let

\[
 \alpha_w(G)=
 \max\left\{\sum_{E\in I}w_E:I\text{ is stable in }G\right\}. \tag{1.1}
\]

Double counting owner-route incidences gives

\[
                         |\mathscr E|R=WD.                 \tag{1.2}
\]

Give every indexed route the symmetric fractional weight

\[
                         x_E={1\over D}.                   \tag{1.3}
\]

### Theorem 1.1 (transitive matching-to-weighted-rank principle)

If \(G\) has a stable set \(I\) of size \(\nu\), then, for every
\(w\ge0\),

\[
 \boxed{
 \sum_Ex_Ew_E
 \le {|\mathscr E|\over D\nu}\,\alpha_w(G)
 ={W\over R\nu}\,\alpha_w(G).}                            \tag{1.4}
\]

#### Proof

Average the translates \(\gamma I\), \(\gamma\in\Gamma\), with uniform
indexed multiplicity. Transitivity makes the probability that a fixed
route belongs to \(\gamma I\) equal to

\[
                         {\nu\over|\mathscr E|}.
\]

Therefore

\[
 {1\over|\Gamma|}\sum_{\gamma\in\Gamma}
       \sum_{E\in\gamma I}w_E
 ={\nu\over|\mathscr E|}\sum_Ew_E.
\]

Some translate has weight at least this average, so

\[
 \alpha_w(G)\ge{\nu\over|\mathscr E|}\sum_Ew_E.
\]

Multiply by \(|\mathscr E|/(D\nu)\), and use (1.2).
\(\square\)

### Corollary 1.2 (near-perfect matching is sufficient and necessary)

If \(I\) covers \(W-L\) owners, so that

\[
                         R\nu=W-L,
\]

then

\[
 {1\over D}\sum_Ew_E
 \le {W\over W-L}\alpha_w(G).                             \tag{1.5}
\]

Thus \(L=o(W/H)\) gives relative error \(o(1/H)\).

Conversely, if

\[
 {1\over D}\sum_Ew_E\le(1+\varepsilon)\alpha_w(G)
\]

for every \(w\ge0\), then the choice \(w\equiv1\) gives

\[
 {W\over R}\le(1+\varepsilon)\nu,
\]

and hence

\[
                         L\le{\varepsilon\over1+\varepsilon}W. \tag{1.6}
\]

For a transitive single orbit, the weighted and unweighted losses are
therefore the same at first order.

## 2. Where symmetrization is valid

The group in Theorem 1.1 must preserve the complete route object:

* owner support;
* physical target labels, acted on by the same coordinate permutation;
* radius and collar eligibility;
* both lower and upper flags;
* every conflict used in \(G\).

If a decoration is not preserved by the full coordinate group, the route
catalogue must first be decomposed into its actual automorphism orbits.
One may not average an RSK-radius label, a fixed priority, or a chosen
tail certificate across coordinate permutations which do not preserve
that label.

Indexed duplicates cause no difficulty. They are distinct orbit elements,
receive equal fractional weight, and their translates are counted with the
same multiplicity. In an integral stable set at most one duplicate of a
physical route can occur because duplicates share every owner and target.

## 3. A mixture of transitive orbits

Let

\[
                         \mathscr E=\dot\bigcup_{j\in J}\mathscr E_j
\]

be actual route orbits. In orbit \(j\), let the route size, owner degree,
and stable-set number be \(R_j,D_j,\nu_j\). Let

\[
                         x_E={\theta_j\over D_j}
 \qquad(E\in\mathscr E_j),                                 \tag{3.1}
\]

where

\[
                         \theta_j\ge0,\qquad\sum_j\theta_j=1. \tag{3.2}
\]

Thus orbit \(j\) contributes owner degree \(\theta_j\), and the complete
fractional owner degree is one. Put

\[
                         \eta_j={R_j\nu_j\over W}.          \tag{3.3}
\]

### Theorem 3.1 (orbit-mixture weighted bound)

For every nonnegative weight \(w\) on the whole catalogue,

\[
 \boxed{
 w\cdot x
 \le
 \left(\sum_{j:\theta_j>0}{\theta_j\over\eta_j}\right)
 \alpha_w(G),}                                            \tag{3.4}
\]

where \(G\) is the full conflict graph, including cross-orbit conflicts.

#### Proof

Apply Theorem 1.1 inside orbit \(j\):

\[
 {\theta_j\over D_j}\sum_{E\in\mathscr E_j}w_E
 \le{\theta_j\over\eta_j}
       \alpha_w(G[\mathscr E_j]).
\]

Every stable set in the induced graph is stable in the full graph, so

\[
                         \alpha_w(G[\mathscr E_j])
                         \le\alpha_w(G).
\]

Sum over \(j\). \(\square\)

### Corollary 3.2

If

\[
                         \eta_j\ge1-\delta
\]

for every positive-mass orbit, then

\[
                         w\cdot x\le{1\over1-\delta}\alpha_w(G). \tag{3.5}
\]

In particular, \(\delta=o(1/H)\) proves the coefficient-scale weighted
rank inequality.

The requirement is a near-perfect matching relative to the entire owner
layer in every orbit, not merely a matching of size
\(\theta_jW/R_j\). If only \(\eta_j\asymp\theta_j\), the right side of
(3.4) can lose one unit for every positive-mass orbit.

This does not say that separate near-perfect matchings are necessary.
A single stable family mixing several orbits can be much better than every
induced-orbit stable set. It says that separate orbit matching numbers are
a clean sufficient criterion only in the full near-perfect regime.

## 4. A composite-factor symmetrization

The more efficient object for radius classes is one stable family which
already mixes their decorations correctly.

Let \(\mathcal F\) be a stable route family covering \(W-L\) owners.
Average its coordinate translates and let \(\bar x\) be the resulting
route vector. Then

\[
                         \sum_{E:X\in M(E)}\bar x_E
 ={W-L\over W}                                             \tag{4.1}
\]

at every owner \(X\). Scale to owner degree one:

\[
                         x={W\over W-L}\bar x.              \tag{4.2}
\]

### Proposition 4.1 (composite-factor weighted rank)

For every \(w\ge0\),

\[
 \boxed{
                         w\cdot x
 \le {W\over W-L}\alpha_w(G).}                             \tag{4.3}
\]

#### Proof

The vector \(\bar x\) is a convex combination of stable-set incidence
vectors, so \(\bar x\in\operatorname {STAB}(G)\). Hence

\[
                         w\cdot\bar x\le\alpha_w(G).
\]

Scale by (4.2). \(\square\)

This proposition permits one integral decorated factor to contain many
radius or frame orbits. It is the correct symmetrization interface for a
Catalan radius census. The hard theorem is the existence of
\(\mathcal F\); symmetrization itself loses only \(L/W\).

## 5. Known recursive strip factors certify the owner inequality

Fix one coordinate perfect matching of the \(2m\) ground points. For a
middle owner \(X\), let \(S(X)\) be the number of split coordinate pairs.
Once the full, empty, and split pair indices are fixed, the orientations
of the \(s=S(X)\) split pairs form \(Q_s\).

Let \(\ell\) be a power of two. In every stratum with \(s\ge\ell\), choose
\(\ell\) active split-pair directions. Fiber \(Q_s\) over the remaining
\(s-\ell\) orientations. The recursive \(F_\ell\)-factor partitions every
active \(Q_\ell\)-fiber into \(2\ell\)-cycles. Thus all owners with
\(S(X)\ge\ell\) are partitioned into embedded recursive necklaces.

Every such necklace is a coordinate relabeling of one core-lifted base
necklace: its fixed core has size \(m-\ell\), and its active supports are
\(\ell\) disjoint coordinate pairs. Hence all selected cycles lie in the
unrestricted owner route orbit.

### Lemma 5.1 (exponentially small untileable owner tail)

If \(\ell=o(m)\), then

\[
 \boxed{
 |\{X:S(X)<\ell\}|\le We^{-c m}}                           \tag{5.1}
\]

for some absolute \(c>0\) and all sufficiently large \(m\).

#### Proof

For a uniformly random middle owner and one fixed coordinate pair,

\[
 \Pr(\text{the pair is split})
 =2{\binom{2m-2}{m-1}\over\binom{2m}{m}}
 ={m\over2m-1}.
\]

Therefore

\[
                         \mathbb ES(X)={m^2\over2m-1}
                         ={m\over2}+O(1).
\]

Expose a uniform random permutation and take its first \(m\) coordinates
as \(X\). A transposition in the exposure changes \(S(X)\) by at most two.
The bounded-difference inequality for random permutations gives

\[
 \Pr\left(S(X)\le{\mathbb ES(X)\over2}\right)
 \le e^{-c m}.
\]

Since \(\ell=o(m)\), eventually
\(\ell<\mathbb ES(X)/2\), proving (5.1). \(\square\)

### Theorem 5.2 (owner-only weighted rank)

For the unrestricted owner-conflict orbit of recursive
\(2\ell\)-necklaces,

\[
 \boxed{
 {1\over D}\sum_Ew_E
 \le\bigl(1+e^{-\Omega(m)}\bigr)\alpha_w(G_{\rm own})
 \qquad(w\ge0).}                                          \tag{5.2}
\]

#### Proof

The fixed-frame strip factor above is an owner-disjoint orbit matching
covering all but the exceptional set in (5.1). Apply Corollary 1.2.
\(\square\)

Thus edge transitivity plus a known exact strip factor completely settles
the weighted owner-packing inequality. No blossom or iterative-rounding
loss remains on the undecorated owner layer.

## 6. The exact loss from unthinned multidepth decoration

The recursive cycle factor is internally lower- and upper-shadow injective
through depth \(\ell/2\). In particular, at any fixed \(q\le H\), one
route has \(R=2\ell\) distinct lower targets.

Let \(G_q^-\) join two routes if they share an owner or a physical lower
depth-\(q\) target. Any stable family \(I\) in \(G_q^-\) therefore has

\[
                         R|I|\le N_q,
\]

where

\[
                         N_q=\binom{2m}{m-q}.
\]

Hence

\[
 \boxed{
 \alpha(G_q^-)\le{N_q\over R}.}                           \tag{6.1}
\]

On the other hand, the symmetric orbit point has total route mass

\[
                         \sum_Ex_E={|\mathscr E|\over D}
                         ={W\over R}.                      \tag{6.2}
\]

### Theorem 6.1 (unthinned decorated weighted obstruction)

For the unit route weight,

\[
 \boxed{
 {\sum_Ex_E\over\alpha(G_q^-)}
 \ge{W\over N_q}.}                                         \tag{6.3}
\]

If \(q/\sqrt m\to a>0\), then

\[
                         {W\over N_q}\longrightarrow e^{a^2}. \tag{6.4}
\]

Thus the weighted rank inequality fails by a fixed positive factor at
every positive Gaussian depth.

#### Proof

Combine (6.1)--(6.2). The asymptotic follows from

\[
 \log{W\over N_q}
 ={q^2\over m}
 +O\left({q\over m}+{q^3\over m^2}\right).
\]

\(\square\)

The obstruction uses only the target count. It applies even when:

* every individual cycle is perfectly shadow-rainbow;
* all coordinate pair frames are allowed;
* the route orbit is edge-transitive;
* owner pair-codegrees are \(o(D)\).

At \(q=\sqrt{m\log m}\), the loss grows as \(m^{1+o(1)}\).

## 7. Why the known strip factor does not certify the decorated inequality

The strip factor in Section 5 selects almost \(W/R\) cycles and every one
of their \(W-o(W)\) owner positions advertises a depth-\(q\) shadow.
There are only \(N_q\) physical targets. Consequently the factor cannot be
stable in \(G_q^-\) once \(N_q<W-o(W)\).

Within one active \(Q_\ell\)-fiber, recursive shadow injectivity removes
internal collisions. It does not alter the global source/target census.
Across fibers and pair-type strata, target collisions are compulsory in
the unthinned normalization.

For the direct SCD route, the correct certified domain at depth \(q\) has
size \(N_q\). Equivalently, exactly \(W-N_q\) owner occurrences must have
radius below \(q\). A useful decorated cycle factor must therefore carry a
radius census satisfying

\[
 \#\{\text{certified owner positions at depth }q\}=N_q
 \qquad(1\le q\le H).                                     \tag{7.1}
\]

The fixed-frame recursive strip factor supplies no such radius labels.
Nor is its cycle partition known to be radius-pure for an external SCD
certificate. Thus Theorem 5.2 is owner-only.

For literal MWB the issue is different: all \(W\) occurrences remain, but
target multiplicities should be balanced around \(W/N_q\). In that setting
the target-conflict graph is intentionally too strong and must be replaced
by target clones or floor/ceiling capacities. The owner symmetrization
theorem remains valid, but Theorem 6.1 should not be misread as an MWB
obstruction.

## 8. Are near-perfect matching numbers for the separate radius orbits enough?

Suppose a fractional Catalan mixture assigns owner-degree mass
\(\theta_j\) to decorated orbit \(j\). Theorem 3.1 gives the sufficient
factor

\[
                         \sum_j{\theta_j\over\eta_j}.
\]

If every \(\eta_j=1-o(1/H)\), the answer is yes. But a high-radius orbit
in which every route position is certified at depth \(q\) has, by
Theorem 6.1,

\[
                         \eta_j\le{N_q\over W}<1.
\]

Thus separate full near-perfect matchings in such orbits are impossible.

A matching of only \(\theta_jW/R_j\) routes gives
\(\eta_j\approx\theta_j\). Substitution into (3.4) pays approximately one
unit for every positive-mass radius orbit, which is fatal when their number
grows. Separate matching numbers at the desired class sizes therefore do
not prove the common weighted inequality.

The valid replacement is Proposition 4.1: construct one composite stable
family containing all radius classes in the Catalan proportions. Its
coordinate orbit then gives the joint fractional marginals and the full
weighted inequality with only the common owner leave \(L/W\).

## 9. Iterative-rounding consequence

For a single transitive orbit, the weighted problem has now disappeared:
it is enough to prove

\[
 \boxed{
 \nu(G)\ge {W-o(W/H)\over R}.}                            \tag{9.1}
\]

Any constructive proof of (9.1)—nibble, absorption, switching, or an exact
factor—immediately implies all nonnegative weighted rank inequalities by
Theorem 1.1.

For the decorated radius mixture, the corresponding statement is:

> Construct one target-rainbow, owner-disjoint composite route family with
> the Catalan radius census, all lower and upper depths served by the same
> cycles, and \(o(W/H)\) uncovered owners.

Proposition 4.1 then performs the complete weighted rounding. There is no
additional adversarial weight to handle.

The known exact strip factor proves (9.1) only for \(G_{\rm own}\). The
unthinned decorated graph has the obstruction (6.3), while no
radius-resolved composite factor is currently known.

## 10. Exact implication boundary

The following statements are proved.

1. On a route-transitive orbit, one near-perfect matching controls every
   nonnegative route weight with exact factor \(W/(R\nu)\).
2. Owner leave \(o(W/H)\) is necessary and sufficient for the
   \(1+o(1/H)\) weighted rank inequality at the symmetric orbit point.
3. The orbit-mixture bound is (3.4).
4. One composite decorated factor is stronger and cleaner than separate
   radius-orbit matchings.
5. Known recursive fixed-frame strip factors give exponentially small
   owner leave and therefore prove the owner-only weighted inequality.
6. Naive all-depth decoration has the weighted obstruction (6.3), equal
   asymptotically to \(e^{a^2}\) at \(q\sim a\sqrt m\).
7. Known strip factors do not supply the necessary radius census or
   cross-cycle physical target resolution.

The following statements are not proved.

1. A radius-resolved composite matching with \(o(W/H)\) owner leave.
2. The decorated common-route weighted rank inequality.
3. A coefficient-one construction.

Thus edge-transitive symmetrization fully removes the weighted issue once
the correct approximate factor exists. The remaining loss is not weighted
duality; it is the construction of one integral, radius-thinned,
multidepth-rainbow route factor.
