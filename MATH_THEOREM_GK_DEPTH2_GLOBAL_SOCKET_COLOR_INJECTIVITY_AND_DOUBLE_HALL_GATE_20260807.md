# Global colour injectivity for GK depth-two sockets and the exact remaining double-Hall gate

**Date:** 2026-08-07  
**Status:** unconditional resource theorem.  It removes the feared global
collisions in the `a` and `B_y` banks for depth-two hinges.  It does not
construct the final 2-bounded path forest.

## 1. Setup

Let `U` be a Dyck word of semilength `m`, let `y(U)` be the downstep closing
its first primitive, and let `b` be an upstep from height one to height two
inside that first primitive.  Call `(U,b)` a **depth-two socket** and put

\[
 a(U,b)=U-\{1,b\},\qquad
 B_y(U,b)=a(U,b)+\{y(U)\}.                             \tag{1.1}
\]

For any downstep `x` in the excursion opened by `b`, the associated
depth-two root is

\[
 V=U-\{b\}+\{x\},\qquad B_x(U,b,x)=a(U,b)+\{x\}=X_V.  \tag{1.2}
\]

Different choices of `x` at one socket share `a` and `B_y`; the issue is
whether colours can also collide between different sockets.

## 2. The `a` bank is globally injective

## Theorem 2.1

The map

\[
                         (U,b)\longmapsto a(U,b)       \tag{2.1}
\]

is injective over all depth-two sockets in `D_m`.

### Proof

Suppose

\[
              a(U,b)=a(U',b')=:a.
\]

Then

\[
              U=a+\{1,b\},\qquad U'=a+\{1,b'\}.       \tag{2.2}
\]

If `b<b'`, the two words agree before `b`.  In `U`, the step `b` starts at
height one and goes upward.  In `U'`, the same position is a downstep, so
it goes from height one to height zero and closes the first primitive.
Consequently the later position `b'` lies outside the first primitive of
`U'`, contradicting that `b'` is a depth-two opener there.  The case
`b'>b` with the roles reversed is identical.  Hence `b=b'`, and (2.2)
then gives `U=U'`. \(\square\)

## 3. The unused `B_y` bank is globally injective

## Theorem 3.1

The map

\[
                         (U,b)\longmapsto B_y(U,b)     \tag{3.1}
\]

is also injective over all depth-two sockets.

### Proof

Let `C=B_y(U,b)` and inspect its height path.  Relative to `U`, the two
upsteps at positions `1,b` have been changed downward and the downstep at
`y=y(U)` has been changed upward.  Therefore

\[
H_C(t)=
\begin{cases}
H_U(t)-2,&1\le t<b,\\
H_U(t)-4,&b\le t<y,\\
H_U(t)-2,&t\ge y.
\end{cases}                                            \tag{3.2}
\]

Before `b`, the first primitive of `U` is positive, so `H_C>=-1`.
Between `b` and `y`, the path `U` has height at least one, and immediately
before `y` it has height one.  Hence `H_C>=-3` there and
`H_C(y-1)=-3`.  From `y` onward, `H_U>=0`, so `H_C>=-2`.

It follows that `-3` is the global minimum of `C`, and `y` is the unique
last step that leaves that global minimum upward.  Thus `y` is recoverable
from `C` alone.  Removing it recovers

\[
                            a=C-\{y\}.                 \tag{3.3}
\]

Theorem 2.1 then recovers `(U,b)` uniquely. \(\square\)

## 4. Exact collision reduction

Let `F` be any set of simple depth-two arcs.  Then:

1. all `a` colours in `F` are distinct exactly when `F` uses at most one
   choice of `x` at each socket `(U,b)`;
2. under the same socket condition, all `B_y` colours are automatically
   distinct;
3. all `B_x` colours are distinct exactly when no two selected arcs have
   the same target root `V`, because `B_x=X_V`.

Thus the root-level rainbow problem reduces exactly to two capacities:

\[
 \boxed{
 \text{socket capacity }1
 \quad+\quad
 \text{target-root capacity }1.}                       \tag{4.1}
\]

The separate global `a`-rainbow and `B_y`-rainbow Hall systems disappear.

If physical owner degree at most two is also imposed, the exact selector
network is

\[
  s\longrightarrow U\;(\text{capacity }2)
   \longrightarrow (U,b)\;(\text{capacity }1)
   \longrightarrow V\;(\text{capacity }1)
   \longrightarrow t,                                  \tag{4.2}
\]

where `(U,b)->V` is present precisely for the legal choices of `x` in the
excursion opened by `b`.

Integral max flow in (4.2) is therefore the exact root-level
socket/target selector.  No relaxation or extra colour coordinate is
hidden in this reduction.

## 5. Sharp topological boundary

The simple depth-two root graph is connected and `(m-1)`-regular, but the
orientation in (1.2) is acyclic.  Its sinks are the `Cat_{m-1}` words
`10A`, and its vertices with no incoming arc are the `Cat_{m-1}` primitive
words `1A0`.

A capacity-faithful directed path cover would therefore be optimal if it
had exactly

\[
                          \operatorname {Cat}_{m-1}    \tag{5.1}
\]

paths.  Equivalently, the source-capacity-one restriction of (4.2) would
need a matching from every nonsink root onto every nonprimitive root.
This holds in the finite audited layers but is not proved here for all
`m`.

Even the optimal value (5.1) is only asymptotically the four-sector
threshold:

\[
 {\operatorname {Cat}_{m-1}\over\operatorname {Cat}_m}
 ={m+1\over2(2m-1)}
 ={1\over4}+{3\over8m}+O(m^{-2}).                      \tag{5.2}
\]

Hence one free-orientation pass cannot by itself give a strict
`<1/4` component ratio.  A second, much smaller bank of legal peak joins,
a conjugate orientation, or a bounded rethread must merge

\[
 {3\over8m}\operatorname {Cat}_m+O(\operatorname {Cat}_m/m^2) \tag{5.3}
\]

additional components to cross the strict threshold.

## 6. Exact remaining lemma

After Theorems 2.1 and 3.1, the smallest root-level statement sufficient
for strict four-sector contraction is:

> **Depth-two double-Hall contraction lemma.**  The network (4.2), possibly
> augmented by one fixed conjugate socket bank, contains a degree-two path
> forest with more than `3 Cat_m/4` edges, and its endpoint state regenerates
> under the same-parity lift.

The only literal resources still needing proof are target facets and owner
degree.  The two lower colour banks are already exact and private.
