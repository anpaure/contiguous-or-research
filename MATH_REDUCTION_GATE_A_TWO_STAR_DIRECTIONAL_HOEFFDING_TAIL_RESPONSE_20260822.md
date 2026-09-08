# Gate A: the first punctured two-star splits into a rooted-position profile and a pair-connected tail response

**Date:** 2026-08-22  
**Status:** exact product-law reduction at the literal carrier order
\(m=12\); both resulting boundary estimates remain open

## 0. Outcome

The first term in the punctured Möbius hierarchy is the signed two-star
kernel \(K(F,H)\), where a further row meets both root-carrier rows
\(F,H\) away from their common root.  This note sums its tail decoration
one step further without making a false transitivity assumption.

A fixed root target can occupy different positional roles in a punctured
row.  Consequently the survival-weighted mean of \(K(F,H)\) over the
second carrier \(H\) need not be constant as a function of the rooted flag
\((v,F)\).  Define this exact one-body profile by

\[
 a(F)={\sum_{H\ne F}q_{FH}K(F,H)\over
             \sum_{H\ne F}q_{FH}},                        \tag{0.1}
\]

where \(q_{FH}\) is the probability that both rows survive.  For a
nonnegative degree weight \(g(d)\), define the conditional pair profile

\[
 L_g(F,H)=\mathbb E[g(d_v)\mid F,H\text{ survive}]          \tag{0.2}
\]

and its conditional second-carrier average

\[
 \ell_g(F)={\sum_{H\ne F}q_{FH}L_g(F,H)\over
                  \sum_{H\ne F}q_{FH}}.                   \tag{0.3}
\]

Then the exact pair average splits as

\[
 \boxed{
 {\sum_{F\ne H}q_{FH}K(F,H)L_g(F,H)\over
       \sum_{F\ne H}q_{FH}L_g(F,H)}
 =\mathbb E_{\omega_g}a(F)+\mathcal C_g,}                 \tag{0.4}
\]

where

\[
 \omega_g(F)\ \propto\
 \mathbb E[\mathbf1_{\{F\text{ survives}\}}(d_v-1)g(d_v)] \tag{0.5}
\]

and

\[
 \boxed{
 \mathcal C_g=
 {\sum_{F\ne H}q_{FH}\{K(F,H)-a(F)\}
          \{L_g(F,H)-\ell_g(F)\}\over
       \sum_{F\ne H}q_{FH}L_g(F,H)}.}                     \tag{0.6}
\]

The residual in (0.6) is directionally canonical: its kernel has zero
weighted sum over \(H\) for every fixed \(F\), and its tail profile has
the same property.  Thus every contribution to \(\mathcal C_g\) needs a
genuine second-carrier dependence on both sides.

At \(m=12\), use

\[
 g_{12}(d)=(d-2)_{10},\qquad
 g_c(d)={(d-c)_+^{12}\over(d)_2},                          \tag{0.7}
\]

with both functions set to zero when their displayed combinatorial
denominator or extension count is unavailable.  If \(\lambda_{12}\) is
the factorial-Palm state tilt and \(\lambda_c\) is the normalized tail
state tilt, then

\[
 \boxed{
 \mathbb E_{\lambda_{12}}\overline K_2
       -\mathbb E_{\lambda_c}\overline K_2
 =\{\mathbb E_{\omega_{12}}a-\mathbb E_{\omega_c}a\}
       +\{\mathcal C_{12}-\mathcal C_c\}.}                 \tag{0.8}
\]

This is a sharper and honest description of the first open cluster.  It
does **not** say that only the fully connected residual (0.6) remains:
the rooted-position term in braces in (0.8) is also live.  A proof must
bound their signed combination, or prove enough cancellation between it
and the higher \(s\)-star terms.

## 1. Product law and the two-star kernel

Put \(b=2r+1\).  A target is a tagged subset of \([b]\), either a middle
target of size \(r\) or a lower target of size \(r-1\).  For a permutation
\(w=(w_0,\ldots,w_{b-1})\), read indices cyclically and define

\[
 E(w)=\{(M,\{w_i,\ldots,w_{i+r-1}\}):1\le i<b\}
 \mathbin{\dot\cup}
 \{(L,\{w_i,\ldots,w_{i+r-2}\}):1\le i<b\}.       \tag{1.1}
\]

Let \(\mathcal C_r\) be the complete catalogue of these rows.  Retain
targets independently with shore probabilities \(p_u\), and write

\[
 q_0=\prod_{u\in G}p_u=x^{2r}y^{2r},\qquad
 w(A)=\prod_{u\in A}p_u^{-1}.                             \tag{1.2}
\]

The first expression in (1.2) is independent of the row \(G\).

Fix a root target \(v\) and put
\(\mathcal S_v=\{F\in\mathcal C_r:v\in F\}\).  For distinct
\(F,H\in\mathcal S_v\), their joint survival probability is

\[
 q_{FH}=\prod_{u\in F\cup H}p_u.                          \tag{1.3}
\]

For a further row \(G\), set

\[
 A=(G\cap F)-\{v\},\qquad B=(G\cap H)-\{v\}.             \tag{1.4}
\]

