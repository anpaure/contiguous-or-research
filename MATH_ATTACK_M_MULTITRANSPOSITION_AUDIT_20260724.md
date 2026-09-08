# Adversarial cross-audit of the multitransposition report

Source audited: `MATH_ATTACK_M_MULTITRANSPOSITION_REPORT_RAW_20260724.md`.

Throughout,

\[
n=2m+1,\qquad W=\binom nm=n\operatorname{Cat}_m,
\qquad N_q=\binom n{m-q},
\]

\[
W=c_qN_q+r_q,\qquad 0\le r_q<N_q,
\qquad
\beta_q=\frac{r_q(N_q-r_q)}{N_q},
\]

and $H_A=\lceil A\sqrt m\rceil$.  All assertions involving the
window $0\le q\le H_A$ are understood for sufficiently large $m$,
so that $H_A\le m-1$.  The logarithms in the word-length estimates are
natural logarithms.

## Audit verdict

The main exact calculus survives.  In particular:

1. the $F$-dependent greedy $O(n)$-term coherent-contraction word is
   proved, and its factor $1-2/n$ and quarter-contraction length are
   correct;
2. the frozen-word martingale identity has exactly the factors $1/4$
   and $1/8$ stated in the report;
3. the aggregate, rankwise, and coordinate restitution formulas and their
   ordering are exact;
4. the scalar integer-floor identity and the propagated wall-crossing
   identity are exact, including the factor
   \(\mathcal R_T^{\rm coord}/4\);
5. the annealed RFEN inequality, if assumed with the corrected quantifiers,
   gives exactly the contraction coefficient $3/4$, error coefficient
   $C_A/8$, and iterated floor $C_A/2$;
6. the conditional rigid-factor obstruction has the correct constant $6$.

There are, however, six material corrections.

- The universal $1000$-sweep expander claim is not implied merely by the
  imported symmetric-exclusion spectral-gap theorem.  It additionally
  needs a deterministic systematic-scan estimate and a numerical graph
  gap.  A complete repair is proved below.
- In line 209 of the raw report,
  \(\mathcal R_T^{\rm coord}/4\), not
  \(\mathcal R_T^{\rm coord}\), is the weighted excess variance beyond
  adjacent-integer rounding.
- The title “strictly weaker corrected target” and the assertion that the
  original FEN “can therefore be weakened” are not correct under the
  actual word quantifiers.  Original FEN and RFEN are different sufficient
  hypotheses and are not logically ordered as stated.
- The wall inequality displayed at raw lines 333--337 is not equivalent to
  annealed RFEN: it is missing an expectation over the random word.
- The quotient in raw line 301 has a $0/0$ case.  It is harmless but must
  be split off.
- “Fragmentation theorem” is only a descriptive name for an unproved,
  route-specific sufficient inequality.  Fragmentation alone is not a
  proved sufficient statistic, and the inequality is not a necessary
  characterization of MWB.

Thus the report does **not** prove FEN, RFEN, fixed-window overload, MWB, or
the contiguous-OR conjecture.  It proves exact identities and reduces this
particular heat route to the corrected unproved inequality stated in
Section 6 below.

## 1. Harmonic contraction word

### Theorem 1.1 (greedy coherent contraction)

Let $F$ be one exact middle wreath factor and let

\[
f_q=\mu_q-\frac{W}{N_q}\mathbf 1,
\qquad
\|f\|_A^2=\sum_{q=0}^{H_A}\frac{\|f_q\|_2^2}{c_q}.
\]

For every integer \(T\ge0\), there is a deterministic length-\(T\)
transposition word \(w=(\tau_1,\ldots,\tau_T)\), chosen from \(F\) and
the fixed window before any component signs are sampled, such that

\[
\|P_{\tau_T}\cdots P_{\tau_1}f\|_A^2
\le \left(1-\frac2n\right)^T\|f\|_A^2,
\qquad P_\tau=\frac{I+\tau}{2}.
\]

Consequently

\[
T_{\rm scalar}
=\left\lceil\frac{\log4}{-\log(1-2/n)}\right\rceil
\]

suffices for quarter contraction, and the convenient choice

\[
T_0=\lceil n\log2\rceil
\]

also suffices.

#### Proof

Put $r=m-q$.  Each wreath has exactly $r$ cyclic $r$-intervals
through any fixed coordinate.  Since an exact factor has
$W/n=\operatorname{Cat}_m$ wreaths,

\[
\sum_{S\ni x}\mu_q(S)=\frac{rW}{n}.
\]

The constant profile has the same point margin because

\[
\frac{W}{N_q}\binom{n-1}{r-1}=\frac{rW}{n}.
\]

Thus $U_rf_q=0$.  The Johnson point-incidence map is nonzero precisely on
$E_0\oplus E_1$, so

\[
f_q\in\bigoplus_{j\ge2}E_j.
\]

For \(v_j\in E_j\), the central average of a uniformly random coordinate
transposition is

\[
\mathbb E_\tau\tau\big|_{E_j}
=\left(1-\frac{2j(n-j+1)}{n(n-1)}\right)I.
\]

Since $P_\tau$ is an orthogonal projection,

\[
\mathbb E_\tau\|P_\tau v_j\|_2^2
=\langle v_j,\mathbb E_\tau P_\tau v_j\rangle
=\left(1-\frac{j(n-j+1)}{n(n-1)}\right)\|v_j\|_2^2.
\]

