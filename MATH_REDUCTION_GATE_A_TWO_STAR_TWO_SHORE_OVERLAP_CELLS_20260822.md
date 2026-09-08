# Gate A: the punctured two-star reduces to two-shore overlap-cell determinants

**Date:** 2026-08-22  
**Status:** exact product-reference reduction at \(m=12\); the signed
boundary estimate in (4.2), and the higher connected kernels, remain open

## 0. Outcome

For the first connected punctured kernel, the earlier position and
second-carrier likelihood covariances recombine into one covariance under
the ordered-pair factorial Palm law.  If \(K(F,H)\) is the signed
two-star kernel and

\[
 S(F,H)={L_c(F,H)\over L_{12}(F,H)}
\]

is the exact cutoff-tail to factorial likelihood ratio, then

\[
 \boxed{
 \Delta_{2,c}:=
 \mathbb E_{\lambda_{12}}\overline K_2
  -\mathbb E_{\lambda_c}\overline K_2
 =-{\operatorname {Cov}_{\Pi_{12}}(K,S)\over\overline S}.}
                                                               \tag{0.1}
\]

Here \(\Pi_{12}\) is the ordered-pair factorial Palm law and
\(\overline S=\mathbb E_{\Pi_{12}}S\).  Thus the positional covariance
and the within-position covariance must not be bounded separately.

For a pair of root rows, let

\[
 \tau(F,H)=(t_M,t_L)                                    \tag{0.2}
\]

record their numbers of common middle- and lower-shore targets away from
the root.  The joint survival probability \(q_{FH}\) is constant on each
two-shore cell.  Conditioning (0.1) on \(\tau\) gives the exact split

\[
 \boxed{
 \operatorname {Cov}_{\Pi_{12}}(K,S)
 =\operatorname {Cov}_{\rho}(\kappa_\tau,s_\tau)
   +\sum_\tau\rho_\tau\eta_\tau.}                       \tag{0.3}
\]

The first term sees only the finite overlap profile.  The second is an
arrangement-sensitive within-cell determinant.  With the notation of
Section 3,

\[
 \boxed{
 \eta_\tau={\mathfrak D_\tau\over A_{12,\tau}^2},\qquad
 \mathfrak D_\tau={1\over2}
 \sum_{P,Q\in\mathcal P_\tau}
 L_{12}(P)L_{12}(Q)
 \{K(P)-K(Q)\}\{S(P)-S(Q)\}.}                           \tag{0.4}
\]

Consequently the within-cell contribution to \(\Delta_{2,c}\) is

\[
 \boxed{
 \Delta_{2,c}^{\rm within}
 =-{1\over Z_c}\sum_\tau q_\tau
                   {\mathfrak D_\tau\over A_{12,\tau}}.} \tag{0.5}
\]

This is tail-mass-relative and keeps cancellation among all overlap
cells.  It does not take a full range and it does not divide a generic
global \(L^2\) error by a rare-tail probability.

Two tempting stronger simplifications are false.

1. Total overlap \(t_M+t_L\) does not determine \(q_{FH}\) when the two
   shore probabilities differ.
2. Even the two-shore vector does not determine \(L_{12}\), \(S\), or the
   full pair orbit.  Individual within-vector determinants can be
   negative.

Thus (0.4), not scalar overlap monotonicity or cellwise positivity, is
the first honest punctured-specific boundary object.

## 1. Product law and the global pair tilt

Put \(b=2r+1\).  The middle targets are the tagged \(r\)-subsets of
\([b]\), and the lower targets are the tagged \((r-1)\)-subsets.  A
permutation \(w=(w_0,\ldots,w_{b-1})\) gives the row

\[
 E(w)=\{(M,\{w_i,\ldots,w_{i+r-1}\}):1\le i<b\}
 \mathbin{\dot\cup}
 \{(L,\{w_i,\ldots,w_{i+r-2}\}):1\le i<b\},             \tag{1.1}
\]

where indices are read cyclically.  The complete catalogue consists of
these rows.  A punctured row contains \(2r\) targets on each shore.
Retain every middle target independently with probability \(x\) and
every lower target with probability \(y\), where \(0<x,y<1\).  Write

\[
 q_0=x^{2r}y^{2r}.                                      \tag{1.2}
\]

Fix a root target \(v\), let \(\mathcal S_v\) be the rows containing it,
and let \(d=d_v(X)\) be the number of live rows in the root star.  For
distinct \(F,H\in\mathcal S_v\), put

\[
 q_{FH}=\Pr(F,H\text{ are live}).                        \tag{1.3}
\]

