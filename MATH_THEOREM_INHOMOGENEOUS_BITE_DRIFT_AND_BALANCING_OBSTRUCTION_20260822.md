# Inhomogeneous isolated-edge bites: exact drift and a balancing obstruction

**Date:** 2026-08-22  
**Status:** unconditional identities and finite counterexample; no claim that
the punctured process attains the counterexample

This note tests a natural bypass for Gate A: replace uniform edge marking by
edge-dependent marking rates chosen from the current residual.  There are two
main conclusions.

1.  The first-order normalized degree drift under arbitrary rates has an
    exact linear form.  If all target deletion hazards are balanced, the only
    remaining nonuniform term is a duplicate-exposure average.
2.  Balanced target deletion and balanced normalized degree drift are not
    simultaneously feasible in every regular hypergraph.  The disjoint union
    of the Fano plane and `K_4^(3)` is an exact obstruction, even though every
    vertex initially has degree three.  Exposure-aware rates can cancel the
    drift only by making the target deletion hazards differ by a factor four.

Thus arbitrary edge weights do repair the old *degree-only* objection in one
sense, but they do not provide a generic self-regularizing bite.  Any positive
punctured-hypergraph implementation must exploit its geometry to balance both
the target loads and the duplicate-exposure rows (or deliberately prioritize
different regions and prove that this does not create a large leave).

## 1. Arbitrary marking rates

Let `H=(V,E)` be a finite simple `k`-uniform hypergraph with

\[
             n=|V|,\qquad Z=|E|,\qquad d(v)>0.
\]

Give every edge `G` a nonnegative rate `lambda_G`.  For sufficiently small
`t>=0`, mark the edges independently with probabilities `t lambda_G`, accept
a marked edge exactly when no other marked edge intersects it, and delete the
vertices of all accepted edges.  Put

\[
 \Lambda=\sum_G\lambda_G,\qquad
 q_v=\sum_{G\ni v}\lambda_G,\qquad
 h_F=\sum_{G:G\cap F\ne\varnothing}\lambda_G.       \tag{1.1}
\]

The quantity `q_v` is the infinitesimal deletion hazard of `v`, while `h_F`
is the infinitesimal destruction hazard of `F`.  Define

\[
 e_v={1\over d(v)}\sum_{F\ni v}h_F-q_v,\qquad
 \bar h={1\over Z}\sum_F h_F,\qquad
 c=\bar h-{k\Lambda\over n}.                        \tag{1.2}
\]

Let `M_v(t)` be the expected residual degree of `v` conditional on `v`
surviving, and use the annealed empirical scale

\[
                  \bar d^{\rm ann}(t)
        ={k\,\mathbb E Z_t\over\mathbb E|V_t|}.      \tag{1.3}
\]

### Theorem 1.1 (inhomogeneous rooted drift)

For every `v`,

\[
 \boxed{
 {d\over dt}\log {M_v(t)\over\bar d^{\rm ann}(t)}\bigg|_{t=0}
       =-(e_v-c).}                                   \tag{1.4}
\]

#### Proof

To first order there is at most one mark, and a unique marked edge is
accepted.  Hence an edge `F` survives with derivative `-h_F`, while a target
`v` survives with derivative `-q_v`.  The unconditional rooted-degree
numerator is

\[
       \sum_{F\ni v}\Pr(F\text{ survives}),
\]

so logarithmic differentiation after division by the target-survival
probability gives

\[
                    {d\over dt}\log M_v(t)\bigg|_0=-e_v.       \tag{1.5}
\]

Similarly,

\[
 {d\over dt}\mathbb E Z_t\bigg|_0=-\sum_Fh_F,
 \qquad
 {d\over dt}\mathbb E|V_t|\bigg|_0=-k\Lambda,       \tag{1.6}
\]

because one accepted edge removes exactly `k` targets.  Thus

\[
              {d\over dt}\log\bar d^{\rm ann}(t)\bigg|_0=-c.
\]

Subtracting proves (1.4).  \(\square\)

The identity has a useful duplicate-exposure form.  For a current edge `F`
put

\[
 R_F=\sum_G\lambda_G\bigl(|F\cap G|-1\bigr)_+.       \tag{1.7}
\]

Since

\[
 \sum_{u\in F}q_u
 =\sum_G\lambda_G|F\cap G|
 =h_F+R_F,
\]

we have the exact identity

\[
                         h_F=\sum_{u\in F}q_u-R_F.   \tag{1.8}
\]

### Corollary 1.2 (what balanced target loads leave open)

If `q_v=q` for every target, then

\[
 \boxed{
 e_v=(k-1)q-\rho_v,
 \qquad
 \rho_v={1\over d(v)}\sum_{F\ni v}R_F.}             \tag{1.9}
\]

Thus equal deletion hazards do not equalize normalized degree drift unless
the duplicate-exposure averages `rho_v` are also equal.

The same calculation works without change for several shores.  If every
edge has `k_sigma` vertices in shore `sigma` and every target in that shore
has load `q_sigma`, then, for `v` in shore `sigma`,

\[
 e_v=\sum_\tau k_\tau q_\tau-q_\sigma-\rho_v.        \tag{1.10}
\]

## 2. An exact incompatibility

Let `P` be the seven-edge Fano plane on seven vertices, and let `T=K_4^(3)`
be the four triples on a four-element set.  Take their vertex-disjoint union

\[
                              H=P\,\dot\cup\,T.       \tag{2.1}
\]

It is a simple `3`-uniform hypergraph with eleven vertices and eleven edges.
Every vertex has degree three.  Every two edges inside either component
intersect.

### Theorem 2.1 (marginal balance and drift balance are incompatible)

For arbitrary nonnegative edge rates on `H`, consider the following two
requirements.

