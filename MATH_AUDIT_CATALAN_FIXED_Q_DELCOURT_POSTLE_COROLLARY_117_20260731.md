# Audit of the fixed-`Q` Delcourt--Postle physical-forest argument

Date: 2026-07-31  
Status: **GO**, subject only to the already stated fixed-uniformity/diagonal
qualification.  The application of Delcourt--Postle Corollary 1.17 is
legitimate for every fixed puncture set `Q`; approximate regularity of the
host is not a hypothesis of that corollary.

Primary source checked: Michelle Delcourt and Luke Postle, *Finding an almost
perfect matching in a hypergraph avoiding forbidden submatchings*,
[arXiv:2204.08981v3](https://arxiv.org/abs/2204.08981v3), Corollary 1.17
(the source label is `cor:SmallCodegreeColoring`).

This audit concerns the invocation in
`MATH_THEOREM_CATALAN_ARBITRARY_COMMON_BASIS_PHYSICAL_FOREST_20260731.md`.
It does not audit the later exact absorber/common-cap step.

## 1. Exact published input

In the notation needed here, Corollary 1.17 says the following.  Fix integers
`r,g>=2` and a real `beta>0`.  There are `D_beta` and `alpha>0` such that,
for `D>=D_beta`, if

1. `G` is an `r`-bounded multihypergraph with
   `Delta(G)<=D` and `Delta_2(G)<=D^(1-beta)`;
2. `H` is a `g`-bounded configuration hypergraph of `G`;
3. `Delta_i(H)<=alpha D^(i-1) log D` for `2<=i<=g`;
4. `Delta_(k,ell)(H)<=D^(k-ell-beta)` for
   `2<=ell<k<=g`;
5. the maximum `2`-codegree of `G` with `H` and the maximum common
   `2`-degree of `H` are at most `D^(1-beta)`;

then

\[
 \chi(L(G)\cup H)\le \chi_\ell(L(G)\cup H)
       \le D(1+D^{-\alpha}).                                      \tag{1.1}
\]

Consequently there is an `H`-avoiding matching of size at least

\[
                  {e(G)\over D}(1-D^{-\alpha}).                   \tag{1.2}
\]

The corollary assumes a maximum degree, not a minimum degree or approximate
regularity.  This is the key distinction from Pippenger-type almost-perfect
matching statements and from Delcourt--Postle's bipartite `A`-perfect
theorem.

## 2. Host hypotheses for the fixed-`Q` slot hypergraph

Take

\[
 r=4,\qquad g=L,\qquad \beta={1\over3},\qquad
 D=D_0:=2(n+1)(n+2).
\]

For every fixed `Q`, Proposition 5.2 of the punctured-forest ledger gives

\[
 \Delta(G_Q)\le D_0,
 \qquad \Delta_2(G_Q)\le2(n+1),                                  \tag{2.1}
\]
and

\[
 |E(G_Q)|\ge4P\binom n2-2C(n^2-1).                              \tag{2.2}
\]

The four resource classes are typed, so every atom has four distinct host
vertices even at a one-slot seam anchor.  Thus `G_Q` is genuinely
four-uniform (and in particular four-bounded).

For all sufficiently large `n`,

\[
                  2(n+1)\le D_0^{2/3}=D_0^{1-\beta},              \tag{2.3}
\]

so the host-codegree hypothesis holds.  No lower-degree statement is
needed.  Puncturing can make `G_Q` highly irregular without affecting this
application.

## 3. Configuration degrees

Let `H_L` consist of host matchings whose projected owner edges form a
simple cycle of length `i`, for `3<=i<=L`.  This is an `L`-bounded
configuration hypergraph; it has no edges of size two.

The completion estimate can be stated cleanly as follows.  Put
`J=n^2-1`, the maximum degree of the physical Johnson graph.  Suppose `ell`
fixed atoms extend to a projected simple `i`-cycle.  Their projected edges
form `c>=1` path components.  Up to `O_L(1)` cyclic orders and orientations,
the `i-ell` missing projected edges form `c` nonempty paths between fixed
endpoint pairs.  A path of `t` edges between fixed endpoints has at most
`J^(t-1)` choices.  Hence the number of projected completions is at most

\[
 O_L(J^{(i-\ell)-c})=O_L(J^{i-\ell-1}).                           \tag{3.1}
\]

Each projected edge has only a bounded number of slot lifts.  Therefore

\[
 \Delta_i(H_L)=O_L(D_0^{i-2}),                                   \tag{3.2}
\]

and, for `2<=ell<i<=L`,

\[
 \Delta_{i,\ell}(H_L)=O_L(D_0^{i-\ell-1}).                       \tag{3.3}
\]

For the fixed positive theorem constant `alpha=alpha(4,L,1/3)`, (3.2)
is eventually at most `alpha D_0^(i-1) log D_0`; (3.3) is eventually at
most `D_0^(i-ell-1/3)`.  Thus the unknown size of `alpha` changes only the
threshold in `n`, not the conclusion.

Because `H_L` has no size-two configurations, both special hypotheses in
Corollary 1.17 vanish exactly:

* its maximum common `2`-degree is zero; and
* the maximum `2`-codegree of `G_Q` with `H_L` is zero.

This use of zero is specific to the **2**-versions in the published
corollary; the larger mixed codegrees are supplied separately by (3.3).

## 4. Largest colour class and the edge-count normalization

Equation (1.1) supplies a proper colouring with at most
`D_0(1+D_0^(-alpha))` colours.  Every colour class is simultaneously a host
matching and `H_L`-avoiding.  Its largest class therefore has size at least

\[
 { |E(G_Q)|\over D_0(1+D_0^{-\alpha})}
 \ge { |E(G_Q)|\over D_0}(1-D_0^{-\alpha}).                       \tag{4.1}
\]

Using

\[
 {P\over C}={n(n-1)\over2(2n+1)},                                \tag{4.2}
\]

the edge ledger gives exactly

\[
 { |E(G_Q)|\over D_0}
 \ge
 P\,{n^3-5n^2-6n-2\over n(n+1)(n+2)}
 =P\left(1-{8\over n}+{16\over n^2}-{34\over n^3}
          +O(n^{-4})\right).                                     \tag{4.3}
\]

Thus, for every fixed `L`, the largest class has `P-o_L(P)` atoms,
uniformly in `Q`.

## 5. Projection and removal of long cycles

A host matching cannot contain two atoms with the same physical owner
pair: that pair determines the same intersection and union colours, so the
two atoms meet at outer-colour host vertices.  Its projection is therefore
simple.  The owner-slot vertices also make its maximum physical degree at
most two (at most one at seam anchors).

The `H_L`-avoidance removes projected cycles of lengths at most `L`.  All
remaining cycles are edge-disjoint and have at least `L+1` edges.  Deleting
one atom from each loses at most `|M|/(L+1)` and leaves a linear forest.

Corollary 1.17 is a fixed-`g` theorem.  One must **not** substitute a growing
`L(n)` directly into it.  The valid conclusion is obtained by the standard
diagonal order:

1. fix `L` and apply the corollary above the corresponding threshold;
2. then choose a stepwise `L=L(n)->infinity` slowly enough that all prior
   fixed-`L` thresholds have been passed.

All bounds and thresholds at a fixed `L` are independent of `Q`, so the
resulting `o(P)` is uniform over all fixed puncture sets `Q`.  No union bound
over the family of possible `Q` is required: the theorem is deterministic
and is applied after `Q` is chosen.

## 6. Verdict and exact scope

The proposed quantifier swap is valid:

\[
 \boxed{\text{choose an arbitrary synchronized common basis }Q\text{ first;
 then obtain }P-o(P)\text{ physical side forests.}}
\]

No cylinder inequality, negative dependence, or quasirandomness of `Q` is
needed for this asymptotic physicalization.

What the argument does **not** supply is an exact `P`-edge forest, a
prescribed leave, a root in every component, correlation between the two
shore matchings, or feasibility of the downstream exact common cap.  Those
remain absorber/integral-correlation questions, not missing hypotheses in
the Delcourt--Postle invocation.
