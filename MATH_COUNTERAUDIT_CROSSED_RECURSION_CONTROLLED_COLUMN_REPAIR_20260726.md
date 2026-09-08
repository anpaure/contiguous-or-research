# Counteraudit of crossed recursion and an exact controlled-column repair

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The crossed recursion asserted in
`MATH_THEOREM_DOUBLE_FACTOR_RECURSION_AND_DOUBLE_ERASURE_HALL_CUT_20260726.md`
is false.  Its proof applies a same-vertex direction identity to two
different vertices.  A two-line `Q_4` counterexample is

\[
                         u=0000,\qquad v=1100.       \tag{0.1}
\]

There is, however, an exact repair.  Keep the zeroth parity-alternating
factor `P_0`, but replace the crossed first factor by a controlled column
permutation whose direction in the opposite half is computed from the
same half-state used by `P_0`.  This gives a genuine same-owner
double-factor certificate, recurses in parallel, and restores the exact
complete-mapping and isometric-cycle conclusions.

The repaired construction also restores the late-cross **augmented**
trace theorem: when the direction support `J` is retained as a tag, its
double-erasure code is injective through depth `R/8`.  It does not prove
literal lower- or upper-OR injectivity, because `J` is not contained in a
raw target.  Thus the repair closes ownership plus the decorated phase
code, but not the coefficient-one target gate.

## 1. The proposed crossed factor fails

Let `G_0,G_1` be the two audited neighbour permutations of `Q_4`, with

\[
                         \delta_1(w)=S_4\delta_0(w),
                         \qquad S_4=(2\ 4),          \tag{1.1}
\]

at the **same** vertex `w`.  The proposed zeroth child is

\[
 P_0(u,v)=
 \begin{cases}
  (G_0u,v),&|u|+|v|=0\pmod2,\\
  (u,G_0v),&|u|+|v|=1\pmod2,
 \end{cases}                                        \tag{1.2}
\]

while the proposed crossed first child is

\[
 P_1^\times(u,v)=
 \begin{cases}
  (u,G_1v),&|u|+|v|=0\pmod2,\\
  (G_1u,v),&|u|+|v|=1\pmod2.
 \end{cases}                                        \tag{1.3}
\]

The claimed direction permutation was

\[
 S_8^\times(Li)=R(S_4i),\qquad
 S_8^\times(Ri)=L(S_4i).                            \tag{1.4}
\]

At the state (0.1), total parity is even.  From the explicit phase table,

\[
                         \delta_0(0000)=1,
                         \qquad\delta_1(1100)=3.    \tag{1.5}
\]

Consequently

\[
 \delta_{P_0}(u,v)=L1,qquad
 \delta_{P_1^\times}(u,v)=R3,                      \tag{1.6}
\]

whereas

\[
                         S_8^\times(L1)=R1.          \tag{1.7}
\]

Thus the same-owner identity fails.

The error is structural, not a bad choice of (1.4).  Fix `u=0000` and
compare the even vertices `v=0000` and `v=1100`.  The zeroth direction is
`L1` at both product vertices, while the crossed first directions are
respectively `R1` and `R3`.  No fixed map of direction labels can send
the one zeroth direction to both outputs.  Equation (1.1) relates
`delta_0(w)` and `delta_1(w)` only when their arguments are the same; it
cannot compare `delta_0(u)` with `delta_1(v)`.

The map `P_1^times` may still be a neighbour permutation in its own
right.  What fails is precisely the double-factor relation needed by the
affine complete-mapping proof.  Hence the original late-cross ownership
claim and everything depending on it must be retracted.

## 2. The controlled-column replacement

Only the zeroth `Q_4` factor is needed for the repair.  Put

\[
                         d(w)=\delta_0(w),
\]

and retain `P_0` from (1.2).  Define

