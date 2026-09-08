# Complete inverse-pair rail potentials determine their ordered banks

**Date:** 2026-08-06  
**Method:** pure reconstruction from the signed basis vectors  
**Status:** unconditional rigidity theorem for semilength at least four.
It rules out the simplest sheet-detachment of a current cycle, but not a
branched multi-current absorber.

## 1. The endpoint potential

Put

\[
                         p=m-2\ge2.                   \tag{1.1}
\]

Let

\[
 X=(x_1,\ldots,x_p),\qquad
 Y=(y_1,\ldots,y_{p+1})                               \tag{1.2}
\]

be disjoint ordered banks, and let `z` lie outside both.  Write `X_j^-`
and `X_j^+` for the prefix and suffix of length `j`, and similarly for
`Y`.  Define the complete signed endpoint potential

\[
 F_{X,Y}(z)=\bigl(F_j(z)\bigr)_{1\le j\le p},          \tag{1.3}
\]

where

\[
 F_j(z)=
 [Y_j^-+z]-[Y_j^++z]+[X_j^-+z]-[X_j^++z].            \tag{1.4}
\]

The complete current of an inverse-pair move with active endpoints `a,d`
is

\[
                  \mathcal D(X,Y;a,d)
                    =F_{X,Y}(a)-F_{X,Y}(d).           \tag{1.5}
\]

## 2. Reconstruction theorem

### Theorem 2.1 (rail-potential rigidity)

For `p>=2`, the value of `F_(X,Y)(z)` determines both ordered banks `X`
and `Y` uniquely.

#### Proof

At depth `j=p`, the two `X` terms cancel, so

\[
 F_p(z)=[(Y-\{y_{p+1}\})+z]
          -[(Y-\{y_1\})+z].                          \tag{2.1}
\]

The two displayed sets are distinct.  The signed basis vector therefore
recovers them individually.  Their union is `Y`; their two set differences
recover the ordered endpoints `y_1` and `y_(p+1)`, while their intersection
recovers the interior of `Y` as a set.

Now use `j=p-1`.  Among the four basis sets in (1.4), exactly two have
their non-`z` part contained in the already recovered set `Y`; these are
the signed `Y` prefix and suffix.  The other two are the signed `X` prefix
and suffix.  They cannot cancel with a `Y` term because the banks are
disjoint.  Their union recovers `X`, and their signs distinguish

\[
                   X-\{x_p\}\quad\hbox{from}\quad
                   X-\{x_1\}.                        \tag{2.2}
\]

Thus both underlying banks and both of their ordered endpoints are known.

For every smaller `j`, each term of (1.4) is now classified uniquely by
whether its non-`z` part lies in `X` or in `Y`, and its sign distinguishes
prefix from suffix.  Hence all prefixes

\[
 X_1^-,X_2^-,\ldots,X_{p-1}^-,qquad
 Y_1^-,Y_2^-,\ldots,Y_p^-                             \tag{2.3}
\]

are recovered.  Successive set differences of (2.3) recover the entries
of both ordered banks one by one.  \(\square\)

The restriction `p>=2` is sharp for this argument.  At semilength three,
`X` has one entry and cancels from the sole nonzero endpoint potential.

## 3. Consequence for current-cycle detachment

Consider a directed active-label cycle

\[
 z_0\longrightarrow z_1\longrightarrow\cdots
 \longrightarrow z_{t-1}\longrightarrow z_0,         \tag{3.1}
\]

and give its edge `i` an ordered profile `(X_i,Y_i)`.  Its current is

\[
 F_{X_i,Y_i}(z_{i+1})-F_{X_i,Y_i}(z_i).               \tag{3.2}
\]

Suppose cancellation is capacity-one at every active label: the positive
potential entering `z_i` is literally equal to the unique negative
potential leaving `z_i`.  Then

\[
                  F_{X_{i-1},Y_{i-1}}(z_i)
                  =F_{X_i,Y_i}(z_i).                  \tag{3.3}
\]

### Corollary 3.1 (no simple profile-changing cycle)

Under the capacity-one hypothesis above and `m>=4`, every edge of (3.1)
has the same ordered profile `(X,Y)`.

#### Proof

Apply Theorem 2.1 to (3.3) at each vertex and propagate around the cycle.
\(\square\)

Thus the obvious attempt to detach the `D_3` automorphism square by giving
successive edges different private tail sheets cannot work while retaining
one-in/one-out literal rail cancellation.  Complete current equality at a
shared active label forces those sheets back to the same ordered banks,
and the central multiplicities of the square remain.

The theorem does **not** rule out:

1. a branched cancellation in which several potentials sum at one label;
2. a packet whose extra rows absorb part of the rail current;
3. a dynamic slot transport with a nontrivial intermediate current; or
4. a bounded terminal residual rather than exact zero.

It identifies the next construction as a genuinely branched or stateful
absorber, not a simple covering of the four-edge cocycle.
