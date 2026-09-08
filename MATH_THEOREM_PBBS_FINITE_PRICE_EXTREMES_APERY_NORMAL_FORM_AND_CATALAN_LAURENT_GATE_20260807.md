# Finite closed-price extremes are weighted clocks; a lossless Apéry form exposes the exact Catalan Laurent gate

**Date:** 2026-08-07

**Status:** unconditional finite-cone theorem, exact fractional-extreme
counterexample, and lossless PBBS Farkas reduction.  The normalized finite
anchored-window cone is not integral: strict unit counting clocks do not
exhaust its extreme rays.  Every physical min-plus price nevertheless has
an exact length-residue Apéry shortest-path form, and the terminal PBBS
functional becomes one explicit coefficient of
\((1-X)(1+X)^{2r-2}(1+\rho X+X^2)\), plus the two exact rank-one boundary
terms.  The final coefficient inequality is not proved.

## 1. The finite anchored-window cone

Let \(\psi(0)=0\), and for \(1\le q\le N\) put

\[
 a_q=\psi(q)-\psi(q-1).
\tag{1.1}
\]

The function \(\psi\) is nonnegative, nondecreasing, and subadditive on
\(\{0,\ldots,N\}\) if and only if

\[
 a_q\ge0
\tag{1.2}
\]

and

\[
 \boxed{
 \sum_{q=x+1}^{x+t}a_q
 \le
 \sum_{q=1}^{t}a_q
 \qquad(x,t\ge1,\ x+t\le N).}
\tag{1.3}
\]

Indeed, (1.3) is exactly

\[
 \psi(x+t)-\psi(x)\le\psi(t).
\tag{1.4}
\]

Write \(\mathsf{AW}_N\) for this rational polyhedral cone.  The singleton
case of (1.3) gives

\[
 0\le a_q\le a_1.
\tag{1.5}
\]

Thus \(a_1=0\) forces \(a=0\).  Every nonzero ray has the unique
normalization

\[
 a_1=1,
\tag{1.6}
\]

and the normalized section is a compact rational polytope.

### Theorem 1.1 (exact active-window characterization)

For \(a\in\mathsf{AW}_N\setminus\{0\}\), let \(\mathcal E(a)\) consist
of

1. the coordinate equations \(a_q=0\) which are tight at \(a\); and
2. the window equations

   \[
   \sum_{q=x+1}^{x+t}a_q
   =\sum_{q=1}^{t}a_q
   \tag{1.7}
   \]

   which are tight at \(a\).

Then the ray \(\mathbb R_{\ge0}a\) is extreme if and only if the normals
of \(\mathcal E(a)\) have rank \(N-1\).  Equivalently, after imposing
\(a_1=1\), their restrictions to the variables
\(a_2,\ldots,a_N\) have rank \(N-1\).

#### Proof

The minimal face of a polyhedral cone containing \(a\) is cut out by all
inequalities tight at \(a\).  It is one-dimensional exactly when the
active normals have codimension one.  Intersecting with (1.6) converts
the same statement into the standard full-rank vertex criterion for the
normalized polytope. \(\square\)

This is an exact finite characterization, but it is a rank criterion,
not a combinatorial classification by arithmetic clocks.  It describes
the full finite price cone when every denomination through \(N\) is
available.  The physically truncated case, with only sizes through
\(D<N\), is the min-plus image treated in Section 4.

## 2. A fractional extreme ray

### Theorem 2.1 (nonintegrality at support six)

The vector

\[
 \boxed{
 a=\left(1,0,{1\over2},{1\over2},0,1\right)}
\tag{2.1}
\]

is a vertex of the normalized section of \(\mathsf{AW}_6\).  Hence it
generates an extreme ray, but it is not a strict unit counting-clock ray.

#### Proof

Its prefix sums are

\[
 1, 1, {3\over2}, 2, 2, 3.
\tag{2.2}
\]

For translated blocks of lengths \(t=1,2,3,4,5\), the largest block
sums are respectively

\[
 1, 1, {3\over2}, 2, 2.
\tag{2.3}
\]

Thus every anchored-window inequality (1.3) holds.

At (2.1), the following five independent equations are tight:

\[
\begin{aligned}
 a_2&=0,\\
 a_5&=0,\\
 a_6&=a_1,\\
 a_3+a_4&=a_1+a_2,\\
 a_4+a_5+a_6&=a_1+a_2+a_3.
\end{aligned}
\tag{2.4}
\]

After \(a_1=1\), they force

\[
 a_2=a_5=0,\qquad a_6=1,\qquad a_3=a_4={1\over2}.
\tag{2.5}
\]

Theorem 1.1 proves extremality. \(\square\)

Multiplying by two, the corresponding extreme price is

\[
 \boxed{
 (\psi(1),\ldots,\psi(6))=(2,2,3,4,4,6).}
\tag{2.6}
\]

Its integer jump measure is

\[
 2\delta_0+\delta_2+\delta_3+2\delta_5.
\tag{2.7}
\]

This is a weighted counting clock with repeated atom positions, not a
strict unit clock.  Consequently a proposed extreme-ray classification
by strict superadditive atom sequences is false already in dimension six.

## 3. Exact weighted-clock normal form

The failure above does not destroy the inverse-clock description.

### Proposition 3.1 (rational rays are weighted clocks)

Every extreme ray of \(\mathsf{AW}_N\) has a rational generator.  After
integer scaling, its cumulative price

\[
 g(n)=\sum_{q=1}^{n}a_q
\tag{3.1}
\]

is integer-valued, nondecreasing, and subadditive.  Its generalized
inverse positions, with repetitions retained, form a finite truncated
superadditive clock.  Conversely, these clocks are in bijection with the
nonzero integer points of \(\mathsf{AW}_N\).

#### Proof

The first assertion follows because \(\mathsf{AW}_N\) is a rational
polyhedral cone.  For the inverse statement, put

\[
 x_m=\max\{0\le n\le N:g(n)\le m\},
\tag{3.2}
\]

and extend the sequence by \(x_m=N\) for \(m\ge g(N)\).  It is
nondecreasing, starts at \(x_0=0\), and satisfies

\[
 x_{m+n}\ge\min\{N,x_m+x_n\}.
\tag{3.3}
\]

When \(x_m+x_n\le N\), this follows from

\[
 g(x_m+x_n)\le g(x_m)+g(x_n)\le m+n.
\tag{3.4}
\]

If \(x_m+x_n>N\), split \(N=u+v\) with \(u\le x_m\) and \(v\le x_n\).
Then \(g(N)\le g(u)+g(v)\le m+n\), so \(x_{m+n}=N\).

Conversely, let a nondecreasing integer sequence \((x_m)_{m\ge0}\)
satisfy \(x_0=0\), be eventually equal to \(N\), and obey (3.3).  Put

\[
 g(n)=\min\{m:x_m\ge n\}.
\tag{3.5}
\]

If \(u+v\le N\), then (3.3), with \(m=g(u)\) and \(n=g(v)\), gives
\(x_{m+n}\ge u+v\), hence

\[
 g(u+v)\le g(u)+g(v).
\tag{3.6}
\]

Thus \(g\) is integer-valued, nondecreasing, and subadditive, so its
increments lie in \(\mathsf{AW}_N\).  The two generalized-inverse
constructions recover one another. \(\square\)

Thus a lossless clock classification must allow multiplicities.  Among
those weighted clocks, extremality is exactly the active-window rank test
of Theorem 1.1.  Unit clocks form a distinguished extreme family, but not
the complete family.

## 4. Lossless finite Apéry normal form

Fix physical piece sizes \(1,\ldots,D\), nonnegative piece prices
\(p_1,\ldots,p_D\), and their exact min-plus closure

\[
 \psi_p(L)=
 \min_{\substack{x\in\mathbb Z_{\ge0}^{D}\\
                  \sum_{i=1}^{D}ix_i=L}}
       \sum_{i=1}^{D}p_ix_i.
\tag{4.1}
\]

For monotone capacity prices, allowing total capacity at least \(L\)
gives the same closure: trim the last used capacity to obtain equality
without increasing its price.

Choose a minimum-density denomination

\[
 {p_h\over h}=\min_{1\le i\le D}{p_i\over i}=:m
\tag{4.2}
\]

