# Unrestricted mixed-frame blossoms and the common-route rounding gate

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or
independent depthwise rounding is used.

## 0. Verdict

The determinant-two recursive-frame triangle has the ordinary odd-cycle
defect. If its three necklace-bundle masses are \(a_{ab},a_{bc},a_{ca}\),
then owner capacities give only

\[
 a_{ab}+a_{bc}\le1,\quad
 a_{bc}+a_{ca}\le1,\quad
 a_{ca}+a_{ab}\le1,
\]

whereas every integral owner packing satisfies the blossom

\[
                         a_{ab}+a_{bc}+a_{ca}\le1.          \tag{0.1}
\]

For an odd necklace cycle of length \(2r+1\), the corresponding inequality
is

\[
                         \sum_{i=0}^{2r}a_i\le r.           \tag{0.2}
\]

In deficiency form, write \(g_i\) for the mass at anchor \(X_i\) supplied
by routes outside the displayed odd-cycle bundles, and \(e_i\) for
discarded owner mass. Then (0.2) is equivalent to the necessary escape
condition

\[
                         \sum_i(g_i+e_i)\ge1.               \tag{0.3}
\]

Thus every odd gadget needs at least one unit of cross-gadget incidence or
one discarded anchor.

The full unrestricted coordinate orbit supplies far more than this
fractionally. Give every indexed recursive necklace weight \(1/D\), where
\(D\) is its owner degree. For two Johnson-adjacent owners the weighted
pair codegree is exactly \(2/m^2\), and a Johnson triangle has weighted
triple codegree zero. Consequently, on every recursive-frame triangle,

\[
 a_{ab}+a_{bc}+a_{ca}={6\over m^2}=o(1),
\]

while

\[
                         \sum_i g_i=3-{12\over m^2}.        \tag{0.4}
\]

Hence cross-gadget routes do not merely meet the triangle blossom: the
symmetric unrestricted point lies a constant distance inside it. More
generally, for any owner set \(S\),

\[
 \sum_R\binom{|M(R)\cap S|}{2}x_R
 \le {2\over m^2}\binom{|S|}{2}.                           \tag{0.5}
\]

All odd anchor sets of size \(o(m)\), including every Gaussian-size odd
cycle, therefore have asymptotically full single-anchor escape mass.

This removes the local blossom as a fractional obstruction. It does not
prove integral rounding. Whole necklaces are hyperedges, not graph edges,
so Edmonds odd-set inequalities are only a small part of the required
stable-set/rank hierarchy. The exact sufficient rounding condition is the
weighted rank inequality

\[
 w\cdot x\le(1+\varepsilon_m)\alpha_w(G_H)
 \quad\hbox{for every }w\ge0,                             \tag{0.6}
\]

where \(G_H\) is the conflict graph on complete multidepth routes. If
\(\varepsilon_m=o(1/H)\), then a convex-decomposition rounding theorem
produces one integral route packing with

\[
 \boxed{
 H\cdot(\text{discarded owners})
 +(\text{missing typed targets})=o(W).}                    \tag{0.7}
\]

In particular the owner leave is \(o(W/H)\). This is an exact conditional
rounding theorem.

Ordinary iterative rounding does not currently prove (0.6). At the
symmetric point every route variable is \(1/D=o(1)\), every owner degree
is exactly one, and every fixed odd blossom has large slack. Thus neither
a large-variable rule nor a low-degree-resource rule can start. A proof
must use a quantitative matching/nibble theorem preserving all-depth
target claims, or establish the full weighted rank bound (0.6). Owner
pair-codegrees alone do neither.

## 1. The unrestricted common-route catalogue

Let

\[
                         \mathcal O=\binom{[2m]}m,
 \qquad W=|\mathcal O|.
\]

Fix \(H\le\ell/2\), where \(\ell\) is a power of two. Let
\(\mathscr R\) be the full indexed coordinate orbit of the legal recursive
\(F_\ell\)-necklaces, together with whatever radius and collar decorations
the declared constant-one compiler requires.

Each route \(R\in\mathscr R\) carries:

* its owner set \(M(R)\), of size \(2\ell\);
* every physical lower and upper target through depth \(H\);
* one common coordinate frame and cyclic order serving all depths.

Let

\[
 \mathcal T
 =\{(q,\sigma,T):
       1\le q\le H,\ \sigma\in\{-,+\},\
       |T|=m+\sigma q\}                                    \tag{1.1}
\]

