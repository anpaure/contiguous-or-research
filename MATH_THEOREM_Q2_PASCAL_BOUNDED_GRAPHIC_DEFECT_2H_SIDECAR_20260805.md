# A bounded graphic defect costs at most `2h` in the q2 Pascal lift

**Date:** 2026-08-05  
**Method:** explicit componentwise puncture, one-edge Z repair, and canonical
endpoint accounting; no computation or search  
**Status:** unconditional bounded-defect q2-Pascal theorem.  If a
q2-complete one-occurrence section leaves `h` factor cycles wholly selected,
the Pascal construction has an explicit path-forest realization with `h`
extra owner occurrences and at most `h` missing q2 masks.  Thus the total
literal/owner sidecar at this interface is at most `2h`.

## 1. Setup and punctures

Use the notation of the q2 Pascal two-factor lift.  Thus

\[
 P={2r-1\choose r-1},\qquad
 Q={2r-1\choose r-2},\qquad
 \kappa=P-Q=\operatorname{Cat}_r,
\tag{1.1}
\]

and each factor component is written cyclically as

\[
 X_0,U_0,X_1,U_1,\ldots,qquad
 Y_i=X_{i-1}\cap X_i.
\tag{1.2}
\]

Let `S` choose exactly one occurrence of every q1 colour `Y` and suppose
that it is q2-complete: every rank-`(r-3)` target occurs as
`Y_i cap Y_(i+1)` at a selected-selected adjacency.

Assume exactly `h` factor cycles are wholly selected.  On each such cycle
choose one position `p` and put

\[
                         S^\circ=S-\{p:\ p\text{ chosen}\}.
\tag{1.3}
\]

Now every factor cycle has an omitted position, while

\[
                         |S^\circ|=Q-h.
\tag{1.4}
\]

Removing `p` can destroy only the two selected adjacencies
`(p-1,p)` and `(p,p+1)`.  Thus the raw q2 loss is at most `2h`.

## 2. The punctured Pascal forest

Apply the componentwise A-sector run surgery to `S^circ`.  There are
`kappa+h` omitted turn positions, so

\[
 \#\operatorname{comp}(F_A)=\kappa+h,qquad
 |E(F_A)|=Q-h.
\tag{2.1}
\]

In the Z-sector, retain the vertex `z+Y_p` for every punctured q1 colour as
an isolated vertex.  If `s` is the number of nonempty selected runs, then

\[
 \#\operatorname{comp}(F_Z)=s+h,qquad
 |E(F_Z)|=Q-h-s.
\tag{2.2}
\]

Add the usual `s` A/Z cross edges.  Before the extra repair below, the
combined graph is a spanning linear forest with

\[
 \kappa+2h\text{ components and }2Q-2h\text{ edges}.
\tag{2.3}
\]

For a puncture `p`, its omitted run has length one.  Locally the usual
surgery deletes the A-edge indexed by `p` and adds

\[
                         X_p--(z+Y_{p+1}).
\tag{2.4}
\]

The selected Z-run has endpoints `z+Y_(p+1)` and `z+Y_(p-1)`, while
`z+Y_p` is isolated.  Add the one repair edge

\[
                         (z+Y_{p-1})--(z+Y_p).
\tag{2.5}
\]

It attaches the isolated vertex to a path endpoint, so it preserves
linearity and acyclicity.  Its union colour is

\[
 z+(Y_{p-1}\cup Y_p)=z+X_{p-1}.
\tag{2.6}
\]

This colour was unused: the corresponding selected-selected Z edge was
destroyed by the puncture, and `p-1` is not an omitted-run terminal, so no
cross edge uses it.  Distinct punctures have distinct `X_(p-1)` states.

After adding (2.5) for all punctures, the forest `F^star` has

\[
 \boxed{
 \#\operatorname{comp}(F^\star)=\kappa+h,qquad
 |E(F^\star)|=2Q-h.}
\tag{2.7}

## 3. Exact intersection defect

Every no-`z` q1 target is still covered.  For a singleton omitted run,
the A-surgery retains the occurrence at `p`, while the cross edge (2.4)
restores the following selected occurrence.  Thus puncturing the section
does not create a no-`z` q1 hole in the final forest.

The repair edge (2.5) restores the z-containing q2 target

\[
                         z+(Y_{p-1}\cap Y_p).
\tag{3.1}

Only the other local adjacency can remain lost:

\[
                         z+(Y_p\cap Y_{p+1}).
\tag{3.2}

It may already have another selected witness elsewhere.  Consequently the
actual missing q2 set `H_2` satisfies

\[
                         |\mathcal H_2|\le h.
\tag{3.3}

All rank-`r` edge-union colours of `F^star` are distinct by the original
Pascal palette proof and (2.6).

## 4. Endpoint completion with exactly one repeat per puncture

For every unpunctured omitted run use the canonical endpoint assignment.
For a puncture `p`, before adding (2.5) the canonical assignment uses

\[
 z+X_{p-1}\quad\text{at }z+Y_{p-1},
 \qquad
 U_p\quad\text{at }X_{p+1}.
\tag{4.1}

After (2.5), the first colour in (4.1) is its edge union and those two old
endpoint roles disappear.  The local path endpoints are now

\[
                         z+Y_p,qquad X_{p+1}.
\]

Keep the assignment `X_(p+1) -> U_p`, and assign `z+Y_p` to one additional
occurrence of

\[
                         z+X_p.
\tag{4.2}

This is a literal containment because `Y_p subset X_p`.  The owner
`z+X_p` is already the union colour of the cross edge (2.4), so (4.2)
creates exactly one repeated rank-`r` owner occurrence.

Globally, `F^star` has `2kappa+2h` endpoint roles.  It uses `2Q-h`
distinct edge unions, leaving

\[
 2P-(2Q-h)=2\kappa+h
\]

distinct rank-`r` owners.  The canonical assignments use all of them and
(4.2) supplies exactly the remaining `h` endpoint roles.  Thus the count
and the literal containment construction agree exactly:

\[
 \boxed{\text{endpoint-owner repeat excess}=h.}
\tag{4.3}

## 5. Bounded-defect theorem

### Theorem 5.1

From a q2-complete q1 section with `h` wholly selected factor cycles one can
construct a spanning Pascal linear forest satisfying:

1. every no-`z` q1 intersection target is covered;
2. at most `h` z-containing q2 targets are missing;
3. all edge-union colours are distinct;
4. every endpoint has a containing owner assignment; and
5. every rank-`r` owner is used once except for exactly `h` explicitly
   named repeated occurrences.

Appending one literal occurrence of every member of `H_2` repairs the q2
palette.  Therefore the complete sidecar at the q2/owner interface has
size

\[
 \boxed{h+|\mathcal H_2|\le2h.}
\tag{5.1}

In particular, proving that the max-height PBBS section has only `O(1)`
wholly selected components is already sufficient for an `O(1)`-defect
q2 Pascal lift; exact cycle-hit is stronger than necessary for the
additive-constant programme.

## 6. Scope

The theorem gives an exact bounded-defect Pascal path system and literal
sidecar.  A downstream regenerative construction must accept the `h`
named repeated endpoint owners and the at most `h` literal q2 repairs.
The theorem does not by itself prove residence, arbitrary-width upper
coverage, or a common-cap compiler for those sidecar occurrences.

