# Direct edgewise side lifts: an exact recursive gate and a chained (3\to7) construction

Date: 2026-07-31  
Status: all-(n) identities and one-sided Hall theorem; exact coupled
reduction; independently replayed *chained* strict constructions at child
parameters (n=3,4,5,6).  The coupled all-(n) matching/forest theorem is
open.  A child-(n=7) continuation is running remotely and is not used below.

## 0. Result

Let (F) be an oriented Catalan linear matching on the (n)-sets of a
(2n)-set (Omega), with (n\ge3) for the complete collar.  Write an atom as

\[
 q=(L_q,U_q,t_q,h_q),\qquad
 L_q=t_q\cap h_q,\quad U_q=t_q\cup h_q.               \tag{0.1}
\]

There is a much smaller subclass of the two punctured side forests than
arbitrary containment diamonds.  For (x\notin U_q), lift (q) to

\[
 q\uparrow x=(L_q+x,U_q+x,t_q+x,h_q+x),               \tag{0.2}
\]

and for (x\in L_q), project it to

\[
 q\downarrow x=(L_q-x,U_q-x,t_q-x,h_q-x).             \tag{0.3}
\]

Both are literal diamonds on the upper and lower side rails of the
two-coordinate collar.

Here **direct** means direct at the level of the undirected physical edge
and its two palette labels.  The order (t_q,h_q) is auxiliary.  Once the
complete support is proved to be a path forest, each final path is oriented
consistently, and an individual lifted edge may thereby be reversed.  The
stronger ordered-lift condition requiring every occurrence to inherit the
arrow (t_q\to h_q) is a different problem and is not certified by the
finite chain below.

This note proves four things.

1. The two child-induced candidate graphs have an exact degree law:
   every extreme outer colour has occurrence-degree (n+2), while a
   middle vertex (v) has occurrence-degree
   (n-d_F(v)).  Consequently each side candidate graph always has a
   matching saturating its extreme shore, for every child forest (F).
2. Requiring the correct punctures turns the two matchings into an exact
   common-basis problem on the child edges.  Adding physical degree/anchor
   caps and one graphic condition is necessary and sufficient for a recursive
   Catalan linear matching.
3. This strict undirected-support system is feasible in one literal chain
   (n=3\to4\to5\to6\to7): every child after the first is exactly the output
   of the preceding strict lift.  The final objects have respectively
   (14,42,132,429) path components, as required.
4. The finite chain is evidence, not induction.  What is still missing is
   a common basis together with representatives lying in the appropriate
   partition/graphic face.

The direct lifts are therefore a genuine candidate for the all-(n)
recursion; they are not merely a rephrasing of the unrestricted finite
fixtures.

## 1. Parameters and candidate graphs

Put

\[
 M=\binom{2n}{n},\qquad N=\binom{2n}{n-1},\qquad
 P=\binom{2n}{n-2},\qquad C=M-P,\qquad R=N-C.          \tag{1.1}
\]

The child support (F) is a path forest with (N) edges on the (M)
rank-(n) vertices and (\operatorname{Cat}_n=M-N) components.

Define an occurrence multigraph (G_F^-) with left shore
(X=\binom\Omega n), right shore
(W^-=\binom\Omega{n+2}), and one occurrence edge

\[
       L_q+x\;\longleftrightarrow\;U_q+x              \tag{1.2}
\]

for every pair ((q,x)) with (x\notin U_q).  The occurrence remembers
((q,x)), even if two occurrences have the same endpoints.  Define
(G_F^+) dually between (W^+=\binom\Omega{n-2}) and (X), using

\[
       L_q-x\;\longleftrightarrow\;U_q-x              \tag{1.3}
\]

for (x\in L_q).

### Theorem 1.1 (exact candidate degrees)

In (G_F^-), every (V\in W^-) has occurrence-degree (n+2), and every
(D\in X) has occurrence-degree

\[
                         d_{G_F^-}(D)=n-d_F(D).        \tag{1.4}
\]

In (G_F^+), every (A\in W^+) has occurrence-degree (n+2), and every
(D\in X) again has occurrence-degree (n-d_F(D)).

#### Proof

Fix (V\in\binom\Omega{n+2}).  For every (x\in V), the child upper
palette contains a unique atom (q_x) with (U_{q_x}=V-x).  Then
((q_x,x)) is one occurrence incident with (V), and these are all its
(n+2) occurrences.

