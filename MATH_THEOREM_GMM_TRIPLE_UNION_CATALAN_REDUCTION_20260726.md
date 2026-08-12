# GMM lower-rainbow cycles: an exact Catalan reduction of the triple-union defect

Date: 2026-07-26

Method: pure mathematics and local-source audit only; no search or finite
computation.

## 0. Outcome

Assume \(m\ge2\).  Let

\[
 R_0,X_0,R_1,X_1,\ldots,R_{N-1},X_{N-1},R_0
\]

be a saturating cycle between ranks \(m-1\) and \(m\), and put

\[
 T_i=R_{i-1}\cup R_i\cup R_{i+1},\qquad
 \delta=N-|\{T_i:i\in\mathbb Z_N\}|.                 \tag{0.1}
\]

The requested assertion is \(\delta=o(W)\), with central normalization

\[
 W_m^{\rm e}=\binom{2m}{m}\quad\hbox{or}\quad
 W_m^{\rm o}=\binom{2m+1}{m}.                       \tag{0.1a}
\]

It is **not proved or refuted for the existential cycle in
Gregor--Mička--Mütze Corollary 2**.  That corollary does not select a
successor rule.

There is, however, an exact construction-specific reduction for the
recursive `sat_2` realization in the local GMM implementation.  Let

\[
 B_r=\binom{2r+1}{r},
\]

and let \(\beta_r\) be the defect (0.1) of the particular Middle Levels
Hamilton cycle used at the recursive base \((2r+1,r)\).  For the even
ground call \((2m,m-1)\),

\[
 \boxed{
 \left|\delta_{2m,m-1}
 -\sum_{r=1}^{m-1}\operatorname{Cat}_{m-r-1}\beta_r\right|
 \le 4\left(\sum_{s=0}^{m-1}\operatorname{Cat}_s-1\right).} \tag{0.2}
\]

For the odd ground call \((2m+1,m-1)\),

\[
 \boxed{
 \left|\delta_{2m+1,m-1}
 -\sum_{r=1}^{m-1}\operatorname{Cat}_{m-r}\beta_r\right|
 \le 4\left(\sum_{s=1}^{m}\operatorname{Cat}_s-1\right).}   \tag{0.3}
\]

Both error terms are \(O(W/m)\).  Thus the Pascal connectors cannot be a
linear obstruction; all possible linear defect lies in the growing Middle
Levels base cycles.  In particular,

\[
 \boxed{\beta_r=o(B_r)\quad\Longrightarrow\quad\delta=o(W)}. \tag{0.4}
\]

A quantitatively optimal sufficient base theorem is

\[
                         \beta_r=O(\operatorname{Cat}_r).    \tag{0.5}
\]

Indeed, (0.5) gives \(\delta=O(W/m)\).

The canonical centered PBBS factor already has the optimal defect

\[
 \beta_r^{\rm PBBS}
 =B_r-\binom{2r+1}{r+2}
 ={2B_r\over r+2}<4\operatorname{Cat}_r,             \tag{0.6}
\]

but it is a 2-factor, not a Hamilton cycle.  A presently isolated explicit
gate for this route is an \(O(\operatorname{Cat}_r)\)-edit
Hamiltonization of that factor through legal Middle Levels switches.  The
available PBBS connector notes explicitly leave this atlas unproved.

In the opposite direction, the standard \(0/1\)-lexical Middle Levels
factor has the exact defect

\[
 \beta_r^{01}=B_r\,{r+1\over2(2r-1)}
 =\left({1\over4}+O(r^{-1})\right)B_r.              \tag{0.6a}
\]

The published \(O(\operatorname{Cat}_r)\)-hexagon Hamiltonization changes
only \(O(\operatorname{Cat}_r)\) triple occurrences.  Hence every output
of that merge scheme still has

\[
                         \beta_r=\left({1\over4}-o(1)\right)B_r. \tag{0.6b}
\]

