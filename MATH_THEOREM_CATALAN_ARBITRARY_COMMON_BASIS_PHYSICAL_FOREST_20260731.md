# Arbitrary common bases have asymptotically complete physical side forests

Date: 2026-07-31  
Status: proved for every fixed synchronized common basis, asymptotically as
`n -> infinity`.  This removes the quasirandom-common-basis hypothesis from
the `P-o(P)` physicalization theorem.  It does **not** give an exact
`P`-edge side factor, a rooted/no-empty side row, a common cap, or `nu=B`.

## 1. Statement

Use the two-coordinate notation

\[
 N=\binom{2n}{n-1},\qquad P=\binom{2n}{n-2},\qquad
 C=\operatorname{Cat}_{n+1}.
\]

Fix **any admissible puncture set** `Q` of cardinality `C`; in particular,
`Q` may be any synchronized common basis supplied by the automatic
common-basis theorem.  On either punctured shore, there is a family of

\[
                         P-o(P)
\]

physical side diamonds such that

1. no punctured lower outer colour is repeated;
2. no upper outer colour is repeated;
3. every ordinary physical owner has degree at most two;
4. every seam anchor has degree at most one; and
5. the projected physical graph is a linear forest.

The error is uniform over `Q`.  Consequently one may choose `Q` first for
any other purpose and physicalize both of its punctured shores up to `o(P)`
omissions.  No concentration or cylinder inequality for the common-basis
distribution is required.

## 2. The fixed-`Q` capacity-slot hypergraph

Let `G_Q` be the four-uniform capacity-slot hypergraph of Proposition 5.2 in
`THREAD_A_CATALAN_TWO_COORDINATE_COMMON_Q_AND_PUNCTURED_FOREST_NIBBLE_20260731.md`.
An atom consists of one punctured lower colour, one upper colour, and one
slot at each of its two physical owners.  Ordinary owners have two slots;
seam anchors have one.  Matchings in `G_Q` are therefore exactly the partial
physical side families satisfying conditions 1--4 above.

The unordered owner pair determines its intersection and union colours.
Thus distinct slot lifts of one physical edge share both outer-colour
vertices and cannot coexist in a host matching.  In particular every host
matching projects to a simple physical graph.

Uniformly in `Q`, with

\[
                         D_0=2(n+1)(n+2),
\]

the exact ledger gives

\[
 |E(G_Q)|\ge 4P\binom n2-2C(n^2-1),\qquad
 \Delta(G_Q)\le D_0,\qquad
 \Delta_2(G_Q)\le2(n+1).                         \tag{2.1}
\]

The graph is irregular after puncturing.  That is harmless here because the
coloring form of the Delcourt--Postle theorem assumes only a maximum-degree
bound, not approximate regularity.

## 3. Conflict system for short projected cycles

Fix `L>=3`.  Define a configuration hypergraph `H_L` on `E(G_Q)`.  A set of
`i` atoms, `3<=i<=L`, is a configuration when

* the atoms are a matching in `G_Q`; and
* their projected physical edges form a simple cycle of length `i`.

There are no projected parallel edges in a matching: two atoms with the
same physical-owner pair have the same intersection and union colours and
hence meet in `G_Q`.

Put `J=n^2-1`, the degree of the physical Johnson graph.  Fixing one atom of
an `i`-cycle leaves a physical path of length `i-1` between prescribed
endpoints.  Ignoring simplicity gives at most `J^(i-2)` projected choices,
and the slot multiplicity is bounded in terms of `L`.  Hence

\[
                    \Delta_i(H_L)=O_L(J^{i-2})=O_L(D_0^{i-2}).       \tag{3.1}
\]

More generally, if `ell` fixed atoms extend to an `i`-cycle, their projected
edges form a bounded collection of path segments.  The `i-ell` missing
edges form nonempty connecting paths between prescribed endpoints.  At
least one closing constraint is present, so

\[
 \Delta_{i,\ell}(H_L)=O_L(J^{i-\ell-1})
                     =O_L(D_0^{i-\ell-1})             \tag{3.2}
\]

for `2<=ell<i<=L`.  These are precisely the cycle estimates in
`ASYMPTOTIC_MATCHING.md`; passing to `G_Q` only deletes atoms and therefore
cannot increase any degree or codegree.

There are no size-two configurations.  Thus both special two-degree terms
in Delcourt--Postle are zero.

## 4. Delcourt--Postle applies without regularity

Use Corollary 1.17 of Delcourt and Postle,
*Finding an almost perfect matching in a hypergraph avoiding forbidden
submatchings*, arXiv:2204.08981v3.  In its coloring form, for fixed
uniformities and fixed `beta>0`, its hypotheses are

\[
 \Delta(G)\le D,\quad \Delta_2(G)\le D^{1-\beta},
\]

together with the corresponding configuration degree and mixed-codegree
bounds.  It concludes

\[
               \chi(L(G)\cup H)\le D(1+D^{-\alpha})               \tag{4.1}
\]

for some fixed `alpha=alpha(L,beta)>0`.