1. **Target balance:** `q_v` has one common value on all eleven vertices.
2. **Rooted erosion balance:** `e_v` has one common value on all eleven
   vertices.

Both requirements hold simultaneously only for the zero rate vector.

More explicitly:

- target balance with common value `q` forces every edge of both components
  to have rate `q/3`; then
  \[
                    e_v={4q\over3}\quad(v\in P),
             \qquad e_v={q\over3}\quad(v\in T);      \tag{2.2}
  \]
- rooted erosion balance forces constant componentwise rates `a` on `P` and
  `b` on `T`, with
  \[
                                  b=4a;               \tag{2.3}
  \]
  the corresponding target hazards are `3a` and `12a`.

#### Proof

Let `B_P` be the point-edge incidence matrix of the Fano plane.  Distinct
points lie on one common line and every point lies on three lines, so

\[
                          B_PB_P^T=2I+J.              \tag{2.4}
\]

This matrix is invertible.  Hence constant point loads force a unique edge
rate vector, and symmetry shows that vector is constant.  For `K_4^(3)`,
index each triple by its omitted point.  Its incidence matrix is `J-I`, also
invertible, so the same conclusion holds.  Therefore target balance forces
all eleven edge rates to equal `q/3`.

In an intersecting component, every edge not containing `v` meets every one
of the three edges containing `v`.  Consequently the external form of
(1.2) gives

\[
 e_v=\sum_{G\not\ni v}\lambda_G.                    \tag{2.5}
\]

There are four nonincident Fano edges and one nonincident `K_4^(3)` edge.
Equation (2.2) follows.

Conversely, in either component (2.5) is
`e_v=Lambda_component-q_v`.  If all `e_v` are equal within that component,
then all `q_v` are equal there; invertibility of the two incidence matrices
again makes the edge rates componentwise constant.  With rates `a` and `b`,
equation (2.5) gives `e_v=4a` on `P` and `e_v=b` on `T`.  Equality is exactly
`b=4a`, proving (2.3).  Simultaneous target balance also requires `a=b`, so
`a=b=0`.  \(\square\)

For comparison with the uniform-rate counterexample, set every edge rate to
one.  Then `q_v=3`,

\[
 \bar h={7\cdot7+4\cdot4\over11}={65\over11},
 \qquad {3\Lambda\over n}=3,
 \qquad c={32\over11}.                              \tag{2.6}
\]

Thus `e_v-c=12/11` on the Fano component and `-21/11` on the
`K_4^(3)` component, recovering the opposite rooted drifts exactly.

## 3. A finite-bite warning

The infinitesimal repair `b=4a` does not make the stopped maximum-degree
event disappear.  Mark the Fano edges with probability `ta` and the
`K_4^(3)` edges with probability `tb`, independently, and use isolated-mark
acceptance.  The event

\[
 \mathcal A=\{\text{exactly one Fano edge is marked and no }K_4^{(3)}
                   \text{ edge is marked}\}          \tag{3.1}
\]

has probability

\[
 \Pr(\mathcal A)=7ta(1-ta)^6(1-tb)^4.               \tag{3.2}
\]

On this event the marked Fano edge is accepted, all seven Fano edges are
destroyed, and its three vertices are removed.  The residual consists of
four isolated Fano vertices and the intact `K_4^(3)`.  Hence

\[
       \bar d'={3\cdot4\over8}={3\over2},
       \qquad \Delta'=3,
       \qquad {\Delta'\over\bar d'}=2,               \tag{3.3}
\]

whereas the initial ratio was one.  In particular, with the drift-balancing
choice `b=4a`, the bad event still has probability `7ta+O(t^2a^2)`.

This does not prove that weighted marking is useless.  One may suppress the
Fano rates until the other component is removed, and the punctured residual
has much more geometry than (2.1).  It proves the narrower, exact point:

> a static edge-dependent rate vector, even one which cancels every
> first-order rooted drift, does not by itself provide stopped cap
> preservation.  A viable weighted algorithm also needs a finite-jump
> mechanism (gentle external rows, dependent sampling, or state-separated
> priorities) and a proof that this mechanism retains enough matching
> progress.

The relevant finite jump is explicit.  If one edge `G` is selected from a
current `k`-uniform hypergraph, then for every uncovered `v notin G`,

\[
 d'(v)=d(v)-a_G(v),\qquad Z'=Z-C_G,\qquad n'=n-k,    \tag{3.4}
\]

where `C_G=|{F:F cap G ne empty}|`.  Therefore

\[
 \boxed{
 {d'(v)/\bar d'\over d(v)/\bar d}
 =\left(1-{a_G(v)\over d(v)}\right)
   {1-k/n\over1-C_G/Z}.}                            \tag{3.5}
\]

Identity (3.5) is the exact finite counterpart of Theorem 1.1.  It shows
why controlling only the average rate vector cannot replace a bound on the
realized external row `a_G(v)`.

## 4. Consequence for the punctured Gate A attack

The weighted-bite route has now been reduced to a precise positive object.
At a current punctured residual, one would need rates (or a dependent
matching-valued bite) which simultaneously provide:

1. enough total target load for the same geometric descent;
2. target loads balanced at the shore scale;
3. duplicate-exposure averages balanced at the rooted scale, by (1.9)--(1.10);
4. a finite-jump or high-moment bound for the realized rows in (3.5).

Items 2 and 3 are independent linear constraints, not two formulations of
one constraint.  Item 4 is not implied by their expectation-level solution.
Thus edge-dependent marking has not yet bypassed the stopped scalar in the
current-scale external-row theorem.  The exact obstruction above rules out
declaring the bypass complete merely from a balanced fractional target load
or from cancellation of the infinitesimal rooted drift.
