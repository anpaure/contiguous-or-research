# Polynomial protected matchings extend in the middle-level incidence graph

**Date:** 2026-08-06  
**Method:** Johnson spectral localization and the two sharp partial-shadow
thresholds; no computation or search  
**Status:** unconditional matching-extension theorem.  It is the
capacity-one analogue of the protected two-factor theorem.  A polynomial
partial matching whose two endpoint exposures are below one half by a
fixed linear margin extends to a perfect matching.  Consequently the two
alternating edge classes of any oriented polynomial protected path forest
extend separately to perfect matchings.  Their union is a directed cycle
cover as a bipartite multigraph; eliminating common unprotected edges and
forcing the desired component structure remain separate.

## 1. Setting

Let

\[
 \mathcal L={ [2r-1]\choose r-1},\qquad
 \mathcal U={ [2r-1]\choose r},\qquad
 W=|\mathcal L|=|\mathcal U|,
 \tag{1.1}
\]

and let `G` be the inclusion graph between the two shores.  It is
`r`-regular.

Let `F` be a matching in `G`.  Write

\[
 Z=V(F)\cap\mathcal L,\qquad
 Y=V(F)\cap\mathcal U,\qquad
 X=\mathcal L\setminus Z,
 \tag{1.2}
\]

so `|Z|=|Y|=:f`.  Define the two literal exposure parameters

\[
 \alpha(F)=\max_{x\in X}|N_G(x)\cap Y|,
 \tag{1.3}
\]

\[
 \beta(F)=\max_{U\in\mathcal U}|N_G(U)\cap Z|.
 \tag{1.4}
\]

Put

\[
 D_\alpha=r-\alpha(F),\qquad
 D_\beta=r-\beta(F),\qquad
 K(D)={2D-1\choose D}.
 \tag{1.5}
\]

The problem is to find a perfect matching of `G` containing `F`, or,
equivalently, a perfect matching of the residual graph

\[
 G_F=G[X,\mathcal U\setminus Y].
 \tag{1.6}
\]

## 2. Cardinality localization for a failed residual Hall shore

For `A subseteq mathcal L`, write

\[
 s(A)=|N_G(A)|-|A|.
 \tag{2.1}
\]

### Lemma 2.1 (spectral near-equality localization)

For every nonempty proper `A subset mathcal L`,

\[
 \boxed{
 s(A)\ge {2r-1\over r^2}
          {|A|(W-|A|)\over W}.}
 \tag{2.2}
\]

#### Proof

For `U in mathcal U`, put `a_U=|A cap N_G(U)|`.  Edge counting gives

\[
 r\,s(A)
 =\sum_{U\in N_G(A)}(r-a_U).
 \tag{2.3}
\]

The Johnson edge boundary of `A` is

\[
 |\partial_JA|=\sum_U a_U(r-a_U).
 \tag{2.4}
\]

Since `a_U<=r`, equations (2.3)--(2.4) imply

\[
 s(A)\ge {1\over r^2}|\partial_JA|.
 \tag{2.5}
\]

The Johnson graph `J(2r-1,r-1)` has Laplacian gap `2r-1`.  Applying the
Laplacian inequality to `1_A` gives

\[
 |\partial_JA|\ge(2r-1)|A|\left(1-{|A|\over W}\right).
 \tag{2.6}
\]

Substitution proves (2.2).  `square`

### Corollary 2.2

If `A subseteq X` fails Hall in `G_F`, then

\[
 \boxed{
 \min\{|A|,W-|A|\}< {2r^2\over2r-1}\,f.}
 \tag{2.7}
\]

#### Proof

Failure means

\[
 |N_G(A)\setminus Y|\le|A|-1.
 \tag{2.8}
\]

Therefore

\[
 s(A)
 \le |N_G(A)\cap Y|-1
 \le f-1<f.
 \tag{2.9}
\]

If `q=min{|A|,W-|A|}`, then

\[
 {|A|(W-|A|)\over W}={q(W-q)\over W}\ge q/2.
\]

Combine this with Lemma 2.1.  `square`

Thus every obstruction to extending a polynomial matching has a
polynomial small side.  The next two lemmas exclude both choices of that
side under sub-half exposure.

## 3. The small failed shore

### Lemma 3.1

Every failed residual shore satisfies

\[
 \boxed{|A|\ge K(D_\alpha).}
 \tag{3.1}
\]

#### Proof

Take an inclusion-minimal failed shore `A`.  Put

\[
 \mathcal C=N_G(A)\setminus Y.
 \tag{3.2}
\]

Then `|mathcal C|<|A|`.  Every `x in A` has at least

\[
 r-|N_G(x)\cap Y|\ge D_\alpha
 \tag{3.3}
\]

members of `mathcal C` containing it.  Complement `A` and `mathcal C`
inside `[2r-1]`.  The resulting adjacent-rank families have side ratio
strictly below one, and every member on the rank-`r` side contains at
least `D_alpha` members of the other family.  The sharp partial-shadow
threshold gives

\[
 |A|\ge {2D_\alpha-1\choose D_\alpha}=K(D_\alpha).
\]

Every failed shore contains an inclusion-minimal one, so the bound holds
without minimality.  `square`

## 4. The co-small failed shore

Let `A subseteq X` fail Hall and put

