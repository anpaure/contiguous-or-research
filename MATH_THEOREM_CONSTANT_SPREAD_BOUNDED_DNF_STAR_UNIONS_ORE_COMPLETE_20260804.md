# Constant-spread reservoir: bounded monotone DNF unions of principal stars pass protected Ore

**Date:** 2026-08-04  
**Status:** unconditional asymptotic pure-mathematical theorem.  For every
DNF width satisfying `4^h(h+log m)=o(m)`, the single alternative-random constant-spread
reservoir satisfies the protected Ore inequality on every union of
principal up-stars, even when the core ranks vary.  This includes every
tree or other configuration of Hamming-adjacent cores within the width
bound.  The proof gives exact
owner fibres, exact local protected-current gluing, and exact
inclusion--exclusion for the Ore slack.  It does not cover widths outside
the displayed growth condition or arbitrary positive-defect cuts.

No computation, search, or solver output is used.

## 0. Setting

Put

\[
 n=2m-1,\qquad k=m-1,\qquad
 \mathcal L={[n]\choose k},\qquad
 \mathcal U={[n]\choose m}.
\]

Use the single alternative-random constant-spread reservoir `P` from
`MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md`.
Its frozen estimates, valid for all sufficiently large `m`, are

\[
 \lambda_P(B)\le15|B|+2m
 \qquad(B\subseteq\mathcal L),
\tag{0.1}
\]

and, for every nonempty core `C_i` of size `c_i<=m-2`, with
`rho_i=m-c_i`,

\[
 \lambda_P(\mathcal A_{C_i})
 \le2N_{\rho_i},
 \qquad
 N_{\rho_i}:=H_{\rho_i}(m)+m+H_d,
\tag{0.2}
\]

where

\[
 \mathcal A_{C_i}=\{L\in\mathcal L:C_i\subseteq L\},
 \qquad
 H_{\rho_i}(m)=\sum_{j=0}^{\rho_i}{m\choose j},
 \qquad d=O(\sqrt m),\qquad H_d=2^{o(m)}.
\]

Fix distinct nonempty cores

\[
 C_1,\ldots,C_h\subseteq[n],
 \qquad1\le c_i:=|C_i|\le m-2,
\tag{0.3}
\]

and define the monotone DNF cut

\[
 \mathcal A=\bigcup_{i=1}^h\mathcal A_{C_i}.
\tag{0.4}
\]

The width `h` may depend on `m` subject to Theorem 3.1.

## 1. Exact local owner fibre and protected current

For `U in mathcal U`, define its active clause set

\[
 I(U)=\{i:C_i\subseteq U\}.
\]

When `I(U)` is nonempty, put

\[
 J_U=\bigcap_{i\in I(U)}C_i.
\tag{1.1}
\]

For a protected incidence `UL`, let `del(U,L)` be the unique member of
`U minus L`.

### Theorem 1.1 (DNF fibre-intersection law)

At one owner `U`,

\[
 \boxed{
 a_U=
 \begin{cases}
  0,&I(U)=\varnothing,\\
  m-|J_U|,&I(U)\ne\varnothing.
 \end{cases}}
\tag{1.2}
\]

Every nonzero fibre has size at least two.  Its exact protected Ore loss is

\[
 \boxed{
 \lambda_U(\mathcal A)
 =|\{UL\in E(P):\operatorname{del}(U,L)\in J_U\}|.}
\tag{1.3}
\]

Consequently

\[
 \boxed{
 \lambda_P(\mathcal A)
 \le\sum_{i=1}^h\lambda_P(\mathcal A_{C_i})
 \le2\sum_{i=1}^hN_{\rho_i}.}
\tag{1.4}
\]

#### Proof

The lower facets of `U` are indexed by the deleted coordinate `x in U`.
A facet `U-x` satisfies clause `C_i` exactly when

\[
 C_i\subseteq U,
 \qquad x\notin C_i.
\]

Thus, when some clause is active, the selected deletion set is

\[
 \bigcup_{i\in I(U)}(U\setminus C_i)
 =U\setminus J_U,
\]

which proves (1.2).  Since every active core has size at most `m-2`, its
own deletion set already has size at least two.

For a fibre of size at least two, local protected loss is the number of
protected incidences to unselected facets.  Those are exactly the
deletions in `J_U`, proving (1.3).

Every coordinate of `J_U` belongs to every active core.  Hence every
incidence counted by (1.3) is counted by the individual protected loss of
each active clause, and in particular at least once in their sum.  Sum
over owners and apply (0.2). \(\square\)

There is an exact cancellation refinement.  If

