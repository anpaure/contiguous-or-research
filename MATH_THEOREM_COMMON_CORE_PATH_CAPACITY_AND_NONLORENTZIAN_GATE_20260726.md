# Common-core path polynomials: exact capacity, the product-saddle floor, and the non-Lorentzian support gate

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad N=\binom{2m}{m-H},
\tag{0.1}
\]

and use the common-core path length

\[
 L=m-3H+1.
\tag{0.2}
\]

Write

\[
 \Lambda={W\over N},\qquad
 T=LN,\qquad
 \rho={T\over W}={L\over\Lambda}=1-o(1).
\tag{0.3}
\]

Throughout, the asymptotic hypotheses are

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 0\le1-{L\over\Lambda}=o(1).
\tag{0.3a}
\]

The second condition is the explicit packing calibration; it is not a
consequence of the first-order estimate for \(H\) alone.  In particular
it gives \(T\le W\) and \(W-T=o(W)\).  For each rank-\(M\) top \(U\), let
\(\mathscr P(U)\) be the full all-core labelled catalogue of length-\(L\)
core-safe tight paths (the core is part of the option), and define

\[
 Q_U({\bf z})
 =\sum_{P\in\mathscr P(U)}\prod_{X\in P}z_X,
 \qquad
 Q({\bf z})=\prod_U Q_U({\bf z}).
\tag{0.4}
\]

Variables are indexed by middle owners
\(X\in\binom{[2m]}m\).  Repeated labelled representations are retained
as coefficients.  Every monomial of \(Q_U\) is squarefree of degree
\(L\).

This note proves five exact statements.

1. The uniform fractional exponent \(\rho{\bf1}\) is not merely in the
   Newton polytope.  It is the exact positive-real capacity minimizer:

   \[
   \boxed{
   \operatorname {Cap}_{\rho{\bf1}}Q
   :=\inf_{{\bf z}>0}{Q({\bf z})\over\prod_Xz_X^\rho}
   =Q({\bf1}).}
   \tag{0.5}
   \]

   Hence no positive-real capacity or Newton-polytope separator can
   prove that the near-squarefree coefficient is absent.

2. At this exact saddle, the independent product law still has a linear
   floor.  If \(K_X\) is the load of owner \(X\), then

   \[
   K_X\sim\operatorname {Bin}(R,p),\qquad
   R=\binom mH,\qquad
   p={L\over\binom MH},\qquad Rp=\rho,
   \tag{0.6}
   \]

   and therefore

   \[
   \boxed{
   \mathbb E\sum_X\binom{K_X}{2}
    ={\rho^2\over2}\left(1-{1\over R}\right)W,}
   \tag{0.7}
   \]

   \[
   \boxed{
   \mathbb E|\{X:K_X=0\}|
    =W(1-p)^R=(e^{-\rho}+o(1))W.}
   \tag{0.8}
   \]

   Thus exact capacity, gradient balance, and the Hessian/second
   factorial moment stop at a \((1/2+o(1))W\) floor.

3. There is a sharp conditional algebraic-support theorem.  If
   \(\operatorname {supp}Q\) were an M-convex set, then \(Q\) would
   contain a squarefree monomial of degree \(T\).  Such a monomial gives
   the optimal partial-path floor

   \[
   \sum_X\left(\binom{K_X}{2}-K_X+1\right)
   =W-T=o(W).
   \tag{0.9}
   \]

4. The required M-convexity cannot be inherited root by root.  For all
   sufficiently large calibrated \(m\), the support of every root
   factor \(Q_U\) violates basis exchange.  Consequently \(Q_U\) is
   neither a homogeneous stable polynomial nor a Lorentzian polynomial.
   Since stability passes from a product to each factor, the full
   product \(Q\) is not stable either.

5. In fact the *global* Minkowski-sum support is not M-convex.  An
   interior adjacent transposition exposes a two-point root face whose
   direction has two positive and two negative coordinates.  The four
   changed owner targets determine their top, so a generic normal lifts
   this edge to a two-point exposed face of the full product support.
   Consequently the full product \(Q\) is not Lorentzian either.

No estimate

\[
 \min_{{\bf k}\in\operatorname {supp}Q}
 \sum_X\binom{k_X}{2}=o(W)
\tag{0.10}
\]

