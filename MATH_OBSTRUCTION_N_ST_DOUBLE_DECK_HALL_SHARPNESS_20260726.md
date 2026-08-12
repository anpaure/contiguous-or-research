# The critical PBBS double deck has no local Hall saving

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 N=2r+1,
 \qquad B_r=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil .
\]

The corrected PBBS gate is

\[
 \overline\nu_H=o_A(B_r/\sqrt r),                 \tag{0.1}
\]

or, after all spatial lifts,

\[
 \nu_H(P_r)=o_A(B_r\sqrt r).                     \tag{0.2}
\]

The critical-saturation reduction says that failure of (0.1) produces a
positive-density packing by Gaussian-height simple fixed-core sectors and
also a pairwise disjoint family of their one-edge translates. This note
proves that this **double-deck condition supplies no additional local Hall
capacity at all**.

There are three exact results.

1. If \(\sigma\) is the one-edge deck translation, then

   \[
      \sigma I\cap\sigma J=\sigma(I\cap J).       \tag{0.3}
   \]

   Hence the conflict system in the translated deck is isomorphic to the
   original conflict system. Requiring both \(\{I\}\) and
   \(\{\sigma I\}\) to be pairwise disjoint is equivalent to requiring
   only the first condition. In a two-copy formulation, every second-deck
   set-packing row is just a renamed first-deck row.

