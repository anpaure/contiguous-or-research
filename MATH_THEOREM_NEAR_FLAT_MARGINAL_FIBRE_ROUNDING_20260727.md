# Aggregate marginal flatness gives a low-collision integer load

Date: 2026-07-27

Method: pure mathematics only.

## 0. Outcome

Put

\[
 n=2m,\qquad \Omega=\binom{[2m]}m,\qquad
 W=|\Omega|=\binom{2m}m,
\]

and let

\[
 \Psi(L)=\sum_{D\in\Omega}\binom{L_D}{2}.
\]

The load-space question left open in
`MATH_THEOREM_COMMON_CORE_COORDINATE_MARGINAL_FLATNESS_20260727.md`
has a positive answer.  The correct hypothesis is aggregate normalized
flatness, and the actual legal common-core interval implies it.

### Theorem A (near-flat marginal rounding)

Suppose that $T/W\to1$, that $b_1,\ldots,b_{2m}$ are integers with

\[
 0<b_i<T,\qquad \sum_{i=1}^{2m}b_i=mT,
\tag{0.1}
\]

and, on putting

\[
 \varepsilon_i={b_i\over T}-{1\over2},
\]

one has

\[
 \|\varepsilon\|_\infty=o(1),\qquad
 \|\varepsilon\|_2^2=o(1).
\tag{0.2}
\]

Then there is a nonnegative integer load $L\in\mathbb Z_{\ge0}^{\Omega}$
such that

\[
 \sum_D L_D=T,\qquad
 \sum_{D\ni i}L_D=b_i\quad(1\le i\le2m),
\tag{0.3}
\]

and

\[
 \boxed{\Psi(L)=o(W).}
\tag{0.4}
\]

### Corollary B (the legal common-core marginal box is sufficient)

Use the notation

\[
 M=m+H,\qquad d=m-3H+1,\qquad \kappa=4H-1,
\]

\[
 N=\binom{2m}{M},\qquad T=dN=W-o(W),
\tag{0.5}
\]

where \(H=(1+o(1))\sqrt{m\log m}\).  If the integer marginals satisfy
the exact legal interval

\[
 (m-\kappa)\binom{2m-1}{M-1}
 \le b_i\le
 m\binom{2m-1}{M-1}
\tag{0.6}
\]

and $\sum_i b_i=mT$, then (0.3)--(0.4) hold.

Thus there is no high-energy obstruction in the abstract fibre of any
legal common-core singleton-marginal vector.  This does **not** assert
that the low-collision vector is a coefficient of the common-core product:
physical path support and all higher-rank traces are extra constraints.

The aggregate condition in (0.2) is essential.  The weaker statement

\[
 b_i=W/2+o(W)\quad\hbox{uniformly in }i
\tag{0.7}
\]

is false by itself.  Section 6 constructs a nonempty marginal fibre
satisfying (0.7) on which every load has \(\Psi=\Omega(W)\).

## 1. The legal interval implies aggregate flatness

Write

\[
 \delta_i=b_i-{T\over2}.
\tag{1.1}
\]

Since

\[
 \binom{2m-1}{M-1}={M\over2m}N,
 \qquad T=(M-\kappa)N,
\]

the two endpoints in (0.6), measured from \(T/2\), are exactly

\[
 -a\le\delta_i\le c,
 \qquad
 a={\kappa HN\over2m},\qquad
 c={\kappa N\over2}.
\tag{1.2}
\]

Also $\sum_i\delta_i=0$.  If

\[
 P=\sum_{\delta_i>0}\delta_i
   =\sum_{\delta_i<0}(-\delta_i),
\]

then the lower bound in (1.2) gives

\[
 P\le 2ma=\kappa HN.
\tag{1.3}
\]

Consequently

\[
 \begin{aligned}
 \|\delta\|_2^2
 &\le c\sum_{\delta_i>0}\delta_i
      +a\sum_{\delta_i<0}(-\delta_i)\\
 &\le (a+c)\kappa HN
 =O(\kappa^2HN^2).
 \end{aligned}
\tag{1.4}
\]

Since \(T\asymp mN\), \(\kappa=O(H)\), and

\[
 {H^3\over m^2}
 =O\left({(\log m)^{3/2}\over\sqrt m}\right)=o(1),
\]

equation (1.4) gives

\[
 \sum_i\left({b_i\over T}-{1\over2}\right)^2
 =O\left({H^3\over m^2}\right)=o(1).
\tag{1.5}
\]

