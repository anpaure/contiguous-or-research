# Audit of the rank-twisted macroblock packet tiling

Date: 2026-07-26

Audited source:
`MATH_THEOREM_RANK_TWISTED_MACROBLOCK_PACKET_TILING_20260726.md`.

Method: pure mathematics only.

## 0. Verdict

The owner-packing theorem is correct.  In particular:

1. rank-dependent matchings define a genuine disjoint partition of every
   local Boolean lattice;
2. tensoring those partitions and subdividing each sufficiently large
   orientation cube gives an owner-disjoint physical \(Q_r\) near-factor;
3. the union over all local-rank vectors in the low-dimension estimate costs
   only \(2^{o(m)}\), so the leave is indeed \(2^{m+o(m)}\); and
4. every selected physical axis joins \(A_j\) to \(C_j\).

Two qualifications should be recorded.

* The statement that every depth-\(q\) window uses exactly \(q\) crossing
  axes is true for an installed return-free/isometric compiler and
  \(1\le q\le r\).  A bare cube has no distinguished windows, and an
  arbitrary non-return-free walk need not use \(q\) distinct axes.
* The construction removes a single matching common to the entire middle
  layer, but it does **not** remove fixed-frame status structure inside a
  packet.  Every packet has a frozen local-rank vector, hence one frozen
  product matching and one frozen full/empty/split status vector.  The
  construction is a rank-stratified union of fixed-frame packets, not
  within-packet frame motion.

There is also one harmless wording correction.  Under the theorem's general
hypothesis \(d=m^{o(1)}\), the residual factor \(2^{O(d)}\) is
subexponential, not necessarily polynomial.  It is polynomial for the
displayed choice \(d=\Theta(\log m)\).

The first exact source/target compatibility kernel is derived in Section 5.
It reduces the remaining Hall problem to cyclic cross-correlations evaluated
at a shift determined by the target rank and the number of axes assigned to
the block.

## 1. The local rank-dependent cells really partition

Fix \(B=A\mathbin{\dot\cup}C\), with \(|A|=|C|=d\).  For each
\(0\le k\le2d\), let \(M_k\) be a perfect matching from \(A\) to \(C\).
For a \(k\)-set \(X\), its zero/one/two endpoint status on every edge of
\(M_k\) is unique.  Fixing the zero and two statuses and allowing the one
statuses to orient freely gives an orientation cube.

These cubes are disjoint and partition \(\binom Bk\).  A cube move swaps the
occupied endpoint of one split edge, so it preserves rank \(k\); therefore
it never changes the matching \(M_k\) used to define the cell.  Since the
rank layers are disjoint,

\[
 2^B=\mathop{\dot\bigcup}_{k=0}^{2d}\binom Bk
\]

is partitioned even though the matching varies with \(k\).

For

\[
 M_k=\{a_i c_{i+k}:i\in\mathbb Z_d\},
 \tag{1.1}
\]

the union over \(k\) is \(K_{d,d}\), because every offset occurs modulo
\(d\).  This proves the claimed global frame diversity, but it does not
alter the preceding within-cell constancy.

Tensoring the local partitions and freezing the residual coordinates gives
a disjoint partition of the full Boolean lattice.  Restricting to total rank
\(m\) preserves disjointness.  A product cell with \(S\) split axes is a
literal \(Q_S\); choosing a deterministic \(r\)-subset of those axes and
freezing the other orientations in all possible ways partitions it into
literal \(Q_r\)'s.  Thus the owner argument contains no compatibility gap.

## 2. The low-dimension count, including the union over rank vectors

Put

\[
 b=\lfloor m/d\rfloor,\qquad N=db,
 \qquad \rho=2m-2db<2d.
\]

Fix a complete local-rank vector \(\mathbf k\).  It fixes a matching on each
macroblock and hence a matching with \(N\) edges on the nonresidual
coordinates.  For one edge, two of its four endpoint states are split and
two are nonsplit.  Therefore the exact number of nonresidual subsets with
exactly \(s\) split edges is

\[
 2^N\binom Ns.
 \tag{2.1}
\]

Consequently

\[
 \#\{X:S_{\mathbf k}(X)<r\}
 =2^N\sum_{s<r}\binom Ns
 =2^{N+o(m)}
 =2^{m+o(m)},
 \tag{2.2}
\]

because \(r=o(m)\), \(N=m-O(d)\), and hence
\(\log_2\sum_{s<r}\binom Ns=o(m)\).

The subsets which actually induce \(\mathbf k\) form a subfamily of the
family counted in (2.2).  There are at most

\[
 (2d+1)^b,
 \qquad
 \log_2(2d+1)^b=O\!\left({m\log d\over d}\right)=o(m)
 \tag{2.3}
\]

rank vectors.  The union bound is therefore valid even though different
vectors use different matchings.  Finally the residual coordinates cost