or a positive linear lower bound is proved.  The exact residual is now
more specific: one needs an approximate box-saturation theorem much
weaker than M-convexity for a Minkowski sum of tight-path supports.
Ordinary capacity, stability, and Lorentzian technology cannot supply
it.

## 1. Tight-path normal form

Fix a top \(U\), \(|U|=M\).  A middle core-safe path is determined, as
far as its middle support is concerned, by an injective word

\[
 w=(w_1,\ldots,w_K),\qquad
 K=L+H-1=m-2H,
\tag{1.1}
\]

in \(U\).  Its deleted \(H\)-sets are

\[
 J_i(w)=\{w_i,w_{i+1},\ldots,w_{i+H-1}\},
 \qquad 1\le i\le L,
\tag{1.2}
\]

and its middle owners are

\[
 X_i(w)=U\setminus J_i(w).
\tag{1.3}
\]

Conversely, every injective word (1.1) occurs in the core-safe
catalogue: its complement in \(U\) has size \(3H\); choose any \(2H\)
of those labels as the protected core and place the remaining \(H\)
labels in the unused initial tail block.

For a support \(B(w)=\{J_1(w),\ldots,J_L(w)\}\), form the graph
\(\Gamma(B(w))\) whose vertices are its \(H\)-sets and whose edges join
sets meeting in exactly \(H-1\) labels.  Global injectivity of \(w\)
gives

\[
 |J_i(w)\cap J_j(w)|=
 \begin{cases}
 H-|i-j|,&|i-j|<H,\\
 0,&|i-j|\ge H.
 \end{cases}
\tag{1.4}
\]

Hence

\[
                         \Gamma(B(w))=P_L.
\tag{1.5}
\]

This elementary support invariant will witness failure of exchange.

## 2. Exact positive-real capacity

For a nonnegative polynomial \(F\) and a nonnegative exponent vector
\({\boldsymbol\alpha}\) of the same total degree, put

\[
 \operatorname {Cap}_{\boldsymbol\alpha}F
 =\inf_{{\bf z}>0}{F({\bf z})\over{\bf z}^{\boldsymbol\alpha}}.
\tag{2.1}
\]

### Theorem 2.1 (capacity saturation)

Equation (0.5) holds.

#### Proof

Put \(z_X=e^{x_X}\) and

\[
 F({\bf x})=\log Q(e^{\bf x})-\rho\sum_Xx_X.
\tag{2.2}
\]

The first term is a finite log-sum-exp, so \(F\) is convex.  The
coordinate group \(S_{2m}\) preserves the full product catalogue and
acts transitively on the middle layer.  Under the coefficient-weighted
uniform law on all labelled product terms, every owner therefore has
the same expected exponent.  The total exponent is always \(T\), so
that expectation is \(T/W=\rho\).  Consequently

\[
                         \nabla F({\bf0})=0.
\tag{2.3}
\]

A stationary point of a convex function is a global minimizer.  Thus
the infimum in (2.1), with
\({\boldsymbol\alpha}=\rho{\bf1}\), is attained at \({\bf z}={\bf1}\),
and equals \(Q({\bf1})\). \(\square\)

The argument uses the full nonlinear polynomial, not a target-weight
Hall inequality.  It shows that even the strongest ordinary
positive-real capacity test is exactly on the feasible side.

## 3. The exact saddle second factorial moment

Choose one labelled path independently and uniformly in every top.
Fix a middle owner \(X\).  It lies in exactly

\[
                         R=\binom mH
\tag{3.1}
\]

rank-\(M\) tops.  In any one such top the stabilizer of the top is
transitive on its \(\binom MH\) middle subsets.  Since every path has
exactly \(L\) owners,

\[
 \Pr(X\hbox{ is used by the path in }U)
 =p={L\over\binom MH}.
\tag{3.2}
\]

Choices at distinct tops are independent.  This proves (0.6), using
the incidence identity

\[
 {\binom MH\over\binom mH}={W\over N}=\Lambda.
\tag{3.3}
\]

### Theorem 3.1 (linear product-saddle floor)

Equations (0.7)--(0.8) hold.  Moreover

\[
 \operatorname {tr}\nabla^2\log Q(e^{\bf x})\big|_{{\bf x}=0}
 =\sum_X\operatorname {Var}K_X
 =\rho(1-p)W=(1+o(1))W.
\tag{3.4}
\]

#### Proof

For a binomial random variable,

