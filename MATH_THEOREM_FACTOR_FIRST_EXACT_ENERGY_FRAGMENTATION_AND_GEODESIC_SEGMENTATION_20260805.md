# Factor-first exact energy, upper-run fragmentation, and geodesic Catalan segmentation

**Date:** 2026-08-05  
**Method:** pure mathematics; exact counting and Johnson-path geometry; no
computation, search, solver, or probabilistic black box  
**Status:** unconditional identities and an exact sufficient extraction
theorem.  The note audits the factor-first valley reduction and the optional
threshold-core obstruction, corrects one residence sentence in the former,
and replaces the informal “quarter of the Catalan repeats” target by a
precise cap-two geodesic segmentation certificate.  It does **not** construct
that certificate in every dimension.

## 0. Setting

Put

\[
 n=2r-1,\qquad
 \mathcal L={ [n]\choose r-1},\qquad
 \mathcal O={ [n]\choose r},\qquad
 \mathcal H={ [n]\choose r+1},
\]

and

\[
 W=|\mathcal L|=|\mathcal O|,
 \qquad
 U=|\mathcal H|=W{r-1\over r+1},
 \qquad
 C=W-U={2W\over r+1}=\operatorname {Cat}_r.
\tag{0.1}
\]

Let (F) be the Johnson projection of a spanning simple two-factor of the
middle-level incidence graph.  Thus (F) is a spanning simple two-factor on
(\mathcal O), every edge (e=XY) has colours

\[
 \ell(e)=X\cap Y\in\mathcal L,
 \qquad
 u(e)=X\cup Y\in\mathcal H,
\tag{0.2}
\]

and (\ell:E(F)\to\mathcal L) is a bijection.  We call this the
**lower-exact factor** property.

## 1. Audit of the two input notes

The following parts of
`MATH_THEOREM_FACTOR_FIRST_CATALAN_VALLEY_COLLAR_REDUCTION_20260805.md`
are exact.

1. Suppressing every lower vertex of a middle-level two-factor produces a
   simple Johnson two-factor.  Two different lower vertices cannot produce
   the same Johnson edge, since that edge has the unique intersection colour
   (X\cap Y).
2. In an upper-surjective factor, the upper repeat surplus is exactly
   (W-U=C).
3. If consecutive edges (PM_0,M_0M_1) have the same upper colour, then
   their three owners are three facets of one rank-((r+1)) set and have
   exactly the displayed balanced-collar left-seam form.
4. A following collision-free Johnson arm and one fresh final transition
   give the literal generalized collar.

One sentence after Lemma 3.1 needs correction.  It says that separation by
more than (h) of **every** coordinate's successive insertion/deletion
events automatically makes every upper valley clean.  At an upper valley,
the seam label (\rho _1) is deleted on (P\to M_0) and immediately
reinserted on (M_0\to M_1).  Hence the stated unqualified separation
condition is incompatible with the valley it is meant to certify.  The
proof-safe replacement is:

> exempt the forced seam pair for (\rho _1), and require that the next
> (h+1) transitions have no other deletion/insertion collision, with the
> final deletion still in the old core and the final insertion fresh.

Lemma 3.1 itself already states the correct literal conditions and is not
affected.

The exact interval-cover number, robust one-point gap family, oscillating
collar, threshold slack, and conditional overload calculation in
`MATH_THEOREM_OPTIONAL_MIDDLE_CORE_THRESHOLD_CONTAINER_OBSTRUCTION_20260805.md`
also audit correctly.  In particular,

\[
 \tau_\square(\mathcal B)={g\choose g/2-1},
 \qquad
 \sigma(\mathcal A)={g\over r}
 {g\choose g/2}{2r-1-g\choose r-g/2},
\tag{1.1}
\]

and an aligned (b)-collar bank would overload that cut by the factor
((\sqrt{\pi g/8}+o(1))).  This is a genuine no-go for deriving factor
extension from local one-point data.  It is not an obstruction after a full
lower-exact factor has already been selected; the next theorem explains the
quantifier difference exactly.

## 2. The full factor has exact cut energy

For (A\subseteq\mathcal L), put

\[
 N(A)=\{X\in\mathcal O:\exists a\in A,\ a\subset X\},
 \qquad
 \delta(A)=|N(A)|-|A|,
\tag{2.1}
\]

and, for (e=XY\in E(F)), define

\[
 w_A(e)=\mathbf 1_{\{\ell(e)\notin A\}}
 \bigl(\mathbf 1_{\{X\in N(A)\}}+
       \mathbf 1_{\{Y\in N(A)\}}\bigr).
\tag{2.2}
\]

This is the same protected-transition test used in the optional-cut notes.

### Theorem 2.1 (factor-conditioned transition identity)

Every lower-exact spanning two-factor satisfies, for every
(A\subseteq\mathcal L),