and put

\[
 e_i=p_i-mi\ge0,qquad e_h=0.
\tag{4.3}
\]

For \(L\ge1\), define

\[
 \mathcal C_{h,L}^{(D)}=
 \left\{x\in\mathbb Z_{\ge0}^{\{1,\ldots,D\}\setminus\{h\}}:
 \sum_{i\ne h}ix_i\le L,
 \quad
 \sum_{i\ne h}ix_i\equiv L\pmod h
 \right\}.
\tag{4.4}
\]

### Theorem 4.1 (exact length-residue Apéry formula)

For every \(L\),

\[
 \boxed{
 \delta_e(L):=\psi_p(L)-mL
 =\min_{x\in\mathcal C_{h,L}^{(D)}}x\cdot e.}
\tag{4.5}
\]

#### Proof

Given a partition of \(L\), delete all size-\(h\) pieces.  The remaining
ordinary length is at most \(L\), has residue \(L\) modulo \(h\), and its
reduced cost is \(x\cdot e\).  Conversely, every vector in (4.4) can be
completed to length \(L\) by

\[
 {L-\sum_{i\ne h}ix_i\over h}
\tag{4.6}
\]

zero-reduced-cost size-\(h\) pieces. \(\square\)

If only lengths at most \(N\) are needed, formula (4.5) is a finite
shortest-path problem on the state space

\[
 (\ell,a),\qquad 0\le\ell\le N,\quad a\in\mathbb Z/h\mathbb Z,
\tag{4.7}
\]

where a size-\(i\) edge increases ordinary length by \(i\), changes the
residue by \(i\), and costs \(e_i\).  It is lossless: the finite
availability shoulder is precisely the length coordinate \(\ell\).
Dropping that coordinate gives the stabilized cyclic Apéry distance and
therefore loses exactly the shoulder information.

## 5. Exact finite Farkas form

Let \(s_i\ge0\) be piece supplies and \(d_L\ge0\) job demands, with

\[
 \sum_{i=1}^{D}is_i=\sum_{L=1}^{N}Ld_L.
\tag{5.1}
\]

The fractional partition system is

\[
\begin{aligned}
 \sum_{\pi\in\mathscr P_D(L)}z_{L,\pi}&=d_L,\\
 \sum_{L,\pi}m_i(\pi)z_{L,\pi}&\le s_i,\\
 z_{L,\pi}&\ge0.
\end{aligned}
\tag{5.2}
\]

Its exact Farkas dual is

\[
 \boxed{
 \sum_{i=1}^{D}s_i y_i
 \ge
 \sum_{L=1}^{N}d_L
       \min_{\pi\in\mathscr P_D(L)}
       \sum_{i=1}^{D}m_i(\pi)y_i
 \qquad(y\ge0).}
\tag{5.3}
\]

Testing arbitrary \(y\ge0\) is lossless even though only closed tables
are needed.  Replacing \(y\) by its min-plus closure leaves every job
minimum unchanged and can only lower the supply side.  Hence (5.3) for
closed tables implies it for raw tables, while the converse is immediate.

After choosing a minimum-density \(h\), (5.3) is equivalently

\[
 \boxed{
 \sum_{i=1}^{D}s_i e_i
 \ge
 \sum_{L=1}^{N}d_L\,\delta_e(L),}
\tag{5.4}
\]

where \(\delta_e\) is the exact length-residue minimum (4.5).  The linear
part cancels by (5.1).  This is the requested lossless residue/Apéry
normal form of the finite Farkas dual.

### Proposition 5.1 (equivalence with monotone covering prices)

Under the volume balance (5.1), inequality (5.4) for every reduced vector
\(e\ge0\) having at least one zero coordinate is equivalent to positivity
of the signed margin for every nonnegative nondecreasing raw piece-price
table and its covering closure.

#### Proof

Given a nondecreasing table \(p\), choose a minimum-density denomination
\(h\) as in (4.2).  Equations (4.3)--(4.5) and volume balance turn its
margin exactly into the difference in (5.4).

Conversely, fix \(e\ge0\) with \(e_h=0\).  Choose \(m\ge0\) large enough
that

