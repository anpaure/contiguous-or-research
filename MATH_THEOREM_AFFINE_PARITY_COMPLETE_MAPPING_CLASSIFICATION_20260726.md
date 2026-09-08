# Affine parity complete mappings: exact classification and a half-logarithmic trace ceiling

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The pointwise ownership equations in
`MATH_THEOREM_PARITY_COMPLETE_MAPPING_PAIRED_ORDER_LIFT_20260726.md`
have a large and completely explicit jointly affine family.  Label the
`r=2^t` coarse directions by the additive group

\[
                         G=\mathbb F_2^t
\]

and put `V=F_2^G`.  For linear maps `A,B:V -> G`, set

\[
                    d_p(x)=Ax+Bp+c.                 \tag{0.1}
\]

Write

\[
 \phi_A(u)=u+Ae_u,\qquad \psi_B(u)=u+Be_u.          \tag{0.2}
\]

Then (0.1) gives doubled-permutation coarse cycles and all the parity
complete-mapping equations if and only if `phi_A` is one `r`-cycle and
`psi_B` is a permutation of `G`.  Thus any cyclic ordering `phi` of `G`
and any permutation `psi` of `G` give a solution by declaring

\[
 Ae_u=u+\phi(u),\qquad Be_u=u+\psi(u).               \tag{0.3}
\]

In particular `psi=phi` gives a genuinely context-dependent solution for
`r>=4`.

However, every jointly affine solution has only one `t`-bit moving
syndrome.  At aligned coarse depth `d`, every nonempty physical trace fibre
has size at least

\[
                         2^{\,2d-t-1},                \tag{0.4}
\]

and the proportion of distinct aligned traces is at most

\[
                         {2r\over4^d}.                \tag{0.5}
\]

Consequently exact aligned trace injectivity is impossible once
`2d>t+1`, and asymptotic near-injectivity fails almost completely whenever

\[
                         d-\tfrac12\log_2 r\longrightarrow\infty. \tag{0.6}
\]

Affine Latin-square substitutions do not enlarge this class: after
absorbing their two invertible linear arguments into `A` and `B`, they are
again (0.1).  Hence the affine/linear route solves ownership and cycle
structure exactly but cannot reach a Gaussian protected window.  A
surviving construction must make the cyclic order itself depend on much
more than one affine direction syndrome.  The nonlinear double-factor
identity is not ruled out by this theorem.

## 1. Setup

Let `r=2^t`, identify the coordinate set of `Q_r` with `G=F_2^t`, and
write

\[
 V=\mathbb F_2^G,\qquad
 E=\{p\in V:\sum_{u\in G}p_u=0\},\qquad
 O=V\setminus E.                                    \tag{1.1}
\]

For `u in G`, let `e_u` denote the corresponding coordinate vector of
`V`.  Fix linear maps

\[
                         A,B:V\longrightarrow G      \tag{1.2}
\]

and `c in G`.  For `p in E` and `x in V`, define

\[
 d_p(x)=Ax+Bp+c,qquad F_p(x)=x+e_{d_p(x)},          \tag{1.3}
\]

and

\[
                         T_x(p)=p+e_{d_p(x)}.         \tag{1.4}
\]

The addition in the subscript of `e` is addition in `G`.  Define the two
coordinate permutations candidates

\[
 \phi_A(u)=u+Ae_u,qquad \psi_B(u)=u+Be_u.           \tag{1.5}
\]

## 2. Exact classification

### Theorem 2.1 (jointly affine classification)

The following are equivalent.

1. Every `F_p`, `p in E`, is a neighbour permutation all of whose cycles
   have length `2r` and a doubled-permutation direction word, and every
   `T_x:E -> O` is bijective.
2. The map `phi_A` is a single cycle of length `r` on `G`, and `psi_B` is
   a permutation of `G`.

When these conditions hold, the direction word on the `F_p`-cycle through
`x` is

\[
 s,\phi_A(s),\ldots,\phi_A^{r-1}(s),
 s,\phi_A(s),\ldots,\phi_A^{r-1}(s),                \tag{2.1}
\]

where `s=Ax+Bp+c`.

#### Proof

Fix `p` and abbreviate `c_p=Bp+c`.  If the current state is `x` and its
outgoing direction is

\[
                             s=Ax+c_p,
\]

then after that move the new direction is

\[
 A(x+e_s)+c_p=s+Ae_s=\phi_A(s).                     \tag{2.2}
\]

