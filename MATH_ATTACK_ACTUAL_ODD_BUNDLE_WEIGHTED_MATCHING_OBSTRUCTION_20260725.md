# Actual bounded-displacement odd bundles obstruct star-concentrated weighted matching

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or web input
is used.

## 0. Outcome

The desired star-concentration theorem is false even for literal
bounded-displacement return-free strips, and it is false for a genuinely
nonclique matching obstruction.

For every fixed \(r\ge1\), and more generally for every growing \(r\)
satisfying the explicit packing conditions in Section 2, there is a legal
protected multicover whose heavy part has bundle quotient

\[
 C_{2r+1}.                                           \tag{0.1}
\]

Every tag has degree exactly \(D\), every protected target has degree at
most \(D\), and two heavy paths on distinct tags have either no common
protected target or exactly one common middle owner.  Thus every cross-tag
intersection has width one and every nonlinear cross-tag overlap moment
vanishes.

Give unit test weight to the heavy edge copies and zero weight to fillers.
Then

\[
 w({\cal Q})={2r+1\over2}D,
 \qquad
 \nu_w({\cal Q})=r,                                 \tag{0.2}
\]

and hence

\[
 \boxed{
 {w({\cal Q})\over\nu_w({\cal Q})}
 =D\left(1+{1\over2r}\right).}                     \tag{0.3}
\]

For \(r=1\) this is the Shannon triangle.  For \(r=2\), the support
conflict graph is a blown-up \(C_5\), not a clique, and (0.3) is
\(5D/4\).

No tag or target star contains more than \(D\) test weight.  Consequently

\[
 \boxed{
 \min_z w({\cal Q}\setminus\operatorname{Star}(z))
 ={2r-1\over2}D,}                                   \tag{0.4}
\]

where \(z\) ranges over all tag and protected-target resources.  In
particular, the nonclique \(C_5\) obstruction leaves at least \(3D/2\)
outside every star.

Therefore any universal weighted matching estimate

\[
 w(E)\le(1+\varepsilon_Q)D\nu_w                    \tag{0.5}
\]

requires

\[
 \varepsilon_Q\ge{1\over2r}.                       \tag{0.6}
\]

Taking \(r=2\) shows that actual strip geometry does not give even
\(\varepsilon_Q=o(1)\), much less the coefficient-safe
\(\varepsilon_Q=o(1/Q)\).  In additive coefficient form the unavoidable
error is at least \(D/4\) for the nonclique example; the triangle gives
\(D/2\).  There is no gain in \(Q\).

There is also an exact positive augmenting theorem which locates the
failure.  If the heavy bundle quotient is bipartite, tag and target-star
capacities alone give an exact decomposition into \(D\) matchings, and
therefore

\[
 w(E)\le D\nu_w                                     \tag{0.7}
\]

for every test weight.  The obstruction is the odd blossom inequality,
not a missing clique estimate.  For an odd bundle cycle with rational
bundle masses \(a_i\), the additional condition required at coefficient
one is

\[
 \boxed{
 \sum_{i=0}^{2r}a_i
 \le r+o(r/Q).}                                     \tag{0.8}
\]

Pairwise star capacities yield only

\[
 \sum_i a_i\le r+\frac12+O(r\eta),                  \tag{0.9}
\]

leaving an exact half-unit blossom gap.  Four-antichain pruning,
pair-square decay, and bounded displacement do not remove this gap for an
arbitrary rational point.  A positive theorem for the particular uniform
pruning point must prove (0.8), or the full weighted matching-cover
inequality, from how that point was sampled.

## 1. The exact weighted bundle theorem

The following elementary model separates the augmenting issue from the
strip realization.

Let \(G\) be a simple graph.  For every \(i\in V(G)\), let
\({\cal A}_i\) be a family of \(a_i\) objects with one common tag.  Suppose

* two objects in the same \({\cal A}_i\) conflict through that tag;
* every object of \({\cal A}_i\) conflicts with every object of
  \({\cal A}_j\) when \(ij\in E(G)\); and
* objects in distinct nonadjacent bundles are disjoint.

A matching in the union chooses at most one object from each bundle, and
the chosen bundle indices form an independent set of \(G\).

### Theorem 1.1 (bipartite quotient gives the exact weighted matching bound)

Suppose \(G=L\mathbin{\dot\cup}R\) is bipartite and

\[
 a_i+a_j\le D\qquad(ij\in E(G)),
 \qquad a_i\le D.                                   \tag{1.1}
\]

Then the objects can be partitioned into \(D\) matchings.  Consequently,
for every nonnegative object weight \(w\),

\[
 \boxed{w(E)\le D\nu_w.}                           \tag{1.2}
\]

#### Proof

