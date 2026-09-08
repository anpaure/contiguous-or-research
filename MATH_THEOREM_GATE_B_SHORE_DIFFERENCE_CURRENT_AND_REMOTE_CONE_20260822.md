# Gate B: a shore-difference current bound and the remote cone

**Date:** 2026-08-22

**Status.**  This note proves a shore-adapted estimate for every blocker
set, before inclusion--exclusion is summed.  It improves the factor `2r` in
the usual rooted-current bound to `2j` after subtracting the middle and
lower shores.  Applied to the complete remote zero-avoidance tail outside
the sixteen four-cut atoms, it gives

\[
 \boxed{|R_r(t)-R_{r-1}(t)|\le CjD_Mr^{-3},\qquad
        |R_s(t)|\le CD_Mr^{-2}.}                              \tag{0.1}
\]

Thus for fixed harmonic depth the remote dressing lies in a cone of angle
`O(1/r)` about the common-shore line.  This is the relative mechanism which
an absolute `O(D_M/r^2)` estimate misses.  It does not by itself prove that
the full two-column determinant is nonzero: a rooted-core determinant at
the corresponding order is still required.

## 1. Configurations and currents

Put `b=2r+1`.  A word `w=(w_0,...,w_(b-1))` defines cyclic windows

\[
 I_s^w(a)=\{w_a,w_{a+1},\ldots,w_{a+s-1}\},
 \qquad a\in\mathbb Z_b,                                    \tag{1.1}
\]

with indices read modulo `b`.  Its directed punctured configuration is

\[
 E(w)=\{(M,I_r^w(a)):a\ne0\}\mathbin{\dot\cup}
      \{(L,I_{r-1}^w(a)):a\ne0\}.                            \tag{1.2}
\]

Fix `j` disjoint ordered label pairs `(a_i,b_i)`.  On an `s`-set put

\[
 H_{s,j}(S)=\prod_{i=1}^j
 (\mathbf1_{\{a_i\in S\}}-\mathbf1_{\{b_i\in S\}}),        \tag{1.3}
\]

and define the shore current of one configuration by

\[
 K_s(w)=\sum_{a=1}^{b-1}H_{s,j}(I_s^w(a)),
 \qquad s\in\{r,r-1\}.                                     \tag{1.4}
\]

For a set `J` of prescribed tagged targets, let

\[
 \deg(J)=|\{w:E(w)\supseteq J\}|,
 \qquad
 \Omega_s(J)=\sum_{w:E(w)\supseteq J}K_s(w).                \tag{1.5}
\]

The same definitions may be made after relabelling all targets and all
distinguished pairs, and may then be averaged with arbitrary coefficients
of absolute value at most one.  In particular they include the signed
boundary-event profiles used in the zero-avoidance quotient.

## 2. The pointwise shore coupling

### Theorem 2.1

For every word `w` and every choice of the `j` distinguished pairs,

\[
                         \boxed{|K_r(w)-K_{r-1}(w)|\le2j.}   \tag{2.1}
\]

Consequently, for every blocker set `J`,

\[
 \boxed{|\Omega_r(J)-\Omega_{r-1}(J)|\le2j\deg(J),\qquad
        |\Omega_s(J)|\le2r\deg(J).}                         \tag{2.2}
\]

#### Proof

Pair the two windows at the same retained start.  They are nested and
differ in exactly one label:

\[
 I_r^w(a)=I_{r-1}^w(a)\mathbin{\dot\cup}\{w_{a+r-1}\}.
                                                                    \tag{2.3}
\]

The product (1.3) depends only on membership of the `2j` distinguished
labels.  Therefore the two summands at start `a` agree unless
`w_(a+r-1)` is distinguished.  If it is distinguished, only one factor in
(1.3) changes, by one, while every other factor lies in `{-1,0,1}`; the
absolute change of the product is at most one.  As `a` runs through the
retained starts, each label occurs as `w_(a+r-1)` at most once.  At most
`2j` summands can therefore change, proving (2.1).

Sum (2.1) over the `deg(J)` words containing `J` to obtain the first
inequality in (2.2).  Each shore has `b-1=2r` retained starts and every
summand in (1.4) has absolute value at most one, which proves the second.
`square`

### Corollary 2.2 (signed families and boundary averaging)

Let `A` be any finite family of blocker sets, let `|c_J|<=1`, and let

\[
 T_s=\sum_{J\in A}c_J\Omega_s(J),\qquad
 \mathcal M(A)=\sum_{J\in A}\deg(J).                        \tag{2.4}
\]

