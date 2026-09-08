# Audit and exact integral gate for common-core tight-path fusion

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 N=N_H,
\tag{0.1}
\]

and

\[
 M=m+H,\qquad s=m-H,\qquad L=s-2H+1=m-3H+1.
\tag{0.2}
\]

Assume the hypotheses of
MATH_THEOREM_S_GLOBAL_COMMON_CORE_PROMOTION_ATLAS_20260726.md:

\[
 H=(1+o(1))\sqrt{m\log m},\qquad m>4H,
\tag{0.3}
\]

and

\[
 L+c_0H\le {W\over N}\le m+C_0H
\tag{0.4}
\]

for fixed positive constants \(c_0,C_0\).

The source's random-core degree calculations, clone-Hall theorems,
literal core-safe path construction, and

\[
                         O(H^{3/2}N)=o(W)
\tag{0.5}
\]

aggregate rankwise hole ledger are correct.

Two scope corrections are required.

1. The proof of its Theorem 4.1 averages over options in which the core
   varies.  It does not itself prove a fractional path packing for the
   one fixed core assignment used in its Theorems 1--3.
2. Its final gate must specify a full order of
   \(S_U=U\setminus Q_U\), not only the length-\((s-H)\) subword
   carrying the middle windows.  The omitted ordered \(H\)-prefix
   determines lower traces near the path boundary.

The first gap is repairable.  The fixed good cores themselves admit one
simultaneous fractional distribution on literal tail orders with nested
tags, respecting every middle and signed target capacity.

The integral fusion, however, is not a formal consequence of the
rankwise Hall matchings.  This note proves three exact obstructions.

* Once targets are assigned to phase/depth cells, one tail order exists
  if and only if an explicit signature bipartite graph has a perfect
  matching.
* For a complete trace table, fusion is equivalent to the diagonal-shell
  identities
  \[
        D_{j,\ell}=D_{j+1,\ell+1}
  \]
  and distinctness between different diagonals.
* Already at depth one, lower and upper assignments must satisfy the
  joint cuts
  \[
  r_-(A)+r_+(\mathcal X\setminus A)\ge b
  \qquad(A\subseteq\mathcal X).
  \tag{0.6}
  \]
  Separate lower and upper Hall only check two endpoint cuts.  A literal
  core-safe path with \(b=L-1\) is constructed below for which both
  separate matchings exist but the common flow has value only \(L-2\).

There is also a literal determinant-\(2\) triangle on three distinct
tops.  Thus the local order polytope is integral, but global
identification of physical targets introduces genuine odd-set cuts.

The route does not yet prove coefficient one.  The exact residual
ledger is to choose one configuration in every top fibre with total
physical target-collision excess \(o(W)\); see Theorem 6.0.  A stronger,
clean sufficient integral theorem is the near-perfect matching estimate

\[
 \boxed{\nu(\mathcal K_{\mathbf Q})
       =N-o(N/\sqrt m)}
\tag{0.7}
\]

for the fixed-core, all-depth path-configuration hypergraph defined in
Section 6.  Neither the exact collision statement nor this stronger
matching estimate is proved here.

## 1. Audit of the common-core atlas

For every rank-\(M\) top \(U\), the source chooses a core

\[
                         Q_U\in\binom U{2H}.
\tag{1.1}
\]

At the middle, a top has

\[
                         d_0=\binom{s}{H}
\tag{1.2}
\]

core-compatible owners.  For a fixed middle owner \(X\), the random
number of compatible tops has mean

\[
 \binom mH{\binom m{2H}\over\binom M{2H}}
 ={(m!)^2\over H!(m-2H)!M!}
 ={d_0\over W/N}.
\tag{1.3}
\]

The threshold \(d_0/L\) exceeds this mean by relative amount

\[
                         {W/N\over L}-1=\Theta(H/m).
\tag{1.4}
\]

Its Chernoff exponent is therefore at least

\[
                  c\,{d_0H^2\over m^3}\gg m.
\tag{1.5}
\]

Since \(W<4^m\), the union bound proving the middle maximum-degree cap
is valid.  The clone-Hall proof also handles arbitrary partial clone
sets: completing every touched top fibre leaves its neighbourhood
unchanged and only increases the number of clones to be bounded.

At signed rank \(m+r\), \(-H<r<H\), the exact left degree and mean
right degree are