Use the palette \([D]\).  Give the \(a_i\) objects in a bundle
\(i\in L\) distinct colours from

\[
 \{1,2,\ldots,a_i\},                                \tag{1.3}
\]

and give the \(a_j\) objects in a bundle \(j\in R\) distinct colours
from

\[
 \{D-a_j+1,\ldots,D\}.                              \tag{1.4}
\]

For an edge \(ij\), (1.1) makes the two intervals disjoint.  Equal colours
therefore form matchings.  These \(D\) matchings partition all objects, so
one has weight at least \(w(E)/D\).  This proves (1.2). \(\square\)

This is an exact weighted augmenting theorem: every nonnegative dual
vector is handled simultaneously.  It uses the two shores of the bundle
quotient, rather than trying to put most of the dual mass in one star.

### Theorem 1.2 (odd-cycle blossom)

Let \(G=C_{2r+1}\) and \(a_i=D/2\), with \(D\) even.  Put unit weight on
every object.  Then

\[
 w(E)={2r+1\over2}D,
 \qquad
 \nu_w=\alpha(C_{2r+1})=r.                          \tag{1.5}
\]

Hence (0.3) holds.  The edge and vertex clique constraints are all tight:

\[
 a_i+a_{i+1}=D,qquad a_i=D/2.                      \tag{1.6}
\]

#### Proof

The total weight is immediate.  A matching chooses at most one object per
bundle and its bundle indices are independent, so it has weight at most
\(r\).  Conversely, choose one arbitrary object from each member of a
maximum independent set of the odd cycle.  Those objects are pairwise
disjoint by the bundle hypotheses, giving weight \(r\). \(\square\)

Thus the first graph outside the bipartite theorem produces exactly the
missing matching-polytope inequality.  No clique calculation is involved
when \(r\ge2\).

## 2. Literal return-free realization of every admissible odd cycle

Use the return-free parameters

\[
 d=\ell-1,qquad g=d+2Q,                             \tag{2.1}
\]

and put \(n=2r+1\).  Assume

\[
 d\ge2Q,qquad g\le H-Q,                            \tag{2.2}
\]

\[
 m-d\ge2nQ,qquad m-d+nH\le2m.                     \tag{2.3}
\]

Every fixed odd \(n\) satisfies (2.3) eventually in the calibrated regime
\(H=o(m)\), \(Q=o(m)\), \(d=o(m)\).  Growing cycles are also allowed up to

\[
 n\le
 \min\left\{{m-d\over2Q},{m+d\over H}\right\}.     \tag{2.4}
\]

Choose mutually disjoint blocks, with indices modulo \(n\),

\[
 |S_0|=m-d,qquad |A_i|=d,qquad |R_i|=H-d.          \tag{2.5}
\]

The size of their union is

\[
 m-d+nd+n(H-d)=m-d+nH\le2m,                        \tag{2.6}
\]

so they fit in the Boolean ground set.  Define middle owners and carriers

\[
 X_i=S_0\mathbin{\dot\cup}A_i,                      \tag{2.7}
\]

\[
 U_i=S_0\mathbin{\dot\cup}A_{i-1}
          \mathbin{\dot\cup}A_i\mathbin{\dot\cup}R_i.
                                                               \tag{2.8}
\]

Then \(|X_i|=m\), \(|U_i|=m+H\), and

\[
 U_i\cap U_{i+1}=X_i.                               \tag{2.9}
\]

For nonadjacent \(i,j\),

\[
 U_i\cap U_j=S_0,qquad |S_0|=m-d<m-Q.             \tag{2.10}
\]

Inside \(S_0\), choose all \(2n\) sets

\[
 K_i^-,K_i^+\qquad(i\in\mathbb Z/n\mathbb Z)       \tag{2.11}
\]

pairwise disjoint and of size \(Q\).  Inside every \(R_i\), choose
disjoint \(Q\)-sets \(R_i^-,R_i^+\).  The unused part has size

\[
 |R_i\setminus(R_i^-\cup R_i^+)|=H-g\ge Q.         \tag{2.12}
\]

Let \(\alpha_i\) be an order of \(A_{i-1}\) and \(\beta_i\) an order of
\(A_i\).  Choose the boundary orders so that

\[
 \beta_i[d-Q+1,d]\cap\alpha_{i+1}[1,Q]=\varnothing
 \qquad(i\bmod n).                                  \tag{2.13}
\]

This is possible independently in every \(A_i\) by \(d\ge2Q\).

On tag \(U_i\), take the oriented return-free geodesic from
\(X_{i-1}\) to \(X_i\) with complete departure and arrival orders

\[
 a^{(i)}=(R_i^-;\alpha_i;K_i^+),
 \qquad
 b^{(i)}=(K_i^-;\beta_i;R_i^+),                     \tag{2.14}
\]

