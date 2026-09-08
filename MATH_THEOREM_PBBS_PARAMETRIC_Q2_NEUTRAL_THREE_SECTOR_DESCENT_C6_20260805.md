# A parametric q2-neutral PBBS C6 with strict action-profile descent

**Date:** 2026-08-05  
**Method:** literal cyclic-parenthesis algebra; no computation or search  
**Status:** unconditional for integers `t>=1` and `h>=t+3`.  The connector
lies on three distinct, wholly max-height-selected PBBS components and
preserves the selected q2 multiset exactly.  It supplies a strict descent
triangle in the action-profile quotient.  It does not prove angle-level
quotient expansion or a spanning loose forest.

## 1. Literal family

Put

\[
 m=t+h+1,qquad n=2m+1,
\tag{1.1}
\]

and work on cyclic coordinates `{0,1,...,2m}`.  Define

\[
 a_0=0,quad a_1=1,quad a_2=2t+2,quad
 g=2t+3,quad c=2t+h+3,quad d=c+1.
\tag{1.2}
\]

Let

\[
\begin{aligned}
 A&=\{2,\ldots,t+1\},&
 B&=\{t+2,\ldots,2t+1\},\\
 C&=\{g,\ldots,c-1\},&
 E&=\{d,\ldots,2m\}.
\end{aligned}
\tag{1.3}
\]

Thus `|A|=|B|=t`, `|C|=h`, `|E|=h-1`.  Put

\[
                         H=A\cup C,qquad K=B\cup E.
\tag{1.4}
\]

Then `|H|=m-1`, `|K|=m-2`, and the ground set is the disjoint union

\[
 H\mathbin{\dot\cup}K\mathbin{\dot\cup}
 \{a_0,a_1,a_2,c\}.
\tag{1.5}
\]

As usual, with subscripts modulo three, define

\[
 R_i=K+a_i,quad
 P_i=K+a_i+a_{i+1},quad
 Q_i=K+a_i+c,quad
 L_i=P_i-d.
\tag{1.6}
\]

## 2. The three old edges are PBBS edges

The deficit-three decomposition of `H` is

\[
 0_{a_0}\,\varnothing\,
 0_{a_1}(1^t0^t)\,
 0_{a_2}(1^h0^h).
\tag{2.1}
\]

Let `Z_i=H+a_i`.  Flipping one of the three unmatched zeros makes
`a_(i+2)` the forward survivor.  Because `h>=t+3`, the rightmost global
maximum in every normalized `Z_i` lies in the displayed height-`h`
mountain and is followed by `c`.  More explicitly the normalized Dyck
shapes are

\[
\begin{aligned}
 D(Z_0)&=(1^h0^h)(10)(1^t0^t),\\
 D(Z_1)&=1(1^t0^t)0(1^h0^h),\\
 D(Z_2)&=(1^t0^t)1(1^h0^h)0.
\end{aligned}
\tag{2.2}
\]

Their unique highest pieces have respective heights `h`, `h`, and
`h+1`, and the post-maximum down-step is `c` in all three cases.  Hence

\[
 r_+(Z_i)=a_{i+2},qquad r_-(Z_i)=c.
\tag{2.3}
\]

The forward and inverse PBBS formulas now give

\[
 f(Z_i)=K+c+a_{i+1}=Q_{i+1},
 \qquad
 f^{-1}(Z_i)=K+a_{i+1}+a_{i+2}=P_{i+1}.
\tag{2.4}
\]

Thus the centered PBBS factor contains all three directed edges

\[
                         P_i\longrightarrow Q_i.
\tag{2.5}
\]

## 3. The companion deletion is the common pivot `d`

Define three middle states

\[
\begin{aligned}
 X_0&=A\cup C\cup\{c\},\\
 X_1&=\{a_0\}\cup A\cup(C-\{g\})\cup\{c\},\\
 X_2&=\{a_1\}\cup A\cup(C-\{g\})\cup\{c\}.
\end{aligned}
\tag{3.1}
\]

Their forward roots and normalized Dyck shapes are

