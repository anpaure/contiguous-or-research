# Mean-conflict persistence: punctured triangle surplus and harmonic arrival control

Date: 2026-09-05

Status: new deterministic geometry and drift theorems, plus a sequential
positive-probability criterion. The adaptive arrival bound C.5a.7 and the
full nu conjecture remain open. This is a separate research scratch; it
does not change the master or index.

## 1. Results

1. At the complete punctured catalogue, the normalized mean conflict has
   **strictly positive** one-row drift for all sufficiently large r:
   `E[chi(H')-chi(H)] = Theta(D_M/(r Z))`. This is a punctured example,
   not an arbitrary-hypergraph counterexample. The excess is small, but
   an exact supermartingale argument for chi is false even initially.
2. Nevertheless, puncture balance gives a deterministic adaptive theorem.
   On every matching residual, the ambient ground-label first-harmonic
   projection of the normalized degree deviation has full-layer squared
   norm at most `1/(2r)` and fourth moment `O(r^-2)`. No cap, product law,
   exchangeability, or uniform-slice hypothesis is used.
3. Consequently the entire first-harmonic contribution to C.5a's arrival
   test is summable, with total `O_K(r^(-1+alpha) log r)=o(1)`.
   Only the ground-label harmonic degrees at least two remain in that
   fourth-moment route. This is a proved adaptive localization, not an
   estimate for the remaining component.
4. For a different, sequential matching law, a one-sided integrated
   triangle-minus-variance surplus of merely **constant size** suffices
   for positive-probability near-factor existence. A high-probability
   fourth-moment arrival comparison is not necessary for that criterion.
   The finite-denominator error is exponentially summable under the mean
   cap alone, despite the absence of maximum target-degree caps.

The geometric inputs imported from the master are only the definition of
the punctured catalogue, its degrees, and the proved pair inventory in
C.8. All new implications are proved here.

## 2. Triangle witnesses and the high-pair geometry

For any finite hypergraph with nonempty edges, let B be its closed conflict
matrix, let `C_F=sum_G B_FG`, and put

\[
 Z=|E|,\quad T=\sum_F C_F,\quad
 S_3=\sum_v d(v)^3,\quad \lambda_{uv}=d(\{u,v\})\quad(u\ne v).
\]

Let Lambda be the symmetric target matrix with off-diagonal entries
`lambda_uv` and zero diagonal. Then

\[
 \boxed{S_3-\sum_{\{u,v\}}\lambda_{uv}^3
       \le \operatorname{tr}(B^3)
       \le S_3+\operatorname{tr}(\Lambda^3).}                 \tag{2.1}
\]

Proof: the trace counts ordered triples of pairwise conflicting rows,
including repeated rows. Triples with a common target are counted by S_3
with multiplicity equal to their common-target count t. Their excess
`(t-1)_+` is at most `binom(t,2)`, giving the lower bound. A triple with
no common target has three distinct witnesses, one for each pairwise
intersection. Summing all choices of these witnesses counts at most
`tr(Lambda^3)` row-witness tuples, and counts every such triple at least
once. This proves the upper bound.

In the punctured catalogue, call a target pair high if it is a
middle-middle disjoint pair or a lower-middle containment pair. Write
`Lambda=P+Q`, with P supported on high pairs and Q on the other pairs.
The high-pair graph on **all targets** is triangle-free for r>=2:

- Three pairwise disjoint r-sets do not fit on 2r+1 labels.
- A nonempty (r-1)-set cannot be contained in two disjoint r-sets.
- There are no high lower-lower pairs.

This is not the separate triangle-freeness of the boundary-cut graph.
It implies `tr(P^3)=0` in every induced residual, for arbitrary current
pair-codegree weights. If

\[
 a=\|P\|_{\rm op},\quad b_0=\|Q\|_{\rm op},\quad
 h_2=\operatorname{tr}(P^2),\quad \ell_2=\operatorname{tr}(Q^2),
\]

then the following is a deterministic residual bound:

\[
 \boxed{\operatorname{tr}(\Lambda^3)
 \le 3a\sqrt{h_2\ell_2}+(3a+b_0)\ell_2.}                 \tag{2.2}
\]