and persistent core

\[
 C_i=S_0\setminus(K_i^-\cup K_i^+).                \tag{2.15}
\]

The sizes are exact:

\[
 |C_i|=m-g,qquad |a^{(i)}|=|b^{(i)}|=g.            \tag{2.16}
\]

After the first \(Q\) buffer exchanges, the owner is \(X_{i-1}\); after
the following \(d\) central exchanges, it is \(X_i\).  The unused block
in (2.12) supplies the literal radius-\(Q\) queue buffer, exactly as in the
return-free triangle construction.

## 3. Exact protected-intersection theorem

Let \({\cal S}_Q(P_i)\) denote the complete raw protected strip: all
middle owners and both signed depths through \(Q\) on the physical phase
interval.

### Theorem 3.1 (the strip-intersection graph is the cycle)

The paths in Section 2 satisfy

\[
 \boxed{
 {\cal S}_Q(P_i)\cap{\cal S}_Q(P_{i+1})=\{X_i\},}  \tag{3.1}
\]

and

\[
 \boxed{
 {\cal S}_Q(P_i)\cap{\cal S}_Q(P_j)=\varnothing
 \quad\text{for nonadjacent }i,j.}                 \tag{3.2}
\]

#### Proof

Every target of \(P_i\) is a subset of its carrier \(U_i\).  For
nonadjacent paths, a common target would be a subset of
\(U_i\cap U_j=S_0\), whose size is smaller than \(m-Q\).  All protected
targets have rank at least \(m-Q\), proving (3.2).

For adjacent paths, the carrier intersection is \(X_i\), of size \(m\).
A common upper target has rank greater than \(m\), so is impossible.  A
common middle owner has rank \(m\), and hence must equal \(X_i\), which is
indeed the end owner of \(P_i\) and the start owner of \(P_{i+1}\).

It remains to exclude a common lower target.  Equal lower targets have
the same depth \(q\le Q\).  At the start of \(P_{i+1}\), the only
depth-\(q\) lower cell contained in \(X_i\) is

\[
 X_i\setminus\alpha_{i+1}[1,q].                    \tag{3.3}
\]

At the end of \(P_i\), every depth-\(q\) lower cell contained in \(X_i\)
has the form

\[
 X_i\setminus
 \left(
 \beta_i[d-s+1,d]\cup K_i^+[1,q-s]
 \right),qquad0\le s\le q.                        \tag{3.4}
\]

If \(s<q\), the deleted set in (3.4) has a nonempty \(S_0\)-part, whereas
the deleted set in (3.3) lies in \(A_i\).  If \(s=q\), the two deleted
sets are nonempty subsets of the disjoint boundary sets in (2.13).  They
are unequal in either case.  Thus no common lower target exists, proving
(3.1). \(\square\)

Priority decoration cannot add intersections and always retains the
middle owners.  Therefore (3.1)--(3.2) hold for every decorated protected
claim set as well.

The proof uses the exact displacement \(d\), the radius-\(Q\) endpoint
collars, and carrier intersections.  It is not an abstract realization of
an odd cycle.

## 4. Diffuse bundles and degree calibration

Fix the first \(Q\) entries of every \(\alpha_i\), the last \(Q\) entries
of every \(\beta_i\), and all buffer data.  Permute unconstrained central
entries.  Reversal is the only possible duplicate oriented presentation
of one simple geodesic support, so every \(P_i\) has at least

\[
 N_{\rm var}\ge{1\over2}(d-Q)!                     \tag{4.1}
\]

distinct variants.  The proof of Theorem 3.1 uses only the fixed boundary
data, and consequently every variant in bundle \({\cal P}_i\) has the same
cross-bundle intersections (3.1)--(3.2).

At the s=4 degree scale

\[
 D=m^{23/6-o(1)},                                   \tag{4.2}
\]

one has \(N_{\rm var}>D\) for all sufficiently large \(m\).  Assume \(D\)
is even and choose \(D/2\) variants in every \({\cal P}_i\).

Above each tag \(U_i\), choose another \(D/2\) filler strips whose
protected targets avoid every core bundle and every filler on a different
tag.  This follows by finite avoidance.  At any fixed protected slot a
uniform oriented parameter on \(U_i\) is uniform over the corresponding
Boolean rank in \(U_i\); the forbidden family has polynomial size, while
the central rank layer in \(U_i\) is superpolynomial.  Hence a random
parameter avoids all forbidden targets with probability \(1-o(1)\), and
the orbit contains more than the required polynomial number of fillers.

The resulting multicover has tag degree exactly \(D\).  An anchor
\(X_i\) belongs to the \(D/2\) paths in each of the two adjacent bundles,
so its degree is exactly \(D\).  By Theorem 3.1 every other core target is
confined to one bundle and has degree at most \(D/2\); filler targets also
have degree at most \(D/2\).  Therefore

