# Ladder-contracted common-core paths: effective conflicts and the sharp isolated-nibble barrier

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

This note contracts the vertical signed-rank ladders in
`MATH_THEOREM_COMMON_CORE_TIGHT_PATH_CONFIGURATION_HYPERGRAPH_20260726.md`.
It never treats the \(2d+1\) masks of a tag-\(d\) phase as independent
nibble vertices.

## 0. Outcome

Retain the notation

\[
 H=(1+o(1))\sqrt{m\log m},\quad
 M=m+H,\quad s=m-H,\quad L=m-3H+1,
\tag{0.1}
\]

\[
 W=\binom{2m}m,\quad N=N_H,\quad
 D=M!,\quad
 \rho_q=\frac{b_q}{\Lambda_q}\le1,
 \quad \Lambda_q=\frac{N_q}{N},
\tag{0.2}
\]

and

\[
 k=L+2\sum_{q=1}^{H-1}b_q
   =(\sqrt\pi+o(1))m^{3/2}.
\tag{0.3}
\]

For a phase of tag \(d\), its **contracted ladder** is the single
structured object

\[
 \lambda=(X_{-d}\subset X_{-d+1}\subset\cdots\subset X_d),
 \qquad |X_r|=m+r.
\tag{0.4}
\]

Two ladders conflict when they share any physical target at the same
signed rank. A path configuration consists of \(L\) chronologically
coupled ladders.

The exact conclusions are:

1. If

   \[
    R_d=\rho_0+2\sum_{q=1}^d\rho_q,
   \tag{0.5}
   \]

   then the number of complete path states, over other roots, which
   conflict with one fixed height-\(d\) ladder is

   \[
    \boxed{
    \deg_{\rm eff}(\lambda)
      =D R_d+O(D(d+1)/m).}
   \tag{0.6}
   \]

   For every tag height which actually occurs, \(R_d=\Theta(d+1)\).

2. For arbitrary disjoint ladders of heights \(d,e\),

   \[
    \deg_{\rm eff}(\lambda,\mu)
      \le \frac{C D}{m}(2d+1)(2e+1).
   \tag{0.7}
   \]

   If the two ladders occur in one common physical path, the chronology
   improves this to

   \[
    \boxed{
    \deg_{\rm eff}(\lambda,\mu)
      \le \frac{C D}{m}\min\{R_d,R_e\}.}
   \tag{0.8}
   \]

   Thus the co-path relative ladder codegree is \(O(1/m)\). After
   contraction the formal edge rank is \(L\sim m\), so the product is
   only \(O(1)\), not \(o(1)\). Vertical contraction reaches a critical
   boundary; it does not enter a black-box vanishing-codegree regime.

3. More decisively, let \(\Gamma(P)\) be the set of complete states over
   roots different from that of \(P\) which share at least one physical
   target with \(P\). Then, uniformly in every path state,

   \[
    \boxed{
                         |\Gamma(P)|=(1-o(1))kD.}
   \tag{0.9}
   \]

   Hence the ladder conflicts of a fixed path do not substantially
   coalesce in catalogue measure. The worst-case \(O(H^2)\) intersection
   of two paths is real but exceptionally sparse.

4. Consider the natural tentative nibble: activate roots independently
   with probability \(p\), choose a uniform path state at each activated
   root, and retain only isolated states. Its expected output is at most

   \[
    \boxed{
       pN\exp(-(1-o(1))pk)
       \le (1+o(1))\frac{N}{e k}.}
   \tag{0.10}
   \]

   The previous \(\Omega(N/k)\) one-bite theorem is therefore sharp in
   order for every isolated-contention nibble, even after exact ladder
   contraction. Activating at rate \(1/L\) gives \(pk\asymp\sqrt m\)
   and exponentially small survival; no finite-density isolated bite is
   possible.

The barrier (0.10) does not rule out a coordinated matching inside the
nontrivial conflict components of a tentative bite. Such a procedure is
already a slack version of the original rooted matching problem. No
ladder-aware regeneration theorem reaching root leave
\(o(N/\sqrt m)\) is proved. What is proved is that contraction alone
cannot turn the existing independent nibble into such a theorem.

## 1. Contracted ladder objects

Fix one physical path state \(P=e(U,z)\). At phase \(j\), whose fixed
tag is \(d_j=d\), put

\[
 \lambda_j(P)
 =\bigl(C_{z,j}(-d),C_{z,j}(-d+1),\ldots,C_{z,j}(d)\bigr).
\tag{1.1}
\]

