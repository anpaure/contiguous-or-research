# Independent audit V3: protected Ore residual-capacity DM uncrossing

**Date:** 2026-08-04  
**Verdict:** **GO**.  No computation, search, or solver output is used.

Audited theorem:
`MATH_THEOREM_PROTECTED_ORE_RESIDUAL_CAPACITY_DM_UNCROSSING_20260804.md`,
SHA-256
`fd528c5cb0fa2c50af611271ee3ef1f0bbbcc1849cee7226335ebb88c8dd2bf2`.

Author self-audit:
`MATH_AUDIT_PROTECTED_ORE_RESIDUAL_CAPACITY_DM_UNCROSSING_SELF_20260804.md`,
SHA-256
`21d5f57b9e034f09a412d958146a3cb0552cb4454ec446a056aaea5fd31af88b`.

This audit supersedes the V2 audit at SHA
`8abf05bf37e76fbe475e8b9310a69cbd10aab4fc1f0b20ed58c7f35da6e5abec`
for the expanded Section 6.  Sections 1--5 and 7 retain the proofs already
independently validated there.

## 1. Incidence-lift lower degrees and the forced bank

In the incidence lift of a family of simple owner paths, every Johnson edge
is subdivided by its immediate-lower intersection.  Each protected lower
vertex appearing in the lift is incident with the two adjacent owner edges,
and lower-colour simplicity prevents collision with another path edge.
Thus every protected lower vertex has degree exactly two and every other
lower vertex has degree zero.  Therefore

\[
 Z_P=\{x:d_P(x)=2\}
\]

is exactly the protected lower bank and

\[
 2|Z_P|=|E(P)|.
\]

The irreducibility theorem for the unique minimal deficient shore excludes
every lower vertex of protected degree two from `A^-`.  Hence, for
`C=L-A^-`,

\[
 Z_P\subseteq C.
\]

This is the necessary forced-element step; it is not an assumption about an
arbitrary co-small complement.

## 2. Exact substitution in the co-small criterion

Every protected edge has its lower endpoint in `Z_P subseteq C`.  It follows
simultaneously that

\[
 D_P(C)=|E(P)|,
 \qquad
 \operatorname{def}_P(C)=2|C|-|E(P)|,
 \qquad
 p_U=e_P(U,C)=d_P(U)
\]

for every owner `U`.

The frozen exact co-small criterion is

\[
 \theta(C)>\operatorname{def}_P(C)+R_P(C).
\]

At an owner with `d_C(U)=m`, its contribution to `theta-R` is
`2-p_U=2-d_P(U)`.  At an owner with `d_C(U)=m-1`, it is

\[
 1-\min(d_P(U),1),
\]

which equals one exactly when `d_P(U)=0` and otherwise equals zero.  All
other owners contribute zero.  Therefore

\[
 \theta(C)-R_P(C)=\Omega_P(C)
\]

with precisely the definition in (6.2), and failure is equivalent to

\[
 \Omega_P(C)>2|C|-|E(P)|.
\]

Reversing the same exact equivalence proves that a complement containing
`Z_P` is safe whenever the weak reverse inequality holds.  Since
`Z_P subseteq C` and `2|Z_P|=|E(P)|`, the size floor

\[
 |C|\ge|E(P)|/2
\]

also follows exactly.

## 3. Optional-bank gap saturation

Write `C=Z_P dotcup B` and define

\[
 g_U=m-|N(U)\cap Z_P|,
 \qquad
 b_U=|N(U)\cap B|.
\]

Disjointness gives

\[
 d_C(U)=|N(U)\cap Z_P|+b_U=m-g_U+b_U.
\]

Thus

\[
 d_C(U)=m\iff b_U=g_U,
 \qquad
 d_C(U)=m-1\iff b_U=g_U-1.
\]

Substitution into the already verified ownerwise expression for `Omega`
gives exactly

\[
 \Omega_P(C)=\sum_U\left[
 (2-d_P(U))\mathbf1_{\{b_U=g_U\}}
 +\mathbf1_{\{d_P(U)=0\}}\mathbf1_{\{b_U=g_U-1\}}
 \right].
\]

When `g_U=0`, the second equality would require `b_U=-1`; declaring that
indicator zero is correct.

Finally,

\[
 2|C|-|E(P)|
 =2|Z_P|+2|B|-2|Z_P|
 =2|B|.
\]

Hence the complementary cut fails if and only if

\[
 \Omega_P(Z_P\cup B)>2|B|.
\]

Both directions are exact; this is not merely a sufficient density test.

## 4. Remaining scope

The co-small result classifies failure after the forced protected lower bank
is inserted.  It does not prove the optional-bank gap-saturation inequality,
exclude a co-small deficient shore, or settle the shifted/initial-colex
transfer.  Those remain the stated open rows.

The Section 6/7 equation tags are corrected in the frozen theorem.  The
independent V3 verdict is **GO** at the hashes listed above.