\[
 \mathbb E\binom{K_X}{2}=\binom R2p^2,
 \qquad
 \Pr(K_X=0)=(1-p)^R,
 \qquad
 \operatorname {Var}K_X=Rp(1-p).
\tag{3.5}
\]

Sum over the \(W\) owners.  Since \(Rp=\rho\to1\) and
\(p=\rho/R=o(1)\), equations (0.7), (0.8), and (3.4) follow.
The Hessian identity is the standard log-partition covariance identity,
obtained by differentiating the finite polynomial. \(\square\)

For the partial-path floor functional

\[
 \Phi_{\rm path}({\bf k})
 =\sum_X\left(\binom{k_X}{2}-k_X+1\right),
\tag{3.6}
\]

homogeneity gives the exact identity

\[
 \Phi_{\rm path}({\bf k})
 =\sum_X\binom{k_X}{2}+W-T.
\tag{3.7}
\]

Thus the product saddle has

\[
 \mathbb E\Phi_{\rm path}
 =\left({1\over2}+o(1)\right)W,
\tag{3.8}
\]

whereas any squarefree support point has the optimal value
\(W-T=o(W)\).  The gap is entirely correlation/support, not capacity.

## 4. What M-convex support would prove

Recall that a finite constant-sum set
\(B\subseteq\mathbb Z_{\ge0}^{W}\) is M-convex if for every
\({\bf a},{\bf b}\in B\) and every coordinate \(i\) with
\(a_i>b_i\), there is a coordinate \(j\) with \(a_j<b_j\) such that

\[
                         {\bf a}-e_i+e_j\in B.
\tag{4.1}
\]

### Theorem 4.1 (M-convex squarefree rounding)

Let \(G({\bf z})\) be any homogeneous nonnegative polynomial of degree
\(T\le W\).  Suppose a transitive variable group preserves \(G\), and
suppose \(\operatorname {supp}G\) is M-convex.  Then \(G\) has a
squarefree monomial.

In particular, if \(\operatorname {supp}Q\) were M-convex, then
\(\min\Phi_{\rm path}=W-T=o(W)\).

#### Proof

The coefficient-weighted barycenter of the support is fixed by the
transitive group.  Since every support vector has coordinate sum \(T\),
the barycenter is

\[
                         {T\over W}{\bf1}\in[0,1]^W.
\tag{4.2}
\]

For completeness, use the box-integrality lemma for integral base
polyhedra.  If \(B(g)\) is the base polytope of an integer submodular
rank \(g\) and \(u\) is integral, then, whenever the intersection is
nonempty,

\[
 B(g)\cap\{x_i\le u_i\}=B(g_u),\qquad
 g_u(S)=\min_{T\subseteq S}\bigl(g(T)+u(S\setminus T)\bigr).
\tag{4.3}
\]

The two systems of subset inequalities imply one another, and \(g_u\)
is again integer submodular; hence its base polytope is integral.  The
convex hull of an M-convex set is such an integral base polytope, and
its integer points are exactly the M-convex set.  Apply (4.3) with
\(u_i=1\).  The intersection is nonempty by (4.2), so it has an integer
point \({\bf b}\).  The
coordinates of \({\bf b}\) are nonnegative integers at most one and
sum to \(T\), so \({\bf b}\) is squarefree.  Integrality and saturation
give \({\bf b}\in\operatorname {supp}G\). \(\square\)

Thus an M-convexity theorem for the *global Minkowski sum* would solve
the middle common-core gate exactly.  The next section shows why it
cannot be obtained factorwise.

## 5. Root path support violates exchange

### Theorem 5.1 (non-M-convex root support)

For all sufficiently large calibrated \(m\), and every top \(U\), the
set of monomial supports of \(Q_U\) is not M-convex.

#### Proof

Choose one injective word \(w^0\) of length \(K\), and write its windows
as

\[
                         E_1,E_2,\ldots,E_L.
\tag{5.1}
\]

Let \({\cal F}\) be the family of \(H\)-sets \(F\subset U\) satisfying

\[
 |F\cap E_2|=H-1
 \quad\hbox{or}\quad
 |F\cap E_L|=H-1.
\tag{5.2}
\]

Its size is at most

\[
                         |{\cal F}|\le2H(M-H).
\tag{5.3}
\]

Choose a uniformly random injective word \(w^1\) of length \(K\).
Every one of its \(L\) windows is a uniform \(H\)-subset of \(U\), so