The trace formula gives

\[
 C_{z,j}(-d)\subset C_{z,j}(-d+1)\subset\cdots
 \subset C_{z,j}(d),
\tag{1.2}
\]

with one coordinate added at each step. We regard the whole saturated
flag (1.2), including its order, as one phase object.

Let \(V(\lambda)\) denote its set of \(2d+1\) physical targets. For a
ladder belonging to a state over root \(U\), define its effective
conflict star by

\[
 \Gamma(\lambda)
 =\{F:\operatorname {root}(F)\ne U,
           V(\lambda)\cap P(F)\ne\varnothing\}.
\tag{1.3}
\]

For two target-disjoint ladders, put

\[
 \Gamma(\lambda,\mu)=\Gamma(\lambda)\cap\Gamma(\mu).
\tag{1.4}
\]

These are conflict degrees, not incidence degrees of an artificial
full-flag vertex. A different path conflicts with \(\lambda\) as soon as
it repeats any one member of the flag.

For completeness, if \(g_d\) is the number of phase positions with tag
exactly \(d\), the number of complete height-\(d\) saturated flags is

\[
 |\mathscr L_d|
 =N_d\frac{(m+d)!}{(m-d)!},
\tag{1.5}
\]

and a fixed such flag occurs in

\[
 \boxed{
 D_{\rm flag}(d)=g_d\frac{(m-d)!^2}{s!}}
\tag{1.6}
\]

path states.

#### Proof of (1.5)--(1.6)

Choose the lower endpoint of size \(m-d\), choose the \(2d\) coordinates
added before the upper endpoint, and order those additions. This gives

\[
 \binom{2m}{m-d}\binom{m+d}{2d}(2d)!
 =N_d\frac{(m+d)!}{(m-d)!},
\]

proving (1.5).

For a fixed flag and a fixed phase position of tag \(d\), first choose
the top extension of its upper endpoint in
\(\binom{m-d}{H-d}\) ways. The \(2d\) intermediate positions are forced
by the ordered flag, the upper deletion suffix may be ordered in
\((H-d)!\) ways, and the remaining positions in \((m-d)!\) ways. Thus
the count is

\[
 g_d\binom{m-d}{H-d}(H-d)!(m-d)!
 =g_d\frac{(m-d)!^2}{s!}.
\]

\(\square\)

Equality

\[
                         |\mathscr L_d|D_{\rm flag}(d)=NDg_d
\tag{1.7}
\]

checks the ledger exactly.

## 2. A path-row codegree summation lemma

The pointwise estimate \(d(X,Y)\le4D/m\) is not sufficient by itself;
there are \(\Theta(k^2)\) pairs in a path. The path interval geometry
gives a much stronger row sum.

### Lemma 2.1 (minimum active deletion length)

There is an absolute \(c>0\) such that every positive-degree upper trace
has deletion length

\[
                         \ell\ge g:=c\frac mH.
\tag{2.1}
\]

Middle and lower traces have deletion length at least \(H\), so every
target in every protected path has interval length at least \(g\).

#### Proof

If the upper depth is \(q\) and \(b_q>0\), definition of \(b_q\) gives
\(N_q/N_H\ge2\). Put \(\ell=H-q\). The exact product is

\[
 \frac{N_q}{N_H}
 =\prod_{i=q+1}^{H}\frac{m+i}{m-i+1}.
\tag{2.2}
\]

Every logarithmic factor is \(O(H/m)\). To make the logarithm of the
product at least \(\log2\), there must be
\(\ell=\Omega(m/H)\) factors. \(\square\)

### Lemma 2.2 (one physical trace versus one path)

There is an absolute \(C\) such that, for every path state \(P\) and
every target \(X\in P\),

\[
 \boxed{
 \sum_{\substack{Y\in P\\Y\ne X}}d(X,Y)
 \le\frac C m\,d(X).}
\tag{2.3}
\]

#### Proof

Represent \(X\) by its deleted interval \(I\) in the common tail word,
and let \(J\) be the interval of another target \(Y\). Put

\[
                         u=|I\triangle J|.
\tag{2.4}
\]

Suppose first that \(I\cap J\ne\varnothing\). Two intersecting integer
intervals with symmetric difference \(u\) have endpoint displacement
of total absolute value \(u\). Therefore, for fixed \(I\), at most

\[
                         4(u+1)
\tag{2.5}
\]

integer intervals \(J\) have this value of \(u\). The exact pair formula
of the configuration hypergraph gives