Moreover \(c/T=O(H/m)=o(1)\), and the same is true of \(a/T\).
Thus (0.2) follows.  Notice that the asymmetric *exact* interval and
the zero-sum identity are both used: coordinatewise \(o(W)\) alone
does not imply (1.5).

## 2. A near-uniform fractional load with the exact marginals

We use the following standard local fact about the hypersimplex.  A proof
is included to record the uniformity in the growing dimension.

### Lemma 2.1 (local maximum-entropy parametrization)

Let \(U\) be uniform on \(\Omega\).  If

\[
 q_i={1\over2}+\varepsilon_i,\qquad
 \sum_i\varepsilon_i=0,\qquad
 \|\varepsilon\|_\infty=o(1),\qquad
 \|\varepsilon\|_2=o(1),
\tag{2.1}
\]

then there is a probability distribution \(p\) on \(\Omega\) with

\[
 \sum_{D\ni i}p_D=q_i
\tag{2.2}
\]

and

\[
 \chi^2(p\|U)
 :=W\sum_D\left(p_D-{1\over W}\right)^2=o(1).
\tag{2.3}
\]

#### Proof

On the hyperplane

\[
 V=\{\theta\in\mathbb R^{2m}:\sum_i\theta_i=0\}
\]

put

\[
 F(\theta)=\log\mathbb E_U
     \exp\left(\sum_i\theta_i{\mathbf 1}_{\{i\in D\}}\right).
\tag{2.4}
\]

At zero, \(\nabla F(0)=\tfrac12\mathbf1\).  The covariance matrix of
the uniform \(m\)-subset has, on \(V\), the single eigenvalue

\[
 \rho_m={m\over2(2m-1)}\ge {1\over4}.
\tag{2.5}
\]

There are absolute constants $r_0,c,C>0$ such that, uniformly in
\(m\),

\[
 cI_V\preceq\nabla^2F(\theta)\preceq CI_V
 \qquad(\theta\in V,\ \|\theta\|_2\le r_0).
\tag{2.6}
\]

For completeness, (2.6) follows directly from sampling without
replacement.  For every $v\in V$, Hoeffding's comparison with
independent sampling gives

\[
 \mathbb E_Ue^{t\langle v,X-\mathbb EX\rangle}
 \le e^{C_0t^2\|v\|_2^2}.
\tag{2.7}
\]

Hence all mixed third moments of unit linear forms are bounded by an
absolute constant.  Exponential tilting by a vector of norm at most
$r_0$ preserves those bounds (apply Cauchy--Schwarz and (2.7)).
The derivative of a quadratic form of the Hessian is such a mixed third
cumulant.  Taking $r_0$ small and using (2.5) proves the lower bound
in (2.6); the same moment bound proves the upper bound.

The exponential-family moment map $\nabla F$, modulo constants, maps
onto the interior of the hypersimplex.  Equivalently, the strictly convex
function

\[
 G(\theta)=F(\theta)-\langle q,\theta\rangle
\]

has a unique minimizer $\theta_*\in V$.  This can also be seen directly:
\(q_i\in(1/3,2/3)\) eventually, so \(G\) is coercive on \(V\).
On the sphere $\|\theta\|_2=r_0$, (2.6) gives

\[
 \langle\theta,\nabla G(\theta)\rangle
 \ge cr_0^2-r_0\|\varepsilon\|_2>0.
\]

Thus $\theta_*$ lies inside that sphere.  Strong monotonicity in
(2.6) now gives

\[
 \|\theta_*\|_2\le C\|\varepsilon\|_2=o(1).
\tag{2.8}
\]

Set

\[
 p_D={e^{\langle\theta_*,{\mathbf 1}_D\rangle}
       \over W e^{F(\theta_*)}}.
\tag{2.9}
\]

The critical-point equation gives (2.2).  Finally,

\[
 1+\chi^2(p\|U)
 =\exp\big(F(2\theta_*)-2F(\theta_*)\big).
\tag{2.10}
\]

Taylor's theorem and the upper bound in (2.6) show that the exponent in
(2.10) is \(O(\|\theta_*\|_2^2)=o(1)\).  This proves (2.3). \(\square\)

Apply Lemma 2.1 with $q_i=b_i/T$, and put

\[
 y_D=Tp_D,\qquad \lambda={T\over W}.
\tag{2.11}
\]

Then $y\ge0$, and it has the exact real constraints

\[
 \sum_Dy_D=T,\qquad \sum_{D\ni i}y_D=b_i.
\tag{2.12}
\]

Moreover, by (2.3),