\[
\begin{array}{c|c|c}
 &r_+&D\\ \hline
X_0&a_2&(1^{h+1}0^{h+1})(1^t0^t)\\
X_1&g&1^h0^{h-1}\,10\,1^t0^t\,0\\
X_2&g&(1^h0^h)(1^{t+1}0^{t+1}).
\end{array}
\tag{3.2}
\]

The displayed words are Dyck.  Their rightmost global maxima occur at the
end of the first one-run and are followed by `d`: the competing later
heights are respectively `t`, `t+1`, and `t+1`, all strictly below the
first heights `h+1,h,h`.  Therefore

\[
                         r_-(X_0)=r_-(X_1)=r_-(X_2)=d.
\tag{3.3}
\]

Also `X_i^c=P_i+r_+(X_i)`, so the forward formula gives

\[
                         f(X_i)=P_i,qquad X_i=f^{-1}(P_i).
\tag{3.4}
\]

Applying the inverse formula once more and intersecting with `P_i` gives

\[
 f^{-2}(P_i)\cap P_i=P_i-d=L_i.
\tag{3.5}
\]

Thus all three unchanged companion q1 rows delete the one common core
coordinate `d`.

## 4. All six occurrences are forced selected

Peak-pruning additivity applied to (2.2) gives the three action profiles,
or equivalently soliton partitions,

\[
 \boxed{
 (h,t,1),qquad (h,t+1),qquad (h+1,t).}
\tag{4.1}
\]

Their largest-minus-second-largest gaps are

\[
 h-t,\qquad h-t-1,qquad h+1-t,
\tag{4.2}
\]

all at least two under `h>=t+3`.  The soliton-gap forcing theorem therefore
says that every factor edge in all three components is the unique
max-height occurrence of its q1 colour.  In particular the three old rows
`R_i` and the three companion rows `L_i` all belong to every max-height
q1 section.

The profiles in (4.1) are pairwise distinct, so the three old edges lie on
three distinct PBBS components.

## 5. Exact q2 neutrality and topology

The clean switch

\[
                         P_iQ_i\longmapsto P_iQ_{i+1}
\tag{5.1}
\]

preserves each upper q1 colour and cyclically transports the lower q1 rows
`R_i`.  Equation (3.5) is exactly the common-deletion condition, so its
only changed q2 turns are

\[
 (K-d+a_0,K-d+a_1,K-d+a_2)
 \longmapsto
 (K-d+a_1,K-d+a_2,K-d+a_0).
\tag{5.2}
\]

Thus the selected q2 multiset is unchanged.  Since the old edges lie on
three distinct cycles, (5.1) merges those cycles into one.

## 6. A strict quotient potential

For a soliton partition `lambda`, put

\[
 \Psi(\lambda)=\sum_j\binom{\lambda_j}{2}
 =\sum_{s\ge1}(s-1)a_s.
\tag{6.1}
\]

Writing

\[
 \lambda_A=(h,t,1),\quad
 \lambda_B=(h,t+1),\quad
 \lambda_C=(h+1,t),
\]

the connector satisfies

\[
 \Psi(\lambda_B)-\Psi(\lambda_A)=t,
 \qquad
 \Psi(\lambda_C)-\Psi(\lambda_B)=h-t.
\tag{6.2}
\]

Both differences are positive.  Hence every member of this parametric
family is a strict action-profile descent triangle

\[
                   (h+1,t)\quad\longrightarrow\quad
                   (h,t+1)\quad\longrightarrow\quad
                   (h,t,1).
\tag{6.3}
\]

The arrows in (6.3) orient the vertices of the quotient hyperedge toward
lower `Psi`; they do not assert that PBBS time evolution changes its
invariant soliton partition.

This gives a genuine q2-neutral analogue of the earlier unrestricted
profile-descent move.  It also shows that soliton content and the convex
energy `Psi` are not invariants of q2-neutral common-pivot connectivity.

What remains is angle-level expansion: the theorem gives at least one
three-component hyperedge between the displayed sectors, but it does not
show that every action torus in a sector has a suitably placed literal
copy, nor that copies admit a physically disjoint spanning loose forest.