\[
 \mathbb E|B(w^1)\cap{\cal F}|
 \le {2LH(M-H)\over\binom MH}=o(1).
\tag{5.4}
\]

For all sufficiently large \(m\), there is therefore a word \(w^1\)
whose support \(B_1=B(w^1)\) avoids \({\cal F}\).  Put
\(B_0=B(w^0)\).  Since

\[
                         |E_1\cap E_2|=H-1,
\tag{5.5}
\]

one has \(E_1\in{\cal F}\), and hence \(E_1\in B_0\setminus B_1\).

Suppose the basis exchange axiom held at this coordinate.  Then some
\(F\in B_1\setminus B_0\) would make

\[
                         B'=(B_0-\{E_1\})\cup\{F\}
\tag{5.6}
\]

the support of another tight path.  But the \((H-1)\)-intersection
graph on \(B_0-\{E_1\}\) is the path

\[
                         E_2-E_3-\cdots-E_L.
\tag{5.7}
\]

For the graph on \(B'\) to be \(P_L\), the new vertex \(F\) must attach
to one of the two endpoints \(E_2,E_L\).  Attaching only to an internal
vertex creates degree three, attaching to more vertices also fails, and
attaching to none disconnects the graph.  Yet (5.2) contains every set
which can attach to an endpoint, and \(B_1\cap{\cal F}\) is
empty.  Thus no such \(F\) exists, contradicting exchange. \(\square\)

### Corollary 5.2 (stable/Lorentzian route is unavailable)

Every \(Q_U\) is a homogeneous multiaffine polynomial with nonnegative
coefficients.  The support of such a stable polynomial is a matroid base
family, and the support of a Lorentzian polynomial is M-convex.  Theorem
5.1 therefore shows that \(Q_U\) is neither stable nor Lorentzian.

If the full product \(Q=\prod_UQ_U\) were stable, every factor would be
stable, because a product is nonvanishing on the product upper half-plane
only if each factor is.  Hence \(Q\) is not stable.

The factorwise theorem alone would still allow the much larger
Minkowski sum \(\operatorname {supp}Q\) to become M-convex.  The next
section rules out that exact possibility as well.  It does not rule out
a weaker approximate box-saturation property sufficient for \(o(W)\)
collision defect.

## 6. A global exposed-edge obstruction

The exact M-convex regularization suggested above is in fact impossible.
What remains possible is only a weaker approximate box-saturation
property.

### Theorem 6.1 (the full product support is not M-convex)

For all sufficiently large calibrated \(m\),

\[
 \boxed{\operatorname {supp}Q\text{ is not M-convex}.}
\tag{6.1}
\]

Consequently the full product polynomial \(Q\) is not Lorentzian.

#### Proof

Fix a top \(U\), an injective word \(w_1,\ldots,w_K\), and an index

\[
 H+1\le j\le L-2.
\tag{6.2}
\]

Such an index exists because \(m\ge4H+2\) for all sufficiently large
\(m\).  Put

\[
 x=w_j,\qquad y=w_{j+1},\qquad
 a=j-H+1,qquad b=j+1=a+H.
\tag{6.3}
\]

Swap the adjacent letters \(x,y\).  Of the \(L\) consecutive
\(H\)-windows, exactly the windows at indices \(a,b\) change.  Write

\[
 \begin{aligned}
 A&=S\cup\{x\},& A'&=S\cup\{y\},\\
 B&=T\cup\{y\},& B'&=T\cup\{x\},
 \end{aligned}
\tag{6.4}
\]

where \(|S|=|T|=H-1\) and \(S\cap T=\varnothing\).  Let \(B_0,B_1\)
be the two deleted-window supports and let

\[
 {\cal K}=B_0\cap B_1,qquad |{\cal K}|=L-2.
\tag{6.5}
\]

Give weight two to every member of \({\cal K}\), weight one to
\(A,A',B,B'\), and weight zero to every other \(H\)-set.  Both \(B_0\)
and \(B_1\) have weight \(2L-2\).  If a contender omits \(c\ge1\)
members of \({\cal K}\), then it contains at most \(\min(4,c+2)\) of
the exceptional windows, and hence has weight at most

\[
 2(L-2-c)+\min(4,c+2)<2L-2.
\tag{6.6}
\]

Thus every maximizing tight-path support contains all of \({\cal K}\)
and exactly two exceptional windows.

Deleting the two old windows at \(a,b\) splits the induced Johnson path
into three nonempty components.  For \(H\ge3\), direct intersection
counts show that \(A,A'\) can bridge only the first gap and \(B,B'\)
only the second.  Hence a connected path completion chooses one member
of each pair.  Its path order is the original order, up to reversal.

For an oriented sequence of consecutive windows \(V_1,\ldots,V_L\),
put

\[
 \ell_i=V_i\setminus V_{i+1},\qquad
 e_i=V_{i+1}\setminus V_i.
\tag{6.7}
\]

Every injective-word tight path satisfies the lag identity

\[
 e_i=\ell_{i+H}.
\tag{6.8}
\]

At \(i=a-1\), the first-gap choice gives \(e_{a-1}=x\) for \(A\)
and \(e_{a-1}=y\) for \(A'\).  At \(b-1=a+H-1\), the second-gap
choice gives \(\ell_{b-1}=x\) for \(B\) and \(\ell_{b-1}=y\) for
\(B'\).  Therefore (6.8) permits exactly

\[
 (A,B)\quad\hbox{or}\quad(A',B'),
\tag{6.9}
\]

and excludes the two mixed choices.  Reversing a realizing word gives
the same test in the canonical orientation.  Hence the displayed
weight exposes exactly the segment joining \(B_0\) and \(B_1\) in the
deleted-window support polytope.  Complementation inside \(U\) is a
coordinate relabelling, so this is also an exposed edge of the owner
support polytope.

Pass now to the owner variables \(X_J=U\setminus J\).  Since the old
windows \(A,B\) are disjoint,

\[
 X_A\cup X_B=U.
\tag{6.10}
\]

The exposed edge direction is

\[
 d={\bf1}_{X_{A'}}+{\bf1}_{X_{B'}}
   -{\bf1}_{X_A}-{\bf1}_{X_B}.
\tag{6.11}
\]

If two support vectors in the factor of another top \(V\) had
difference parallel to \(d\), squarefreeness forces the scalar to be
\(\pm1\).  All four changed owners would then lie in \(V\).  In
particular (6.10) gives \(U\subseteq V\), and equal top sizes force
\(U=V\).  Thus no distinct top factor has a support difference parallel
to \(d\).

We use the following elementary normal-cone fact.  For an exposed edge
of direction \(d\), a tie hyperplane contains its entire normal cone
only if the corresponding support difference is parallel to \(d\).
Indeed the orthogonal complement of the linear span of the edge normal
cone is precisely \(\mathbb Rd\).  Therefore a generic normal in the
relative interior of the root edge cone avoids the finitely many tie
hyperplanes from every other top factor.  It exposes one exponent vector
in every other factor and the two-point edge in the factor of \(U\).

Faces commute with Minkowski sums, and positivity of coefficients gives

\[
 \operatorname {supp}Q=\sum_V\operatorname {supp}Q_V.
\tag{6.12}
\]

Hence the corresponding global support face consists of exactly two
exponent vectors and has direction (6.11).  This direction has two
positive and two negative coordinates.  The two-point face fails the
unit exchange axiom (equivalently, edges of an integral polymatroid base
polytope are parallel to \(e_i-e_j\)).  Faces of M-convex sets are
M-convex, so the full support cannot be M-convex.  Lorentzian support is
M-convex, proving the final assertion. \(\square\)

## 7. Exact remaining alternatives

The direct coefficient problem now has three sharply separated levels.

1. **Convex/capacity level:** solved exactly by Theorem 2.1.  It is
   feasible with equality.
2. **Product-saddle fluctuation level:** solved exactly by Theorem 3.1.
   It has a linear floor and therefore cannot be rounded by an
   uncorrelated second-moment argument.
3. **Integral support level:** unresolved.  It is enough to prove either

   \[
   \min_{{\bf k}\in\operatorname {supp}Q}
      \sum_X\binom{k_X}{2}=o(W),
   \tag{7.1}
   \]

   or some approximate box-saturation assertion weaker than the global
   M-convexity ruled out by Theorem 6.1.  A negative result must instead
   prove a genuinely nonlinear inequality separating every support
   vector from the box \([0,1]^W\) by order \(W\).

The obstruction is therefore not lack of entropy or positive capacity.
There is ample fractional entropy, but the local Hamilton-tight-path
supports have explicit exchange holes.  What remains is whether the
catalogue-wide Minkowski sum heals those holes to \(o(W)\), or retains a
macroscopic nonlinear defect.
