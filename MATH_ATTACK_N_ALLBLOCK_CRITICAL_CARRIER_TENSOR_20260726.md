# Lane N: exact critical-lift carrier tensor for the all-block conjugate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let \(F_r\) be the canonical anchored \(D_r\)-port factor on a local
coordinate set \(J\), \(|J|=2r\), let \(\star\) be its rooted cyclic anchor,
and put

\[
 \eta_r=(2\ 3)(4\ 5)\cdots(2r-2\ 2r-1),
 \qquad G_r(P)=\eta_rF_r(\eta_rP).
 \tag{0.1}
\]

The whole shallow carrier tensor of this pair admits an exact closed
description which is stronger than the first-insertion matrix.

1. Write the rooted coordinate word of the canonical row as

   \[
     \omega_F(P)=(a_1,\ldots,a_r,b_1,\ldots,b_r,\star).
     \tag{0.2}
   \]

   Then

   \[
     \boxed{\omega_G(P)=\eta_r^\star\omega_F(\eta_rP),}
     \tag{0.3}
   \]

   where \(\eta_r^\star\) fixes \(\star\).

2. In a one-hole lift to an ambient word of length \(2m+1\), suppose the
   displayed local word is one contiguous block of length \(2r+1\). If

   \[
      2r+1<m-H,
      \qquad 1\le q\le H,
      \qquad k_q=m-q,
      \tag{0.4}
   \]

   then a length-\(k_q\) ambient cyclic interval has at most one boundary
   cut strictly inside the local block. Therefore every affected target
   is exactly a fixed exterior collar joined to either a proper prefix or
   a proper suffix of (0.2). There are no hidden strict-interior local
   windows. Formula (3.2) below is the complete row/start tensor.

3. After summing all \(D_r\) fillings in one fixed context \(C\), the
   complete affected histogram satisfies the exact conjugacy law

   \[
      \boxed{U^G_{C,q}=\eta_{C*}U^F_{C,q},\qquad
             D_{C,q}=(\eta_{C*}-I)U^F_{C,q}.}
      \tag{0.5}
   \]

   Here \(\eta_C\) is the inherited physical permutation on the local
   coordinates and fixes the entire exterior collar. Equation (0.5)
   already includes both crossing sides and all collisions *inside* the
   context. Across different contexts one must sum their physical vectors
   before taking a hinge; the permutations \(\eta_C\) need not be the same.

4. Consequently a whole-context \(F\leftrightarrow G\) switch has no
   intrinsic cap direction. On every two-point \(\eta_C\)-orbit its exact
   hinge is the rearrangement expression (5.2). Its magnitude is at most

   \[
      \min\{|u(T)-u(\eta_CT)|,
              |a(T)-a(\eta_CT)|\},
      \tag{0.6}
   \]

   where \(a=\ell-\beta\) is unaffected load minus quota. In particular,
   an \(\eta_C\)-symmetric effective background gives exactly zero endpoint
   gain. Any gain is produced solely by physical collision with an
   asymmetric background/quota.

5. If the local full \(X/Y\) overlay is connected and the physical target
   fibres of distinct lifted contexts are recoverable/disjoint, then the
   zero-margin CRH certificate cannot improve on the better deterministic
   endpoint. For every law, context by context,

   \[
      \boxed{\Phi_C+\mathcal R_C
                  \ge \min\{H_C(F),H_C(G)\}.}
      \tag{0.7}
   \]

   Correlations between different context bits do not change (0.7),
   because every target sees only one bit. Thus under these two explicit
   hypotheses the all-block pair fails the CRH mechanism unless one of its
   two deterministic endpoints already has the required \(o(W)\) hinge.
   A genuine escape must use nontrivial local overlay fragmentation or
   cross-context physical target merging with proved targetwise covariance.

