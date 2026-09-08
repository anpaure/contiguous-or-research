# Finite-order edge beta tail and the protected-arm growth no-go

Date: 2026-07-27

Scope: a sharp positive replacement for the invalid all-order
pair-column initializer in the repaired-ring first-moment top strip.

## Dynamic scope correction

The abstract finite-tail lemma and the protected-arm growth no-go below
remain valid.  They do not prove a hereditary estimate for the actual
process.  The actual residual is vertex-induced, not an arbitrary
edge-deletion subhypergraph, and endpoint conditioning changes the
neutral pair scale from $m^{-2}$ to $m^{-2}u_t^{-1}$.

At the whole-arm level this density loss is still summable:

\[
 \int_0^T{dt\over m^2u_t}=O((mz)^{-1})=o(1).
\]

Complete physical-union normalization also makes the compensation
deficit in Section 5 exactly zero.  The exact stopped conditional
inequalities and the remaining factorial link-energy gate are in
`MATH_AUDIT_ACTUAL_STOPPED_PAIR_SPREAD_COIN_FIBRE_AND_PAIR_SAFE_PROCESS_20260727.md`.

## 0. Outcome

There is a clean finite-order theorem.

* Prove the strong endpoint factor \(\alpha\) only through a finite
  order \(B=\Theta(\log ^2m)\).
* Beyond \(B\), use only an aggregate common-event fraction
  \(\beta=O(\operatorname {polylog}(m)/m)\).
* If the eligible physical arms remain fixed, the complete backward
  series is bounded by

  \[
    e^{A\alpha}
    +\left({\alpha\over\beta}\right)^B e^{A\beta}.
  \tag{0.1}
  \]

  With suitable constants this is \(1+o(1)\).

The fixed-arm hypothesis is load-bearing.  If every protected extension
column becomes a new marginally normalized arm, then the aggregate
common-event fraction grows at least at the linear scale
\((a+j)/m\).  The corresponding backward majorant increases by a factor
\(\Theta(\log m)\) per level after the initial buffer.  It overwhelms
an \(\alpha^B\) initializer after only
\(O(\log ^3m/\log\log m)\) further levels.  Thus a beta tail alone
cannot close a tower with growing protected arms.

For compensation columns, the exact extra condition is a weighted
common-resource deficit bound.  Equality resolution is sufficient only
if the reference is normalized by the complete union of physical
resources; resolving the finitely displayed coincidences is not enough.

## 1. Abstract finite-order beta-tail lemma

Let \(F_j(t)\), \(j\ge0\), be nonnegative stopped observables on an
interval \([t_0,t_1]\).  Suppose an integrating factor has removed the
ordinary first-moment reference drift and

\[
                         \mathcal G F_j(t)
                         \le\kappa(t)F_{j+1}(t).
\tag{1.1}
\]

Put

\[
                         A=\int_{t_0}^{t_1}\kappa(t)\,dt.
\tag{1.2}
\]

Assume, for some base mass \(M\), excess \(s\), and integer \(B\ge1\),

\[
 F_j(t_0)\le M\alpha^{s+j}qquad(0\le j\le B),
\tag{1.3}
\]

and

\[
 F_j(t_0)\le
 M\alpha^{s+B}\beta^{j-B}qquad(j>B).
\tag{1.4}
\]

Here \(\beta\) is the **aggregate** next-column fraction: all choices of
the eligible pair of arms, endpoint colors, and orientations have
already been included in it.

### Theorem 1.1 (finite strong initializer, weak infinite tail)

Under (1.1)--(1.4),

\[
 \boxed{
 \mathbb E F_0(t_1)
 \le M\alpha^s
 \left[
 e^{A\alpha}
 +\left({\alpha\over\beta}\right)^B e^{A\beta}
 \right].}
\tag{1.5}
\]

In particular, if

\[
 A\alpha=o(1),
 \qquad
 B\log(\beta/\alpha)-A\beta\longrightarrow+\infty,
\tag{1.6}
\]

then

\[
                         \mathbb EF_0(t_1)
                         \le(1+o(1))M\alpha^s.
\tag{1.7}
\]

#### Proof

The backward Duhamel expansion for (1.1), obtained either by iterated
integration or by the usual backward exponential potential, is

\[
 \mathbb EF_0(t_1)
 \le\sum_{j\ge0}{A^j\over j!}F_j(t_0).
\tag{1.8}
\]

The part \(j\le B\) is at most

\[
                         M\alpha^s e^{A\alpha}.
\tag{1.9}
\]

The remaining part is at most

