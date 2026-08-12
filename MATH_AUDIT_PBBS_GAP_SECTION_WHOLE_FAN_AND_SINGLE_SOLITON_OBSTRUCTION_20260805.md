# Audit of the PBBS whole-fan gap section and protected-opening reduction

**Date:** 2026-08-05  
**Audited file:**
`MATH_THEOREM_PBBS_GAP_SECTION_WHOLE_FAN_AND_PROTECTED_OPENING_REDUCTION_20260805.md`  
**Method:** independent symbolic replay; no computation or search  
**Verdict:** **GO**, with the protected-Hamiltonization conclusion retained
only as a reduction and with the wholly selected single-soliton obstruction
made explicit.

## 1. Survivor identities

For the global corridor of a rank-`(m-q)` target, at step `t` put

\[
                         r=q-t-1.
\]

The imported clean-label deletion calculation gives exactly

\[
 U_+(K_t)=\{A_t,A_{t+1},A_{t+2}\},
 \qquad
 U_-(K_t)=\{C_r,C_{r+1},C_{r+2}\}.
\]

It also identifies `A_t` as the strict cyclic predecessor of `C_r` among
the retained forward marks.  Thus the proposed selected boundary is the
literal PBBS edge

\[
                         K_t+C_r\longrightarrow K_t+A_t.
\]

No new survivor assertion is being imported implicitly.

## 2. Gap order for `q>=3`

The reverse corridor inequality says that moving backward from `A_0` to
`A_h` crosses at most `h` reverse marks.  Hence `A_h` occurs no earlier
than the open gap following

\[
                         C_{2q-h}.
\]

For the earliest possible survivor `A_(t+2)`, compare this index with the
third retained reverse mark:

\[
 [2q-(t+2)]-[r+2]=q-3.
\]

It is nonnegative for `q>=3`.  Therefore no retained forward mark lies in
either of the first two open gaps after `C_r`.  Equality at a shared
coordinate is harmless because the expansion is `C,A`, placing the
forward mark after the endpoint `C_(r+2)`.

The induced gap counts are consequently

\[
                         (0,0,3),
\]

and the potential values away from `C_r` are `-1,-2`.  Thus `C_r` is the
unique maximum.

## 3. Boundary depths

At `q=2,t=0`, the statement is exactly the previously audited entrance
restriction: survivors

\[
 A_0,A_1,A_2;qquad C_1,C_2,C_3
\]

have zero forward marks in the first gap and at most one in the second.

At `q=2,t=1`, the survivors are

\[
 A_1,A_2,A_3;qquad C_0,C_1,C_2.
\]

The inequalities `y_h<=h` put none in the first gap and at most `A_3` in
the second.  Again the two nonbase potential values are `-1` and at most
`-1`.  This edge is uniquely selected.  The `q=1` edge is the definition
of the section.

Hence every edge of every declared corridor is selected independently of
all tie choices elsewhere.

## 4. Protected transport

If a degree-two spanning factor retains all selected section edges, it
retains every selected corridor literally.  At an internal corridor vertex
the two corridor edges already exhaust degree two, so another factor edge
cannot be interposed.  The intersection target is unchanged, and De Morgan
gives the complementary upper union on the same retained path.

This verifies the protected transport theorem.  It does not assert that
such a Hamilton factor exists.

The alternative deleted-edge condition is also exact.  An old interval
survives iff none of its internal edges is deleted.  A target survives iff
one of its occurrence intervals survives.  Since an exact interval has one
set value, choices for distinct upper targets have no shared-cell capacity
constraint; this is a targetwise transversal avoidance condition, not a
Hall matching.

## 5. All-unit bank freedom

The separately audited all-unit calculation proves that every outgoing
edge of its PBBS component is outside the gap section.  A selected corridor
starts with a section edge and remains in that edge's PBBS component.
Therefore no selected corridor can enter the all-unit component.  The
complete lower and complementary upper named banks are disjoint from it,
and the `m-1` quiet suffix is a literal free reserve.

## 6. Single-soliton obstruction replay

For

\[
                         A=0_r1^m0^m,
\]

let `p` be the final up-step and `v_1,...,v_m` the subsequent down-steps.
For `K=A-{p}`, forward and reverse cancellation leave

\[
 U_+(K)=\{r,v_{m-1},v_m\},
 \qquad
 U_-(K)=\{p,v_1,v_2\}.
\]

For `m>=3`, the expanded gap counts from `C_p` are `(0,0,3)`.  At `m=2`,
the two shared down-step coordinates give `(0,1,2)` under the fixed `C,A`
order.  In both cases `C_p` is the unique potential maximum and `A_r` is
its last preceding forward mark.  Thus the outgoing edge `K+p -> K+r` is
selected.  Root rotation proves the complete component is selected.

It follows immediately that a rethread deleting only unselected old edges
cannot touch this component.  The unselected native-C6 component
hypergraph is therefore nonspanning.  This is a real obstruction, not a
failure of the proof method.

## 7. Final scope

The audit validates:

1. the whole-fan strengthening;
2. simultaneous lower/complementary-upper protected transport;
3. the targetwise forbidden-cut formulation;
4. the all-unit quiet reserve; and
5. the wholly selected single-soliton obstruction.

It does not validate:

1. a Hamilton cycle retaining the full section (which the obstruction
   actually forbids);
2. a selected-edge puncture/rerouting theorem;
3. source residence or common-cap transport; or
4. an unconditional `B(k)` or `B(k)+O(1)` construction.