\[
 S:=\sum_D(y_D-\lambda)^2
 ={T^2\over W}\chi^2(p\|U)=o(W).
\tag{2.13}
\]

Since \(K=W-T=o(W)\), Cauchy--Schwarz gives

\[
 A:=\sum_D|y_D-1|
 \le \sqrt{WS}+K=o(W).
\tag{2.14}
\]

This is the analytic core: the desired real load is \(o(W)\) in
$L^1$ from the all-one vector.

## 3. Integer rounding with only \(o(W)\) damage

For every \(D\), independently round \(y_D\) to one of its two adjacent
integers, with expectation \(y_D\).  Write the resulting nonnegative
integer vector as \(Z\).  If \(y_D=k+t\), \(k\in\mathbb Z_{\ge0}\) and
$0\le t<1$, then

\[
 Z_D=\begin{cases}k,&\text{with probability }1-t,\\
                    k+1,&\text{with probability }t.
       \end{cases}
\tag{3.1}
\]

Three elementary estimates are enough.  First,

\[
 \mathbb E|Z_D-1|=|y_D-1|.
\tag{3.2}
\]

Second, if (v_D=\operatorname {Var}Z_D=t(1-t)), then

\[
 v_D\le |y_D-1|,
\]

so

\[
 V:=\sum_Dv_D\le A=o(W).
\tag{3.3}
\]

Third, direct inspection of the intervals $0\le y\le1$,
$1\le y\le2$, and $y\ge2$ gives

\[
 \mathbb E\binom{Z_D}{2}
 \le (y_D-1)_+ +(y_D-1)_+^2.
\tag{3.4}
\]

Equations (2.13)--(2.14) imply

\[
 \sum_D(y_D-1)_+=o(W),
\]

and

\[
 \sum_D(y_D-1)^2
 \le2S+2K^2/W=o(W).
\]

Thus

\[
 \mathbb E\Psi(Z)=o(W).
\tag{3.5}
\]

Let

\[
 R_0=\sum_DZ_D-T,
 \qquad
 E_i=\sum_{D\ni i}Z_D-b_i.
\tag{3.6}
\]

The expectations vanish.  By (3.3),

\[
 \mathbb E|R_0|\le\sqrt V,
 \qquad
 \mathbb E|E_i|\le\sqrt V.
\tag{3.7}
\]

Since \(W=\binom{2m}m\) is exponential in \(m\),

\[
 m\sqrt V=o(W).
\tag{3.8}
\]

Combining (2.14), (3.2), and (3.5)--(3.8), there is one outcome \(Z\)
for which

\[
 \Psi(Z)+\sum_D|Z_D-1|
 +m|R_0|+\sum_i|E_i|=o(W).
\tag{3.9}
\]

The rounding is not yet exact, but only \(o(W)\) unit corrections remain.

## 4. Exact total and exact parity-free marginal correction