For a nonnegative degree weight \(g\), define

\[
 L_g(F,H)=\mathbb E[g(d)\mid F,H\text{ are live}].       \tag{1.4}
\]

At the literal carrier order \(m=12\), use the counting convention
\((n)_k=0\) for \(n<k\), fix \(c\ge11\), and put

\[
 g_{12}(d)=(d-2)_{10},\qquad
 g_c(d)={(d-c)_+^{12}\over(d)_2},                        \tag{1.5}
\]

where the second expression is zero for \(d<2\).  Abbreviate

\[
 L_{12}=L_{g_{12}},\qquad L_c=L_{g_c}.                   \tag{1.6}
\]

Assume \(|\mathcal S_v|\ge12\).  Full support gives
\(L_{12}(F,H)>0\).  Assume also that the cutoff tail is nonempty, and
define

\[
 Z_{12}=\sum_{F\ne H}q_{FH}L_{12}(F,H),\qquad
 Z_c=\sum_{F\ne H}q_{FH}L_c(F,H).                       \tag{1.7}
\]

The sums are over ordered pairs.  Statewise extension counting gives

\[
 Z_{12}=\mathbb E(d)_{12},\qquad
 Z_c=\mathbb E(d-c)_+^{12}.                              \tag{1.8}
\]

Define the two ordered-pair laws

\[
 \Pi_{12}(F,H)={q_{FH}L_{12}(F,H)\over Z_{12}},\qquad
 \Pi_c(F,H)={q_{FH}L_c(F,H)\over Z_c},                  \tag{1.9}
\]

and

\[
 S(F,H)={L_c(F,H)\over L_{12}(F,H)},\qquad
 \overline S={Z_c\over Z_{12}}.                         \tag{1.10}
\]

Then

\[
 \Pi_c(P)={\Pi_{12}(P)S(P)\over\overline S}.            \tag{1.11}
\]

For a state \(X\), let

\[
 Y_2(X)=\sum_{\substack{F,H\in\mathcal S_v\\F\ne H\\
                         F,H\text{ live in }X}}K(F,H),
 \qquad
 \overline K_2(X)={Y_2(X)\over(d(X))_2},                 \tag{1.12}
\]

with value zero when \(d<2\).  Let \(\lambda_{12}\) and \(\lambda_c\)
be the state laws tilted respectively by \((d)_{12}\) and
\((d-c)_+^{12}\).

### Theorem 1.1 (unsplit pair-likelihood identity)

For every real pair statistic \(K\),

\[
 \mathbb E_{\Pi_{12}}K-\mathbb E_{\Pi_c}K
 =-{\operatorname {Cov}_{\Pi_{12}}(K,S)\over\overline S}. \tag{1.13}
\]

For the punctured signed two-star kernel,

\[
 \mathbb E_{\Pi_{12}}K-\mathbb E_{\Pi_c}K
 =\mathbb E_{\lambda_{12}}\overline K_2
  -\mathbb E_{\lambda_c}\overline K_2.                  \tag{1.14}
\]

#### Proof

Equation (1.11) gives

\[
 \mathbb E_{\Pi_c}K
 ={\mathbb E_{\Pi_{12}}KS\over\overline S}.
\]

Subtract and use
\(\mathbb E_{\Pi_{12}}S=\overline S\).  For (1.14), the identities

\[
 (d)_2g_{12}(d)=(d)_{12},\qquad
 (d)_2g_c(d)=(d-c)_+^{12}
\]

show that the two pair laws are precisely the factorial and cutoff-tail
state tilts followed by a uniform ordered live-pair choice.  \(\square\)

For completeness, the kernel used in the application is the following.
For a further catalogue row \(G\), put

\[
 A=(G\cap F)-\{v\},\qquad B=(G\cap H)-\{v\},\qquad
 w(U)=\prod_{u\in U}p_u^{-1}.                            \tag{1.15}
\]

Its contribution is zero if \(A\) or \(B\) is empty, and otherwise is

\[
 k_G(F,H)=
 \begin{cases}
 p_v^{-1}\{w(A\cup B)-w(A)-w(B)+1\},&v\in G,\\[3pt]
 w(A\cup B)-w(A)-w(B),&v\notin G.
 \end{cases}                                             \tag{1.16}
\]

Then \(K(F,H)=\sum_Gk_G(F,H)\).  Nothing in Theorem 1.1 depends on the
special form (1.16); that form matters in the boundary estimate.

## 2. Why the two-shore vector is the correct first partition

Let \(\delta_M=1\) if \(v\) is a middle target and \(0\) otherwise, and
put \(\delta_L=1-\delta_M\).  Define

