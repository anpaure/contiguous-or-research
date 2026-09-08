# Leaf-tensored q2-neutral PBBS profile descent

**Date:** 2026-08-05  
**Method:** symbolic block extension of the parametric common-pivot C6  
**Status:** unconditional for `t>=2`, `ell>=1`, `h>=t+3`.  It extends the
three-sector q2-neutral descent to partitions with an arbitrary singleton
tail.  It still gives one action-profile hyperedge, not angle-level
expansion.

## 1. Construction

Put

\[
                         m=h+t+\ell+1.
\]

On a cyclic binary word of length `2m+1`, choose the deficit-three core
`H` with block decomposition

\[
 0_{a_0}(10)^\ell\,
 0_{a_1}(1^t0^t)\,
 0_{a_2}(1^h0^h).
\tag{1.1}
\]

Let `c` be the first down-step and `d` the second down-step of the final
height-`h` mountain.  Let `K` be the complement of
`H+{a_0,a_1,a_2,c}`.  Define

\[
 R_i=K+a_i,quad P_i=K+a_i+a_{i+1},quad
 Q_i=K+a_i+c,quad L_i=P_i-d.
\tag{1.2}
\]

All ranks are the clean-C6 ranks: `|H|=m-1`, `|K|=m-2`.

## 2. PBBS and common-pivot verification

For `Z_i=H+a_i`, the normalized Dyck shapes are

\[
\begin{aligned}
 D(Z_0)&=(1^h0^h)\,1(10)^\ell0\,(1^t0^t),\\
 D(Z_1)&=(10)^\ell\,1(1^t0^t)0\,(1^h0^h),\\
 D(Z_2)&=(1^t0^t)\,1(1^h0^h)0\,(10)^\ell.
\end{aligned}
\tag{2.1}
\]

The final mountain is uniquely responsible for the rightmost global
maximum, so its first down-step `c` is the reverse survivor in all three
states.  The forward survivors cycle through the `a_i`.  Therefore the
old PBBS shore is `P_i->Q_i`, exactly as in the untensored construction.

For the three predecessor states `X_i=f^(-1)(P_i)`, cutting at their
forward roots gives

\[
\begin{aligned}
 D(X_0)&=1^{h+1}0^h(10)^\ell0(1^t0^t),\\
 D(X_1)&=1^h0^{h-1}1(10)^\ell0(1^t0^t)0,\\
 D(X_2)&=(1^h0^h)(10)^\ell1(1^t0^t)0.
\end{aligned}
\tag{2.2}
\]

The first maxima have heights `h+1,h,h`.  Every later competitor has
height at most `max(2,t)`, `max(3,t+1)`, and `max(1,t+1)`, respectively.
Under `h>=t+3`, the reverse survivor of every `X_i` is therefore the first
post-maximum down-step `d`.  Hence

\[
                         P_i\cap f^{-2}(P_i)=P_i-d=L_i.
\tag{2.3}
\]

The clean switch `P_iQ_i -> P_iQ_(i+1)` is consequently q2-neutral by the
common-deletion theorem.

## 3. Action profiles and descent

Peak-pruning applied to (2.1) gives the three soliton partitions

\[
 \boxed{
 (h,t,2,1^{\ell-1}),qquad
 (h,t+1,1^\ell),qquad
 (h+1,t,1^\ell).}
\tag{3.1}

They are pairwise distinct for `t>=2`.  Their top gaps are at least two,
so all six relevant q1 occurrences are uniquely max-height selected, and
the three old edges lie on three distinct PBBS components.  The C6 merges
those components while preserving q1 and q2.

For

\[
                         \Psi(\lambda)=\sum_j\binom{\lambda_j}{2},
\]

the successive differences from the first partition in (3.1) to the
second, and from the second to the third, are

\[
                         t-1,qquad h-t,
\tag{3.2}
\]

both positive.  Thus singleton tails do not obstruct strict q2-neutral
profile descent.

When `t=1`, the first two profiles in (3.1) coincide.  The literal C6 and
q2-neutrality remain valid, but action profiles alone no longer prove that
its two corresponding old edges lie on distinct angle components; no
three-component topology claim is made in that boundary case.