If either set is empty, put \(k_G(F,H)=0\).  Otherwise put

\[
 k_G(F,H)=
 \begin{cases}
 p_v^{-1}\{w(A\cup B)-w(A)-w(B)+1\},&v\in G,\\[3pt]
 w(A\cup B)-w(A)-w(B),&v\notin G.
 \end{cases}                                             \tag{1.5}
\]

The signed two-star kernel is

\[
                         K(F,H)=\sum_{G\in\mathcal C_r}k_G(F,H). \tag{1.6}
\]

It is symmetric, but rooted flags \((v,F)\) need not form one orbit under
the stabilizer of \(v\).  In particular, neither denominator nor numerator
in (0.1) is asserted to be independent of \(F\).

## 2. Directional Hoeffding identity

Let \(X\) be the product target-retention state and put

\[
 d=d_v(X)=|\{F\in\mathcal S_v:F\preceq X\}|.              \tag{2.1}
\]

For a nonnegative function \(g\) with
\(0<\mathbb E[(d)_2g(d)]<\infty\), define \(L_g\) by (0.2), and put

\[
 A(F)=\sum_{H\ne F}q_{FH},\qquad
 B(F)=\sum_{H\ne F}q_{FH}K(F,H),\qquad
 a(F)=B(F)/A(F).                                          \tag{2.2}
\]

Every \(q_{FH}\) is positive, so \(A(F)>0\).  Define \(\ell_g\) by
(0.3).  Directly from the definitions,

\[
 \sum_{H\ne F}q_{FH}\{K(F,H)-a(F)\}=0,                  \tag{2.3}
\]

\[
 \sum_{H\ne F}q_{FH}\{L_g(F,H)-\ell_g(F)\}=0.          \tag{2.4}
\]

### Theorem 2.1 (exact directional split)

Let

\[
 D_g=\sum_{F\ne H}q_{FH}L_g(F,H)=\mathbb E[(d)_2g(d)],    \tag{2.5}
\]

Define

\[
 \omega_g(F)={A(F)\ell_g(F)\over D_g}.                   \tag{2.6}
\]

Then \(\omega_g\) is a probability law, (0.4)--(0.6) hold, and

\[
 \boxed{A(F)\ell_g(F)
 =\mathbb E[\mathbf1_{\{F\preceq X\}}(d-1)g(d)].}         \tag{2.7}
\]

#### Proof

First,

\[
 q_{FH}L_g(F,H)
 =\mathbb E[\mathbf1_{\{F,H\preceq X\}}g(d)].            \tag{2.8}
\]

Summing over ordered distinct pairs gives (2.5).  Summing (2.8) over
\(H\ne F\) gives (2.7), because a state in which \(F\) survives has
exactly \(d-1\) choices of \(H\).  Summing (2.7) over \(F\) gives
\(D_g\), so (2.6) is a probability law.

Write \(K(F,H)=a(F)+\{K(F,H)-a(F)\}\) in the numerator of
(0.4).  The first part is

\[
 \sum_FA(F)a(F)\ell_g(F)=D_g\mathbb E_{\omega_g}a(F).    \tag{2.9}
\]

By (2.3), subtracting \(\ell_g(F)\) inside the second part changes it by
zero.  The result is exactly \(D_g\mathcal C_g\).  Divide by \(D_g\).
\(\square\)

The directional choice in (2.2) is intentional.  A naive symmetric
subtraction \(K(F,H)-a(F)-a(H)+\text{constant}\) need not have zero row
sums because the weighted root-star pair law is not a product law.

### Proposition 2.2 (the one-body term is a finite position profile)

For either shore, the rooted flags \((v,F)\), with \(v\in F\), split into
exactly \(2r\) coordinate-relabeling orbits, indexed by the start position
\(i\in\{1,\ldots,2r\}\) of \(v\) in the canonical punctured row.  Hence

\[
 a(F)=a_{\sigma,i}\quad
 \text{when }v\text{ has shore }\sigma\text{ and position }i. \tag{2.10}
\]

The same is true of \(A(F)\), \(\ell_g(F)\), and every conditional profile
defined only from the product law and the rooted flag.  Consequently

\[
 \boxed{
 |\mathbb E_{\omega_{12}}a-\mathbb E_{\omega_c}a|
 \le \max_{1\le i\le2r}a_{\sigma,i}
       -\min_{1\le i\le2r}a_{\sigma,i}.}                  \tag{2.11}
\]

#### Proof

The tagged containment graph inside a punctured row is the alternating
path

\[
 L_1,M_1,L_2,M_2,\ldots,L_{2r},M_{2r}.                   \tag{2.12}
\]

