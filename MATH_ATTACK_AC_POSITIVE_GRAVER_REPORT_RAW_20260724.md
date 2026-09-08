The lane yields a genuine positive augmentation theorem, but not MWB itself. The exact obstruction is now clean: Graver theory gives legal monotone descent once a better exact factor exists; signed saturation does not supply that positive endpoint. In fact, some perfectly regular balanced quota targets are not even fractionally realizable.

## 1. Support-feasible lifted-Graver descent

Let \(A=A_m\), \(B_H=\bigoplus_{q\le H}A_{m-q}\), and

\[
\mathfrak F_m=\{x\in\mathbb Z_{\ge0}^{\Omega}:Ax=\mathbf1\}.
\]

Every \(x\in\mathfrak F_m\) is automatically a \(0/1\) exact factor indicator and has

\[
|\operatorname{supp}x|=\operatorname{Cat}_m=\frac Wn.
\]

For \(\mu=B_Hx\), define the weighted floor energy

\[
E_H(x)=
\sum_{q=1}^H\frac1{2c_q}
\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\]

It satisfies

\[
E_H(x)\ge \sum_{q\le H}\frac{O_q(x)}{c_q},
\]

and vanishes exactly when every lower load is \(c_q\) or \(c_q+1\).

Introduce the lifted matrix

\[
\mathcal M_H=
\begin{pmatrix}
A&0\\
B_H&-I
\end{pmatrix}.
\]

**Theorem 1 — exact conformal augmentation.**  
For every \(m\), \(1\le H\le m-2\), and exact factors \(x,x^\star\) with \(E_H(x^\star)<E_H(x)\), there is an applicable \(g=(p,B_Hp)\in\operatorname{Gr}(\mathcal M_H)\) such that \(x+p\) is an exact factor and

\[
E_H(x)-E_H(x+p)
\ge
\frac{E_H(x)-E_H(x^\star)}
{|\operatorname{supp}x\setminus\operatorname{supp}x^\star|}
\ge
\frac{E_H(x)-E_H(x^\star)}{\operatorname{Cat}_m}.
\tag{1}
\]

**Proof.** Conformally decompose

\[
(x^\star-x,B_Hx^\star-B_Hx)=g_1+\cdots+g_t
\]

into lifted Graver elements. Since \(x^\star-x\in\{-1,0,1\}^{\Omega}\), every projected summand is squarefree, and \(x+p_i\ge0\). Its middle equation is still \(A(x+p_i)=\mathbf1\), so it is an exact factor.

Every nonzero \(p_i\in\ker A\) has both signs because all columns of \(A\) have sum \(n\). The negative supports of different summands are disjoint, giving

\[
t\le|\operatorname{supp}x\setminus\operatorname{supp}x^\star|
\le\operatorname{Cat}_m.
\]

For one lower coordinate, with increments \(\delta_i\) of a common sign,

\[
\begin{aligned}
&E_H\!\left(\mu+\sum_i\delta_i\right)-E_H(\mu)
-\sum_i\bigl(E_H(\mu+\delta_i)-E_H(\mu)\bigr)\\
&\qquad=
\sum_{q,S}\frac1{c_q}\sum_{i<j}
\delta_{i,qS}\delta_{j,qS}\ge0.
\end{aligned}
\]

Thus the sum of the individual energy changes is at most
\(E_H(x^\star)-E_H(x)<0\), proving (1). ∎

Consequences:

- Local minima under the full lifted Graver basis are exactly global energy minima.
- Every projected move is a support-feasible union of complete middle-ownership components.
- If a zero-energy exact factor exists, every factor reaches zero through at most \(\operatorname{Cat}_m\) strict conformal Graver descents.
- The move may contain an entire factor. No sub-factor-scale support bound follows.

The last qualification is essential. Lifted Graver minimality may force many ordinary ownership components to be bundled because their lower-rank effects cancel in every proper split.

## 2. Exact overload, rather than the stronger quadratic energy

The same construction applies directly to the MWB objective.

Write \(W=c_qN_q+r_q\). Introduce nonnegative integral variables

\[
h_q+s_q=\mathbf1,\qquad \mathbf1^\top h_q=r_q,
\]