\[
 \frac{d(X,Y)}{d(X)}
 \le\frac{(u+1)u!}{(m-3H)^u}.
\tag{2.6}
\]

Consequently all intersecting \(J\)'s contribute at most

\[
 \sum_{u\ge1}
 4(u+1)^2\frac{u!}{(m-3H)^u}
 =O(1/m).
\tag{2.7}
\]

The series is decreasing geometrically after its first term because
\(u\le4H=o(m)\).

If \(I,J\) are disjoint, then Lemma 2.1 gives

\[
                         u=|I|+|J|\ge2g.
\tag{2.8}
\]

There are at most \(k\) choices for \(Y\), and the disjoint-interval
part of the exact pair formula gives

\[
 \frac{d(X,Y)}{d(X)}
 \le m\frac{u!}{(m-3H)^u}
 \le m\left(\frac{4H}{m-3H}\right)^u.
\tag{2.9}
\]

Using \(u\ge2g=\Omega(m/H)\), \(k=O(m^{3/2})\), and
\(H=\Theta(\sqrt{m\log m})\), the total of (2.9) is
\(m^{-\omega(1)}\). Combining it with (2.7) proves (2.3). \(\square\)

### Corollary 2.3 (whole-path pair moment)

For every path state,

\[
 \boxed{
 \sum_{\{X,Y\}\subseteq P}d(X,Y)
 \le\frac C m\sum_{X\in P}d(X)
 =O(kD/m).}
\tag{2.10}
\]

This includes the vertical pairs, all unequal-phase diagonals, and both
signs. The vertical-spine lower bound from the predecessor note shows
that the order \(kD/m=\Theta(D\sqrt m)\) is attained.

## 3. Effective ladder degrees and codegrees

### Theorem 3.1 (one-ladder effective degree)

Let \(\lambda\) have height \(d\) and belong to a path over root \(U\).
Then

\[
 \boxed{
 |\Gamma(\lambda)|
 =D R_d+O(D(d+1)/m),
 \qquad
 R_d=\rho_0+2\sum_{q=1}^d\rho_q.}
\tag{3.1}
\]

If a tag of height \(d\) occurs, then

\[
                         c_1(d+1)\le R_d\le2d+1
\tag{3.2}
\]

for an absolute \(c_1>0\).

#### Proof

For each target \(X\in V(\lambda)\), let \(\mathcal S_X\) be the set of
states over roots other than \(U\) which contain \(X\). Then

\[
 |\mathcal S_X|=d(X)-d(U,X).
\]

The degree formulas give

\[
 \sum_{X\in V(\lambda)}d(X)=DR_d,
 \qquad
 \sum_{X\in V(\lambda)}d(U,X)=O(D(d+1)/m).
\tag{3.3}
\]

The union bound gives the upper side of (3.1). Bonferroni gives

\[
 \left|\bigcup_X\mathcal S_X\right|
 \ge\sum_X|\mathcal S_X|
      -\sum_{X<Y}d(X,Y).
\tag{3.4}
\]

Apply Lemma 2.2 and sum only over the one ladder to bound the pair term
by \(O(D(d+1)/m)\). This proves (3.1).

Whenever \(d\) occurs as a tag, all \(b_q\) for \(q\le d\) are positive.
For the chosen floor profile, a positive ratio
\(b_q/\Lambda_q\) is bounded below by an absolute constant: in the
uncapped case \(b_q=\lfloor\Lambda_q\rfloor-1\) with
\(\Lambda_q\ge2\), and in the capped case the ratio tends to one. This
proves (3.2). \(\square\)

### Theorem 3.2 (effective ladder codegrees)

Let \(\lambda,\mu\) be target-disjoint ladders of heights \(d,e\).
Then

\[
 \boxed{
 |\Gamma(\lambda,\mu)|
 \le\frac{4D}{m}(2d+1)(2e+1).}
\tag{3.5}
\]

If the two ladders occur in one common path state, then

\[
 \boxed{
 |\Gamma(\lambda,\mu)|
 \le\frac C m D\min\{R_d,R_e\}.}
\tag{3.6}
\]

Consequently the co-path effective relative codegree is \(O(1/m)\).

#### Proof

A state in both conflict stars contains some
\(X\in V(\lambda)\) and some \(Y\in V(\mu)\). Therefore

\[
 |\Gamma(\lambda,\mu)|
 \le\sum_{X\in V(\lambda)}\sum_{Y\in V(\mu)}d(X,Y).
\tag{3.7}
\]