\[
 t_M=|(F\cap H)\cap V_M|-\delta_M,\qquad
 t_L=|(F\cap H)\cap V_L|-\delta_L.                      \tag{2.1}
\]

Thus \(\tau(F,H)=(t_M,t_L)\) removes the common root.  Since each row has
\(2r\) targets on each shore,

\[
 \boxed{
 q_{FH}=q_\tau
 =x^{\,4r-t_M-\delta_M}
  y^{\,4r-t_L-\delta_L}.}                               \tag{2.2}
\]

#### Proof

The intersection contains \(t_M+\delta_M\) middle targets and
\(t_L+\delta_L\) lower targets.  Hence the union contains respectively
\(4r-t_M-\delta_M\) and \(4r-t_L-\delta_L\) targets.  Independence gives
(2.2).  \(\square\)

The scalar total \(T=t_M+t_L\) loses the two exponents in (2.2).  It is
therefore not weight-sufficient when \(x\ne y\).  If \(x=y\), total
overlap does fix \(q_{FH}\), but it still need not determine either
conditional degree transform.

Nor does \(\tau\) classify pair orbits.  A fixed punctured row is a
shore-coloured alternating path whose endpoints lie on opposite shores.
Every shore-preserving automorphism fixes the path orientation and then
every path vertex.  The same-start differences reconstruct every label
except the puncture label, which is the unique unused label.  Thus the
coordinate stabilizer of a fixed row is trivial.  After fixing \(F\), a
full second-row label generally remains necessary; overlap counts alone
cannot be an exact orbit parameter.

## 3. Exact overlap-cell decomposition

Let

\[
 \mathcal P_\tau=
 \{(F,H):F,H\in\mathcal S_v,\ F\ne H,\ \tau(F,H)=\tau\}. \tag{3.1}
\]

For every nonempty cell define

\[
 \begin{aligned}
 A_{12,\tau}&=\sum_{P\in\mathcal P_\tau}L_{12}(P),&
 A_{c,\tau}&=\sum_{P\in\mathcal P_\tau}L_c(P),\\
 B_{12,\tau}&=\sum_{P\in\mathcal P_\tau}K(P)L_{12}(P),&
 B_{c,\tau}&=\sum_{P\in\mathcal P_\tau}K(P)L_c(P).
 \end{aligned}                                           \tag{3.2}
\]

Put

\[
 \rho_\tau={q_\tau A_{12,\tau}\over Z_{12}},\qquad
 \kappa_\tau={B_{12,\tau}\over A_{12,\tau}},\qquad
 s_\tau={A_{c,\tau}\over A_{12,\tau}},                  \tag{3.3}
\]

and

\[
 \mathfrak D_\tau
 =A_{12,\tau}B_{c,\tau}
   -B_{12,\tau}A_{c,\tau},\qquad
 \eta_\tau={\mathfrak D_\tau\over A_{12,\tau}^2}.        \tag{3.4}
\]

### Theorem 3.1 (two-shore cell identity)

Equations (0.3)--(0.5) hold.  More explicitly,

\[
 \boxed{
 \Delta_{2,c}
 =-{1\over\overline S}
 \left\{
 \operatorname {Cov}_{\rho}(\kappa_\tau,s_\tau)
 +\sum_\tau\rho_\tau
       {\mathfrak D_\tau\over A_{12,\tau}^2}
 \right\}.}                                             \tag{3.5}
\]

#### Proof

Conditional on \(\tau\), (2.2) cancels from the law \(\Pi_{12}\).  Hence
the conditional pair law assigns mass

\[
 {L_{12}(P)\over A_{12,\tau}}                            \tag{3.6}
\]

to \(P\in\mathcal P_\tau\).  Its conditional means of \(K\) and \(S\)
are \(\kappa_\tau\) and \(s_\tau\), while its conditional covariance is

\[
 {B_{c,\tau}\over A_{12,\tau}}
 -{B_{12,\tau}\over A_{12,\tau}}
  {A_{c,\tau}\over A_{12,\tau}}
 ={\mathfrak D_\tau\over A_{12,\tau}^2}.                \tag{3.7}
\]

The law of total covariance proves (0.3), and (0.1) proves (3.5).
Finally,

\[
 {1\over\overline S}\rho_\tau\eta_\tau
 ={q_\tau\over Z_c}{\mathfrak D_\tau\over A_{12,\tau}},
\]

which gives (0.5).

To prove (0.4), expand

\[
 \sum_{P,Q}L_{12}(P)L_{12}(Q)
 \{K(P)-K(Q)\}\{S(P)-S(Q)\}.
\]