and

\[
B_qx-h_q-p_q+d_q=c_q\mathbf1.
\]

Thus \(h_q\) selects the \(r_q\) high quotas, while \(p_q,d_q\) record surplus and deficit. For fixed \(x\),

\[
\min_{h_q,p_q,d_q}\mathbf1^\top p_q=O_q(x).
\tag{2}
\]

Indeed, writing \(\delta_S=\mu(S)-c_q\), \(T=\sum_{\delta_S\ge1}\delta_S\), and \(a=\#\{\delta_S\ge1\}\),

\[
\min\mathbf1^\top p_q
=T-\min(r_q,a)
=\max(T-r_q,T-a)
=\max(D_q^-,D_q^+).
\]

Let

\[
J(x,h,p,d)=\sum_{q\le H}\frac{\mathbf1^\top p_q}{c_q}.
\]

**Theorem 2 — exact-overload Graver descent.**  
If the auxiliary variables are chosen optimally for the current factor \(F\), and \(F\) is not globally optimal for \(J\), an applicable Graver move of the extended equality matrix changes \(x\) to another exact factor \(F'\) with

\[
J(F')-J^\star
\le
\left(1-\frac1{\operatorname{Cat}_m}\right)
\bigl(J(F)-J^\star\bigr).
\tag{3}
\]

Moreover, a global optimum is reachable through at most
\(\operatorname{Cat}_m\) strict factor-changing Graver moves.

The proof is linear: in a conformal decomposition toward a global optimizer, every summand has nonpositive objective change, since omitting a positive summand would beat the optimum. Summands with zero \(x\)-part have nonnegative change by fixed-\(x\) optimality, hence zero. At most \(\operatorname{Cat}_m\) remaining summands change \(x\).

For \(H=H_A\),

\[
J^\star=W\beta_m(A).
\]

Thus this theorem eliminates false local minima for the exact MWB objective, but gives no upper bound on \(J^\star\).

## 3. Exact semigroup interpretation

The zero-overload system is obtained by setting \(p_q=d_q=0\). Its fixed right-hand side is always:

- in the rational cone, using the uniform fractional exact factor and
  \(h_q=(r_q/N_q)\mathbf1\);
- in the integer lattice, using any exact factor with signed
  \(h_q=B_qx-c_q\mathbf1\).

Therefore:

\[
\boxed{
\text{No perfectly balanced exact factor}
\iff
\text{the zero-overload right-hand side is a genuine semigroup hole.}
}
\]

The optimum \(J^\star\) is precisely the weighted repair cost of that possible hole. MWB asks that this repair cost be \(o(W)\), not that the hole disappear completely.

For a preassigned integral quota tuple \(b\), the situation is worse: signed saturation gives \((\mathbf1,b)\) in the integer lattice, but it need not lie in the rational cone.

## 4. Universal containment cuts and an explicit cone obstruction

Let \(r=m-q\) and \(\mathcal U\subseteq\binom{[n]}r\). Put

\[
\partial_q^+\mathcal U
=
\{M\in\tbinom{[n]}m:\exists R\in\mathcal U,\ R\subseteq M\}.
\]

**Theorem 3 — containment cut.**  
Every fractional exact factor satisfies

\[
\boxed{\mu_q(\mathcal U)\le|\partial_q^+\mathcal U|.}
\tag{4}
\]

For one cyclic order, every cyclic \(r\)-interval has exactly \(q+1\) cyclic \(m\)-extensions, while every cyclic \(m\)-interval has exactly \(q+1\) cyclic \(r\)-subintervals. Counting these order-specific incidences proves the columnwise inequality; summing with nonnegative factor weights and \(A_mx=\mathbf1\) gives (4).

Hence a balanced target \(c_q\mathbf1+\mathbf1_{\mathcal H}\) must obey

\[
c_q|\mathcal U|+|\mathcal H\cap\mathcal U|
\le|\partial_q^+\mathcal U|.
\tag{5}
\]

Point margins alone do not imply these cuts.

**Theorem 4 — regular balanced targets outside the cone.**  
Let \(n=2m+1\) be a sufficiently large odd prime and

\[
a=\lceil2\log_2n\rceil,\qquad 2a<m-2.
\]

At depth one, put \(r=m-1\), \(N=\binom nr\), and let \(\mathcal U\) be all \(r\)-sets containing some cyclic \(a\)-block in a fixed ground cycle. Then

\[
|\mathcal U|
\le n\binom{n-a}{r-a}
<\frac Nn.
\tag{6}
\]

Furthermore,

\[
|\partial^+\mathcal U|
\le\frac{m+2}{m-a}|\mathcal U|
<2|\mathcal U|.
\tag{7}
\]

Here (7) follows because every \(R\in\mathcal U\) has \(m+2\) upper neighbors, while every shadow member contains at least \(m-a\) members of \(\mathcal U\).

At depth one, \(c_1=1\) and the number of high quotas is

\[
d=W-N=\frac{2N}{m}>|\mathcal U|.
\]

All nontrivial subset orbits under cyclic translation have size \(n\). Thus \(\mathcal U\) extends by whole orbits to a cyclic-invariant, hence point-regular, high family \(\mathcal H\) of size \(d\). Set

\[
b_1=1+\mathbf1_{\mathcal H}.
\]

This is a valid regular floor/ceiling quota, but it violates (5):

\[
b_1(\mathcal U)=2|\mathcal U|
>|\partial^+\mathcal U|.
\]

Consequently,

\[
\boxed{(\mathbf1,b)\in\text{signed lattice}\setminus\text{fractional cone}.}
\tag{8}
\]

Other depths can simultaneously be assigned cyclic-orbit regular quotas; the separator ignores them.

There is also a quantitative negativity certificate. Put

\[
\Delta=2|\mathcal U|-|\partial^+\mathcal U|
\ge
\frac{m-2a-2}{m-a}|\mathcal U|.
\]

Every signed lift \(y\) of this target satisfies

\[
\|y^-\|_1\ge\frac{\Delta}{n}
=\Omega\!\left(\frac W{n^3}\right).
\tag{9}
\]

Therefore any coefficient-one Petr–Turek selector expression reaching this deliberately chosen target uses
\(\Omega(W/n^3)\) cells, counting multiplicity.

This is not a counterexample to MWB: another jointly selected quota may lie in the cone or semigroup.

## 5. Mesoscopic locality is unavoidable for selector positivization

Independently of the preceding cone obstruction, a nonzero connected support-feasible composite of \(s\) Petr–Turek selector cells satisfies

\[
\boxed{s\ge\left\lceil\frac{m+1}{2}\right\rceil.}
\tag{10}
\]

One adjacent swap changes two middle intervals, so

\[
|\mathcal W_m(C)\cap\mathcal W_m(D)|
\ge n-2d_\circ(C,D).
\]

Middle-disjoint orders therefore have \(d_\circ(C,D)\ge m+1\). A selector cell has diameter at most two, and a connected \(s\)-cell union has diameter at most \(2s\). If \(2s\le m\), each sign of a support-feasible trade contains at most one surviving order; equality of the two middle-incidence columns then forces the zero trade.

This is only a selector-cell bound. Genuine nonlocal MSW \(2\)-for-\(2\) trades exist, and arbitrary lifted-Graver moves are not proved to have \(\Omega(m)\) wreath support.

## Final scope

What is proved:

- exact support-feasible Graver descent for weighted floor energy;
- an exact \(1/\operatorname{Cat}_m\) global-gap improvement bound;
- exact Graver descent for the true weighted overload objective;
- a genuine semigroup-hole formulation with overload as repair cost;
- universal fractional containment cuts;
- explicit regular balanced targets outside the cone;
- exact mesoscopic selector lower bounds.

What remains unproved is precisely a global positivity estimate such as

\[
E_{H_A}^\star
=O_A(H_A\operatorname{Cat}_m)=o(W),
\]

or, at the exact MWB level,

\[
J_{H_A}^\star=o(W)
\qquad\text{for every fixed }A.
\]

The Graver theorem is comparison-based and cannot supply either bound from signed saturation. This lane remains entirely unlabelled; it constructs no common balanced nested owner resolution and makes no reverse implication from MWB to labelled synchronization.