Now fix (D\in\binom\Omega n).  For every (x\in D), the child lower
palette contains a unique atom (q_x) with (L_{q_x}=D-x).  The pair
((q_x,x)) is a lift occurrence unless (x\in U_{q_x}).  The latter holds
exactly when (D) is one of the two physical endpoints of (q_x).
Incidences (q\ni D) and invalid coordinates (x=D\setminus L_q) are
therefore in bijection.  This proves (1.4).  Complementation gives the
lower-side statement. \(\square\)

### Corollary 1.2 (unpunctured side Hall is automatic)

For every (F), (G_F^-) has a matching saturating all (P) vertices of
(W^-), and (G_F^+) has a matching saturating all (P) vertices of
(W^+).  More precisely, for every nonempty
(mathcal A\subseteq W^-),

\[
             |N_{G_F^-}(\mathcal A)|
             \ge \left\lceil {n+2\over n}|\mathcal A|\right\rceil
             >|\mathcal A|,                            \tag{1.5}
\]

and the dual inequality holds below.

#### Proof

There are exactly ((n+2)|\mathcal A|) candidate occurrences leaving
(mathcal A).  By (1.4), each middle neighbour receives at most (n)
occurrences.  Hence
((n+2)|\mathcal A|\le n|N(\mathcal A)|).  This count remains valid in
the presence of parallel occurrences.  Hall's theorem applies.  The lower
side is dual. \(\square\)

Thus the strict recursive ansatz has no isolated one-sided outer-palette
obstruction.  The real constraint is which middle vertices are left
unmatched on the two shores.

### Theorem 1.3 (physical lift-degree law)

Let (H_F^-) be the physical occurrence multigraph on
(\binom\Omega{n+1}) containing all edges (e^-(q,x)), and define
(H_F^+) dually on (\binom\Omega{n-1}).  Then

\[
\begin{aligned}
 d_{H_F^-}(Y)&=\sum_{x\in Y}d_F(Y-x)-2,
                    &&Y\in\binom\Omega{n+1},\\
 d_{H_F^+}(Z)&=\sum_{x\notin Z}d_F(Z+x)-2,
                    &&Z\in\binom\Omega{n-1}.          \tag{1.6}
\end{aligned}
\]

In particular, an upper physical vertex (Y) has degree zero exactly when
the unique child edge of upper colour (Y) is a one-edge component of
(F) and every other rank-(n) facet of (Y) is an isolated child
vertex.  Hence there are at most (K=\operatorname{Cat}_n) zero-degree
vertices on either side.

#### Proof

An occurrence incident with (Y) is obtained by choosing (x\in Y) and
an edge of (F) incident with (Y-x), except that the child edge whose
upper colour is (Y) is forbidden for each of its two endpoints: in those
two representations the added label (x) already lies in the child upper
colour.  This proves the first identity.  The second is its deletion dual.

The two endpoints of the unique upper-colour-(Y) child edge already
contribute one each to the displayed sum.  Equality with two therefore
forces both endpoint degrees to be one and every other facet degree to be
zero; the converse is immediate.  Distinct zero-degree (Y)'s have
distinct upper-colour child edges, so their number is at most the number of
one-edge components, and hence at most (K). \(\square\)

Any no-empty anchored side must put every such zero-degree vertex into its
anchor bank.  Thus (1.6) gives a canonical forced subset of (Q), of order
at most (K) on each shore.  Selecting one common (Q) containing both
forced sets remains part of the coupled gate.

## 2. Exact coupled SDR condition

Orient every component of (F).  For (Q\subseteq E(F)), put

\[
 T(Q)=\{t_q:q\in Q\},\qquad H(Q)=\{h_q:q\in Q\}.       \tag{2.1}
\]

The maps (q\mapsto t_q) and (q\mapsto h_q) are injective.  A strict
upper selection is a set (S^-\) of (P) occurrences ((q,x)), and a
strict lower selection is a set (S^+\) of (P) occurrences.

### Theorem 2.1 (strict coupled SDR normal form)

The side outer palettes and inherited central ports are exact if and only
if there is one (Q\subseteq E(F)), (|Q|=C), such that

\[
\begin{aligned}
 \{U_q+x:(q,x)\in S^-\}&=\binom\Omega{n+2},\\
 \{L_q+x:(q,x)\in S^-\}&=X\setminus T(Q),             \tag{2.2}\\
 \{L_q-x:(q,x)\in S^+\}&=\binom\Omega{n-2},\\
 \{U_q-x:(q,x)\in S^+\}&=X\setminus H(Q).             \tag{2.3}
\end{aligned}
\]

Every equality is an equality of sets, so it includes injectivity.

#### Proof

