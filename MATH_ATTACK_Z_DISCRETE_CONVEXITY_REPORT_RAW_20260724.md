## Lane Z verdict

The discrete-convexity route fails in its standard form.

The floor energy is separable convex on unrestricted load space, but its restriction to the genuine positive exact-factor fibre is neither \(M\)-convex nor \(L^\natural\)-convex. Ownership-component coordinates do not repair this globally: their exact Hessian is a signed Gram matrix. The correct local-to-global theorem uses the Graver basis of an augmented matrix containing the lower-rank loads, and that basis contains cancellation-coupled unions of ownership components.

None of these facts proves or disproves the fixed-window positive-cut lemma \(LM_A\). That lemma remains the exact unproved gate.

### 1. Normalization

For \(1\le H\le m-1\), define the half-energy

\[
\Psi_H(F)=\frac12\sum_{q\le H}\frac{Q_q(F)}{c_q},
\qquad
Q_q(F)=\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\]

If \(f_q=\mu_q-(W/N_q)\mathbf1\), then

\[
\Psi_H(F)=\frac12\sum_{q\le H}\frac{\|f_q\|_2^2-\beta_q}{c_q},
\]

where \(\beta_q\) is factor-independent. Since \(Q_q\ge2O_q\),

\[
\Psi_H(F)\ge\sum_{q\le H}\frac{O_q(F)}{c_q}.
\]

Thus \(\Psi_{H_A}=o(W)\) remains a sufficient fixed-window MWB target.

## 2. Exact structural failure of standard \(M/L\)-convexity

Let \(\mathscr W_m\) be wreath columns modulo rotation and reversal, and

\[
\mathcal X_m=\{x\in\mathbb Z_{\ge0}^{\mathscr W_m}:A_mx=\mathbf1\}.
\]

### Theorem Z1

For every \(m\ge2\), the nontrivial exact-factor fibre \(\mathcal X_m\) is neither \(M\)-convex, \(M^\natural\)-convex, nor \(L^\natural\)-convex.

#### Proof

Every factor is binary and has size

\[
\sum_Cx_C=\frac Wn=\operatorname{Cat}_m.
\]

The fibre is nontrivial: \(S_n\) acts transitively on the

\[
|\mathscr W_m|=\frac{(2m)!}{2}>\operatorname{Cat}_m
\]

wreath columns, so a nonempty proper factor has a distinct relabelled image.

Suppose a one-column exchange were feasible:

\[
A_m(x-e_C+e_D)=\mathbf1.
\]

Then the middle columns of \(C,D\) would coincide. The middle-interval family determines the unoriented cyclic order—indeed, the number of its intervals containing \(u,v\) is \(m-d_C(u,v)\)—so \(C=D\) in \(\mathscr W_m\). Hence no nonzero unit exchange exists.

This violates the \(M\)-exchange axiom. The unpaired alternative in \(M^\natural\)-exchange changes the fixed factor size, while the paired alternative is the impossible exchange above.

For distinct binary factors \(x,y\),

\[
\left\lfloor\frac{x+y}{2}\right\rfloor=x\wedge y,
\qquad
\left\lceil\frac{x+y}{2}\right\rceil=x\vee y.
\]

Their sizes are \(\operatorname{Cat}_m-k\) and \(\operatorname{Cat}_m+k\) for some \(k\ge1\), so neither is an exact factor. Thus midpoint closure fails. ∎

The same obstruction survives after passing to loads. At actual set rank \(r\), every factor load satisfies

\[
\sum_S\mu(S)=W,
\qquad
U_r\mu=r\operatorname{Cat}_m\,\mathbf1.
\]

An exchange \(\mu-e_S+e_T\) preserves point margins only if \(S=T\). Therefore every nonsingleton rank-load image, and every nonsingleton joint multirank image, fails \(M/M^\natural\)-exchange. For \(m\ge3\), the first-shadow image is nonsingleton because a singleton image would be constant and integral, contradicting

\[
\frac{W}{N_1}=\frac{m+2}{m}\notin\mathbb Z.
\]

So this obstruction applies directly in every fixed Gaussian window.

## 3. Exact component-cube calculus

Let \(F,G\) be exact factors and \(K\) the connected components of their ownership overlay. Put

\[
z_K=\mathbf1_{G\cap K}-\mathbf1_{F\cap K},
\qquad
v_K=B_Hz_K,
\]

where \(B_H\) concatenates all depth-\(q\) maps for \(q\le H\). Every component subset \(I\) gives a genuine exact factor \(F_I\).

### Theorem Z2

On this Boolean component cube,