The universal pair bound \(d(X,Y)\le4D/m\) proves (3.5).

If the ladders lie in a common path, fix the one with smaller \(R\)-mass
and apply Lemma 2.2 to every target in it, summing only over targets of
the other ladder. The result is at most

\[
 \frac C m\sum_{X\in V(\lambda)}d(X)
 =\frac C mDR_d.
\]

Interchanging the ladders proves (3.6). Divide by Theorem 3.1 and use
(3.2) to obtain the relative statement. \(\square\)

The contraction has therefore done something real. Before contraction,
one path had \(\Omega(\sqrt m)\) normalized pair mass from adjacent
vertices of the same vertical ladders. After contraction, the relevant
co-path ladder codegree is \(O(1/m)\) and there are only \(L\sim m\)
ladders. The formal product is critical:

\[
                         L\cdot O(1/m)=O(1),
\tag{3.8}
\]

not divergent, but also not \(o(1)\). A black-box nibble whose error
requires a vanishing product still does not apply.

## 4. The full-path effective conflict degree

For a path state \(P=e(U,z)\), define

\[
 \Gamma(P)
 =\{F:\operatorname {root}(F)\ne U,\ P(F)\cap P\ne\varnothing\}.
\tag{4.1}
\]

The contracted path has \(L\) ladder objects, but \(\Gamma(P)\) retains
the literal capacity rule: sharing one target anywhere in two ladders is
a conflict.

### Lemma 4.1 (degree mass of one path)

Uniformly in \(P\),

\[
 \sum_{X\in P}d(X)=(1-o(1))kD,
\tag{4.2}
\]

and

\[
 \sum_{X\in P}d(U,X)=O(kD/m).
\tag{4.3}
\]

#### Proof

The first sum divided by \(D\) is

\[
 \kappa
 =L\rho_0+2\sum_{q=1}^{H-1}b_q\rho_q.
\tag{4.4}
\]

For an uncapped depth,
\(b_q=\Lambda_q-O(1)\), so its contribution to \(k-\kappa\) is
\(O(1)\). There are \(O(H)\) such depths. At the
\(O(\sqrt H)\) capped depths, the loss is \(O(H)\) per depth. The middle
loss is \(O(H)\). Hence

\[
                         k-\kappa=O(H^{3/2})=o(k),
\tag{4.5}
\]

proving (4.2). The root--target codegree bound
\(d(U,X)\le3D/m\), summed over the \(k\) targets, proves (4.3).
\(\square\)

### Theorem 4.2 (asymptotically unclustered conflict stars)

For every path state,

\[
 \boxed{
                         |\Gamma(P)|=(1-o(1))kD.}
\tag{4.6}
\]

#### Proof

For \(X\in P\), let \(\mathcal S_X\) again denote its state star after
deleting states over root \(U\). The union bound and Lemma 4.1 give

\[
 \left|\bigcup_{X\in P}\mathcal S_X\right|
 \le\sum_X|\mathcal S_X|
 \le(1+o(1))kD.
\tag{4.7}
\]

Bonferroni, Lemma 4.1, and Corollary 2.3 give

\[
 \begin{aligned}
 \left|\bigcup_{X\in P}\mathcal S_X\right|
 &\ge\sum_X(d(X)-d(U,X))
       -\sum_{X<Y}d(X,Y)\\
 &\ge(1-o(1))kD-O(kD/m)
  =(1-o(1))kD.
 \end{aligned}
\tag{4.8}
\]

The union is exactly \(\Gamma(P)\), proving (4.6). \(\square\)

This theorem is stronger than the worst-case intersection bound. Two
particular paths may share \(O(H^2)\) traces, but the set of catalogue
states which share two or more prescribed traces with \(P\) has total
mass only \(O(kD/m)\). Thus almost every conflict edge is witnessed by
one physical target only.

## 5. The sharp isolated-nibble barrier

Consider the following entire class of tentative-selection bites.

1. Every root is activated independently with a common probability
   \(p\in[0,1]\).
2. At every activated root, one of its \(D\) path states is selected
   uniformly.
3. A selected state is retained only if it has no target conflict with
   any other selected state.

The rule in item 3 may discard additional states, but it may not retain
a nonisolated state. This is the standard independent isolated-contention
nibble, now applied after exact ladder contraction.

### Theorem 5.1 (no finite-density isolated bite)

The expected number \(Z_p\) of retained states satisfies