\[
 \boxed{\sum_{e\in E(F)}w_A(e)=2\delta(A).}
\tag{2.3}
\]

#### Proof

Sum, over all factor edges, the incidences of endpoints lying in (N(A)).
Every owner has factor degree two, so the total is (2|N(A)|).  If
(\ell(e)\in A), both endpoints of (e) contain that lower colour and
hence lie in (N(A)).  Lower exactness says that there are exactly (|A|)
such edges, contributing (2|A|).  Removing precisely these incidences
leaves (2.3). \(\square\)

This is stronger than an orbit average: it holds for every literal factor
and every cut simultaneously.

Let

\[
 \sigma(A)=\sum_{X\in\mathcal O}\min\{2,a_X\}-2|A|,
 \qquad
 a_X=|\{a\in A:a\subset X\}|.
\tag{2.4}
\]

The exact shadow identity gives

\[
 (r-1)\sigma(A)=(r-2)\delta(A)+\beta(A),
 \qquad \beta(A)\ge0.
\tag{2.5}
\]

### Corollary 2.2 (factor-first fractional co-selection margin)

Let (P\subseteq E(F)) be random, under any law satisfying

\[
 \Pr(e\in P)\le p\qquad(e\in E(F)).
\tag{2.6}
\]

Then simultaneously for every fixed cut (A),

\[
 \boxed{
 \mathbb E\sum_{e\in P}w_A(e)
 \le 2p\delta(A)
 \le {2p(r-1)\over r-2}\sigma(A).}
\tag{2.7}
\]

Thus an edge-balanced law for a collar bank occupying
(p=O(h/r)=O(r^{-1/2})) of the factor has a uniform
(O(r^{-1/2})) fractional margin against every optional cut.  What remains
integral is the existence of the factor and of one physically spaced collar
selection; no separate middle-core Hall cut remains after that factor has
been chosen.

## 3. Exact upper-run fragmentation

Orient every component of (F).  For (H\in\mathcal H), let

\[
 m_H=|\{e\in E(F):u(e)=H\}|.
\tag{3.1}
\]

Assume in this section that (F) is upper-surjective, so (m_H\ge1).
Let (\rho_H) be the number of maximal nonempty (H)-runs on factor
components which are **not** monochromatic (H)-components.  A component
all of whose edge colours are (H) contributes zero to (\rho_H).
Let (v_H) be the number of owners at which the two incident factor edges
both have upper colour (H), and put (V=\sum_Hv_H).

### Theorem 3.1 (fragmentation identity)

\[
 \boxed{
 v_H=m_H-\rho_H,
 \qquad
 V=C-\Phi,
 \qquad
 \Phi:=\sum_{H\in\mathcal H}(\rho_H-1).}
\tag{3.2}
\]

If no factor component is monochromatic in one upper colour, then
(\Phi\ge0).

#### Proof

A run of (a) consecutive (H)-edges on a nonmonochromatic cyclic
component has (a-1) internal equal-colour junctions.  A monochromatic
component of (a) edges has (a) such junctions.  Summing gives
(v_H=m_H-\rho_H).  Since

\[
 \sum_Hm_H=W,
 \qquad
 |\mathcal H|=U,
 \qquad
 W-U=C,
\]

summing the first identity gives the second.  In the absence of a
monochromatic component, every represented upper colour has at least one
ordinary run, so (\rho_H\ge1). \(\square\)

Hence the scalar repeat ledger alone does not produce valleys.  It produces

\[
 \sum_H(m_H-1)=C,
\tag{3.3}
\]

whereas the literal valley count is (C-\Phi).  The missing quantity is the
signed run-fragmentation energy (\Phi).

At the level of colour words this distinction is sharp.  For (r\ge3),
(C\le U); take (C) symbols twice and every other symbol once, and
interleave the second copies so that no equal symbols are adjacent.  The
repeat surplus is (C), but (V=0).  This is only an arithmetic colour-word
example, not a claimed physical middle-level factor; it proves that no
argument using multiplicities alone can force even one upper valley.

## 4. Catalan repeat deletion is the exact forest normal form

Let (D\subseteq E(F)) and put (Q=F-D).

### Theorem 4.1 (repeat-deletion equivalence)

The following are equivalent.

1. (Q) is a spanning upper-exact linear forest with exactly (U) edges.
2. For every (H\in\mathcal H),

   \[
    |D\cap u^{-1}(H)|=m_H-1,
   \tag{4.1}
   \]

   and (D) meets every cycle component of (F).

Under either condition,

\[
 |D|=C,
 \qquad
 Q\text{ has exactly }C\text{ path components},
\tag{4.2}
\]

and its lower colours are automatically injective.

#### Proof

