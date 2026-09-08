# Audit: the crossed double factor fails, but the recursive context array is valid

Date: 2026-07-26

Method: direct hand verification only.

## 0. Verdict

The crossed-double-factor claim used in
`MATH_THEOREM_DOUBLE_FACTOR_RECURSION_AND_DOUBLE_ERASURE_HALL_CUT_20260726.md`
and copied into
`MATH_THEOREM_LATIN_DIRECTION_ARRAY_COMPLETE_SHALLOW_SOLUTION_20260726.md`
is false.  It compares direction fields evaluated at two different child
states.

A later repair replaces that false opposite-state child by a shorewise
translation evaluated at the same state as the zeroth direction.  It is a
valid neighbour-permutation witness and restores the augmented-code
compiler; see
`MATH_THEOREM_CROSSED_COLUMN_WITNESS_REPAIR_20260726.md`.  This does not
alter the literal-target warning: without an interface which reveals
`J`, augmented trace injectivity is not literal lower/upper injectivity.

This does **not** reopen the local parity-complete trace gate.  The earlier
construction in
`MATH_ATTACK_S_PARITY_COMPLETE_MAPPING_TRACE_ENTROPY_CUT_20260726.md`
builds the entire context array recursively and is valid.  It proves exact
row factors, exact full-cube column bijections, forward and reverse aligned
trace injectivity through coarse depth (n/4), and the literal half-step
statement through physical length (n/2-1) in the coordinate-disjoint
Johnson interface.

Thus the correct disposition is:

* retract the crossed-double-factor recursion and every theorem which uses
  it to justify column exactness;
* retain the late-cross **zeroth-factor phase decoder** only as a statement
  about that one factor;
* cite the recursive context-array theorem for the actual local compiler.

## 1. Explicit counterexample to the crossed relation

The claimed crossed recursion starts from a double factor
((G_0,G_1,S)) on (Q_h) and defines, for
(epsilon(u,v)=|u|+|v|\pmod2),

\[
 P_0(u,v)=
 \begin{cases}(G_0u,v),&\epsilon=0,\\(u,G_0v),&\epsilon=1,
 \end{cases}                                                     \tag{1.1}
\]

and

\[
 P_1^\times(u,v)=
 \begin{cases}(u,G_1v),&\epsilon=0,\\(G_1u,v),&\epsilon=1.
 \end{cases}                                                     \tag{1.2}
\]

It then declares

\[
 S^\times(Li)=R(Si),\qquad S^\times(Ri)=L(Si).                   \tag{1.3}
\]

At an even-total-parity owner, however, the two outgoing directions are

\[
                         L\delta_0(u),\qquad R\delta_1(v)
                         =RS\delta_0(v),                          \tag{1.4}
\]

whereas (1.3) sends the first to (RS\delta_0(u)).  Equality would require
(delta_0(u)=\delta_0(v)), which is not implied by equal parity.

For the displayed (Q_4) seed, take

\[
                         u=0000,\qquad v=1100.                    \tag{1.5}
\]

Both have even weight, while

\[
                         \delta_0(u)=1,\qquad\delta_0(v)=3.       \tag{1.6}
\]

With (S=(2\ 4)), (1.4) gives directions (L1) and (R3), but
(S^\times(L1)=R1).  This is a literal same-owner counterexample.

The proof line saying “Equation (3.3) uses (Si), while (3.4) uses the
right direction (Si)” silently uses the same symbol (i) for
(delta_0(u)) and (delta_0(v)).  They need not agree.

## 2. Consequences of the failure

The zeroth child (P_0) in (1.1) is still an exact isometric factor, and
its fixed-point-free block map may still have the stated double-erasure
phase-decoding property.  What fails is the existence of the asserted
partner (P_1^\times) with direction field
(S^\times\delta_{P_0}).  Therefore the affine identity

\[
 S^\times T_x(p)+x=P_1^\times(S^\times p+x)                       \tag{2.1}
\]

cannot be invoked, and column bijectivity of the resulting direction array
does not follow.

