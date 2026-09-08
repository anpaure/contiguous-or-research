# The second-order exposure signal and the nonfactorizing Venn remainder

**Date:** 2026-08-22

**Status:** unconditional inclusion--exclusion reduction, exact mass bound,
exact finite Gram calibration, and a counterexample to boundary-component
factorization.  Harmonic control of the higher-order remainder remains open.

## 1. Exact cancellation to order two

Fix the identity punctured configuration `E_0`.  For a rank-`s` target
`S`, `s in {r,r-1}`, write

\[
 e_s(S)=\sum_{F:S\in F_s}(|F\cap E_0|-1)_+.                   \tag{1.1}
\]

For `J subseteq E_0`, let `deg(S,J)` denote the number of configurations
containing `S` and every target in `J`; if `S` itself belongs to `J`, the
repeated condition is imposed only once.

### Theorem 1.1 (exposure begins at two blockers)

\[
 \boxed{
 e_s(S)=\sum_{\substack{J\subseteq E_0\\|J|\ge2}}
                 (-1)^{|J|}\deg(S,J).}                         \tag{1.2}
\]

Define the second-order vector and remainder by

\[
 W_{2,s}(S)=\sum_{\{T,U\}\in{E_0\choose2}}\deg(S,T,U),
 \qquad R_s=W_{2,s}-e_s.                         \tag{1.3}
\]

Then `R_s(S)>=0` for every target.

#### Proof

For every integer `t>=0`,

\[
 (t-1)_+=\sum_{m=2}^{t}(-1)^m{t\choose m}.          \tag{1.4}
\]

Indeed the right side is zero at `t=0`, while for `t>=1` it is
`-[1-t]=t-1` by the binomial theorem.  Apply (1.4) with
`t=|F cap E_0|`, multiply by `1_(S in F_s)`, and swap the finite sums.
This proves (1.2).  Moreover

\[
 {t\choose2}-(t-1)_+={t-1\choose2},                \tag{1.5}
\]

with both sides zero at `t=0`; summing (1.5) proves nonnegativity. `square`

Thus the degree term and every one-blocker term cancel exactly.  The first
new compensated direction is the triple-codegree operator `W_2`, not the
full zero-avoidance partition function.

## 2. The higher-order remainder has only `O(1/r)` of the mass

Put

\[
 M_a(E_0)=\sum_F{|F\cap E_0|\choose a}.             \tag{2.1}
\]

Every configuration contains exactly `2r` targets on either central shore.
Summing (1.3)--(1.5) over one shore gives the exact identities

\[
 \boxed{
 \|W_{2,s}\|_1=2rM_2(E_0),
 \qquad
 \|R_s\|_1=2r\sum_F{|F\cap E_0|-1\choose2}
             \le2rM_3(E_0).}                       \tag{2.2}
\]

The following boundary estimate suffices here.

### Lemma 2.1 (self-contained moment scale)

There is an absolute constant `C` such that, for every
`J subseteq E_0`, `|J|>=2`,

\[
 {\deg(J)\over D_M}\le C^{|J|}r^{2-v(J)},           \tag{2.3}
\]

where `v(J)` is the number of incident vertices of the boundary-edge
subgraph of `J`.  Consequently

\[
                         M_2(E_0)=\Theta(D_M),
 \qquad M_3(E_0)=O(D_M/r).                           \tag{2.4}
\]

#### Proof

Anchor one target.  Its retained positional start has at most `b-1`
choices, and each additional rank-`r` or rank-`(r-1)` interval has at most
four relative starts with a prescribed intersection with the anchor.
For each start tuple, label assignments contribute the product of the
Venn-cell factorials.  Refining those cells by the `v(J)` cyclic boundary
gaps loses at most a factor `8` per added target: each new interval adds
two cuts, and the only uncancelled split has a complementary piece of size
at most three.  Log-convexity of factorials then maximizes the gap product
by making one gap as large as possible, giving
`C^|J| r^(2-v(J))` after division by
`D_M=2r r!(r+1)!`.  This proves (2.3).

The boundary graph has maximum degree four and no triangles once `b>=11`;
the finitely many smaller cases alter only constants.  For pairs, there
are `O(r)` choices with `v=3` and `O(r^2)` with `v=4`, so (2.3) gives
`M_2=O(D_M)`.  The containment path has `Theta(r)` pairs, each of exact
codegree

\[
                         (4r-1)(r-1)!(r+1)!=\Theta(D_M/r),    \tag{2.5}
\]

giving the reverse bound.  For triples, the possibilities `v=4,5,6`
number respectively `O(r),O(r^2),O(r^3)`.  Equation (2.3) bounds all three
totals by `O(D_M/r)`, proving (2.4). `square`

Consequently

\[
 \boxed{
 {\|R_s\|_1\over\|W_{2,s}\|_1}
 \le {M_3(E_0)\over M_2(E_0)}
 =O(r^{-1}).}                                       \tag{2.6}
\]

This is a strong total-mass approximation.  It is not yet a Gram-angle
approximation: a small signed harmonic component can determine a direction
after the vector is normalized.

## 3. Exact finite Gram calibration of the second-order signal

Let `alpha_(r,j)^(2)` be the dimensionless five-vector angle obtained by
replacing the two full exposure vectors by `W_(2,r),W_(2,r-1)`.
Complete-catalogue enumeration and exact harmonic Gram arithmetic give