\[
 p_i=mi+e_i\qquad(1\le i\le D)
\tag{5.5}
\]

is nondecreasing.  Then \(h\) is a minimum-density denomination and the
covering closure is \(mL+\delta_e(L)\).  Its linear part again cancels by
(5.1), leaving precisely (5.4). \(\square\)

## 6. Specialization to the PBBS Catalan gradient

Take the terminal PBBS pair at depth \(D\).  Put

\[
 M=r-D,qquad
 V_c=V_{r-1,D},qquad V_p=V_{r,D},qquad
 \lambda={V_p\over V_c},qquad \rho=2-\lambda>0.
\tag{6.1}
\]

Let \(C(z)=1+zC(z)^2\), \(X=C(z)-1=zC(z)^2\), and define

\[
 \mathscr L(F)
 =V_c[z^M]C(z)^{2D+1}(1-\lambda z)F(X).
\tag{6.2}
\]

Away from the two modified rank-one endpoints,

\[
 \mathcal A_{D+k}=\mathscr L(X^k).
\tag{6.3}
\]

The PBBS supply and demand vectors are

\[
 s_i=\mathcal A_{D-i}\quad(1\le i\le D),
 \qquad
 d_L=\mathcal A_{D+L}\quad(1\le L\le M-1).
\tag{6.4}
\]

For a reduced physical price \(e\), define the finite Laurent defect

\[
 \Phi_e(X)=
 \sum_{i=1}^{D}e_iX^{-i}
 -\sum_{L=1}^{M-1}\delta_e(L)X^L.
\tag{6.5}
\]

### Theorem 6.1 (exact Catalan Laurent coefficient identity)

The terminal PBBS Farkas margin is

\[
\boxed{
\begin{aligned}
 \mathfrak F_{r,D}(e)
 ={}&\mathscr L(\Phi_e)
   +V_p\delta_e(M-2)\\
 &-(V_c+V_p)\delta_e(M-1).
\end{aligned}}
\tag{6.6}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
 \mathfrak F_{r,D}(e)
 ={}&V_c[X^M](1-X)(1+X)^{2r-2}
       (1+\rho X+X^2)\Phi_e(X)\\
 &+V_p\delta_e(M-2)
 -(V_c+V_p)\delta_e(M-1).
\end{aligned}}
\tag{6.7}
\]

#### Proof

For all supply indices \(D-i\le D-1\), equation (6.3) is exact.  It is
also exact for demand indices through \(r-3\).  At the last two indices,
the modified rank-one convention gives

\[
\begin{aligned}
 \mathcal A_{r-2}
 &=\mathscr L(X^{M-2})-V_p,\\
 \mathcal A_{r-1}
 &=\mathscr L(X^{M-1})+V_c+V_p.
\end{aligned}
\tag{6.8}
\]

Insert (6.4)--(6.5) in the reduced Farkas margin (5.4).  The two
corrections in (6.8) give the last line of (6.6).

Finally the Catalan change of variables

\[
 z={X\over(1+X)^2}
\tag{6.9}
\]

turns (6.2) into

\[
 \mathscr L(F)
 =V_c[X^M](1-X)(1+X)^{2r-2}
       (1+\rho X+X^2)F(X),
\tag{6.10}
\]

proving (6.7). \(\square\)

## 7. Exact remaining inequality

The all-depth volume-seed theorem is now exactly the statement that, for
every terminal \((r,D)\), every choice of minimum-density \(h\), and every
nonnegative reduced edge-cost vector \(e\) with \(e_h=0\), the right side
of (6.7) is nonnegative, where \(\delta_e\) is the finite constrained
shortest path (4.5).

This formulation retains all three pieces which earlier reductions could
not hold simultaneously:

1. the exact PBBS factor
   \((1+X)^{2r-2}(1+\rho X+X^2)\);
2. every cyclic residue interaction; and
3. the finite availability shoulder.

The fractional extreme ray (2.1) rules out a classification using only
strict unit clocks.  Formula (6.7) is therefore the lossless finite target:
a proof must establish coefficient positivity for the full weighted-clock
or length-residue cone, not merely for arithmetic or strict clocks.
