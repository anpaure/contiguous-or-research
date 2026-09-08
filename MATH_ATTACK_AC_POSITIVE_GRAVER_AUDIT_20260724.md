# Independent adversarial audit of MATH_ATTACK_AC_POSITIVE_GRAVER_REPORT_RAW_20260724.md

## 1. Verdict

The report's principal mathematical conclusions survive:

1. the lifted floor-energy Graver augmentation theorem is correct, including its exact \(1/\operatorname{Cat}_m\) gap bound;
2. the auxiliary formulation gives the true overload \(O_q\), and the linear Graver contraction is correct after auxiliary reoptimization;
3. the mobile-quota zero-overload system has the stated cone/lattice/semigroup interpretation;
4. the containment cuts hold for every fractional exact factor;
5. the prime-dimensional construction gives a cyclic-invariant, point-regular balanced quota outside the fractional cone;
6. the signed-negativity estimate is correct after adding one omitted lower bound for \(|\mathcal U|\); and
7. the selector-cell locality bound is correct under explicit connectivity, support-feasibility, and unoriented-wreath conventions.

No result here proves MWB. The Graver results are comparison theorems: once a better positive exact factor exists, they produce a legal improving move. They do not bound the optimum or produce the better endpoint. The explicit bad quota is preassigned and therefore does not obstruct choosing the quota jointly with the factor.

Required corrections and qualifications are:

- Squarefreeness and ownership-component structure apply to lifted Graver moves applicable at an exact-factor vertex, not to arbitrary lifted Graver elements.
- The proof gives no sub-factor support bound, but it does not exhibit a factor-scale or many-component lifted Graver element in the fixed window.
- The exact-overload contraction is for
  \[
  \bar J(F):=\min_{h,s,p,d}J(F,h,s,p,d)
  =\sum_{q\le H}\frac{O_q(F)}{c_q},
  \]
  after reoptimizing the auxiliaries.
- The mobile-\(h\) semigroup cone and the raw cone for a fixed prescribed quota \(b\) are different. The fixed-\(b\) example is in lattice minus cone, not a semigroup hole.
- Signed saturation applies only to prescribed quotas with the correct totals and point margins.
- The claimed \(\Omega(W/n^3)\) separation needs a lower bound on \(|\mathcal U|\), whereas the report displays only an upper bound. The missing bound is true.
- The selector-cell count requires a nonnegative exact-factor baseline.

## 2. Lifted floor-energy augmentation

Let
\[
\mathcal M_H=
\begin{pmatrix}
A&0\\
B_H&-I
\end{pmatrix}.
\]
For exact factors \(x,x^\star\),
\[
d=(x^\star-x,B_Hx^\star-B_Hx)
\in\ker_{\mathbb Z}\mathcal M_H.
\]
Take a conformal Graver decomposition
\[
d=\sum_{i=1}^t g_i,
\qquad
g_i=(p_i,v_i)\sqsubseteq d.
\]
The lifted kernel equations give
\[
Ap_i=0,
\qquad
v_i=B_Hp_i.
\tag{2.1}
\]

In particular, \(p_i=0\) forces \(v_i=0\). Thus the first lift has no nonzero
vertical-only summands that could evade the count below.

Because \(x^\star-x\in\{-1,0,1\}^{\Omega}\), every \(p_i\) in this particular decomposition is squarefree. Also \(x+p_i\) lies coordinatewise between \(x\) and \(x^\star\), so
\[
x+p_i\ge0,
\qquad
A(x+p_i)=\mathbf1.
\]
It is another exact factor.

Every column of \(A\) has sum \(n\), whence
\[
0=\mathbf1^\top Ap_i=n\mathbf1^\top p_i.
\]
Every nonzero \(p_i\) has both signs. Their negative supports are pairwise disjoint and each meets
\[
\operatorname{supp}x\setminus\operatorname{supp}x^\star.
\]
Therefore
\[
t\le
|\operatorname{supp}x\setminus\operatorname{supp}x^\star|
\le\operatorname{Cat}_m.
\tag{2.2}
\]

