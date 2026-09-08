# The `T_2` variable-successor tag clock has one forced two-seam contradiction

**Date:** 2026-08-13  
**Status:** exact finite obstruction to the unmodified variable-successor
tag block.  It does not rule out a local tag sweep/reset collar.

## 1. The two exceptional base targets

Write the five rank-seven upper owners as

\[
\begin{aligned}
 a&=1010110011010, & b&=1011100011010,\\
 c&=1011110001010, & d&=1010011011010,\\
 e&=1000111011010.
\end{aligned}                                             \tag{1.1}
\]

The two old/new seam pairs are

\[
\begin{array}{c|c|c|c}
 &\text{old seam}&\text{new seam}&\text{common rank-eight value}\\ \hline
B&a\longrightarrow b&c\longrightarrow a&1011110011010\\
C&d\longrightarrow a&a\longrightarrow e&1010111011010.
\end{array}                                                \tag{1.2}
\]

The displayed values follow from the literal OR identities

\[
 a\cup b=c\cup a=1011110011010,\qquad
 d\cup a=a\cup e=1010111011010.                            \tag{1.3}
\]

These are exactly the two unmatched conservative `Z_13` seam signatures
in the complete `ML(13)` relay audit.

## 2. Boundary tag of a lifted seam

In the variable-successor block, the last lifted owner over a base owner
`u` and the first lifted owner over its successor `v` are

\[
 C+V_u+t^+(u)+D_0,qquad C+V_v+t(v)+D_0.                   \tag{2.1}
\]

The common-successor equation gives `t^+(u)=t(v)`.  Hence their union is

\[
 C+(V_u\cup V_v)+\{t(v)\}+D_0.                            \tag{2.2}
\]

Thus, for a fixed literal core and clock embedding, the auxiliary fibre
of a base seam is determined by the tag of its **head**.

## 3. Exact contradiction

### Theorem 3.1

No tag map satisfying the nondegenerate variable-successor conditions

\[
 t(s^-(v))=t(s^+(v))=:t^+(v)\ne t(v)                     \tag{3.1}
\]

can give the old and new witnesses in both rows of (1.2) the same literal
tag-clock fibres.  In fact it cannot align either row.

#### Proof

The owner `a` has old successor `b` and new successor `e`.  Equation
(3.1) at `a` therefore says

\[
                         t(b)=t(e)=t^+(a)\ne t(a).          \tag{3.2}
\]

By (2.2), the old `B` seam `a -> b` carries tag `t(b)`, while its new mate
`c -> a` carries tag `t(a)`.  Literal equality of their lifted targets
would require

\[
                         t(b)=t(a),                         \tag{3.3}
\]

contradicting (3.2).

Likewise the old `C` seam `d -> a` carries tag `t(a)`, while its new mate
`a -> e` carries tag `t(e)`.  Literal equality would require

\[
                         t(a)=t(e),                         \tag{3.4}
\]

again contradicting (3.2).  Both failures are therefore the same forced
nontrivial midpoint constraint at `a`.  \(\square\)

## 4. Exact escape boundary

If one permits

\[
                         t(a)=t^+(a),                       \tag{4.1}
\]

then both tag equalities (3.3)--(3.4) become possible.  But the two
`D_h` owners at the midpoint of `Gamma(a)` then coincide: the intended
tag exchange is no longer a Johnson edge, owner simplicity fails, and
simply deleting the duplicate shortens this one block relative to every
other block.  The uniform physical-width argument no longer applies.

There is a further topology constraint on such a reset.  In any
fixed-base vertex-block substitution, write `L_v,R_v` for the auxiliary
payloads of the incoming and outgoing endpoints over base owner `V_v`.
If every inter-block join is the literal old base Johnson exchange, then

\[
                         R_u=L_{s^\pm(u)}.                   \tag{4.2}
\]

The two seam alignments above force

\[
                         R_a=L_a.                            \tag{4.3}
\]

Since both endpoints also have the same base owner `V_a`, they are the
same owner target.  A positive-length simple path from one to the other
therefore repeats that owner.  If the repeated endpoints are instead
coalesced, the closed internal sweep uses two incident edges at that owner
in addition to its incoming and outgoing base edges, producing degree
four.

Thus a **tag-only closed sweep is not sufficient**.  The smallest live
repair must either:

* change a base/core/clock endpoint payload and balance the resulting
  owner current elsewhere; or
* leave `a` as an undilated singleton and prove its coordinate residence
  from the surrounding chronology.

A more general reset collar of one of these two kinds is not ruled out.