Suppose first that `phi_A` is an `r`-cycle.  The first `r` iterates in
(2.2) visit every coordinate exactly once, so after `r` moves the state is
`x+1`; the next `r` moves repeat the same direction order and return to
`x`.  No shorter positive prefix returns to `x`: before time `r` it has
toggled a nonempty proper set of distinct coordinates, and between times
`r` and `2r` it has toggled the complement of such a set.  Thus every
orbit has length `2r`, (2.1) holds, and `F_p` is a neighbour permutation.

Conversely, if one `F_p` has the asserted doubled-permutation cycles, then
(2.2), starting at any state, visits every member of `G` during its first
`r` moves.  Hence one orbit of `phi_A` contains all of `G`, so `phi_A` is
an `r`-cycle.  Notice also that this forces `A` to be onto.  Indeed, all
increments `u+phi_A(u)=Ae_u` lie in `im A`; if `im A` were proper, every
`phi_A`-orbit would remain in one coset of `im A`.

It remains to classify (1.4).  Assume that `psi_B` is injective.  If
`T_x(p)=T_x(p')` and the two selected directions are `u` and `v`, then,
unless `p=p'`,

\[
 p+p'=e_u+e_v,qquad
 u+v=B(p+p')=Be_u+Be_v.                              \tag{2.3}
\]

Equation (2.3) says `psi_B(u)=psi_B(v)`, contrary to injectivity.  Thus
`T_x` is injective; its two shores have the same finite cardinality, so it
is bijective.

For necessity, suppose `psi_B(u)=psi_B(v)` for distinct `u,v`.  Then

\[
                         Be_u+Be_v=u+v.               \tag{2.4}
\]

Since `A` is onto, choose `x` with `Ax+c=u`.  Put `p=0` and
`p'=e_u+e_v`, both in `E`.  Their selected directions at `x` are `u` and
`v`, respectively, and consequently

\[
 T_x(0)=e_u=T_x(e_u+e_v),                            \tag{2.5}
\]

contradicting bijectivity.  Hence `psi_B` is a permutation.  This proves
the equivalence. \(\square\)

### Corollary 2.2 (explicit nonconstant solutions)

Choose any `r`-cycle `phi` and any permutation `psi` of `G`, and define
`A,B` columnwise by (0.3).  Then (1.3) satisfies all the conclusions of
Theorem 2.1.

Taking `psi=phi` gives

\[
                         d_p(x)=A(x+p)+c.             \tag{2.6}
\]

For `r>=4` this is genuinely context dependent on the even shore.

#### Proof

The first assertion is immediate from Theorem 2.1.  If `A` vanished on
`E`, then `Ae_u=Ae_v` for all `u,v`, so `u+phi(u)` would be a constant
`a` and `phi(u)=u+a`.  Such a translation of an elementary abelian
2-group has cycles of length at most two and cannot be an `r`-cycle when
`r>=4`.  Thus `Ap` is nonconstant on `E`. \(\square\)

## 3. The affine trace ceiling

Assume the equivalent conditions of Theorem 2.1.  For `1<=d<r`, let

\[
 J_{p,d}(x)=\{d_p(x),d_p(F_px),\ldots,
                         d_p(F_p^{d-1}x)\}.           \tag{3.1}
\]

The aligned physical lower-trace code from the paired-order lift is

\[
 \mathcal C_d(p,x)=
       \bigl(J_{p,d}(x),x|_{J_{p,d}(x)^c},
                         p|_{J_{p,d}(x)^c}\bigr).    \tag{3.2}
\]

The upper code has the same form with the reversed interval.

### Theorem 3.1 (pointwise affine collision bound)

Every nonempty fibre of either aligned signed code has cardinality at
least

\[
                         2^{\max\{0,2d-t-1\}}.       \tag{3.3}
\]

Moreover

\[
 |\operatorname{im}\mathcal C_d|
       \le r\,2^{2(r-d)},                           \tag{3.4}
\]

and therefore its collision excess on `E x V` is at least

\[
 2^{2r-1}-r\,2^{2(r-d)}
       =2^{2r-1}\left(1-{2r\over4^d}\right).         \tag{3.5}
\]

#### Proof

By (2.1), `J_{p,d}(x)` is a length-`d` cyclic interval of the one fixed
oriented cycle `phi_A`.  For `d<r`, its underlying set uniquely determines
its first direction `s_J`: the unique member whose predecessor under
`phi_A` is outside the interval.

Fix a code value in the image, hence fix `J`, the outside coordinates of
`x`, and the outside coordinates of `p`.  The `2d` unknown inside bits
`(x|_J,p|_J)` satisfy

\[
 A_Jx_J+B_Jp_J
 =s_J+c+A_{J^c}x_{J^c}+B_{J^c}p_{J^c},              \tag{3.6}
\]

together with the one parity equation making `p` even.  This is a
consistent affine system of at most `t+1` independent binary equations.
Its solution space therefore has dimension at least `2d-t-1`.  Every
solution has initial direction `s_J`; recurrence (2.2) then gives exactly
the same interval `J`.  This proves (3.3).  Reversing the oriented cycle
gives the identical argument for the other sign.

There are exactly `r` length-`d` cyclic intervals of `phi_A`.  For each
one, the two outside restrictions in (3.2) have at most
`2^{2(r-d)}` values.  This proves (3.4).  Since
`|E x V|=2^{2r-1}`, subtraction proves (3.5). \(\square\)

### Corollary 3.2 (half-logarithmic no-go)

An aligned signed trace cannot be injective at depth `d` if

\[
                             2d>t+1.                  \tag{3.7}
\]

For a sequence of affine systems, if

\[
 d-\tfrac12\log_2r\longrightarrow\infty,            \tag{3.8}
\]

then the aligned trace collision excess is
`(1-o(1))2^{2r-1}`.  In particular, no jointly affine system supplies
near-injective aligned and half-step traces through a protected depth
`H` satisfying (3.8).

#### Proof

The first statement follows from (3.3), and the second from (3.5).
Failure of an aligned code already refutes simultaneous aligned/half-step
near-injectivity. \(\square\)

## 4. Affine and one-symbol Latin-square ansatzes

### Proposition 4.1 (affine Latin squares give nothing new)

Let

\[
                         L(z,w)=Pz+Qw+\ell            \tag{4.1}
\]

be an affine Latin operation on `G`, so `P,Q` are invertible.  If

\[
                         z=A_0x+a_0,\qquad w=B_0p+b_0,
\]

and `d_p(x)=L(z,w)`, then `d_p(x)` has the form (0.1), with

\[
                         A=PA_0,qquad B=QB_0.         \tag{4.2}
\]

Thus Theorems 2.1 and 3.1 classify this entire ansatz.

#### Proof

Expand (4.1) and collect its `x`, `p`, and constant terms. \(\square\)

There is a slightly broader entropy obstruction which is useful for a
nonlinear Latin square with only one `G`-valued context symbol.

### Proposition 4.2 (finite order-library bound)

Suppose the even contexts are assigned to `K` factor types.  Assume that
every type uses one common doubled cyclic direction order on all its
components.  Then at aligned depth `d<r`,

\[
 |\operatorname{im}\mathcal C_d|
       \le Kr\,2^{2(r-d)},                           \tag{4.3}
\]

so the distinct-trace proportion is at most

\[
                         {2Kr\over4^d}.               \tag{4.4}
\]

In particular, a one-symbol Latin construction with `K<=r` has negligible
distinct-trace proportion whenever `d-\log_2r -> infinity`.

#### Proof

Each type supplies only the `r` cyclic length-`d` intervals of its common
order.  Thus at most `Kr` direction sets occur.  After a direction set is
fixed, the two outside restrictions have at most `2^{2(r-d)}` values.
Divide the resulting image bound by `|E x V|=2^{2r-1}`. \(\square\)

## 5. Exact boundary

The affine construction proves that the ownership equation is not the
algebraic obstruction.  Its failure is precisely an information bottleneck:
one affine initial-direction syndrome has `t=log_2r` bits, while an aligned
depth-`d` physical trace erases `2d-1` free bits after the parity equation.

The theorem does **not** rule out a system in which the factor order itself
depends on a high-entropy nonlinear function of `p`.  In particular, the
same-vertex double-factor construction

\[
                         d_p(x)=\delta_0(Sp+x)         \tag{5.1}
\]

from `MATH_THEOREM_DOUBLE_FACTOR_AFFINE_PARITY_COMPLETE_MAPPING_20260726.md`
is outside the jointly affine direction-index ansatz unless `delta_0` is
affine as a map into the coordinate-label group.  Its recursive trace code,
or a genuinely many-symbol Latin recursion, is the minimum surviving
finite gate.