Then

\[
 |T_s|\le2r\mathcal M(A),\qquad
 |T_r-T_{r-1}|\le2j\mathcal M(A).                           \tag{2.5}
\]

The same inequalities hold if every current is first averaged over a
probability space and multiplied by a sign of modulus one.

#### Proof

Apply (2.2), the triangle inequality, and then Jensen's inequality for the
optional average. `square`

## 3. The complete remote zero-avoidance tail

We record the application without suppressing its counting input.  After
the standard multiplication of cut labels by `-2 modulo b`, the blocker
graph is

\[
 B_r=\operatorname {Cay}(\mathbb Z_b,\{\mathord\pm1,
                                      \mathord\pm3\}),       \tag{3.1}
\]

with two edges punctured.  The two boundary-event roots are `p=0,q=5`.
For a blocker set `J`, write `V(J)` for its incident cuts.  The signed
boundary current vanishes unless `{p,q}` is contained in `V(J)`: if an
event-root pair is not split by a blocker, transposing its two positions
fixes the blocker constraints and reverses the harmonic sign.

Let `A_rem(t)` consist of all nonvanishing inclusion--exclusion blocker
sets except the sixteen four-vertex rooted atoms (ten two-edge matchings
and six matching-minus-path atoms).  The boundary-codegree estimate is

\[
 {\deg(J)\over D_M}\le C_0^{|J|}r^{2-|V(J)|},
 \qquad D_M=2r\,r!(r+1)!.                                  \tag{3.2}
\]

Here is the short summation needed below.  A bounded-degree exploration
from fixed roots has at most `A^m` connected `m`-edge shapes.  A connected
shape meeting both `p,q`, outside the six four-vertex paths, has at least
five vertices.  If the roots lie in separate components, the only
four-vertex possibility is a two-edge matching; every other rooted shape
again has at least five vertices.  Equations (3.2) and
`|J|<=2(|V(J)|-1)` therefore make the total weight of the nonlocal rooted
shape `O(D_M/r^3)`.

Additional components contain neither root.  Dropping mutual
vertex-disjointness only enlarges their sum.  A connected component with
`v` vertices has `O(rA^m)` placements and contributes the factor
`C_0^m r^{-v}` after the common `D_Mr^2` rooted normalization is removed.
The one-edge case is `O(1/r)`, and all larger cases form a convergent
geometric tail for large `r`.  The exponential formula hence multiplies
the rooted estimate by `exp(O(1/r))`.  If the rooted shape is one of the
sixteen four-vertex atoms but at least one additional component is present,
that added component itself supplies the missing `O(1/r)`.  Thus, uniformly
in the event shift,

\[
              \boxed{\mathcal M(A_{\rm rem}(t))
                     \le C D_M/r^3.}                        \tag{3.3}
\]

The finitely many `r` below the geometric-tail threshold are absorbed by
enlarging `C`.

Let `R_s(t)` be the signed inclusion--exclusion current of this remote
family, including the boundary-event probability average.  Corollary 2.2
and (3.3) give

\[
 |R_s(t)|\le {2CD_M\over r^2},
 \qquad
 |R_r(t)-R_{r-1}(t)|\le {2CjD_M\over r^3},                  \tag{3.4}
\]

which is (0.1) after changing the absolute constant.

In common/transverse coordinates

\[
 R_+(t)={R_r(t)+R_{r-1}(t)\over2},\qquad
 R_-(t)={R_r(t)-R_{r-1}(t)\over2},                          \tag{3.5}
\]

the conclusion is

\[
 |R_+(t)|=O(D_M/r^2),\qquad
 |R_-(t)|=O(jD_M/r^3).                                      \tag{3.6}
\]

For fixed `j`, the remote vector is therefore confined to an `O(1/r)`
cone around the common-shore line.  For `j` comparable with `r`, (3.6)
does not improve the old absolute estimate; the uniform all-depth transfer
still needs a depth-sensitive rooted-core argument.

## 4. Scope

The theorem is exact before blocker summation and is independent of the
number of blocker components.  It proves the missing shore-adapted
directional bound at every fixed depth, especially `j=2`.  It does not
control cancellation along the common-shore line and it does not certify a
nonzero determinant for the fully dressed two-column profile.  The next
finite calculation is the six-vertex rooted-core determinant at `j=2`;
the five-vertex truncation is insufficient and can have the opposite sign.