Condition (4.1) leaves exactly one edge of every upper colour, hence exactly
(U) edges.  Deleting at least one edge from every factor cycle makes the
remainder a spanning linear forest.  It therefore has (W-U=C) components.
Every retained lower colour is distinct because all lower colours were
distinct in (F).

Conversely, an upper-exact graph with (U) edges has exactly one edge of
each of the (U) upper colours, proving (4.1).  A subgraph of a disjoint
union of cycles is a forest exactly when at least one edge was deleted from
each cycle. \(\square\)

Thus a factor-first construction can be split, without loss, into

\[
 \boxed{
 \text{lower-exact factor }F
 \;\longrightarrow\;
 \text{Catalan repeat deletion }D
 \;\longrightarrow\;
 \text{upper-exact Catalan forest }Q.}
\tag{4.3}
\]

The desired valleys are precisely cap-two incidences between a deleted
repeat and the first retained edge of a component.

There is also an exact criterion for whether such a repeat deletion can
break every factor cycle at all.  Let `cal K(F)` be the component set of
`F`.  For a family `S subseteq cal K(F)`, let

\[
 R(S)=\{H\in\mathcal H:\text{some edge of a cycle in }S
                         \text{ has upper colour }H\}.
\tag{4.4}
\]

### Theorem 4.2 (cycle--surplus Hall criterion)

An upper-surjective lower-exact factor admits a set `D` satisfying
Theorem 4.1 if and only if

\[
 \boxed{
 |S|\le\sum_{H\in R(S)}(m_H-1)
 \qquad(S\subseteq\mathcal K(F)).}
\tag{4.5}
\]

#### Proof

Replace every upper colour `H` by `m_H-1` labelled deletion tokens and
join all of those tokens to every factor cycle containing an `H`-edge.
Hall's theorem gives a matching saturating the factor cycles exactly under
(4.5).  For every matched cycle, delete one occurrence of its matched
colour.  Distinct cycles give distinct edge occurrences, and no colour has
used more than `m_H-1` deletions.  For each `H`, add arbitrary further
`H`-occurrences until exactly `m_H-1` have been deleted.  At least one
`H`-occurrence remains, and every factor cycle was hit, so Theorem 4.1
applies.

Conversely, assign to every factor cycle one of its deleted edges.  A colour
`H` can receive at most `m_H-1` assignments.  The resulting capacitated
matching forces (4.5). \(\square\)

In particular, every factor cycle must contain a repeated upper colour and
`c(F)<=C`.  Upper surjectivity alone implies neither statement.  Thus even
before spacing and geodesicity, the factor-first route has one exact global
cycle-versus-repeat Hall gate.

## 5. The cap-two geodesic segmentation certificate

Orient every cycle of (F), and hence every component of (Q=F-D).  A
nontrivial component is written

\[
 K=(M_0,M_1,\ldots,M_\ell),
\tag{5.1}
\]

where the preceding deleted edge is (d_K=PM_0\in D).

Call (K) **cap-two at its entrance** when

\[
 u(PM_0)=u(M_0M_1).
\tag{5.2}
\]

Write

\[
 M_j=M_{j-1}-\{\lambda_j\}+\{\rho_j\}.
\tag{5.3}
\]

Call (K) an **outward Johnson geodesic** when

\[
 d_J(M_0,M_j)=j\qquad(0\le j\le\ell).
\tag{5.4}
\]

Then all (\lambda_j) are distinct members of (M_0), all (\rho_j)
are distinct members of ([n]-M_0), and the two lists are disjoint.  In
particular (\ell\le r-1).

Under (5.2), there is a unique
(q_-(K)\in M_0-\{\lambda_1\}) such that

\[
 P=M_0-\{q_-(K)\}+\{\rho_1\}.
\tag{5.5}
\]

For a fixed collar depth (h), call (K) **(h)-admissible** when

\[
 \ell\ge h+2,
 \qquad
 q_-(K)\notin\{\lambda_1,\ldots,\lambda_h\},
\tag{5.6}
\]

and (5.2)--(5.4) hold.

### Theorem 5.1 (all admissible components give disjoint collars)

Every (h)-admissible component supplies the generalized balanced collar

\[
 P,M_0,M_1,\ldots,M_h,M_{h+1}.
\tag{5.7}
\]

The collars supplied by all (h)-admissible components are pairwise
vertex-disjoint, and hence also disjoint in their lower-factor resources.

#### Proof

Equation (5.2) gives the balanced left seam (5.5).  Geodesicity gives the
two disjoint rails

\[
 \lambda_1,\ldots,\lambda_h,
 \qquad
 \rho_1,\ldots,\rho_h.
\]

Condition (5.6) leaves (q_-(K)) in the fixed core after the first (h)
deletions.  The next transition deletes
(q_+=\lambda_{h+1}) from that core and inserts the fresh label
(z=\rho_{h+1}).  These are exactly the generalized collar identities.