2. Let a simple sector \(I\) have trace length \(k_I\), active half-size
   \(s_I\), and inactive cores \(K_I,K'_I\), both of size

   \[
      q_I=r-s_I.
   \]

   In a height subdeck of edge volume \(E\), every pairwise trace-disjoint
   family satisfies, for all integers \(t,u\ge0\),

   \[
   \boxed{
    \sum_I
       \binom{q_I}{t}\binom{q_I}{u}k_I
    \le
       \Delta_{r;t,u}E,}                          \tag{0.4}
   \]

   where

   \[
    \Delta_{r;t,u}:=
      \binom{r+1}{t}\binom{r+1}{u}
      -\binom r{t-1}\binom r{u-1}.               \tag{0.4a}
   \]

   This is the complete mixed core-subset hierarchy obtained by charging
   \(t\) enclosing coordinates in the first deck and \(u\) enclosing
   coordinates in the translated deck, including the exact disjoint-core
   exclusion at the shared coordinate of the paired edge columns. When
   \(s_I\le A\sqrt r\) and \(t+u=o(\sqrt r)\), its coefficient differs
   from the scalar edge-volume coefficient by only \(1+o_A(1)\). Even for
   \(t,u=O(\sqrt r)\), it differs by only a constant. Thus no member of
   this hierarchy gives the required vanishing gain.

3. This absence of gain is not merely a formal relaxation. For every
   fixed \(A>0\), every fixed \(c\) with

   \[
                      A/2<c<A,                    \tag{0.5}
   \]

   and infinitely many ranks, a genuine PBBS Gaussian-height inverse
   fibre contains pairwise quotient-edge-disjoint, literal, simple
   fixed-core first-return sectors whose traces cover the limiting fraction

   \[
             \boxed{\theta(c)={1-e^{-4c^2}\over2}>0}          \tag{0.6}
   \]

   of that fibre deck. Their one-edge translates are pairwise disjoint as
   well. Moreover, if

   \[
       {t\over\sqrt r}\longrightarrow\alpha,
       \qquad
       {u\over\sqrt r}\longrightarrow\beta,
       \qquad 0\le\alpha,\beta<\infty,
   \]

   then the utilization of the mixed capacity (0.4) tends exactly to

   \[
       \boxed{
       \theta(c)e^{-c(\alpha+\beta)}>0.}           \tag{0.7}
   \]

   In particular, every fixed-order and every \(o(\sqrt r)\)-order
   double-deck core Hall cut is saturated by the same positive limiting
   fraction \(\theta(c)\).

The family in item 3 has total fibre size

\[
 \exp(O(\sqrt r\log r))=o(B_r/r^K)                \tag{0.8}
\]

for every fixed \(K\). Therefore it is not a counterexample to (0.1).
It is instead a sharp obstruction to the proposed route: the missing
\(O\)-to-\(o\) saving cannot follow from trace disjointness, its shifted
copy, the exact fixed-core normal form, or any bounded/Gaussian-order
subset-enclosure Hall hierarchy. A successful proof must use a global
distribution theorem across reduced cores or a genuinely chronology-
sensitive long-period statistic.

## 1. The translated deck duplicates the conflict graph

Let \(\mathcal E^0\) be one step-two transition deck and let
\(\mathcal E^1\) be its one-edge translate. Chronological translation is
a bijection

\[
                  \sigma:\mathcal E^0\longrightarrow\mathcal E^1.
                                                               \tag{1.1}
\]

For a trace \(I\subseteq\mathcal E^0\), its companion trace is
\(\sigma I\subseteq\mathcal E^1\).

### Lemma 1.1 (exact double-deck redundancy)

For every two traces \(I,J\subseteq\mathcal E^0\),

\[
 \boxed{\sigma I\cap\sigma J=\sigma(I\cap J).}    \tag{1.2}
\]

Consequently a family \(\mathcal P\) obeys

\[
 I\cap J=\varnothing
 \quad\hbox{and}\quad
 \sigma I\cap\sigma J=\varnothing
 \qquad(I\ne J)                                  \tag{1.3}
\]

if and only if its original traces are pairwise disjoint.

#### Proof

Equation (1.2) holds for every injective map \(\sigma\). The second
condition in (1.3) is therefore equivalent to the first one. \(\square\)

This statement is about pairwise disjointness **within each deck**, which
is exactly the condition retained by the parity split in the simple-return
reduction. It does not assert that a trace is disjoint from its own
translate after the two deck copies are identified.

There is an equivalent configuration-hypergraph statement. Replace each
trace \(I\) by the two-copy configuration

\[
                    \widehat I=I^0\cup(\sigma I)^1.            \tag{1.4}
\]

Two configurations conflict in the second copy exactly when they conflict
in the first. Thus the configuration conflict graph is unchanged. In the
standard fractional set-packing relaxation, the constraint indexed by
\(\sigma e\in\mathcal E^1\) is the same row as the constraint indexed by
\(e\in\mathcal E^0\). Hence duplication of the deck cannot change either
the integral feasible families or the fractional packing optimum.

## 2. The full core-subset capacity hierarchy

Use the complementary rank-\(r\) owner normalization. At a transition
edge \(e=XY\), exactly the \(r+1\) coordinates in \(X\cup Y\) have a
positive-residence gap containing that edge: the \(r-1\) common
coordinates, the departing coordinate, and the arriving coordinate.

For a simple sector \(I\), the fixed-core theorem supplies disjoint cores
\(K_I,K'_I\), both of size \(q_I=r-s_I\), such that

* every coordinate of \(K_I\) has a residence gap containing the whole
  first-deck trace \(I\);
* every coordinate of \(K'_I\) has a residence gap containing the whole
  translated trace \(\sigma I\).

Let \(\mathcal E\) be any height-invariant quotient subdeck of size
\(E\), or its physical lift divided by the common spatial factor. Let
\(\mathcal P\) be a pairwise quotient-edge-disjoint family of simple
sectors in \(\mathcal E\).

### Lemma 2.1 (one-coordinate intersection of paired columns)

Let the consecutive omitted labels at times \(j,j+1\) be
\(\lambda_j\ne\lambda_{j+1}\). The available residence-coordinate sets
of the paired step-two edges

\[
 e^0=A_jA_{j+2},
 \qquad
 e^1=A_{j+1}A_{j+3}
\]

are

\[
 R^0=A_j\cup A_{j+2}=A_j\cup\{\lambda_j\},
 \qquad
 R^1=A_{j+1}\cup A_{j+3}
     =A_{j+1}\cup\{\lambda_{j+1}\}.              \tag{2.1}
\]

They obey

\[
 |R^0|=|R^1|=r+1,
 \qquad
 \boxed{R^0\cap R^1=\{\lambda_{j+1}\}.}         \tag{2.2}
\]

#### Proof

The two-step recurrence gives

\[
 A_{j+2}=A_j-\{\lambda_{j+1}\}+\{\lambda_j\},
\]

and the shifted analogue gives (2.1). Consecutive Kneser owners
\(A_j,A_{j+1}\) are disjoint. The label \(\lambda_j\) is absent from
both, while \(\lambda_{j+1}\in A_j\) because consecutive omitted labels
cannot agree. Thus the sole common member is \(\lambda_{j+1}\). \(\square\)

### Theorem 2.2 (exact mixed double-deck enclosure capacity)

For every \(t,u\ge0\), with the convention that an out-of-range binomial
coefficient is zero,

\[
 \boxed{
  \sum_{I\in\mathcal P}
       \binom{q_I}{t}\binom{q_I}{u}|I|
  \le
       \Delta_{r;t,u}E,}                           \tag{2.3}
\]

#### Proof

First take all \(N\) spatial lifts of the quotient subdeck and of every
selected nonwrapping trace. Distinct quotient traces have mutually
disjoint lift families, and every quotient incidence below is thereby
multiplied by the same factor \(N\). It is therefore enough to count in
the labelled physical deck and divide by \(N\) at the end.

For each \(I\), each edge \(e\in I\), each \(t\)-set
\(T\subseteq K_I\), and each \(u\)-set \(U\subseteq K'_I\), record the
incidence \((e,T,U)\). The number of recorded incidences is the left side
of (2.3).

Fix an edge \(e\). Pairwise trace disjointness puts it in at most one
selected trace. Every member of \(K_I\) belongs to the \((r+1)\)-set of
first-deck residence coordinates available at \(e\), and every member of
\(K'_I\) belongs to the \((r+1)\)-set of translated-deck residence
coordinates available at \(\sigma e\). Moreover \(K_I\cap K'_I\) is
empty. By Lemma 2.1, the two available \((r+1)\)-sets meet in one
coordinate. The number of ordered \((T,U)\) pairs with
\(|T|=t,|U|=u,T\cap U=\varnothing\) is therefore

\[
 \binom{r+1}{t}\binom{r+1}{u}
 -\binom r{t-1}\binom r{u-1}
 =\Delta_{r;t,u}.                                 \tag{2.4}
\]

The subtracted term counts precisely the pairs in which both sets use the
unique shared coordinate; after that choice their remaining elements lie
in disjoint \(r\)-sets. Summing over the \(E\) edge columns proves (2.3).
\(\square\)

The cases \((t,u)=(1,0)\) and \((0,1)\) are the two core-enclosure
ledgers. The theorem shows that taking arbitrary fixed subsets of both
cores simultaneously produces a whole hierarchy, not a stronger
asymptotic scale.

### Corollary 2.3 (no asymptotic coefficient gain)

Suppose \(s_I\le H\le A\sqrt r+1\), and put \(q_*=r-H\). Then

\[
 \sum_{I\in\mathcal P}|I|
 \le
 {\Delta_{r;t,u}
  \over
  \binom{q_*}{t}\binom{q_*}{u}}E.                \tag{2.5}
\]

If \(t,u=o(\sqrt r)\), the multiplier in (2.5) is

\[
                         1+o_A(1).                \tag{2.6}
\]

If \(t,u=O(\sqrt r)\), it is bounded above and below by positive
constants depending only on \(A\) and the two implied constants.

#### Proof

The first assertion follows from \(q_I\ge q_*\). For
\(v=O(\sqrt r)\),

\[
 \begin{aligned}
 \log{\binom{r+1}{v}\over\binom{r-H}{v}}
 &=\sum_{j=0}^{v-1}
   \log\left(1+{H+1\over r-H-j}\right)\\
 &=O_A(v/\sqrt r+v^2/r).
 \end{aligned}                                    \tag{2.7}
\]

This tends to zero for \(v=o(\sqrt r)\) and stays bounded for
\(v=O(\sqrt r)\). Also

\[
 {\Delta_{r;t,u}\over
   \binom{r+1}{t}\binom{r+1}{u}}
 =1-{tu\over(r+1)^2}=1-o(1)                      \tag{2.8}
\]

uniformly for \(t,u=O(\sqrt r)\). Apply the preceding estimates to
\(v=t,u\). \(\square\)

Combining (2.5) with \(|I|\ge h+2\) recovers only the reciprocal-height
bound, with coefficient \(1+o(1)\) for all sub-Gaussian subset orders. It
does not create a vanishing factor.

## 3. A genuine Gaussian PBBS double-deck saturator

The preceding capacity comparison is sharp inside actual PBBS dynamics.
We invoke the exact mountain-core transport and predecessor-passage
theorem proved in
`MATH_ATTACK_U_QUOTIENT_CHRONOLOGY_SATURATION_20260725.md`, and then
derive and audit the additional simplicity, double-deck, and mixed-capacity
conclusions needed here. No converse beyond that proved theorem is used.

Fix \(h\ge4\) with

\[
                         p=2h-1                  \tag{3.1}
\]

prime, and put

\[
                         y=r-h.
\]

The rank-\(r\) inverse fibre over the mountain core of height \(h-1\) is

\[
 \Omega_{r,h}=\left\{
   (n_0,\ldots,n_{p-1})\in\mathbb Z_{\ge0}^{p}:
   \sum_jn_j=y\right\},                           \tag{3.2}
\]

of size

\[
 P_{r,h}=\binom{y+p-1}{p-1}
        =\binom{r+h-2}{2h-2}.                     \tag{3.3}
\]

The PBBS step-two quotient map rotates the coordinates of (3.2) by one.
A phase starts a genuine first omitted-label return of gap \(2h+1\) if
and only if its current coordinate satisfies

\[
                              n_0=0.              \tag{3.4}
\]

Every such return has height \(h\), positive residence \(h+1\), and
trace length

\[
                              k=h+2.              \tag{3.5}
\]

Let \(U_{r,h}\) be the number of compositions having at least one zero
coordinate. Then

\[
 U_{r,h}=P_{r,h}-\binom{y-1}{p-1},                \tag{3.6}
\]

where the second binomial is zero when \(y<p\). Every zero-containing
composition is nonconstant, and primality of \(p\) gives it full rotation
period \(p\). Therefore the zero-containing compositions form exactly

\[
                         {U_{r,h}\over p}         \tag{3.7}
\]

quotient cycles. Choose one phase satisfying (3.4) on each such cycle.

### Lemma 3.1 (the selected returns are simple fixed-core sectors)

Every selected return in (3.7) is simple. Its fixed-core parameters are

\[
                    s=h,
                    \qquad q=r-h.                \tag{3.8}
\]

#### Proof

The displayed return has the minimum gap \(2h+1\) permitted by the
height-gap theorem at invariant Dyck height \(h\). If any label repeated
inside its half-open omitted-label word, two consecutive occurrences of
that label would delimit a return of odd gap strictly smaller than
\(2h+1\). Height is PBBS-invariant, so the height-gap theorem would give a
contradiction. Thus the half-open label word is repetition-free.

A simple return of gap \(2s+1\) has trace length \(s+2\). Comparing with
(3.5) gives \(s=h\), and the fixed-core theorem gives
\(q=r-s=r-h\). \(\square\)

### Lemma 3.2 (literal double-deck packing)

The \(U_{r,h}/p\) selected traces are pairwise quotient-edge-disjoint, and
their one-edge translates are pairwise quotient-edge-disjoint.

#### Proof

There is one selected trace on each of distinct quotient cycles. Since

\[
                         h+2<2h-1=p              \tag{3.9}
\]

for \(h\ge4\), every trace is nonwrapping on its cycle. Hence the selected
traces are disjoint. The translated traces are disjoint by Lemma 1.1.
\(\square\)

Thus this is a literal PBBS realization of the double-deck normal form,
not a static fixed-core decoration.

## 4. Exact limiting utilization

Assume

\[
                         {h\over\sqrt r}\longrightarrow c>0. \tag{4.1}
\]

From (3.3)--(3.6),

\[
 {U_{r,h}\over P_{r,h}}
 =1-\prod_{i=1}^{p-1}{y-i\over y+i}.              \tag{4.2}
\]

Uniform Taylor expansion, using \(p=2h+O(1)\) and \(y=r+O(\sqrt r)\),
gives

\[
 \begin{aligned}
 \sum_{i=1}^{p-1}\log{y-i\over y+i}
 &=-{2\over y}\sum_{i=1}^{p-1}i+o(1)\\
 &=-4c^2+o(1).
 \end{aligned}                                    \tag{4.3}
\]

Therefore

\[
             {U_{r,h}\over P_{r,h}}
             \longrightarrow1-e^{-4c^2}.         \tag{4.4}
\]

The fraction of fibre edges covered by the selected traces is

\[
 { (h+2)U_{r,h}\over pP_{r,h}}
 \longrightarrow {1-e^{-4c^2}\over2}
 =\theta(c).                                      \tag{4.5}
\]

By translation the same fraction is covered in the second deck.

### Theorem 4.1 (sharpness of all Gaussian-order core cuts)

Let \(t=t(r)\), \(u=u(r)\) satisfy

\[
 {t\over\sqrt r}\longrightarrow\alpha,
 \qquad
 {u\over\sqrt r}\longrightarrow\beta,
 \qquad0\le\alpha,\beta<\infty.                 \tag{4.6}
\]

For the selected PBBS family, its utilization ratio in (2.3) is

\[
 \mathcal R_{t,u}(r,h)=
 {\binom{r-h}{t}\binom{r-h}{u}(h+2)U_{r,h}/p
  \over
  \Delta_{r;t,u}P_{r,h}},                         \tag{4.7}
\]

and

\[
 \boxed{
 \mathcal R_{t,u}(r,h)
 \longrightarrow
 {1-e^{-4c^2}\over2}e^{-c(\alpha+\beta)}.}       \tag{4.8}
\]

#### Proof

By (2.8), replacing \(\Delta_{r;t,u}\) by
\(\binom{r+1}{t}\binom{r+1}{u}\) changes the ratio by \(1+o(1)\).
For \(v/\sqrt r\to\gamma<\infty\),

\[
 \begin{aligned}
 \log{\binom{r-h}{v}\over\binom{r+1}{v}}
 &=\sum_{j=0}^{v-1}
   \log\left(1-{h+1\over r+1-j}\right)\\
 &=-{(h+1)v\over r}+o(1)
 \longrightarrow-c\gamma.                       \tag{4.9}
 \end{aligned}
\]

Indeed, the total quadratic logarithm error is
\(O(vh^2/r^2)=O(r^{-1/2})\), while replacing the varying denominators by
\(r\) costs \(O(hv^2/r^2)=O(r^{-1/2})\). Apply (4.9) with
\(v=t,u\), and combine with (4.5). \(\square\)

For \(t,u=o(\sqrt r)\), (4.8) equals \(\theta(c)>0\). Hence even allowing
the Hall dual to inspect a growing, sub-Gaussian number of enclosing
coordinates in both fixed cores does not yield a vanishing utilization
factor. At the full Gaussian order it still yields only another positive
constant.

## 5. Horizon and corrected-deck audit

Fix \(A>0\) and choose \(c\) as in (0.5). Take any sequence of odd primes
\(p\to\infty\), put

\[
 h={p+1\over2},
 \qquad
 r=\left\lceil{h^2\over c^2}\right\rceil .       \tag{5.1}
\]

Then \(h/\sqrt r\to c\). Since \(c<A\),

\[
                         h+1\le H                \tag{5.2}
\]

eventually, so the returns lie within the residence horizon. Since
\(c>A/2\),

\[
                         p=2h-1>H+1              \tag{5.3}
\]

eventually, so their quotient cycles are retained in the corrected
long-cycle deck. All floor errors are absorbed by the strict inequalities
in (0.5).

The inverse-fibre size nevertheless satisfies

\[
 \log P_{r,h}=O(\sqrt r\log r)=o(r),              \tag{5.4}
\]

whereas

\[
 \log B_r=r\log4-O(\log r).                      \tag{5.5}
\]

This proves (0.8). The **outer inverse-fibre** quotient cycles have period
\(p=\Theta(\sqrt r)\), as required by (5.3), but the normalized
first-pruned mountain core itself is fixed by the reduced PBBS map and has
period one. Thus this family lies inside the already removable
short-**reduced-core**-period sector when capacities are summed over all
cores. These two periods must not be conflated.

## 6. Exact implication boundary

The following proposed implications are false:

\[
 \begin{gathered}
 \text{simple fixed-core sectors}
 +\text{ pairwise trace disjointness}
 +\text{ pairwise translated-trace disjointness}
 \\
 \Longrightarrow
 \text{vanishing utilization of a Gaussian height deck},     \tag{6.1}
 \end{gathered}
\]

and, for every \(t,u=O(\sqrt r)\),

\[
 \begin{gathered}
 \text{the preceding hypotheses}
 +\text{ all }(t,u)\text{ core-subset enclosure capacities}
 \\
 \Longrightarrow
 o(1)\text{ utilization}.                         \tag{6.2}
 \end{gathered}
\]

The counterexample to (6.1)--(6.2) is literal PBBS dynamics on an actual
Gaussian-height invariant fibre. It is not a counterexample to the global
gate (0.1), because the fibre has exponentially negligible Catalan mass.

Thus the critical double-deck saturation normal form is useful only as a
localization theorem. Its shifted-deck clause is not an additional source
of Hall expansion. To prove (0.1), one must add a statistic which the
mountain fibre does not possess at global scale. The currently exact
possibilities are:

1. a Catalan-weighted theorem showing that all reduced-core transports
   capable of positive double-deck utilization have total mass
   \(o(B_r)\);
2. a long-period chronology theorem, after deleting all core periods
   \(L\) with \(L\log r=o(r)\);
3. a cross-fibre passage-hyperplane inequality which is not a nonnegative
   combination of the local enclosure rows (2.3).

No such global theorem is proved here. The theorem-level conclusion is
the sharp obstruction: **the entire local double-deck Hall/capacity route,
including its growing core-subset hierarchy, cannot supply the critical
\(O\)-to-\(o\) saving.**

## 7. Independent audit of the decisive constants

1. **Trace length.** A gap \(2h+1\) return has step-two positive
   residence \(h+1\) and includes its insertion/removal boundary edges,
   hence \(h+2\) quotient transition edges.
2. **Simplicity.** Any internal repeated label gives a consecutive return
   gap at most \(2h-1\), contradicting the height-\(h\) gap lower bound
   \(2h+1\).
3. **Period.** A zero-containing composition with positive total is
   nonconstant. Prime period \(p\) therefore makes its rotation orbit
   exactly \(p\), so the orbit count is \(U_{r,h}/p\).
4. **Nonwrapping.** \(h+2<p=2h-1\) is equivalent to \(h>3\).
5. **Zero-coordinate mass.** The positive compositions are counted by
   \(\binom{y-1}{p-1}\); division by (3.3) gives the product in (4.2).
6. **Exponential constant.** Since
   \(2\sum_{i=1}^{p-1}i/y=p(p-1)/y\to4c^2\), the missing-positive-
   composition factor is \(e^{-4c^2}\), not \(e^{-2c^2}\).
7. **Packing fraction.** Multiplication by trace length and division by
   orbit period gives \((h+2)/p\to1/2\), yielding (0.6).
8. **Core ratio.** For \(v\sim\gamma\sqrt r\), the logarithm of the
   core-capacity ratio is \(-hv/r+o(1)\to-c\gamma\). The two cores add
   their exponents and give (0.7).
9. **Implication scope.** The construction disproves local and fibrewise
   vanishing-capacity statements only. Equation (5.4) explicitly prevents
   promotion to a global counterexample to \((\mathrm{ST}_A)\).