For one lower coordinate define
\[
\phi_q(u)=\frac{(u-c_q)(u-c_q-1)}{2c_q}.
\]
For conformal increments \(\delta_i\),
\[
\phi_q\!\left(u+\sum_i\delta_i\right)-\phi_q(u)
-\sum_i\bigl(\phi_q(u+\delta_i)-\phi_q(u)\bigr)
=\frac1{c_q}\sum_{i<j}\delta_i\delta_j\ge0.
\tag{2.3}
\]
Thus
\[
E_H(x^\star)-E_H(x)
\ge
\sum_i\bigl(E_H(x+p_i)-E_H(x)\bigr).
\]
Writing \(G=E_H(x)-E_H(x^\star)>0\), some summand satisfies
\[
E_H(x)-E_H(x+p_i)
\ge\frac Gt
\ge\frac{G}{|\operatorname{supp}x\setminus\operatorname{supp}x^\star|}
\ge\frac G{\operatorname{Cat}_m}.
\tag{2.4}
\]
Theorem 1 and its constant are exact.

If \(x^\star\) has zero energy, repeat the comparison toward the same \(x^\star\). Each selected move removes at least one current wreath absent from \(x^\star\), so at most \(\operatorname{Cat}_m\) strict descents are required.

The local/global conclusion is valid when local means no applicable unit move from \(\operatorname{Gr}(\mathcal M_H)\). Binary exact-factor feasibility rules out a nontrivial feasible positive multiple.

### Component scope

The correct statement is:

> Every lifted Graver move applicable at an exact-factor vertex projects to a squarefree factor-to-factor difference and hence is a union of complete middle-ownership overlay components.

Arbitrary elements of \(\operatorname{Gr}(\mathcal M_H)\) need not be squarefree or applicable.

If an applicable difference has ownership decomposition
\[
p=\sum_{K\in\mathscr K}p_K,
\]
then \((p,B_Hp)\) is lifted-conformally indecomposable exactly when no nonempty proper component union \(I\subsetneq\mathscr K\) satisfies
\[
B_Hp_I\sqsubseteq B_Hp.
\tag{2.5}
\]
This is the precise cancellation-packet criterion. It explains how lower-rank cancellation can force bundling, but does not prove that arbitrarily many components or an entire factor occur in a fixed-window lifted Graver element. The safe conclusion is only
\[
\boxed{\text{no sub-factor-scale support bound follows from this argument}.}
\]

## 3. Exact overload augmentation

For each \(q\), the full nonnegative integral system is
\[
h_q+s_q=\mathbf1,
\qquad
\mathbf1^\top h_q=r_q,
\]
\[
B_qx-h_q-p_q+d_q=c_q\mathbf1.
\tag{3.1}
\]
Integrality forces \(h_q,s_q\in\{0,1\}^{N_q}\).

For fixed \(x\), put
\[
\delta_S=\mu_q(S)-c_q,
\qquad
T=\sum_{\delta_S\ge1}\delta_S,
\qquad
a=\#\{S:\delta_S\ge1\}.
\]
For fixed \(h_q\), the optimum is
\[
p_q=(\delta-h_q)_+,
\qquad
d_q=(h_q-\delta)_+.
\]
Putting a high quota on a positive \(\delta_S\) reduces \(\mathbf1^\top p_q\) by one, so
\[
\min_{h_q,p_q,d_q}\mathbf1^\top p_q=T-\min(r_q,a).
\tag{3.2}
\]
Since \(\sum_S\delta_S=r_q\),
\[
D_q^-=T-r_q,
\qquad
D_q^+=T-a,
\]
and
\[
T-\min(r_q,a)=\max(D_q^-,D_q^+)=O_q(x).
\tag{3.3}
\]
The linearization is exact.

Theorem 2 uses the Graver basis of the full matrix in (3.1), not the earlier \(\mathcal M_H\). This full matrix should be displayed in the lead report.

Define
\[
\bar J(F)=\min_{h,s,p,d}J(F,h,s,p,d)
=\sum_{q\le H}\frac{O_q(F)}{c_q}.
\tag{3.4}
\]
Let \(z\) be auxiliary-optimal over \(F\), and \(z^\star\) a global optimizer. In a conformal decomposition
\[
z^\star-z=\sum_i g_i,
\]
write
\[
\gamma_i=J(z+g_i)-J(z).
\]
Linearity makes \(\gamma_i\) base-independent. Since \(z^\star-g_i\) is feasible, \(\gamma_i>0\) would imply
\[
J(z^\star-g_i)=J^\star-\gamma_i<J^\star,
\]
contradicting global optimality. Hence \(\gamma_i\le0\).

If \(g_i\) has zero \(x\)-part, then \(z+g_i\) is feasible over the same factor. Auxiliary optimality gives \(\gamma_i\ge0\), and hence \(\gamma_i=0\). This is where current auxiliary optimality is essential.