6. At the critical scale \(r/\sqrt m\to\kappa\in(0,\infty)\) and
   \(H=\lceil A\sqrt m\rceil\), the exact weighted carrier ceiling is

   \[
     {1\over2}\sum_{q\le H}{1\over c_q}
        \|\mu_q^G-\mu_q^F\|_1
     \le
     \bigl(2\kappa J_A+o_A(1)\bigr)W,
     \qquad
     J_A=\int_0^A {dx\over\lfloor e^{x^2}\rfloor}.
     \tag{0.8}
   \]

   Hence the pair is at the first scale where macroscopic action is not
   excluded. But (0.8) is only an upper bound. The exact normalized
   active-cut statistic \(\alpha_r\) in (4.7) must stay bounded away from
   zero, and physical collisions must retain a favourable part of its
   tagged action. The first-matching theorem alone proves only
   \(\alpha_r=\Omega(1/r)\), which yields \(o(W)\) action and is insufficient.

Thus the all-block seed passes exactness and the previously proved extensive
row-distance test, but its full critical carrier hinge is not proved. The
new sharp boundary is (0.5)--(0.8), not the source-resolved \(1/9\) first
matching.

## 1. Rooted coordinate words and cut flags

For an anchored factor \(H\in\{F,G\}\), write

\[
 X_t^H(P)=
 (P\setminus A_t^H(P))\cup B_t^H(P),
 \tag{1.1}
\]

where

\[
 A_t^H(P)=\{a_1^H(P),\ldots,a_t^H(P)\},
 \qquad
 B_t^H(P)=\{b_1^H(P),\ldots,b_t^H(P)\}.
 \tag{1.2}
\]

The rooted word is

\[
 \omega_H(P)=(a_1^H,\ldots,a_r^H,
               b_1^H,\ldots,b_r^H,\star).
 \tag{1.3}
\]

Coordinate conjugation of every phase proves (0.3). For
\(0\le c\le2r+1\), let \(\Pi_c^H(P)\) be the set of the first \(c\)
symbols of \(\omega_H(P)\). Before the anchor,

\[
 \Pi_c^H(P)=
 \begin{cases}
   A_c^H(P),&0\le c\le r,\\[1mm]
   P\cup B_{c-r}^H(P),&r\le c\le2r.
 \end{cases}
 \tag{1.4}
\]

In particular

\[
 \Pi_r^F(P)=\Pi_r^G(P)=P,
 \qquad
 \Pi_{2r}^F(P)=\Pi_{2r}^G(P)=J.
 \tag{1.5}
\]

Equation (0.3) gives the exact flag conjugacy

\[
 \boxed{
 \Pi_c^G(P)=\eta_r^\star\Pi_c^F(\eta_rP)
 \quad(0\le c\le2r+1).}
 \tag{1.6}
\]

Define the number of genuinely changed internal cuts by

\[
 d_\partial(P)=
 \#\{1\le c\le2r-1:
        c\ne r,\ \Pi_c^F(P)\ne\Pi_c^G(P)\}.
 \tag{1.7}
\]

For \(1\le t<r\), equality of the two phase-\(t\) states is equivalent to
simultaneous equality of \(A_t\) and \(B_t\). Hence, writing

\[
 N_X(P)=\#\{1\le t<r:X_t^F(P)\ne X_t^G(P)\},
\]

one has the exact comparison

\[
       \boxed{N_X(P)\le d_\partial(P)\le2N_X(P).}
 \tag{1.8}
\]

There is also a word-Hamming lower bound. Let \(\rho(P)\) be the number
of positions where \(\omega_F(P)\) and \(\omega_G(P)\) differ. The cuts at
which their prefix sets agree partition both words into common symbol
blocks. A nontrivial block of length \(L\ge2\) has \(L-1\) unequal
internal cuts and at most \(L\le2(L-1)\) changed positions. Summing over
the nontrivial blocks gives

\[
                         \boxed{d_\partial(P)\ge\rho(P)/2.}
 \tag{1.9}
\]

Thus a positive-density \(\Theta(r)\)-position activity theorem would imply
the positive active-cut density needed below. No such trajectory theorem
is presently proved for (0.1).