\[
 h_U(x)=|\{i\in I(U):x\in C_i\}|,
\]

then

\[
 \boxed{
 \sum_i\lambda_U(\mathcal A_{C_i})-
 \lambda_U(\mathcal A)
 =\sum_{\substack{UL\in E(P)\\ I(U)\ne\varnothing}}
 \left(h_U(\operatorname{del}(U,L))-
 \mathbf1_{\{h_U(\operatorname{del}(U,L))=|I(U)|\}}
 \right).}
\tag{1.5}
\]

Inactive clauses contribute zero.  Formula (1.5) shows why a protected
path can switch from one satisfied clause to another without paying union
loss, even though it exits an individual core star.

## 2. Exact slack inclusion--exclusion

For a set `Q subseteq[n]`, define

\[
 \delta(Q)=
 \left|\{U\in\mathcal U:Q\subseteq U\}\right|
 -\left|\{L\in\mathcal L:Q\subseteq L\}\right|.
\tag{2.1}
\]

It depends only on `q=|Q|`; write the common value as `delta_q`.  Explicitly,

\[
 \delta_q=
 \begin{cases}
 {2m-1-q\choose m-q}-{2m-1-q\choose m-1-q},&0\le q\le m-1,\\
 1,&q=m,\\
 0,&q>m.
 \end{cases}
\tag{2.2}
\]

In particular `delta_0=0`, and for `1<=q<=m-1`, putting
`rho_q=m-q`,

\[
 \delta_q={q\over\rho_q}
 {m+\rho_q-1\choose\rho_q-1}.
\tag{2.3}
\]

### Theorem 2.1 (exact DNF slack)

For `Q_I=union_(i in I) C_i`,

\[
 \boxed{
 {\sigma(\mathcal A)\over2}
 =\sum_{\varnothing\ne I\subseteq[h]}
 (-1)^{|I|+1}\delta(Q_I).}
\tag{2.4}
\]

Moreover the sequence `delta_q` is nonincreasing for `1<=q<=m`, and

\[
 \boxed{
 {\delta_{q+1}\over\delta_q}
 ={(m-q)(q+1)\over q(2m-q-1)}\le1
 \qquad(1\le q\le m-2).}
\tag{2.5}
\]

#### Proof

Every active owner has at least two selected facets by Theorem 1.1.
Therefore

\[
 {\sigma(\mathcal A)\over2}=|N(\mathcal A)|-|\mathcal A|.
\tag{2.6}
\]

Both the lower DNF and its upper neighbourhood are unions of the
corresponding principal stars.  Their intersections indexed by `I` have
common core `Q_I`.  Inclusion--exclusion and subtraction prove (2.4),
including the cases `|Q_I|>=m` covered by (2.2).

Formula (2.3) is the difference of the two adjacent binomial coefficients.
A direct quotient gives (2.5).  Its last inequality is equivalent to

\[
 m-q\le q(m-1),
\]

which holds for `q>=1`.  Finally `delta_m=1<=delta_(m-1)=m-1`.
\(\square\)

For two cores this gives an exact local-margin gluing identity.  Define

\[
 \mu_P(B)=\sigma(B)-\lambda_P(B).
\]

If
`Q=C_1 union C_2`, then

\[
\begin{aligned}
 \mu_P(\mathcal A_{C_1}\cup\mathcal A_{C_2})
 &={}&\mu_P(\mathcal A_{C_1})+
       \mu_P(\mathcal A_{C_2})\\
 &&-2\delta(Q)+\zeta_P(C_1,C_2),
\end{aligned}
\tag{2.7}
\]

where `zeta_P(C_1,C_2)` is the nonnegative cancellation current in (1.5).
For Hamming-adjacent equal-size cores, `|Q|=c+1`; hence the entire scalar
overlap tax is exactly `2delta_(c+1)`.

## 3. Uniform bounded-DNF closure

### Theorem 3.1 (quantitative DNF-width closure)

Let `h=h(m)` satisfy

\[
 \boxed{4^h(h+\log m)=o(m).}
\tag{3.1}
\]

Then the constant-spread reservoir satisfies

\[
 \boxed{
 \lambda_P\left(\bigcup_{i=1}^h\mathcal A_{C_i}\right)
 \le
 \sigma\left(\bigcup_{i=1}^h\mathcal A_{C_i}\right)}
\tag{3.2}
\]

for every collection of distinct nonempty cores (0.3), of arbitrary
ranks.  In particular this holds for fixed `h`, and more generally for

\[
 h\le(1/2-\varepsilon)\log_2m
\]

with any fixed `epsilon>0`.

Indeed, in that range

