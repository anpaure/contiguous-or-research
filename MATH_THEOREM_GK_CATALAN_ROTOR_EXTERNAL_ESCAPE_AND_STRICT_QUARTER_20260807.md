# The Catalan-rotor cover makes the ordinary escape bank abstractly external and component-disjoint

**Date:** 2026-08-07  
**Status:** corrected-scope abstract root theorem.  The endpoint and
component-disjointness statements are unconditional.  The former claim
that paired `C_6`s physically fuse the base and escape edges is retracted:
their common fixed edge cancels and leaves a nonalternating `00` pair.
Thus the note proves an abstract strict-quarter component matching, not a
literal factor contraction.  See
`MATH_CORRECTION_GK_ROOT_PATH_C6_SYMMETRIC_DIFFERENCE_NONALTERNATING_20260807.md`.

## 1. Endpoint permutation of the rotor cover

Use the Catalan bijection

\[
 \theta(\varnothing)=\varnothing,
 \qquad
 \theta(1A0N)=A1N0.                                  \tag{1.1}
\]

For a primitive Dyck word `C=1E0`, put

\[
                         g(C)=1\theta(E)0.             \tag{1.2}
\]

Both `theta` and `g` are bijections on their respective Dyck banks.
If

\[
                         A=C_1C_2\cdots C_s            \tag{1.3}
\]

is the primitive-component decomposition of `A`, define

\[
                         \Psi(A)=g(C_1)g(C_2)\cdots g(C_s).             \tag{1.4}
\]

Thus `Psi` is a bijection of every Dyck layer and preserves the number and
order of top-level primitive components.

## Theorem 1.1 (exact endpoints)

In the explicit standard cover from the Catalan-rotor theorem, the path
starting at the primitive root

\[
                         P(A)=1A0                       \tag{1.5}
\]

ends at the sink root

\[
                         S(\Psi(A))=10\Psi(A).          \tag{1.6}
\]

It has exactly `s` selected root edges, where `s` is the number of
primitive components in (1.3).

### Proof

The standard-cover map removes the last primitive component of the
current first-primitive interior and places its `g`-image immediately
after that first primitive.  Hence the successive roots are

\[
\begin{aligned}
 1C_1\cdots C_s0
 &\longrightarrow (1C_1\cdots C_{s-1}0)g(C_s)\\
 &\longrightarrow (1C_1\cdots C_{s-2}0)g(C_{s-1})g(C_s)\\
 &\longrightarrow\cdots\longrightarrow
 10g(C_1)\cdots g(C_s).
\end{aligned}                                         \tag{1.7}
\]

This proves both assertions. \(\square\)

## 2. The rigid two-child family

For `D in D_{m-3}`, put

\[
 U_D=11D0100,\qquad
 V_D=11D0010,\qquad
 W_D=10D1100.                                         \tag{2.1}
\]

The standard-cover edge out of `U_D` is exactly

\[
                         U_D\longrightarrow V_D.       \tag{2.2}
\]

Indeed the interior of the first primitive of `U_D` is

\[
                         (1D0)(10),                    \tag{2.3}
\]

whose final primitive is `10`; applying the rotor rule gives (2.2).  This
also agrees with the independent indegree-one forcing theorem for `V_D`.

The unused first-child socket gives the ordinary matching-close escape

\[
                         U_D\longrightarrow W_D.       \tag{2.4}
\]

Both (2.2) and (2.4) are root-rotation edges, so each individually has an
alternating paired-root `C_6`.  They share the fixed root edge at `U_D`.
Their symmetric difference is a simple length-ten incidence cycle, but it
is **not alternating**: after the shared fixed edge cancels, the two
surviving cross edges at `X_{U_D}` both have status zero.  Consequently an
additional phase-repair or higher alternating circuit is required to use
both edges physically.

## 3. The ordinary escape is always external

The primitive component index of the path starting at `U_D` is

\[
                         A_D=(1D0)(10).                \tag{3.1}
\]

By Theorem 1.1 its sink is