Take, concretely, `beta=1/3` and `D=D_0`.  Equation (2.1) gives

\[
 2(n+1)\le D_0^{2/3}
\]

for all sufficiently large `n`.  For every fixed `3<=i<=L`, (3.1) gives

\[
 \Delta_i(H_L)=O_L(D_0^{i-2})
     \le \alpha D_0^{i-1}\log D_0,
\]

and for `2<=ell<i<=L`, (3.2) gives

\[
 \Delta_{i,\ell}(H_L)=O_L(D_0^{i-\ell-1})
     \le D_0^{i-\ell-1/3}.
\]

Finally `H_L` has no size-two configurations.  In the exact terminology of
Corollary 1.17, both the maximum `2`-codegree of `G_Q` with `H_L` and the
maximum common `2`-degree of `H_L` are therefore zero.  Thus every
hypothesis of the corollary holds, and (4.1) follows uniformly over every
fixed `Q`.

Each colour class is an `H_L`-avoiding matching.  Taking the largest colour
class gives

\[
 |M|\ge { |E(G_Q)|\over D_0}(1-D_0^{-\alpha}).                     \tag{4.2}
\]

This is the key quantifier swap: no minimum degree, approximate regularity,
or probability law on `Q` appears.

## 5. Size calculation

The exact Catalan ratio is

\[
 {P\over C}={n(n-1)\over2(2n+1)}.                                 \tag{5.1}
\]

Substituting (5.1) into (2.1) yields

\[
 { |E(G_Q)|\over D_0}
 \ge
 P\,{n^3-5n^2-6n-2\over n(n+1)(n+2)}
 =P\left(1-{8\over n}+{16\over n^2}-{34\over n^3}
          +O(n^{-4})\right).                                      \tag{5.2}
\]

Combining (4.2) and (5.2), for each fixed `L`,

\[
                         |M|=P-o_L(P).                             \tag{5.3}
\]

Its physical projection has maximum degree two, is simple, and has no cycle
of length at most `L`.

## 6. From fixed girth to a linear forest

Every remaining projected cycle has at least `L+1` edges, and cycles in a
maximum-degree-two graph are edge-disjoint.  Deleting one atom from each
cycle loses at most `|M|/(L+1)` atoms.  Quantitatively, the preceding fixed-
`L` result gives

\[
 \limsup_{n\to\infty}\ \sup_Q {P-|F_Q|\over P}\le {1\over L+1}.
 \tag{6.1}
\]

Now let `L->infinity`.  Equivalently, one may choose a stepwise diagonal
`L=L(n)->infinity` slowly enough to pass every fixed-`L` threshold.  This
order of limits is essential because the Delcourt--Postle theorem is stated
for fixed configuration rank `g=L`.  The result is a linear forest `F_Q`
with

\[
                            |F_Q|=P-o(P),                           \tag{6.2}
\]

uniformly in `Q` in the asymptotic-existence sense: the same threshold works
for every `Q` at each fixed `L` because all estimates above are independent
of `Q`.

Applying the theorem independently on the two shores gives two such side
forests for the same preselected common basis.  The attachment-pruning
argument of Corollary 6.6 in the Thread-A note keeps every seam and deletes
at most `2C=O(P/n)=o(P)` further side atoms, so the complete two-shore
physical support can also be made acyclic with `o(P)` total loss.

Here "complete support" means the union of all forced seam/central pieces
with the **selected partial** side atoms.  It does not mean exact palette
coverage or a completed Catalan path factor.  In particular, pruning may
create additional side components; some may contain no seam anchor, and the
theorem does not pair the two exposed ends of a component by complementation.
Thus acyclicity of the attachment union is strictly weaker than the
one-complement-reset-per-component condition in the AGCF atomization.

Finally,

\[
 {N\over P}={n+2\over n-1},\qquad
 N-P={3P\over n-1}.                                                \tag{6.3}
\]

After isolated physical vertices are included, each side forest has

\[
                 N-|F_Q|={3P\over n-1}+o(P)=o(P)
\]

components.

## 7. Exact scope

This theorem closes the previous **asymptotic correlation bridge**

\[
 \text{automatic common basis}
 \quad+\quad
 \text{physical punctured side forests}
 \quad+\quad
 \text{joint attachment acyclicity}
\]

with `o(P)` loss, for an arbitrarily preselected synchronized common basis.

The common basis in this collar theorem should not be identified with an
AGCF's unordered complementary endpoint-pair bank, nor with the orientation
transversal used in the three-sector split.  The usefulness of the uniform
quantifier is instead that a path-dependent endpoint/seam state may be
chosen first and its induced punctured rows still receive the same
`P-o(P)` forest body.

It does not close coefficient one.  The matching has `P-o(P)`, not `P`,
atoms; it need not be rooted or no-empty; and it does not preserve/regenerate
the exact downstream common cap.  The remaining theorem is an exact,
correlated absorber/cover-down statement, not common-basis concentration.
One promising input is the whole Delcourt--Postle coloring: its many
high-girth colour classes form a distributed exchange reservoir, whereas a
single largest class supplies only the near-forest proved here.