\[
 d_r=\binom{s}{H-r},\qquad
 \mu_r={d_r\over\Lambda_r},\qquad
 \Lambda_r={N_{|r|}\over N}.
\tag{1.6}
\]

For

\[
 b_0=L,\qquad
 b_q=\min\left\{L-1,
       \max\left\{0,\left\lfloor{N_q\over N}\right\rfloor-1\right\}
       \right\}
 \quad(1\le q<H),
\tag{1.7}
\]

put \(b_H=0\).  Whenever \(b_{|r|}>0\), the Chernoff exponent at
\(d_r/b_{|r|}\) is at least

\[
                         c\,{d_r\over\Lambda_r^3}.
\tag{1.8}
\]

For \(r>0\), positivity of \(b_r\) implies
\(H-r=\Omega(m/H)\); for \(r<0\), one has \(H-r\ge H\).
Consequently (1.8) is much larger than \(m\), uniformly over all
protected ranks.  The union bound over \(O(HW)\) target rows is valid.
The ensuing rankwise clone-Hall matchings are therefore correct.

At an uncapped depth,

\[
                         0\le N_q-b_qN<2N.
\tag{1.9}
\]

The cap \(b_q=L-1\) occurs only for \(q=O(\sqrt H)\), and then

\[
                         {N_q\over N}-(L-1)=O(H).
\tag{1.10}
\]

Thus both signs together have the deficit (0.5).  Finally,

\[
 {H^{3/2}N\over W}
 =O\left({H^{3/2}\over m}\right)=o(1).
\tag{1.11}
\]

This verifies every numerical and asymptotic assertion in the source's
Theorems 1.1--3.2 and Proposition 3.3.

Its core-safe path count is also exact.  If
\(S=U\setminus Q\), \(|S|=s\), then exactly

\[
                         s-2H+1=L
\tag{1.12}
\]

length-\(2H\) central words lie wholly inside the ordered \(S\)-block.
They are consecutive phases.  At every non-top rank, different phases
delete distinct equal-length intervals of an injective word.  At the
top rank the deletion is empty, explaining the requirement of at most
one tag \(H\).

## 2. A simultaneous fractional point for the fixed good cores

Fix one core assignment satisfying all the degree caps above.  For each
top \(U\), put \(S_U=U\setminus Q_U\), and fix an arbitrary order of
the elements of \(Q_U\).  This supplies the literal cyclic rooting;
none of the retained target sets depends on that order.  Choose nested phase sets

\[
 [L]=A_0\supseteq A_1\supseteq\cdots
 \supseteq A_{H-1}\supseteq A_H=\varnothing,
 \qquad |A_q|=b_q.
\tag{2.1}
\]

They define one fixed tag pattern.  Independently and uniformly order
the \(s\) elements of every \(S_U\).

### Theorem 2.1 (fixed-core common-history fractional feasibility)

The resulting distribution on literal tagged paths has load at most one
on every middle target and every protected signed target.  It has total
mass one in every top fibre.

#### Proof

Fix a target \(Y\) of rank \(m+r\), put

\[
                         \ell=H-r,
\tag{2.2}
\]

and suppose \(Q_U\subseteq Y\subseteq U\).  Then
\(I=U\setminus Y\) is a fixed \(\ell\)-subset of \(S_U\).  At a fixed
phase, the deletion interval of a uniform \(S_U\)-order is a uniform
\(\ell\)-subset.  The \(b_{|r|}\) active phase positions are distinct,
so

\[
 \Pr_U(Y\hbox{ is used})={b_{|r|}\over\binom{s}{\ell}}
                         ={b_{|r|}\over d_r}.
\tag{2.3}
\]

The fixed-core degree cap gives

\[
 \operatorname{load}(Y)
 =\deg_r(Y){b_{|r|}\over d_r}\le1.
\tag{2.4}
\]

At the middle, all \(L\) phases are active, and the identical argument
gives

\[
 \operatorname{load}(X)
 =\deg_0(X){L\over d_0}\le1.
\tag{2.5}
\]

Every sampled object is one order with one nested phase profile.
\(\square\)

Hence every nonnegative additive Farkas cut passes even after the good
cores have been fixed.  The remaining obstruction is integral and
common-history, not fractional or rankwise.

## 3. Exact local reconstruction of one tail order

Fix \(U,Q\), put \(S=U\setminus Q\), and let