For $2\le j\le r\le m$, the function $j(n-j+1)$ is increasing on
this range and

\[
j(n-j+1)\ge2(n-1).
\]

Therefore the multiplier is at most $1-2/n$.  Summing with the positive
weights $1/c_q$ gives

\[
\mathbb E_\tau\|P_\tau f\|_A^2
\le\left(1-\frac2n\right)\|f\|_A^2.
\]

At each stage at least one transposition attains the average or better.
Choosing such a transposition greedily and applying the same argument to
the current vector proves the iterated estimate.  Finally,

\[
\left(1-\frac2n\right)^{\lceil n\log2\rceil}
\le \exp\left(-\frac2n\lceil n\log2\rceil\right)
\le\frac14.
\]

There is no missing factor of two.  \(\square\)

Two wording corrections are needed.  The word may depend on $A$, or
equivalently on the selected weighted window, as well as on $F$.
Also, $T_{\rm scalar}$ is the exact integer threshold furnished by this
scalar estimate; the report does not prove that it is the shortest possible
transposition word.

### Theorem 1.2 (repaired universal expander scan; imported-input theorem)

Let $G$ be a simple $10$-regular graph on $[n]$ whose combinatorial
Laplacian satisfies

\[
\lambda_2(L_G)\ge1.
\]

Order its $5n$ edges in any fixed order and let $S_G$ be the product of
the corresponding projections $P_e=(I+\tau_e)/2$ over one complete
sweep.  Assuming the symmetric-exclusion spectral-gap theorem, on the
mean-zero subspace of every rank space

\[
\|S_Gx\|_2^2\le\frac{648}{649}\|x\|_2^2.
\]

Hence $1000$ repeated sweeps form a universal $5000n$-term word with

\[
\|S_G^{1000}x\|_2^2<\frac14\|x\|_2^2.
\]

The same estimate holds on the weighted direct sum of these mean-zero rank
subspaces and is uniform in \(F\) and \(A\).

#### Proof of the missing systematic-scan step

Write the edges as $e_1,\ldots,e_{5n}$, put

\[
x_i=P_{e_i}x_{i-1},\qquad
a_i=(I-P_{e_i})x_{i-1},\qquad y=x_{5n},
\]

and use orthogonality of each projection to obtain

\[
D:=\|x\|_2^2-\|y\|_2^2=\sum_i\|a_i\|_2^2.
\]

Set $Q_e=I-P_e=(I-\tau_e)/2$.  Immediately after edge $e_i$ is
processed, $Q_{e_i}x_i=0$.  A later projection associated with a disjoint
edge commutes with $Q_{e_i}$ and cannot increase its norm.  A later
projection associated with an incident edge $e_k$ can increase it by at
most $\|a_k\|_2$.  Every edge in a simple $10$-regular graph has at most

\[
2(10-1)=18
\]

incident competing edges.  Therefore

\[
\|Q_{e_i}y\|_2
\le\sum_{\substack{k>i\\e_k\cap e_i\ne\varnothing}}\|a_k\|_2.
\]

Cauchy--Schwarz, followed by counting at most $18$ earlier competitors
for each $k$, gives

\[
\sum_i\|Q_{e_i}y\|_2^2\le18^2D=324D.
\]

The imported symmetric-exclusion theorem says that on every nonconstant
rank space

\[
\operatorname{gap}\left(\sum_e(I-\tau_e)\right)=\lambda_2(L_G).
\]

Thus $H_G:=\sum_eQ_e$ has gap $\lambda_2(L_G)/2$, and

\[
\frac{\lambda_2(L_G)}2\|y\|_2^2
\le\langle y,H_Gy\rangle
=\sum_e\|Q_ey\|_2^2
\le324D.
\]

It follows that

\[
\|S_Gx\|_2^2=\|y\|_2^2
\le\frac{648}{648+\lambda_2(L_G)}\|x\|_2^2.
\]

For $\lambda_2(L_G)\ge1$, this is at most $648/649$.  Moreover,
the first four nonnegative terms in the binomial expansion give

\[
\left(1+\frac1{648}\right)^{1000}
\ge1+\frac{1000}{648}
+\frac{\binom{1000}{2}}{648^2}
+\frac{\binom{1000}{3}}{648^3}>4.
\]

Hence $(648/649)^{1000}<1/4$.  A $10$-regular graph has exactly $5n$
edges, proving the term count.  \(\square\)

This repairs, but does not make self-contained, raw line 54.  The precise
scope is:

- the exclusion theorem supplies the gap of the **sum**
  \(\sum_e(I-\tau_e)\), not contraction of its ordered product;
- the systematic-scan proof above is an additional lemma;
- the number \(1000\) guarantees non-strict quarter contraction under the
  numerical gap
  \[
  \lambda_2(L_G)\ge648(4^{1/1000}-1),
  \]
  while strict contraction below \(1/4\) requires strict inequality; the
  convenient hypothesis \(\lambda_2(L_G)\ge1\) implies the latter;
- existence for every sufficiently large relevant $n$ of a simple
  $10$-regular graph with this numerical gap is a second imported input,
  absent from the raw report;
