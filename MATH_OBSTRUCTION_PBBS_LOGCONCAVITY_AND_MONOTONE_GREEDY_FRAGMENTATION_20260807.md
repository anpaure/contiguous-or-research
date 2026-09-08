# Log-concavity does not imply reflected partition order, and largest-step PBBS routing fails at depth five

**Date:** 2026-08-07

**Status:** two unconditional exact scope obstructions and one exact
curvature target.  A strictly positive, strictly log-concave integer
profile with integer mean can fail the reflected all-price inequality.
The natural largest-available-step DAG flow also fails on the actual
terminal PBBS depth-five coefficient, although that coefficient is known
to admit a fractional fragmentation.  Thus a successful Catalan kernel
must use more than log-concavity and more than monotone size order; it must
retain residue or first-return state.

## 1. The reflected partition functional

Let

\[
 a_0,a_1,\ldots,a_N>0,
 \qquad
 \sum_{j=0}^{N}(j-D)a_j=0
\tag{1.1}
\]

for an integer \(D\).  Its reflected signed coefficient is

\[
 \mu_L=\mathbf1_{L\le D}a_{D-L}-a_{D+L},
 \qquad L\ge1,
\tag{1.2}
\]

where coefficients outside the support are zero.  Thus

\[
 \sum_LL\mu_L=0.
\tag{1.3}
\]

The desired partition order is

\[
 \sum_L\mu_L\psi(L)\ge0
\tag{1.4}
\]

for every nonnegative nondecreasing subadditive covering price \(\psi\).
For the terminal PBBS profile, \(a_j=\mathcal A_j\) in
`MATH_THEOREM_PBBS_CENTERED_BALLOT_PROFILE_AND_EXACT_FRAGMENTATION_GATE_20260807.md`.

## 2. Strict log-concavity and exact centering are insufficient

### Proposition 2.1 (five-point counterexample)

Take

\[
 \boxed{(a_0,a_1,a_2,a_3,a_4)=(2,4,6,6,1),
 \qquad D=2.}
\tag{2.1}
\]

This profile is strictly positive and strictly log-concave:

\[
 4^2>2\cdot6,qquad
 6^2>4\cdot6,qquad
 6^2>6\cdot1.
\tag{2.2}
\]

Its mean is exactly two, because

\[
 \sum_ja_j=19,qquad
 \sum_jja_j=38.
\tag{2.3}
\]

Nevertheless, (1.2) is

\[
 (\mu_1,\mu_2)=(-2,1).
\tag{2.4}
\]

For the valid one-denomination closed price

\[
 \psi(L)=\left\lceil{L\over2}\right\rceil,
\tag{2.5}
\]

one gets

\[
 \boxed{
 \sum_L\mu_L\psi(L)=-2+1=-1<0.}
\tag{2.6}
\]

Equivalently, the reflected primal has one size-two supply piece and two
size-one jobs.  Their volumes agree, but one indivisible size-two piece
cannot be used as two size-one pieces.

Thus none of the following generic data implies reflected partition
order:

1. positivity of the centered profile;
2. exact integer mean;
3. strict log-concavity; or
4. even a single reflection sign change, if its orientation is not
   controlled.

No PBBS coefficient is being contradicted here.  The example proves that
the strict log-concavity theorem for \(\mathcal A\) needs genuinely
Catalan extra structure.

Even abstract palindromic-gradient structure does not rescue the claim.
The profile (2.1) is the lower-half gradient

\[
 a_j=q_{4-j}-q_{3-j}
 \quad(q_{-1}:=0)
\tag{2.6a}
\]

of the strictly log-concave palindromic row

\[
 (q_0,\ldots,q_8)=(1,7,13,17,19,17,13,7,1).
\tag{2.6b}
\]

Indeed its lower-half successive differences are
\((1,6,6,4,2)\), which reverse to (2.1), and

\[
 7^2>1\cdot13,quad
 13^2>7\cdot17,quad
 17^2>13\cdot19,quad
 19^2>17^2.
\tag{2.6c}
\]

Thus the extra input cannot be merely “gradient of a symmetric
log-concave row.”  It must exploit the specific factor
\((1+X)^{2r-2}(1+\rho X+X^2)\), or an equivalent ballot first-return
identity.

### Proposition 2.2 (localization is applicable, but its extremal family already fails)

The discrete localization theorem of Marsiglietti and Melbourne applies
to the mean equality without losing that equality, but it does not help
the desired inequality.  In fact a truncated geometric extreme already
fails it.

