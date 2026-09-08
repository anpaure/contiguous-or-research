# Locally orthogonal factorizations as coherent Room atlases

Date: 2026-07-27

Method: pure mathematics.  No finite search is used.

## 0. Outcome

Put

\[
 \Omega=[2r-1],\qquad
 \mathcal L=\binom{\Omega}{r-1},\qquad
 \mathcal M=\binom{\Omega}{r},\qquad
 \mathcal U=\binom{\Omega}{r+1}.
\]

The locally orthogonal factorization problem has an exact atlas form.
Every 1-factorization of the inclusion graph
`B(L,M)` is equivalent to a family of row-Latin, skew local charts

\[
 q_A:\{(a,b)\in A^2:a\ne b\}\longrightarrow [r]
 \qquad(A\in\mathcal U)
\]

satisfying one overlap equation.  The local defect `Delta_A` is simply the
unordered-pair collision defect of `q_A`.

There is **no local obstruction**.  If `r` is a prime power, every individual
chart has an explicit finite-field realization with

\[
 G_A=K_r+\text{a spanning 2-factor},\qquad \Delta_A=0.
\]

Thus the open theorem is exactly a gluing theorem for optimal Room-like
charts.  The overlap equation, not local design existence, is the hard part.

Two canonical global factorizations sit cleanly on either side of this
reduction.

* The PBBS unmatched-zero matching is one member of the Kierstead--Trotter
  lexical 1-factorization, so it has an explicit full completion.  This is
  not repeated unmatched-zero recursion: the other factors use the other
  lexical scan indices.  The standard `0/1` pair has a linear upper-shadow
  defect for `r>=5`, so that completion is not locally perfect.
* The modular factorization has a closed local formula in terms of the gap
  word `b_i=a_i-i`.  On a consecutive upper set it has local defect
  `Theta(r^3)`, so neither a uniform `O(r)` theorem nor a naive cyclic-
  difference proof is possible for that construction.

The remaining viable statements are therefore:

1. construct a coherent atlas of the optimal finite-field charts; or
2. prove that the lexical or modular atlas has **average** defect `O(r)` even
   though some of its charts/pairs are bad.

## 1. Exact coherent-atlas equivalence

Let `c(X,Y)` be a proper edge colouring of `B(L,M)` by `[r]`.  Since the
graph is `r`-regular and bipartite, such a colouring is precisely a
1-factorization.

For `A in U` and distinct `a,b in A`, define

\[
 X_{ab}=A\setminus\{a,b\},\qquad Y_a=A\setminus\{a\},
\]

and

\[
 q_A(a,b):=c(X_{ab},Y_a).
\tag{1.1}
\]

Thus the first argument is the point omitted by the middle set and the
second argument is the additional point omitted by the lower set.

### Theorem 1.1 (coherent Room-atlas theorem)

Proper `r`-edge-colourings of `B(L,M)` are equivalent to families `(q_A)`
with the following three properties.

1. **Row Latin:** for every `A` and `a in A`,

   \[
   b\longmapsto q_A(a,b),\qquad b\in A\setminus\{a\},
   \tag{1.2}
   \]

   is a bijection onto `[r]`.

2. **Skew:** for distinct `a,b in A`,

   \[
   q_A(a,b)\ne q_A(b,a).
   \tag{1.3}
   \]

3. **Overlap coherence:** if `Y in M`, `b in Y`, and `a,a' notin Y`, then

   \[
   q_{Y+a}(a,b)=q_{Y+a'}(a',b).
   \tag{1.4}
   \]

For the corresponding factorization, the local colour-pair multigraph is

\[
 G_A=\big\{\{q_A(a,b),q_A(b,a)\}:\{a,b\}\in\binom A2\big\}
\tag{1.5}
\]

with multiplicity.

#### Proof

Starting with a proper edge colouring, (1.2) is properness at the middle
vertex `Y_a`.  Equation (1.3) is properness at the lower vertex `X_ab`.
For (1.4), both sides are the colour of the same edge

\[
 Y\setminus\{b\}\;--\;Y.
\]

Conversely, suppose the charts satisfy (1.2)--(1.4).  For an edge
`X subset Y`, write `b=Y\setminus X`, choose any `a notin Y`, and set

\[
 c(X,Y)=q_{Y+a}(a,b).
\tag{1.6}
\]