Consequently the recursive construction with this standard lexical base
has a linear root defect: at least
\((1/8-o(1))W_m^{\rm e}\) for the even root and
\((1/16-o(1))W_m^{\rm o}\) for the odd root.  Thus that concrete base
choice is refuted.

For contrast, the explicit GJM lexical path rule, normalized by
\(W_m^{\rm lex}=\binom{2m+1}{m}\), has

\[
 \delta\ge\left({1\over4}-o(1)\right)W_m^{\rm lex}. \tag{0.7}
\]

Thus the lexical realization is refuted, but (0.7) cannot be transferred
to an arbitrary GMM/Mütze--Su cycle.

## 1. Exact turn form

Fix a simple saturating incidence cycle between ranks \(k\) and \(k+1\):

\[
 R_0,X_0,R_1,X_1,\ldots,R_{N-1},X_{N-1},R_0,
 \qquad R_i\subset X_i\supset R_{i+1}.              \tag{1.1}
\]

Because the two lower facets of \(X_i\) are distinct,

\[
 X_i=R_i\cup R_{i+1}.                               \tag{1.2}
\]

Write

\[
 R_{i+1}=R_i-\alpha_i+\beta_i,
 \qquad \alpha_i\in R_i,\quad\beta_i\notin R_i.     \tag{1.3}
\]

The two exterior labels \(\alpha_{i-1}\) and \(\beta_i\) at \(R_i\) are
distinct, since otherwise \(X_{i-1}=X_i\).  Therefore

\[
 \boxed{
 T_i=X_{i-1}\cup X_i
 =R_{i-1}\cup R_i\cup R_{i+1}
 =R_i\cup\{\alpha_{i-1},\beta_i\}.}                \tag{1.4}
\]

In particular every \(T_i\) has rank \(k+2\).  The defect in (0.1) is
exactly the collision excess of this multiset.

We shall repeatedly use the following elementary fact.

### Lemma 1.1 (replacement Lipschitz bound)

Replacing \(t\) occurrences in a multiset of fixed cardinality changes
its collision excess by at most \(t\).

#### Proof

One replacement changes the support size by at most one.  The cardinality
of the multiset is unchanged.  Iterate. \(\square\)

## 2. The recursive cycle and its four-position splice

This section concerns one concrete realization, not the bare existential
quantifier in GMM Corollary 2.

Let \(C_{n,k}\) be the lower rank-\(k\) cyclic order in the recursive
`sat_2` construction.  At every nonbase state \(n>2k+1\), let \(z\) be
the final coordinate.  The construction takes:

1. \(C_{n-1,k}\) with \(z\) absent, deletes its distinguished edge, and
   traverses the resulting path in reverse;
2. \(C_{n-1,k-1}\) with \(z\) adjoined to every vertex, deletes its
   distinguished edge, and traverses the resulting path forward;
3. joins the two pairs of path endpoints crosswise.

This is a 2-sum of two cycles along their distinguished edges.  The
recursion stops at \(k=0\) or at a Middle Levels state \(n=2k+1\).
Every coordinate conjugation or reversal used to install a Middle Levels
base leaves its defect \(\beta_r\) unchanged.

### Theorem 2.1 (exact defect recurrence)

If \(n>2k+1\), then

\[
 \boxed{
 |\delta_{n,k}-\delta_{n-1,k}-\delta_{n-1,k-1}|\le4.} \tag{2.1}
\]

A \(k=0\) child is assigned defect zero.

#### Proof

Deleting one edge from each child and adding the two cross edges changes
the unordered predecessor/current/successor triple only at the four cut
endpoints.  Reversing the first path has no effect on the union of such a
triple.

Before those four endpoint values are replaced, every inherited target
from the first child omits \(z\), whereas every inherited target from the
second child contains \(z\).  Hence the two inherited supports are
disjoint and their collision excesses add exactly.  Lemma 1.1, applied to
the at most four changed endpoint occurrences, gives (2.1). \(\square\)

