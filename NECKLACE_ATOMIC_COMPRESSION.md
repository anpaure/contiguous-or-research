# Necklace bundles after chain-atom compression

This note audits the proposed last step in `MIXED_PAIR_ROUNDING.md`:
replace each typed block by its `R=2ell` symmetric-chain segments and then
round in an `R`-uniform hypergraph.  There is a real reduction here, but it
is **not** an ordinary hypergraph matching reduction.  Native chain segments
from different blocks can overlap in one mask without being equal.  The
honest object is an `R`-uniform hypergraph on the middle layer together with
a family of conflict cliques, one clique for every nonmiddle target.

The audit below gives:

* a rigorous obstruction to quotienting native chain segments into ordinary
  atom vertices;
* an exact conflict-system reduction with an exact defect formula;
* the improved `O(1/m^2)` middle codegree after projection; and
* the remaining growing-rank parameters that a new rounding theorem has to
  exploit.

Throughout,

\[
 W=\binom{2m}{m},\qquad R=2\ell,
 \qquad N_q=\binom{2m}{m-q},\qquad \rho_q=N_q/W.
\tag{0.1}
\]

A typed block `(B,d)` has middle cycle

\[
                 B=(X_0,\ldots,X_{R-1})
\tag{0.2}
\]

and decomposes internally as

\[
 e(B,d)=\bigsqcup_{t\in\mathbb Z/R\mathbb Z}
             \mathcal C_t^{(d)},
\qquad
 \mathcal C_t^{(d)}:
 L_d(t)\subset\cdots\subset L_1(t)\subset X_t
 \subset U_1(t)\subset\cdots\subset U_d(t).
\tag{0.3}
\]

The `R` chains in (0.3) are pairwise mask-disjoint **inside one block**.

## 1. Why native chains are not global atoms

An ordinary atom compression would need a global collection of atom
vertices such that two blocks sharing a mask also share an atom vertex.  If
one native chain segment is to cost one atom, intersecting native segments
must therefore be identified.  This immediately degenerates.

### Proposition 1 (the native-atom overlap graph is connected)

Consider the full mixed-pair block family and radius-one native segments.
Make a graph whose vertices are the segments

\[
                 S\subset X\subset U,
\qquad |S|=m-1, |X|=m, |U|=m+1,
\tag{1.1}
\]

that occur in an oriented chain decomposition of a partial pair-flip block,
and join two segment vertices when they share a mask.  For all sufficiently
large `m` (and `ell=o(m)`), this graph is connected.

#### Proof

All available segments centred at the same middle set `X` share the mask
`X`, so they lie in one overlap component.

Now let `X,Y` be Johnson neighbours and put

\[
                 S=X\cap Y,
\qquad X=S\cup\{a\},\quad Y=S\cup\{b\}.
\tag{1.2}
\]

Choose a coordinate perfect matching containing the pair `{a,b}`, make it
active, and choose the active order so that the pair-flip cycle uses the
edge `X Y`.  One of the two orientations gives a native segment centred at
`X` whose lower member is `S`.  Reversing that local orientation, or using a
second partial block with first move out of `Y`, gives a native segment
centred at `Y` with the same lower member `S`.  There are enough remaining
split pairs to extend either prescribed first direction to an `ell`-active
partial block because `ell=o(m)`.  Hence the components belonging to `X`
and `Y` meet.

The Johnson graph `J(2m,m)` is connected, so all middle centres, and thus
all radius-one native segments, lie in one component.  QED.

Every positive-radius segment shares its middle member with a radius-one
segment.  Thus, if all positive radii are considered together, their native
overlap graph is connected as well.

### Corollary 2 (no lossless equality quotient)

There is no nontrivial map `phi` from native positive-radius chain segments
to atom vertices with