\[
 C_{S_4}(u,v)=
 \begin{cases}
  (u,v+e_{S_4d(u)}),&|u|+|v|=0\pmod2,\\
  (u+e_{S_4d(v)},v),&|u|+|v|=1\pmod2.
 \end{cases}                                        \tag{2.1}
\]

### Lemma 2.1 (exact column permutation)

`C_(S_4)` is a neighbour permutation of `Q_8`.

#### Proof

It plainly toggles one coordinate and swaps the total-parity shores.
Consider an odd target `(u,w)`.  Its unique even predecessor under the
first clause is

\[
                         v=w+e_{S_4d(u)}.            \tag{2.2}
\]

Indeed,

\[
 |u|+|v|=|u|+|w|+1=0\pmod2.                        \tag{2.3}
\]

Thus the even-to-odd restriction is bijective.  Similarly an even target
`(w,v)` has the unique odd predecessor

\[
                         u=w+e_{S_4d(v)},            \tag{2.4}
\]

and its parity is odd because `|w|+|v|=0`.  Hence the odd-to-even
restriction is bijective as well.  \(\square\)

Define the fixed-point-free involution

\[
 X_8(Li)=R(S_4i),\qquad X_8(Ri)=L(S_4i).            \tag{2.5}
\]

### Lemma 2.2 (same-owner controlled direction)

At every product vertex `z`,

\[
                         \delta_{C_{S_4}}(z)
                         =X_8\delta_{P_0}(z).        \tag{2.6}
\]

#### Proof

At even total parity, `P_0` uses `Ld(u)` and `C_(S_4)` uses
`R(S_4d(u))`.  At odd total parity, they use respectively `Rd(v)` and
`L(S_4d(v))`.  These are exactly the two clauses of (2.5).  \(\square\)

Unlike (1.3), the controlled column deliberately reads the same local
state as `P_0`; this is why the same-owner relation is now literal.

## 3. Parallel recursion of the repaired certificate

For any neighbour permutation `H` on `Q_h`, define

\[
 \mathcal R(H)(a,b)=
 \begin{cases}
  (Ha,b),&|a|+|b|=0\pmod2,\\
  (a,Hb),&|a|+|b|=1\pmod2.
 \end{cases}                                        \tag{3.1}
\]

### Lemma 3.1

If `H` is a neighbour permutation, then `R(H)` is a neighbour
permutation.  If `H_0,H_1` satisfy

\[
                         \delta_{H_1}=X\delta_{H_0}, \tag{3.2}
\]

then

\[
 \delta_{\mathcal R(H_1)}
 =(X\oplus X)\delta_{\mathcal R(H_0)}.              \tag{3.3}
\]

#### Proof

Every move changes total parity, so the selected outer half alternates and

\[
                         \mathcal R(H)^2(a,b)=(Ha,Hb).       \tag{3.4}
\]

The right side is bijective; hence `R(H)^2`, and therefore `R(H)`, is
bijective.  At a fixed product vertex, both recursive maps select the
same outer half.  Relation (3.2) inside that half is exactly (3.3).
\(\square\)

Starting from

\[
                         (G_8,C_8,X_8)
                         =(P_0,C_{S_4},X_8),         \tag{3.5}
\]

iterate

\[
 G_{2h}=\mathcal R(G_h),\qquad
 C_{2h}=\mathcal R(C_h),\qquad
 X_{2h}=X_h\oplus X_h.                              \tag{3.6}
\]

This gives a genuine double-factor certificate in every dimension

\[
                         R=8\,2^t.                  \tag{3.7}
\]

Only the zeroth factor needs an isometric cycle structure.  The original
`G_4` consists of isometric `C_8` cycles; the parity-alternating recursion
therefore makes `G_R` an exact factor into isometric `C_(2R)` cycles.
No cycle-length or isometry hypothesis on the auxiliary column `C_R` is
used by the affine complete-mapping lemma.

## 4. The affine lift is now exact

For even `p in Q_R` and `x in Q_R`, put

