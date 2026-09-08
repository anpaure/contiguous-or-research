# A double-factor affine solution of the parity complete-mapping equations

Date: 2026-07-26

> **Trace audit.**  The ownership theorem below is correct, but the `Q_4`
> seed is not a positive tagged-code seed.  Its exact aligned tagged-code
> multiplicities at completed-pair depths `d=1,2,3,4` are respectively
> `1,2,8,128`; see
> `MATH_AUDIT_DOUBLE_FACTOR_AFFINE_PARITY_COMPLETE_MAPPING_20260726.md`.
> Thus context dependence alone does not reduce even the tagged parity
> collision.  Forgetting `J` can only merge these fibres.
> Also, the eight even contexts index only two distinct coarse factors,
> each with multiplicity four.
>
> **Later correction.**  The originally proposed crossed child is false:
> it compares direction fields at different child owners.  The
> shorewise-translation witness in
> `MATH_THEOREM_CROSSED_COLUMN_WITNESS_REPAIR_20260726.md` repairs column
> exactness and restores the late-cross augmented-code theorem.  Literal
> lower/upper targets still need an independent decoder for the support
> `J`; augmented injectivity alone is not literal trace injectivity.

## 0. Outcome

The pointwise ownership equations in
`MATH_THEOREM_PARITY_COMPLETE_MAPPING_PAIRED_ORDER_LIFT_20260726.md`
have a nonconstant algebraic solution whenever one has two neighbour
permutations whose directions are related by a coordinate permutation at
the same vertex.

This converts the common-phase `Q_4` braid into a literal context-dependent
pair-clustered factor on `Q_8`.  It is the first solution of the exact
complete-mapping equation in which the coarse successor depends on the
parity context.  Subsequent audit shows that the literal affine-lift
recursion, direct tensors, and the homogeneous parallel or fully crossed
product recursions are not near-injective.  The naive crossed product is
itself false, but a controlled-column replacement repairs it.  Cross once
with that witness and then recurse in parallel: its forward and reverse
**tagged** codes `(J,p_out,x_out)` are exactly injective through coarse
depth `R/8`, hence throughout the Gaussian range.  A raw lower or upper
OR target does not determine `J`, so literal target injectivity remains
open.

## 1. Double-factor lemma

Let `S` be a permutation of `[r]`.  Suppose `G_0,G_1` are neighbour
permutations of `Q_r` with direction functions `delta_0,delta_1` satisfying

\[
 G_j(y)=y\oplus e_{\delta_j(y)},\qquad
                         \delta_1(y)=S\delta_0(y)     \tag{1.1}
\]

for every `y`.  No conjugacy of the vertices is assumed; (1.1) is a
same-vertex relation between the two outgoing directions.

For every even `p` and every `x`, put

\[
 y=Sp\oplus x,qquad d_p(x)=\delta_0(y),qquad
 F_p(x)=x\oplus e_{d_p(x)}.                           \tag{1.2}
\]

### Theorem 1.1 (affine parity complete mapping)

Every `F_p` is a neighbour permutation, and for every `x` the map

\[
                         T_x(p)=p\oplus e_{d_p(x)}     \tag{1.3}
\]

is a bijection from the even to the odd parity shore.  Hence (1.2)
satisfies the exact parity complete-mapping gate.

#### Proof

For fixed `p`, the affine coordinate change `y=Sp+x` turns (F_p) into

\[
 Sp\oplus F_p(x)
 =y\oplus e_{\delta_0(y)}=G_0(y).                    \tag{1.4}
\]

Thus `F_p` is an affine conjugate of `G_0` and is a permutation.

For fixed `x`, the same coordinate change turns (1.3) into

\[
 S T_x(p)\oplus x
 =y\oplus e_{S\delta_0(y)}
 =y\oplus e_{\delta_1(y)}=G_1(y).                    \tag{1.5}
\]

The affine map `p -> Sp+x` is a bijection from one parity shore of `Q_r`
to one parity shore (depending on `x`), and `G_1` bijects the two shores.
Equation (1.5) therefore proves that `T_x` is bijective.  \(\square\)

If every cycle of `G_0` is an isometric `C_(2r)`, the same is true for all
`F_p`.  The parity lift theorem then gives an exact pair-clustered physical
`C_(4r)`-factor of `Q_(2r)`.

## 2. The common-phase braid supplies the hypotheses

Use the notation of
`MATH_THEOREM_Q4_COMMON_PHASE_BLOCK_TRANSPOSITION_20260726.md`.  Let `G_0`
be the successor permutation of the factor with word `1234 1234`, and
let `G_1` be the successor permutation of the factor with word
`1432 1432`, both oriented by their common phase colouring.  Put

\[
                              S=(2\ 4).                \tag{2.1}
\]

At a phase of colour `j`, the outgoing directions are respectively

\[
\begin{array}{c|cccccccc}
j&0&1&2&3&4&5&6&7\\ \hline
\delta_0&1&2&3&4&1&2&3&4\\
\delta_1&1&4&3&2&1&4&3&2.
\end{array}                                           \tag{2.2}
\]

Since the colouring is common owner by owner, (2.2) gives exactly

\[
                              \delta_1(y)=S\delta_0(y) \tag{2.3}
\]

for all sixteen vertices.

### Corollary 2.1 (first nonconstant exact lift)

For `r=4`, equations

\[
 d_p(x)=\delta_0(Sp+x),\qquad p\in Q_4^{\rm even},    \tag{2.4}
\]

define eight indexed context-dependent coarse `C_8`-factors `F_p`
satisfying every column complete-mapping equation.  Their adjacent
`b_i,a_i` expansion is an exact physical `C_16`-factor of `Q_8`.

There are exactly two distinct functions `F_p`, each used by four even
contexts.  Indeed

\[
 \operatorname {Stab}_{\rm tr}(\delta _0)
   =\langle0101,1010\rangle,
\]

and this space is preserved by `S`; on the even shore the factor type is
the single bit `p_1\oplus p_3=p_2\oplus p_4`.  The construction is
therefore genuinely nonconstant, but it is already fourfold degenerate.

## 3. Exact boundary

Theorem 1.1 solves ownership, pair clustering, and context dependence in
one identity.  It does not make the trace code

\[
 (J_{p,d}(x),x|_{J^c},p|_{J^c})                     \tag{3.1}
\]

injective.  At `r=4` its nonempty tagged fibre sizes at depths `1,2,3,4` are
exactly `1,2,8,128`, the same as for the context-independent lift.

Exact recursive double-factor relations do exist; see
`MATH_THEOREM_DOUBLE_FACTOR_RECURSION_AND_TRACE_CEILING_20260726.md` and
`MATH_THEOREM_DOUBLE_FACTOR_RECURSION_AND_DOUBLE_ERASURE_HALL_CUT_20260726.md`.
The literal affine-lift recursion and the homogeneous product recursions
remain trace-degenerate.  The mixed recursion just cited closes its
two-sided tagged double-erasure Hall map exactly; see
`MATH_THEOREM_CONTROLLED_CROSS_DOUBLE_FACTOR_AUGMENTED_CODE_20260726.md`
and `MATH_COUNTERAUDIT_CROSSED_RECURSION_CONTROLLED_COLUMN_REPAIR_20260726.md`.
A full growing construction therefore still needs support and boundary
roles to be recovered after forgetting the tag `J`, followed by the outer
packet coupling which realizes the local choices without owner overlap.

Thus neither the complete-mapping equation, bare recursive factorhood,
nor the explicitly tagged erasure code remains the first local gate.  The
next local gate is literal OR support recovery; the outer Hall coupling is
separate.