\[
 w=(w_1,\ldots,w_s)
\tag{3.1}
\]

be a permutation of \(S\).  For phase \(1\le j\le L\) and deletion
length \(0\le\ell\le2H\), define

\[
 R_{j,\ell}
 =\{j+2H-\ell,\ldots,j+2H-1\}\subseteq[s],
 \qquad R_{j,0}=\varnothing,
\tag{3.2}
\]

\[
 I_{j,\ell}=\{w_t:t\in R_{j,\ell}\},\qquad
 T_{j,\ell}=U\setminus I_{j,\ell}.
\tag{3.3}
\]

Here \(\ell=H\) is the middle, \(\ell=H-q\) is upper depth \(q\),
and \(\ell=H+q\) is lower depth \(q\).

Let \(\mathcal O\) be any set of observed phase/depth cells, with
prescribed deletion sets \(I_{j,\ell}\subseteq S\) of the required
sizes.  For \(a\in S\), \(t\in[s]\), define the membership signatures

\[
 \tau(a)=({\bf1}_{a\in I_{j,\ell}})_{(j,\ell)\in\mathcal O},
 \qquad
 \sigma(t)=({\bf1}_{t\in R_{j,\ell}})_{(j,\ell)\in\mathcal O}.
\tag{3.4}
\]

### Theorem 3.1 (signature-Hall fusion)

The prescribed cells arise from one tail order if and only if

\[
 |\{a\in S:\tau(a)=\eta\}|
 =
 |\{t\in[s]:\sigma(t)=\eta\}|
\tag{3.5}
\]

for every binary signature \(\eta\).

Equivalently, the bipartite graph

\[
 a\sim t\quad\Longleftrightarrow\quad\tau(a)=\sigma(t)
\tag{3.6}
\]

has a perfect matching, or, equivalently, satisfies every Hall cut.

#### Proof

If \(w_t=a\), membership of \(a\) in every prescribed deletion set must
equal membership of position \(t\) in the corresponding positional
interval.  Thus a realizing word gives a perfect matching in (3.6).
Conversely, a perfect matching places every coordinate in its matched
position and gives (3.3).

The graph (3.6) is a disjoint union of complete bipartite graphs, one
for each signature.  It has a perfect matching exactly when the two
shores of every component have equal sizes, which is (3.5).
\(\square\)

Thus the exact local obstruction is not pairwise containment alone.  All
Boolean atoms of the assigned deletion sets must have the same sizes as
the corresponding Boolean atoms of the positional intervals.

For a complete array define

\[
 D_{j,\ell}=I_{j,\ell}\setminus I_{j,\ell-1}
 \qquad(1\le\ell\le2H).
\tag{3.7}
\]

### Theorem 3.2 (diagonal-shell criterion)

A complete array comes from one tail order if and only if:

1. \(I_{j,0}=\varnothing\);
2. \(I_{j,\ell-1}\subset I_{j,\ell}\), and every
   \(D_{j,\ell}\) is a singleton;
3. for \(j<L,\ell<2H\),
   \[
   D_{j,\ell}=D_{j+1,\ell+1};
   \tag{3.8}
   \]
4. shells on different diagonals are distinct:
   \[
   j+2H-\ell\ne k+2H-r
   \ \Longrightarrow\
   D_{j,\ell}\ne D_{k,r}.
   \tag{3.9}
   \]

The inducing order is unique, with

\[
                         D_{j,\ell}=\{w_{j+2H-\ell}\}.
\tag{3.10}
\]

#### Proof

Necessity follows from (3.2)--(3.3).  Conversely,
\(t=j+2H-\ell\) ranges over every \(1\le t\le s\).
The diamond identities identify all shells on one diagonal, and (3.9)
makes the \(s\) diagonal labels distinct.  They therefore define a
permutation \(w_1,\ldots,w_s\) of \(S\).  Nesting gives

\[
 I_{j,\ell}
 =\bigcup_{h=1}^{\ell}D_{j,h}
 =\{w_{j+2H-\ell},\ldots,w_{j+2H-1}\}.
\tag{3.11}
\]

This proves sufficiency and uniqueness. \(\square\)

The equality (3.8) is the smallest exact cross-phase/cross-rank identity
erased by separate Hall.

There is no local convex-hull defect hidden here.  If \(z_{t,a}\) is a
doubly stochastic assignment of coordinates \(a\in S\) to positions
\(t\in[s]\), then