be the typed literal target set. For a route \(R\), let
\(C_H(R)\subseteq\mathcal O\dot\cup\mathcal T\) be the union of its owner
claims and all its certified typed-target claims.

There are two relevant conflict graphs.

1. \(G_{\rm own}\) has vertex set \(\mathscr R\), with
   \(R\sim R'\) when \(M(R)\cap M(R')\ne\varnothing\).
   Its stable sets are owner-disjoint physical route families.
2. \(G_H\) has \(R\sim R'\) when
   \(C_H(R)\cap C_H(R')\ne\varnothing\).
   Its stable sets are simultaneously owner-disjoint and target-rainbow
   through every protected depth.

The second graph is a stronger sufficient architecture. In the
radius-thinned SCD normalization, where certified source and target totals
agree, a stable set covering all resources is exactly a literal
multidepth resolution.

## 2. Blossom inequalities in the augmented master LP

Use the common multidepth primal from the preceding note:

\[
 \begin{aligned}
 \min\quad&
 \sum_Rd_Rx_R+\sum_X\kappa_Xe_X+\sum_tw_th_t,\\
 \text{subject to}\quad&
 \sum_{R:X\in M(R)}x_R+e_X=1 &&(X\in\mathcal O),\\
 &\sum_{R:t\in C_H(R)}x_R+h_t\ge1 &&(t\in\mathcal T),\\
 &x_R,e_X,h_t\ge0.                                        \tag{2.1}
 \end{aligned}
\]

Let \(\mathfrak C\) be a family of odd cycles in \(G_{\rm own}\). For
\(C\in\mathfrak C\), put

\[
                         r_C={|C|-1\over2}.
\]

Every integral owner packing satisfies

\[
                         \sum_{R\in C}x_R\le r_C.           \tag{2.2}
\]

Adjoin (2.2) to (2.1).

### Proposition 2.1 (blossom-augmented dual)

The dual of the blossom-augmented LP is

\[
 \boxed{
 \begin{aligned}
 \max\quad&
 \sum_ty_t-\sum_Xz_X-\sum_{C\in\mathfrak C}r_C\gamma_C,\\
 \text{subject to}\quad&
 0\le y_t\le w_t,\qquad z_X\ge-\kappa_X,\qquad
 \gamma_C\ge0,\\
 &\sum_{t\in C_H(R)}y_t-\sum_{X\in M(R)}z_X
   -\sum_{C\ni R}\gamma_C\le d_R
                                      &&(R\in\mathscr R).
 \end{aligned}}                                           \tag{2.3}
\]

#### Proof

Use the dual variables \(y_t,z_X\) as in the unaugmented common-route
dual. Put a multiplier \(\gamma_C\ge0\) on

\[
                         \sum_{R\in C}x_R-r_C\le0.
\]

It contributes \(-r_C\gamma_C\) to the dual objective and
\(\sum_{C\ni R}\gamma_C\) to the Lagrangian coefficient of \(x_R\).
Rearranging the nonnegativity of that coefficient gives the route
inequality in (2.3). \(\square\)

The same formula applies to any valid rank cut

\[
                         \sum_{R\in\mathcal A}x_R
                         \le\nu(\mathcal A),                \tag{2.4}
\]

where \(\nu(\mathcal A)\) is the largest owner-disjoint subfamily of
\(\mathcal A\). One replaces \(r_C\) by \(\nu(\mathcal A)\) and
\(\gamma_C\) by \(\gamma_{\mathcal A}\).

## 3. Recursive-frame odd cycles and deficiency form

Let \(B_0,\ldots,B_{2r}\) be genuine recursive-frame necklaces such that

\[
 B_{i-1}\cap B_i=\{X_i\}
\]

at distinct anchors, and nonconsecutive necklaces are owner-disjoint.
Let \(\mathscr B_i\) be a bundle of variants of \(B_i\) which retain this
intersection law, and set

\[
                         a_i=\sum_{R\in\mathscr B_i}x_R.    \tag{3.1}
\]

At anchor \(X_i\), let \(g_i\) be the total incidence of selected routes
outside \(\mathscr B_{i-1}\cup\mathscr B_i\), and let \(e_i\) be its
discarded mass. The owner equation is

\[
                         a_{i-1}+a_i+g_i+e_i=1.             \tag{3.2}
\]

### Proposition 3.1 (odd-cycle blossom and escape)

Every integral solution satisfies

\[
                         \sum_{i=0}^{2r}a_i\le r,           \tag{3.3}
\]

and therefore

\[
                         \boxed{\sum_{i=0}^{2r}(g_i+e_i)\ge1.} \tag{3.4}
\]

#### Proof

An integral owner packing can choose variants from at most \(r\) of the
\(2r+1\) cyclic bundles, since chosen bundle indices form an independent
set of \(C_{2r+1}\). This proves (3.3).

Sum (3.2) over all anchors. Every \(a_i\) occurs twice, so

\[
 2\sum_i a_i+\sum_i(g_i+e_i)=2r+1.
\]

Use (3.3) to obtain (3.4). \(\square\)

The pairwise owner equations alone yield only

\[
                         \sum_i a_i\le r+\frac12.
\]

Thus (3.4) is exactly the missing half-unit escape from the restricted
half-cycle solution.

For a general route subfamily \(\mathcal A\), the exact necessary
inequality is (2.4), not merely its odd-cycle special case. Equivalently,
for every nonnegative weight field \(w\) on routes,

\[
 \boxed{
 \sum_Rw_Rx_R\le\alpha_w(G_{\rm own}),}                    \tag{3.5}
\]

where \(\alpha_w\) is the maximum weight of an owner-disjoint route
family. The collection (3.5) is the complete weighted rank hierarchy.

## 4. Exact unrestricted-orbit codegrees

Take the indexed orbit of one \(R_0=2\ell\) necklace. Its exact owner
degree is

\[
                         D=R_0(m!)^2.                       \tag{4.1}
\]

Give every indexed route the symmetric weight

\[
                         x_R={1\over D}.                    \tag{4.2}
\]

Every owner then has total weight one.

If two middle owners have Johnson distance \(j\), their indexed route
codegree is

\[
 \lambda_j=
 \begin{cases}
 \displaystyle{2D\over\binom mj^2},&1\le j<\ell,\\[6pt]
 \displaystyle{D\over\binom m\ell^2},&j=\ell,\\[6pt]
 0,&j>\ell.
 \end{cases}                                               \tag{4.3}
\]

In particular,

\[
 \boxed{
 \max_{X\ne Y}
 \sum_{R:X,Y\in M(R)}x_R={2\over m^2}.}                    \tag{4.4}
\]

No orientation cube, and hence no recursive necklace, contains a Johnson
triangle. Thus for pairwise Johnson-adjacent
\(X_a,X_b,X_c\),

\[
 \boxed{
 \sum_{R:X_a,X_b,X_c\in M(R)}x_R=0.}                       \tag{4.5}
\]

These are exact orbit identities, not independence estimates.

## 5. Cross-gadget routes overwhelm every fixed triangle blossom

Fix the physical triangle

\[
 X_a=K+a,\qquad X_b=K+b,\qquad X_c=K+c.
\]

Let \(\mathscr B_{ab}\) be all unrestricted orbit necklaces containing
\(X_a,X_b\), and define the other two bundles cyclically. Put

\[
 a_{ab}=x(\mathscr B_{ab}),\quad
 a_{bc}=x(\mathscr B_{bc}),\quad
 a_{ca}=x(\mathscr B_{ca}).                                \tag{5.1}
\]

Equations (4.4)--(4.5) give

\[
 a_{ab}=a_{bc}=a_{ca}={2\over m^2},                        \tag{5.2}
\]

and the three bundle families are disjoint.

At \(X_a\), define \(g_a\) to be the mass of routes which contain \(X_a\)
but neither \(X_b\) nor \(X_c\). Then

\[
                         g_a=1-{4\over m^2},                \tag{5.3}
\]

and similarly at \(X_b,X_c\).

### Theorem 5.1 (fractional unrestricted triangle escape)

At the symmetric unrestricted point,

\[
 \boxed{
 a_{ab}+a_{bc}+a_{ca}={6\over m^2}=o(1)<1,}                \tag{5.4}
\]

while

\[
 \boxed{
 g_a+g_b+g_c=3-{12\over m^2}.}                             \tag{5.5}
\]

Thus the blossom escape condition (3.4) has asymptotic slack two.

#### Proof

Equation (5.4) is the sum of (5.2). Equation (4.5) says that the two
pair-bundle families incident with one anchor are disjoint. Subtract their
total mass \(4/m^2\) from the owner degree one to obtain (5.3), and sum.
\(\square\)

The restricted determinant-two point put mass \(1/2\) on three specially
chosen necklaces. The unrestricted symmetric point does not approximate
that adversarial face: it disperses the same anchor mass over almost
entirely single-anchor cross-gadget routes.

## 6. Uniform escape from larger odd anchor sets

Let \(S\subseteq\mathcal O\), and write

\[
                         k_R(S)=|M(R)\cap S|.
\]

### Proposition 6.1 (pair-moment escape)

At the symmetric unrestricted point,

\[
 \boxed{
 \sum_R\binom{k_R(S)}2x_R
 \le {2\over m^2}\binom{|S|}{2}.}                         \tag{6.1}
\]

Consequently,

\[
 \boxed{
 \sum_{R:k_R(S)=1}x_R
 \ge |S|-{2|S|(|S|-1)\over m^2}.}                         \tag{6.2}
\]

#### Proof

Double-count pairs of distinct owners of \(S\) lying on one route:

\[
 \sum_R\binom{k_R(S)}2x_R
 =\sum_{\{X,Y\}\in\binom S2}
   \sum_{R:X,Y\in M(R)}x_R.
\]

Apply (4.4) termwise to obtain (6.1).

The owner degree equations give

\[
 |S|=\sum_Rk_R(S)x_R.
\]

For \(k\ge2\), one has \(k\le2\binom k2\). Therefore the total incidence
from routes meeting \(S\) at least twice is at most twice the left side of
(6.1). Removing it from \(|S|\) proves (6.2). \(\square\)

For \(|S|=O(H)=O(\sqrt m)\), the error term in (6.2) is \(O(m^{-1})\).
Thus every Gaussian-size odd anchor system has essentially \(|S|\) units
of single-anchor cross-gadget mass. All such owner blossoms are very far
from tight at the symmetric fractional point.

This conclusion concerns owner incidences. It gives no bound on collisions
among the lower and upper typed targets carried by those escaping routes.

## 7. Why Edmonds blossoms are not the full polytope

If every route were an edge joining two owner resources, then the owner
packing problem would be graph matching, and degree constraints plus all
odd-set inequalities would describe its matching polytope.

A necklace claims \(2\ell\) owners. The owner packing problem is therefore
hypergraph matching, or equivalently stable set in \(G_{\rm own}\).
Odd cycles give necessary inequalities, but the exact stable-set polytope
is

\[
 \operatorname {STAB}(G_{\rm own})
 =
 \left\{
 x\ge0:
 w\cdot x\le\alpha_w(G_{\rm own})
 \text{ for every }w\ge0
 \right\}.                                                \tag{7.1}
\]

The equality follows from separation and the fact that the stable-set
polytope is down-monotone: a separating normal may be replaced by its
nonnegative part.

Thus even perfect control of every odd necklace cycle would not prove
integrality. Higher cliques, odd antiholes, and general weighted rank
facets remain. Adding typed-target noncollision replaces
\(G_{\rm own}\) by the still larger graph \(G_H\).

## 8. A blossom-complete rounding theorem

The following theorem gives the exact quantitative condition needed for
the requested \(o(W/H)\) owner leave.

Let \(\mathcal Z=\mathcal O\dot\cup\mathcal T\) be a resource family and
let \(C_H(R)\subseteq\mathcal Z\) be the claims of route \(R\). Assume a
fractional common-route resolution

\[
 \boxed{
 \sum_{R:z\in C_H(R)}x_R=1
 \qquad(z\in\mathcal Z).}                                  \tag{8.1}
\]

Let \(G_H\) join routes with intersecting claim sets.

### Theorem 8.1 (weighted-rank rounding)

Suppose that, for some \(\varepsilon\ge0\),

\[
 \boxed{
 w\cdot x\le(1+\varepsilon)\alpha_w(G_H)
 \qquad\hbox{for every }w\ge0.}                            \tag{8.2}
\]

Then there is an integral stable set \(\mathcal I\) of routes such that

\[
 \boxed{
 H\,|\mathcal O\setminus C_H(\mathcal I)|
 +|\mathcal T\setminus C_H(\mathcal I)|
 \le{\varepsilon\over1+\varepsilon}
       \bigl(H|\mathcal O|+|\mathcal T|\bigr).}             \tag{8.3}
\]

#### Proof

By (7.1), condition (8.2) is exactly

\[
                         {x\over1+\varepsilon}
                         \in\operatorname {STAB}(G_H).
\]

Hence there are stable sets \(\mathcal I_j\) and coefficients
\(\lambda_j\ge0\), \(\sum_j\lambda_j=1\), such that

\[
 {x\over1+\varepsilon}
 =\sum_j\lambda_j\mathbf1_{\mathcal I_j}.                  \tag{8.4}
\]

Give every owner resource weight \(H\) and every typed target weight one.
Since each \(\mathcal I_j\) is stable, its route claim sets are disjoint,
so the total weight it covers is the sum of the weights of its selected
route claims. Averaging (8.4) and using (8.1), the expected covered weight
is

\[
 {1\over1+\varepsilon}
 \bigl(H|\mathcal O|+|\mathcal T|\bigr).
\]

Some \(\mathcal I_j\) covers at least this much. Its uncovered weight
satisfies (8.3). \(\square\)

### Corollary 8.2 (coefficient-scale leave)

If

\[
                         |\mathcal T|=O(HW)
\]

and (8.2) holds with

\[
                         \varepsilon=o(1/H),
\]

then the selected integral route family has

\[
 |\mathcal O\setminus C_H(\mathcal I)|=o(W/H),
\qquad
 |\mathcal T\setminus C_H(\mathcal I)|=o(W).               \tag{8.5}
\]

This is the requested iterative-rounding conclusion at the level of an
exact convex decomposition. If maximum-weight stable-set separation for
the relevant route graph were available, (8.4) could be produced by
column generation and peeled iteratively. The unresolved mathematics is
the weighted rank estimate (8.2), not the final rounding step.

## 9. Why elementary iterative rounding stalls

At the symmetric orbit point,

\[
                         x_R={1\over D}
\]

for every indexed route, while \(D=2\ell(m!)^2\) is enormous. Thus there
is no route variable bounded below by any inverse polynomial in \(m\).

Every owner equation is exactly tight with fractional degree one. Hence
there is no low-degree owner constraint which can be discarded cheaply.
By Theorem 5.1 and Proposition 6.1, every fixed or Gaussian-size odd
blossom has large slack, so no such blossom forces a variable to become
large.

Therefore the two standard iterative-rounding moves,

1. round a variable of value at least a fixed threshold;
2. drop a constraint of small residual support,

do not follow from the current orbit identities. A successful iteration
must instead select a large pseudorandom nibble and prove that after
conditioning:

* owner degrees remain nearly regular;
* every lower and upper target degree remains adequate;
* the weighted rank ratio in (8.2) stays \(1+o(1/H)\);
* the accumulated owner leave is \(o(W/H)\).

The exact owner codegree ratio \(2/m^2\) is favorable, but generic
growing-uniformity matching theorems do not give the needed leave. For an
\(R_0\)-uniform \(D\)-regular hypergraph with maximum codegree \(C\), the
available general estimate has uncovered fraction of order

\[
 R_0\left({C\log(1+C)\over D}\right)^{1/(R_0-1)}.           \tag{9.1}
\]

With \(R_0=2\ell\) growing polynomially, the exponent
\(1/(R_0-1)\) makes (9.1) far larger than \(1/H\), and often vacuous.
Object-specific recursive-frame structure is therefore essential.

## 10. Exact implication boundary

The following statements are proved.

1. The necessary recursive-frame odd-cycle inequalities are (3.3), with
   escape form (3.4).
2. Their exact blossom-augmented common-route dual is (2.3).
3. At the symmetric unrestricted orbit point, every physical triangle
   blossom has the exact slack (5.4)--(5.5).
4. Every Gaussian-size odd anchor set has the uniform escape bound (6.2).
5. Odd blossoms alone do not describe the whole-necklace packing
   polytope.
6. The full weighted rank estimate (8.2), with
   \(\varepsilon=o(1/H)\), yields an integral route family with
   \(o(W/H)\) discarded owners and \(o(W)\) typed-target holes.

The following statements are not proved.

1. The weighted rank estimate (8.2) for the unrestricted recursive-frame
   catalogue.
2. Preservation of its target degrees under a long pseudorandom nibble.
3. A global coefficient-one construction.

The local determinant-two obstruction is therefore neutralized
fractionally by cross-gadget routes, but not yet rounded. The minimal
remaining theorem is a blossom-complete, all-depth weighted matching bound
at relative error \(o(1/H)\); pair codegrees and fixed odd-set inequalities
do not by themselves reach that scale.
