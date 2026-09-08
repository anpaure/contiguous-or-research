# Arbitrary-tail q2-neutral PBBS profile descent

**Date:** 2026-08-05  
**Method:** rooted-Dyck factorization, peak pruning, and the clean-C6
common-deletion criterion; no computation or search  
**Status:** unconditional.  An arbitrary Dyck tail of height strictly below
the middle mountain can be carried through the parametric PBBS connector.
The resulting clean C6 is selected, q2-neutral, and genuinely
three-component.  The equal-height boundary remains an angle-level problem.

## 1. The block template

Let `E` be any Dyck word of semilength `ell` and height `e`.  Fix integers

\[
                 0\le e<t,\qquad h\ge t+3,
\tag{1.1}
\]

and put

\[
                 m=\ell+t+h+1,\qquad n=2m+1.
\tag{1.2}
\]

Choose a cyclic deficit-three word `H` with its forward-unmatched zeros
displayed as

\[
 0_{a_0}\,E\;0_{a_1}\,(1^t0^t)\;
 0_{a_2}\,(1^h0^h).
\tag{1.3}
\]

Let `c` and `d` be respectively the first and second down-steps of the
final height-`h` mountain.  Let `K` be the complementary rank-`(m-2)`
core determined by

\[
 [n]=H\mathbin{\dot\cup}K\mathbin{\dot\cup}
          \{a_0,a_1,a_2,c\}.
\tag{1.4}
\]

With subscripts modulo three, define

\[
 R_i=K+a_i,\qquad P_i=K+a_i+a_{i+1},\qquad
 Q_i=K+a_i+c,\qquad L_i=P_i-d.
\tag{1.5}
\]

## 2. The old shore is PBBS

Put `Z_i=H+a_i`.  Flipping one forward-unmatched zero consumes it and the
next unmatched zero, so the remaining one is the forward survivor.  The
three normalized rooted shapes are

\[
\begin{aligned}
 D(Z_0)&=(1^h0^h)\,1E0\,(1^t0^t),\\
 D(Z_1)&=E\,1(1^t0^t)0\,(1^h0^h),\\
 D(Z_2)&=(1^t0^t)\,1(1^h0^h)0\,E.
\end{aligned}
\tag{2.1}
\]

Their displayed maximal factors have heights respectively

\[
 h,\qquad h,\qquad h+1.
\tag{2.2}
\]

Every competing factor has height at most `t+1`.  By (1.1), the displayed
maximum is strict in all three shapes, and its rightmost maximum is followed
by the coordinate `c`.  The reverse cycle lemma therefore gives

\[
 r_-(Z_i)=c.
\tag{2.3}
\]

Together with the forward survivors, the PBBS formulas give

\[
 f(Z_i)=Q_{i+1},\qquad f^{-1}(Z_i)=P_{i+1}.
\tag{2.4}
\]

Thus the centered PBBS factor contains all three directed old edges

\[
                         P_i\longrightarrow Q_i.
\tag{2.5}
\]

## 3. The companion deletion is the same coordinate

The predecessor states `X_i=f^{-1}(P_i)` have, after cutting at their
forward roots, the following shapes:

\[
\begin{aligned}
 D(X_0)&=1^{h+1}0^h\,E\,0\,(1^t0^t),\\
 D(X_1)&=1^h0^{h-1}\,1E0\,(1^t0^t)\,0,\\
 D(X_2)&=(1^h0^h)\,E\,1(1^t0^t)0.
\end{aligned}
\tag{3.1}
\]

The initial mountain pieces have heights `h+1,h,h`.  The later pieces
have heights at most

\[
 \max(e,t),\qquad \max(e+2,t),\qquad \max(e,t+1),
\tag{3.2}
\]

respectively.  Conditions (1.1) make all three initial maxima strict.  In
each word the coordinate following the rightmost maximum is `d`.  Hence

\[
                         r_-(X_i)=d
\tag{3.3}
\]

and a second inverse PBBS step gives

\[
             P_i\cap f^{-2}(P_i)=P_i-d=L_i.
\tag{3.4}

Thus the three unchanged companion rows delete one common core coordinate.

## 4. Selection and component separation

Let `beta` denote the peak-pruning profile and put

\[
 b=\beta(E)+\beta(1^t0^t)+\beta(1^h0^h).
\tag{4.1}
\]

Wrapping a Dyck word of height `q` contributes one box in pruning layer
`q+1`.  Therefore the three action profiles of the centers in (2.1) are

\[
             b+e_{e+1},\qquad b+e_{t+1},\qquad b+e_{h+1}.
\tag{4.2}

They are pairwise different because `e<t<h`.  Their conjugate soliton
partitions have top two parts separated by at least

\[
                         h-(t+1)\ge2.
\tag{4.3}

The soliton-gap forcing theorem consequently puts every edge of all three
PBBS components into every max-height q1 section.  In particular all three
rows `R_i` and all three companions `L_i` in (1.5) are selected.  Since the
profiles (4.2) differ, the three old edges lie on three distinct PBBS
components.

## 5. Exact q2 neutrality and descent

Equation (3.4) is precisely the common-deletion hypothesis for a clean
C6.  Hence the switch

\[
                         P_iQ_i\longmapsto P_iQ_{i+1}
\tag{5.1}
\]

preserves the q1 intersection multiset, preserves every immediate upper
colour edgewise, and rotates the only changed q2 turns:

\[
 (K-d+a_0,K-d+a_1,K-d+a_2)
 \longmapsto
 (K-d+a_1,K-d+a_2,K-d+a_0).
\tag{5.2}

Because the three old edges lie on distinct cycles, the switch merges
those cycles into one.

For a soliton partition `lambda`, set

\[
                         \Psi(\lambda)=\sum_j\binom{\lambda_j}{2}.
\tag{5.3}
\]

The three siblings in (4.2) are obtained by extending a part of length
`e`, `t`, or `h`.  Consequently their `Psi` values differ successively by

\[
                         t-e>0,\qquad h-t>0.
\tag{5.4}

Thus (5.1) is a strict q2-neutral action-profile descent triangle for an
arbitrary carried tail `E`.

## 6. Consequence and exact boundary

The earlier parametric theorem is the case `E=empty`; the leaf-tensored
theorem is the case `E=(10)^ell`.  The present result shows that neither
the detailed leaf positions nor the lower soliton partition are an
obstruction: every tail whose largest part is strictly below `t` passes
unchanged through the connector.

The condition `e<t` is the exact point at which the proof obtains three
different action profiles.  If `e=t`, the first two profiles in (4.2)
coincide.  The literal PBBS and common-pivot calculations still go through
under the same height margin, but action content no longer decides whether
the two equal-profile old edges lie on different angle tori.  Resolving
that equality boundary is therefore a pure action-angle displacement
problem, not a q1/q2 or max-height problem.