## 2. What the first matching does and does not force

Let \(R_n\) be defined by

\[
 \sum_{n\ge0}R_nz^n={C(z)^2\over2C(z)-1}.
 \tag{2.1}
\]

The all-block first-return matrix implies that the canonical and conjugate
first insertion coordinates agree only when both \(P\) and \(\eta_rP\) have
top first-return class. There are exactly \(R_{r-1}\) such roots. For
every other root,

\[
 P\cup\{b_1^F(P)\}\ne P\cup\{b_1^G(P)\},
\]

and therefore the cut \(c=r+1\) in (1.4) changes. Consequently

\[
 \boxed{
 \sum_{P\in D_r}d_\partial(P)
       \ge C_r-R_{r-1}
       =\left({8\over9}+o(1)\right)C_r.}
 \tag{2.2}
\]

This proves extensive *row count* and recovers the row-distance lower
bound, but it is only one changed cut per certified row. Since a row has
\(2r-2\) potentially active internal cuts, (2.2) gives only

\[
 {1\over(2r-2)C_r}\sum_Pd_\partial(P)
 \ge {C_r-R_{r-1}\over(2r-2)C_r}
 ={4\over9r}+o(r^{-1}).
 \tag{2.3}
\]

The source-resolved \(1/9\) quota theorem therefore does not establish a
positive active-cut density. Moreover the intrinsic singleton target
\(b_1(P)\) is an internal coordinate of (1.3). Under (0.4), no shallow
ambient interval can isolate it by placing both boundaries inside the
local block. It affects the outer carrier only through the full prefix
\(P\cup\{b_1(P)\}\) and the other crossing flags. This is the precise
reason that the first-insertion histogram is not the critical-lift carrier
histogram.

## 3. Exact one-boundary-cut theorem

Let an ambient rooted coordinate word have length

\[
                         N=2m+1
\]

and contain one displayed contiguous local block \(Q\) of length

\[
                         b=2r+1.
\]