First correct the total.  If $R_0<0$, add one unit on $-R_0$
distinct cells currently having load one.  If $R_0>0$, delete one unit
from \(R_0\) distinct load-one cells.  Equation (3.9) leaves \(W-o(W)\)
such cells, whereas \(|R_0|=o(W)\), so this is possible.  Call the new
load \(Z'\).  It has total \(T\), still satisfies

\[
 \Psi(Z')=o(W),\qquad
 |\{D:Z'_D\ne1\}|=o(W),
\tag{4.1}
\]

and its degree-error vector

\[
 e_i=b_i-\sum_{D\ni i}Z'_D
\tag{4.2}
\]

has

\[
 \sum_ie_i=0,
 \qquad
 \|e\|_1=o(W).
\tag{4.3}
\]

The factor $m|R_0|$ in (3.9) is exactly what ensures the second
assertion in (4.3).

Pair one positive unit of $e_i$ with one negative unit of $e_j$.
For that ordered pair choose an \(m\)-set

\[
 j\in X,\qquad i\notin X,
\]

such that both

\[
 X\quad\hbox{and}\quad Y=X-\{j\}+\{i\}
\tag{4.4}
\]

currently have load one.  There are exactly

\[
 \binom{2m-2}{m-1}={Wm\over2(2m-1)}=(1/4+o(1))W
\tag{4.5}
\]

candidate pairs \(X\leftrightarrow Y\).  At every stage only \(o(W)\)
cells are nonunit, so a fresh pair satisfying (4.4) exists.

Replace one copy of \(X\) by one copy of \(Y\).  This changes the
coordinate degrees by $+e_i-e_j$, preserves total mass, and increases
$\Psi$ by exactly one.  After

\[
 {1\over2}\|e\|_1=o(W)
\]

such operations all coordinate marginals are exact.  The resulting load
\(L\) is nonnegative, satisfies (0.3), and has

\[
 \Psi(L)\le\Psi(Z')+\tfrac12\|e\|_1=o(W).
\]

This proves Theorem A.  There is no parity obstruction: after the total
is corrected, the integer error vector has coordinate sum zero, so its
positive and negative units pair exactly.  The correction (4.4) is an
oriented Johnson edge.  Equivalently, complement pairs supply the flat
background and Johnson edges supply the full root lattice of exact
marginal corrections.

## 5. What simple realization can and cannot do

If all $b_i\le W/2$, a simple load may sometimes realize the fibre by
deleting \(W-T\) distinct \(m\)-sets from the complete family.  This is
not available uniformly: legal marginals may have $b_i>W/2$, in which
case at least one duplicate is forced.  Theorem A proves the appropriate
replacement: the number of colliding unordered copies can always be made
\(o(W)\).

The proof is also stronger than a complement-pair orientation argument.
A full complement pair contributes one occurrence at every coordinate,
which explains the centre (1/2), but orientations alone cannot exceed
degree (W/2).  The sparse Johnson corrections in Section 4 handle both
signs and all exact congruences while using only \(o(W)\) collisions.

## 6. Coordinatewise flatness alone is false

This section records the sharp boundary of the theorem.

Fix a partition

\[
 [2m]=A\sqcup B,\qquad |A|=|B|=m,
\]

and let

\[
 a=\left\lfloor {cW\over\sqrt m}\right\rfloor
\]

for a fixed $c>0$.  Take $T=W$ and prescribe

\[
 b_i=\begin{cases}W/2+a,&i\in A,\\
                    W/2-a,&i\in B.
       \end{cases}
\tag{6.1}
\]

These are integer marginals with $\sum_i b_i=mW$, and

\[
 b_i=W/2+o(W)
\]

uniformly.  The fibre is nonempty: the uniform-matroid base polytope has
the integer decomposition property (equivalently, the bipartite degree
sequence with \(W\) right vertices of degree \(m\) and left degrees
$b_i$ satisfies the Gale--Ryser inequalities).

Nevertheless every nonnegative integer load in this fibre has linear
collision energy.  Let \(\mathcal A\) be the \(2m\) by \(W\) incidence
matrix of the \(m\)-sets and put \(f=L-\mathbf1\).  Since \(\sum_DL_D=W\),

\[
 \|f\|_2^2=2\Psi(L).
\tag{6.2}
\]

On the coordinate-sum-zero subspace, $\mathcal A\mathcal A^*$ has
the single eigenvalue

\[
 \alpha=\binom{2m-2}{m-1}
 ={Wm\over2(2m-1)}.
\tag{6.3}
\]

The marginal deviation is

\[
 \delta=(a,\ldots,a,-a,\ldots,-a)=\mathcal Af,
\]

so

\[
 2ma^2=\|\delta\|_2^2
 \le\alpha\|f\|_2^2=2\alpha\Psi(L).
\]

Therefore

\[
 \boxed{
 \Psi(L)\ge {2(2m-1)a^2\over W}
          =(4c^2+o(1))W.}
\tag{6.4}
\]

The example has

\[
 \sum_i(b_i/T-1/2)^2=2c^2+o(1),
\]

so it violates precisely the aggregate condition (0.2).  It also
violates the narrow side of the exact common-core interval (0.6).

## 7. Exact boundary for the constant-one program

The following load-space statement is now proved:

> Every integer singleton-marginal vector allowed by the legal
> common-core flatness interval has an exact nonnegative integer
> realization with \(\Psi=o(W)\).

Thus no obstruction depending only on total mass and singleton marginals
can refute collision rounding inside the legal box.  Conversely,
coordinatewise near-flatness without its aggregate legal content is
insufficient, by (6.4).

What remains is support-sensitive.  The vector supplied by Theorem A is
not shown to arise from one literal path at every common-core top, and the
fresh Johnson corrections do not preserve the lower- and upper-rank trace
choices.  A proof of constant one still needs either:

1. a physical lifting theorem realizing this low-collision load inside
   the common-core product support while controlling every signed trace;
   or
2. a routing theorem implementing the Section 4 corrections by legal
   boundary swaps with aggregate vertical toll \(o(W)\).

The marginal-fibre question itself is closed.