This is well-defined by (1.4).  At a fixed middle vertex `Y`, choose one
`a notin Y`; then (1.2), as `b` ranges over `Y`, says that the `r` incident
edge colours are all distinct.

At a fixed lower vertex `X`, take distinct `a,b notin X` and put
`A=X+{a,b}`.  The colours of the two edges to `X+a` and `X+b` are

\[
 q_A(b,a)\quad\hbox{and}\quad q_A(a,b),
\]

respectively, and are distinct by (1.3).  Hence all `r` edges at `X` have
distinct colours as well.  The colouring is proper.  Formula (1.5) follows
directly from the definitions. \(\square\)

### Corollary 1.2 (exact form of the open target)

The target `Delta_A=0` for every `A` is equivalent to a coherent atlas
satisfying (1.2)--(1.4) and

\[
 \big\{\{q_A(a,b),q_A(b,a)\}:\{a,b\}\in\binom A2\big\}
   =K_r+R_A,
\tag{1.7}
\]

where `R_A` is a spanning 2-factor on the colour set, with doubled edges
allowed.  The asymptotic theorem asks only that the aggregate deviation
from (1.7) be `O(r|U|)` or `o(r^2|U|)`.

This is a one-sided Room/Howell frame: every symbol `a in A` sees every
row colour once, while the unordered projection of occupied cells is
`K_r` plus a 2-factor.  It is not, without an additional column condition,
a classical Howell design.

## 2. An explicit optimal projective Room chart

The next theorem proves that (1.2), (1.3), and (1.7) are locally compatible
with equality.

### Theorem 2.1 (finite-field chart)

Let `r=q` be a prime power with `q>=4`.  Identify the local point set with

\[
 A=\mathbb P^1(\mathbb F_q)=\mathbb F_q\cup\{\infty\}
\]

and the colour set with `F_q`.  Choose

\[
 \alpha,\beta\in\mathbb F_q^*,\qquad
 \alpha\ne\beta,\quad \alpha+\beta\ne0,
 \qquad \delta\in\mathbb F_q^*.
\]

Define, for finite distinct `a,b`,

\[
 \begin{aligned}
 Q(a,b)&=\alpha a+\beta b,\\
 Q(a,\infty)&=(\alpha+\beta)a,\\
 Q(\infty,b)&=(\alpha+\beta)b+\delta.
 \end{aligned}
\tag{2.1}
\]

Then every row of `Q` is a permutation of `F_q`, opposite entries are
distinct, and

\[
 \big\{\{Q(a,b),Q(b,a)\}:\{a,b\}\in\binom A2\big\}
   =K_q+C_\delta,
\tag{2.2}
\]

where

\[
 C_\delta=\big\{\{x,x+\delta\}:x\in\mathbb F_q\big\}
\tag{2.3}
\]

is a spanning 2-regular multigraph.  In odd characteristic it is a disjoint
union of simple cycles of length `char(F_q)`; in characteristic two it is a
doubled perfect matching.  Consequently the chart has `Delta=0`.

#### Proof

Fix finite `a`.  As finite `b ne a` varies, `alpha*a+beta*b` takes every
field value except `(alpha+beta)a`; the infinity entry supplies exactly
that missing value.  The infinity row is a permutation because
`alpha+beta ne 0`.

For finite `a ne b`,

\[
 Q(a,b)-Q(b,a)=(\alpha-\beta)(a-b)\ne0.
\]

For the infinity pair the difference is `delta ne 0`.

On ordered finite pairs, the map

\[
 (a,b)\longmapsto
 (\alpha a+\beta b,\,\beta a+\alpha b)
\]

has determinant `alpha^2-beta^2 ne 0`, commutes with swapping the two
coordinates, and maps the off-diagonal to itself.  It therefore induces a
bijection on unordered pairs of distinct field elements.  These pairs give
one copy of `K_q`.  The `q` pairs containing infinity give exactly (2.3).
Every field element has degree two in (2.3), including multiplicity.  This
proves (2.2). \(\square\)

For `q=3`, the following off-diagonal array supplies the exceptional chart:

\[
 \begin{array}{c|cccc}
   &0&1&2&3\\ \hline
 0&-&0&1&2\\
 1&1&-&2&0\\
 2&2&0&-&1\\
 3&0&1&2&-
 \end{array}
\tag{2.4}
\]