\[
 x_{j,\ell,a}
 =\sum_{t\in R_{j,\ell}}z_{t,a}
\tag{3.12}
\]

is an integral extended formulation after projection: the
\(z\)-polytope is the Birkhoff polytope.  Global identification of an
entire target set as one capacity resource is where integrality can
fail.

## 4. The first joint Hall cut at depth one

Fix one top and three separately assigned families

\[
 \mathcal R\subseteq\binom U{m-1},\qquad
 \mathcal X\subseteq\binom U m,\qquad
 \mathcal Y\subseteq\binom U{m+1},
\tag{4.1}
\]

with

\[
 |\mathcal R|=|\mathcal Y|=b\le|\mathcal X|.
\tag{4.2}
\]

For \(A\subseteq\mathcal X\), let \(r_-(A)\) be the maximum number of
members of \(A\) which can be matched to distinct members of
\(\mathcal R\) through \(R\subset X\).  Define \(r_+(A)\) analogously
through \(X\subset Y\), \(Y\in\mathcal Y\).

### Theorem 4.1 (common-support flow theorem)

There is a size-\(b\) middle support carrying both a lower and an upper
matching if and only if

\[
 \boxed{
 r_-(A)+r_+(\mathcal X\setminus A)\ge b
 \quad\hbox{for every }A\subseteq\mathcal X.}
\tag{4.3}
\]

#### Proof

Use the node-capacitated network

\[
 s\longrightarrow\mathcal R\longrightarrow\mathcal X
 \longrightarrow\mathcal Y\longrightarrow t,
\tag{4.4}
\]

with containment arcs and unit capacity on every displayed vertex.
An integral flow of value \(b\) is exactly \(b\) vertex-disjoint paths
\(R-X-Y\), and its middle vertices form the required support.
Conversely, concatenate the two matchings through each used middle
vertex.

Max-flow integrality gives an integral optimum.  Eliminating the two
outside layers from the min-cut formula is the standard intersection
formula for the two transversal matroids on \(\mathcal X\):

\[
 \max|I|
 =\min_{A\subseteq\mathcal X}
 \bigl(r_-(A)+r_+(\mathcal X\setminus A)\bigr).
\tag{4.5}
\]

This proves (4.3). \(\square\)

Separate Hall says only

\[
 r_-(\mathcal X)=r_+(\mathcal X)=b.
\tag{4.6}
\]

These are endpoint cases and do not imply (4.3).

### Theorem 4.2 (physical one-unit failure at the actual quota)

For all sufficiently large \(m\), \(b_1=L-1\), and for every top
\(U\) and core \(Q\) there are:

* a literal core-safe tight middle path
  \(\mathcal X=\{X_1,\ldots,X_L\}\);
* \(L-1\) distinct core-compatible lower targets; and
* \(L-1\) distinct core-compatible upper targets

such that both separate containment matchings exist, but their maximum
common support has size \(L-2\).

#### Proof

The lower bound (0.4) gives

\[
 {N_1\over N}={m\over m+1}{W\over N}\ge L+\Omega(H),
\tag{4.7}
\]

so the cap in (1.7) gives \(b_1=L-1\).

Take any tail order and put

\[
 X_i=U\setminus\{c_i,\ldots,c_{i+H-1}\},
 \qquad1\le i\le L.
\tag{4.8}
\]

Two members have Johnson distance one exactly when their indices differ
by one.  Choose

\[
 a_i\in X_i\setminus Q
\tag{4.9}
\]

different from the at most two coordinates
\(X_i\setminus X_{i\pm1}\), and set

\[
                         R_i=X_i\setminus\{a_i\}.
\tag{4.10}
\]

Since \(|X_i\setminus Q|=m-2H>2\),
this is possible.  Containment and equal-size distance give

\[
                         R_i\subseteq X_j
 \quad\Longleftrightarrow\quad i=j.
\tag{4.11}
\]

Likewise choose

\[
 e_i\in U\setminus X_i
\tag{4.12}
\]

away from the at most two coordinates \(X_{i\pm1}\setminus X_i\), and
put

\[
                         Y_i=X_i\cup\{e_i\}.
\tag{4.13}
\]

This is possible because \(H>2\), and

\[
                         X_j\subseteq Y_i
 \quad\Longleftrightarrow\quad i=j.
\tag{4.14}
\]

Now take