If one child has \(k=0\), it is a singleton rather than a cycle with a
distinguished edge.  In that boundary case, first augment the nontrivial
child multiset by one artificial rank-\((k+2)\) target containing \(z\).
This artificial occurrence is disjoint from the nontrivial inherited
support.  Passing to the parent changes at most the two nontrivial cut
endpoints and the singleton occurrence.  The error is therefore at most
three, and in particular still bounded by four as asserted in (2.1).

Two points in this proof are essential.  The supports are separated only
for the inherited entries; new endpoint targets may collide across the
two children, and their entire effect is included in the four-unit error.
Also, this is a support estimate, not an assertion that the new endpoint
targets are distinct.

## 3. Exact Catalan leaf census

Put

\[
 h=n-2k-1.                                           \tag{3.1}
\]

At a recursive split the child \((n-1,k)\) changes \(h\) to \(h-1\),
while \((n-1,k-1)\) changes it to \(h+1\).  A Middle Levels leaf is the
first hit of \(h=0\), and a \(k=0\) leaf is the other absorbing boundary.

### Lemma 3.1 (even root)

In the recursion tree rooted at \((2m,m-1)\):

* the Middle Levels leaf \((2r+1,r)\) occurs
  \(\operatorname{Cat}_{m-r-1}\) times, \(1\le r\le m-1\);
* \(k=0\) occurs \(\operatorname{Cat}_{m-1}\) times;
* the total number of leaves is

  \[
  L_m^{\rm e}=\sum_{s=0}^{m-1}\operatorname{Cat}_s. \tag{3.2}
  \]

#### Proof

The initial height is one.  To finish at \((2r+1,r)\), a branch uses
\(u=m-r-1\) height-increasing steps and \(u+1\) height-decreasing steps,
staying positive until its last step.  The first-passage ballot number is
\(\operatorname{Cat}_u\).  The same ballot decomposition at the \(k=0\)
boundary gives \(\operatorname{Cat}_{m-1}\).  Summing gives (3.2).
\(\square\)

### Lemma 3.2 (odd root)

In the recursion tree rooted at \((2m+1,m-1)\):

* the Middle Levels leaf \((2r+1,r)\) occurs
  \(\operatorname{Cat}_{m-r}\) times, \(1\le r\le m-1\);
* \(k=0\) occurs \(\operatorname{Cat}_{m}\) times;
* the total number of leaves is

  \[
  L_m^{\rm o}=\sum_{s=1}^{m}\operatorname{Cat}_s.   \tag{3.3}
  \]

#### Proof

Now the initial height is two.  If \(u=m-r-1\), first passage to zero uses
\(u\) up-steps and \(u+2\) down-steps.  The ballot number is

\[
 {2\over 2u+2}\binom{2u+2}{u}
 ={1\over u+2}\binom{2u+2}{u+1}
 =\operatorname{Cat}_{u+1}.
\]

The \(k=0\) boundary gives \(\operatorname{Cat}_m\), and summing gives
(3.3). \(\square\)

Every nonleaf has exactly two children.  Therefore a recursion tree with
\(L\) leaves has \(L-1\) splice nodes.

## 4. Catalan-weighted base reduction

At a Middle Levels base put

\[
 \beta_r:=\delta_{2r+1,r},
 \qquad B_r:=\binom{2r+1}{r}.                       \tag{4.1}
\]

Iterating Theorem 2.1 over the two recursion trees and applying Lemmas 3.1
and 3.2 proves (0.2) and (0.3).  For completeness, the relevant sizes are

\[
 \operatorname{Cat}_{m-1}
 ={1\over2(2m-1)}\binom{2m}{m},                    \tag{4.2}
\]

and

\[
 \operatorname{Cat}_m
 ={1\over2m+1}\binom{2m+1}{m}.                     \tag{4.3}
\]

Since a terminal segment of the Catalan sequence dominates its preceding
sum geometrically, (4.2)--(4.3) show that both splice errors are \(O(W/m)\).

The leaf vertices partition the root lower vertices.  Consequently the
exact occurrence identities are