\[
 \boxed{\Delta({\cal H})=D}                         \tag{4.3}
\]

on the augmented tag--target hypergraph.

Across distinct tags, two core paths have singleton intersection exactly
when their bundle indices are adjacent, and otherwise have empty
intersection.  Fillers add no cross-tag intersection.  Thus the s=4
four-antichain condition holds with width one and, for every \(w\ge1\),
the centred nonlinear cross-tag moment is exactly zero.

## 5. Weighted matching dual and star-concentration error

Let \({\cal Q}=\bigcup_i{\cal P}_i\), put \(w(P)=1\) on \({\cal Q}\), and
put weight zero on fillers.  Theorem 3.1 identifies the bundle quotient
with \(C_{2r+1}\).  Theorem 1.2 therefore gives (0.2)--(0.3).

For completeness, the star weights on \({\cal Q}\) are as follows.

* A tag star contains its one core bundle and has weight \(D/2\).
* An anchor target \(X_i\) contains the two adjacent bundles and has weight
  \(D\).
* Every other target is confined to one bundle and has weight at most
  \(D/2\).

Hence

\[
 \max_z w({\cal Q}\cap\operatorname{Star}(z))=D,   \tag{5.1}
\]

which proves (0.4).  The obstruction is therefore not a perturbation of
one heavy tag or target star.  For \(C_5\), a maximum-weight matching uses
two nonadjacent bundles, while at least \(3D/2\) test weight remains
outside every single star.

Suppose a proposed theorem had additive coefficient error
\(E(D,Q)\):

\[
 w(E)\le(D+E(D,Q))\nu_w.                            \tag{5.2}
\]

Equations (0.2) give the necessary lower bound

\[
 \boxed{E(D,Q)\ge {D\over2r}.}                     \tag{5.3}
\]

Thus \(C_5\) forces \(E(D,Q)\ge D/4\), uniformly in \(Q\).  No
\(O(D/Q)\), \(o(D)\), or coefficient-safe \(o(D/Q)\) error is possible
from the stated geometric hypotheses.

More generally, if all odd bundle quotients shorter than \(2r+1\) were
somehow excluded, the realized \(C_{2r+1}\) still forces error
\(D/(2r)\).  To reach \(o(D/Q)\), one must control every odd bundle cycle
of length \(O(Q)\), whenever that length lies below the physical limit
(2.4).  This is a hierarchy of blossom inequalities, not one EKR star
statement.

## 6. The exact gate for the particular uniform pruning point

The construction above chooses an adversarial rational subpoint of the
legal strip catalogue.  It does not assert that a separately fixed uniform
s=4 isolated-pruning point places mass \(1/2\) in every displayed bundle.
That distinction is the only surviving opening.

Let \(a_i=x({\cal A}_i)\) be the masses of option bundles in a physical odd
cycle for that fixed point.  Tag capacity gives \(a_i\le1\), and the anchor
target shared by consecutive bundles gives

\[
 a_i+a_{i+1}\le1+\eta.                             \tag{6.1}
\]

Summing (6.1) around the odd cycle yields only

\[
 \sum_{i=0}^{2r}a_i
 \le {2r+1\over2}(1+\eta)
 =r+{1\over2}+O(r\eta).                             \tag{6.2}
\]

On the other hand, the unit test vector on the corresponding cleared edge
copies has matching-cover ratio at most \((1+\varepsilon_Q)D\) only if

\[
 \sum_{i=0}^{2r}a_i\le r(1+\varepsilon_Q).          \tag{6.3}
\]

Thus \(\varepsilon_Q=o(1/Q)\) requires exactly (0.8).  The pairwise
capacities leave a half-unit too much, regardless of the bounded
displacement of the strips.

Balancing tag--target-pair fibres can make the particular endpoint-pair
bundles in Section 4 very small.  It does not by itself establish (0.8)
for an adversarial dual vector dispersed over many small bundles.  The
needed positive assertion is therefore one of the following equivalent
forms:

1. every physical odd bundle system satisfies (0.8), hereditarily under
   the chosen pruning point;
2. the cleared multicover satisfies
   \[
    \sum_e y_e\le(1+o(1/Q))D
       \max_{M\text{ matching}}\sum_{e\in M}y_e
       \qquad(y\ge0);                               \tag{6.4}
   \]
3. after contracting the genuinely heavy tag/pair-star pieces, the
   resulting bundle quotient has only \(o(1/Q)\) total odd-blossom defect.

Theorem 1.1 shows why a bipartite quotient would be enough.  The literal
odd-cycle construction proves that bounded-displacement strip geometry
does not force such a quotient and does not make heavy weighted
obstructions star-concentrated.