Replace \(Q=\omega_F(P)\) by \(Q'=\omega_G(P)\), leaving the outside word
fixed. Fix a cyclic interval length \(k\) satisfying

\[
                         b<k<N-b.
 \tag{3.1}
\]

We choose the inherited orientation of the local block so that it is
written as \(Q\). If a legal aligned context presents the local word in
the reverse orientation, replace every prefix \(\Pi_c\) below by the
corresponding suffix
\(J^\star\setminus\Pi_{b-c}\) and interchange the two exterior families.
This is only the reindexing \(c\leftrightarrow b-c\); equations
(3.2)--(3.9) and all norms are unchanged. The same observation covers a
fixed inherited coordinate relabelling by conjugating \(\eta_r^\star\).

### Lemma 3.1 (one internal boundary)

No length-\(k\) cyclic interval has both boundary cuts strictly inside
\(Q\). A window with no internal boundary contains either all of \(Q\)
or none of \(Q\), and hence is unchanged. For every internal cut \(c\),
exactly two windows use it: one has local part \(\Pi_c(P)\), and the other
has local part \(J^\star\setminus\Pi_c(P)\), where
\(J^\star=J\cup\{\star\}\).

#### Proof

The directed distance between two cuts strictly inside one \(b\)-block is
either less than \(b\) or greater than \(N-b\). It cannot equal \(k\)
under (3.1). A cyclic interval whose two boundaries lie outside a
contiguous block either crosses both exterior boundary edges and contains
the whole block, or crosses neither and avoids it. Finally a fixed cut is
the initial boundary of one length-\(k\) interval and the terminal boundary
of one; the preceding argument shows that their other boundaries are
outside \(Q\). Their local portions are the complementary prefix and
suffix stated above. \(\square\)

For a fixed lifted context \(C\), let
\(E^-_{C,q,c},E^+_{C,q,c}\) be the two exterior parts in Lemma 3.1, and
let \(\iota_C\) be the inherited local coordinate injection. At lower
depth \(q\), \(k=m-q\), the complete signed row tensor is therefore

\[
\boxed{
\begin{aligned}
 d_{C,P,q}=\sum_{c=1}^{2r}\Big(&
 e_{E^-_{C,q,c}\cup\iota_C(\Pi_c^G(P))}
 -e_{E^-_{C,q,c}\cup\iota_C(\Pi_c^F(P))}\\
 &+e_{E^+_{C,q,c}\cup
          \iota_C(J^\star\setminus\Pi_c^G(P))}
 -e_{E^+_{C,q,c}\cup
          \iota_C(J^\star\setminus\Pi_c^F(P))}
 \Big).
\end{aligned}}
\tag{3.2}
\]

The summands at \(c=r,2r\) vanish by (1.5); the endpoint cuts may equally
be retained as zero terms. Formula (3.2) is row- and start-resolved. It
contains both crossing collars, not just the local \(X_t\)-states.

For \(0\le c\le2r+1\), define the canonical prefix histogram

\[
 H_c^F=\sum_{P\in D_r}e_{\Pi_c^F(P)},
 \qquad
 \overline H_c^F
 =\sum_{P\in D_r}e_{J^\star\setminus\Pi_c^F(P)}.
 \tag{3.3}
\]

Changing variables \(P\mapsto\eta_rP\) in (1.6) gives

\[
 H_c^G=\eta_{r*}^\star H_c^F,
 \qquad
 \overline H_c^G=\eta_{r*}^\star\overline H_c^F.
 \tag{3.4}
\]

Let \(\Phi^-_{C,q,c},\Phi^+_{C,q,c}\) be the two physical push-forwards in
(3.2). Summing (3.2) over every local root gives

\[
\boxed{
 D_{C,q}=\sum_c\left[
  \Phi^-_{C,q,c}(\eta_*H_c^F-H_c^F)
 +\Phi^+_{C,q,c}(\eta_*\overline H_c^F-
                                   \overline H_c^F)
                    \right].}
 \tag{3.5}
\]

The exterior sets are disjoint from the local coordinates and are fixed
by the inherited physical involution \(\eta_C\). Hence all terms in (3.5)
factor simultaneously, proving

\[
                         \boxed{D_{C,q}
                           =(\eta_{C*}-I)U^F_{C,q}.}
 \tag{3.6}
\]

For an actual full ownership component \(K\), the same change of variables
gives the component-resolved law

\[
 \boxed{V_{C,K,q}=\eta_{C*}U_{C,\eta_rK,q}.}
 \tag{3.7}
\]

Thus an \(\eta_r\)-stable component preserves every physical
\(\eta_C\)-orbit total. If components are paired by \(\eta_r\), (3.7)
relates their actions but does not make either component separately
orbit-invariant.

Different first-fringe contexts generally have different local coordinate
sets and hence different physical involutions \(\eta_C\). Therefore the
global difference is

\[
                         D_q=\sum_CD_{C,q},
 \tag{3.8}
\]

not one global permutation coboundary. Physical target collisions between
the summands in (3.8) must be resolved before applying a cap hinge.

The complementary upper-shadow tensor requires no new calculation. Let
\(\mathfrak c(T)=[2m+1]\setminus T\). The complement of a cyclic
\((m-q)\)-interval is the paired cyclic \((m+q+1)\)-interval, so

\[
 D^{\rm upper}_{C,q}=\mathfrak c_*D^{\rm lower}_{C,q},
 \qquad
 V^{\rm upper}_{C,K,q}
   =\mathfrak c_*V^{\rm lower}_{C,K,q}.
 \tag{3.9}
\]

Since \(\mathfrak c\) commutes with \(\eta_C\), equations
(3.6)--(3.7), the cut count, and every \(\ell^1\) estimate hold verbatim
on the upper side. Thus (3.2) together with (3.9) is the complete
two-sided lower/upper row-start carrier tensor.

## 4. Critical-scale constants and the missing activity estimate

For one row and one depth, (3.2) shows that a changed cut can change at
most two physical target occurrences. Hence, with

\[
 e_{C,P,q}={1\over2}
       \|z^G_{C,P,q}-z^F_{C,P,q}\|_1,
\]

one has

\[
 \boxed{e_{C,P,q}\le2d_\partial(P)\le4(r-1).}
 \tag{4.1}
\]

The first inequality allows physical collisions to cancel changes; with
row/start tags retained, equality holds in the corresponding occurrence
count.

Let \(a_{m,r}\) be the number of size-\(m\) Catalan roots with no
size-\(r\) fringe subtree. First-fringe packetization gives

\[
 P_{m,r}={C_m-a_{m,r}\over C_r}
 \tag{4.2}
\]

disjoint contexts, and at \(r=\Theta(\sqrt m)\),

\[
                         a_{m,r}=o(C_m).
 \tag{4.3}
\]

Put

\[
 \lambda_{m,q}={\binom{2m+1}m\over
                         \binom{2m+1}{m-q}},
 \qquad c_q=\lfloor\lambda_{m,q}\rfloor,
 \qquad
 \Omega_{A,m}=\sum_{q\le\lceil A\sqrt m\rceil}{1\over c_q}.
 \tag{4.4}
\]

Uniformly for \(q=x\sqrt m\), \(0\le x\le A\),

\[
 \lambda_{m,q}
 =\prod_{i=1}^q{m+1+i\over m-q+i}
 =\exp(x^2+O_A(m^{-1/2})).
 \tag{4.5}
\]

Only \(O_A(1)\) mesh points can be affected by the finitely many floor
thresholds in a fixed compact \(x\)-window. Riemann summation therefore
gives

\[
 \boxed{
 {\Omega_{A,m}\over\sqrt m}\longrightarrow
 J_A:=\int_0^A{dx\over\lfloor e^{x^2}\rfloor}.}
 \tag{4.6}
\]

Combining (4.1)--(4.4), and writing

\[
 \alpha_r={1\over(2r-2)C_r}\sum_{P\in D_r}d_\partial(P),
 \qquad0\le\alpha_r\le1,
 \tag{4.7}
\]

gives the exact tagged action and the physical ceiling

\[
\begin{aligned}
 \mathscr A^{\rm tag}_{A,m,r}
   &=2\Omega_{A,m}P_{m,r}\sum_Pd_\partial(P)\\
   &=4(r-1)\alpha_r\Omega_{A,m}(C_m-a_{m,r}),
                                                        \tag{4.8}\\
 {1\over2}\sum_{q\le H}{1\over c_q}
       \|\mu_q^G-\mu_q^F\|_1
   &\le\mathscr A^{\rm tag}_{A,m,r}.                 \tag{4.9}
\end{aligned}
\]

Since \(W=(2m+1)C_m\), if \(r/\sqrt m\to\kappa\), then

\[
 {\mathscr A^{\rm tag}_{A,m,r}\over W}
       \longrightarrow2\kappa J_A\alpha,
 \tag{4.10}
\]

along every subsequence on which \(\alpha_r\to\alpha\). In particular
(0.8) follows by \(\alpha_r\le1\).

Equations (2.2)--(2.3) prove only

\[
                         \alpha_r\ge{4\over9r}+o(r^{-1}).
 \tag{4.11}
\]

Thus the currently certified part of (4.8) is \(o(W)\). To turn the
all-block pair into a critical active seed, one must still prove

\[
                         \liminf_{r\to\infty}\alpha_r>0
 \tag{4.12}
\]

on a positive-density root set, or a weaker physical theorem giving the
same \(\Theta(W)\) retained action after collisions. The fact that
\(\eta_r\) moves \(\Theta(r)\) coordinate *positions in its definition*
does not by itself prove (4.12) for the conjugated MSW row words.

## 5. Exact conjugacy hinge with backgrounds and collisions

Consider one fixed context and one depth after all its internal row/start
collisions have been merged. Put

\[
 u=U^F_{C,q},\qquad v=\eta_{C*}u,
 \qquad a=\ell_q-\beta_q,
 \tag{5.1}
\]

where \(\ell_q\) is every occurrence not in this context and \(\beta_q\)
is the chosen balanced quota. On a nontrivial orbit
\(\{T,T'\}\), \(T'=\eta_CT\), the exact new-minus-old hinge is

\[
\boxed{
 \Delta_{T,T'}=
 (a_T+u_{T'})_+ +(a_{T'}+u_T)_+
 -(a_T+u_T)_+ -(a_{T'}+u_{T'})_+.}
 \tag{5.2}
\]

Writing \(I_u\) for the interval between \(u_T,u_{T'}\), and \(I_a\) for
the interval between \(-a_T,-a_{T'}\), integration of the hinge derivative
shows

\[
 |\Delta_{T,T'}|=|I_u\cap I_a|,
 \tag{5.3}
\]

with sign opposite to
\((u_T-u_{T'})(a_T-a_{T'})\). Consequently

\[
 \boxed{
 |\Delta_{T,T'}|
 \le\min\{|u_T-u_{T'}|,|a_T-a_{T'}|\}.}
 \tag{5.4}
\]

Summing the two-point orbits gives

\[
 \boxed{
 |K_{\beta_q}(\ell_q+v)-K_{\beta_q}(\ell_q+u)|
 \le{1\over2}\min\{\|u-\eta_{C*}u\|_1,
                    \|a-\eta_{C*}a\|_1\}.}
 \tag{5.5}
\]

Fixed targets contribute zero. Thus an \(\eta_C\)-invariant effective
background \(a\) makes the entire deterministic context switch hinge-flat.
The local conjugate creates no cap descent before it meets an asymmetric
physical background.

For several contexts, (5.2)--(5.5) may be applied sequentially, but the
effective background for a later context includes all earlier choices.
Summing isolated formal gains without recomputing this background is not
valid.

## 6. A sharp connected-context zero-margin obstruction

The following lemma is independent of conjugacy and explains why a large
connected local overlay is dangerous for CRH at zero margin.

### Theorem 6.1 (one-bit mean relief is paid by its exact remainder)

Let one recoverable physical target block have two equal-mass endpoint
load vectors \(x^0,x^1\), with arbitrary fixed backgrounds already
included, and let \(\beta\) be any quota vector. Choose endpoint one with
probability \(t\in[0,1]\). Put

\[
 H_e=\sum_T(x^e(T)-\beta(T))_+,
 \qquad
 \Phi(t)=\sum_T((1-t)x^0(T)+tx^1(T)-\beta(T))_+,
 \tag{6.1}
\]

and

\[
 e={1\over2}\|x^1-x^0\|_1,
 \qquad
 R(t)={1\over2}\sum_T
    \sqrt{\operatorname {Var}(x^{\varepsilon}(T))}
      =\sqrt{t(1-t)}\,e.
 \tag{6.2}
\]

Then

\[
 \boxed{\Phi(t)+R(t)\ge\min\{H_0,H_1\}.}
 \tag{6.3}
\]

#### Proof

The positive-part objective is \(1\)-Lipschitz in half-\(\ell^1\) on
equal-mass vectors. The mean vector is at half-\(\ell^1\) distance \(te\)
from \(x^0\) and \((1-t)e\) from \(x^1\). Hence

\[
 \Phi(t)\ge H_0-te,
 \qquad
 \Phi(t)\ge H_1-(1-t)e.
\]

It follows that

\[
 \Phi(t)\ge\min(H_0,H_1)-\min(t,1-t)e.
\]

Finally
\(\sqrt{t(1-t)}\ge\min(t,1-t)\), which proves (6.3). \(\square\)

The weighted multidepth form follows by applying the proof at each depth
with weight \(1/c_q\). Suppose now that

1. the direct local full \(X/Y\) overlay is connected, so one first-fringe
   context contributes one bit; and
2. the physical target blocks of different contexts are recoverable and
   disjoint.

Then every target depends on only one context bit. Its variance depends
only on that bit's marginal, so arbitrary correlations between different
bits do not alter (6.2). Summing (6.3) gives

\[
 \boxed{
 \Phi_\beta(\mathbb P)+\mathcal R_\beta(\mathbb P)
 \ge\sum_C\min\{H_C(F),H_C(G)\}.}
 \tag{6.4}
\]

For the all-block conjugate, when the effective background/quota is
\(\eta_C\)-invariant, (5.2) gives \(H_C(F)=H_C(G)\). In that natural
collision-free symmetric case, fractional mixing plus zero-margin rounding
cannot improve the deterministic endpoint objective at all.

The hypotheses of (6.4) are substantive. First-fringe row packets are
disjoint, but their *shadow targets* need not be disjoint. If physical
targets merge across contexts, negative covariance can lower the sum of
square roots in the CRH remainder. Likewise a fragmented local overlay
provides several bits in one context. These are precisely the two escapes
not covered by Theorem 6.1.

For comparison, the standalone raw first column gives a completely
explicit instance. Put

\[
 w_j=C_{j-1}C_{r-j}.
\]

The canonical endpoint has \(w_j\) at \(2j\); the conjugate endpoint has
\(w_j\) at \(2j+1\) for \(j<r\); both have \(w_r=C_{r-1}\) at \(2r\).
For a whole-factor Bernoulli mixture with parameter \(t\), zero background,
and constant hard cap \(p\), its exact mean hinge and remainder are

\[
\begin{aligned}
 \Phi_1(t)
 &=\sum_{j<r}\left[((1-t)w_j-p)_+
                         +(tw_j-p)_+\right]
      +(C_{r-1}-p)_+,\\
 \mathcal R_1(t)
 &=\sqrt{t(1-t)}\,(C_r-C_{r-1}).
 \tag{6.5}
\end{aligned}
\]

Theorem 6.1 gives

\[
 \Phi_1(t)+\mathcal R_1(t)
 \ge\sum_{j<r}(w_j-p)_+ +(C_{r-1}-p)_+.
 \tag{6.6}
\]

Thus even in the projection where the conjugate visibly splits every
nonterminal even bin from its odd mate, the exact zero-margin rounding
certificate cannot beat the deterministic endpoint when the entire
overlay is one bit. This is a diagnostic identity, not a substitute for
the shallow ambient prefix/suffix tensor.

## 7. Exact implication boundary

Proved in this report:

1. the complete two-sided critical-lift row/start tensor
   (3.2), (3.9);
2. the aggregate context coboundary (3.6), including both collars;
3. the component transport law (3.7);
4. the critical action ceiling with exact constant \(2\kappa J_A\);
5. the exact active-cut statistic and the fact that the first matching
   proves only \(\alpha_r=\Omega(1/r)\);
6. the background-sensitive orbit hinge (5.2)--(5.5); and
7. the connected, target-disjoint zero-margin obstruction (6.4).

Not proved:

* a uniform component classification for the direct all-block overlay;
* positive-density linear row-word activity (4.12);
* context recoverability or, conversely, a useful cross-context collision
  theorem for the actual first-fringe shadows;
* a directed protected-mass estimate after all physical collisions; or
* targetwise covariance \(o(W)\) in the merged carrier system.

Accordingly the all-block conjugate is a legitimate explicit critical
candidate, but it has not met CRH. If its overlay is connected and its
carriers are recoverable, Theorem 6.1 gives a sharp no-go. If either
hypothesis fails, the exact surviving task is to exploit the resulting
fragmentation or target merging in (3.7)--(3.8) and verify the actual CRH
mean and covariance inequalities.