In particular, Lemma 2.1 and Theorem 3.1 of
`MATH_THEOREM_LATIN_DIRECTION_ARRAY_COMPLETE_SHALLOW_SOLUTION_20260726.md`
must not be cited.  Their row factor (G_R^0) and phase decoder can be
correct while property 2, the parity-column Latin equation, remains
unsupported.

## 3. The valid replacement

Let (n=4\cdot2^t).  The valid construction defines a direction array
for **every** context recursively, rather than deriving it from a crossed
partner.

### 3.1 Base

On (Q_4), let (G) have word (1234,1234), let (delta) be its
outgoing field, and put

\[
                         S=(1\ 4\ 3\ 2).                         \tag{3.1}
\]

The incoming direction identity is

\[
                         G^{-1}(y)=y+e_{S\delta(y)}.              \tag{3.2}
\]

For every (p,x\in Q_4), set

\[
 y=Sp+x,\qquad d_{4,p}(x)=\delta(y).                              \tag{3.3}
\]

Then

\[
\begin{aligned}
 Sp+F_{4,p}(x)&=G(Sp+x),\\
 S\Theta_{4,x}(p)+x&=G^{-1}(Sp+x),
\end{aligned}                                                    \tag{3.4}
\]

so every row and every full-cube column is a neighbour permutation.

### 3.2 Recursion

Split (p=(p_L,p_R)), (x=(u,v)), and define

\[
 F_{2h,p}(u,v)=
 \begin{cases}
  (F_{h,p_L}(u),v),&|u|+|v|=0,\\
  (u,F_{h,p_R}(v)),&|u|+|v|=1.
 \end{cases}                                                     \tag{3.5}
\]

The branch depends only on (x), not on (p).  Therefore, for fixed
(x), its column map is literally

\[
 \Theta_{2h,x}(p_L,p_R)=
 \begin{cases}
  (\Theta_{h,u}(p_L),p_R),&|u|+|v|=0,\\
  (p_L,\Theta_{h,v}(p_R)),&|u|+|v|=1.
 \end{cases}                                                     \tag{3.6}
\]

This is bijective and parity reversing by induction.  Squaring a row map
advances both child rows once, so every row consists of isometric
(C_{4h})'s.

There is no comparison of (delta(u)) with (delta(v)) in this proof.

## 4. Trace and half-step audit

The base direction fibres are cosets of

\[
 K=\langle1111,0101\rangle.                                     \tag{4.1}
\]

For every direction (i),

\[
                         K\cap\langle e_i,e_{S i}\rangle=0,     \tag{4.2}
\]

which gives exact forward and reverse joint depth-one recovery.

At a recursive split, a length-(q) direction segment projects to
consecutive child segments of depths

\[
 (\lfloor q/2\rfloor,\lceil q/2\rceil).                          \tag{4.3}
\]

The support cardinalities identify the child which moves first when (q)
is odd.  Thus the parent joint code splits into the two child joint codes,
and induction gives exact forward and reverse injectivity for

\[
                         q\le n/4.                                \tag{4.4}
\]

For the physical paired lift, a coarse direction appears as
((b_i,a_i)).  In the coordinate-disjoint Johnson realization, a literal
signed target identifies every varied physical direction: occupancy is
zero/two on a varied swap pair and one on an untouched pair.  Hence a
partial boundary block identifies its missing mate.  Completing at most
one move at each end reduces any unaligned interval to an aligned interval
one coarse step deeper.  The worst case remains within (4.4) whenever

\[
                         \ell\le n/2-1.                            \tag{4.5}
\]

This verifies the stated half-step scope.  Without the coordinate-disjoint
swap-pair decoder, only the augmented-code version follows.

## 5. Final scope

The local parity-complete compiler is therefore closed, but by (3.3)--
(3.6), not by a crossed double factor.  It gives the exact local range
needed for any protected (H=O(\sqrt n)) window after choosing
(n\ge2(H+1)).

The remaining obstacle is external: owner-disjoint installation and the
aggregate cross-packet literal target overlap/Hall deficit.  No local
row, column, aligned trace, or half-step theorem remains open in the
coordinate-disjoint interface.