\[
 4^h(h+\log m)
 \le m^{1-2\varepsilon}O(\log m)=o(m).
\]

#### Proof

First delete every redundant clause: if `C_i subset C_j`, then
`mathcal A_(C_j) subseteq mathcal A_(C_i)`.  The remaining cores form an
antichain and define the same DNF.  If only one remains, apply the frozen
principal-star theorem.  Otherwise retain `h` as an upper bound on their
number, and put

\[
 A_i={m+\rho_i-1\choose\rho_i-1},
 \qquad
 \delta_i={c_i\over\rho_i}A_i,
 \qquad
 \alpha_h=\min\left\{{1\over17},2^{-(h+1)}\right\}.
\tag{3.3}
\]

### Case 1: `rho_i/m<=alpha_h` for every remaining core

Drop all positive odd terms of order at least three from (2.4).  Assign
each negative even subset `I` to one index `j(I) in I`.  Antichainness
implies `Q_I` strictly contains `C_(j(I))`, so monotonicity gives

\[
 \delta(Q_I)\le\delta_{c_{j(I)}+1}
 \le {2\rho_{j(I)}\over m}\delta_{j(I)}
 \le2\alpha_h\delta_{j(I)}.
\tag{3.4}
\]

At most `2^(h-1)` even subsets are assigned to any fixed index.  Therefore

\[
 {\sigma(\mathcal A)\over2}
 \ge\sum_i\delta_i-2^h\alpha_h\sum_i\delta_i
 \ge{1\over2}\sum_i\delta_i.
\tag{3.5}
\]

Since `alpha_h<=1/17`,

\[
 \sigma(\mathcal A)\ge\sum_i\delta_i
 =\sum_i{c_i\over\rho_i}A_i
 \ge16\sum_iA_i
 \ge16|\mathcal A|.
\tag{3.6}
\]

The union has size at least `2m+1`.  Indeed, if some `rho_i>=3`, that
single star has size at least `{m+2 choose 2}>2m`; if every `rho_i=2`,
two distinct core stars have union size at least

\[
 2(m+1)-1=2m+1.
\tag{3.7}
\]

The all-cut bound (0.1) now gives

\[
 \lambda_P(\mathcal A)
 \le15|\mathcal A|+2m
 \le16|\mathcal A|
 \le\sigma(\mathcal A).
\]

### Case 2: `rho_i/m>alpha_h` for at least one core

Choose an index `i_*` maximizing `rho_i`, and put

\[
 \rho_*:=\rho_{i_*},
 \qquad A_*:=A_{i_*},
 \qquad N_*:=N_{\rho_*}.
\tag{3.8}
\]

Choose one coordinate `x_i in C_i` for every core, and let `R` be the set
of chosen coordinates.  Then `|R|<=h`, and every lower vertex avoiding
`R` lies outside `mathcal A`.  For all sufficiently large `m`,

\[
 {W-|\mathcal A|\over W}
 \ge{{2m-1-h\choose m-1}\over{2m-1\choose m-1}}
 \ge3^{-h}.
\tag{3.9}
\]

For the last inequality, expand the ratio as

\[
 \prod_{j=0}^{h-1}{m-j\over2m-1-j}.
\]

Condition (3.1) implies `h=o(m)`, and every factor is at least `1/3`
once `2h<=m+1`.

The frozen Johnson spectral inequality therefore gives

\[
 \sigma(\mathcal A)
 \ge {4\cdot3^{-h}\over m}|\mathcal A|
 \ge {4\cdot3^{-h}\over m}A_*.
\tag{3.10}
\]

There is an absolute `kappa>0` such that the entropy comparison gives

\[
 \log_2{A_*\over N_*}
 \ge\kappa {m\over4^h}-O(\log m).
\tag{3.11}
\]

Indeed, for `alpha=rho_*/m<=1/2`, the entropy gap is

\[
 g(\alpha)=(1+\alpha)\log_2(1+\alpha)
 +(1-\alpha)\log_2(1-\alpha),
\]

and `g(alpha)>=alpha^2/ln 2`.  For `alpha>=1/2` the gap is bounded below
by an absolute constant.  In the first range use
`H_(rho_*)(m)<=(rho_*+1)binom(m,rho_*)`; in the second use
`H_(rho_*)(m)<=2^m`.  Standard uniform binomial estimates then lose only
`O(log m)` from these entropy gaps.  Since
`rho_*/m>alpha_h`, one has `alpha^2>=Omega(4^(-h))`.

Condition (3.1) also implies
`rho_*>=d` for all sufficiently large `m`, so `H_(rho_*)(m)>=H_d` and no
larger subexponential term is hidden in `N_*`.