\[
 \mathcal R=\{R_1,\ldots,R_{L-1}\},\qquad
 \mathcal Y=\{Y_2,\ldots,Y_L\}.
\tag{4.15}
\]

They separately match to
\(\{X_1,\ldots,X_{L-1}\}\) and
\(\{X_2,\ldots,X_L\}\).  A common support of size \(L-1\) would have
to equal both sets, which is impossible.  The support
\(\{X_2,\ldots,X_{L-1}\}\) has value \(L-2\), so this is the maximum.
Equivalently, with \(A=\{X_2,\ldots,X_L\}\),

\[
 r_-(A)+r_+(\mathcal X\setminus A)
 =(L-2)+0<L-1.
\tag{4.16}
\]

\(\square\)

This is a counterexample to postprocessing arbitrary separate Hall
outputs, not to a fresh joint choice.

## 5. A literal physical odd-set obstruction

The local order polytope from Section 3 is integral.  The global
target--configuration matrix is not.

### Theorem 5.1 (determinant two on three distinct tops)

For \(m\ge4H\), the unrestricted literal core-safe path catalogue
contains three configurations on distinct top roots and three middle
targets whose incidence matrix is

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix}.
\tag{5.1}
\]

#### Proof

Choose pairwise disjoint sets

\[
 |C|=m-H,\qquad |A_1|=|A_2|=|A_3|=H,
\tag{5.2}
\]

and put, cyclically,

\[
 U_1=C\cup A_1\cup A_2,\quad
 U_2=C\cup A_2\cup A_3,\quad
 U_3=C\cup A_3\cup A_1.
\tag{5.3}
\]

Choose a \(2H\)-core inside \(C\) for each top.  Since the middle
subword has length \(m-2H\ge2H\), choose:

* on \(U_1\), a path containing deletion windows \(A_1,A_2\);
* on \(U_2\), a path containing \(A_2,A_3\);
* on \(U_3\), a path containing \(A_3,A_1\).

On target rows

\[
                         C\cup A_1,\quad C\cup A_2,\quad C\cup A_3,
\tag{5.4}
\]

the incidence matrix is (5.1), up to permuting rows or columns.
\(\square\)

The determinant has absolute value \(2\).  If the three configuration
variables are \(y_1,y_2,y_3\), no protected target belongs to all three
configurations.  Indeed, such a target would be contained in

\[
 U_1\cap U_2\cap U_3=C,
\]

but every protected target has rank at least \(m-H+1>|C|\); the three
root selectors are also distinct.  Hence \(y_1=y_2=y_3=1/2\) is
feasible for every row of the full fractional capacity system, and
target capacities imply only

\[
                         y_1+y_2+y_3\le {3\over2},
\tag{5.5}
\]

whereas every integral target-simple selection obeys the odd-clique cut

\[
                         y_1+y_2+y_3\le1.
\tag{5.6}
\]

This proves a precise joint odd-set obstruction.  It is not a global
counterexample: each top has many alternative path configurations.

## 6. The exact global configuration gate

Return to the fixed good cores \(\mathbf Q=(Q_U)_U\), and fix the nested
phase sets \(A_q\) from (2.1).  Define
\(\mathcal K_{\mathbf Q}\) as follows.

Its vertices are:

* one root selector for every top;
* one typed vertex for every middle target; and
* typed lower and upper copies of every protected signed target.

For each top \(U\) and every order of \(S_U\), add the edge containing
its root selector, all \(L\) middle targets, and, for every
\(1\le q<H\), both signed traces of the phases in \(A_q\).
Parallel labelled edges are retained.  Put

\[
 D=s!,\qquad
 k=L+2\sum_{q=1}^{H-1}b_q.
\tag{6.1}
\]

For a choice of one edge \(e_U\) in every top fibre, put

\[
 \lambda_v=|\{U:v\in e_U\}|,
 \qquad
 K(e)=\sum_{v:\lambda_v>0}(\lambda_v-1).
\tag{6.1a}
\]

Root-selector vertices are not included in this sum.

### Theorem 6.0 (exact full-root collision ledger)

For every one-configuration-per-top choice, the number of unrepresented
protected targets is exactly

\[
                         \Delta+K(e),
\tag{6.1b}
\]

where

\[
 \Delta=(W-LN)
       +2\sum_{q=1}^{H-1}(N_q-b_qN)
       =O(H^{3/2}N)=o(W).
\tag{6.1c}
\]

