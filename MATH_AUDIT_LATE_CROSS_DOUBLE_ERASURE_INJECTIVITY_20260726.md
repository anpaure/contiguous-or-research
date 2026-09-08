# Audit of the repaired late-cross augmented code

Date: 2026-07-26

## Verdict

The blockwise decoder is correct, but only after two scope corrections.

First, the naive crossed partner is false: at
`(u,v)=(0000,1100)` its direction is `R3`, not the required `R1`.
The controlled shorewise-translation column in
`MATH_COUNTERAUDIT_CROSSED_RECURSION_CONTROLLED_COLUMN_REPAIR_20260726.md`
repairs the same-owner relation without changing the zeroth factor or its
direction supports.

Second, the decoder requires the support `J` as metadata.  A raw lower or
upper OR target does not determine `J`; completed and untouched empty/full
pairs can coincide.  Therefore the theorem is an augmented-code theorem,
not literal target injectivity.

With those corrections, the exact statement passes.  For
`R=8*2^t` and `d<=R/8`, every forward or reverse interval visits each
bottom `Q_8` block at most once.  In a touched block, its selected side
gives the block parity, and the selected `Q_4` direction fibre is a coset
of

\[
                         L=\langle0101,1010\rangle,
\]

whose one-coordinate punctures are injective.  This recovers the selected
bit; block parity recovers its `S_8`-mate.  Hence

\[
 y\mapsto
 \left(J_d^\pm(y),
 y|_{[R]\setminus(J_d^\pm(y)\cup S_RJ_d^\pm(y))}\right)
\]

is injective.  Consequently the explicitly tagged affine code

\[
 (J_d^\pm(S_Rp+x),p|_{J^c},x|_{J^c})
\]

has exact fibre degree one.  This includes cyclic seams and the endpoint
`d=R/8`.  It does not imply injectivity after the tag `J` is forgotten.