\[
 B=X\setminus A,
 \qquad
 \mathcal Q=(\mathcal U\setminus Y)
             \setminus N_{G_F}(A).
 \tag{4.1}
\]

### Lemma 4.1

One has

\[
 \boxed{|B|\ge K(D_\beta)+1.}
 \tag{4.2}
\]

#### Proof

Because the two residual shores have the same cardinality `W-f`, Hall
failure gives

\[
 |\mathcal Q|
 =(W-f)-|N_{G_F}(A)|
 \ge(W-f)-(|A|-1)=|B|+1.
 \tag{4.3}
\]

Every `U in mathcal Q` has no neighbour in `A`.  At most `beta(F)` of its
`r` lower facets lie in `Z`; all remaining facets lie in `X`, and hence in
`B`.  Thus every member of `mathcal Q` contains at least

\[
 r-\beta(F)=D_\beta
 \tag{4.4}
\]

members of `B`.  Apply the strict-imbalance partial-shadow theorem to the
adjacent-rank families `(B,mathcal Q)`.  It gives

\[
 |B|\ge {2D_\beta-1\choose D_\beta-1}+1
       =K(D_\beta)+1.
\]

`square`

## 5. Extension theorem

### Theorem 5.1 (polynomial protected matching extension)

Fix constants `C<infinity` and `epsilon>0`.  If

\[
 f\le r^C
 \tag{5.1}
\]

and

\[
 \alpha(F),\beta(F)\le(1/2-\epsilon)r,
 \tag{5.2}
\]

then, for all sufficiently large `r`, `F` extends to a perfect matching
of `G`.

#### Proof

Suppose `A` is a failed residual Hall shore.  By Corollary 2.2 either
`|A|=O(r^(C+1))` or `W-|A|=O(r^(C+1))`.  In the first case Lemma 3.1
contradicts

\[
 K(D_\alpha)
 \ge 2^{(1+2\epsilon)r-O(\log r)}.
 \tag{5.3}
\]

In the second case

\[
 |B|=|X|-|A|=W-f-|A|=O(r^{C+1}),
\]

and Lemma 4.1 contradicts the analogous exponential lower bound for
`K(D_beta)`.  Hence the residual graph satisfies Hall.  A perfect
matching of it, together with `F`, is a perfect matching of `G`.  `square`

The constants in (5.2) are far stronger than needed.  The same proof works
whenever both `K(D_alpha)` and `K(D_beta)` dominate `rf`.

## 6. Directed protected path forests

Let `P` be the incidence lift of a polynomial-size owner-path forest.
Orient every component of `P`.  Colour its incidence edges alternately
`0,1` along the chosen orientation, and let `F_0,F_1` be the two colour
classes.  Both are matchings.

### Corollary 6.1 (separate directed-role completion)

If the full forest has the two exposures

\[
 \alpha(P),\beta(P)\le(1/2-\epsilon)r,
 \tag{6.1}
\]

then each `F_i` extends to a perfect matching `M_i` of `G`.  Hence

\[
                         M_0\mathbin{\uplus_{\rm col}}M_1
 \tag{6.2}
\]

is a directed spanning cycle cover as a bipartite multigraph and contains
every protected path with its prescribed orientation.

#### Proof

Because `P` is the incidence lift of an **owner**-path forest, every used
lower vertex has protected degree two and is incident with one edge of
each colour.  Hence the lower endpoint set of each `F_i` is exactly the
used-lower set of `P`.  The upper endpoint set of `F_i` is a subset of the
protected owners.  It follows, with the domains in the definitions kept
fixed, that both exposure parameters for `F_i` are at most those of `P`.
Theorem 5.1 applies separately to `F_0` and `F_1`.  Orient `M_0` from the
owner shore to the lower shore and `M_1` in the reverse direction.  Every
vertex then has indegree and outdegree one, and the prescribed alternating
arcs of `P` occur with their chosen directions.  If an unprotected edge
belongs to both perfect matchings, it forms a directed two-cycle; this is
why `uplus_col` in (6.2) denotes the coloured multiset union rather than a
disjoint union of underlying edge sets, and why the conclusion is a
multigraph cover rather than a simple two-factor.  `square`

## 7. Scope for the PBBS collar bank

The protected PBBS five-collar forest plus the rank-stratified upper
backup paths has polynomial size and exposure at most `r/3`.  Corollary
6.1 therefore permits every protected component to be assigned its
required old/new direction and extends both alternating matching roles.

This closes the **separate directed-matching Hall rows**.  It does not yet
prove:

1. that the two extensions can be selected without common unprotected
   edges;
2. that their simple component graph has the PBBS-required connectivity;
3. clipped residence or one common literal antecedent;
4. strict-lower common histories; or
5. the private typed-cap suffix rank.

Thus the remaining PBBS direction problem is a synchronization and
component-switching problem, not a one-role matching-supply obstruction.

## 8. Dependencies

The two sharp adjacent-rank partial-shadow thresholds used in Lemmas 3.1
and 4.1 are proved in
`MATH_THEOREM_SUBLINEAR_EXPOSURE_PROTECTED_FACTOR_SMALL_CUT_AND_OPTIONAL_CORE_REDUCTION_20260805.md`.
The Johnson spectral calculation is the capacity-one specialization of
`MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md`.
