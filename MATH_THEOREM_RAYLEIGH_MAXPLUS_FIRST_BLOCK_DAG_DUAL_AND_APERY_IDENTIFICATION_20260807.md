# The sharp Rayleigh first-block closure is exactly the all-grid Bellman gate

**Date:** 2026-08-07

**Status:** unconditional pure-mathematical identification.  The sharp
max-plus replacement for the false first-carry theta bound is the
unbounded-knapsack Bellman clock of an endpoint-saturated finite table.
It has an exact acyclic-flow dual and the standard finite-head plus
Apéry-coset normal form.  Its universal nonnegativity is therefore
exactly the existing all-grid Bellman problem, not a new easier
inequality.  No universal sign is proved here.

## 1. Exact endpoint saturation and least extension

Put

\[
 A={\sqrt\pi\over2},\qquad a=A^2={\pi\over4},
\tag{1.1}
\]

and let \(K\) be the Rayleigh signed-tail kernel.  Fix

\[
 0=y_0<y_1<\cdots<y_{h-1}\le1
\tag{1.2}
\]

satisfying

\[
 y_{i+j}\ge y_i+y_j\qquad(i+j<h).
\tag{1.3}
\]

Define

\[
 \beta(y)=
 \max\left\{1,\max_{1\le i<h}(y_i+y_{h-i})\right\},
\tag{1.4}
\]

and put

\[
 v_i=y_i\quad(1\le i<h),\qquad v_h=\beta(y).
\tag{1.5}
\]

For \(n\ge0\), let

\[
\boxed{
 L_y(n)=
 \max_{\substack{x\in\mathbb Z_{\ge0}^{h}\\
                  \sum_{i=1}^{h}ix_i=n}}
       \sum_{i=1}^{h}v_ix_i.}
\tag{1.6}
\]

### Theorem 1.1 (endpoint-saturated least clock)

The value \(\beta(y)\) is the least endpoint value which both reaches the
threshold one and completes the prefix to an internally superadditive
table.  Moreover,

\[
 L_y(n)=y_n\quad(0\le n<h),\qquad L_y(h)=\beta(y),
\tag{1.7}
\]

and \(L_y\) is the pointwise least strict superadditive clock extending
this table.

#### Proof

Let \(\pi\) be any partition of \(h\) into lower parts.  Separate one
part \(i\).  Repeated use of (1.3) bounds the weight of all remaining
parts by \(y_{h-i}\), so

\[
 \operatorname{wt}(\pi)\le y_i+y_{h-i}.
\tag{1.8}
\]

Every displayed pair is itself a partition.  Hence the best lower
partition of \(h\) has value

\[
 \max_{1\le i<h}(y_i+y_{h-i}),
\tag{1.9}
\]

which proves the endpoint assertion.

The same merging argument proves (1.7).  Combining maximizing
partitions gives

\[
 L_y(m+n)\ge L_y(m)+L_y(n).
\tag{1.10}
\]

Also \(L_y(n+1)\ge L_y(n)+y_1>L_y(n)\).  Finally, every superadditive
extension dominates the value of every partition in (1.6), and hence
dominates \(L_y\). \(\square\)

Define the sharp first-block functional

\[
\begin{aligned}
 \mathcal Q_h(y)
 ={}&h-\sum_{r=0}^{h-1}e^{-a(1-y_r)^2}\\
 &-\sum_{n\ge0}e^{-a(1+L_y(n))^2}.
\end{aligned}
\tag{1.11}
\]

Since \(L_y(n)=y_n\le1\) before \(h\), while
\(L_y(n)\ge L_y(h)\ge1\) from \(h\) onward,

\[
\boxed{
 \mathcal Q_h(y)=\sum_{n\ge0}K\!\left(A L_y(n)\right).}
\tag{1.12}
\]

Thus the sharp replacement is already a Bellman sum, not merely a lower
bound resembling one.

## 2. Exact acyclic-flow/Farkas dual

For a fixed terminal capacity \(N\), form the directed acyclic graph with
vertices \(0,1,\ldots,N\) and edges

\[
 t\longrightarrow t+i
\qquad(1\le i\le h,\ t+i\le N)
\tag{2.1}
\]