Fix a finite support interval \(I\) and let \(K\) be the convex hull of
the log-concave probability laws on \(I\) satisfying

\[
 \mathbb E[J]\ge D.
\tag{2.7}
\]

The extreme-point theorem for a half-space slice says that every extreme
point of \(K\) is log-affine on a subinterval:

\[
 p_j=cq^j\mathbf1_{a\le j\le b}.
\tag{2.8}
\]

See [Marsiglietti--Melbourne, Corollary 2.13 and the preceding
extreme-point theorem](https://arxiv.org/abs/2004.12005).

If a log-concave law \(p\in K\) has \(\mathbb E_pJ=D\), decompose it into
extreme points of \(K\).  Every component has mean at least \(D\), while
their weighted mean is exactly \(D\).  Hence every component with
positive weight also has mean exactly \(D\).  Therefore, for each fixed
linear reflected objective, localization really does reduce a generic
mean-\(D\) log-concave assertion to mean-\(D\) truncated geometrics.  No
second equality constraint is being smuggled into the theorem; it is the
supporting-face argument for (2.7).

That reduced assertion is false.  Let \(q\in(1,2)\) be the unique root of

\[
 q^3-q-2=0
\tag{2.9}
\]

and take the log-affine profile

\[
 \boxed{
 (a_0,a_1,a_2,a_3)=(1,q,q^2,q^3),
 \qquad D=2.}
\tag{2.10}
\]

Its mean is exactly two, since

\[
 \sum_{j=0}^{3}(j-2)q^j=q^3-q-2=0.
\tag{2.11}
\]

Its reflected coefficient is again

\[
 \mu_1=q-q^3=-2,
 \qquad
 \mu_2=1.
\tag{2.12}
\]

Consequently the ceiling price (2.5) gives

\[
 \boxed{\sum_L\mu_L\psi(L)=-1.}
\tag{2.13}
\]

Thus discrete localization is valid here and produces a sharp **no-go**:
no proof based only on positivity, log-concavity, normalization, and mean
\(D\) can establish reflected partition order.  Any successful use of
extremal reduction would have to preserve additional PBBS structure such
as the palindromic weighted-binomial gradient (3.8); the log-concave
localization theorem does not preserve that nonlinear subclass.

## 3. An exact stronger inequality which would orient the crossing

Write

\[
 \ell_j=\log a_j,
 \qquad
 \kappa_j=\ell_{j-1}-2\ell_j+\ell_{j+1}
 =\log{a_{j-1}a_{j+1}\over a_j^2}.
\tag{3.1}
\]

Strict log-concavity says only \(\kappa_j<0\).  The following ordered
curvature condition is strictly stronger:

\[
 \boxed{
 \kappa_j\le\kappa_{j+1}
 \quad(1\le j<2D).}
\tag{3.2}
\]

Equivalently,

\[
 \boxed{
 {a_{j-1}a_{j+1}\over a_j^2}
 \le
 {a_ja_{j+2}\over a_{j+1}^2}.}
\tag{3.3}
\]

### Lemma 3.1 (oriented-curvature crossing criterion)

Assume (3.2), together with

\[
 a_{D-1}>a_{D+1},
 \qquad
 a_0<a_{2D}.
\tag{3.4}
\]

Then

\[
 a_{D-L}-a_{D+L}
\tag{3.5}
\]

has exactly one sign change as \(L=1,ldots,D\), and its orientation is
positive followed by negative.

#### Proof

Put

\[
 g_L=\ell_{D-L}-\ell_{D+L}
 \qquad(0\le L\le D).
\tag{3.6}
\]

Then \(g_0=0\), while a direct second difference gives

\[
 g_{L+1}-2g_L+g_{L-1}
 =\kappa_{D-L}-\kappa_{D+L}\le0.
\tag{3.7}
\]

Thus \(g_L\) is concave.  Equations (3.4) say \(g_1>0\) and
\(g_D<0\).  A concave sequence with these endpoint signs crosses zero
exactly once, from positive to negative.  Exponentiation preserves the
sign comparison in (3.5). \(\square\)

For the PBBS profile, the available theorem proves \(\kappa_j<0\) on the
whole relevant segment.  It does **not** yet prove (3.2).  In the
palindromic notation

\[
 {\mathcal A_j\over V_{r-1,D}}
 =[X^{r-j}](1-X)(1+X)^{2r-2}(1+\rho X+X^2),
\tag{3.8}
\]

condition (3.3), plus the two endpoint comparisons (3.4), is an explicit
finite rational inequality in \((r,D,\rho)\).  Proving it would establish
the exact residual sign orientation, but even that would not by itself
prove the complete partition order, as the next section makes clear.

## 4. The largest-step ordered-composition flow

After pointwise cancellation, let \(s_i=(\mu_i)_+\) be residual part
supplies and \(d_L=(-\mu_L)_+\) residual jobs.  Consider the residual DAG

\[
 u\longrightarrow u-i
 \qquad(1\le i\le\min(D,u)).
\tag{4.1}
\]

The natural monotone greedy rule is:

1. process residual states \(u\) in strictly decreasing order;
2. at state \(u\), include its external job mass \(d_u\) and all flow
   already sent there from larger states; and
3. route as much of that mass as possible through the largest step
   \(i\le u\) whose global supply \(s_i\) has not been exhausted, then
   continue with the next-largest available step.

If this reaches zero and exhausts every supply, its path decomposition is
an explicit fractional partition kernel.  It is not an all-depth theorem.

### Proposition 4.1 (exact terminal depth-five greedy obstruction)

At terminal depth five,

\[
 D=5,qquad r=38,
\tag{4.2}
\]

and

\[
\begin{aligned}
 V_{37,5}&=158985138106653726685,\\
 V_{38,5}&=130481704855775740733.
\end{aligned}
\tag{4.3}

The residual positive coefficients are

\[
\begin{array}{c|r}
i&s_i\\ \hline
1&21279569910196437387025065868478826962600\\
2&34970060092946175659259439535875570177610\\
3&35643542966207173624078631184458913199600\\
4&21524456516363635750552331668676317892830.
\end{array}
\tag{4.4}
\]

There is no residual size-five supply; \(\widehat\mu_5<0\), and every
later coefficient is negative.

Apply the deterministic rule above using the exact ballot formula.  Its
capacity-exhaustion ledger is

\[
\begin{array}{c|c|r|r}
\text{event}&\text{residual }u&\text{last routed mass}
 &\text{unrouted mass at }u\\ \hline
s_4\text{ exhausted}&6&
685058031404524686695424601167495558158&
17400220954310870491395356681452890717738\\
s_3\text{ exhausted}&3&
4833332382756550419548475986033151566097&
22843849575855377080186534863604466287876\\
s_1\text{ exhausted}&1&
21279569910196437387025065868478826962600&
7066233618224837027837574881989803818930.
\end{array}
\tag{4.5}
\]

At the last line, the only unused supply is

\[
 \boxed{
 3533116809112418513918787440994901909465}
\tag{4.6}
\]

pieces of size two.  The stranded residual-one mass is exactly twice
this number:

\[
\boxed{
7066233618224837027837574881989803818930
=2\cdot
3533116809112418513918787440994901909465.}
\tag{4.7}
\]

Thus total volume is still exact, but the remaining size-two pieces
cannot serve the remaining size-one residuals.  The greedy flow is
infeasible.

All entries in (4.3)--(4.7) are direct substitutions and deterministic
recurrences; no optimizer or search is involved.  The terminal
depth-five all-price theorem is already proved by a residue-prefix
certificate, so this is only a no-go for monotone largest-step routing.

## 5. What an all-depth Catalan kernel must add

The two obstructions separate three levels of structure.

1. **Log-concavity** controls local ratios but not the orientation of the
   reflected residual and not modular indivisibility.
2. **Ordered curvature** (3.2), with (3.4), would give the desired exact
   positive-then-negative crossing.  This is the first additional
   coefficient inequality suggested by the palindromic Catalan form.
3. **Residue-aware reservation** is still necessary after the crossing.
   Proposition 4.1 shows that a Monge rule which sees only current size
   consumes the wrong small-part inventory and strands a pure parity
   defect.

Consequently a viable first-return construction must carry at least one
residue/return-state variable.  In the ordered-composition DAG it must
produce nonnegative flows \(y_{u,i}\) satisfying

\[
 \sum_{i\le u}y_{u,i}-\sum_{i=1}^{D}y_{u+i,i}=d_u,
 \qquad
 \sum_{u\ge i}y_{u,i}=s_i,
\tag{5.1}
\]

while reserving small steps for the future residue classes.  The
palindromic first-return identity supplies the natural state space; plain
log-concavity and size-monotone greedy routing do not supply the required
reservation inequality.
