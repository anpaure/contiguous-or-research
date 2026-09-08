# Gate A: root-containing connected stars are negligible on the disjoint carrier cell

**Date:** 2026-08-22  
**Status:** proved product-law theorem; removes the root-containing part of
every connected carrier kernel on the pairwise off-root-disjoint cell

## 0. Result

Fix an integer \(s\ge2\), a target \(v\), and distinct catalogue rows
\(F_1,\ldots,F_s\) through \(v\) which are pairwise disjoint away from \(v\). In the
root-containing part of the connected kernel \(K_s^\circ\), the Boolean
Möbius coefficient factors exactly:

\[
 \widehat g_{G,(F_1,\ldots,F_s)}^\circ([s])
 =p_v^{-1}\prod_{i=1}^s
       \{w((G\cap F_i)-\{v\})-1\},\qquad G\ni v.       \tag{0.1}
\]

Consequently, if \(D\) is the complete-catalogue degree of \(v\),
\(q_0\) is the unconditional survival probability of a row, and
\(z_v=Dq_0/p_v\) is the product-law mean degree conditional on retaining
\(v\), then

\[
 0\le {q_0K_{s,\mathrm{root}}^\circ(F_1,\ldots,F_s)\over z_v}
 \le R_s,                                                \tag{0.2}
\]

where \(R_s\) is the already-proved rooted overlap kernel

\[
 R_s=\max_F{1\over D}\sum_{G\ne F}
       \{x^{-s|(F\cap G)-\{v\}|}-1\}.                   \tag{0.3}
\]

If `x>=r^-alpha` with `s alpha<1/2`, Lemma C.3bis.1 therefore gives

\[
 \boxed{
 {q_0K_{s,\mathrm{root}}^\circ\over z_v}
 =O_s\!\left({1\over rx^{3s}}+{1\over r^2x^{4s}}\right).} \tag{0.4}
\]

For every \(2\le s\le12\), (0.4) is \(o(1)\) uniformly in the live
Gate-A range \(x\ge r^{-\alpha}\),
\(\alpha\le1/(256K)\), \(K\ge1\). This estimate is pointwise in the
carrier labels. It survives an arbitrary cutoff-tail tilt supported on
the disjoint cell and therefore incurs no division by a rare tail mass.

For \(s=2\), the dominant-cell determinant of G.18--G.19 may hence replace
the full kernel by its external-row part at a total \(o(z_v)\) cost after
the required multiplication by \(q_0\). The remaining external kernel is

\[
 K_{2,\mathrm{ext}}^\circ(F,H)
 =\sum_{\substack{G\not\ni v\\A,B\ne\varnothing}}
   \bigl[(w(A)-1)(w(B)-1)-1\bigr],                       \tag{0.5}
\]

where \(A=(G\cap F)-\{v\}\) and \(B=(G\cap H)-\{v\}\).
Thus the still-open dominant-cell problem is purely an external bridge-row
problem. This note does not control exceptional overlap cells or (0.5).

## 1. Setup

Use the complete directed-punctured catalogue \(\mathcal C_r\). Targets
are retained independently, with \(p_u\in\{x,y\}\), \(0<x\le y\le1\),
and

\[
 w(A)=\prod_{u\in A}p_u^{-1},\qquad
 q_0=x^{2r}y^{2r}.                                      \tag{1.1}
\]

Fix a root target \(v\). Every row through \(v\) has conditional survival
probability \(q_0/p_v\); hence, if its catalogue degree is \(D\),

\[
                         z_v={Dq_0\over p_v}.             \tag{1.2}
\]

For an integer \(s\ge2\) and an ordered \(s\)-tuple
\(\alpha=(F_1,\ldots,F_s)\) of distinct rows through \(v\), and a further
row \(G\ni v\), put

\[
 B_i=(G\cap F_i)-\{v\},\qquad
 B_I=\bigcup_{i\in I}B_i.                                \tag{1.3}
\]

The root-containing summand in G.15 is

\[
 g_G^\circ(I)=p_v^{-1}\{w(B_I)-1\},                     \tag{1.4}
\]

and its connected coefficient is

\[
 \widehat g_G^\circ([s])
 =\sum_{I\subseteq[s]}(-1)^{s-|I|}g_G^\circ(I).          \tag{1.5}
\]

Define

\[
 K_{s,\mathrm{root}}^\circ(\alpha)
 =\sum_{\substack{G\in\mathcal C_r\\v\in G}}
       \widehat g_G^\circ([s]).                          \tag{1.6}
\]

## 2. Exact factorization

Assume

\[
                         F_i\cap F_j=\{v\}\quad(i\ne j). \tag{2.1}
\]

Then the sets \(B_1,\ldots,B_s\) are pairwise disjoint. Therefore

\[
                         w(B_I)=\prod_{i\in I}w(B_i).     \tag{2.2}
\]