- this universal word controls only the coherent vector.  It proves no
  component-noise, wall-crossing, fragmentation, FEN, or RFEN estimate.

The expander paragraph is optional: Theorem 1.1 and the annealed iid-word
argument below already supply the coherent contraction actually used by
the heat route.

## 2. Frozen-word martingale ledger

### Theorem 2.1 (exact ledger)

Fix a transposition word $w=(\tau_1,\ldots,\tau_T)$ independently of all
component signs.  It may be deterministic, or it may first be randomly
sampled and then conditioned upon.  Let

\[
P_t=\frac{I+\tau_t}{2},\qquad
M=P_T\cdots P_1,\qquad
Q_t=P_T\cdots P_{t+1}.
\]

At time $t$, condition on the complete heat history through time $t-1$.
Assume that the current ownership components and their effects
$\delta_{t,K}$ are measurable at that time, and that the component signs
$\varepsilon_{t,K}$ are conditionally independent fair Rademachers.  Then

\[
f_t=P_tf_{t-1}+\xi_t,
\qquad
\xi_t=\frac12\sum_K\varepsilon_{t,K}\delta_{t,K},
\]

and

\[
f_T=Mf_0+\sum_{t=1}^TQ_t\xi_t.
\]

If

\[
\mathcal N_T
=\sum_{t=1}^T\mathbb E
  \sum_K\|Q_t\delta_{t,K}\|_A^2,
\]

where the outer expectation includes the earlier heat history on which the
components may depend, then exactly

\[
\boxed{
\mathbb E\|f_T-Mf_0\|_A^2=\frac{\mathcal N_T}{4}.}
\]

Consequently, with

\[
B_A=\sum_q\frac{\beta_q}{c_q},
\qquad
d=\frac12(\|Mf_0\|_A^2-B_A),
\]

one has

\[
\boxed{
\mathbb E\Psi_A(F_T)=d+\frac{\mathcal N_T}{8}.}
\]

#### Proof and factor audit

For $s<t$, $Q_s\xi_s$ is measurable before the time-$t$ signs and
$\mathbb E(\xi_t\mid\mathcal F_{t-1})=0$.  Hence all cross-time inner
products have mean zero.  Conditional independence of the signs at one
time also kills all $K\ne K'$ terms.  Therefore

\[
\mathbb E\|Q_t\xi_t\|_A^2
=\frac14\mathbb E\sum_K\|Q_t\delta_{t,K}\|_A^2.
\]

Summing proves the variance identity.  The definition of $\Psi_A$ has an
additional prefactor $1/2$, changing $1/4$ into $1/8$.  No factor is
missing.  \(\square\)

The exact-factor assertion at every leaf is valid relative to the imported
ownership-component switching theorem: a complete side choice in every
component produces a genuine integral exact factor.  The ledger itself
does not prove that structural input.

The frozen-word hypothesis is essential.  If future transpositions are
chosen after observing current signs, then $Q_t$ is not a deterministic
future suffix and the displayed multistep orthogonality need not hold.
Future **component decompositions** may adapt to the current factor: fair
heat still has conditional mean $P_s f_{s-1}$, so a word fixed in advance
is enough.

Likewise, for a deterministic suffix one cannot replace
$\|Q_t\delta^{(j)}\|^2$ by
$\alpha_j^{T-t}\|\delta^{(j)}\|^2$.  That identity is available only after
averaging a future suffix sampled independently of the current effect.

## 3. Exact floor restitution and every normalization

Put

\[
d_q=\frac{\|Mf_q\|_2^2-\beta_q}{2c_q},
\qquad d=\sum_qd_q,
\qquad D^+=\sum_q(d_q)_+,
\]

\[
u_q=\lambda_q\mathbf1+Mf_q,
\qquad \lambda_q=\frac W{N_q},
\]

and

\[
\Theta(u)=\sum_{q,S}
\frac{\{u_q(S)\}(1-\{u_q(S)\})}{c_q}.
\]

Then the raw report's three identities are exactly

\[
\mathbb E\Psi_A(F_T)
=(d)_++\frac{\mathcal R_T^{\rm agg}}8
=D^++\frac{\mathcal R_T^{\rm rk}}8
=h(u)+\frac{\mathcal R_T^{\rm coord}}8,
\]

where

\[
\mathcal R_T^{\rm agg}=\mathcal N_T-8(-d)_+,
\]

\[
\mathcal R_T^{\rm rk}
=\mathcal N_T-8\sum_q(-d_q)_+,
\]

\[
\mathcal R_T^{\rm coord}=\mathcal N_T-4\Theta(u),
\]

and

\[
h(u)=\frac12\sum_q\frac{
\|Mf_q\|_2^2+
\sum_S\{u_q(S)\}(1-\{u_q(S)\})-
\beta_q}{c_q}.
\]

The symbol $d_+$ in raw line 138 must be replaced by $(d)_+$.

### 3.1 Proof of nonnegativity and ordering

For a fixed rank define

\[
g_\lambda(x)=(x-\lambda)^2+\{x\}(1-\{x\}).
\]

On every interval $[k,k+1]$, this is affine with slope
$2k+1-2\lambda$; its slope jumps upward by $2$ at every integer.
It is therefore convex.  Since $\sum_Su_q(S)=W=N_q\lambda_q$, Jensen's
inequality gives

