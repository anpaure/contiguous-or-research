# Independent audit of the prospective GMN coloured pull-tree theorem

Date: 2026-08-01  
Audited file:
`MATH_THEOREM_R_PROSPECTIVE_GMN_COLORED_PULL_TREE_AND_LEXICAL_UPPER_OBSTRUCTION_20260801.md`  
Method: independent symbolic proof audit; no finite search.

## Verdict

The theorem is **VALID WITH ITS STATED CONSTRUCTION-SPECIFIC SCOPE**.
The following points are load-bearing.

## 1. Parameter and arithmetic audit

The owner middle-levels graph on ranks `m-1,m` of `[2m-1]` is the lexical
graph with parameter `r=m-1`.  Hence

\[
 W_r=\binom{2m-1}{m-1},
\]

and a lexical opposite triple has rank `r+2=m+1`, exactly the immediate
upper owner rank.

The imported exact missing-colour count is

\[
 M_r=W_r\frac{(r-2)(r-3)}{2(r+2)(2r-1)}.
\]

One alternating incidence hexagon changes the selected incident pair at
only its three lower vertices, so it changes at most three turn-map values.
This is an adaptive telescoping bound and does not require disjoint turn
supports.  A canonical pull spanning tree has

\[
 s=p_r-1\le\operatorname {Cat}_r-1.
\]

Consequently the residual target-hole bound is

\[
 M_r-3(\operatorname {Cat}_r-1)
 =\frac{W_r(2r^3-21r^2-11r+18)}
        {2(r+2)(2r-1)(2r+1)}+3.
\]

At `r=11`, `M_11=178296`, `Cat_11=58786`, and the residual is `1941`.
The cubic numerator is `18` there and is increasing for `r>=11`; at `r=10`
the residual is `-7069`.  Thus `r=11`, equivalently `m=12`, is the first
threshold proved by this bound.

Opening a Hamilton cycle by deletion cannot create a new lower turn, so the
hole lower bound survives.  A new endpoint connector is a new edit and must
be charged separately.

## 2. Auxiliary-tree audit

Canonical pull hexagons are edge-disjoint.  Therefore every physical
incidence has either its baseline value or one affine toggle variable, and
the incidence formula in the theorem is exact.  The labelled graphic rows

\[
 y(E)=p_r-1,
 \qquad y(E(S))\le |S|-1
\]

are exactly the spanning-tree polytope on binary labels, including loops
and parallel two-cycles.  With forced labels `A` and forbidden labels `Z`,
extension is equivalent to `A` being a forest and `(H_r-Z)/A` being
connected.

This protects edges only.  A full pivot boundary state must impose every
incidence in its footprint because a different pull may share a boundary
vertex.

## 3. Upper-state audit

Upper colour belongs to the unordered pair of final incidences at a lower
turn, not to an auxiliary pull label.  Two edge-disjoint pulls may use the
two different old factor edges at the same lower vertex.  The pair-state
variables in the theorem are therefore exact and necessary.

For two such labels, a static additive signed delta requires vanishing mixed
difference

\[
 [\kappa_{gh}]-[\kappa_g]-[\kappa_h]+[\kappa_0]=0.
\]

The generic four-colour rectangle makes this vector nonzero.  Thus no
context-free upper-colour flow on uncoloured GMN labels follows from
edge-disjointness.

## 4. Prospective owner-flow audit

The exact live quantifier is joint over `(M_0,Q_0,J)`:

* `M_0` contains the pivot predecessor shore;
* `Q_0` contains the successor shore and one occurrence of every upper
  colour, with tail/head/graphic independence and the pivot root first;
* `J` matches free component ports and joins the `Cat_m` components.

Given an acyclic component reservoir, deleting the pivot component's
incoming copy and applying ordinary Hall is necessary and sufficient for a
path rooted at that component.  Acyclicity is essential: without it, a
size-`C-1` port matching can contain a disjoint directed cycle.

The graphic--Rado theorem in the main note is valid only under hereditary
private-witness safety.  It is a sufficient face, not an exact description
of shared-turn GMN pulls.

## 5. Scope corrections retained

1. The arbitrary-`M_0` correlated pivot theorem does not plant the pivot in
   the fixed lexical factor.  A positive pull implementation must construct
   one common factor decomposition.
2. The `m=3` protected-owner counterexample has lexical parameter `r=2` and
   is logically separate from the `r>=3` lexical defect formula.
3. The no-go applies to the canonical `0/1` lexical GMN pull-tree family,
   not to PBBS, an arbitrary Middle-Levels Hamilton cycle, or noncanonical
   long packets.
4. Cross-boundary physical OR intervals can in principle provide masks
   absent from the projected turn map.  They are outside the theorem and
   require explicit address/provenance accounting.
5. Residence, deeper shadows, common cap, compiler matching, and
   regeneration remain unproved.

No unsupported implication from arbitrary protected tickets, marginal
graphic extendibility, or a per-pull signed colour vector remains in the
audited theorem.