Different (Q)-components are vertex-disjoint.  The prefix
(M_0,\ldots,M_{h+1}) omits its own terminal vertex because
(\ell\ge h+2).  The extra owner (P) is the terminal vertex of the
preceding (Q)-component.  Such terminals are distinct, and if the
preceding component is itself selected, its terminal lies outside its
selected prefix.  Therefore the owner sets in (5.7) are pairwise disjoint.
Lower-resource disjointness follows from the lower-exact factor. \(\square\)

This theorem packages spacing automatically: collars live at entrances of
different Catalan forest components, rather than being chosen as overlapping
windows on an undifferentiated factor cycle.

## 6. Exact long-component count

Suppose every component of (Q) has at most (r-1) edges; this holds in
particular when every component is an outward Johnson geodesic.  Let (p)
be the number of components with at least (h+2) edges.  Since (Q) has
(C) components and (U) edges,

\[
 U\le p(r-1)+(C-p)(h+1).
\]

Hence

\[
 \boxed{
 p\ge
 {U-C(h+1)\over r-h-2}
 ={W(r-2h-3)\over(r+1)(r-h-2)}.}
\tag{6.1}
\]

The odd collar demand is

\[
 b={W\over2r-1}-1.
\tag{6.2}
\]

### Corollary 6.1 (bounded geodesic segmentation gives the full bank)

Assume

\[
 r^2-3rh-6r+3h+5\ge0.
\tag{6.3}
\]

If every component counted by (p) is (h)-admissible, then (F)
contains at least (b) pairwise resource-disjoint depth-(h) generalized
collars.

In particular, the simpler condition (r\ge4h+8) implies (6.3).

#### Proof

Condition (6.3) is exactly

\[
 (2r-1)(r-2h-3)\ge(r+1)(r-h-2).
\]

Together with (6.1), it gives

\[
 p\ge {W\over2r-1}=b+1.
\]

Apply Theorem 5.1 and retain any (b) collars.  Substitution of
(r=4h+8) in the left side of (6.3) gives
(4h^2+19h+21>0), and the expression increases thereafter. \(\square\)

At deadline scale (h=\Theta(\sqrt r)), (6.3) holds for all sufficiently
large (r).  Thus, once a cap-two outward-geodesic Catalan segmentation is
constructed, the Catalan arithmetic supplies more than the required number
of long components automatically.  No separate spacing theorem, protected
factor extension, or optional-core analysis remains.

## 7. The sharpened positive target

The strongest exact target exposed by this audit is now:

> **Cap-two geodesic Catalan segmentation.**  Construct an upper-surjective
> lower-exact spanning middle-level factor (F), together with a Catalan
> repeat deletion set (D), such that (Q=F-D) has outward-geodesic
> components and at least the long components guaranteed by (6.1) have
> cap-two, seam-clean entrances.

This target simultaneously supplies:

1. the complete owner/lower factor;
2. every immediate upper colour;
3. the exact Catalan repeat ledger;
4. physical spacing of the collars by forest components; and
5. collision-free rail residence inside each selected collar.

It is strictly stronger than the scalar “quarter of the repeats” statement,
but its extra strength is exactly what turns the scalar budget into literal
resource-disjoint depth-(h) collars.

## 8. Exact scope and self-audit

The note proves no all-(r) existence theorem for (F,D).  In particular:

1. upper-surjective lower-exact two-factor existence is still an integral
   correlated selection problem;
2. Theorem 3.1 shows that upper multiplicities alone do not localize their
   repeats;
3. Theorem 4.1 does not produce a repeat deletion set whose components are
   short or geodesic;
4. the component-length count does not force the cap-two entrance or the
   seam condition (q_-\notin\{\lambda_1,\ldots,\lambda_h\});
5. arbitrary-width upper witnesses and the terminal common cap remain
   outside this factor/q1 theorem.

The arithmetic checks used above are:

\[
 {2r-1\choose r+1}
 ={2r-1\choose r}{r-1\over r+1},
 \qquad
 C={2W\over r+1},
\tag{8.1}
\]

\[
 U-C(h+1)
 ={W\over r+1}(r-2h-3),
\tag{8.2}
\]

and

\[
 \begin{aligned}
 &(2r-1)(r-2h-3)-(r+1)(r-h-2)\\
 &\hspace{35mm}=r^2-3rh-6r+3h+5.
 \end{aligned}
\tag{8.3}
\]

All uses of “geodesic” are prefix-geodesic from the displayed entrance, not
merely “simple path.”  All uses of “resource-disjoint” in Theorem 5.1 refer
to owner and lower-factor resources; distinct upper targets are already
globally witnessed by (F), but upper occurrences of different collars are
not asserted disjoint.  This matches the exact scope of the factor-first
reduction.