\[
 2^\rho\le2^{2d}=2^{o(m)}.
 \tag{2.4}
\]

Multiplying (2.2)--(2.4) proves

\[
 L\le2^{m+o(m)}.
 \tag{2.5}
\]

Restricting to rank \(m\) only decreases this number.  Since
\(W=\binom{2m}m=2^{2m-o(m)}\), equation (2.5) is \(o(W/H)\) uniformly for
every \(H\le m\).

Thus there is no missing exponential factor in the union over rank vectors.
The source proof merely leaves the cardinality conversion from its binomial
probability implicit; equation (2.2) supplies it.

## 3. Crossing-axis claim

Every flexible edge of every local cell belongs to some \(M_{j,k}\), and
each such edge has one endpoint in \(A_j\) and one in \(C_j\).  Selecting an
\(r\)-subset of flexible axes cannot change that fact.  Hence every retained
packet has exactly

\[
 s(P)=r
 \tag{3.1}
\]

cross-half axes.  If a base coordinate partition refines the displayed
halves, the endpoints also lie in different atoms of that refinement.

For an isometric \(C_{2r}\) factor, the direction word is \(\pi\pi\), with
\(\pi\) a permutation of the \(r\) axes.  Therefore every consecutive
window of length \(q\le r\) uses exactly \(q\) distinct axes, all of which
cross halves.  This verifies the occurrence-toll claim in the compiler
regime \(q\le H=o(r)\).  The qualification ``isometric/return-free and
\(q\le r\)'' should accompany the sentence in Theorem 0.1.

## 4. The surviving rank-conditioned status invariant

For every retained packet \(P\), the following data are constant on all of
its owners:

\[
 \mathbf k(P)=(k_1,\ldots,k_b),
 \qquad
 M(P)=\bigcup_jM_{j,k_j},
 \tag{4.1}
\]

together with the full and empty edge sets of the product status cell.  Only
the orientations of selected split edges vary.

Thus the claim that there is no *single* global matching common to all rank
layers is correct, but the stronger interpretation ``there is no fixed
frame/status invariant'' would be false.  The exact surviving invariant is

\[
 \boxed{\text{local rank vector }+\text{ its rank-selected product matching }
        +\text{ the product status profile}.}
 \tag{4.2}
\]

In particular, a depth-\(q\) window does not change frames while it moves
through one packet.  Rank twisting only changes the frame when one passes
to a different rank-vector stratum.  This prevents direct reuse of a single
global-matching Hall cut, but it leaves open a disaggregated Hall cut over
\(\mathbf k\).

## 5. First exact source/target compatibility formula

Write

\[
 x_i(Y)=\mathbf1_{\{a_i\in Y\}},
 \qquad
 y_i(Y)=\mathbf1_{\{c_i\in Y\}},
\]

and, for the cyclic matching of offset \(s\), define

\[
\begin{aligned}
 f_s(Y)&=\sum_{i\in\mathbb Z_d}x_i(Y)y_{i+s}(Y),\\
 e_s(Y)&=\sum_{i\in\mathbb Z_d}(1-x_i(Y))(1-y_{i+s}(Y)).
\end{aligned}
\tag{5.1}
\]

These are respectively the numbers of full and empty edges of \(M_s\).
If \(t=|Y|\), then

\[
 e_s(Y)=d-t+f_s(Y).
 \tag{5.2}
\]

### 5.1 Lower targets

Let \(T\) be a global lower target of rank \(m-q\), put
\(T_j=T\cap B_j\), and write \(t_j=|T_j|\).  Suppose \(\ell_j\) of the
\(q\) completed axes lie in block \(j\).  Then necessarily

\[
 \ell_j\ge0,
 \qquad
 \sum_j\ell_j=q,
 \qquad
 k_j=t_j+\ell_j.
 \tag{5.3}
\]

The rank-twisted frame in this block is therefore \(M_{t_j+\ell_j}\).
The target is physically liftable in this allocation exactly when

\[
 \boxed{
 \ell_j\le e_{t_j+\ell_j}(T_j)\quad\text{for every }j.}
 \tag{5.4}
\]

Indeed, the \(\ell_j\) used axes must be empty in the lower intersection;
choosing any \(\ell_j\) such empty edges and one source orientation on each
produces a unique local source.  Hence the exact number of raw compatible
middle source owners in the full rank-twisted cell atlas is

\[
 \boxed{
 C_q^-(T)=
 2^q\!\sum_{\substack{\ell_1+\cdots+\ell_b=q\\\ell_j\ge0}}
 \prod_{j=1}^b
 \binom{e_{t_j+\ell_j}(T_j)}{\ell_j}.}
 \tag{5.5}
\]