\[
  S(\Psi(A_D))
   =10\,g(1D0)g(10)
   =10\,(1\theta(D)0)(10).                            \tag{3.2}
\]

For nonempty `D`, this word ends in `0010`, whereas `W_D` ends in `1100`.
For empty `D`, (3.2) is `101010`, while `W_D=101100`.  Thus they are
different in every case.

## Corollary 3.1

`W_D` is never the endpoint of the component starting at `U_D`.
Consequently every edge (2.4) joins two different standard-cover
components.  No internal-close alternative is required.

## 4. The whole escape bank is component-disjoint

Let `A'_D` be the primitive start index of the component ending at `W_D`.
Since

\[
                         W_D=S(D\,1100),               \tag{4.1}
\]

Theorem 1.1 gives

\[
                         A'_D=\Psi^{-1}(D\,1100).      \tag{4.2}
\]

The word `1100` is fixed by `g`.  Because `Psi` acts independently on
primitive components, every `A'_D` ends in the primitive component
`1100`.  In contrast, every `A_D` in (3.1) ends in the primitive component
`10`.  Therefore

\[
                 \{A_D:D\in{\cal D}_{m-3}\}
                 \cap
                 \{A'_D:D\in{\cal D}_{m-3}\}
                 =\varnothing.                        \tag{4.3}
\]

Both maps are injective: this is immediate for `D -> A_D`, and for
`D -> A'_D` it follows from injectivity of `D -> D1100` and of `Psi`.

## Theorem 4.1 (abstract component-matching escape bank)

All

\[
                         \operatorname{Cat}_{m-3}      \tag{4.4}
\]

ordinary escape edges (2.4) join pairwise disjoint pairs of distinct
abstract standard-cover components.  Hence there is no abstract component
cycle deletion and no loss of a factor two.

The root sockets are also private: (2.2) uses the later-child socket of
`U_D`, while (2.4) uses its first-child socket.  Across different `D`,
global socket-colour injectivity makes the corresponding `a` and `B_y`
banks private, and the targets `W_D` are distinct.  This resource
injectivity does not cure the local phase defect at the shared root.

## 5. Abstract strict one-quarter component count

Put

\[
                         N=\operatorname{Cat}_m,
 \qquad                  C=\operatorname{Cat}_{m-1}.  \tag{5.1}
\]

The rotor cover has `C` components.  After adding the full component
matching of Theorem 4.1, it has

\[
                         C-\operatorname{Cat}_{m-3}    \tag{5.2}
\]

components.  The strict inequality

\[
 C-\operatorname{Cat}_{m-3}<{N\over4}                \tag{5.3}
\]

is equivalent to

\[
 m(m^2-1)>6(2m-5)(2m-3).                             \tag{5.4}
\]

The cubic difference is

\[
                         m^3-24m^2+95m-90.             \tag{5.5}
\]

It is positive for every `m>=20` (and increasing there).  Direct integer
comparison gives the same threshold for the consecutive large range; no
small-`m` claim is needed for the asymptotic induction.

## Corollary 5.1 (abstract root-level strict contraction)

For every `m>=20`, the explicit standard depth-two cover plus the full
ordinary paired-`C_6` escape bank has fewer than

\[
                         {1\over4}\operatorname{Cat}_m                \tag{5.6}
\]

abstract root components.

Thus ordinary Hall, endpoint topology and lower-colour privacy are closed
at the abstract selector level.  Literal reverse/rethread phase is not.

## 6. Exact remaining scope

The theorem is not yet a physical strict-quarter factor, much less an
all-`k` OR-word construction.  What remains is:

1. construct a phase-repair circuit, higher alternating circuit, or
   opposite-phase factor for the length-two path
   `V_D--U_D--W_D`;
2. lift the repaired factor with coordinate residence and erosion
   envelopes;
3. retain arbitrary-width upper witnesses; and
4. retain one terminal lower/common-cap compiler with bounded deficiency and a
   regenerating endpoint state.

The former support-two internal-close helper packet is unnecessary for the
**abstract** component matching, but its claimed length-18 alternating
fusion is independently retracted by the same phase audit.