\[
 \begin{aligned}
 M\alpha^{s+B}\beta^{-B}
       \sum_{j>B}{(A\beta)^j\over j!}
 &\le
 M\alpha^s
       \left({\alpha\over\beta}\right)^B e^{A\beta}.
 \end{aligned}
\tag{1.10}
\]

This proves (1.5), and (1.6) gives (1.7). \(\square\)

The theorem remains true for a finite tower by putting \(F_j=0\) past
its terminal physical level.

## 2. The repaired-ring selected-edge parameter

Let \(A_1,\ldots,A_a\) be fixed physical repaired-edge arms, each with
at most \(K\) resources.  Assume first that their unprotected resource
sets are pairwise disjoint.  For a possible next selected edge \(g\),
let

\[
                         \ell_g=\#\{i:g\cap A_i\ne\varnothing\}.
\tag{2.1}
\]

The common-event excess is bounded by

\[
                         (\ell_g-1)_+\le\binom{\ell_g}{2}.
\tag{2.2}
\]

If \(\Delta_2\) is the maximum pair codegree and \(\Delta\) the free
edge-column degree scale, then

\[
 \begin{aligned}
 \sum_g\binom{\ell_g}{2}
 &\le
 \sum_{1\le i<i'\le a}
 \sum_{u\in A_i,v\in A_{i'}}d(u,v)\\
 &\le\binom a2K^2\Delta_2.
 \end{aligned}
\tag{2.3}
\]

The total marginal free-column mass has scale \(aK\Delta\).  Therefore
the **aggregate** common-event fraction is

\[
 \boxed{
 \beta_E(a)\le
 C a\,{K\Delta_2\over\Delta}.}
\tag{2.4}
\]

At time zero in the repaired promotion-ring catalogue,

\[
                         {\Delta_2\over\Delta}=O(m^{-2}),
 \qquad K=(1+o(1))m,
\tag{2.5}
\]

and hence

\[
                         \beta_E(a)=O(a/m).
\tag{2.6}
\]

This is the version which already includes all \(\binom a2\) possible
arm pairs.  The pointwise fraction for one prescribed pair is
\(O(1/m)\); multiplying that number by another \(a^2\) would double
count the free first incidence.  The correct aggregate loss is linear
in \(a\), as in (2.4).

Suppose

\[
 a\le C_a\log ^2m,qquad
 A\le C_Tm\log m,qquad
 \alpha=m^{-19/10+o(1)},qquad
 B=C_B\log ^2m.
\tag{2.7}
\]

Then

\[
                         A\beta_E=O(C_TC_a\log ^3m)
\tag{2.8}
\]

and

\[
                         \log(\beta_E/\alpha)
                         =(9/10+o(1))\log m.
\tag{2.9}
\]

Consequently (1.6) holds when the initializer constant \(C_B\) is
chosen larger than the absolute constant in (2.8).  Thus the beta tail
has exactly enough exponential room in the fixed-arm edge-only model.

The strong initializer must actually be available through \(B\).  If
the base type has excess \(s\) and the local path-mesh theorem is
certified through total core incidence \(L_{\rm pm}\), the required
condition is

\[
                         2(s+B)\le L_{\rm pm}.
\tag{2.10}
\]

This condition must be checked; it is not implied by
\(s\le L\) and a path-mesh theorem stated only through order \(2L+2\).

## 3. What “fixed arms” must mean

Theorem 1.1 applies to the physical edge tower only under the following
frozen-extension condition.

> **FE.** Auxiliary columns introduced to record common-event deficits
> do not become new marginally normalized survivor objects in the next
> level.  Equivalently, their later deletion is nonpositive after the
> chosen normalization, and every future positive union deficit is still
> measured only among the original \(a\) physical arms.

Under FE, \(a\) stays fixed and (2.6) gives one common beta for the
entire tail.  This is the sharp positive theorem.

The current ordered-column construction does not satisfy FE: its base
contains current degree and survivor factors for every previously
adjoined protected column.  A later edge killing two such columns once
creates positive normalized drift.  Thus those columns are eligible
arms whether or not the proof calls their raw deletion terminal.

One possible way to realize FE would be a chronological expansion in
which every auxiliary column is normalized at its birth and then frozen.
That requires birth-time-labelled bases and a new generator calculation;
using the time-zero degree for all births introduces the uncontrolled
factor \(\Delta_0/\Delta_t\).  FE is therefore an exact additional
construction condition, not a convention available for free.

## 4. Rigorous arm-growth no-go for the beta majorant

Assume instead that after \(j\) extensions there are

\[
                         a_j=a_0+j
\tag{4.1}
\]

eligible arms.  Even the favorable aggregate codegree estimate then has
the scale

\[
                         \beta_j={c(a_0+j)\over m}.
\tag{4.2}
\]

Suppose the strong initializer stops at \(B\) and the weakest tail
majorant is iterated with equality:

\[
 F_B=M\alpha^{s+B},
 \qquad
 F_j=F_B\prod_{i=B}^{j-1}\beta_i\quad(j>B).
\tag{4.3}
\]

The \(j\)-th Duhamel term relative to \(M\alpha^s\) is

\[
 R_j=\alpha^B{A^j\over j!}
       \prod_{i=B}^{j-1}{c(a_0+i)\over m}.
\tag{4.4}
\]

Its exact successive ratio is

\[
 {R_{j+1}\over R_j}
 ={Ac(a_0+j)\over m(j+1)}.
\tag{4.5}
\]

If \(A\ge c_Am\log m\), then for
\(j\ge\max\{a_0,1\}\),

\[
                         {R_{j+1}\over R_j}
                         \ge c'\log m.
\tag{4.6}
\]

For \(a_0+B=O(\log ^2m)\), direct Stirling bounds give

\[
                         R_{j_0}\ge\exp[-C\log ^3m]
\tag{4.7}
\]

at some \(j_0=O(a_0+B)\).  Therefore

\[
 R_{j_0+q}\ge
 \exp[-C\log ^3m](c'\log m)^q.
\tag{4.8}
\]

Taking

\[
                         q={2C\log ^3m\over\log\log m}
\tag{4.9}
\]

gives \(R_{j_0+q}\to\infty\).  Hence any physical tower extending at
least

\[
                         O(\log ^3m/\log\log m)
\tag{4.10}
\]

levels past the strong initializer has an exploding beta majorant.

This is a rigorous no-go for the proposed **method from only the beta
assumptions**: the assumptions admit the extremal sequence (4.3), and
their own Duhamel upper envelope is unbounded.  It is not a theorem that
the actual repaired catalogue attains (4.3).  Additional depletion,
negative dependence, or a frozen-extension representation could still
improve the physical tower.

If arm-pair choices are bounded quadratically rather than through the
aggregate first-incidence normalization (2.4), then
\(\beta_j\asymp(a_0+j)^2/m\), and the explosion is only faster.

## 5. Exact compensation condition

Let \(A_1,\ldots,A_a\) be the eligible physical arms and let

\[
                         \ell_y=\#\{i:y\in A_i\}.
\tag{5.1}
\]

The total marginal compensation hazard is

\[
                         H_\circ^{\rm marg}
                         =\sum_y\chi_t(y)\ell_y,
\tag{5.2}
\]

whereas the actual hazard of the union of the coin events is

\[
                         H_\circ^{\rm union}
                         =\sum_y\chi_t(y)\mathbf1_{\ell_y>0}.
\tag{5.3}
\]

Thus the exact common-coin deficit is

\[
                         C_\circ
                         =\sum_y\chi_t(y)(\ell_y-1)_+.
\tag{5.4}
\]

The compensation analogue needed by Theorem 1.1 is

\[
 \boxed{
 C_\circ
 \le\beta_\circ H_\circ^{\rm marg},
 \qquad
 \beta_\circ=O(\operatorname {polylog}(m)/m),}
\tag{Coin-beta}
\]

uniformly for every tower state, or in the corresponding
incidence-weighted aggregate form.

For two prescribed arms the pointwise ratio is governed by their
weighted common-resource mass

\[
                         \sum_{y\in A_i\cap A_{i'}}\chi_t(y).
\tag{5.5}
\]

There is no unconditional \(O(1/m)\) bound: two distinct repaired rows
can share \(K-O(1)\) owners, and the active compensation rates can be
concentrated on those owners.

Complete physical-resource union normalization would make the coin
deficit vanish: each shared resource is then one marginal object, not
one copy per arm.  But this means resolving **all** shared resources,
not only the \(O(L)\) coincidences displayed by a finite mixed type.
Alternatively one must prove (Coin-beta).  This is the exact additional
condition for compensation columns.

## 6. Consequence for the top-strip program

The edge-only beta idea is mathematically viable in the following
precise conditional form:

1. a strong current or globally propagated initializer through a margin
   \(B\) satisfying (2.10);
2. fixed eligible arms in the sense FE;
3. the aggregate edge fraction (2.4) with its required dynamic or
   time-zero propagation interpretation; and
4. constants satisfying (1.6).

For the compensated process, add (Coin-beta), or use a complete physical
union normalization.

Without FE, protected-arm growth defeats the beta summation by
Theorem 4.1.  Thus the next constructive question is not whether the
numerical beta tail is small—it is—but whether one can build a
chronological/frozen auxiliary-column expansion whose extension columns
do not become new marginal arms.