of reward \(v_i\).  Let \(f_{t,i}\) be a unit flow from zero to \(N\).
Then

\[
\boxed{
 L_y(N)=
 \max_f\sum_{t,i}v_i f_{t,i}.}
\tag{2.2}
\]

Explicitly, \(f\ge0\) sends one unit from zero to \(N\) and has zero net
flow at every intermediate vertex.  The path-flow matrix is totally
unimodular, so allowing fractional flow does not change the value.
Linear-programming duality gives the exact potential form

\[
\boxed{
\begin{aligned}
 L_y(N)=\min\;&u_N,\\
 u_0={}&0,\\
 u_{t+i}-u_t\ge{}&v_i
 \qquad(t+i\le N).
\end{aligned}}
\tag{2.3}
\]

This is the lossless finite Farkas form of the closure: primal paths are
ordered partitions, and dual potentials are Bellman supersolutions.
There is no additional linear Farkas certificate for the sign of
\(\mathcal Q_h\), because \(K\) is nonlinear and changes monotonicity
inside the compact interval.

## 3. Maximum-density Apéry normal form

Put

\[
 \lambda=\max_{1\le i\le h}{v_i\over i},
\qquad
 S=\{i:v_i=i\lambda\},
\qquad
 g=\gcd S,
\tag{3.1}
\]

and define reduced rewards

\[
 d_i=v_i-i\lambda\le0.
\tag{3.2}
\]

For \(0\le r<g\), let \(\alpha_r\) be the maximum reduced reward of a
walk from zero to \(r\) in the residue graph modulo \(g\).  A maximizing
walk can be chosen simple, because every noncritical edge has strictly
negative reduced reward.  Put

\[
 s_r=\lambda r+\alpha_r,\qquad P=g\lambda,
\qquad
 W_{qg+r}=qP+s_r.
\tag{3.3}
\]

The maximum-density Apéry theorem gives

\[
\boxed{
 L_y(n)\le W_n\quad(n\ge0),\qquad
 L_y(n)=W_n\quad(n\ge H),\qquad
 H=h(h-1).}
\tag{3.4}
\]

Consequently, with

\[
 Q_r=\max\left\{0,\left\lceil{H-r\over g}\right\rceil\right\},
\tag{3.5}
\]

the sharp functional has the exact finite-head decomposition

\[
\boxed{
\mathcal Q_h(y)
=\sum_{0\le n<H}K\!\left(A L_y(n)\right)
 +\sum_{r=0}^{g-1}\sum_{q\ge Q_r}
   K\!\left(A(qP+s_r)\right).}
\tag{3.6}
\]

Equivalently,

\[
\boxed{
\mathcal Q_h(y)
=\sum_{n\ge0}K(AW_n)
 +\sum_{0\le n<H}
   \left(K(A L_y(n))-K(AW_n)\right).}
\tag{3.7}
\]

All infinite structure is therefore a finite family of shifted Gaussian
lattices.  The only nonperiodicity is the explicit finite availability
shoulder in (3.7).

## 4. Exact comparison with the all-grid theorem

Set

\[
 c_i=A v_i\qquad(0\le i\le h).
\tag{4.1}
\]

Then \(c\) is precisely an endpoint-saturated, first-crossing,
internally superadditive table, and its all-grid Bellman clock is

\[
 V_n=A L_y(n).
\tag{4.2}
\]

Conversely, after dividing by \(A\), every strict endpoint-saturated
first-crossing table has the form (1.2)--(1.5).  Weak tables and exact
threshold equalities follow by the usual strict perturbation and
Gaussian dominated convergence.  Lowering an arbitrary first-crossing
endpoint to its saturated value can only lower the Bellman clock after
the crossing, where \(K\) is increasing.  The established first-crossing
deletion theorem, followed by endpoint saturation, therefore gives

\[
\boxed{
\mathcal Q_h(y)\ge0\text{ for every }h,y
\quad\Longleftrightarrow\quad
\text{the universal all-grid Bellman inequality}.}
\tag{4.3}
\]

Thus the max-plus repair lands exactly on the previously audited
minimal-counterexample theorem.  If (4.3) fails, choose a negative table
with minimal first-crossing size \(h\).  Positivity through grid five
forces \(h\ge6\), and the established Apéry trichotomy applies:

