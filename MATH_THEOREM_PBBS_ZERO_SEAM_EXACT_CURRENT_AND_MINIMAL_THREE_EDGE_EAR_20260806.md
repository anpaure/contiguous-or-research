# The PBBS adjacent-height zero seam has a minimal three-edge repair ear

**Date:** 2026-08-06  
**Method:** literal monotone-height set algebra; no computation or search  
**Status:** unconditional owner-graph theorem.  It identifies the exact
upper value changed at every adjacent-height zero seam and constructs the
shortest simple Johnson detour whose total union restores that old value.
It does not prove that the detour is an alternating exchange in the fixed
PBBS two-factor; that physical lift remains the next gate.

## 1. The monotone height spine

On `[2r+1]={0,1,...,2r}`, put

\[
 A_h=0\,1^h0^h(10)^{r-h},
 \qquad U_h=[2r+1]\setminus A_h.
 \tag{1.1}
\]

For `h>=2`, direct comparison of the two binary words gives

\[
 A_h=A_{h-1}-\{2h-1\}+\{h\},
\]

and therefore

\[
 \boxed{U_{h-1}=U_h-\{2h-1\}+\{h\}.}
 \tag{1.2}
\]

Thus the named PBBS height connector is the Johnson spine

\[
 U_2,U_3,\ldots,U_H.
\]

The adjacent-pentagon identity is

\[
 P_{h,0}=U_h=Q_{h-1,1}.
 \tag{1.3}
\]

Hence the old factor has a zero-length intercut arc at `U_h`, whereas the
simultaneous head rethread installs the two spine edges incident with
`U_h`.

## 2. Exact old and new three-owner values

At the zero seam `U_h`, the old local three-owner segment is

\[
 P_{h-1,1},\ U_h,\ Q_{h,0}.
 \tag{2.1}
\]

The common-deletion identity at the left cut gives

\[
 P_{h-1,1}\cup U_h
 =U_{h-1}\cup U_h
 =U_h\cup\{h\}.
 \tag{2.2}
\]

Moreover the explicit first head is

\[
 Q_{h,0}=U_h-\{h+1\}+\{1\}.
 \tag{2.3}
\]

Therefore the old local target is

\[
 \boxed{Y_h^{\rm old}=U_h\cup\{1,h\}.}
 \tag{2.4}
\]

The new local spine segment is

\[
 U_{h-1},\ U_h,\ U_{h+1}.
\]

Using (1.2) at heights `h` and `h+1` gives

\[
 \boxed{Y_h^{\rm new}=U_h\cup\{h,2h+1\}.}
 \tag{2.5}
\]

Thus the zero-seam current is the literal one-coordinate exchange

\[
                         1\longleftrightarrow2h+1.
 \tag{2.6}
\]

This also explains why merely unioning the two separate `q1` identities
does not prove two-cut transparency: the old outgoing edge at `U_h` is not
the old edge whose upper colour is transported onto the new spine edge.

## 3. A three-edge repair inside the old target

Choose

\[
 x\in U_h\setminus\{2h-1\}.
 \tag{3.1}
\]

Define two rank-`r+1` owners

\[
 \begin{aligned}
 V_1&=U_h-\{2h-1,x\}+\{h,1\},\\
 V_2&=U_h-\{x\}+\{1\}.
 \end{aligned}
 \tag{3.2}
\]

### Theorem 3.1 (minimal repair ear)

The sequence

\[
 \boxed{U_{h-1},\ V_1,\ V_2,\ U_h}
 \tag{3.3}
\]

is a simple three-edge Johnson path.  Its three rank-`r` lower colours are

\[
 \begin{aligned}
 I_1&=U_h-\{2h-1,x\}+\{h\},\\
 I_2&=U_h-\{2h-1,x\}+\{1\},\\
 I_3&=U_h-\{x\},
 \end{aligned}
 \tag{3.4}
\]

and are pairwise distinct.  The complete owner union of the ear is exactly
the lost old value:

\[
 \boxed{U_{h-1}\cup V_1\cup V_2\cup U_h
       =U_h\cup\{1,h\}=Y_h^{\rm old}.}
 \tag{3.5}
\]

#### Proof

Equation (1.2) shows that the first transition in (3.3) exchanges `x` for
`1`.  The second exchanges `h` for `2h-1`, and the third exchanges `1` for
`x`.  Hence all three are Johnson edges.  The owners are distinct by their
members among `{1,h,2h-1,x}`.  Their intersections are exactly (3.4):
`I_1` contains `h`, `I_2` contains `1`, and `I_3` contains `2h-1`, while
the other two distinguishing labels are absent in each case.  Thus the
lower colours are distinct.  Every owner is contained in
`U_h union {1,h}`, and the two endpoints together with the interior owners
supply both extra labels.  This proves (3.5).  \(\square\)

### Proposition 3.2 (two-edge target repair is impossible)

There is no two-edge Johnson path

\[
                         U_{h-1},V,U_h
\]

whose two lower colours are distinct and whose complete owner union is
`Y_h^old`.

#### Proof

The endpoints are adjacent and have common rank-`r` facet

\[
                         I=U_{h-1}\cap U_h.
\]

Write

\[
 U_{h-1}=I\cup\{h\},\qquad U_h=I\cup\{2h-1\}.
\]

A common Johnson neighbour has one of two forms.  If it contains `I`, then
`V=I union {c}`.  The endpoints do not contain `1`, so obtaining the target
union `Y_h^old` forces `c=1`; both lower intersections are then `I`, and
the incidence walk repeats its lower vertex.

If `V` does not contain `I`, adjacency to both endpoints forces

\[
 V=(I\setminus\{y\})\cup\{h,2h-1\}
\]

for some `y in I`.  This gives distinct lower colours, but no owner in the
two-edge path contains `1`; its union is not `Y_h^old`.  These are all
possibilities.  \(\square\)

Thus three owner edges are the sharp local aperture for a simple repair.

## 4. Physical lifting gate

The ear (3.3) is an owner-graph path, not yet a legal local modification of
the fixed PBBS factor.  Replacing the direct connector edge by (3.3) also
uses the two new owners `V_1,V_2` and the three new lower colours in (3.4),
all of which already have incidences elsewhere in the spanning factor.

The exact next lemma is therefore:

> **Alternating three-ear lift.**  Choose `x` (or a bounded companion
> packet around it) so that the symmetric difference between the PBBS
> factor and all ears (3.3) is a disjoint or serially applicable family of
> alternating circuits, while preserving the common-history/source and
> typed-cap interfaces.

If such lifts exist at all high seams, the direct zero-length spine edges
can be replaced by positive-length paths which literally recreate every
target (2.4).  Longer synchronized collars may then be attached without
the degree-three overlap found for independent role-zero collars.

Nothing in Theorem 3.1 proves this alternating lift, component control, or
arbitrary-width exterior transparency beyond the displayed local target.

## 5. Dependencies

* `MATH_THEOREM_PBBS_AH_LADDER_PENTAGON_RETURN_20260805.md`;
* `MATH_THEOREM_PBBS_PENTAGON_THREE_SCREEN_COMMON_HISTORY_AND_UPPER_CURRENT_GATE_20260805.md`;
* `MATH_THEOREM_PBBS_SYNCHRONIZED_INCOMING_COLLAR_CANCELS_COMPLETE_UPPER_CURRENT_20260805.md`;
* `MATH_AUDIT_PBBS_SYNCHRONIZED_COLLAR_AND_POLYNOMIAL_EXTENSION_20260806.md`.