The two pure diagonal sectors have (P) atoms each.  On the upper side,
the (C) middle lower colours omitted by the pure sector must be exactly
the (C) inherited tail ports used by the (0\to z) seams; this is
(2.2).  The lower statement is identical with heads and (2.3).  Conversely,
these four equalities partition both outer palettes among the five collar
sectors. \(\square\)

There is an exact matroid formulation.  Let (mathcal T_F^-) be the
transversal matroid on (X) represented by (G_F^-), and let
(mathcal T_F^+) be its lower analogue.  Corollary 1.2 says both have
rank (P).  Pull ((\mathcal T_F^-)^*) back through the tail injection and
((\mathcal T_F^+)^*) back through the head injection.  Call the resulting
restrictions (mathcal A_F^{\rm dir}) and
(mathcal B_F^{\rm dir}).  Their ranks are at most (C), but Corollary 1.2
does not prove equality: rank (C) is equivalent to independence of the
non-tail, respectively non-head, terminal bank in the corresponding
primal transversal matroid.  Then (2.2)--(2.3) hold for one (Q) exactly
when (Q) is a common basis.  Equivalently,

\[
 r_{\mathcal A_F^{\rm dir}}(S)+
 r_{\mathcal B_F^{\rm dir}}(E(F)\setminus S)\ge C
                       \quad(S\subseteq E(F)).         \tag{2.4}
\]

Unlike the unrestricted two-shadow common-basis theorem, (2.4) has not
been proved uniformly.  The representing graphs here retain only the
child-edge lifts (1.2)--(1.3).

### Proposition 2.2 (the unrestricted uniform-density proof cannot transfer)

For the authenticated parameter-(3) base forest, the minimum rank density
of the strict upper pulled-back dual matroid is (3/4), whereas the density
needed to repeat the unrestricted common-basis proof is

\[
                           {C\over N}={14\over15}.      \tag{2.5}
\]

The lower strict dual has minimum density (10/11), also below (14/15).
Nevertheless, the two strict matroids have four common bases of order
(14).  Recording a basis by the unique retained edge, their ids are

\[
                              0,1,5,11.                \tag{2.6}
\]

#### Proof

There are only fifteen child edges.  Exhaust all (2^{15}) subsets on
each shore.  For a subset (S) of tail (respectively head) endpoints,
compute

\[
 r_{\mathcal T^*}(S)=|S|-6+
 r_{\mathcal T}(X\setminus S)                         \tag{2.7}
\]

by exact augmenting-path matching in the strict candidate graph.  The
upper minimum (3/4) occurs already on edge set
({0,1,5,11}), whose dual rank is three.  The lower minimum (10/11)
and the basis list follow from the same exhaustive computation. \(\square\)

Thus the strict route does not inherit the clean constant-vector proof of
the unrestricted incidence theorem.  It needs either a different common-
basis argument or a recursively preserved choice rule.  The exact audit is

```text
scratch/audit_catalan_direct_edgewise_n3_matroid_density_20260731.py
scratch/catalan_direct_edgewise_n3_matroid_density_20260731.audit.json
```

## 3. The physical condition

For a chosen occurrence ((q,x)), let its undirected physical edge be

\[
 e^-(q,x)=\{t_q+x,h_q+x\},\qquad
 e^+(q,x)=\{t_q-x,h_q-x\}.                             \tag{3.1}
\]

Use the usual five sectors: child trace (c), pure upper trace (0),
central trace (z), pure lower trace (cz), and the two seam families for
(Q).  Let (mathcal G(F,Q,S^-,S^+)) be their complete undirected
physical support.

### Theorem 3.1 (exact undirected-support recursive condition)

The strict direct support produces a Catalan linear matching at parameter
(n+1) if and only if (2.2)--(2.3) hold and

\[
       \Delta(\mathcal G)\le2,\qquad \mathcal G\text{ is acyclic}. \tag{3.2}
\]

Equivalently, one may require the two side supports to be anchor-capped
linear forests and the contracted attachment graph (\Gamma_Q) to be a
forest.

#### Proof

Theorem 2.1 gives every lower and upper outer colour exactly once.  The
middle traces are disjoint.  Condition (3.2) says the undirected physical
support is a linear forest.  Orient every path consistently; then tail and
head roles are globally injective, and every oriented physical edge is one
of the two valid orientations of its diamond.  This is exactly a Catalan
linear matching.  This argument does not preserve the auxiliary arrows of
the child occurrences.  The contracted formulation is the forest
contraction identity.
\(\square\)

### Corollary 3.1A (the untouched rail has an independent parent)