Consequently, if

\[
 \boxed{
 K^*(\mathcal K_{\mathbf Q})
 :=\min_{e_U\in\mathcal K_{\mathbf Q}(U)}K(e)=o(W),}
\tag{6.1d}
\]

then the selected literal paths, followed by the missing masks and the
audited boundary/exterior repairs, give one Boolean-OR word of length
\(W+o(W)\).

#### Proof

The protected target universe has size

\[
 B=W+2\sum_{q=1}^{H-1}N_q.
\tag{6.1e}
\]

The core-safe mask-disjointness theorem ensures that no configuration
edge repeats a protected target.  There are therefore exactly \(kN\)
target occurrences.  Since

\[
 \sum_v\lambda_v
 =|\{v:\lambda_v>0\}|+K(e),
\tag{6.1f}
\]

the number of holes is

\[
 B-|\{v:\lambda_v>0\}|=B-kN+K(e)=\Delta+K(e).
\tag{6.1g}
\]

The delayed-atom compiler contributes \(LN\) state symbols and at most
\(2HN\) bridge-one collar symbols.  Appending the holes and the \(2N\)
boundary-rank masks gives length at most

\[
 LN+2HN+\Delta+K(e)+2N.
\tag{6.1h}
\]

Here

\[
 LN+\Delta
 =W+2\sum_{q=1}^{H-1}(N_q-b_qN)=W+o(W),
\tag{6.1i}
\]

while \(HN=o(W)\) and \(N=o(W)\).  The delayed-atom compilation and
economical product-SCD exterior are precisely the already-audited
compiler inputs in
MATH_AUDIT_COMMON_CORE_TIGHT_PATH_FUSION_SUFFICES_20260726.md,
Sections 2 and 4; this theorem proves the new owner/target ledger, not
those compiler lemmas.  Thus (6.1d) proves the assertion. \(\square\)

Condition (6.1d), rather than target-disjoint matching, is the exact
weakest condition furnished by this one-path-per-top plus
append-the-holes ledger.  The following matching condition is a clean
stronger route.

### Theorem 6.1 (fractional value and quantitative integral implication)

The uniform assignment \(x_e=1/D\) is a fractional matching of total
value \(N\), so

\[
                         \nu^*(\mathcal K_{\mathbf Q})=N.
\tag{6.2}
\]

Moreover,

\[
                         k=\Theta(m^{3/2}).
\tag{6.3}
\]

If a matching has size \(N-t\), the number of unowned protected targets
is exactly

\[
 \Delta+kt,
\tag{6.4}
\]

where

\[
 \Delta=(W-LN)
       +2\sum_{q=1}^{H-1}(N_q-b_qN)
       =O(H^{3/2}N)=o(W).
\tag{6.5}
\]

Consequently (0.7) implies one literal Boolean-OR word of length
\(W+o(W)\), after the already-audited boundary and exterior repairs.

#### Proof

The fractional assertion is Theorem 2.1 with root selectors added.
Root capacity bounds the total fractional value by \(N\), proving
(6.2).

Since \(b_q\le N_q/N\),

\[
 \sum_{q=1}^{H-1}b_q
 \le {1\over N}\sum_{q=1}^{H-1}N_q
 =O(m^{3/2}),
\tag{6.6}
\]

using the standard Gaussian bound
\(N_q/W\le\exp(-q^2/(m+H))\) and \(W/N=O(m)\).
For the reverse bound, if \(1\le q\le\lfloor\sqrt m\rfloor\), then

\[
 {N_q\over W}
 =\prod_{i=1}^q {m-i+1\over m+i}\ge c
\tag{6.6a}
\]