1. the endpoint is the unique least critical denomination and lies on
   the threshold face;
2. a lower critical denomination produces a smaller positive formal
   Apéry clock, with negativity possible only through the finite shoulder
   in (3.7); or
3. the formal subthreshold Apéry clock first crosses only back at size
   \(h\), giving the no-descent carry branch.

The sharp first-block closure therefore does not bypass any old branch.
It recovers the exact all-grid frontier in normalized coordinates.

## 5. What happens to the two-plateau theta counterexample

Take \(h=2m\) and

\[
 y_r=
 \begin{cases}
  r\varepsilon,&0\le r\le m,\\
  1-(h-r)\varepsilon,&m<r<h,
 \end{cases}
\qquad
 0<\varepsilon<{1\over h}.
\tag{5.1}
\]

Put

\[
 d=m+1,\qquad c=1-h\varepsilon>0.
\tag{5.2}
\]

The lower generators of size at most \(m\) have reward \(i\varepsilon\);
the generators of size at least \(d\), including the saturated endpoint,
have reward \(i\varepsilon+c\).  A partition of \(n\) containing \(t\)
upper generators has reward \(n\varepsilon+tc\), and the largest possible
number of upper generators is \(\lfloor n/d\rfloor\).  Therefore

\[
\boxed{
 L_y(n)=n\varepsilon+
 c\left\lfloor{n\over d}\right\rfloor.}
\tag{5.3}
\]

Writing \(n=qd+r\), \(0\le r<d\), gives the exact periodic clock

\[
 L_y(qd+r)=qP+r\varepsilon,
\qquad
 P=d\varepsilon+c=1-(m-1)\varepsilon.
\tag{5.4}
\]

Hence

\[
\boxed{
 \mathcal Q_h(y)
 =\sum_{q\ge0}\sum_{r=0}^{m}
 K\!\left(A(qP+r\varepsilon)\right).}
\tag{5.5}
\]

The unique maximum-density denomination is \(d=m+1\), and

\[
 P<1,\qquad
 P+(m-1)\varepsilon=1.
\tag{5.6}
\]

Thus the preceding theta-defect argument does not give a counterexample
to the sharp functional; after max-plus closure it gives the different
train (5.5).  This is an exact periodic long-wrap clock in the
subthreshold no-descent branch: its first crossing is delayed until the
residue \(m-1\), at the original capacity \(h=2m\).  The false
\(\Phi_{\beta}\) estimate discarded the repetition of the
higher-density size-\(d\) generator.  Formula (5.5) restores it exactly.

The sign of the delayed-crossing train (5.5) over its full parameter
range is not proved here.  It is part of the already isolated no-descent
periodic gate, rather than a new theta-prefix problem.

There is, however, a decisive sign comparison in the small-\(\varepsilon\)
regime which produced the false theta-prefix inequality.  Let

\[
 C_A=\sum_{q\ge0}K(qA)>0
\tag{5.7}
\]

be the proved ceiling-clock sum at step \(A\).  For fixed \(m\), Gaussian
dominated convergence in (5.5) gives

\[
\boxed{
 \lim_{\varepsilon\downarrow0}\mathcal Q_h(y)
 =(m+1)C_A>0.}
\tag{5.8}
\]

On the other hand, put

\[
 \delta=\Phi_1(0)+\Phi_1(1)-2
 =4\sum_{k\ge1}e^{-4\pi k^2}>0,
 \qquad
 \gamma=\Phi_1(1)-\Phi_1(0)=1-2e^{-\pi/4}.
\tag{5.9}
\]

When \(m\delta>\gamma\), the false \(\Phi_{\beta}\) margin tends to the
strictly negative Bellman lower bound \(\gamma-m\delta<0\).  Therefore
one may choose the same sufficiently small positive \(\varepsilon\) so
that

\[
 \sum_{r<h}\Phi_{\beta(y)}(y_r)>h
 \qquad\text{but}\qquad
 \mathcal Q_h(y)>0.
\tag{5.10}
\]

Thus the explicit theta counterexample is not merely inconclusive after
max-plus repair: in the regime used to disprove the relaxed target, the
exact clock passes strictly.