Indeed, expand the trace into `3 tr(P^2 Q)+3 tr(P Q^2)+tr(Q^3)`.
Frobenius Cauchy gives
`|tr(P^2 Q)| <= ||P||op sqrt(tr(P^2) tr(Q^2))`.
Since Q^2 is positive semidefinite,
`|tr(P Q^2)| <= ||P||op tr(Q^2)`, and diagonalizing Q gives
`tr(Q^3) <= ||Q||op tr(Q^2)`.

Importantly, (2.2) is current-scale and valid without a degree cap.
Its right side must still be estimated at the actual current scale;
substituting initial degrees in a depleted residual is not legitimate.

## 3. Strictly positive initial punctured drift

Now H is the complete directed punctured catalogue, r tends to infinity,
`s=2r`, `D=D_M`, and `D_L=(r+2)D/r`. Define

\[
 a_0=s(D_M+D_L),\qquad
 \zeta={D_M^2+D_L^2\over D_M+D_L}.
\]

Row transitivity makes every C_F equal to a common c. Put `e=a_0-c`.
For a fixed row F, let S_H and S_L be the sums of codegrees over its high
and low unordered target pairs. The exact pair inventory in C.8 gives

\[
 S_H=(12+O(r^{-1}))D,\qquad S_L=O(D/r),\qquad
 \max_{u\ne v}\lambda_{uv}=O(D/r).                         \tag{3.1}
\]

Each row's high-pair graph is the union of the containment path and the
middle-disjointness path, and has maximum degree at most four. For an
intersection of t targets, its number of induced high pairs is at most
`2t <= 4(t-1)` when t>=2. Thus, including self-overlap,

\[
 \boxed{S_H/4\le e\le S_H+S_L.}                           \tag{3.2}
\]

The upper bound is `(t-1)_+ <= binom(t,2)`; the lower bound follows by
summing the preceding high-pair bound over the conflicting row.
In particular `e=Theta(D)` and `c=Theta(rD)`.

Each middle target has r+1 disjoint middle high neighbors and r contained
lower high neighbors. A lower target has r+2 high middle neighbors.
Consequently the maximum row sum of P is O(D). The row sum of Lambda at
target v is exactly `(4r-1)d(v)`. Double counting pairs inside rows gives

\[
 \|P\|_{\rm op}=O(D),\quad \|Q\|_{\rm op}=O(rD),\quad
 h_2=2ZS_H=O(ZD),\quad \ell_2=2ZS_L=O(ZD/r).
\]

Equation (2.2) proves `tr(Lambda^3)=O(ZD^2)`. Also

\[
 \sum_{\{u,v\}}\lambda_{uv}^3
 \le \Delta_2\sum_{\{u,v\}}\lambda_{uv}^2
 =\Delta_2 Z(S_H+S_L)=O(ZD^2/r).                           \tag{3.3}
\]

The incidence identities give `S_3=Za_0 zeta`, whereas `T=Zc`.
Combining (2.1), (3.2), and (3.3) proves the two-sided new estimate

\[
 \boxed{\operatorname{tr}(B^3)-T\zeta=\Theta(ZD^2)>0.}     \tag{3.4}
\]

Choose one current row uniformly and delete its targets. For general
two-shore sizes n_M,n_L define

\[
 f(n_M,n_L)={n_Mn_L\over s^2(n_M+n_L)},\qquad
 \chi=fT/Z^2.
\]

At the initial state, `Z'=Z-c` and both child shore sizes are deterministic.
The exact trace identity C.5a.8 therefore gives

