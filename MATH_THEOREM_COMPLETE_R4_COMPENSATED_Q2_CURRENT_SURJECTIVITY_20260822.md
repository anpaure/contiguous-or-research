# The complete `r=4` compensated kernel realizes every balanced depth-two current

**Date:** 2026-08-22  
**Status:** exact finite theorem with an integral modular-rank certificate.
This proves genuine shallow freedom in the compensated Gibbs polytope at
one nontrivial rank.  It is not yet an all-`r` theorem and therefore does
not close Gate B.

## 1. Three incidence maps

Put `Omega=[9]`.  For a word `w=(w_0,...,w_8)`, read subscripts modulo
nine and define

\[
 E(w)=\{(M,I_4^w(s)):1\le s\le8\}
 \mathbin{\dot\cup}
 \{(L,I_3^w(s)):1\le s\le8\},                     \tag{1.1}
\]

where `I_k^w(s)={w_s,...,w_(s+k-1)}`.  Let

\[
 \mathcal C=\{E(w):w\in S_9\},\qquad
 \mathcal V={\Omega\choose4}\mathbin{\dot\cup}{\Omega\choose3}.
                                                                    \tag{1.2}
\]

Containment-path reconstruction makes `w -> E(w)` injective, so the
catalogue has `9!` labelled columns.

For completeness, put `L_s=I_3^w(s)` and `M_s=I_4^w(s)`.  The containment
graph of the retained tagged targets is

\[
 L_1-M_1-L_2-M_2-\cdots-L_8-M_8.
\]

The shores distinguish its endpoints and hence orient the path.
The differences `M_s-L_s={w_(s+3)}` recover eight positions of `w`, and
the unused label recovers the last one.  This proves injectivity directly.

The central incidence matrix is

\[
                         A_{vG}=\mathbf1_{\{v\in G\}}.        \tag{1.3}
\]

For the rooted duplicate-exposure matrix it is convenient to omit the
positive row-degree normalization:

\[
 \widetilde P_{vG}
   =\sum_{F\in\mathcal C:\,v\in F}(|F\cap G|-1)_+.           \tag{1.4}
\]

Multiplying every target row by its reciprocal complete-catalogue degree
gives the normalized matrix `P` used by the compensated-rate theorem.
Thus `ker P=ker tilde P`.

Every `G=E(w)` remembers its unique word.  Define the depth-two lower
window incidence

\[
 Q_{XG}=\mathbf1\{X=I_2^w(s)\text{ for some }s\in\mathbb Z_9\},
 \qquad X\in{\Omega\choose2}.                       \tag{1.5}
\]

Each column of `Q` is the edge set of a Hamilton nine-cycle on `Omega`.
Finally stack

\[
                              B=\begin{bmatrix}A\\ \widetilde P\end{bmatrix}.
                                                                  \tag{1.6}
\]

A signed rate perturbation `eta` is compensated exactly when `B eta=0`.

## 2. Exact ranks

### Theorem 2.1 (rank certificate)

Over the rationals,

\[
 \boxed{
       \operatorname {rank}B=417,\qquad
       \operatorname {rank}Q=28,\qquad
       \operatorname {rank}\!\begin{bmatrix}B\\Q\end{bmatrix}=444.}
                                                               \tag{2.1}
\]

#### Proof: upper bounds

There are 210 target rows in each of `A` and `tilde P`, hence 420 rows in
`B`.  Three independent relations hold.

First, every configuration has eight targets on each central shore:

\[
 \sum_{v\in{\Omega\choose4}}A_{vG}
 =\sum_{v\in{\Omega\choose3}}A_{vG}=8.             \tag{2.2}
\]

Second, swapping the sums in (1.4) gives

\[
 \sum_{v\in{\Omega\choose4}}\widetilde P_{vG}
 =\sum_{v\in{\Omega\choose3}}\widetilde P_{vG}
 =8\sum_{F\in\mathcal C}(|F\cap G|-1)_+.          \tag{2.3}
\]

The last sum in (2.3) is a constant `D_0>0`, because the coordinate action
is transitive on the complete catalogue.  Therefore

\[
 \sum_{v\in{\Omega\choose4}}\widetilde P_{vG}
 =D_0\sum_{v\in{\Omega\choose4}}A_{vG}.            \tag{2.4}
\]

The shore difference in (2.2), the shore difference in (2.3), and (2.4)
are independent row relations.  Hence

\[
                              \operatorname {rank}B\le417.    \tag{2.5}
\]

For `Q`, every Hamilton-cycle column has coordinate degree two.  The eight
differences between its nine coordinate-degree row sums are independent,
so

\[
                              \operatorname {rank}Q\le36-8=28.\tag{2.6}
\]

Moreover `sum_X Q_(XG)=9` for every column, while
`sum_(v in binom(Omega,4)) A_(vG)=8`.  Thus the constant row belongs to
both row spaces.  Equations (2.5)--(2.6) give