Let (G) be any Catalan linear forest at child parameter (n).  Replace
the isolated translated rail (c+F) by (c+G), leaving (Q), the two
direct sides, the punctured (z)-rail and both seam families unchanged.
All palettes remain exact, and the result is a linear forest if and only if
(G) and the complementary three-sector support are linear forests.

#### Proof

The (c)-rail uses exactly the two tagged palette banks
(c+\binom\Omega{n-1}) and (c+\binom\Omega{n+1}), independently of its
Catalan forest.  No seam or side edge meets a (c)-rail physical vertex.
Palette multiplicities and physical topology therefore direct-sum.
\(\square\)

Thus the general recursion is two-parent: (F) supplies direct incidence
and attachment geometry, while an independently chosen (G) supplies the
untouched rail.  The chained witness below is only the specialization
(G=F).

This makes the missing theorem a coupled **matching + partition + graphic**
selection problem.  Bare Hall, including Corollary 1.2, does not imply the
graphic row.

### Lemma 3.2 (the observed no-empty shore is one graphic base)

Fix an anchor set (A) of order (C) in one side physical layer, and let
(S) be a (P)-edge side forest on all (N) physical vertices.  Adjoin a
new vertex (\rho) and the star

\[
                         E_\rho=\{\rho a:a\in A\}.     \tag{3.3}
\]

Then every component of (S) contains an anchor if and only if there is
(R_\rho\subseteq E_\rho), (|R_\rho|=C-K=N-P), for which

\[
                         S\cup R_\rho                 \tag{3.4}
\]

is a spanning tree.

#### Proof

If every component contains an anchor, choose one anchor in each component
and join it to (\rho).  The number of components is (N-P=C-K), and the
result is connected with (N) edges on (N+1) vertices, hence a tree.
Conversely, remove the root-star edges from a tree (3.4).  Every resulting
component contains the anchor incident with its unique former root edge;
two root edges into one component would have made a cycle through (\rho).
\(\square\)

Thus the empirically stable upper-shore condition below is not informal
topology: it is a graphic-matroid base condition after adjoining one root
star.  The palette rows remain two independent partition/matching rows, so
this observation does not turn the full selection into ordinary two-matroid
intersection.

## 4. Literal chained construction through parameter seven

The retained search starts from the authenticated parameter-(3) child
forest.  At each step it permits only the undirected occurrence supports
(0.2)--(0.3), enforces (2.2)--(2.3), the physical degree and seam-anchor
caps, then adds literal cycle cuts from the complete three-rail support.
The output path forest is coherently oriented and fed into the next step;
that new component orientation is part of the next-stage choice.

An independent consumer reconstructs every atom and checks all four
palettes, both side forests, the contracted (\Gamma_Q), and the final
ambient path decomposition.  The result is

\[
\begin{array}{c|rrrrrr}
n&M&N&P&C&|Q|&\#\text{ambient paths}\\ \hline
3&20&15&6&14&14&14\\
4&70&56&28&42&42&42\\
5&252&210&120&132&132&132\\
6&924&792&495&429&429&429.
\end{array}                                             \tag{4.1}
\]

Thus one strict recursive chain constructs Catalan linear matchings at
parameters (4,5,6,7).  In every row the two side and full cycle ranks are
zero and the full maximum degree is two.

There is one additional, non-forced pattern worth preserving.  If (c_j)
counts side components containing (j) seam anchors, the selected shores
have

\[
\begin{array}{c|cc}
n&(c_0,c_1,c_2)^-&(c_0,c_1,c_2)^+\\ \hline
3&(0,4,5)&(0,4,5)\\
4&(0,14,14)&(1,12,15)\\
5&(0,48,42)&(2,44,44)\\
6&(12,141,144)&(16,133,148).
\end{array}                                             \tag{4.2}
\]

In particular, the upper strict side has no anchor-free component through
child parameter five; the child-six continuation is the first member of
this chain with anchor-free components on both shores.  Thus the earlier
``one no-empty shore'' pattern was finite evidence rather than a propagated
invariant.  The exact component ledger still holds, but any induction must
carry a cover-down/attachment state that permits a sparse empty-component
bank.

The physical-degree law (1.6) exposes a second local state.  Define the two
facet slacks by

\[
 \eta^-(F)=\min_Y d_{H_F^-}(Y),\qquad
 \eta^+(F)=\min_Z d_{H_F^+}(Z).                       \tag{4.3}
\]

Along the chained children they are

