# Phase-column hashing: affordable calibration, but no singleton cure

## 0. Verdict

A phase-column sparsification has a real entropy advantage:

\[
 p_{\rm phase}=\frac{g!}{g^g}
 =\exp(-g+O(\log g)),
\]

so the original catalogue degree
\(D=\exp(\Theta(g\log m))\) remains exponential after thinning.  The
thinning preserves every calibrated tag and target degree.

However, this affordable hash colors **occurrences**, not physical targets.
It leaves every singleton path intersection intact and therefore does not
remove the projective-plane obstruction.

If one strengthens an **iid target hash** so that a physical target has one
globally consistent phase color, a path with \(K\asymp gQ\) claimed targets
survives with probability at most

\[
 p_{\rm physical}\le g!\,g^{-K},
\]

which annihilates the catalogue because \(Q\to\infty\).  Thus there is a
sharp dichotomy:

* affordable phase rainbows preserve calibration but do not change the
  physical conflict hypergraph;
* a target-consistent \(g\)-partition attacks singleton conflicts but costs
  \(e^{-\Theta(K\log g)}\), which is fatal.

This iid dichotomy has an important structured exception.  A coordinate
subset-sum hash with affine labels on the \(a\)- and \(b\)-strings
correlates all row colors using only \(O(g)\) coordinate equations.  It is
audited separately in
MATH_ATTACK_AFFINE_HASH_FIBRE_AND_PROJECTIVE_AUDIT_20260725.md.  The iid
calculation below does not rule it out.  Even that affine hash, however,
still needs a geodesic-specific singleton-dispersal theorem.

---

## 1. The affordable occurrence-phase hash

Let a decorated path \(P\) have \(g\) physical phase columns.  Independently
for every path copy and every one of its phases, choose a color uniformly
from \([g]\).  Retain \(P\) when its \(g\) colors are all distinct.

### Proposition 1.1 (exact survival probability)

\[
 \boxed{
 \Pr(P\text{ is retained})
 =p_g:=\frac{g!}{g^g}
 =\sqrt{2\pi g}\,e^{-g}(1+o(1)).}
 \tag{1.1}
\]

This is immediate: there are \(g^g\) color strings and \(g!\) bijective
ones.

Let \(F\) be any calibrated fibre: a tag fibre, or the fibre of paths
claiming one fixed signed target.  Since the rainbow event depends only on
the new independent occurrence colors,

\[
 \boxed{\mathbb E|F_{\rm rb}|=p_g|F|.}
 \tag{1.2}
\]

In particular, all tag and target ratios are unchanged in expectation.

The events are independent between distinct decorated path copies.  Hence
for every \(0<\delta<1\),

\[
 \Pr\bigl(\,||F_{\rm rb}|-p_g|F||>\delta p_g|F|\,\bigr)
 \le2\exp\!\left(-\frac{\delta^2p_g|F|}{3}\right).
 \tag{1.3}
\]

In the full geodesic catalogue

\[
 \log D=\Theta(g\log m),
 \qquad
 \log(p_gD)=\Theta(g\log m).
 \tag{1.4}
\]

Thus \(p_gD\) is superexponentially larger than the logarithm of the total
number of tag and protected-target fibres.  A union bound in (1.3) gives a
deterministic occurrence-phase sparsification for which every calibrated
fibre is

\[
 (1\pm o(1))p_g
 \tag{1.5}
\]

times its original size.  So the row-calibration question has a positive
answer at the occurrence level.

---

## 2. Why this is not a physical \(g\)-partition

Suppose paths \(P,E\) share a physical target \(S\), occurring in phase
\(i\) of \(P\) and phase \(j\) of \(E\).  The two occurrence colors were
chosen independently.  Conditioning on both paths being rainbow changes
neither physical support.  Therefore

\[
 \boxed{
 P,E\text{ still share }S\text{ with probability }1.}
 \tag{2.1}
\]

Their two *occurrence copies* of \(S\) may carry different palette colors,
but allowing the two colors to act as different resources would permit the
same physical target to be used twice.  Projecting back to the Boolean
target restores the original conflict.

Equivalently, the lifted occurrence hypergraph is \(g\)-partite, but the
map from its colored target occurrences to physical targets is many-to-one.
A matching in the lift is not necessarily a matching after this
projection.  The projection's duplicate ledger is exactly the original
singleton-intersection problem.