\[
\sum_Sg_{\lambda_q}(u_q(S))
\ge N_qg_{\lambda_q}(\lambda_q)
=\beta_q.
\]

The rank contribution $h_q$ to $h$ is consequently nonnegative.  If

\[
\Theta_q=\frac1{c_q}
\sum_S\{u_q(S)\}(1-\{u_q(S)\}),
\]

then

\[
h_q=d_q+\frac{\Theta_q}{2}\ge d_q.
\]

Thus \(h_q\ge(d_q)_+\), so \(h\ge D^+\).  Also, the
coordinatewise adjacent-integer variance bound gives
\(\mathcal N_T/4\ge\Theta(u)\), and hence
\(\mathcal R_T^{\rm coord}\ge0\); a direct proof is given in Section 3.2.
Together with

\[
\left(-\sum_qd_q\right)_+
\le\sum_q(-d_q)_+,
\]

this proves

\[
\boxed{
\mathcal R_T^{\rm agg}\ge
\mathcal R_T^{\rm rk}\ge
\mathcal R_T^{\rm coord}\ge0.}
\]

The exact differences are

\[
\mathcal R_T^{\rm agg}-\mathcal R_T^{\rm rk}
=8\left[\sum_q(-d_q)_+-\left(-\sum_qd_q\right)_+\right],
\]

and

\[
\mathcal R_T^{\rm rk}-\mathcal R_T^{\rm coord}
=8(h-D^+).
\]

All factors here are correct.

### 3.2 Scalar integer-floor identity

Let $Z$ be integer-valued with mean $u=k+\theta$, where
$k=\lfloor u\rfloor$ and $0\le\theta<1$.  Expanding around $u$ gives

\[
\mathbb E[(Z-k)(Z-k-1)]
=\operatorname{Var}(Z)-\theta(1-\theta).
\]

Therefore

\[
\boxed{
\operatorname{Var}(Z)=\theta(1-\theta)
+\mathbb E[(Z-k)(Z-k-1)].}
\]

The last integrand is nonnegative at every integer.  Thus the first term is
the minimum variance with the prescribed mean, attained by the distribution
on the two adjacent integers $k,k+1$.

Applying this coordinatewise to the terminal integral loads yields

\[
\boxed{
\frac{\mathcal R_T^{\rm coord}}4
=\frac{\mathcal N_T}{4}-\Theta(u),}
\]

which is precisely the weighted terminal variance beyond optimal
adjacent-integer rounding.  Raw line 209 is off by the factor $4$ in its
prose; its displayed formulas are correct.

The estimate

\[
\sum_{q\le H_A}\frac{N_q}{c_q}=\Theta_A(H_AW)
=\Theta_A(nH_A\operatorname{Cat}_m)
\]

also has to be interpreted narrowly.  It shows that the crude bound

\[
\Theta(u)\le\frac14\sum_q\frac{N_q}{c_q}
\]

is too large by a factor of order $n$ for the desired Catalan-scale
error.  It does **not** prove that the actual $\Theta(u)$, or its
cancellation against the martingale variance, cannot be controlled by
exact-factor structure.  Raw line 219 overstates what the scale calculation
alone establishes.

### 3.3 Compact normalization ledger

The factors of two and four can be tracked as follows:

\[
\begin{array}{c|c}
\text{quantity}&\text{exact normalization}\\ \hline
\text{one component perturbation}&
\xi_{t,K}=\varepsilon_{t,K}\delta_{t,K}/2\\
\text{propagated profile variance}&
\mathbb E\|f_T-Mf\|_A^2=\mathcal N_T/4\\
\text{contribution to }\mathbb E\Psi_A&\mathcal N_T/8\\
\text{aggregate floor subtraction}&8(-d)_+\\
\text{rankwise floor subtraction}&8\sum_q(-d_q)_+\\
\text{coordinate floor subtraction}&4\Theta(u)\\
\text{weighted excess variance}&\mathcal R_T^{\rm coord}/4\\
\text{excess-energy contribution}&\mathcal R_T^{\rm coord}/8
\end{array}
\]

No displayed normalization in the raw algebra is wrong; the error is the
single prose identification at line 209.

## 4. Harmful wall identity and the one-step parity check

### Theorem 4.1 (exact propagated integer-wall formula)

Define

\[
\phi(x)=x^2+\{x\}(1-\{x\}).
\]

For all real $b,u$,

\[
\boxed{
\frac{\phi(b+u)+\phi(b-u)}2-\phi(b)
=\sum_{\ell\in\mathbb Z}(|u|-|b-\ell|)_+.}
\]

If component signs are revealed chronologically under the hypotheses of
Theorem 2.1, and $b_{t,K,q,S}$ is the conditional terminal mean immediately
before revealing $\varepsilon_{t,K}$, then

\[
\boxed{
\frac{\mathcal R_T^{\rm coord}}4
=\mathbb E\sum_{t,K,q,S}\frac1{c_q}
\sum_{\ell\in\mathbb Z}
\left(
\frac{|(Q_t\delta_{t,K})_{q,S}|}{2}
-|b_{t,K,q,S}-\ell|
\right)_+.}
\]

#### Proof

On $[k,k+1]$, $\phi$ is the affine interpolation of $k^2$ and
$(k+1)^2$, with slope $2k+1$.  Distributionally,