\[
 \sum_{r=1}^{m-1}\operatorname{Cat}_{m-r-1}B_r
 +\operatorname{Cat}_{m-1}
 =\binom{2m}{m-1},                                  \tag{4.4}
\]

and

\[
 \sum_{r=1}^{m-1}\operatorname{Cat}_{m-r}B_r
 +\operatorname{Cat}_{m}
 =\binom{2m+1}{m-1}.                                \tag{4.5}
\]

### Corollary 4.1 (little-oh transfer)

If \(\beta_r=o(B_r)\), then the recursive cycles at both roots satisfy
\(\delta=o(W)\).

#### Proof

Given \(\varepsilon>0\), choose \(r_0\) so that
\(\beta_r\le\varepsilon B_r\) for \(r\ge r_0\).  Equations
(4.4)--(4.5) bound the contribution of these leaves by
\(\varepsilon W\).  Each of the finitely many \(r<r_0\) contributes
\(O(W/m)\), as follows from the fixed-offset Catalan ratios.  The splice
error is also \(O(W/m)\).  First let \(m\to\infty\), then
\(\varepsilon\to0\). \(\square\)

### Corollary 4.2 (optimal Catalan-scale transfer)

If \(\beta_r\le K\operatorname{Cat}_r\) for all \(r\), then

\[
 \delta_{2m,m-1}=O_K(W/m),
 \qquad
 \delta_{2m+1,m-1}=O_K(W/m).                       \tag{4.6}
\]

#### Proof

The two weighted sums are bounded using the Catalan convolutions

\[
 \sum_{r=1}^{m-1}\operatorname{Cat}_{m-r-1}
                         \operatorname{Cat}_r
 =\operatorname{Cat}_m-\operatorname{Cat}_{m-1},   \tag{4.7}
\]

and

\[
 \sum_{r=1}^{m-1}\operatorname{Cat}_{m-r}
                         \operatorname{Cat}_r
 =\operatorname{Cat}_{m+1}-2\operatorname{Cat}_m. \tag{4.8}
\]

Both right sides are \(O(\operatorname{Cat}_m)=O(W/m)\).  Add the splice
errors. \(\square\)

### Corollary 4.3 (where a linear defect must live)

For the even root,

\[
 \delta_{2m,m-1}\ge\beta_{m-1}-O(W/m).             \tag{4.9}
\]

For the odd root the same inequality holds.  Since
\(B_{m-1}=W/2\) in the even case and

\[
 {B_{m-1}\over\binom{2m+1}{m}}
 ={m+1\over2(2m+1)}
\]

in the odd case, a positive-density defect in the top Middle Levels base
forces a positive-density defect at the root.  Conversely, connectors or
any fixed finite set of base sizes contribute only \(O(W/m)\).

Therefore, for a coherently chosen family of recursive bases,
\(\beta_r=o(B_r)\) is not merely sufficient: it is the exact scalar gate
for \(\delta=o(W)\).  Necessity follows from the top leaf \(r=m-1\), and
sufficiency is Corollary 4.1.

## 5. The optimal PBBS base factor and the exact missing connector

On \([2r+1]\), every Middle Levels Hamilton cycle projects to a Hamilton
cycle on the \(B_r\) rank-\(r\) sets whose edge unions exhaust the
rank-\((r+1)\) sets.  Its triple targets have rank \(r+2\).  Hence every
such cycle satisfies the unavoidable lower bound

\[
 \beta_r\ge B_r-\binom{2r+1}{r+2}
 ={2B_r\over r+2}.                                  \tag{5.1}
\]

The centered PBBS construction gives a Johnson 2-factor \(F_r\) with the
following audited properties:

1. its edge-union colours are all rank-\((r+1)\) sets, exactly once;
2. the complements of its triple targets are the PBBS angle colours;
3. every rank-\((r-1)\) angle colour occurs;
4. \(F_r\) has at most \(\operatorname{Cat}_r\) components.

For completeness, let \(f\) be the PBBS permutation.  The centered edge
indexed by \(X\) is