\[
 y=X_Rp+x,\qquad
 d_p(x)=\delta_{G_R}(y),\qquad
 F_p(x)=x+e_{d_p(x)}.                               \tag{4.1}
\]

For fixed `p`, translation by `X_Rp` conjugates `F_p` to `G_R`, so every
`F_p` is an isometric `C_(2R)` factor.  For fixed `x`, let

\[
                         T_x(p)=p+e_{d_p(x)}.         \tag{4.2}
\]

Then

\[
 X_RT_x(p)+x
 =y+e_{X_R\delta_{G_R}(y)}
 =C_R(y).                                            \tag{4.3}
\]

Since `C_R` is a neighbour permutation, it bijects the two parity shores.
The affine change `p mapsto X_Rp+x` does the same shore bookkeeping as in
the original complete-mapping lemma.  Therefore every `T_x` is a
bijection from even to odd contexts.  The adjacent `(b_i,a_i)` lift is an
exact physical factor into isometric `C_(4R)` cycles.

This proves that the controlled-column repair completely restores
ownership, physical factorhood, cycle length, and isometry.

## 5. What survives of the late-cross decoder

The repair changes only the auxiliary certificate `C_R`.  It leaves the
zeroth factor `G_R` and the involution `X_R` exactly equal to the objects
used in the punctured-fibre late-cross decoder.  Consequently all of its
local statements remain valid:

1. every forward or reverse direction interval of depth `d<=R/8` visits
   each bottom `Q_8` block at most once;
2. the selected bottom direction and the six bits outside its
   `X_8`-pair recover the full bottom phase; and
3. both augmented phase maps
   
   \[
   y\longmapsto
   \left(J_d^\pm(y),
   y|_{[R]\setminus(J_d^\pm(y)\cup X_RJ_d^\pm(y))}
   \right)                                          \tag{5.1}
   \]
   
   are injective.

Thus the repaired construction gives an exact one-copy owner factor
together with a collision-free, two-sided **decorated** trace code
through every fixed Gaussian band.

## 6. The metadata obstruction

The support `J` in (5.1) is not part of a literal lower or upper OR
target.  This is already visible on one edge of `Q_2`.  The two paths

\[
                         00\longleftrightarrow10,
                         \qquad
                         00\longleftrightarrow01     \tag{6.1}
\]

have different direction supports `{1}` and `{2}`, but the same lower
target `00`.  Likewise

\[
                         01\longleftrightarrow11,
                         \qquad
                         10\longleftrightarrow11     \tag{6.2}
\]

have different direction supports and the same upper target `11`.

In general, if a path starts at `z` and toggles the direction set `D`,
then the literal signed targets are

\[
 L=z\wedge(z+1_D),\qquad
 U=z\vee(z+1_D).                                    \tag{6.3}
\]

Neither `L` nor `U` determines `D`: a zero outside `D` is
indistinguishable in `L` from a toggled coordinate, and a one outside
`D` is indistinguishable in `U` from a toggled coordinate.

Therefore `(J, exterior state)` is a strict refinement of the raw target.
Injectivity before forgetting `J` does not imply injectivity after
forgetting it.  Any identity equating the fibres of (5.1) with literal
physical target fibres requires an additional recoverability theorem for
`J`; no such theorem is supplied by the controlled column or the
punctured-coset decoder.

## 7. Exact boundary

The original crossed factor is rigorously refuted by (0.1)--(1.7).
The controlled-column replacement proves:

* an exact same-owner double-factor certificate at `Q_8`;
* exact parallel recursion to every `R=8*2^t`;
* an exact physical owner factor into isometric cycles; and
* exact two-sided injectivity of the augmented `J`-tagged phase code for
  every `d<=R/8`.

It does **not** prove literal lower/upper target injectivity or
coefficient one.  The surviving target-level gate is exact:

> Prove that the raw lower and upper targets recover enough of `J` to
> make the forgetful map from augmented traces asymptotically injective,
> or derive a raw-target Hall cut for the repaired factor.