Every row is a permutation of `{0,1,2}`, opposite entries differ, and each
of the three colour pairs occurs twice.  Thus `G=2K_3` and `Delta=0`.

### Corollary 2.2 (no local lower bound)

For infinitely many `r`, and in fact for every prime-power `r>=3`, the
minimum possible value of the local defect among row-Latin skew charts is
zero.  Any lower bound on the average defect of a genuine Boolean
1-factorization must use overlap coherence (1.4); it cannot be proved one
upper interval at a time.

## 3. The coherent projective-atlas gate

The finite-field construction turns the global target into a sharply stated
cocycle problem.

For each `A in U`, choose a bijection

\[
 \theta_A:A\longrightarrow\mathbb P^1(\mathbb F_r)
\]

and a colour permutation `gamma_A in S_r`, and put

\[
 q_A(a,b)=\gamma_A
   Q\big(\theta_A(a),\theta_A(b)\big).
\tag{3.1}
\]

Every such chart is locally perfect.  By Theorem 1.1 these charts glue to
a globally perfect locally orthogonal factorization if and only if, for
every `Y in M`, `b in Y`, and `a,a' notin Y`,

\[
 \gamma_{Y+a}Q(\theta_{Y+a}(a),\theta_{Y+a}(b))
 =
 \gamma_{Y+a'}Q(\theta_{Y+a'}(a'),\theta_{Y+a'}(b)).
\tag{3.2}
\]

Equation (3.2) is the exact missing theorem.  It is a transition-function
or cocycle equation on overlaps of the `(r+1)`-set charts.  If it has a
solution, Proposition 3.2 of the fresh-rotor note gives q1 CPCR equal to
zero for **every** pair of factor colours, not merely for one selected pair.

Conversely, among factorizations whose local charts are isomorphic to the
finite-field chart `Q`, every globally locally-perfect factorization yields
data `(theta_A,gamma_A)` satisfying (3.2).  Hence (3.2) is an exact
equivalence inside this algebraic construction class, not only a sufficient
condition.

## 4. Why the naive cyclic chart is maximally wrong

The projective construction also diagnoses the failure of a pure difference
rule.  Suppose `r` is even, identify `A` with the cyclic group
`Z_(r+1)`, identify the colours with its `r` nonzero elements, and set

\[
 q(a,b)=b-a.
\tag{4.1}
\]

Each row is a permutation and opposite entries are distinct because the
odd-order group has no nonzero involution.  However the unordered colour
pair of `{a,b}` is only

\[
 \{d,-d\},\qquad d=b-a.
\]

Only `r/2` colour pairs occur, each with multiplicity `r+1`.  Therefore

\[
 \Delta
 =\frac r2\binom{r+1}{2}-r
 =\frac{r^2(r+1)}4-r
 =\Theta(r^3).
\tag{4.2}
\]

Thus cyclic equivariance by itself is anti-orthogonal: it collapses every
translation class into one colour pair.  A successful cyclic construction
must contain a genuinely two-coordinate mixing term, exactly as the
invertible matrix in Theorem 2.1 does.

## 5. PBBS and the lexical completion

For the balanced pair of levels `(r-1,r)` in `Q_(2r-1)`, the
Kierstead--Trotter `i`-lexical matchings

\[
 M^0,M^1,\ldots,M^{r-1}
\]

are pairwise disjoint perfect matchings and partition every incidence edge.
This is Lemma 6 of Gregor--Jaeger--Mütze--Sawada--Wille, *Gray codes and
symmetric chains*.  The circular/parenthesis unmatched-zero selector is the
extreme lexical factor.  Hence it **does** have an explicit completion to a
1-factorization.

This completion should not be described as recursively applying the
unmatched-zero rule after deleting its edges.  The residual graph is no
longer another Boolean adjacent-level graph with a new unmatched zero.  The
correct completion labels all down-steps by their lexical scan indices and
uses one index per factor.

The completion is not locally perfect.  Apply
`MATH_THEOREM_LEXICAL_MIDDLE_LEVELS_OPPOSITE_TRIPLE_DEFECT_20260726.md`
with its parameter `s=r-1`.  For the pair `M^0 union M^1`, the number of
omitted rank-`(r+1)` union colours is