The same conclusion holds for a global hash of middle owners followed by
the condition that the \(g\) owners of a path are rainbow.  That gives a
genuine \(g\)-partition of the owner resources, but a lower or upper target
can occur under differently colored owners in different paths.  It does
not partition the physical target resources.

---

## 3. Iid target-consistent phase colors are fatal

Now give every physical protected target \(S\) one independent uniform
color \(h(S)\in[g]\).  A path chooses a bijection

\[
 \pi:\{\text{its }g\text{ phases}\}\longrightarrow[g]
\]

and is admissible only if every claimed target in phase \(t\) has color
\(\pi(t)\).

Every protected path claims \(K\asymp gQ\) distinct targets.  For a fixed
\(\pi\), all \(K\) color equations are independent, so its survival
probability is \(g^{-K}\).  Union bounding over the \(g!\) possible phase
bijections gives

\[
 \boxed{
 p_{\rm phys}\le g!\,g^{-K}.}
 \tag{3.1}
\]

Since \(K\asymp gQ\),

\[
\begin{aligned}
 \log(Dp_{\rm phys})
 &\le
 \Theta(g\log m)+g\log g-K\log g\\
 &=
 -\Theta(gQ\log g),
\end{aligned}
 \tag{3.2}
\]

because \(Q\to\infty\) and, in the calibrated regime,
\(Q\log g\gg\log m\).  Hence

\[
 \boxed{Dp_{\rm phys}=o(1).}
 \tag{3.3}
\]

With high probability a typical tag has no target-consistently colored
path at all.  This is the target-level \(e^{-K}\) obstruction in its exact
phase-palette form.

More generally, if a phase may use a palette of \(b<g\) colors but every
physical target has a fixed palette membership, the cost is still
\(\exp[-\Theta(K)]\) unless the target palettes occupy a
\(1-o(1/Q)\) fraction of all colors.  In that latter regime the palette
does not significantly thin singleton conflicts.

---

## 4. The projective-plane obstruction survives affordable phase rainbows

The failure is not merely a missing proof.

Take the projective-plane tag-target hypergraph: in one plane, underlying
edges are the lines, every two lines meet in one physical target, and every
tag has a calibrated family of choices.  Partition the private targets of
each edge arbitrarily into \(g\) phase columns, and include many parallel
decorated copies carrying every phase permutation.

Apply the occurrence-phase rainbow thinning of Section 1.  Every underlying
line retains the same asymptotic fraction \(p_g\) of its parallel copies,
so all tag and target degrees remain calibrated.  Nevertheless, any two
retained underlying lines in the same plane still meet in their unique
physical projective point.  Therefore a physical matching still uses at
most one of them.

In particular:

\[
 \boxed{
 \text{internal phase-rainbow calibration does not improve the
 projective matching ratio.}}
 \tag{4.1}
\]

The nonlinear width-two moment remains zero in this example, exactly as
before: all distinct physical intersections are singletons.

This abstract construction is not asserted to be a geodesic subcatalogue.
It proves that “calibrated \(g\)-partite phase sparsification” by itself is
not the missing theorem.  Any successful use of phases must invoke an
additional property of the actual geodesic incidence, such as the
column-link dispersal bound, and must keep that property hereditary under
the residual weighting.

---

## 5. What a useful phase palette would have to prove

The affordable hash can be retained as an entropy reserve.  To affect the
physical singleton obstruction, it needs a separate reconciliation theorem
of the following form.

> **Physical phase-reconciliation theorem.**  Select one affordable
> occurrence-rainbow path on almost every tag and reconcile its colored
> target occurrences so that
> \[
>  \sum_S(r_S-1)_+=o(W),
> \]
> while changing or discarding only \(o(W/g)\) phase columns.

The projective-plane lift above shows that this statement cannot follow
from internal rainbowness and calibrated degrees alone.  For the geodesic
catalogue it would have to follow from the actual ordered column links.

Thus occurrence-phase hashing preserves the exponential catalogue and
calibrated row loads, but by itself does not control either term of the
current propagation gate.  The affine coordinate-hash exception changes
the entropy conclusion of Section 3, not the abstract projective-plane
warning of Section 4:

\[
 \sum_t\left(
 \frac{\mathscr E_t}{\eta_t^2}
g\alpha^2\mathscr B_t
 \right).
\]