\[
\phi''=2\sum_{\ell\in\mathbb Z}\delta_\ell.
\]

Integrating this atomic second derivative against the symmetric triangular
kernel of radius $|u|$ proves the first formula.

Before one sign is revealed, the two conditional terminal means of a fixed
coordinate are

\[
b\pm\frac12(Q_t\delta_{t,K})_{q,S}.
\]

The formula computes the conditional Jensen gap in $\phi$.  Summing those
gaps over the chronological reveal telescopes from $\phi(u_q(S))$ to the
expectation of $\phi$ at the terminal integral load.  Since $\phi(z)=z^2$
for integral $z$, the resulting difference is terminal variance minus
the adjacent-integer floor.  Section 3.2 identifies that difference with
\(\mathcal R_T^{\rm coord}/4\).  \(\square\)

The factor $1/2$ in the wall radius comes from the component perturbation;
the factor $1/4$ on the left is exact.  Adaptive future ownership
components cause no problem because their fair conditional mean is still
propagated by the already frozen suffix $Q_t$.

### 4.2 One-transposition parity specialization

The raw report uses $C_p$ without defining its normalization.  The exact
definition is as follows.  On a moved unordered pair
$p=\{S,\tau S\}$, let

\[
d_K=a_K(S)-a_K(\tau S),
\qquad
\ell_p=\mu(S)+\mu(\tau S).
\]

The ownership-component construction must be imported here: each component
preserves the pair sum and its two side choices give opposite effects
$(d_K,-d_K)$.  The fair pair variance is then

\[
\frac12\sum_Kd_K^2.
\]

The two coordinates have mean $\ell_p/2$, whose total adjacent-integer
variance floor is $\frac12\mathbf1_{\ell_p\ {\rm odd}}$.  Hence

\[
C_p:=\frac12\sum_Kd_K^2
-\frac12\mathbf1_{\ell_p\ {\rm odd}}.
\]

Since $a+b\equiv a-b\pmod2$,

\[
\ell_p\equiv\sum_Kd_K
\equiv\#\{K:d_K\text{ odd}\}\pmod2.
\]

It follows exactly that