The constant \(-1\) in (1.4) has zero \(s\)-th Boolean difference, and
the elementary product identity

\[
 \sum_{I\subseteq[s]}(-1)^{s-|I|}
       \prod_{i\in I}z_i=\prod_{i=1}^s(z_i-1)            \tag{2.3}
\]

applied with \(z_i=w(B_i)\) proves (0.1). In particular every summand is
nonnegative.

If \(G=F_j\) for some \(j\), then \(B_i=\varnothing\) for every
\(i\ne j\), and the product in (0.1) is zero because \(s\ge2\). We may
therefore sum only over \(G\notin\{F_1,\ldots,F_s\}\).

## 3. Hölder bound

Put

\[
 h_i(G)=w((G\cap F_i)-\{v\})-1\ge0,\qquad
 t_i(G)=|(G\cap F_i)-\{v\}|.                            \tag{3.1}
\]

Hölder's inequality and extension of each nonnegative marginal sum give

\[
 {1\over D}\sum_{\substack{G\ni v\\
                 G\notin\{F_1,\ldots,F_s\}}}
       \prod_{i=1}^sh_i(G)
 \le\prod_{i=1}^s
 \left\{{1\over D}\sum_{\substack{G\ni v\\G\ne F_i}}
                    h_i(G)^s\right\}^{1/s}.             \tag{3.2}
\]

Because \(p_u\ge x\),

\[
 0\le h_i(G)\le x^{-t_i(G)}-1,
 \qquad h_i(G)^s\le x^{-s t_i(G)}-1.                    \tag{3.3}
\]

The second inequality uses \((a-1)^s\le a^s-1\) for \(a\ge1\).
Each factor in (3.2) is consequently at most \(R_s^{1/s}\). Combining
(0.1), (1.2), and (3.2) yields

\[
 {q_0K_{s,\mathrm{root}}^\circ(\alpha)\over z_v}
 ={1\over D}\sum_{G\ni v}\prod_{i=1}^sh_i(G)
 \le R_s,                                               \tag{3.4}
\]

which proves (0.2).

The rooted boundary-polymer estimate in Lemma C.3bis.1, used with its parameter
\(c=s\), states (provided \(s\alpha<1/2\)) that

\[
 R_s=O_s\!\left({1\over rx^{3s}}+{1\over r^2x^{4s}}\right). \tag{3.5}
\]

This proves (0.4). If \(x\ge r^{-\alpha}\), its two terms are
\(O_s(r^{-1+3s\alpha})\) and \(O_s(r^{-2+4s\alpha})\).
They are both \(o(1)\) when \(\alpha<1/(3s)\). For \(s\le12\), the live
assumption \(\alpha\le1/(256K)\), \(K\ge1\), is more than sufficient.

## 4. Consequence for the two-star determinant

Let \(F,H\) share only \(v\). In G.15.11 their off-root intersection
sets \(A,B\) are disjoint. Hence the root-row contribution is

\[
 K_{2,\mathrm{root}}^\circ(F,H)
 =p_v^{-1}\sum_{G\ni v}(w(A)-1)(w(B)-1),                \tag{4.1}
\]

whereas for \(G\not\ni v\),

\[
 w(A\cup B)-w(A)-w(B)
 =(w(A)-1)(w(B)-1)-1.                                   \tag{4.2}
\]

Equation (4.2) proves (0.5). By (0.4), every value of (4.1) lies in

\[
 \left[0,{z_v\over q_0}
 O\!\left({1\over rx^6}+{1\over r^2x^8}\right)\right]. \tag{4.3}
\]

For any two probability measures \(\mu,\nu\) supported on the disjoint
cell, including an arbitrary positive tail tilt of the factorial law,

\[
 q_0\left|\mathbb E_\mu K_{2,\mathrm{root}}^\circ
             -\mathbb E_\nu K_{2,\mathrm{root}}^\circ\right|
 \le z_v O\!\left({1\over rx^6}+{1\over r^2x^8}\right)
 =o(z_v).                                                \tag{4.4}
\]

No lower bound on the normalizing tail mass occurs in (4.4). Therefore
the arrangement-sensitive determinant on the dominant cell has, up to
an \(o(z_v)\) error at the required scale, only the external bridge kernel
(0.5). Exceptional overlap cells, the external kernel, and the later
stopped transfers remain open.

## 5. Exact finite audit

The script

    scratch/verify_gate_a_disjoint_root_star_suppression_20260822.py

constructs the complete \(r=3\) catalogue and, with rational two-shore
retention probabilities, checks (0.1) term by term for all \(4320\)
off-root-disjoint unordered pairs through a fixed middle root. It then
checks the Hölder conclusion (0.2) against the exact \(R_2\) sum. This is
an audit of the finite identities; the asymptotic estimate itself is the
analytic consequence of Lemma C.3bis.1 proved above.