\[
 \boxed{
 \mathbb EZ_p
 \le pN\exp(-(1-o(1))pk).}
\tag{5.1}
\]

Uniformly in \(p\),

\[
 \boxed{
                         \mathbb EZ_p
                         \le(1+o(1))\frac N{e k}.}
\tag{5.2}
\]

Consequently an activation \(p\asymp1/L\) has survival probability at
most

\[
                         \exp(-\Theta(k/L))
                         =\exp(-\Theta(\sqrt m)),
\tag{5.3}
\]

and a fixed positive activation density has survival
\(\exp(-\Theta(m^{3/2}))\).

#### Proof

Fix a selected state \(P\) over root \(U\). For every other root \(V\),
let

\[
 a_V(P)=|\{F:\operatorname {root}(F)=V,\ F\in\Gamma(P)\}|.
\tag{5.4}
\]

Conditional on \(P\), root \(V\) produces no selected conflict with
probability

\[
                         1-p\frac{a_V(P)}D.
\]

The roots act independently, so the probability that \(P\) is isolated
is

\[
 \begin{aligned}
 \prod_{V\ne U}\left(1-p\frac{a_V(P)}D\right)
 &\le
 \exp\left(-\frac pD\sum_{V\ne U}a_V(P)\right)\\
 &=\exp\left(-\frac pD|\Gamma(P)|\right)\\
 &\le\exp(-(1-o(1))pk),
 \end{aligned}
\tag{5.5}
\]

by Theorem 4.2. Multiplying by the activation probability and summing
over the \(N\) roots proves (5.1).

The maximum of \(p e^{-(1-o(1))pk}\) occurs at
\(p=(1+o(1))/k\) and equals \((1+o(1))/(ek)\), proving (5.2).
Equation (5.3) follows from \(k/L=\Theta(\sqrt m)\). \(\square\)

The predecessor note constructed an isolated bite of size
\(\Omega(N/k)\). Theorem 5.1 proves that this order is optimal for the
whole isolated-contention class. Vertical contraction does not improve
its density.

## 6. What a genuine ladder-aware nibble would have to add

Theorem 5.1 does not bound a rule which activates many roots and then
computes a coordinated matching inside each nontrivial conflict
component. Such a rule may retain nonisolated tentative states after
discarding their competitors. But at activation density \(p\), a typical
tentative state has conflict degree of order \(pk\). Thus:

* for \(p=\Theta(1/k)\), components are at the ordinary sparse-nibble
  scale and only \(\Theta(N/k)\) roots are exposed per bite;
* for \(p=\Theta(1/L)\), the conflict scale is \(\Theta(\sqrt m)\);
* for fixed \(p>0\), the conflict scale is \(\Theta(m^{3/2})\).

A finite-density procedure must therefore solve a large structured
matching inside its bite. Fractional capacity is available, but proving
that the bite contains a matching retaining \((1-o(1))pN\) roots is a
slack version of the same common-history theorem, not a consequence of
the ladder degrees (3.1) or codegrees (3.6).

The smallest credible positive successor is a nonisolated
**contiguous-block contention resolution**. It would group consecutive
phase ladders, solve their nearest-diagonal conflicts jointly, and prove
that after every bite the remaining full path catalogue retains the
ratios \(\rho_q\) simultaneously. To reach coefficient one it must end
with

\[
                         N-|Q|=o(N/\sqrt m).
\tag{6.1}
\]

No such regeneration or absorption theorem is proved here.

## 7. Audited boundary

Proved:

1. the exact full-flag count and occurrence degree for one contracted
   phase ladder;
2. the path-row codegree summation lemma (2.3), without re-expanding the
   ladder in the nibble model;
3. the effective ladder degree (3.1);
4. arbitrary and co-path effective ladder codegrees (3.5)--(3.6);
5. the critical contracted parameter \(L\delta_{\rm eff}=O(1)\);
6. the exact full-path conflict degree \((1-o(1))kD\); and
7. the sharp \(O(N/k)\) upper bound for every independent
   keep-only-isolated nibble.

Not proved:

1. a finite-density nonisolated contention resolution;
2. regeneration of the joint signed-rank ratios after a bite;
3. a matching with root leave \(o(N/\sqrt m)\);
4. a common-history absorber; or
5. coefficient one.

The natural barrier is now precise. Vertical contraction removes an
artificial within-ladder moment, but it does not make conflicts of whole
paths coalesce: their effective conflict degree remains asymptotically
\(kD\). Any successful finite-density nibble must coordinate conflicting
tentative paths rather than isolate them.
