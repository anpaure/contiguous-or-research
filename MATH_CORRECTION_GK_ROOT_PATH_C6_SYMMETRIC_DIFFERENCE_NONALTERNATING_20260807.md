# Root-path `C_6` fusion is a simple cycle, but not an alternating switch

**Date:** 2026-08-07  
**Method:** literal edge-status audit; no computation or search  
**Status:** unconditional correction.  The Catalan-rotor matching and its
abstract component-disjointness remain valid, but the existing paired-root
`C_6` circuits do not by themselves give the claimed degree-two physical
rethread along a root path of length at least two.

## 1. The local status at a shared root

For an edge `e=UV` of the Greene--Kleitman root-rotation graph, the
paired-root hinge circuit `C_e` is an alternating incidence `C_6`.  At the
endpoint root `U`, it contains

\[
 f_U=X_Ut(X_U),
\]

which is selected in the fixed Greene--Kleitman matching, and one cross
edge incident with `X_U`, which is unselected.  Distinct root-rotation
edges incident with `U` have the same fixed edge `f_U` and distinct cross
edges.

Let `e_1=VU` and `e_2=UW` be two consecutive edges of a simple root path.
The circuits `C_{e_1}` and `C_{e_2}` meet exactly in `f_U`.  Their symmetric
difference deletes `f_U` and retains the two distinct cross edges at
`X_U`.  Both retained edges have status zero in the initial factor.
Therefore the fused cycle has the local status pair

\[
                         0,0
\]

at `X_U` and is not alternating.

## Theorem 1.1 (sharp alternation boundary)

Let

\[
 U_0e_1U_1e_2\cdots e_rU_r
\]

be a simple path in the root-rotation graph, and put

\[
 C(P)=\mathop{\triangle}_{i=1}^r C_{e_i}.
\]

Then `C(P)` is the simple incidence cycle of length `4r+2` proved in the
root-path fusion theorem.  Relative to the fixed Greene--Kleitman factor,
it is alternating if and only if `r=1`.

### Proof

For `r=1`, `C(P)` is the original alternating `C_6`.

For `r>=2`, every internal root `U_i` is incident in `C(P)` with the two
cross edges supplied by `C_{e_i}` and `C_{e_{i+1}}`; the common selected
edge `f_{U_i}` cancels.  Both cross edges were unselected in the initial
factor, so two consecutive edges of `C(P)` have equal status.  Hence
`C(P)` is not alternating.  \(\square\)

There is a dual formulation after toggling both endpoint circuits against
a complementary reference factor: the two surviving edges at every
internal root have the same status again.  The obstruction is equality of
the phases, not the convention assigning zero or one to the fixed edge.

## 2. Sequential toggling does not repair the problem

The two `C_6`s cannot simply be toggled one after the other.  Initially
both are alternating and share the selected edge `f_U`.  Toggling either
one flips `f_U` while leaving the other two fixed-matching edges of the
second circuit unchanged.  The second circuit then has two fixed edges of
one status and its shared fixed edge of the opposite status, so it is not
alternating.  Reversing the order gives the same obstruction.

Thus neither simultaneous symmetric difference nor serial application is
a valid factor switch through an internal root.

## 3. Consequences for the current theorem chain

The following conclusions remain correct:

1. the Catalan rotor is a bijection and gives the stated optimal abstract
   depth-two path cover;
2. the ordinary escape roots `W_D` lie in components distinct from the
   components starting at `U_D`;
3. those source and destination component banks are pairwise disjoint;
4. the corresponding root edges form a valid abstract component matching.

The following physical conclusions do **not** follow from the present
paired-`C_6` theorem:

1. that the forced edge `U_DV_D` together with the escape edge `U_DW_D`
   gives a literal degree-two rethread through `U_D`;
2. that the four-`C_6` helper-path symmetric difference is an alternating
   length-18 switch; or
3. that an arbitrary root path can be fused into one alternating
   incidence switch.

In particular, the word **alternating** in Corollary 3.1 of
`MATH_THEOREM_GK_INTERNAL_CLOSE_FOUR_C6_HELPER_PATH_20260807.md` is false
under the stated fixed-factor phases, and the physical inference in
`MATH_THEOREM_GK_CATALAN_ROTOR_EXTERNAL_ESCAPE_AND_STRICT_QUARTER_20260807.md`
requires an additional lemma.

## 4. Exact replacement gate

A valid physical lift of an abstract root path needs one of:

1. a phase-repair circuit at every internal root that changes one of the
   two cross-edge phases without changing the protected palettes;
2. a higher alternating circuit whose literal edge set is not the bare
   symmetric difference of the endpoint `C_6`s; or
3. a second factor phase in which consecutive root edges use opposite
   fixed-edge conventions.

The smallest unresolved local case is already a length-two root path.  It
asks for a literal alternating rethread realizing two incident
root-rotation edges while retaining degree two at their common root.  Any
all-parameter fusion theorem must first close this case.