for an absolute \(c>0\), because the logarithm of this product is
bounded below by \(-C\sum_{i\le q}i/m=-O(1)\).  Also \(W/N=\Theta(m)\)
and \(L=\Theta(m)\).  Hence \(b_q\ge c'm\) on
\(\Theta(\sqrt m)\) depths.  This proves (6.3).

The protected target set has size

\[
 B=W+2\sum_{q=1}^{H-1}N_q.
\tag{6.7}
\]

A matching of size \(N-t\) owns exactly \(k(N-t)\) distinct protected
targets.  Since \(B-kN=\Delta\), its hole count is (6.4).

Compile its \(N-t\) paths.  Their state count is \(L(N-t)\), and their
bridge-one collar cost is \(2H(N-t)\).  Append all protected holes and
the \(2N\) boundary-rank masks.  The resulting length is at most

\[
 L(N-t)+2H(N-t)+\Delta+kt+2N.
\tag{6.8}
\]

Using \(k=L+2\sum b_q\), this is

\[
 LN+2H(N-t)+\Delta
 +2t\sum_{q=1}^{H-1}b_q+2N.
\tag{6.9}
\]

Now

\[
 LN+\Delta
 =W+2\sum_{q=1}^{H-1}(N_q-b_qN)
 =W+o(W).
\tag{6.10}
\]

Also \(HN=o(W)\), \(N=o(W)\), and, if
\(t=o(N/\sqrt m)\),

\[
 t\sum_qb_q=o(Nm)=o(W).
\tag{6.11}
\]

This proves the literal \(W+o(W)\) bound. \(\square\)

Thus the scalar and fractional parts of the fixed-core fusion problem
are complete.  The exact residual condition for this ledger is (6.1d);
the integral matching estimate (0.7) is a stronger sufficient route.

For completeness, let \(x^0_e=1/D\) on every labelled edge, and let
\(\mathsf P\) be the matching polytope of
\(\mathcal K_{\mathbf Q}\).

### Theorem 6.2 (exact joint weighted criterion)

For \(0\le\varepsilon<1\), the following are equivalent:

\[
                         (1-\varepsilon)x^0\in\mathsf P,
\tag{6.12}
\]

and, for every nonnegative edge weight \(y\),

\[
 \boxed{
 \nu_y\ge(1-\varepsilon)
       {1\over D}\sum_e y_e,}
\tag{6.13}
\]

where \(\nu_y\) is the maximum weight of a matching.

#### Proof

Membership in the matching polytope expresses the left side of (6.12)
as a convex combination of matching incidence vectors.  Averaging
\(y\) shows that one matching has weight at least the right side of
(6.13).

Conversely, if (6.12) fails, separate \((1-\varepsilon)x^0\) from the
closed matching polytope.  Its down-monotonicity permits a nonnegative
separating normal: replace every negative coefficient by zero and, for
each candidate matching vector, set those coordinates to zero, which
remains in the polytope.  The resulting nonnegative weight violates
(6.13). \(\square\)

If (6.12) holds with
\(\varepsilon=o(m^{-1/2})\), some matching in its convex decomposition
has size \(N-o(N/\sqrt m)\), and Theorem 6.1 applies.  The ordinary
target-capacity inequalities prove only that \(x^0\) lies in the
fractional matching relaxation.  The triangle (5.1) displays one class
of additional integral cuts in the unrestricted core-safe catalogue;
it does not assert that the same three-edge minor occurs for every
particular fixed good-core assignment.

## 7. Precise proved and unproved boundary

Proved here:

1. the source atlas's counting, Hall, path, and error estimates;
2. simultaneous fixed-core fractional feasibility on literal tagged
   paths;
3. the exact signature-Hall and diagonal-shell criteria for one local
   tail order;
4. the complete depth-one common-support cut and a physical one-unit
   failure of separate Hall at the actual quota;
5. a literal determinant-\(2\) odd triangle on distinct roots; and
6. the exact collision ledger (6.1d), and the stronger quantitative
   implication from (0.7) to one \(W+o(W)\) word.

Not proved:

1. the full-root collision estimate \(K^*(\mathcal K_{\mathbf Q})=o(W)\);
2. the stronger near-perfect integral matching (0.7), or a theorem
   controlling its nonlocal integral cuts to the required scale;
3. exact completion to one full SCD; or
4. coefficient one.

The exact minimum surviving lemma for this audited compiler ledger is:

> For the fixed good cores, choose one literal all-depth path
> configuration in every top fibre so that the aggregate physical
> target-collision excess is \(o(W)\).

A stronger sufficient lemma is the joint weighted criterion (6.13)
with \(\varepsilon=o(m^{-1/2})\); it yields (0.7), and
\(k=\Theta(m^{3/2})\) shows that this is the exact leave rate for the
matching-and-discard subroute.  A failure need only be a joint,
nonlocal integrality obstruction; the evidence here does not classify
all such failures as odd-set cuts.  Separate-rank Hall, one-set Farkas
weights, and local tail-order integrality are already closed.