\[
 \boxed{
 \alpha_{4,2}^{(2)}
 ={496145882096395115\over2871985372664539779}
 =0.1727536243\ldots}                                \tag{3.1}
\]

and

\[
\boxed{\begin{aligned}
 \alpha_{5,2}^{(2)}
 &= {920020551945270166975711
       \over12998197791101807219670856}
 =0.0707806241\ldots,\\
 \alpha_{5,3}^{(2)}
 &= {596657511940736589690394281
       \over1103569337664148347762679657}
 =0.5406615530\ldots.
\end{aligned}}                                                \tag{3.2}
\]

Multiplication by the relative-density orbit factors gives

\[
 \widehat\sigma_{4,2}^{2,(2)}=0.6910144972\ldots,
 \quad
 \widehat\sigma_{5,2}^{2,(2)}=1.8200731914\ldots,
 \quad
 \widehat\sigma_{5,3}^{2,(2)}=5.7928023535\ldots.             \tag{3.3}
\]

For comparison, the corresponding full-exposure values are
`0.7968568099...`, `2.3498049481...`, and `5.5737108700...`.
Thus order two already captures the observed finite scale and ordering,
but three data points are not an asymptotic theorem.

## 4. Why literal boundary-component factorization is false

The boundary graph represents a base middle target `M_i` by
`{i,i+r}`.  At `r=4`, take

\[
 M_1=\{1,2,3,4\},\qquad M_2=\{2,3,4,5\}.            \tag{4.1}
\]

Their boundary edges `{1,5}` and `{2,6}` are vertex-disjoint, so they are
two disconnected singleton boundary components.

### Proposition 4.1 (exact nonfactorization)

For the two rank-four roots

\[
 S_0=\{0,1,2,5\},\qquad S_1=\{0,1,6,7\},            \tag{4.2}
\]

literal enumeration of the `9!` directed words gives

\[
\begin{array}{c|cc|c}
S&\deg(S,M_1)&\deg(S,M_1,M_2)&
 \deg(S,M_1,M_2)/\deg(S,M_1)\\ \hline
S_0&672&0&0\\
S_1&1008&432&3/7.
\end{array}                                                   \tag{4.3}
\]

Hence a boundary component disjoint from the root component does not
contribute an `S`-independent factor.

The reason is global Venn-cell merging.  For a root `S` and a family
`J={T_1,...,T_m}`, anchor the positional start of `S`.  The exact state is
the pair of Venn-cell count families

\[
 n_{\eta,\epsilon}
 =|S^\eta\cap\{x:(\mathbf1_{x\in T_i})_{i=1}^m=\epsilon\}|,
 \quad \eta\in\{0,1\},\ \epsilon\in\{0,1\}^m.      \tag{4.4}
\]

For every compatible tuple of positional starts, the label-assignment
factor is

\[
                         \prod_{\eta,\epsilon}n_{\eta,\epsilon}!.       \tag{4.5}
\]

Disconnected boundary gaps having the same global membership vector merge
inside one factorial in (4.5), coupling the components.

There is an exact mixture representation,

\[
 n!=\int_0^\infty e^{-x}x^n\,dx,                  \tag{4.6}
\]

which makes (4.5) a product conditional on one Gamma variable per global
Venn cell.  But (4.4) has up to `2^(m+1)` cells.  No bounded-dimensional
saddle variable or local transfer state follows from (4.6).  Finding a
controlled compression of this growing Venn state is a new theorem, not a
consequence of boundary-graph connectedness.

## 5. Correct next gate

The most economical positive route is now:

1. compute the module Gram of the explicit triple-codegree vectors `W_2`
   and prove
   `inf_j alpha_(r,j)^(2) Theta_(r,j)>=r^(-C)`;
2. strengthen (2.4) from total mass to the normalized harmonic Gram norm
   required by the stability lemma; and
3. absorb `R_s` as a perturbation.

For fixed `j=3`, step 1 is a finite Hahn/Venn sum over base target-pair
types.  In the bulk and top regimes it requires a uniform positive
representation or saddle analysis.  Step 2 cannot be replaced by (2.4):
the latter contains no lower bound on the harmonic norm of `W_2` and no
signed correlation estimate with the shallow deck.

The alternative log-partition route must retain the global Venn merge
state or prove that its induced cumulants have a low-rank saddle
approximation.  Proposition 4.1 rules out deleting disconnected components
before such a theorem is established.

## 6. Exact verifiers

Run

```text
python3 scratch/verify_exposure_zero_avoidance_decomposition_20260822.py
```

It verifies (1.2)--(1.5) targetwise at `r=4`, checks both angles in
Sections 3--4, and certifies the counts (4.3).

The exact `r=5` second-order angles are checked with GMP arithmetic by

```text
clang++ -std=c++20 -O3 -march=native -pthread -Wall -Wextra -Wpedantic \
  $(pkg-config --cflags gmpxx) \
  scratch/research_r5_compensated_gram_angles_20260822.cpp \
  $(pkg-config --libs gmpxx) \
  -o /tmp/research_r5_compensated_gram_angles_20260822
/tmp/research_r5_compensated_gram_angles_20260822
```

It independently streams all `11!` configurations, constructs `W_2`, and
checks both fractions in (3.2) exactly.