\[
\begin{array}{c|rrrr}
n&3&4&5&6\\ \hline
\eta^-(F_n)&3&3&4&5\\
\eta^+(F_n)&3&3&3&4.
\end{array}                                           \tag{4.4}
\]

Thus every physical vertex has at least three strict continuation
occurrences at every audited stage; in particular none is forced to become
an anchor.  The local candidate propagation invariant surviving all four
stages is

\[
                         \boxed{\eta^\pm(F)\ge3}.                  \tag{4.5}
\]

The child-six row refutes the stronger no-empty-shore invariant previously
suggested by the first three stages.  A proof of DERF must therefore combine
(4.5) with a cover-down/attachment state which permits sparse anchor-free
components.  Proving that a recursively supplied child has an extension
whose output again has this enlarged state would be enough for induction.
No such preservation theorem is presently claimed.

The independently replayed files are

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.witness.json
scratch/audit_catalan_direct_edgewise_side_lift_n3_n6_20260731.py
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.audit.json
```

The witness file is solver-produced.  The audit does not trust its claimed
palettes or topology; it reconstructs them from the child paths, child-edge
indices and lift coordinates.

## 5. Propagation invariant and exact missing theorem

The finite one-parent chain reuses an undirected Catalan path support together with a
fresh coherent orientation of every component: the next candidate bank and
all of its degrees are reconstructed from that oriented child.  No
symmetry, SCD, or hidden ordering is assumed.  What has *not* been shown is
that every Catalan forest—or even every forest produced by this strict
recursion—has a component orientation satisfying the next coupled
selection.

Component orientation does not change either direct occurrence multigraph:
the conditions (x\notin U_q), (x\in L_q), the palette labels and the
undirected physical edge depend only on the child edge.  On each child path,
orientation only chooses which terminal vertex is omitted from the tail
image and which is omitted from the head image.  Hence any strict balanced-
expansion preservation argument is a Boolean endpoint-choice problem before
the common set (Q) is selected; it is not a search over different
occurrence graphs.

The sharp induction target is therefore:

> **Corrected two-parent direct edgewise recursive forest theorem (DERF).**  Start
> with the authenticated parameter-three undirected support, and call a
> support recursively supplied when it is the output of an earlier
> successful undirected direct lift.  Every recursively supplied structural
> support (F_n) has a coherent component orientation, a common independent
> (C)-set (Q) of
> (mathcal A_{F_n}^{\rm dir},mathcal B_{F_n}^{\rm dir}), and
> representatives (S^-,S^+) satisfying (3.2).  The untouched (c)-rail
> may be filled by an independent Catalan forest (G_n); structural and
> guarded filler outputs for the next parameter need not be the same
> forest.

The stronger assertions “every Catalan forest is extendable” and “every
coherent orientation is extendable” are false or unnecessary and are not
claimed.  A proof of corrected DERF, together with the parameter-(3)
base, would prove Catalan Linear Matching in every dimension.  In the
larger program this supplies the exact ordered four-transversal needed by
the carrier/compiler construction.

The all-(n) progress is therefore cleanly separated:

* candidate degrees and unpunctured side Hall: **proved**;
* exact coupled common-basis/graphic reduction: **proved**;
* chained strict construction through child (n=6): **verified**;
* common-basis representatives satisfying the graphic row for all (n):
  **open**.

There is also an exact caution about trying to replace this state by a
simple path-run invariant.  Consecutive lower colours and consecutive upper
colours along every child path are Johnson-adjacent.  For (n\ge6), one
can choose (Q) as exactly (\operatorname{Cat}_n) nontrivial contiguous
edge-runs, producing auxiliary path covers of both anchor palettes.
However, their internal anchors have degree two, so these are not selected
collar side atoms; and the deterministic run bank on the induced
parameter-six child has zero-candidate strict extremes on both shores.
Thus run structure and the direct common basis must be selected jointly.
The precise theorem and replay are in

```text
MATH_LEMMA_CATALAN_CONTIGUOUS_Q_RUN_BANK_AND_DIRECT_INCIDENCE_COUPLING_20260731.md
scratch/audit_catalan_contiguous_q_run_bank_20260731.py
```

## 6. Remote (n=7) status

The child-(n=7) continuation is materially larger and is not being run on
the user's local machine.  At the time of this update, one CPU search was
running under

```text
/home/amodo/or15/work/side_lift_recursive_20260731
```

on `ssh h100`.  No result from that run is used in any theorem above.  The
verified child-(n=6) row is retained in

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.witness.json
scratch/audit_catalan_direct_edgewise_side_lift_n3_n6_20260731.py
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.audit.json
```