Its two endpoints lie on different tagged shores, one on the lower shore
and one on the middle shore.  Coordinate relabeling preserves the shore
tags and therefore fixes the orientation of the path and the index \(i\).
Conversely, if
\((v,E(w))\) and \((v',E(w'))\) have the same shore and index, the label
permutation \(w_j\mapsto w'_j\) maps the first rooted flag to the second.
The path also reconstructs the word: the \(2r\) same-start differences
\(M_i-L_i\) give all but the puncture letter, and the unique unused label
gives that last letter.  Thus there are no additional orbits.  Invariance of the product
law and of (1.3)--(1.6) proves (2.10) and the corresponding assertions for
the other profiles.  Inequality (2.11) holds for any two probability laws
on the finite index set.  \(\square\)

Thus the first term in (0.8) no longer requires a tail-probability lower
bound.  It is enough to prove the deterministic boundary estimate

\[
 q_0\operatorname {osc}_{1\le i\le2r}a_{\sigma,i}=o(z).   \tag{2.13}
\]

The estimate (2.13) is not proved here.  Its expected source is the single
puncture boundary: changing the hole in the underlying full cyclic deck
changes only two tagged targets, but turning that observation into a
uniform bound on the signed ratio (0.1) still requires a boundary-polymer
calculation.

## 3. Literal \(m=12\) specialization

For integers, use the counting convention

\[
 (n)_k=0\quad\hbox{when }n<k.                             \tag{3.1}
\]

Let

\[
 f_c(d)=(d-c)_+^{12},\qquad c\ge11,                       \tag{3.2}
\]

and define \(g_{12},g_c\) by (0.7), with \(g_c(d)=0\) for
\(d<2\).  Let

\[
 {d\lambda_{12}\over d\mathbb P}={(d)_{12}\over\mathbb E(d)_{12}},
 \qquad
 {d\lambda_c\over d\mathbb P}={f_c(d)\over\mathbb E f_c(d)}. \tag{3.3}
\]

For \(d\ge2\), let

\[
 \overline K_2(X)={1\over(d)_2}
 \sum_{F\ne H}\mathbf1_{\{F,H\preceq X\}}K(F,H),        \tag{3.4}
\]

and set it to zero below degree two.  Statewise,

\[
 (d)_2g_{12}(d)=(d)_{12},\qquad
 (d)_2g_c(d)=f_c(d).                                      \tag{3.5}
\]

Therefore

\[
 \mathbb E_{\lambda_{12}}\overline K_2
 ={\sum_{F\ne H}q_{FH}K(F,H)L_{g_{12}}(F,H)\over
   \sum_{F\ne H}q_{FH}L_{g_{12}}(F,H)},                  \tag{3.6}
\]

and the identical formula with \(g_c\) equals
\(\mathbb E_{\lambda_c}\overline K_2\).  Applying Theorem 2.1 twice
proves (0.8).

The one-carrier weights in (2.7) simplify to

\[
 A(F)\ell_{12}(F)
 =\mathbb E[\mathbf1_{\{F\preceq X\}}(d-1)_{11}],        \tag{3.7}
\]

\[
 A(F)\ell_c(F)
 =\mathbb E\left[\mathbf1_{\{F\preceq X\}}{f_c(d)\over d}\right]. \tag{3.8}
\]

Thus the first brace in (0.8) is a finite rooted-position regression, and
the second brace is a pair-connected response in which both the geometric
kernel and the tail profile have had their first-coordinate averages
removed.

## 4. Exact remaining scale

The signed contribution of this kernel to the product-reference hazard
comparison is

\[
 \mathcal R_{2,c}=q_0{12\choose2}
 \left[
  \{\mathbb E_{\omega_{12}}a-\mathbb E_{\omega_c}a\}
  +\{\mathcal C_{12}-\mathcal C_c\}
 \right].                                                \tag{4.1}
\]

It appears inside the positive part of the signed sum over
\(2\le s\le12\); (4.1) should not automatically be replaced by its
absolute value.  A uniform bound \(\mathcal R_{2,c}=o(z)\), together with
the analogous bound on the remaining signed kernels, is a sufficient
reference scale: since \(z/Z=2r/n\), summing one jump per loss of \(2r\)
shore targets turns \(o(z)/Z\) into \(o(1)\) per unit logarithmic density,
hence \(o(\log r)\) down to polynomial density.

The exact coefficient-one obligation is the cumulative bound

\[
 \sum_{j<J}{1\over Z_j}
 \left[\sum_{s=2}^{12}\mathcal R_{s,c,j}\right]_+
 \le(\kappa+o(1))\log r,
 \qquad \kappa<2-20\alpha.                               \tag{4.2}
\]

For \(s=2\), a boundary proof must now control the **signed combination**
of the rooted-position term and the directional connected response in
(4.1).  This note proves neither estimate.  After product-reference
closure, exact-slice, stopped-law, realized-center, and unequal-purge
transfers remain separate obligations.

## 5. Exact checker

The script

`scratch/verify_gate_a_two_star_directional_tail_response_20260822.py`

uses the complete \(r=2\) punctured catalogue, the full root star, literal
carrier order \(12\), and rational arithmetic.  It verifies (2.3)--(2.8),
the direct pair/state identities (3.5)--(3.6), and the decomposition (0.8)
for both the factorial and cutoff-tail weights.  It also confirms that the
root-star pair extension mass is genuinely nonconstant across rooted flags,
so replacing (0.1) by a constant would be an invalid transitivity step.