\[
                         e_X=\{f^{-1}(X),f(X)\},
\]

and has union colour \(X^c\).  At a Johnson owner \(Y\), the two incident
edges are indexed by \(f(Y)\) and \(f^{-1}(Y)\).  Hence the complement of
the triple target at \(Y\) is

\[
 f^{-1}(Y)\cap f(Y)=\chi(Y),                        \tag{5.1a}
\]

the PBBS angle colour.  The complement map is a bijection between
rank-\((r+2)\) and rank-\((r-1)\) targets, so complete angle support proves
that \(F_r\) attains equality in (5.1), giving (0.6).

Moreover, on an \(f\)-orbit of length \(\ell(2r+1)\), the centered
monodromy \(f^{-2}\) has \(\gcd(2,\ell)\) components.  The PBBS homomesy
census gives \(\sum\ell=\operatorname{Cat}_r\), and consequently
\(c(F_r)\le\operatorname{Cat}_r\).

### Lemma 5.1 (edit stability)

Let \(F,F'\) be spanning 2-factors on the same rank-\(r\) owner set.  If
the unordered neighbour pair changes at at most \(s\) owners, then

\[
                         |\beta(F')-\beta(F)|\le s. \tag{5.2}
\]

#### Proof

The triple target centered at an owner depends only on that owner and its
two neighbours.  Hence at most \(s\) occurrence values are replaced, and
Lemma 1.1 applies. \(\square\)

It follows that the following statement would prove (0.5), and therefore
the requested estimate for the entire recursive construction.

### PBBS Middle Levels connector lemma (unproved)

For every \(r\), the centered PBBS factor \(F_r\) can be changed into one
Hamilton cycle by legal alternating switches in the Middle Levels
incidence graph so that:

1. every rank-\((r+1)\) incidence vertex is still used exactly once;
2. the unordered neighbour pair changes at only
   \(O(\operatorname{Cat}_r)\) rank-\(r\) owners.

A sufficient way to obtain this is a physically legal constant-size
connector forest with \(O(\operatorname{Cat}_r)\) switches.  The component
count makes this rate numerically possible, but does not prove the
existence of the switches.  The audited PBBS connector analysis leaves
exactly this topology-identification/connector-atlas statement open.

The scalar minimum hypothesis needed by (0.2) is only
\(\beta_r=o(B_r)\).  The displayed connector lemma is a stronger, explicit
construction which would give the optimal \(O(\operatorname{Cat}_r)\)
bound.

## 6. Exact linear defect of the standard lexical Middle Levels base

Let \(F_{01}\) be the union of the \(0\)- and \(1\)-lexical perfect
matchings between ranks \(r\) and \(r+1\) of \(Q_{2r+1}\).  For a lower
word \(x\), let \(y_0(x),y_1(x)\) be its two upper neighbours and put

\[
                         \Phi(x)=y_0(x)\cup y_1(x).  \tag{6.1}
\]

After suppressing the upper shore, \(\Phi(x)\) is exactly the union of
the predecessor, \(x\), and the successor in the projected Johnson
2-factor.

### Theorem 6.1 (exact lexical target holes)

For \(r\ge3\), the number of rank-\((r+2)\) targets omitted by \(\Phi\)
is

\[
\boxed{
 M_r
 =\binom{2r-1}{r-3}
  -{2\over r-1}\binom{2r-2}{r-3}
 =B_r\,{(r-2)(r-3)\over2(r+2)(2r-1)}.}             \tag{6.2}
\]

Consequently

\[
 \beta_r(F_{01})
 =B_r-\left(\binom{2r+1}{r+2}-M_r\right)
 =B_r\,{r+1\over2(2r-1)}.                          \tag{6.3}
\]

#### Proof

Use the Greene--Kleitman factorization into Dyck valleys.  A target
\(T\in\binom{[2r+1]}{r+2}\) has, for a unique \(b\ge0\), the form

\[
 T=u_0\,1\cdots1\,u_{b+2}\,1\,u_{b+3}\,0\cdots
       0\,u_{2b+3},                                 \tag{6.4}
\]

where the \(2b+4\) Dyck valleys have total semilength \(r-b-1\).
The lexical scan gives the exact fibre formula

\[
 |\Phi^{-1}(T)|
 ={\bf1}_{u_{b+1}=\varnothing}
  +{\bf1}_{u_{b+2}=\varnothing}\qquad(b\ge1),        \tag{6.5}
\]

and, for \(b=0\), the additional term

\[
                         {\bf1}_{u_0=u_3=\varnothing}. \tag{6.6}
\]

Indeed, if the central valley of a lower word is nonempty, write its
right factorization as \(v0w1\).  The two lexical flips perform

\[
                         v0w10\longmapsto v1w11,
\]

which is inverted by the second indicator in (6.5).  If the central
valley is empty and there remains another unmatched zero, the flips
perform

\[
                         0u0\longmapsto1u1,
\]

which is inverted by the first indicator.  The only boundary case is a
chain with one star: \(0(v0w1)\mapsto1v1w1\), giving (6.6).
These three cases exhaust the lexical scan.

Let \(C(z)=\sum_{j\ge0}\operatorname{Cat}_jz^j\).  Ignoring the rescued
boundary targets (6.6), the number with both central valleys nonempty is

\[
\begin{aligned}
 M_r^{\rm raw}
 &=\sum_{b=0}^{r-3}[z^{r-b-1}](C-1)^2C^{2b+2}\\
 &=\sum_{b=0}^{r-3}{b+3\over r}\binom{2r}{r-b-3}
 =\binom{2r-1}{r-3}.                                \tag{6.7}
\end{aligned}
\]

Here \(C-1=zC^2\), the power formula
\([z^a]C^p=p(2a+p)^{-1}\binom{2a+p}{a}\), and a one-line
telescoping were used.  The \(b=0\) rescue has size

\[
 [z^{r-1}](C-1)^2=[z^{r-3}]C^4
 ={2\over r-1}\binom{2r-2}{r-3}.                   \tag{6.8}
\]

Subtracting proves (6.2); elementary binomial ratios give (6.3).
\(\square\)

### Corollary 6.2 (lexical Hamiltonization remains linearly bad)

One factor-alternating \(C_6\) changes at most three lower-centred triple
occurrences.  The published lexical merge tree uses

\[
 s=p_r-1\le\operatorname{Cat}_r-1={B_r\over2r+1}-1
\]

hexagons.  Lemma 1.1 therefore gives

\[
 \beta_r^{\rm Ham}
 \ge B_r\,{r+1\over2(2r-1)}-3\operatorname{Cat}_r
 =\left({1\over4}-o(1)\right)B_r.                  \tag{6.9}
\]

Putting the top base \(r=m-1\) into (0.2)--(0.3), using nonnegativity of
all other base defects and the \(O(W/m)\) splice error, yields

\[
 \delta_{2m,m-1}\ge(1/8-o(1))W_m^{\rm e},\qquad
 \delta_{2m+1,m-1}\ge(1/16-o(1))W_m^{\rm o}.        \tag{6.10}
\]

This refutes the recursive GMM fallback **when its Middle Levels base is
the standard lexical-factor Hamiltonization**.  It does not refute a
different base cycle with \(\beta_r=o(B_r)\).

The local source bundle does not self-containedly prove that the routine
in `mlc_hamcycle.cpp` is edge-for-edge this GMN lexical Hamiltonization.
It identifies the routine as the Mütze--Nummenpalo \(H_n/\sigma\)
algorithm and its local \(\tau\)-move as an alternating hexagon, but the
remaining provenance lemma--that its unflipped base is exactly the
\(0/1\)-lexical factor and its selected \(\tau\)-moves are the compatible
GMN merge tree--is imported rather than proved locally.  Therefore (6.10)
is unconditional for the recursive variant which explicitly chooses the
published lexical base, and conditional on this provenance lemma for that
particular executable routine.

## 7. A genuine linear no-go for the four-level lexical rule

The separate GJM lexical lower forest has an explicit collision injection.
For each word \(y\) of length \(2m-1\) and weight \(m-2\), split \(y=A0B\)
at its first global minimum and form

\[
                         x=A010B,\qquad x'=A001B.    \tag{7.1}
\]

The two lexical flags selected from \(x\) and \(x'\) have the same
two-step union \(A111B\), and distinct \(y\)'s give disjoint collision
pairs.  Hence there are

\[
                         \binom{2m-1}{m-2}          \tag{7.2}
\]

disjoint colliding pairs.  After discarding the labels at the endpoints
of the \(D=2W_m^{\rm lex}/(m+2)\) lexical paths, at least

\[
 \binom{2m-1}{m-2}-2D
 =\left({1\over4}-o(1)\right)W_m^{\rm lex}.         \tag{7.3}
\]

literal predecessor/current/successor collisions remain.

Thus any construction which changes only \(o(W_m^{\rm lex})\) lexical successor
positions retains a linear defect.  This refutes that explicit lexical
route.  It is not a counterexample to the GMM existence theorem or to the
recursive `sat_2` route unless an additional \(o(W_m^{\rm lex})\)-edit comparison with
the lexical forest is proved; no such comparison is available.

## 8. Adversarial audit

The strongest claims above survive the following failure modes.

1. **Corollary 2 is existential.**  The recursive cycle analyzed in
   Sections 2--4 is one optional realization.  It is not canonically
   selected by the published corollary.
2. **Cross-child collisions are not ignored.**  Only inherited supports
   are separated by \(z\).  All new cross-child coincidences are charged
   to the four changed endpoint occurrences in (2.1).
3. **The Catalan reduction is integral.**  It is an exact recursion-tree
   census, not a fractional averaging statement.  Every root lower owner
   belongs to exactly one terminal leaf, as recorded in (4.4)--(4.5).
4. **Small base cases cannot accumulate linearly.**  For each fixed \(r\),
   its Catalan multiplicity is \(O(W/m)\); the same is true of the entire
   splice ledger.
5. **PBBS is not silently called Hamiltonian.**  Formula (0.6) is proved
   for a 2-factor.  Promoting it to a suitable Middle Levels base cycle is
   precisely the unproved connector lemma.
6. **The two lexical obstructions have different scopes.**  Theorem 6.1
   applies to the standard \(0/1\)-lexical Middle Levels factor and its
   \(O(\operatorname{Cat}_r)\)-switch Hamiltonization.  Section 7 applies
   to the separate four-level GJM forest.  Neither applies to every
   Mütze--Su saturating cycle.
7. **The scale is sharp.**  Even a perfect-support Middle Levels base has
   defect \(2B_r/(r+2)=\Theta(\operatorname{Cat}_r)\), because there are
   fewer rank-\((r+2)\) targets than occurrences.  Thus (0.5), rather than
   zero defect, is the correct optimal base target.

## 9. Precise proved/conditional boundary

Unconditionally proved here:

* the four-position splice recurrence (2.1);
* the exact Catalan reductions (0.2)--(0.3);
* the transfer implications (0.4)--(0.5);
* optimal triple support for the centered PBBS 2-factor;
* the exact linear defect (6.2)--(6.3) of the \(0/1\)-lexical Middle
  Levels factor;
* persistence of that defect through the published Catalan-scale
  hexagon Hamiltonization;
* a linear obstruction for the separate four-level lexical path rule.

Not proved:

* \(\beta_r=o(B_r)\) for a nonlexical family of Middle Levels Hamilton
  cycles;
* the PBBS Middle Levels connector lemma;
* the requested triple-union estimate for some unspecified existential
  choice in GMM Corollary 2.

Therefore this route does not yet prove coefficient one.  Its smallest
remaining scalar lemma is \(\beta_r=o(B_r)\) for a chosen growing Middle
Levels base family; its smallest explicit construction lemma is the PBBS
connector statement in Section 5.