At most \(\operatorname{Cat}_m\) summands have nonzero \(x\)-part, by (2.2), and all objective decrease comes from them. Thus one factor-changing summand gives, after reoptimizing its projected factor \(F'\),
\[
\boxed{
\bar J(F')-J^\star
\le
\left(1-\frac1{\operatorname{Cat}_m}\right)
\bigl(\bar J(F)-J^\star\bigr).
}
\tag{3.5}
\]

For the finite strict path, take one conformal decomposition toward \(z^\star\), omit all zero-cost summands, and apply only the \(\gamma_i<0\) summands. Every partial conformal sum is feasible, and their changes sum to \(J^\star-\bar J(F)\). Hence a global optimum is reached in at most \(\operatorname{Cat}_m\) strict factor changes. Applying every factor-changing summand would not justify strictness, since some may have zero cost.

For \(H=H_A\),
\[
J^\star=W\beta_m(A)
\tag{3.6}
\]
exactly. Nothing above bounds this value.

## 4. Cone, lattice, and semigroup formulations

### 4.1 Mobile high quotas

Set \(p_q=d_q=0\) in (3.1), leaving \(h_q\) variable. The fixed right-hand side lies in the rational cone. Averaging an exact factor over the symmetric group gives lower load
\[
\frac W{N_q}=c_q+\frac{r_q}{N_q},
\]
and one may take
\[
h_q=\frac{r_q}{N_q}\mathbf1,
\qquad
s_q=\left(1-\frac{r_q}{N_q}\right)\mathbf1.
\]

It also lies in the integer lattice. For any integral exact factor \(x\), take signed
\[
h_q=B_qx-c_q\mathbf1,
\qquad
s_q=\mathbf1-h_q.
\]
Then
\[
\mathbf1^\top h_q=W-c_qN_q=r_q.
\]

Nonnegative integral membership forces \(x\) to be a \(0/1\) exact factor and \(h_q,s_q\) to be complementary \(0/1\) vectors. Hence it is equivalent to one exact factor having all loads in \(\{c_q,c_q+1\}\) simultaneously:
\[
\boxed{
\text{no perfectly balanced exact factor}
\iff
\text{the mobile-}h\text{ right-hand side is a cone/lattice semigroup hole}.
}
\tag{4.1}
\]

Within the explicitly slack-augmented system, \(J^\star\) is the minimum weighted use of the designated surplus generators. Repair cost is correct in this operational sense, but is not an intrinsic metric on the original semigroup.

### 4.2 Fixed prescribed quotas

For prescribed \(b\), the raw problem is
\[
Ay=\mathbf1,
\qquad
B_Hy=b.
\tag{4.2}
\]
This is a different cone. Signed saturation puts \((\mathbf1,b)\) in its integer lattice only when the quota differences have zero point margins—equivalently, when \(b\) has the correct total and point-incidence margins in each covered rank. The report's cyclic-invariant quotas satisfy this.

A target in lattice minus rational cone is not a semigroup hole, because a hole must already lie in cone intersect lattice.

## 5. Containment cuts

Let \(r=m-q\), with \(1\le q\le m-1\), and let
\[
\mathcal U\subseteq\binom{[n]}r.
\]
For a cyclic-order column \(C\), let
\[
u_C=\#\{\text{cyclic }r\text{-intervals in }\mathcal U\},
\]
\[
v_C=\#\{\text{cyclic }m\text{-intervals in }\partial_q^+\mathcal U\}.
\]
Every selected cyclic \(r\)-interval has \(q+1\) cyclic \(m\)-extensions, all in the upper shadow. Every cyclic \(m\)-interval contains at most \(q+1\) selected cyclic \(r\)-subintervals. Therefore
\[
u_C\le v_C.
\tag{5.1}
\]
For a fractional exact factor \(x\ge0\),
\[
\mu_q(\mathcal U)
=\sum_Cx_Cu_C
\le\sum_Cx_Cv_C
=\sum_{M\in\partial_q^+\mathcal U}(Ax)_M
=|\partial_q^+\mathcal U|.
\tag{5.2}
\]
Theorem 3 is correct. Its range should be stated; the report only needs \(q\le m-2\).

## 6. Prime-dimensional prescribed quota

Let \(n=2m+1\) be a sufficiently large odd prime,
\[
a=\lceil2\log_2n\rceil,
\qquad
r=m-1,
\qquad
N=\binom nr.
\]
Let \(\mathcal U\) be the \(r\)-sets containing a cyclic \(a\)-block in a fixed ground cycle.

The union bound and coefficient ratio give
\[
|\mathcal U|
\le n\binom{n-a}{r-a},
\]
\[
\frac{\binom{n-a}{r-a}}N
=\prod_{i=0}^{a-1}\frac{r-i}{n-i}
<2^{-a}\le n^{-2},
\]
so
\[
|\mathcal U|<\frac Nn.
\tag{6.1}
\]

Every \(R\in\mathcal U\) has \(n-r=m+2\) upper \(m\)-neighbors. If \(M\in\partial^+\mathcal U\), then \(M\) contains a cyclic \(a\)-block \(B\). Deleting any of the \(m-a\) points of \(M\setminus B\) leaves a member of \(\mathcal U\). Hence
\[
|\partial^+\mathcal U|
\le\frac{m+2}{m-a}|\mathcal U|
<2|\mathcal U|,
\tag{6.2}
\]
where the last inequality is exactly \(m>2a+2\).

At depth one,
\[
\frac WN=\frac{m+2}{m},
\qquad
c_1=1,
\qquad
d=W-N=\frac{2N}{m}.
\tag{6.3}
\]
Thus \(d>N/n>|\mathcal U|\).

The orbit divisibility is exact. For prime \(n\), every nonempty proper subset has cyclic orbit \(n\), so \(n\mid|\mathcal U|\). Also
\[
n\mid\binom nk
\qquad(1\le k\le n-1),
\]
and hence \(n\mid N\), \(n\mid W\), and \(n\mid d\). Therefore \(d-|\mathcal U|\) is a nonnegative multiple of \(n\), and enough unused orbits exist to extend \(\mathcal U\) to a cyclic-invariant \(\mathcal H\) of size \(d\).

Cyclic invariance gives point degree
\[
\deg_{\mathcal H}(i)=\frac{r|\mathcal H|}{n}.
\]
Thus
\[
b_1=\mathbf1+\mathbf1_{\mathcal H}
\]
is a point-regular floor/ceiling quota with point margin \(rW/n\). Since \(\mathcal H\supseteq\mathcal U\),
\[
b_1(\mathcal U)=2|\mathcal U|
>|\partial^+\mathcal U|.
\tag{6.4}
\]
It is outside the fractional cone by (5.2).

At other covered depths, \(r_q=W-c_qN_q\) is a multiple of \(n\), because \(W\) and every nontrivial \(N_q\) are divisible by \(n\). Whole-orbit high families give simultaneous cyclic-invariant point-regular quotas. Starting from an exact factor, simultaneous integral selector surjectivity gives a common signed lift because all rankwise differences have zero point margins.

Hence
\[
\boxed{
(\mathbf1,b)
\in\text{admissible signed lattice}
\setminus\text{fractional cone}.
}
\tag{6.5}
\]

## 7. Quantitative separation

Put
\[
\Delta=2|\mathcal U|-|\partial^+\mathcal U|.
\]
For every column \(C\),
\[
0\le v_C-u_C\le n.
\]
If \(y\) is any signed lift of the prescribed target, then
\[
\begin{aligned}
\Delta
&=b_1(\mathcal U)-|\partial^+\mathcal U|\\
&=\sum_Cy_C(u_C-v_C)\\
&\le n\|y^-\|_1.
\end{aligned}
\]
Thus
\[
\boxed{\|y^-\|_1\ge\Delta/n.}
\tag{7.1}
\]

The report omits the lower bound needed for its final asymptotic. One fixed cyclic \(a\)-block gives
\[
|\mathcal U|\ge\binom{n-a}{r-a}.
\]
Moreover
\[
\frac{\binom{n-a}{r-a}}N
=2^{-a}
\prod_{i=0}^{a-1}
\left(1-\frac{i+3}{n-i}\right).
\tag{7.2}
\]
Since \(a=O(\log n)\), the product is \(1-o(1)\); for large \(n\) it is at least \(1/2\). Also \(2^{-a}\ge1/(2n^2)\). Consequently
\[
|\mathcal U|\ge\frac{N}{4n^2}
=\Omega(W/n^2).
\tag{7.3}
\]
Since
\[
\Delta
\ge\frac{m-2a-2}{m-a}|\mathcal U|
=\Omega(|\mathcal U|),
\]
(7.1) yields
\[
\boxed{\|y^-\|_1=\Omega(W/n^3).}
\tag{7.4}
\]
The conclusion is correct, but (7.2)–(7.3) were missing.

For the selector consequence, specify the affine baseline. If
\[
y=x_F+\sum_{i=1}^s\varepsilon_i z_i,
\]
where \(x_F\ge0\) is an exact-factor indicator and each coefficient-one Petr–Turek cell has negative \(\ell_1\)-mass two, then
\[
\|y^-\|_1\le2s.
\]
Hence
\[
s\ge\frac{\Delta}{2n}
=\Omega(W/n^3).
\tag{7.5}
\]
Integral coefficients are allowed when absolute coefficient is counted as multiplicity. This is not a statement about expressions beginning from an arbitrary signed baseline.

## 8. Mesoscopic selector locality

Assume that connected means connected in the intersection graph of selector-cell cyclic-order supports, and that support-feasible means the reduced positive and negative supports are squarefree middle packings.

A selector cell has adjacent-swap diameter at most two, so a connected union of \(s\) cells has diameter at most \(2s\). One adjacent swap changes at most two middle intervals:
\[
|\mathcal W_m(C)\cap\mathcal W_m(D)|
\ge n-2d_\circ(C,D).
\tag{8.1}
\]
If \(2s\le m\), every pair of surviving orders shares a middle interval. Each sign-packing therefore contains at most one order. A nonzero kernel vector would have the form \(e_C-e_D\) with equal middle-incidence columns. In the unoriented-wreath quotient these columns determine the same wreath, forcing zero. Thus
\[
\boxed{
s\ge\left\lceil\frac{m+1}{2}\right\rceil.
}
\tag{8.2}
\]

Three conventions are essential:

1. connectivity is through shared order vertices;
2. support-feasibility is squarefree packing compatibility; and
3. reversal-identical columns are identified, or the proof is performed in the unoriented wreath quotient.

Without the third convention, \(e_C-e_{C^{\rm rev}}\) is a duplicate-column kernel vector. The bound concerns Petr–Turek selector composites only. It gives no \(\Omega(m)\) wreath-support bound for MSW trades or arbitrary lifted Graver moves, and it cannot be applied to the fixed-\(b\) signed lift, which is not support-feasible.

## 9. MWB and jointly chosen quotas

The exact implication scope is:

- The quadratic theorem removes nonglobal local minima under applicable full lifted-Graver moves.
- The linear theorem does the same for the exact unlabelled objective \(\bar J(F)\), with high cells optimized independently at each depth.
- Neither theorem bounds the optimum. In particular, neither proves
  \[
  J^\star=o(W)
  \quad\text{or}\quad
  \beta_m(A)\to0.
  \]
- The prescribed prime-dimensional quota proves that totals, cyclic symmetry, and point regularity do not imply fractional positivity. It does not show that the mobile-\(h\) zero-overload system is a semigroup hole.
- MWB minimizes jointly over the factor and rankwise high-quota families. The bad fixed \(b\) supplies no lower bound on \(J^\star\), \(\beta_m(A)\), or MWB.
- The \(h_q\) variables impose no cross-depth nesting or common owner. Thus the result remains unlabelled and supplies no common balanced nested resolution.
- Adding nested-resolution constraints would produce a different extended matrix and would still require a new positive-feasibility or optimum theorem.

For completeness, if \(J^\star=0\), the exact factor's own lower maps are balanced at every depth and form a nested resolution, so zero semigroup repair gives zero labelled error. This exceptional zero case does not provide the asymptotic stability theorem needed to pass from small positive overload to small labelled error.

The stable conclusion is
\[
\boxed{
\begin{array}{c}
\text{signed saturation and full Graver augmentation remove}\\
\text{lattice indices and false local minima, but not the positive endpoint;}\\[1mm]
\text{the remaining MWB theorem is still }J^\star=o(W).
\end{array}
}
\]

## 10. Final theorem ledger

- **Theorem 1:** accepted, with applicable-at-a-factor-vertex attached to squarefreeness and component claims.
- **Theorem 2:** accepted for \(\bar J(F)\) after auxiliary reoptimization; display the full extended matrix and strict-path argument.
- **Semigroup formulation:** accepted for the mobile-\(h\) zero-overload system.
- **Fixed prescribed quota:** accepted as admissible lattice minus cone, not as a semigroup hole.
- **Containment cut:** accepted for \(1\le q\le m-1\).
- **Prime regular quota:** accepted; orbit divisibility and point margins should be explicit.
- **Quantitative negativity:** accepted after adding (7.3).
- **Selector-cell lower bound:** accepted with the baseline and conventions in Sections 7–8.
- **MWB implication:** no new implication beyond descent to \(J^\star\); positivity and the \(o(W)\) optimum bound remain unproved.