\[
 {\mathbb E\chi'\over\chi}
 ={f(n_M-s,n_L-s)\over f(n_M,n_L)}
 {1-2c/Z+\operatorname{tr}(B^3)/(ZT)\over(1-c/Z)^2}.        \tag{3.5}
\]

Here `s/n_sigma=D_sigma/Z`. Expanding the explicit rational functions,
whose arguments are exponentially small, gives

\[
 {\mathbb E\chi'\over\chi}
 =1+{\operatorname{tr}(B^3)-T\zeta\over ZT}
       +O(r^2D^2/Z^2)
 =1+\Theta(D/(rZ)).                                      \tag{3.6}
\]

The error is smaller than the displayed main term since `r^3D/Z=o(1)`.
Also `chi=1-Theta(1/r)`. Hence

\[
 \boxed{\mathbb E[\chi'-\chi]=\Theta(D/(rZ))>0.}           \tag{3.7}
\]

There is a finite exact certificate without constructing B. Put
`d_0=D/Z`, `a=a_0/D`, `h=f'/f`, and
`L=(zeta/D)(S_H/D)/4-(Delta_2/D)((S_H+S_L)/D)`.
When L>0, (2.1)--(3.3) and `c<=a_0` imply

\[
 {\mathbb E\chi'\over\chi}-1
 \ge h\{(\zeta/D)d_0+Ld_0/a\}-(1-h)-(ad_0)^2             \tag{3.8}
\]

whenever the right side is positive and `ad_0<1`. Indeed, after putting
(3.5) over the denominator `(1-c/Z)^2`, its numerator minus that denominator
is `h tr(B^3)/(ZT)-(1-h)+2(1-h)c/Z-(c/Z)^2`.
Drop the positive cross term and apply the preceding bounds. The remaining
positive numerator only increases on division by `(1-c/Z)^2<=1`.
The checker certifies positivity of (3.8) by exact rational arithmetic at
r=24,48,96,192. The asymptotic proof covers all sufficiently large r.

For the parallel isolated-mark law, use the bounded observable `min(chi,2)`,
with value two at empty states. At the initial state and every one-mark
child it agrees with chi for sufficiently large r. Differentiating its
expectation at marking probability zero therefore multiplies (3.7) by Z,
so this bounded initial tangent is positive as well. One must not take an
untruncated expectation of chi with its infinite empty-state convention.
This does not assert the sign for a finite C.5a bite. It does not imply a
cap violation: the initial cap slack for a fixed K>1 is constant, and the
drift in (3.7) is very small.

## 4. An unconditional adaptive first-harmonic theorem

Fix one shore, whose target rank is k in `{r,r-1}`. Put `b=2r+1`,
`s=b-1`, and `N=binom(b,k)`. Suppose t punctured rows have been selected
as a matching. Let R be the remaining targets on this shore, including
isolated targets, so `n=N-st` and `xi=n/N`.

Take any nonempty family of current catalogue rows supported on the
remaining targets of both shores. It need not be the entire induced
catalogue. Let Z be its size, let d(A) be its degree at target A, and
let `z=sZ/n`. Define a function on the entire original k-layer by

\[
 u(A)=\mathbf1_{\{A\in R\}}(d(A)/z-1).                    \tag{4.1}
\]

Its full-layer mean is zero. Let P_1 be orthogonal projection, in the
uniform original-layer inner product, onto

\[
 \left\{A\longmapsto\sum_{i\in A}a_i:\ \sum_i a_i=0\right\}.
\]

**Theorem.** For r>=3, on every such state,

\[
 \boxed{\mathbb E_{A\in\binom{[b]}k}(P_1u(A))^2\le1/s,
 \qquad \mathbb E_{A\in\binom{[b]}k}(P_1u(A))^4=O(s^{-2}).} \tag{4.2}
\]

Moreover `-1 <= P_1u(A) <= k/(b-k) <= 1` pointwise.
The constants are absolute and do not depend on xi, the history, or Z.

### Proof by the omitted-window marginals

For each current row, let its omitted rank-k window be its dirty window.
Let p_i be the fraction of current dirty windows containing ground label i.
Let m_i be the number of selected dirty windows containing i. A full cyclic
row has exactly k rank-k windows containing i, so a punctured row has
`k-1_{i in dirty}` such targets. Thus

\[
 \sum_{A\in R:i\in A}d(A)=kZ-Zp_i,
 \qquad |\{A\in R:i\in A\}|=Nk/b-kt+m_i.                 \tag{4.3}
\]

These are literal row counts, not distributional statements. Set

\[
 q_i=\xi p_i+(s/N)m_i.
\]

Because `xi+st/N=1`, the vector q is a convex combination of dirty-window
inclusion marginals. Consequently `0<=q_i<=1` and `sum_i q_i=k`.
Subtract the two expressions in (4.3), using `z=sZ/n`, to obtain

\[
 {1\over N}\sum_A u(A)\mathbf1_{\{i\in A\}}
 ={k/b-q_i\over s}.                                      \tag{4.4}
\]

Equivalently, there is an exact positive row-mixture identity:
`u(A)+1=(N/s) E_mu 1_{A in F}`. Give each current row mass `xi/Z` and
each selected row mass `s/N`; these masses sum to one. This identity uses
disjointness of the selected rows and makes the dirty-marginal convexity
transparent. No claim that this mixture is uniform is involved.

On the zero-sum coefficient space, the Gram matrix of the coordinate
indicators on the uniform k-layer is scalar

\[
 \lambda_1={k(b-k)\over b(b-1)}.
\]

This follows directly from probabilities k/b and k(k-1)/(b(b-1)). Hence

\[
 \boxed{P_1u(A)=\sum_{i\in A}{b(k/b-q_i)\over k(b-k)}
 ={k^2-b\sum_{i\in A}q_i\over k(b-k)}.}                   \tag{4.5}
\]

The pointwise assertion follows from `0<=sum_{i in A}q_i<=k`.
Also `sum_i(q_i-k/b)^2 <= k(b-k)/b`, so (4.5) and the Gram identity
give the squared-norm bound exactly.

For completeness, the fourth moment needs no hypercontractivity theorem.
Write the coefficients in (4.5) as a_i, and set `A_j=sum_i a_i^j`.
For `p_j=(k)_j/(b)_j`, expansion by equality patterns, using `sum a_i=0`,
gives

\[
 \mathbb E\left(\sum_{i\in A}a_i\right)^4
 =(p_1-7p_2+12p_3-6p_4)A_4
       +3(p_2-2p_3+p_4)A_2^2.                            \tag{4.6}
\]

Since `b/4<=k<=b/2`, one has `max |a_i|<=4/b` and `A_2<=8/b`.
Thus `A_4<=128/b^3`, `A_2^2<=64/b^2`, and (4.6) is `O(b^-2)`.
For example, `2048/s^2` is a valid bound for r>=3. This proves (4.2).

In fact the sharp bound over all possible dirty-marginal vectors q is
obtained by taking q to be a k-set indicator. The fourth moment is convex
in q, q is a mixture of those indicators, and all indicator choices have
the same moment by label symmetry. In (4.6) this gives the exact upper
bound with

\[
 A_2={b\over k(b-k)},\qquad A_4={1\over k^3}+{1\over(b-k)^3}.
\]

Since `k=r` or `r-1` and `b=2r+1`, that bound equals
`3/s^2+O(s^-3)`. Sharpness here concerns the convex set of dirty marginals;
it does not claim that its extremizers are reached by the stopped process.

### Consequence for the actual C.5a arrival law

Put `u_{>=2}=u-P_1u` separately on each shore. It is orthogonal to constants
and every ground-label first harmonic on the original layer. Restricting
the fourth-moment bound to R gives the **deterministic** estimate

\[
 {1\over n}\sum_{A\in R}|P_1u(A)|^4\le {C\over s^2\xi}.
\]

Since `|a+b|^4<=8(|a|^4+|b|^4)`, C.5a.5 yields on every nonempty state
of lower residual density x

\[
 \boxed{T_K(H)\le {C_K\over r^2x}
  +{8\over(K-1)^2}\sum_{\sigma=M,L}{1\over n_\sigma}
    \sum_{A\in R_\sigma}|u_{\sigma,\ge2}(A)|^4.}           \tag{4.7}
\]

In the original stopped process, this holds at the raw child, before
discarding it for a new cap violation. It holds after conditioning on any
history because it is pathwise. The empty-child contribution is
`exp(-Omega(r))` by the cap-free deletion-envelope bound C.5a.4. Multiplying
by the actual arrival indicators and taking expectations is therefore
legitimate. Summing the first term of (4.7) over C.5a's `O_K(r log r)`
rounds gives

\[
 \boxed{O_K(r^{-1+\alpha}\log r)=o(1)\quad(\alpha<1).}     \tag{4.8}
\]

Thus the first-harmonic contribution is already controlled under the
adaptive arrival law. To prove C.5a.7 through (4.7), it remains sufficient
to bound only the displayed higher-harmonic empirical fourth moments at
the C.5a.7 scale. No bound for those moments is asserted here.

There is also an exact L2 localization requiring no fourth-moment
decomposition. Put `eta_sigma=z_sigma/(z_M+z_L)` and use full-layer norms
to define

\[
 H_2=\sum_\sigma{\eta_\sigma\over\xi_\sigma}
                      \|u_{\sigma,\ge2}\|_2^2.
\]

The incidence upper bound for chi and full-layer orthogonality give

\[
 \boxed{\chi\le1+H_2+{1\over sx}.}                        \tag{4.9}
\]

Indeed, `U_{2,sigma}=||u_sigma||_2^2/xi_sigma` exactly, including the
zero values on deleted targets. Thus for `sx>=2/(K-1)`, a violating child
necessarily has `H_2>(K-1)/2`. An alternative bounded arrival test is
`min(1,4H_2^2/(K-1)^2)`. Controlling its stopped expectation would suffice
for the same first-exit argument. This localizes cap failure itself, not
just an upper bound for T_K, to the higher-harmonic energy.

## 5. A weaker sequential existence criterion

Run a different process: select one current row uniformly and delete its
targets. At jump j the shore sizes are deterministic, `n_sigma=N_sigma-sj`.
Stop at lower density at most `x_*=r^-alpha` or at `chi>K`, with density
priority. No purges or other deletions are used.

For a live state put

\[
 \bar C=T/Z,\quad V_C=Z^{-1}\sum_F(C_F-\bar C)^2,\quad
 \beta=\bar C/Z,\quad \delta=\max_F C_F/Z,
\]
\[
 A(H)={\operatorname{tr}(B^3)-2ZV_C\over ZT},\quad
 \rho={f(n_M,n_L)\over f(n_M-s,n_L-s)}-1,\quad
 R(H)=[A(H)-\rho]_+.
\]

Here rho is the **exact** shore correction, not a product-law center.
Its leading term is
`(z_M^2+z_L^2)/[Z(z_M+z_L)]`.

For `delta<=1/2`, the exact finite-jump upper bound is

\[
 \boxed{\mathbb E[\chi(H')\mid H]
       \le\chi(H)\{1+R(H)+8\delta\beta\}.}                \tag{5.1}
\]

To prove it, let `L_F=T-T(H_F)>=0` and `c_F=C_F/Z`. Since
`(1-c)^-2 <= 1+2c+8c^2` for `0<=c<=1/2`,

\[
 {T-L_F\over T(1-c_F)^2}
 \le 1-L_F/T+2c_F+8c_F^2.
\]

The exact identity `sum_F L_F=2 sum_F C_F^2-tr(B^3)` cancels the mean
conflict terms on averaging. The result is `1+A(H)+8 delta beta`.
Multiplication by `f'/f=1/(1+rho)` proves (5.1). In particular, no Taylor
expansion of `L_F/T` and no bound on an individual target degree was used.

### Exponentially summable finite-size error

The rank is `q=2s`. C.5a.2 and `chi<=K` imply

\[
 \beta\le Ks^2(1/n_M+1/n_L)\le2Ks^2/n_L,\qquad
 \delta^2\le2s\beta\le4Ks^3/n_L.                         \tag{5.2}
\]

There are at most `N_L/s` jumps, and every live lower shore exceeds
`x_*N_L`. Thus, uniformly over all stopped histories,

\[
 \boxed{\sum_{j<\tau}\delta_j\beta_j
 =O_K\left({s^{5/2}\over x_*^{3/2}\sqrt{N_L}}\right)
 =e^{-\Omega(r)}.}                                      \tag{5.3}
\]

Notice that using `sum delta_j^2` instead would lose this conclusion.
The mean factor beta is essential.

The process is well defined up to its stop without a degree-floor stop:
by (5.2), every live state has `delta<1`, so the next child is nonempty.
It must either violate the cap or reach the deterministic target jump.

One also recovers the large edge-count floor under the mean cap. For one
jump, `log(Z/Z')=-log(1-c_F)` has conditional mean at most
`beta+2 delta beta` and conditional second moment at most `4 delta beta`.
The stopped martingale has total variance `exp(-Omega(r))`. Moreover,
by the harmonic-sum integral,

\[
 \sum_{j<\tau}\beta_j
 \le 2Ks\log(1/x_*)+o(1)=4K\alpha r\log r+o(1).
\]

The L2 maximal inequality, (5.3), and `log Z_0=(2+o(1))r log r` show
that, with error `exp(-Omega(r))`, every reached state satisfies

\[
 \log Z_j\ge(2-4K\alpha-o(1))r\log r.
\]

For the C.5a range `alpha<=1/(256K)`, this implies `z_M>=exp(r log r)`.
This is a sequential-law proof, not an invocation of parallel-bite descent.

### Positive-probability theorem

Let tau be the preceding stop, and let failure mean a first cap violation
strictly before the density threshold. From (5.1), stopped summation and
`chi_j<=K` on live parents give

\[
 \boxed{\Pr(\text{failure})
 \le {\chi(H_0)\over K}
       +\mathbb E\sum_{j<\tau}R(H_j)+e^{-\Omega(r)}.}      \tag{5.4}
\]

The terminal violating child is retained in this argument. At failure its
chi is greater than K, while chi is nonnegative at every other stop.
This proves (5.4) by Markov's inequality applied after telescoping.

Since `chi(H_0)<=1`, it suffices, for example, to take K=2 and prove

\[
 \mathbb E\sum_{j<\tau}R(H_j)\le1/2-\varepsilon
\]

for a fixed epsilon>0. Then the process produces a punctured matching
leaving lower density `x_*+O(s/N_L)` with probability at least
`epsilon-o(1)`. This is enough for finite-sample existence.
It does not require an `o(1)` fourth-moment arrival estimate.

A pathwise alternative follows by multiplicative compensation in (5.1):
if every stopped path obeys `sum R<=B`, then

\[
 \Pr(\text{failure})\le e^{B+o(1)}\chi(H_0)/K.             \tag{5.5}
\]

The required inequality is only `B<log(K/chi(H_0))`.
Neither integrated-surplus premise is proved for the punctured process.

## 6. Concrete remaining bottleneck

The new results do not infer adaptive law control from a product law.
They locate the remaining problem in two genuinely smaller forms:

- For the original parallel process, the stopped arrival fourth moment of
  `u_{>=2}` in (4.7). First ground-label harmonics are already harmless
  on every matching history. Quadratic and higher label geometry is not
  controlled by the puncture-balance identity.
- For the sequential existence route, the integrated positive part of
  `tr(B^3)-2Z V_C-ZT rho`. The punctured high-pair triangle exclusion
  gives (2.2), but current-scale low-pair energy and the cancellation with
  conflict variance still need adaptive control. The initial surplus is
  positive, so deleting its positive part by a claimed drift sign is invalid.

Even a near-factor from either route is not a full-nu proof by itself.
The literal restored rows must still give the distinct-window almost-cover
required by the master, either in the same dimension or at its weaker
`o(2^b)`-hole cylinder-completion interface. No tours, independent row-bank
construction, or all-depth coverage claim is made here.

## 7. Verification

The companion checker is
`scratch_gate_a_triangle_harmonic_20260905_d42b7.py`.
It checks finite-jump algebra on all simple graphs of order at most five
(with disjoint replication to make the denominators safe), the literal
punctured triangle-witness bounds at r=2,3, the exact pair-inventory lower
bound for the initial surplus at larger r, and the harmonic identities on
actual small matching residuals and arbitrary nonempty current subfamilies.
These checks supplement, rather than replace, the general proofs.

Verified run: 1,099 exact graph cases; both literal catalogues (120 and
5,040 rows); 320 exact harmonic cases; positive trace-surplus lower bounds
at r=12,24,48,96,192; and positive finite-jump drift certificates at
r=24,48,96,192. The asymptotic estimates are proved analytically above.