The function `H_rho(m)` is increasing, so `N_(rho_i)<=N_*` for every
`i`.  By (3.1), the right side of (3.11) dominates
`log_2(hm3^h)`.  Combining (1.4), (3.10), and (3.11) gives

\[
 \sigma(\mathcal A)>2hN_*
 \ge\lambda_P(\mathcal A).
\]

This completes both cases. \(\square\)

### Corollary 3.2 (Hamming-adjacent core trees)

Every union of `h` equal-size principal stars whose core intersection
graph is a tree of Hamming-adjacent cores is safe whenever (3.1) holds.

No tree property is needed: Theorem 3.1 closes every admissible intersection
pattern, even with varying core ranks.  In particular it covers every
shifted partial-colex family whose minimal monotone DNF satisfies (3.1).

## 4. Quantitative width dependence and the Lipschitz-tail obstruction

The generic proof reaches logarithmic width, but only up to the
half-logarithmic threshold in (3.1).  Three losses are genuine:

1. the even inclusion--exclusion multiplicity is exponential in `h`;
2. the certified complement density is only `3^(-h)`; and
3. the path-current bound is `2hN_*` in the worst rank.

Accordingly `alpha_h` in (3.3) tends to zero exponentially, and the
entropy gap in (3.11) is only `Theta(m/4^h)`.  Pairwise adjacency or a
tree intersection graph does not control the higher-order core unions
`Q_I` in (2.4).

This is not merely a technical omission in the local formula.  At an
owner containing several active cores, a path exchange can leave every
old core and enter a new core while the DNF remains satisfied.  The exact
cancellation current (1.5), rather than the sum of individual path
crossings, becomes essential.  Any theorem with unboundedly many clauses
must exploit this cancellation or prove a bounded-width property of the
entire core nerve.  The present theorem makes no such claim.

There is a formal Lipschitz extension, but geometric Macaulay decay alone
does not meet it.  If a head DNF `A_0` has certified margin `M_0`, then the
frozen Hamming theorem closes every family `A` satisfying

\[
 \boxed{|A\triangle A_0|\le {M_0\over2m+2}.}
\tag{4.1}
\]

The proof above supplies, respectively,

\[
 M_0\ge|A_0|-2m
\tag{4.2}
\]

in Case 1, and

\[
 M_0\ge {4\cdot3^{-h}\over m}A_*-2hN_*
\tag{4.3}
\]

in Case 2.

However, consider the ordered DNF of `h` singleton cores.  If `R` is
their coordinate set, then

\[
 A_h=\{L:L\cap R\ne\varnothing\},
\]

and exact complementation gives

\[
 \boxed{
 \sigma(A_h)={2h\over m}{2m-1-h\choose m-1}.}
\tag{4.4}
\]

The next singleton clause adds

\[
 {2m-2-h\choose m-2}
 ={m-1\over2m-1-h}{2m-1-h\choose m-1}
\tag{4.5}
\]

new lower vertices, asymptotically half of the current complement.  Since
no certified margin can exceed `sigma(A_h)`, the largest possible
Lipschitz radius is at most

\[
 {h\over m(m+1)}{2m-1-h\choose m-1}.
\tag{4.6}
\]

The ratio of the single next geometric term (4.5) to the upper bound
(4.6) is

\[
 \boxed{
 {m(m+1)(m-1)\over h(2m-1-h)}
 =\Theta(m^2/h)}
\tag{4.7}
\]

throughout the relevant range `h=o(m)`.  Thus the proposed strategy

> keep `O(log m)` Macaulay centres and pay the geometrically decaying tail
> by Hamming Lipschitz margin

does not work from geometric decay alone, even for singleton cores.  A
larger-width theorem must analyze the ordered star union directly or use
the cancellation current (1.5); it cannot treat the remaining clauses as
an unstructured Hamming tail.

## 5. Scope and dependencies

The theorem closes monotone DNFs satisfying (3.1) on the lower shore for
one physical reservoir.  It does not close arbitrary Macaulay generator
lists beyond that width, general shifted families of larger DNF width,
component placement, or the common cap.

| role | file | SHA-256 |
|---|---|---|
| constant-spread reservoir | `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md` | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |
| exact two-sided ledger and uniform separation | `MATH_THEOREM_PROTECTED_ORE_TWO_SIDED_SUBCUBE_EXACT_REDUCTION_20260804.md` | `6499abf7abf9536bdfcf421206ad1e56d3b3f9d2ce05258b92cb8873ddb26dd7` |
| Johnson spectral inequality | `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md` | `c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0` |