\[
 H_{01}
 =W\frac{(r-3)(r-4)}{2(r+1)(2r-3)}
 =\left(\frac14+O(r^{-1})\right)W
\tag{5.1}
\]

for `r>=5`.  Thus the lexical atlas cannot satisfy `Delta_A=0` throughout.
This is fully consistent with the q1 target: one bad colour pair contributes
only `Theta(W)` to `sum_A Delta_A`, whereas the desired average
`Delta_A=O(r)` permits total defect `O(rW)`.  What remains unknown is the
aggregate profile over all `binom(r,2)` lexical colour pairs.

Accordingly the precise lexical question is

\[
 \boxed{\sum_{A\in\mathcal U}\Delta_A^{\rm lex}=O(rW)?}
\tag{5.2}
\]

rather than whether every lexical pair is upper-rainbow.

## 6. Exact modular-chart formula

The alternative modular 1-factorization admits an equally explicit local
diagnostic.  Number the ground set `1,...,2r-1`.  For a lower set `X`, let
`j_X(a)` be the rank of `a` in the complement of `X`, ordered from largest
to smallest.  Up to a common choice of residues, the modular colour is

\[
 c(X,X+a)=j_X(a)-\sum_{x\in X}x\pmod r.
\tag{6.1}
\]

Fix

\[
 A=\{a_1<a_2<\cdots<a_{r+1}\},\qquad S_A=\sum_{a\in A}a.
\]

For `i<j`, direct rank counting gives

\[
 \boxed{
 p_A(A\setminus\{a_i,a_j\})
 =\{a_j+i-S_A,\ a_i+j-1-S_A\}\pmod r.}
\tag{6.2}
\]

Indeed, among the complement of `A-{a_i,a_j}`, the largest-ranks of
`a_i,a_j` are `r-a_i+i` and `r-1-a_j+j`, respectively; substituting in
(6.1) yields (6.2).

Writing

\[
 b_i=a_i-i,
\]

the oriented difference of the two colours in (6.2) is

\[
 b_j-b_i+1\pmod r.
\tag{6.3}
\]

Thus the modular local defect is an additive-energy statistic of the
nondecreasing gap word `(b_i)`.  This is the right starting point for an
average calculation.

It also gives a sharp uniform obstruction.  If `A` is consecutive, then
all `b_i` are equal, so every image in (6.2) is an adjacent colour pair.
At most `r` of the `binom(r,2)` colour pairs occur.  With
`E=binom(r+1,2)` local edges, Cauchy--Schwarz gives

\[
 \sum_p\binom{m_A(p)}2
 \ge \frac12\left(\frac{E^2}{r}-E\right)
 =\frac{r(r^2-1)}8.
\tag{6.4}
\]

Consequently

\[
 \Delta_A^{\rm mod}
 \ge \frac{r(r^2-1)}8-r
 =\Theta(r^3).
\tag{6.5}
\]

So the modular construction cannot satisfy a pointwise `O(r)` bound.  This
does not decide its average: consecutive charts form a negligible portion
of `U`.  Formula (6.2) reduces that average question to a concrete energy
estimate for random central gap words.

## 7. Exact disposition

The exploration gives one positive theorem, two precise diagnostics, and
one isolated open gate.

* **Positive:** optimal local charts with `Delta_A=0` exist explicitly for
  every prime-power `r`.
* **Exact global reformulation:** a 1-factorization is a coherent row-Latin
  skew atlas; the entire obstruction is equation (1.4).
* **Cyclic diagnosis:** pure difference charts have `Theta(r^3)` defect.
* **PBBS/SCD diagnosis:** PBBS extends to the lexical factorization, but the
  standard `0/1` pair has linear upper holes; only the aggregate estimate
  (5.2) remains plausible.
* **Modular diagnosis:** its defect is exactly the gap-word energy (6.2)--
  (6.3), with cubic exceptional charts.

The highest-value next theorem is therefore one of

\[
 \text{coherent projective Room atlas (3.2)},
 \qquad
 \sum_A\Delta_A^{\rm lex}=O(rW),
 \qquad
 \sum_A\Delta_A^{\rm mod}=O(rW).
\]

Any one of them would prove the desired q1 pair-rounding statement; the
first would prove it with zero defect for every colour pair.
