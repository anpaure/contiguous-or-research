# Minimal exact owner exchange on the functional coatom face is a Boolean \(C_6\)

**Date:** 2026-08-05

**Method:** finite-set algebra; no computation, search, or solver

**Status:** unconditional classification theorem at the owner/state projection.
It proves that support two is impossible and that every nondegenerate
support-three, one-copy, owner-neutral rethread is the standard Boolean
hexagon, up to relabelling and reversal. It does not supply the literal
all-depth or upper-exterior guards needed for a universal word.

## 1. Functional coatom roles

Fix an owner rank \(r\). A functional coatom role is a pair

\[
                         (U,x),
 \qquad |U|=r-1,\qquad x\notin U,                    \tag{1.1}
\]

with owner colour

\[
                         \kappa(U,x)=U\cup\{x\}.     \tag{1.2}
\]

Take three roles, indexed cyclically modulo three,

\[
                         e_i=(U_i,x_i),
\]

and perform the cyclic tail rethread

\[
                         e_i'=(U_i,x_{i+1}).         \tag{1.3}
\]

Assume throughout that

1. the \(U_i\)'s are pairwise distinct;
2. the \(x_i\)'s are pairwise distinct;
3. both the old and new roles are rank-\(r\) legal, so
   \(x_i,x_{i+1}\notin U_i\); and
4. the three old owner colours are pairwise distinct.

The last condition is forced in a one-copy middle-owner selection.

## 2. Exact classification

### Theorem 2.1 (support-three owner-neutral classification)

The cyclic rethread (1.3) preserves the owner multiset,

\[
 \{\!\{U_i+x_i:i\in\mathbb Z_3\}\!\}
 =
 \{\!\{U_i+x_{i+1}:i\in\mathbb Z_3\}\!\},           \tag{2.1}
\]

if and only if there is one rank-\((r-2)\) set \(C\), disjoint from
\(x_0,x_1,x_2\), such that

\[
                         U_i=C\cup\{x_{i-1}\}
                         \qquad(i\in\mathbb Z_3).    \tag{2.2}
\]

Consequently the old and new owner triples are

\[
 \begin{aligned}
  A_i&=C\cup\{x_{i-1},x_i\},\\
  B_i&=C\cup\{x_{i-1},x_{i+1}\}=A_{i-1}.
 \end{aligned}                                      \tag{2.3}
\]

Thus every nondegenerate support-three exact exchange is precisely the
alternating exchange on the Boolean hexagon over the three active labels.

#### Proof

The reverse implication follows immediately from (2.3). For the forward
implication put

\[
                         A_i=U_i+x_i,\qquad
                         B_i=U_i+x_{i+1}.
\]

Because \(x_i\ne x_{i+1}\) and both lie outside \(U_i\), one has
\(A_i\ne B_i\). Since the \(A_i\)'s are distinct, equality of the two
multisets defines a permutation \(\tau\in S_3\) by

\[
                         B_i=A_{\tau(i)}.            \tag{2.4}
\]

The permutation has no fixed point, and is therefore one of the two
three-cycles.

If \(\tau(i)=i+1\), then

\[
                         U_i+x_{i+1}=U_{i+1}+x_{i+1}.
\]

Both coatoms omit \(x_{i+1}\), so deleting that element gives
\(U_i=U_{i+1}\), contrary to hypothesis. Hence necessarily

\[
                         \tau(i)=i-1.                \tag{2.5}
\]

Therefore

\[
                         U_i+x_{i+1}=U_{i-1}+x_{i-1}.\tag{2.6}
\]

The common rank-\(r\) set in (2.6) contains both \(x_{i+1}\) and
\(x_{i-1}\). Removing them leaves a rank-\((r-2)\) set \(C_i\) with

\[
                         U_i=C_i+x_{i-1},\qquad
                         U_{i-1}=C_i+x_{i+1}.        \tag{2.7}
\]

Apply (2.7) with indices \(i\) and \(i+1\). Because indices are modulo
three, both expressions for \(U_i\) adjoin the same active label
\(x_{i-1}=x_{i+2}\). Deleting that label gives \(C_i=C_{i+1}\).
Hence all three cores agree with one set \(C\), proving (2.2).
The legality assumptions show that no \(x_i\) lies in \(C\). Equation
(2.3) follows. \(\square\)

## 3. Minimal-support consequence

### Corollary 3.1 (the first nontrivial exact support is three)

On the one-copy functional coatom face:

* support one is the identity;
* a nontrivial owner-neutral support-two rethread is impossible; and
* every nontrivial owner-neutral support-three rethread is the Boolean
  \(C_6\) of Theorem 2.1.

#### Proof

The support-two assertion is the exact two-switch obstruction: if two
coatom/tail pairs and both crossed pairs are legal, equality of the two
owner multisets forces either the coatoms or the tails to coincide, making
the switch trivial. On three roles, a nonidentity permutation is either a
transposition, which reduces to support two, or a three-cycle. Apply
Theorem 2.1 to the latter. \(\square\)

This is stronger than merely exhibiting one useful hexagon. It says that
there is no different support-three algebraic packet waiting to evade the
known \(C_6\) guards.

## 4. Consequence for the exact-\(B\) and \(B+1\) routes

The classification gives a sharp local dichotomy.

1. An exact-\(B\), length-preserving topology change on the coatom
   functional face must begin with a Boolean \(C_6\) (or use support at
   least four). At the separate owner-factor/\(q1\) projection, the clean
   common-history \(C_6\) has an exact strict-lower lift. The present
   classification does **not** identify every functional-role \(C_6\) with
   that lifted packet; constructing a literal all-depth lift is an
   additional gate.
2. Allowing one repeated role changes the problem. The protected hub
   graft joins an integral residual factor and a reset cycle with exactly
   one duplicated owner/payload chain and therefore serializes at
   \(B(k)+1\). It avoids the support-two colour-neutrality requirement
   rather than contradicting it.

Accordingly, the shortest proof targets are now genuinely disjoint:

\[
 \boxed{\text{exact }B:\ C_6+\text{global upper guard}}
 \qquad\text{or}\qquad
 \boxed{B+1:\ \text{one-shared-state regenerative serializer}.}
\]

## 5. Scope

The theorem is purely at the owner-colour projection. It does not assert:

* that the three roles coexist as literal order-\(d\) trace arcs, or that
  they coincide with the separate clean common-history factor packet;
* residence or zero-gap preservation;
* arbitrary-width upper transparency;
* transport of a typed/shared common cap; or
* an all-dimensional bound for \(\nu(k)\).

Those are exactly the global guards left after the minimal local algebra is
classified.