\[
\boxed{
2C_p
=\sum_Kd_K^2-\mathbf1_{\sum_Kd_K\text{ odd}}
=\sum_K\left(d_K^2-\mathbf1_{d_K\text{ odd}}\right)
+2\left\lfloor
\frac{\#\{K:d_K\text{ odd}\}}2
\right\rfloor.}
\]

The displayed identity in the raw report is correct.  Its prose at line
284 needs a parity qualifier: one odd unit is forced restitution only when
the number of odd $d_K$'s is odd.  When that number is even, the pair mean
is integral and no odd unit is absorbed by the floor.  The remaining terms
measure magnitude excess and paired collisions, not fragmentation by
itself.

## 5. Rankwise contraction, RFEN, and legal iteration

### Theorem 5.1 (annealed contraction of the rankwise coherent residue)

Let $w$ be a length-$T$ word of iid uniform coordinate transpositions,
sampled independently of the heat signs.  Then

\[
\mathbb E_wD^+(w)
\le\left(1-\frac2n\right)^T\Psi_A(F).
\]

#### Proof, including the zero case

For one rank put

\[
X_q=\|f_q\|_2^2,
\qquad
Y_q=\|M_wf_q\|_2^2.
\]

Because the starting load profile is integral with total mass $W$, its
least possible squared distance from the constant vector is $\beta_q$.
Thus $X_q\ge\beta_q$.  Products of orthogonal projections give
$0\le Y_q\le X_q$.

If $X_q>0$, then

\[
(Y_q-\beta_q)_+
\le\frac{X_q-\beta_q}{X_q}Y_q.
\]

Indeed, it is trivial for $Y_q\le\beta_q$; for $Y_q>\beta_q$, the
difference between the right and left sides is
$\beta_q(1-Y_q/X_q)\ge0$.  If $X_q=0$, then
$\beta_q=Y_q=0$, so the desired contribution is zero.  This separately
resolves the $0/0$ omitted in raw line 301, in particular at $q=0$.

Conditioning one iid transposition at a time and using Theorem 1.1's
one-step average gives

\[
\mathbb E_wY_q\le\left(1-\frac2n\right)^TX_q.
\]

After division by $2c_q$ and summation,

\[
\mathbb E_wD^+(w)
\le\left(1-\frac2n\right)^T
\sum_q\frac{X_q-\beta_q}{2c_q}
=\left(1-\frac2n\right)^T\Psi_A(F).
\]

This proves the claim.  \(\square\)

At $T=T_0=\lceil n\log2\rceil$, this is at most
$\Psi_A(F)/4$.

### Correct unproved RFEN statement

The precise all-factor hypothesis sufficient for iteration is:

> **RFEN\(_A\) (UNPROVED).**  For every fixed \(A>0\), there exist constants
> $C_A<\infty$ and $m_A$ such that for every $m\ge m_A$ and every
> exact middle wreath factor $F$, if $w$ is an iid-uniform
> length-$T_0$ transposition word sampled independently and frozen before
> all component signs, then
> \[
> \mathbb E_w\mathcal R_{T_0}^{\rm rk}(F,w)
> \le4\Psi_A(F)+C_AH_A\operatorname{Cat}_m.
> \]

For every frozen word,

\[
\mathbb E_\varepsilon[\Psi_A(F_T)\mid w]
=D^+(w)+\frac18\mathcal R_{T_0}^{\rm rk}(F,w).
\]

Theorem 5.1 and RFEN therefore give exactly

\[
\boxed{
\mathbb E_{w,\varepsilon}\Psi_A(F_T)
\le\frac34\Psi_A(F)
+\frac{C_A}{8}H_A\operatorname{Cat}_m.}
\]

The arithmetic is

\[
\frac14\Psi_A+\frac18(4\Psi_A+C_AH_A\operatorname{Cat}_m)
=\frac34\Psi_A+\frac{C_A}{8}H_A\operatorname{Cat}_m.
\]

No factor of two is missing.

### 5.2 The missing expectation in the wall formulation

Pointwise in a frozen word,

\[
\mathcal R_T^{\rm rk}
=\mathcal R_T^{\rm coord}+8(h-D^+).
\]

Writing $J_{\rm wall}=\mathcal R_T^{\rm coord}/4$, this becomes

\[
\mathcal R_T^{\rm rk}
=4\bigl[J_{\rm wall}+2(h-D^+)\bigr].
\]

Consequently annealed RFEN is **exactly equivalent** to

\[
\boxed{
\mathbb E_w\left[
J_{\rm wall}(w)+2\bigl(h(w)-D^+(w)\bigr)
\right]
\le\Psi_A(F)+\frac{C_A}{4}H_A\operatorname{Cat}_m.}
\tag{Wall-RFEN\(_A\), UNPROVED}
\]

The expectation $\mathbb E_w$ is absent from raw lines 330--338.  The
unaveraged inequality, if required for every word, is a stronger quenched
sufficient condition.  If it is required merely for the existence of some
word, it still does not by itself yield the RFEN contraction: one must also
control $D^+(w)$ for that same word.  Theorem 5.1 controls $D^+$ only
after iid-word averaging.

### 5.3 Original FEN and RFEN are not ordered under their word quantifiers

For a fixed word,

\[
\mathcal R_T^{\rm rk}\le\mathcal R_T^{\rm agg}.
\]

That pointwise inequality does not justify the heading “strictly weaker” or
the sentence at raw line 310.  The hypotheses being compared are:

- original FEN selects one deterministic word, depending on the current
  factor, which simultaneously quarter-contracts the aggregate coherent
  norm and bounds the aggregate remainder;
- RFEN averages the rankwise remainder over an iid-uniform random word and
  uses the separate annealed rankwise contraction of Theorem 5.1.

An existential good deterministic word does not control the iid-word
average, so original FEN does not imply RFEN.  Conversely RFEN controls
neither the aggregate remainder nor one preselected greedy word, so RFEN
does not imply original FEN.  They are different unproved sufficient
targets.  Only after matching the word quantifiers could the pointwise
ordering of remainders be used.

### 5.4 Integral leaf selection and iteration

The annealed argument is legal.  From

\[
\mathbb E_w\left[
\mathbb E_\varepsilon(\Psi_A(F_T)\mid w)
\right]\le B
\]

there is a deterministic word $w_F$, depending on the current $F$, for
which the conditional sign average is at most $B$.  Freeze that word;
then at least one of its integral exact-factor leaves has energy at most
$B$.  At the next macrostep a new word may be selected from the already
chosen factor.  No word is adapted inside a macrostep.

Thus RFEN implies a sequence satisfying

\[
x_{k+1}\le\frac34x_k+\frac{C_A}{8}H_A\operatorname{Cat}_m,
\qquad x_k=\Psi_A(F_k),
\]

and hence

\[
x_k\le\left(\frac34\right)^kx_0
+\frac{C_A}{2}H_A\operatorname{Cat}_m.
\]

The initial bound in the raw report is correct.  A proper subset can occur
as a cyclic interval at most once in one wreath, and there are
$\operatorname{Cat}_m=W/n$ wreaths, so

\[
0\le\mu_q(S)\le\frac Wn,
\qquad \sum_S\mu_q(S)=W.
\]

Therefore

\[
\sum_S\mu_q(S)^2\le\frac{W^2}{n},
\qquad
\|f_q\|_2^2
=\sum_S\mu_q(S)^2-\frac{W^2}{N_q}
\le\frac{W^2}{n}.
\]

The $q=0$ term vanishes, $c_q\ge1$, and $\beta_q\ge0$, giving

\[
\boxed{\Psi_A(F_0)\le\frac{H_AW^2}{2n}.}
\]

For

\[
k=\left\lceil\log_{4/3}(W/2)\right\rceil,
\]

one has $(3/4)^k\le2/W$, so

\[
x_k\le
H_A\operatorname{Cat}_m
+\frac{C_A}{2}H_A\operatorname{Cat}_m
=O_A(H_A\operatorname{Cat}_m)
=O_A(W/\sqrt m)=o(W).
\]

Since \(\log W=\Theta(n)\), there are \(O(n)\) macrosteps.  Each contains
$T_0=O(n)$ transpositions, so the total is $O(n^2)$.  This correctly
incorporates the first-wave correction that one $O(n)$-step word gives
only a constant contraction, not contraction all the way to the Catalan
floor.

### 5.5 Exact implication scope

For integer loads,

\[
\Phi_q
=\frac12(\|f_q\|_2^2-\beta_q)
=\frac12\sum_S
(\mu_q(S)-c_q)(\mu_q(S)-c_q-1),
\]

and the overload satisfies $O_q\le\Phi_q$.  Hence the conditional bound
above implies

\[
\sum_{q\le H_A}\frac{O_q}{c_q}
\le\Psi_A=o(W)
\]

for every fixed $A$.  With constants $C_A$ independent of $m$, the
audited diagonalization yields MWB on a slowly growing Gaussian window.
The frozen exact-factor-to-literal-word and tail theorems then yield the OR
conclusion.  These latter transfers are imported results, not reproved in
the lane-M report.

The correct implication is therefore

\[
\boxed{
\text{all-factor RFEN for every fixed }A
\Longrightarrow
\text{fixed-window overload}
\Longrightarrow
\mathrm{MWB}
\Longrightarrow
\text{the audited literal OR bound}.}
\]

Every arrow here is conditional on its stated imported theorem.  There is
no converse proved.  In particular RFEN is not a necessary characterization
of MWB, and nothing in this route proves labelled common-owner
synchronization.

For every fixed \(A\), a minimizer-only version of RFEN is enough provided
there are constants \(C_A<\infty\) and \(m_A\) such that, for every
\(m\ge m_A\), RFEN holds at one chosen global minimizer
\(F^*_{m,A}\) with that same \(C_A\).  Every terminal leaf then has energy
at least \(\Psi_{\min}\), and therefore

\[
\Psi_{\min}
\le\frac34\Psi_{\min}
+\frac{C_A}{8}H_A\operatorname{Cat}_m,
\]

so

\[
\Psi_{\min}\le\frac{C_A}{2}H_A\operatorname{Cat}_m.
\]

The factor may depend on the pair \((m,A)\).  The same minimum argument works
for original same-word FEN with its own correct quantifier.  Thus raw line
395 should say “RFEN (and likewise original same-word FEN)” instead of
silently switching names.  If an all-factor hypothesis holds, minimizing
inside a heat communicating class bounds that class's **minimum**; it does
not bound every factor or the stationary class mean.

## 6. Obstruction and the actual unproved structural gate

### 6.1 Conditional rigid-factor obstruction

Suppose $F$ has connected ownership overlay with $\tau F$ for every
coordinate transposition $\tau$.  This property persists under coordinate
relabeling.  A connected overlay has one component, so each heat step has
only the two global leaves $F'$ and $\tau F'$.  Inductively every leaf of
every word is a coordinate relabeling of $F$, and
$\Psi_A$ is constant on all leaves.

For a quarter-contracting word write

\[
X=\|f\|_A^2,
\qquad
B=\sum_q\frac{\beta_q}{c_q},
\qquad
Y=\|Mf\|_A^2\le\frac X4.
\]

Then

\[
\Psi_A(F)=\frac{X-B}{2},
\qquad
d=\frac{Y-B}{2}
\le\frac{\Psi_A(F)}4-\frac{3B}{8}
\le\frac{\Psi_A(F)}4.
\]

Hence $(d)_+\le\Psi_A(F)/4$, and the aggregate identity gives

\[
\boxed{
\mathcal R_T^{\rm agg}
=8(\Psi_A(F)-(d)_+)\ge6\Psi_A(F).}
\]

Thus a coefficient-$4$ original FEN bound fails for such a factor whenever

\[
\Psi_A(F)>\frac{C_A}{2}H_A\operatorname{Cat}_m.
\]

There is also an annealed RFEN version.  For every frozen word, rigidity
and the rankwise identity give

\[
\mathcal R_T^{\rm rk}(w)=8(\Psi_A(F)-D^+(w)).
\]

Now let \(w\) be an iid-uniform word of length
\(T_0=\lceil n\log2\rceil\).  Using Theorem 5.1,

\[
\boxed{
\mathbb E_w\mathcal R_T^{\rm rk}(w)
=8\left(\Psi_A(F)-\mathbb E_wD^+(w)\right)
\ge6\Psi_A(F).}
\]

So the same hypothetical factor defeats all-factor RFEN above the same
threshold.  To refute an asymptotic theorem with an unspecified finite
$C_A$, one would need a sequence of genuine rigid exact factors whose
ratio

\[
\frac{\Psi_A(F_m)}{H_A\operatorname{Cat}_m}
\]

is unbounded.  No such factor or sequence is known.  This is a conditional
obstruction to a proof method, not a counterexample to FEN, RFEN, MWB, or
the OR conjecture.

### 6.2 What “fragmentation theorem” can legitimately mean

The exact remaining all-factor statement in this lane is the already boxed
unproved annealed inequality

\[
\mathbb E_w\left[
J_{\rm wall}(w)+2(h(w)-D^+(w))
\right]
\le\Psi_A(F)+\frac{C_A}{4}H_A\operatorname{Cat}_m.
\tag{*}
\]

It simultaneously controls:

- propagated component effects that cross integer walls;
- the gap between coordinatewise floor restitution and rankwise floor
  restitution;

It does **not** control cross-rank cancellation.  That term is exactly
\[
\mathcal R_T^{\rm agg}-\mathcal R_T^{\rm rk}
=8\left[\sum_q(-d_q)_+
-\left(-\sum_qd_q\right)_+\right],
\]
and it was removed when the target passed from aggregate FEN to rankwise
RFEN.

Calling (*) an “exact-factor fragmentation/anti-cancellation theorem” is
acceptable shorthand only if the following scope is stated explicitly.

1. (*) is **unproved**.
2. It is equivalent to RFEN only with the expectation over iid words.
3. It is a sufficient route-specific statement, not a necessary theorem
   characterizing MWB.
4. Component fragmentation by itself is not a known sufficient statistic.
   The one-step formula depends on signed magnitude and on collisions of
   odd component effects, and first-wave occurrence-pair identities show
   that separating occurrences may help or hurt according to their target
   correlation.
5. Failure of (*) at one exact factor would not disprove MWB, which is an
   existential statement about finding some good factor.

The other Section 7 warnings have the following precise status.

- Point-regular higher-harmonic integer profiles can make all one-step
  parity-corrected ideal gains vanish, but these are histogram relaxations,
  not proved exact-factor profiles and not exact-factor counterexamples.
- Repeating a transposition consecutively kills its earlier antisymmetric
  noise, but an intervening noncommuting projection can recreate a component
  in that antisymmetric direction.  Thus the palindrome warning is correct.
- Noise born in the final expander sweep has no later **complete** sweep
  giving uniform contraction.  Earlier positions in that final sweep may
  still be filtered by its remaining suffix; only the final update is wholly
  unfiltered.
- Signed octahedral lifts have no positivity, squarefreeness, disjoint
  middle support, or exact-factor packing guarantee.  They obstruct a
  spectral/lattice-only proof, not RFEN on genuine factors.

## 7. Line-level correction list

For direct revision of the raw report:

1. Lines 38--44: say that the greedy word depends on $F$ **and the fixed
   weighted window $A$** and is frozen before signs.
2. Lines 46--51: replace “exact sufficient length” by “exact integer
   threshold supplied by the scalar contraction estimate.”
3. Line 54: insert the numerical expander-gap hypothesis, the systematic
   scan lemma, and the expander-family existence input from Theorem 1.2.
4. Lines 73--91: state conditional sign independence, predictability of
   component effects, and the expectation over earlier heat histories.
5. Line 106: retain the warning about deterministic suffixes; it is correct.
6. Line 138: replace $d_+$ by $(d)_+$.
7. Line 209: replace $\mathcal R_T^{\rm coord}$ by
   $\mathcal R_T^{\rm coord}/4$ in the prose identification.
8. Lines 211--219: say that the **trivial coordinatewise allowance** is too
   large, not that structural coordinate restitution is impossible to
   absorb.
9. Lines 265--284: define $C_p$, import pair-sum preservation, and qualify
   the “one odd unit” sentence by the parity of the number of odd $d_K$'s.
10. Lines 286 and 310: replace “strictly weaker” by “different annealed
    sufficient target with a pointwise smaller remainder.”
11. Lines 296--302: split off $X_q=0$.
12. Lines 330--338: insert $\mathbb E_w$ around the entire wall expression.
13. Lines 343--382: prefix the conclusion by “conditional on RFEN with the
    all-factor quantifiers above,” and state $H_A\le m-1$.
14. Line 395: write “RFEN (and likewise original same-word FEN), at one
    global minimizer for each \((m,A)\), with one finite \(C_A\) working
    for all sufficiently large \(m\).”
15. Line 405: replace $d_+$ by $(d)_+$.
16. Lines 416--426: label (*) explicitly as **UNPROVED** and
    route-specific; do not present fragmentation alone as the formal gate.

## Final audited theorem inventory

**Proved inside the lane, relative to the standard exact-factor heat
operation:**

- the $F,A$-dependent $O(n)$ coherent-contraction word;
- conditional on the imported exclusion theorem and a \(10\)-regular graph
  with \(\lambda_2(L_G)\ge1\), the universal \(5000n\)-term
  quarter-contraction word;
- the exact frozen-word martingale ledger;
- the full restitution hierarchy;
- the scalar adjacent-integer floor identity;
- the propagated lattice-wall identity;
- the iid-word contraction of $D^+$;
- the legality and constants of RFEN iteration, conditional on RFEN;
- the rigid-factor lower bound, conditional on existence of a rigid factor.

**Imported and requiring explicit scope:**

- exact middle wreath factors and legal ownership-component switches;
- the Johnson/Specht transposition eigenvalue formula;
- the symmetric-exclusion spectral-gap theorem;
- for the optional universal word, an expander family with a numerical
  Laplacian gap;
- the diagonal overload-to-MWB theorem and the literal transfer/tail
  theorems.

**Unproved:**

- RFEN\(_A\);
- equivalently, Wall-RFEN\(_A\) with the required iid-word expectation;
- any exact-factor fragmentation/anti-cancellation theorem implying that
  inequality;
- existence of a high-energy transposition-rigid exact-factor family.

The decisive unresolved step is therefore not harmonic contraction and not
an integer normalization.  It is the positive-fibre, exact-factor estimate
(*) controlling propagated wall crossings together with the rank/coordinate
floor gap.

An independent second audit separately checked the greedy and expander
constants, the martingale/restitution/wall chain, and the RFEN/iteration
implications.  After the scope corrections recorded above, it found no
further mathematical defect.