As usual a binomial coefficient is zero when its lower argument is
inadmissible.  Residual coordinates are frozen and agree in source and
target.

Formula (5.5) counts physical source owners for which *some* return-free
\(q\)-axis path has lower intersection \(T\).  The deterministic selection
of \(r\) axes inside a large cell and the installed compiler can only reduce
this support; (5.5) is not yet the literal occurrence count of the chosen
factor.

### 5.2 Upper targets

Let \(U\) have rank \(m+q\), put \(u_j=|U\cap B_j|\), and use the same
allocation \(\boldsymbol\ell\).  Now the source rank is

\[
 k_j=u_j-\ell_j,
 \tag{5.6}
\]

and every used edge must be full in the upper union.  Thus the exact local
condition is

\[
 \boxed{
 \ell_j\le f_{u_j-\ell_j}(U_j)\quad\text{for every }j,}
 \tag{5.7}
\]

and the raw compatible-source count is

\[
 \boxed{
 C_q^+(U)=
 2^q\!\sum_{\substack{\ell_1+\cdots+\ell_b=q\\\ell_j\ge0}}
 \prod_{j=1}^b
 \binom{f_{u_j-\ell_j}(U_j)}{\ell_j}.}
 \tag{5.8}
\]

Equations (5.4) and (5.7) exhibit the exact twist: the cyclic correlation is
evaluated at a shift which itself depends on the allocation \(\ell_j\).

### 5.3 Exact one-block profile ratio

There is also a closed profile kernel.  Fix a lower allocation \(\ell\),
put \(k=t+\ell\), and measure statuses relative to \(M_k\).  If the source
has \(f\) full edges, then the numbers of source owners and lower targets in
the corresponding profile are

\[
\begin{aligned}
 V_{d;k,f}
 &=\frac{d!\,2^{k-2f}}
        {f!\,(d-k+f)!\,(k-2f)!},\\
 T^-_{d;k,\ell,f}
 &=\frac{d!\,2^{k-2f-\ell}}
        {f!\,(d-k+f+\ell)!\,(k-2f-\ell)!}.
\end{aligned}
\tag{5.9}
\]

Therefore

\[
 \boxed{
 {T^-_{d;k,\ell,f}\over V_{d;k,f}}
 =2^{-\ell}
  { (k-2f)_{\ell}\over(d-k+f+\ell)_{\ell}},}
 \tag{5.10}
\]

where \((z)_\ell=z(z-1)\cdots(z-\ell+1)\).  Equivalently, the exact local
incidence double count is

\[
 T^-_{d;k,\ell,f}\,2^\ell
       \binom{d-k+f+\ell}{\ell}
 =V_{d;k,f}\binom{k-2f}{\ell}.
 \tag{5.11}
\]

The upper formula is the complement of (5.9)--(5.11).  For a fixed global
allocation and profile vector, the source/target ratio is the product of
the local ratios (5.10).

This is the first exact Hall kernel for the construction.  Rank twisting
changes which literal targets occupy a profile at each allocation, but it
does not change the local factorial ratio itself.  Near the central profile
\(k\approx d\), \(f\approx d/4\), the two falling-factorial scales in
(5.10) nearly cancel the factor \(2^{-\ell}\); the kernel is therefore
critical rather than automatically expanding.

### 5.4 Literal compatibility after installing the compiler

For completeness, let \(J_q(X)\) be the set of the next \(q\) physical
directions in the installed return-free cycle starting at owner \(X\).
Every \(e\in J_q(X)\) is a split edge of the frozen product matching
\(M(P(X))\).  Write \(x_e\) for its endpoint contained in \(X\).  Then the
literal signed targets emitted at this start are exactly

\[
 \boxed{
 T_q(X)=X\setminus\{x_e:e\in J_q(X)\},
 \qquad
 U_q(X)=X\cup\bigcup_{e\in J_q(X)}(e\setminus X).}
 \tag{5.12}
\]

Thus a target is actually hit if and only if it occurs in (5.12) for some
source owner.  Equations (5.5) and (5.8) enumerate all physical lifts before
the selected-axis and direction-order restrictions; equation (5.12) is the
exact incidence map after those restrictions.  Passing from the former to
the latter is part of the remaining compiler/Hall theorem.

## 6. Correct boundary

The construction proves owner packing and maximal cross-half axis density.
It does not yet prove target coverage.  The remaining problem is to combine
the overlapping allocation kernels (5.4)--(5.10), the deterministic
\(Q_r\)-axis selection, and one common all-depth compiler into a literal
source-to-target Hall theorem.

No existing fixed-global-frame obstruction applies verbatim, because
different rank vectors use different matchings.  Conversely, the mere fact
that \(\bigcup_kM_k=K_{d,d}\) is only potential reachability; it does not
erase the rank-conditioned status invariant (4.2) or prove simultaneous
coverage.
