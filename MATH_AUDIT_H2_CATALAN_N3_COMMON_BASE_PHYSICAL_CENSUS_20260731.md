# Every common basis is not physically equivalent at (n=3)

Date: 2026-07-31  
Status: complete finite census for one authenticated child forest; exact
separation of incidence, side-anchor capacity, and contracted topology; no
all-(n) claim

## 0. Verdict

The automatic common-basis theorem cannot be followed by an arbitrary
choice of common basis.  Even at the first integral collar parameter, the
physical rows distinguish the bases.

Fix the literal (n=3) child Catalan forest used by the positive
two-coordinate fixture.  It has (15) edges in five paths.  Here

\[
 P=6,\qquad C=14,\qquad R=1.
\]

Thus every candidate deletion bank (Q) retains exactly one of the fifteen
child edges.  All fifteen choices are common incidence bases: both
punctured sides have at least one exact containment bijection.  Nevertheless
only ten admit two anchor-capped side forests with acyclic contracted
attachment graph.

The five failures split exactly as follows.

* Retaining (42\!\to14) or (11\!\to7), the plus shore has respectively
  (16) or (14) incidence bijections but none respects the seam-anchor
  degree cap.
* Retaining (37\!\to35), (56\!\to25), or (44\!\to41), both shores
  have anchor-capped side forests, but every pair has a contracted cycle.
  The minimum possible cycle ranks are respectively (2,2,1).

Hence synchronized incidence, separate physical forests, anchor capacity,
and the partial-involution/contracted-Γ row are genuinely successive
conditions.  A recursive proof must choose (Q) jointly with the two side
signatures.

## 1. Complete search space

The child paths are

```text
19-49
13-28
37-35-42-14-22-50-56-25-11-7-21-52-44-41
38
26.
```

Their intersections and unions are each bijective on the fifteen outer
colours, so this is a literal Catalan path forest.  For each retained edge:

1. the other fourteen edges define (Q), its inherited tail/head punctures,
   and the two fourteen-element anchor banks;
2. each side has six domain and six codomain resources, so all (6!=720)
   bijections are enumerated;
3. every bijection is checked for Boolean containment, physical degree,
   anchor degree and side acyclicity;
4. surviving matchings are quotiented only by their literal anchor-component
   partition; and
5. every minus/plus signature pair is tested in the contracted graph
   Γ, with loops and parallel pairs counted as cycles.

This is an exhaustive enumeration, not a sampled solver run.

## 2. Exact census

All fifteen (Q)'s pass both incidence rows.  Ten pass the complete physical
row.  Across them there are exactly (33) acyclic pairs of contracted side
signatures.  Every successful (Q) has at least one realization with

\[
 c_0^-=c_0^+=0,
 \qquad c_2^-=c_2^+=K=5,
\]

although the two shores need not use the same anchor pairs.  No successful
signature uses the tempting common matching of direct consecutive child
anchors; the direct edge is punctured out, as proved in the anchor-pairing
theorem.

The two capacity failures are not incidence failures: their raw plus-side
matching counts are positive.  Likewise, the three topology failures are
not failures of either side separately.  This gives literal finite
counterexamples to both shortcuts

```text
common incidence basis  => anchor-capped side representatives,

two anchor-capped side representatives => acyclic contracted Gamma.
```

## 3. Relation to the all-(n) target

The common-basis theorem guarantees that the incidence face is nonempty
for every (n\ge4).  This census shows what that theorem does not control:
the physical feasibility depends on which point of the common-basis face is
chosen.  The exact topology state from
`MATH_THEOREM_H2_CATALAN_ANCHOR_PAIRING_CONTRACTION_AND_PHYSICAL_ROW_20260731.md`
is therefore necessary, not bookkeeping overhead.

The census does not prove that every child forest has a physically good
basis, nor does it obstruct selecting one good basis.  Indeed this fixture
has ten.  The all-(n) task remains to prove existence of at least one
jointly good (Q), two label-saturating side forests, and an acyclic union
of their induced partial involutions.

## 4. Artifact

The independent verifier is

```text
scratch/audit_h2_catalan_two_coordinate_n3_all_common_bases_physical_20260731.py
```

and its retained output is

```text
scratch/h2_catalan_two_coordinate_n3_all_common_bases_physical_20260731.audit.json.
```

It authenticates the literal child palettes, enumerates the full search
space above, and stores one witness for every surviving signature.  No
claim is made for another child forest or (n\ge4).