\[
 \operatorname {rank}\!\begin{bmatrix}B\\Q\end{bmatrix}
 \le417+28-1=444.                                  \tag{2.7}
\]

#### Proof: matching lower bounds

We give an exact minor certificate over the prime field

\[
                              \mathbb F_p,\qquad p=1,000,003. \tag{2.8}
\]

Take the base word `(0,1,...,8)`.  The column (1.4) is evaluated by the
literal integer sum over all `9!` words `F`.  Relabel this base column by
the following 900 explicitly indexed coordinate permutations.  For
`0<=t<900`, let

\[
                  j_t=7919t\pmod {9!},                       \tag{2.9}
\]

and take the permutation of Lehmer rank `j_t` in lexicographic order.
The multiplier 7919 is coprime to `9!`, so these labels are distinct.

Gaussian elimination modulo `p` on those 900 restricted columns gives

\[
 \operatorname {rank}_{\mathbb F_p}B=417,\qquad
 \operatorname {rank}_{\mathbb F_p}Q=28,\qquad
 \operatorname {rank}_{\mathbb F_p}
       \begin{bmatrix}B\\Q\end{bmatrix}=444.       \tag{2.10}
\]

The complete replay is
`scratch/verify_complete_r4_compensated_q2_surjectivity_20260822.py`.
It constructs (1.1), evaluates (1.4) with exact integers, generates (2.9)
by the factorial-number system, and performs the displayed modular
elimination.  A nonzero minor modulo `p` is a nonzero integer minor, so
each rank in (2.10) is a lower bound for the corresponding rational rank
of the full matrix.  The upper bounds (2.5)--(2.7) match them, proving
(2.1).  `square`

## 3. Surjectivity onto balanced pair currents

Let

\[
 \mathcal Z_2=\left\{j\in\mathbb R^{\binom92}:
       \sum_{X\ni a}j_X=0\text{ for every }a\in\Omega\right\}.          \tag{3.1}
\]

The vertex-pair incidence matrix of `K_9` has rank nine: if real numbers
`c_a` satisfy `c_a+c_b=0` for every pair, three distinct coordinates force
all of them to vanish.  Hence

\[
                              \dim\mathcal Z_2=36-9=27.        \tag{3.2}
\]

### Corollary 3.1 (complete compensated shallow freedom)

\[
                              \boxed{Q(\ker B)=\mathcal Z_2.} \tag{3.3}
\]

In particular every rational balanced rank-two current has a rational
signed configuration vector `eta` satisfying

\[
                              A\eta=0,\qquad P\eta=0,
 \qquad Q\eta=j.                                    \tag{3.4}
\]

#### Proof

The standard rank identity gives

\[
 \dim Q(\ker B)
 =\operatorname {rank}\!\begin{bmatrix}B\\Q\end{bmatrix}
   -\operatorname {rank}B=444-417=27.               \tag{3.5}
\]

If `eta in ker B`, summing the incidence equations shows
`sum_G eta_G=0`.  Every `Q`-column is a Hamilton cycle and therefore has
coordinate degree two, so

\[
             \sum_{X\ni a}(Q\eta)_X=2\sum_G\eta_G=0.         \tag{3.6}
\]

Thus `Q(ker B) subseteq Z_2`; dimensions (3.2) and (3.5) force equality.
All matrices are rational, so a rational `j` has a rational solution of
the consistent system (3.4).  `square`

The Haar square current

\[
             -[13]+[23]+[14]-[24]+[15]-[25]-[19]+[29]        \tag{3.7}
\]

lies in `Z_2`.  Corollary 3.1 therefore gives a compensated realization
of (3.7), even though the symmetric-group span of the puncture-averaged
Haar trade itself cannot realize it while preserving `P` (the companion
exposure-detection theorem).

Finally let `lambda^0` be the positive uniform rate law.  For any rational
solution `eta` of (3.4), sufficiently small real `epsilon` makes

\[
                         \lambda^0+\epsilon\eta\ge0.          \tag{3.8}
\]

Hence (3.3) is not merely a signed formal identity: it supplies actual
nearby probability laws in the compensated polytope whose depth-two load
changes in any prescribed balanced direction.

This is a fixed-dimensional existence statement.  The rank calculation
does not bound `epsilon` uniformly in `r`, nor
`max_G|eta_G|/lambda_G^0`; those quantitative bounds are separate and are needed
before such perturbations can drive an asymptotic Gibbs process.

## 4. Scope and next theorem

This resolves one local question decisively.  Rooted-exposure compensation
does **not** freeze deeper windows; its complete `r=4` kernel has the
maximum possible rank-two freedom.  The earlier Haar obstruction says only
that the realizing perturbation must be more global than the obvious
puncture-averaged Haar orbit.

For Gate B, the required next result is an all-`r`, quantitative version of
(3.3), preferably with a norm bound on a right inverse of `Q|_(ker B)` and
with simultaneous currents through the Gaussian depth band.  Such a bound
would turn the compensated Gibbs switching theorem from a strict-improvement
statement into a controlled physical reinforcement law.