The two diagonal products give
\(2A_{12,\tau}B_{c,\tau}\); the two cross-products give
\(2B_{12,\tau}A_{c,\tau}\).  Divide by two.  \(\square\)

## 4. The first signed within-cell boundary estimate

The \(s=2\) term in the product-reference hazard comparison is

\[
 q_0{12\choose2}\Delta_{2,c}.                            \tag{4.1}
\]

The exact irreducible within-cell contribution is (0.5).  A clean
tail-relative target, retaining all cancellation among cells, is

\[
 \boxed{
 q_0\left[
 -{1\over Z_c}\sum_\tau q_\tau
       {\mathfrak D_\tau\over A_{12,\tau}}
 \right]_+=o(z),}                                       \tag{4.2}
\]

uniformly in the live density range and deterministic cutoffs used by
Gate A.  Here \(z=\mathbb E d_v\) at the relevant product-reference
state.  Estimate (4.2) is not by itself a bound for (3.5): the signed
between-cell term must also be shown favorable or controlled on the same
scale.  It is the first within-cell estimate exposed after preserving
all position and overlap-cell cancellation.

A stronger but potentially wasteful target would replace the signed sum
in (4.2) by
\(\sum_\tau q_\tau[-\mathfrak D_\tau]_+/A_{12,\tau}\).
There is currently no reason to impose that loss.

The pairwise form (0.4) identifies the local task precisely: control the
negative arrangement correlation between the signed connected kernel
and the exact tail likelihood ratio among pairs having identical shore
overlap counts.  A proof must use the punctured boundary-polymer
structure of \(K\) and of the conditional degree transform.  Generic
FKG does not apply to the carrier-label variable \(P\).

Even after (3.5) is controlled, Gate A still requires the signed sum with
the higher Möbius kernels \(3\le s\le12\), followed by the
product-to-two-shore-slice, stopped erosion, shadow-center, purge, and
degree-floor transfers.

## 5. Exact \(r=2\) audit and the false stronger claims

The checker described in Section 6 uses the complete \(r=2\) catalogue,
a middle root \(v=(M,\{0,1\})\), \(x=3/4\), \(y=1/2\), and \(c=12\).
All arithmetic is rational.

First, total overlap \(T=6\) occurs with two joint survival masses

\[
 {81\over8192}\quad\hbox{and}\quad {243\over16384},      \tag{5.1}
\]

so total overlap does not fix \(q_{FH}\).

Second, fix the position-one row represented by

\[
 F=(4,1,0,2,3).                                         \tag{5.2}
\]

The second rows

\[
 H=(4,3,1,0,2),\qquad J=(4,2,1,0,3)                    \tag{5.3}
\]

have the same two-shore overlap vector \((1,4)\), but

\[
 L_{12}(F,H)-L_{12}(F,J)
 ={51374238358275\over2}\ne0,                           \tag{5.4}
\]

and

\[
 S(F,H)-S(F,J)
 =-{2437815679298638170531944948888
 \over2916882906010537645991730793611375}\ne0.          \tag{5.5}
\]

Thus the vector is weight-sufficient for \(q_{FH}\), but is not a
sufficient statistic for the conditional degree transform.

Finally, individual global vector cells need not have favorable sign.
For \(\tau=(1,4)\), the cell has \(264\) ordered pairs and

\[
 \mathfrak D_{(1,4)}
 =-{69353265067384988728156624982046766080\over267007}<0. \tag{5.6}
\]

For \(\tau=(2,3)\), the cell has \(468\) ordered pairs and

\[
 \mathfrak D_{(2,3)}
 =-{26194450716406951846138782153558720000\over267007}<0. \tag{5.7}
\]

So no cellwise nonnegativity assertion may be used.  In this exact
instance the aggregate between-cell covariance, aggregate within-cell
covariance, and total covariance are nevertheless all positive.  Hence
the complete \(s=2\) shift is favorable; that finite fact is evidence,
not an asymptotic theorem.

## 6. Checker

The self-contained script

scratch/verify_gate_a_two_star_overlap_cell_decomposition_20260822.py

constructs every \(r=2\) row and target state, evaluates the two degree
transforms and the signed kernel by exact rational arithmetic, and
verifies:

1. the global likelihood identity (0.1);
2. both laws of total covariance, using total-overlap and two-shore cells;
3. the exact determinant formula (3.4) in every two-shore cell;
4. constancy of \(q_{FH}\) on two-shore cells and its failure on total
   overlap cells;
5. the witnesses (5.2)--(5.7).