\[
 \mathcal C\cap\mathcal C'\ne\varnothing
       \quad\Longrightarrow\quad
 \phi(\mathcal C)=\phi(\mathcal C')
\tag{1.3}
\]

that turns every typed block into `R` useful atom vertices.  Condition
(1.3) forces `phi` to be constant.

This is the precise defect in the phrase "regard each whole chain segment
as one atomic vertex."  It is valid within one block, but not across the
reservoir.

## 2. A fixed SCD is not a free repair

A fixed global symmetric-chain decomposition would remove the preceding
problem: its chains are globally disjoint.  However, a partial pair block
can use one such chain as a native atom only when the coordinate pairing
contains all paired downward/upward labels of that chain.

Fix a middle set `X` and a prescribed radius-`d` flag

\[
 r_0,\ldots,r_{d-1}\in X,
 \qquad
 u_0,\ldots,u_{d-1}\notin X,
\tag{2.1}
\]

with all labels distinct.  A pair-flip block realizing the shift flag must
pair `r_i` with `u_i` for every `i<d` (up to a common reversal of the flag).
For a uniform random coordinate perfect matching `P`,

\[
 \Pr\bigl(\{r_i,u_i\}\in P\text{ for every }i<d\bigr)
 =\frac{(2m-2d-1)!!}{(2m-1)!!}
 =\prod_{i=0}^{d-1}\frac1{2m-(2i+1)}.
\tag{2.2}
\]

Consequently, a reservoir of `J=m^C` independent coordinate matchings
supports this prescribed flag with probability at most

\[
          J(2m-2d+1)^{-d}.
\tag{2.3}
\]

For `d=Theta(sqrt(m))`, (2.3) is smaller than every inverse polynomial.
Moreover,

\[
 \rho_{\lfloor x\sqrt m\rfloor}
       =\exp(-x^2+o(1)),
\tag{2.4}
\]

so the SCD radius law assigns a positive fraction of all middle sets to
every fixed interval `a sqrt(m)<=d<=b sqrt(m)` with `0<a<b`.  It follows
that a preassigned SCD is, with high probability, incompatible with a
polynomial random reservoir on a macroscopic part of its relevant chains.

This does **not** rule out constructing an SCD after seeing the reservoir.
It shows that doing so is the unresolved wreath-resolved-SCD theorem itself,
not a preprocessing step that can be inserted for free.

## 3. The honest `R`-uniform reduction

Let `H_0` be the labelled multihypergraph whose vertex set is the middle
layer and whose edge associated with a typed block `(B,d)` is

\[
                       \bar e(B,d)=\{X_0,\ldots,X_{R-1}\}.
\tag{3.1}
\]

The label `d` is retained; parallel projected edges with different labels
are allowed.

For every nonmiddle target `S` in the certified band define

\[
 \mathcal F_S=\{(B,d):S\in e(B,d)\}.
\tag{3.2}
\]

Regard every two distinct members of `F_S` as a forbidden pair.  Thus each
`F_S` is a conflict clique on the edge set of `H_0`.

### Proposition 3 (exact conflict reduction)

A collection `M` of typed blocks is pairwise disjoint as a collection of
mask sets if and only if

1. the projected edges `bar e`, `e in M`, form a matching in `H_0`; and
2. `|M intersect F_S|<=1` for every nonmiddle certified target `S`.

#### Proof

A repeated middle mask is exactly an intersection of two projected edges.
A repeated nonmiddle mask is exactly membership of the same two typed edges
in `F_S` for that mask.  Inside one typed edge all masks are distinct by
(0.3).  These are all possible intersections.  QED.

This is a genuine compression from mask rank
`R(1+2d)` to base rank `R`, but only at the cost of retaining the conflict
system (3.2).

## 4. Exact coverage accounting after compression

Put

\[
 n_{\ge q}(\mathcal M)
   =|\{e\in\mathcal M:d(e)\ge q\}|.
\tag{4.1}
\]

If `M` is conflict-free, every selected label-`d` edge contributes exactly
`R` distinct masks at each rank `m-q` and `m+q`, for every `1<=q<=d`.
Therefore the number of uncovered masks in the whole certified band is
**exactly**

\[
 \boxed{
 D(\mathcal M)
  = W-R|\mathcal M|
    +2\sum_{q=1}^{h}\bigl(N_q-Rn_{\ge q}(\mathcal M)\bigr).}
\tag{4.2}
\]

Every summand is nonnegative: conflict-freeness makes all contributed masks
at that rank distinct.

Hence the necklace-bundle rounding theorem is equivalent to finding a
conflict-free matching in `H_0` for which (4.2) is `o(W)`.  Merely covering
`(1-o(1))W` middle vertices is not enough.  Since a typical selected chain
has radius `Theta(sqrt(m))`, an uncontrolled middle defect `epsilon W` can
create `Theta(epsilon W sqrt(m))` mask defect.  The matching process needs
weighted/color-balanced defect `o(W)`, exactly as (4.2) records.

The ideal label tails are

\[
 \frac{R n_{\ge q}}W=\sum_{d\ge q}p_d=\rho_q.
\tag{4.3}
\]

Thus (4.2), rather than separate per-rank estimates, is the right statistic
to preserve in a nibble or absorption argument.

## 5. Degree and codegree audit

Use the scaled weights from Theorem 4 of `MIXED_PAIR_ROUNDING.md`, with its
polynomial concentration exponent chosen larger than any fixed constant
needed below.

### Base middle hypergraph

Every middle vertex has weighted degree `1+o(1)`.  If two middle masks
`X,Y` have Johnson distance `t>=1`, formula (4.7) of that note, with `a=0`,
gives

\[
 \deg_w(X,Y)
   \leq\frac{2}{\binom mt^2}+o(m^{-2})
   \le \frac{2+o(1)}{m^2}.
\tag{5.1}
\]

This is a full factor `m` smaller than the worst target codegree in the
uncompressed typed hypergraph.

After thinning to an ordinary polynomial degree `Delta` (and taking the
concentration error `o(Delta/m^2)`), the projected hypergraph has

\[
 d_{H_0}(X)=(1+o(1))\Delta,
 \qquad
 \Delta_2(H_0)\le(2+o(1))\Delta/m^2.
\tag{5.2}
\]

Since `R=2ell=o(m)`,

\[
             R^2\frac{\Delta_2(H_0)}\Delta
                  =O(\ell^2/m^2)=o(1).
\tag{5.3}
\]

Thus the projective-plane obstruction from the original growing-rank
hypergraph disappears at the level of the **base** matching problem.  A
projective plane of rank `R` has relative codegree `Theta(1/R)`, whereas
(5.2) is `O(1/m^2)=o(1/R)`.

### Conflict cliques

For every nonmiddle target `S`,

\[
                   |\mathcal F_S|=(1+o(1))\Delta.
\tag{5.4}
\]

For two distinct targets `S,T` in the certified band, the same-rank,
nested, and nonnested calculations in Theorem 4 give

\[
 |\mathcal F_S\cap\mathcal F_T|
       \le \left(\frac{2}{m-h}+o(1/m)\right)\Delta.
\tag{5.5}
\]

The same bound holds for the mixed incidence of one middle vertex and one
nonmiddle conflict clique.

A label-`d` projected edge belongs to exactly

\[
                         K_d=2Rd
\tag{5.6}
\]

nonmiddle target cliques.  Consequently its conflict-graph degree is at
most

\[
                 (1+o(1))\,2Rd\Delta
                 \le (1+o(1))\,2Rh\Delta.
\tag{5.7}
\]

Under the radius law,

\[
 \mathbb E d=\sum_{q\ge1}\rho_q
       =\left(\frac{\sqrt\pi}{2}+o(1)\right)\sqrt m,
\tag{5.8}
\]

so the average number of conflict cliques incident with one projected edge
is

\[
              (\sqrt\pi+o(1))R\sqrt m
              =(2\sqrt\pi+o(1))\ell\sqrt m.
\tag{5.9}
\]

Equations (5.2)--(5.9) are the audited parameters of the compressed object:

\[
\begin{array}{c|c}
\text{object}&\text{parameter}\\ \hline
\text{base edge rank}&R=2\ell=o(m)\\
\text{base relative pair-codegree}&O(m^{-2})\\
\text{target-clique relative pair-codegree}&O(m^{-1})\\
\text{conflict cliques met by a typical edge}&\Theta(R\sqrt m)\\
\text{conflict cliques met by a maximum-radius edge}&O(Rh).
\end{array}
\tag{5.10}
\]

The base hypergraph is now in a plausible growing-rank nibble regime.  The
unresolved issue is the simultaneous clique avoidance and the much stronger
weighted defect requirement (4.2).  Treating the chain atoms as independent
would lose precisely the nested geometry needed to control (5.5)--(5.9).

## 6. Correct successor theorem

The SCD-atomic proposal should therefore be split into two logically
different statements.

1. **Reservoir-adapted SCD theorem.**  Construct a global SCD whose relevant
   chains are native segments of the reservoir and whose middle projections
   bundle into pair-flip necklaces.  This removes every conflict clique, but
   it is exactly the shift-compatible wreath-resolved-SCD problem; Section 2
   shows that an arbitrary preassigned SCD will not do.

2. **Atomic conflict-rounding theorem.**  In the `R`-uniform hypergraph
   `H_0` with constraint families `F_S`, find a conflict-free matching with
   `D(M)=o(W)` in (4.2), using the nested-chain and common-necklace geometry
   in addition to the numerical bounds (5.10).

The second statement is the honest lower-uniformity reformulation.  It is
strictly more informative than the original `Theta(ell sqrt(m))`-uniform
matching formulation, because it isolates an easy-looking base matching
with `O(m^{-2})` codegree from a structured family of rank-two conflicts.
But it is not yet a theorem obtainable from existing fixed-rank
conflict-free nibble results: both `R` and the number `Theta(R sqrt(m))` of
constraints touched by one edge grow.

The next mathematical attack should be a tailored alternating-necklace
switching or absorption lemma that repairs one conflict clique while
changing only `O(R)` middle atoms and preserving the tail counts in (4.2).
Without such a lemma, "compress to chain atoms and apply Pippenger" is not a
valid proof.

## 7. Audit against existing conflict-free matching theorems

The closest black-box result is Glock--Joos--Kim--Kuehn--Lichev,
[*Conflict-free hypergraph
matchings*](https://arxiv.org/abs/2205.05564).  It does not presently apply,
for three separate reasons.

First, its main theorem fixes the base uniformity before the degree tends to
infinity.  Here the base uniformity is

\[
                         k_0=R=2\ell\longrightarrow\infty.
\tag{7.1}
\]

No uniform dependence on `k_0` in that theorem covers (7.1).

Second, for a 2-conflict system the theorem requires polynomial savings not
only in the base codegree but also in two localized conflict neighborhoods:
for a base edge `e` and base vertex `v`, the number of conflict-neighbours
of `e` containing `v`, and for two disjoint base edges the size of their
common conflict neighbourhood, must both be at most `Delta^(1-epsilon)`.
For a labelled projected edge `e=bar e(B,d)`, write
`T(e)=e(B,d) setminus binom([2m],m)` for its `K=2Rd` nonmiddle targets.
Our present audit gives only

\[
 \bigl|\{f:f\sim e,\ v\in f\}\bigr|
 \leq
 \sum_{S\in \mathcal T(e)}
   \bigl|\mathcal F_S\cap\{f:v\in f\}\bigr|
 \leq O(K\Delta/m),
\tag{7.2}
\]

which is merely the trivial `O(Delta)` bound once `K>>m`.  The analogous
available bound for common conflict neighbourhoods also has no polynomial
saving.  The nested necklace geometry may improve (7.2), but such an
improvement is exactly a new lemma, not a consequence of pair-codegrees.

Third, the more flexible version of that theorem measures the normalized
conflict degree by a parameter `Gamma`.  From (5.7), the available choice is

\[
                   \Gamma=O(Rh)
\quad\text{(or }\Theta(R\sqrt m)\text{ on average).}
\tag{7.3}
\]

Its parameter tradeoff has the form

\[
                         \mu^{-O(\Gamma)}
                              \leq \Delta^{\varepsilon^2},
\tag{7.4}
\]

where `mu` is the uncovered fraction.  To make the weighted defect (4.2)
`o(W)`, an unstructured argument needs at least `mu=o(m^(-1/2))`.
Even the *full* block reservoir has degree at most

\[
 \Delta_{\rm full}
 \leq (h+1)(2m-1)!!(m)_\ell,
 \qquad
 \log\Delta_{\rm full}=O(m\log m),
\tag{7.5}
\]

whereas `R h=2 ell h=omega(m)` under (0.2).  Substituting
`log(1/mu)=Omega(log m)` in the left side of (7.4) exceeds the logarithmic
budget in (7.5).  Thus merely increasing the reservoir degree cannot make
the known parameter regime apply.

Classical Pippenger--Spencer, Ehard--Glock--Joos, and the other standard
nibble theorems likewise assume fixed edge rank or have error exponents
that deteriorate as the square of the rank.  Projection fixes the numerical
projective-plane obstruction for `H_0`, but no existing theorem combines
growing `R`, the conflict load (5.9), and `o(W)` weighted defect.

## 8. The weakest exact theorem actually needed

Pairwise conflict-freeness is cleaner than necessary.  Repeated represented
masks do not invalidate an OR construction; they only waste slots.  This
gives a still weaker exact target.

For an arbitrary selected multiset `M` of typed blocks, let

\[
 c_S(\mathcal M)=|\{e\in\mathcal M:S\in e\}|,
\qquad
 E(\mathcal M)=\sum_{S\in\mathcal U_h}(c_S(\mathcal M)-1)_+,
\tag{8.1}
\]

where

\[
 \mathcal U_h=\{S:m-h\leq |S|\leq m+h\}
\tag{8.2}
\]

is the certified band.  The total number of certified occurrences emitted
by `M` is

\[
 T(\mathcal M)
  =R|\mathcal M|+2R\sum_{q=1}^h n_{\ge q}(\mathcal M),
\tag{8.3}
\]

and `|U_h|=W+2 sum_(q=1)^h N_q`.  Since

\[
 |\{S:c_S>0\}|=T(\mathcal M)-E(\mathcal M),
\]

the number of uncovered band masks is exactly

\[
 \boxed{
 U(\mathcal M)
  =W+2\sum_{q=1}^hN_q
    -R|\mathcal M|-2R\sum_{q=1}^h n_{\ge q}(\mathcal M)
    +E(\mathcal M).}
\tag{8.4}
\]

Formula (4.2) is the special case `E(M)=0` with a base matching.

Therefore the logically weakest missing rounding statement is:

> **Low-excess necklace rounding.**  Select typed blocks of total physical
> length `R|M|=W+o(W)` such that
> \[
> \left|W+2\sum_{q=1}^hN_q
>       -R|\mathcal M|-2R\sum_{q=1}^h n_{\ge q}(\mathcal M)\right|=o(W)
> \]
> and their total collision excess is `E(M)=o(W)`.

Then only `o(W)` masks in the central band are absent and they may be
appended literally; the already proved outer-tail construction costs
`o(W)` more.  This yields `nu(2m)=W+o(W)`.

Low-excess rounding is strictly weaker than a conflict-free matching:

* projected middle blocks may overlap `o(W)` times in total;
* nonmiddle conflict cliques may be hit repeatedly, provided the total
  excess is `o(W)`; and
* no exact per-rank quota is needed beyond the single defect identity
  (8.4).

This is the weakest clean theorem that still closes the asymptotic problem.
The most plausible proof strategy is consequently not an all-or-nothing
conflict-free nibble, but a color-balanced nibble followed by necklace
switchings that drive the **total excess potential** (8.1) down to `o(W)`.