\[
\Psi_H(F_I)
=
\Psi_H(F)
+\sum_{K\in I}
 \left(\langle f,v_K\rangle_H+\frac12\|v_K\|_H^2\right)
+\sum_{\substack{K<L\\K,L\in I}}
 \langle v_K,v_L\rangle_H .
\]

Consequently the mixed Boolean curvature is exactly

\[
\Delta_K\Delta_L\Psi_H=\langle v_K,v_L\rangle_H.
\]

Hence the cube restriction is \(L^\natural\)-convex precisely when

\[
\langle v_K,v_L\rangle_H\le0
\quad(K\ne L).
\]

For a transposition cube \(G=\tau F\), component equivariance gives

\[
\Psi_H(F_I)-\Psi_H(F)
=-\frac12\langle d_I,d_{I^c}\rangle_H.
\]

Thus a positive component-correlation cut—the desired legal descent—forces some positive Gram entry and therefore failure of \(L^\natural\)-convexity in the natural old/new coordinates. Conversely, if all Gram entries are nonpositive, \(F\) is already minimum on that entire transposition cube.

So \(L^\natural\)-convexity has the wrong sign for the positive-cut route: it freezes the current antipodal corner rather than producing descent.

For the direct \(M^\natural\) transfer between the all-one and all-zero component corners,

\[
\Psi_H(\mathbf1)+\Psi_H(\mathbf0)
-\Psi_H(\mathbf1-e_K)-\Psi_H(e_K)
=
\sum_{L\ne K}\langle v_K,v_L\rangle_H.
\]

There is no universal sign for this quantity.

## 4. Genuine component-coordinate obstruction

There is also an integral obstruction beyond the native-coordinate failure, although it lies outside fixed Gaussian windows.

### Theorem Z3

For every \(m\ge9\), the MSW factor contains a genuine component cube on which the lower-rank-\(2\) floor energy admits no orientation making it \(L^\natural\)-convex. Some orientation also violates the direct one-component \(M^\natural\)-exchange inequality.

#### Proof

For \(\tau=(2\,3)\), the \(j=0\) ownership components are the

\[
s=\operatorname{Cat}_{m-2}
\]

independently switchable connected \(2\)-for-\(2\) components indexed by \(R\in\mathcal D_{m-2}\). Their actual rank-\(2\) effects satisfy

\[
\delta_R=B_2z_R,\qquad
\|\delta_R\|_2^2=8.
\]

Let \(D=\binom{2m+1}{2}\). At \(m=9\),

\[
\operatorname{Cat}_7=429>342=2D,
\]

and the Catalan ratio exceeds the quadratic-dimension growth ratio thereafter. Thus \(s>2D\) for every \(m\ge9\).

The elementary obtuse-vector bound says that nonzero vectors
\(w_1,\ldots,w_s\in\mathbb R^D\) with all pairwise inner products nonpositive satisfy \(s\le2D\). To prove it, normalize them, let \(G\) be their Gram matrix, and put \(A=I-G\). Then \(A\) is symmetric and entrywise nonnegative. Since \(G\succeq0\), Perron–Frobenius gives \(\operatorname{spec}(A)\subseteq[-1,1]\), hence \(\operatorname{spec}(G)\subseteq[0,2]\). Therefore

\[
s=\operatorname{tr}G\le2\operatorname{rank}G\le2D.
\]

Orienting component sides only replaces each \(\delta_R\) by \(\pm\delta_R\). Since \(s>2D\), every orientation has a pair with positive inner product, contradicting the submodularity criterion above.

Also \(s>D\), so two effects are nonorthogonal. Orient one so that their inner product is negative. On the resulting exact two-component face,

\[
E_{11}+E_{00}-E_{10}-E_{01}<0,
\]

which is the reverse of the direct \(M^\natural\)-exchange inequality. ∎

This theorem concerns actual rank \(r=2\), i.e. depth \(q=m-2\). It does not show failure of component-cube convexity for \(q\le A\sqrt m\), nor does it construct a nonglobal component-local minimum.

## 5. The correct Graver local-to-global theorem

The objective is separable in the load variables, not in wreath indicators. Therefore the relevant matrix is

\[
\widehat A_H=
\begin{pmatrix}
A_m&0\\
B_H&-I
\end{pmatrix}.
\]

Use the genuine positive box

\[
\widehat{\mathcal F}_H=
\left\{
(x,u)\in\mathbb Z:
\widehat A_H(x,u)=
\binom{\mathbf1}{0},\
0\le x\le1,\
0\le u\le W\mathbf1
\right\}.
\]

The box is essential: omitting it returns to the unrestricted signed fibre.

### Theorem Z4 — exact augmented-Graver optimality

A factor \((x,u)\in\widehat{\mathcal F}_H\) globally minimizes \(\Psi_H\) if and only if there is no feasible improving augmentation

\[
\lambda g,\qquad
g\in\mathcal G(\widehat A_H),\quad \lambda\in\mathbb Z_{>0}.
\]

Binary feasibility forces every feasible nonzero scale to have \(\lambda=1\).

#### Proof

If \(y\) is better, conformally decompose

\[
y-x=g^1+\cdots+g^t
\]

in the augmented kernel. Every individual augmentation remains coordinatewise between the two feasible endpoints. Separable discrete convexity gives

\[
\Psi_H\!\left(x+\sum_jg^j\right)-\Psi_H(x)
\ge
\sum_j\bigl(\Psi_H(x+g^j)-\Psi_H(x)\bigr).
\]

A negative left side forces an improving Graver summand. The converse is immediate. ∎

### Exact packet characterization

For a component union \(J\), put

\[
z_J=\sum_{K\in J}z_K,\qquad v_J=B_Hz_J.
\]

Among moves feasible between factor vertices,

\[
(z_J,v_J)\in\mathcal G(\widehat A_H)
\]

if and only if there is no nonempty proper \(I\subsetneq J\) with

\[
v_I\sqsubseteq v_J.
\]

Thus:

- every connected ownership component is an augmented Graver move;
- augmented Gravers can also be disconnected, cancellation-minimal component packets;
- connected components are the squarefree Gravers of \(A_m\), but not all relevant Gravers of \(\widehat A_H\).

The rank-\(2\) construction above gives a literal two-component augmented Graver packet: opposite-sign overlap prevents either component effect from being conformal to their sum.

## 6. Strongest unconditional near-global estimate

Suppose every individual component between \(F\) and a comparator \(G\) is nonimproving from \(F\). Then, with \(v=\sum_Kv_K\),

\[
\boxed{
\Psi_H(F)-\Psi_H(G)
\le
\frac12\left(
\sum_K\|v_K\|_H^2-\|v\|_H^2
\right)
\le
\frac12\sum_K\|v_K\|_H^2.
}
\]

This constant \(1/2\) is exact for the half-energy normalization; it becomes \(1\) for the full energy.

To compare a component-local factor with a global minimizer, locality must hold against every feasible connected component move, not merely components of one transposition overlay. No available theorem bounds the variance term by \(o(W)\). This is the same unresolved positive-fibre component-noise scale exposed by the heat audits.

## Final fixed-window status

The lane is exhausted as follows:

- **Proved:** standard \(M\), \(M^\natural\), and \(L^\natural\) convexity fail on the genuine exact-factor fibre in every fixed window.
- **Proved:** component-cube curvature is exactly the weighted Gram matrix.
- **Proved:** augmented-Graver optimality gives an exact local-to-global certificate.
- **Proved:** augmented Gravers may require cancellation-coupled component packets.
- **Proved:** a full-depth rank-\(2\) MSW face gives a genuine no-orientation \(L^\natural\) obstruction.
- **Unproved:** whether fixed-window component geometry has any weaker exchange property strong enough to imply
  \[
  \Psi_{H_A}(F)=O_A(H_A\operatorname{Cat}_m)
  \]
  at every transposition-cut local minimum.
- **Unproved:** any \(o(W)\) bound on the component-variance residue.
- **Not implied:** labelled common-owner synchronization; this lane controls only unlabelled histogram energy.

Accordingly, discrete convexity does not prove \(LM_A\). The exact surviving theorem remains the positive-cut/local-minimum lemma from the first-wave synthesis.

The decisive steps above were independently audited, including the \(m\ge9\) Catalan constant, the genuine ownership-component realization, the positive box in the augmented fibre, the packet characterization, and the \(1/2\) near-global constant. Relevant sources are [the first-wave synthesis](/Users/amir.nuriyev/Documents/problem/MATH_ATTACK_FIRST_WAVE_SYNTHESIS_20260724.md), [the trade/Markov report](/Users/amir.nuriyev/Documents/problem/MATH_ATTACK_B_TRADE_MARKOV_REPORT_RAW_20260724.md), [the local-trade formulas](/Users/amir.nuriyev/Documents/problem/MSW_MULTIRANK_LOCAL_TRADES.md), and [the component hierarchy](/Users/amir.nuriyev/Documents/problem/MSW_COMPONENT_HIERARCHY_REDUCTION.md).
