# Second-wave lane Z2: discrete convexity on the exact-factor fibre

## Verdict

The objective and the exact-factor fibre behave in opposite ways.

1. On the unrestricted fixed-mass histogram lattice, both the floor-collision
   energy and the true mobile-quota overload are \(M\)-convex.  For overload
   this has a self-contained integral min-cost-flow exchange proof.

2. After restriction to the genuine exact-factor fibre, standard
   \(M\)-, \(M^\natural\)-, and \(L^\natural\)-convexity fail for purely
   structural reasons: there is no nontrivial unit wreath exchange, the
   load images have fixed point margins and admit no nontrivial unit target
   exchange, and the factor domain is not midpoint closed.

3. Passing to legal ownership-component coordinates does not restore
   discrete convexity.  For every \(m\ge4\), two explicit connected
   \(2\)-for-\(2\) components of the MSW factor have disjoint depth-one
   effects and depth-two inner product exactly \(2\).  Hence the genuine
   two-component face has floor-energy mixed curvature
   
   \[
   \frac{2}{c_2}
   \]
   
   in one orientation, violating Boolean \(L^\natural\)-convexity, and
   \(-2/c_2\) after reversing one coordinate, violating the mandatory direct
   \(M^\natural\)-exchange inequality.  This is a fixed-window obstruction,
   not the earlier deep-rank obstruction.

4. For every \(m\ge4\), the same two components, oppositely oriented, form
   a disconnected augmented-Graver primitive for every
   \(2\le H\le m-1\).  Thus the exact
   lifted Graver test set is strictly richer than the list of connected
   ownership components even in a fixed shallow window.

5. Full augmented-Graver locality is nevertheless exact global locality.
   For floor energy one augments by the load variables.  For overload one
   must augment further by the mobile high-quota selectors and surplus and
   deficit slacks.  In the latter lift, a full Graver move contracts the
   optimized global gap by at least a \(1/\operatorname{Cat}_m\) fraction.
   This comparison theorem gives no upper bound on the global optimum.

6. The quadratic Gram obstruction does not automatically transfer to
   optimized overload.  Overload curvature is supported on floor/ceiling
   quota walls and on the global high-quota-count kink.  No genuine
   nonglobal component-local overload factor is proved here.  The exact
   overload result is ambient \(M\)-convexity plus full decorated-Graver
   local/global optimality, not component-cube convexity.

Consequently this lane does not prove fixed-window overload \(o(W)\), MWB,
or labelled common-owner synchronization.  It gives a positive exact
Graver theorem and a genuine fixed-window obstruction to the proposed
component-coordinate \(M/L\) route.

## 1. Set-up and normalizations

Put

\[
n=2m+1,
\qquad
W=\binom{n}{m},
\qquad
B=\frac Wn=\operatorname{Cat}_m.
\]

Let \(\mathscr W_m\) be the set of unoriented wreath columns, with cyclic
rotation and reversal already quotiented out.  Let \(A_m\) be their
middle-set incidence matrix.  The positive exact-factor fibre is

\[
\mathcal X_m=
\{x\in\mathbb Z_{\ge0}^{\mathscr W_m}:A_mx=\mathbf1\}.
\]

Every member of \(\mathcal X_m\) is automatically binary and has exactly
\(B\) selected wreaths.

Throughout, \(1\le q\le H\le m-1\).  At depth \(q\), the actual set rank is

\[
r=m-q,
\qquad
N_q=\binom nr.
\]

Let \(C_r\) denote the actual rank-\(r\) load map, and put
\(B_q=C_{m-q}\).  Write \(B_qx=\mu_q\) for the depth-\(q\), rank-\(r\)
load vector of the factor.  Every such load has total mass \(W\).  Define

\[
B_Hx=(B_1x,\ldots,B_Hx),
\tag{1.0}
\]

the vertical concatenation of the depth maps.  Also define

\[
c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\qquad
\rho_q=W-c_qN_q,
\qquad 0\le\rho_q<N_q.
\]

The balanced quota set is

\[
\mathcal B_q=
\left\{
b\in\{c_q,c_q+1\}^{N_q}:\mathbf1^\top b=W
\right\}.
\]

For a load \(\mu\) of total \(W\), define its true mobile-quota overload by

\[
O_q(\mu)
=
\min_{b\in\mathcal B_q}
\sum_S(\mu(S)-b(S))_+
=
\frac12\min_{b\in\mathcal B_q}\|\mu-b\|_1.
\tag{1.1}
\]

The equality holds because \(\mu\) and \(b\) have equal total mass.

The half floor-collision energy in one row is

\[
\Phi_q(\mu)
=
\frac12\sum_S
(\mu(S)-c_q)(\mu(S)-c_q-1),
\tag{1.2}
\]

and the weighted window energy is

\[
\Psi_H(x)
=
\sum_{q=1}^H\frac{\Phi_q(B_qx)}{c_q}.
\tag{1.3}
\]

All \(c_q\) in the stated lower window are positive.  The standard exact
inequality is

\[
\Phi_q(\mu)\ge O_q(\mu),
\qquad
\Psi_H(x)\ge
\sum_{q\le H}\frac{O_q(B_qx)}{c_q}.
\tag{1.4}
\]

Here

\[
D_q^-=\sum_S(c_q-\mu(S))_+,
\qquad
D_q^+=\sum_S(\mu(S)-c_q-1)_+.
\]

Indeed, a deficit \(d=c_q-\mu(S)>0\) contributes
\(d(d+1)/2\ge d\) to \(\Phi_q\), while a surplus
\(e=\mu(S)-c_q-1>0\) contributes \(e(e+1)/2\ge e\).
Thus \(\Phi_q\ge D_q^-+D_q^+\ge\max(D_q^-,D_q^+)=O_q\), where
the final exact overload identity is proved in (7.2).

## 2. Positive ambient theorem: overload really is \(M\)-convex

The failure later in this report comes from the exact-factor geometry, not
from a hidden nonconvexity of the histogram objective.

### Theorem Z2.1 — ambient floor and overload exchange

Fix integers \(N\ge1\), \(c\ge0\), and \(W=cN+\rho\), with
\(0\le\rho<N\), and let

\[
\mathcal D_{N,W}
=
\{\mu\in\mathbb Z_{\ge0}^N:\mathbf1^\top\mu=W\}.
\]

Then:

1. The separable floor energy
   
   \[
   \Phi(\mu)=\frac12\sum_i(\mu_i-c)(\mu_i-c-1)
   \]
   
   is \(M\)-convex on \(\mathcal D_{N,W}\).  Its unrestricted separable
   extension to \(\mathbb Z^N\) is also \(L^\natural\)-convex.

2. The balanced overload
   
   \[
   O(\mu)=
   \min_{b\in\{c,c+1\}^N,\ \sum b_i=W}
   \frac12\|\mu-b\|_1
   \]
   
   is \(M\)-convex on \(\mathcal D_{N,W}\).  Explicitly, for every
   \(x,y\in\mathcal D_{N,W}\) and every \(i\) with \(x_i>y_i\), there is
   \(j\) with \(x_j<y_j\) such that
   
   \[
   O(x)+O(y)
   \ge
   O(x-e_i+e_j)+O(y+e_i-e_j).
   \tag{2.1}
   \]

3. Positive weighted direct sums of these row objectives are \(M\)-convex
   on the product of their separately fixed-total domains.  Thus the
   unrestricted joint \(H\)-row histogram objective has the exchange
   property inside the row containing the prescribed coordinate.

#### Proof for the floor energy

Let

\[
\phi(t)=\frac12(t-c)(t-c-1).
\]

Its forward difference is

\[
\phi(t+1)-\phi(t)=t-c,
\]

which is nondecreasing.  If \(x_i>y_i\) and \(x_j<y_j\), then

\[
\begin{aligned}
&\Phi(x)+\Phi(y)
-\Phi(x-e_i+e_j)-\Phi(y+e_i-e_j)\\
&=[\phi(x_i)-\phi(x_i-1)]
  -[\phi(y_i+1)-\phi(y_i)]\\
&\quad+[\phi(y_j)-\phi(y_j-1)]
  -[\phi(x_j+1)-\phi(x_j)]
\ge0.
\end{aligned}
\]

Thus every admissible \(j\) works.  Coordinatewise discrete midpoint
convexity gives the unrestricted \(L^\natural\) statement.

#### Self-contained min-cost-flow proof for overload

Build a directed network with row nodes \(a_i\), quota nodes \(b_j\), and
a common sink \(t\).  Put an arc

\[
a_i\longrightarrow b_j
\]

of unlimited capacity and cost \(0\) when \(i=j\), and cost \(1\) when
\(i\ne j\).  Put an arc

\[
b_j\longrightarrow t
\]

of cost zero, lower capacity \(c\), and upper capacity \(c+1\).  Give row
node \(a_i\) supply \(\mu_i\), and give \(t\) demand \(W\).

Every integral flow chooses a quota vector

\[
b_j\in\{c,c+1\},
\qquad
\sum_jb_j=W.
\]

For fixed \(b\), any flow has off-diagonal cost at least

\[
W-\sum_i\min(\mu_i,b_i)
=
\sum_i(\mu_i-b_i)_+
=
\frac12\|\mu-b\|_1.
\]

This lower bound is attained by retaining \(\min(\mu_i,b_i)\) units on
each diagonal arc and matching the remaining surplus rows to the remaining
deficit columns.  Therefore the integral minimum flow cost is exactly
\(O(\mu)\).

Now let \(P,Q\) be optimal integral flows for \(x,y\), and fix
\(i\) with \(x_i>y_i\).  Form the signed integral edge flow \(P-Q\): orient
an edge in its original direction when \(P_e-Q_e>0\), and in the reverse
direction when \(P_e-Q_e<0\), with the corresponding multiplicity.  Its
divergence at row node \(a_k\) is \(x_k-y_k\); every quota node and the
sink have zero divergence.

Integral flow decomposition therefore supplies a directed unit path from
the chosen positive-divergence row \(a_i\) to a negative-divergence row
\(a_j\).  Necessarily \(x_j<y_j\).  Let \(g_e=1\) when this path traverses
edge \(e\) in its original direction and \(g_e=-1\) when it traverses it
backwards.  Then

\[
P'=P-g,
\qquad
Q'=Q+g
\]

are feasible flows for \(x-e_i+e_j\) and \(y+e_i-e_j\), respectively.
Indeed, on an edge with \(g_e=1\) one has \(P_e\ge Q_e+1\), while on an
edge with \(g_e=-1\) one has \(Q_e\ge P_e+1\).  Hence the operation stays
between the two feasible edge values.  This preserves nonnegativity and,
on every quota arc, preserves the interval \([c,c+1]\).

The two linear costs cancel exactly:

\[
\operatorname{cost}(P')+\operatorname{cost}(Q')
=
\operatorname{cost}(P)+\operatorname{cost}(Q).
\]

Reoptimizing the two new flows proves (2.1).  The case \(N=1\) is
immediate.  This proves \(M\)-convexity.  Direct sums follow by taking
\(j\) in the same fixed-total row as \(i\).  ∎

### Corollary Z2.1a — ambient unit descent

If \(O(\mu)>0\), choose a nearest balanced quota \(b\).  There are indices
\(i,j\) with \(\mu_i>b_i\) and \(\mu_j<b_j\).  Then

\[
O(\mu-e_i+e_j)=O(\mu)-1.
\tag{2.2}
\]

The transfer decreases the half-\(\ell_1\) distance to this particular
\(b\) by one.
Conversely, (1.1) and the triangle inequality show that one unit transfer
can change \(O\) by at most one.

Similarly, if \(\mu_i\ge\mu_j+2\), then

\[
\Phi(\mu-e_i+e_j)-\Phi(\mu)
=-(\mu_i-\mu_j-1)<0.
\tag{2.3}
\]

Thus unrestricted histogram local minima are exactly balanced.  The exact
factor constraints are what forbid these elementary descents.

## 3. Standard \(M/L\)-convexity fails on the genuine fibre

### Theorem Z2.2 — objective-independent domain obstruction

For every \(m\ge2\), the exact-factor indicator domain \(\mathcal X_m\)
is neither \(M\)-convex, \(M^\natural\)-convex, nor
\(L^\natural\)-convex.  Consequently the restriction of either the floor
energy or the balanced overload to this domain, extended by \(+\infty\)
off the domain, has none of these properties.

#### Proof

Every exact factor has fixed cardinality \(B=\operatorname{Cat}_m\).
Suppose a one-wreath exchange were feasible:

\[
A_m(x-e_C+e_D)=\mathbf1.
\]

Then the two middle-incidence columns would be equal.  They determine the
unoriented cyclic order: if \(d_C(u,v)\in\{1,\ldots,m\}\) is the shorter
cyclic distance, the number of middle intervals of \(C\) containing both
\(u,v\) is

\[
m-d_C(u,v).
\]

Thus the column determines every cyclic distance and in particular every
adjacency, so \(C=D\) in \(\mathscr W_m\).  There is no nonzero unit
exchange.

The fibre is nontrivial.  Exact factors exist, while

\[
|\mathscr W_m|=\frac{(2m)!}{2}>\operatorname{Cat}_m.
\]

A factor is therefore a nonempty proper subset of the transitive
\(S_n\)-set \(\mathscr W_m\), so some coordinate relabelling produces a
distinct factor.  Applying the \(M\)-exchange axiom to two distinct factors
requires the impossible unit exchange above.  The unpaired
\(M^\natural\) alternative changes the fixed factor cardinality, and its
paired alternative is again the impossible exchange.

For distinct binary factors \(x,y\), if

\[
k=|\operatorname{supp}x\setminus\operatorname{supp}y|\ge1,
\]

then

\[
\left\lfloor\frac{x+y}{2}\right\rfloor=x\wedge y,
\qquad
\left\lceil\frac{x+y}{2}\right\rceil=x\vee y
\]

have cardinalities \(B-k\) and \(B+k\).  Neither is an exact factor, so
the domain is not discretely midpoint closed.  ∎

### Load-image obstruction

At actual rank \(r\), every exact-factor load also satisfies the fixed
point margins

\[
\mathbf1^\top\mu=W,
\qquad
U_r\mu=rB\,\mathbf1,
\tag{3.1}
\]

where \(U_r\) is point-versus-\(r\)-set incidence.  A unit target exchange

\[
\mu-e_S+e_T
\]

preserves (3.1) only if

\[
\mathbf1_T-\mathbf1_S=0,
\]

hence only if \(S=T\).  Therefore every nonsingleton rank-load image, and
every nonsingleton joint multirank load image, fails standard
\(M/M^\natural\) exchange.

For \(m\ge3\), the depth-one image is nonsingleton.  If it were a singleton,
permutation invariance would make it a constant integral vector, contrary
to

\[
\frac W{N_1}=\frac{m+2}{m}\notin\mathbb Z.
\]

This gives the exact separation:

\[
\boxed{
\text{ambient histogram objective is M-convex}
\quad\text{but}\quad
\text{a nonsingleton exact load image is not an M-domain}.}
}
\tag{3.2}
\]

## 4. Legal ownership-component coordinates

Let \(F,G\) be exact factors.  Cancel their common wreaths and take the
connected components \(K\) of their middle-ownership overlay.  Put

\[
z_K=\mathbf1_{G\cap K}-\mathbf1_{F\cap K},
\qquad
v_K=B_Hz_K.
\]

Every component subset \(I\) gives a genuine exact factor

\[
F_I=F+\sum_{K\in I}z_K.
\]

Define the weighted load inner product

\[
\langle a,b\rangle_H
=
\sum_{q\le H}\frac1{c_q}
\sum_Sa_q(S)b_q(S).
\tag{4.1}
\]

If

\[
f_q=B_qF-\frac W{N_q}\mathbf1,
\]

then direct quadratic expansion gives

\[
\begin{aligned}
\Psi_H(F_I)
=\Psi_H(F)
&+\sum_{K\in I}
\left(
\langle f,v_K\rangle_H+\frac12\|v_K\|_H^2
\right)\\
&+\sum_{\substack{K<L\\K,L\in I}}
\langle v_K,v_L\rangle_H.
\end{aligned}
\tag{4.2}
\]

Thus every two-face has constant mixed curvature

\[
\Gamma_{KL}
=
\Psi_{11}+\Psi_{00}-\Psi_{10}-\Psi_{01}
=
\langle v_K,v_L\rangle_H.
\tag{4.3}
\]

On a Boolean two-face, \(L^\natural\)-convexity requires

\[
\Gamma_{KL}\le0,
\tag{4.4}
\]

because it is exactly the submodular midpoint inequality for \(10,01\).
The direct \(M^\natural\)-exchange inequality for the comparable pair
\(11,00\) requires the opposite sign

\[
\Gamma_{KL}\ge0.
\tag{4.5}
\]

Therefore a nonzero Gram entry obstructs at least one of the two notions,
depending on component orientation.  The next theorem makes this genuine
in a fixed shallow window.

## 5. A genuine fixed-window component obstruction

The only construction input used here is the already proved MSW local
component formula from `MSW_MULTIRANK_LOCAL_TRADES.md` together with the
proved component realization from
`MSW_COMPONENT_HIERARCHY_REDUCTION.md`: for \(\tau=(2\ 3)\), every Dyck
word \(R\in\mathcal D_{m-2}\) indexes a connected, independently
switchable \(2\)-for-\(2\) ownership component \(z_R\) of the MSW exact
factor.  No computational or signed-fibre assertion is used.

### Theorem Z2.3 — exact depth-two curvature

For every \(m\ge4\), let

\[
R_0=(10)^{m-2},
\qquad
R_1=1100(10)^{m-4},
\tag{5.1}
\]

and let \(z_0,z_1\) be the corresponding genuine MSW ownership-component
moves.  In (5.2)--(5.3), \(\langle\cdot,\cdot\rangle_2\) denotes the
ordinary Euclidean inner product on the indicated rank-load row.  Then

\[
\langle C_{m-1}z_0,C_{m-1}z_1\rangle_2=0
\tag{5.2}
\]

at depth one, while

\[
\langle C_{m-2}z_0,C_{m-2}z_1\rangle_2=2
\tag{5.3}
\]

at depth two.  Consequently the weighted half-energy \(\Psi_2\) has

\[
\Delta_0\Delta_1\Psi_2=\frac2{c_2}
\tag{5.4}
\]

on the naturally oriented component face.

#### Proof

Write \(s=m-2\).  For a Dyck word \(R\), split its MSW flip permutation
into insertion and deletion lists \(\mathsf A(R),\mathsf B(R)\).  The flip
recursion gives

\[
\begin{aligned}
\mathsf A(R_0)&=(2,4,\ldots,2s),
&\mathsf B(R_0)&=(1,3,\ldots,2s-1),\\
\mathsf A(R_1)&=(4,3,6,8,\ldots,2s),
&\mathsf B(R_1)&=(2,1,5,7,\ldots,2s-1).
\end{aligned}
\tag{5.5}
\]

For the \(p=0\) component, put \(\beta=2\), \(\gamma=3\), and split the
common tail into parity lists.  Equations (5.5) give

\[
\begin{aligned}
\mathsf E_0&=(6,8,10,\ldots,2m,n),
&\mathsf O_0&=(5,7,9,\ldots,2m-1),\\
\mathsf E_1&=(8,7,10,12,\ldots,2m,n),
&\mathsf O_1&=(6,5,9,11,\ldots,2m-1).
\end{aligned}
\tag{5.6}
\]

For a core \(K\) define the dipole

\[
\partial K=e_{K\cup\{3\}}-e_{K\cup\{2\}}.
\tag{5.7}
\]

At depth two, rank \(m-2\), the exact four-arm formula is

\[
C_{m-2}z
=
\partial\operatorname{suf}_{m-3}(\mathsf O)
+\partial\operatorname{suf}_{m-3}(\mathsf E)
-\partial\operatorname{pre}_{m-3}(\mathsf E)
-\partial\operatorname{pre}_{m-3}(\mathsf O).
\tag{5.8}
\]

For \(m\ge5\), the signed core tables are

\[
\begin{array}{c|cccc}
R_0
&+\{7,9,\ldots,2m-1\}
&+K
&-\{6,8,\ldots,2m-2\}
&-\{5,7,\ldots,2m-3\}\\[1mm]
R_1
&+\{5,9,11,\ldots,2m-1\}
&+K
&-\{7,8,10,12,\ldots,2m-2\}
&-\{5,6,9,11,\ldots,2m-3\},
\end{array}
\tag{5.9}
\]

where

\[
K=\{10,12,\ldots,2m,n\}.
\tag{5.10}
\]

Endpoint and parity comparison shows that \(K\) is the only common core
between the two rows.  Distinct cores give disjoint dipoles, while

\[
\|\partial K\|_2^2=2.
\]

This proves (5.3) for \(m\ge5\).

For \(m=4\), the two signed core lists are

\[
\begin{aligned}
R_0&:\quad +\{7\},+\{9\},-\{6\},-\{5\},\\
R_1&:\quad +\{5\},+\{9\},-\{8\},-\{6\}.
\end{aligned}
\]

The three common-core contributions are \(-2,+2,+2\), again totaling
\(2\).

At depth one, the two dipole-core pairs are

\[
\begin{aligned}
R_0&:\quad
+\{8,10,\ldots,2m,n\},
-\{6,8,\ldots,2m\},\\
R_1&:\quad
+\{7,10,12,\ldots,2m,n\},
-\{7,8,10,12,\ldots,2m\}.
\end{aligned}
\tag{5.11}
\]

These four cores are pairwise distinct, including at \(m=4\), so the
depth-one supports are disjoint and (5.2) follows.  Inserting (5.2)--(5.3)
into (4.3) proves (5.4).  ∎

### Corollary Z2.3a — genuine \(L^\natural\) and \(M^\natural\) failures

Let \(X\) be the MSW factor.  All four vertices

\[
X,
\quad X+z_0,
\quad X+z_1,
\quad X+z_0+z_1
\]

are genuine exact factors.  In the natural old-to-new orientation,

\[
\Psi_2(X+z_0+z_1)+\Psi_2(X)
-\Psi_2(X+z_0)-\Psi_2(X+z_1)
=\frac2{c_2}>0.
\tag{5.12}
\]

This violates Boolean submodularity and hence \(L^\natural\)-convexity.

Reverse the second component coordinate by taking the opposite endpoints.
The two effects are now \(z_0,-z_1\), so the mixed curvature is

\[
-\frac2{c_2}<0.
\tag{5.13}
\]

For the comparable Boolean points \(11,00\), the direct
\(M^\natural\)-exchange axiom requires this mixed difference to be
nonnegative.  It fails.

Thus a genuine fixed-window component face obstructs each proposed
discrete-convexity sign.  The assertion is existence of an
\(L^\natural\)-failing orientation and of an \(M^\natural\)-failing
orientation; it is not a claim that every orientation of the entire MSW
component cube fails \(L^\natural\)-convexity.

## 6. A no-orientation theorem at actual rank two

The fixed-window theorem above is the decisive new obstruction.  For
completeness, the earlier all-orientations obstruction at actual rank two
also admits sharper constants than the first-wave report.

### Lemma Z2.4 — obtuse-vector bound

If nonzero vectors \(w_1,\ldots,w_s\in\mathbb R^d\) satisfy

\[
\langle w_i,w_j\rangle\le0
\qquad(i\ne j),
\]

then

\[
s\le2d.
\tag{6.1}
\]

#### Proof

Normalize the vectors and let \(G\) be their Gram matrix.  Put

\[
A=I-G.
\]

Then \(A\) is symmetric and entrywise nonnegative.  Since \(G\succeq0\),
\(\lambda_{\max}(A)\le1\).  For a symmetric nonnegative matrix its
Perron eigenvalue is its spectral radius, so every eigenvalue of \(A\)
lies in \([-1,1]\).  Hence every nonzero eigenvalue of \(G=I-A\) lies in
\((0,2]\).  Therefore

\[
s=\operatorname{tr}G
\le2\operatorname{rank}G
\le2d.
\]

∎

### Theorem Z2.5 — improved deep-rank thresholds

For the \(s=\operatorname{Cat}_{m-2}\) independently switchable
\(p=0\) MSW components, let \(\delta_R=C_2z_R\) be the effect at actual
set rank two, equivalently at depth \(q=m-2\).  Then:

1. For every \(m\ge7\), no orientation of all component coordinates makes
   the rank-two floor energy \(L^\natural\)-convex.

2. For every \(m\ge6\), some genuine orientation violates the direct
   \(M^\natural\)-exchange inequality.

#### Proof

Let

\[
L=[n]\setminus\{1,2,3,4\}.
\]

The exact rank-two four-arm formula has the form

\[
\delta_R
=
\sum_{t\in L}a_R(t)
\bigl(e_{\{3,t\}}-e_{\{2,t\}}\bigr),
\tag{6.2}
\]

where \(a_R(t)\in\{0,\pm1\}\), exactly two coefficients equal \(+1\),
exactly two equal \(-1\), and the other coefficients vanish.  In
particular,

\[
\sum_{t\in L}a_R(t)=0,
\qquad
\|\delta_R\|_2^2=8.
\]

Thus all effects lie in a space of dimension

\[
d=|L|-1=2m-4,
\tag{6.3}
\]

and all are nonzero.

At \(m=7\),

\[
\operatorname{Cat}_5=42>20=2(2m-4),
\]

and the Catalan ratio

\[
\frac{\operatorname{Cat}_{m-1}}{\operatorname{Cat}_{m-2}}
=\frac{4m-6}{m}
\]

dominates the succeeding linear-dimension ratio because

\[
\frac{4m-6}{m}
>
\frac{2(m+1)-4}{2m-4}
=\frac{m-1}{m-2}
\qquad(m\ge4);
\tag{6.4}
\]

after cross-multiplication the difference is
\(3m^2-13m+12>0\).  Hence

\[
\operatorname{Cat}_{m-2}>2(2m-4)
\qquad(m\ge7).
\]

If some orientation made the component cube \(L^\natural\)-convex, all
signed pairwise inner products would be nonpositive by (4.4), contradicting
Lemma Z2.4.

At \(m=6\),

\[
\operatorname{Cat}_4=14>8=2m-4,
\]

and this inequality also persists.  Therefore some two effects are
nonorthogonal.  Flip one component orientation, if necessary, to make
their inner product negative.  Equation (4.5) then gives a genuine direct
\(M^\natural\)-exchange violation.  ∎

This theorem concerns actual rank two and therefore depth \(m-2\).  It is
not itself a fixed Gaussian-window obstruction.  Theorem Z2.3 is the
separate fixed-window result.

## 7. Exact overload wall calculus

The overload objective is ambiently \(M\)-convex, but its curvature under
large component directions is not the collision Gram form.

Suppress the depth index and write \(W=cN+\rho\).  For a load \(\mu\) of
total \(W\), define

\[
D(\mu)=\sum_S(c-\mu(S))_+,
\qquad
p(\mu)=|\{S:\mu(S)\ge c+1\}|.
\tag{7.1}
\]

If

\[
T(\mu)=\sum_S(\mu(S)-c)_+,
\]

then conservation gives

\[
D=T-\rho,
\qquad
E:=\sum_S(\mu(S)-c-1)_+=T-p.
\]

Consequently

\[
\boxed{
O(\mu)=\max(D,E)=D(\mu)+(\rho-p(\mu))_+.
}
\tag{7.2}
\]

### Theorem Z2.6 — exact component-face curvature for overload

Let \(u,v\) be two legal zero-total load effects such that all four vectors
below are nonnegative loads of total \(W\), and put

\[
\mu_{ab}=\mu+au+bv,
\qquad a,b\in\{0,1\}.
\]

The exact mixed difference

\[
\kappa_O
=O(\mu_{11})-O(\mu_{10})-O(\mu_{01})+O(\mu_{00})
\]

is

\[
\begin{aligned}
\kappa_O
=&\sum_S\bigl[
(c-\mu_S-u_S-v_S)_+
-(c-\mu_S-u_S)_+\\
&\hspace{27mm}
-(c-\mu_S-v_S)_+
+(c-\mu_S)_+
\bigr]\\
&+(\rho-p_{11})_+
-(\rho-p_{10})_+
-(\rho-p_{01})_+
+(\rho-p_{00})_+,
\end{aligned}
\tag{7.3}
\]

where \(p_{ab}=p(\mu_{ab})\).

For squarefree cell effects \(u_S,v_S\in\{-1,0,1\}\), the first-line
deficit hinge contributes:

- \(+1\) when \(u_S=v_S=+1\) and \(\mu_S=c-1\);
- \(+1\) when \(u_S=v_S=-1\) and \(\mu_S=c+1\);
- \(-1\) when \(u_S=-v_S\ne0\) and \(\mu_S=c\);
- \(0\) otherwise.

The last line of (7.3) is an additional nonseparable curvature supported
at the global wall \(p=\rho\).

#### Proof

Substitute (7.2) at the four vertices.  The scalar table follows by checking
the three possible relative positions of \(\mu_S\) at the hinge \(c\).
No other values can contribute because the scalar positive-part function
is affine away from its single kink.  ∎

If all four vertices have \(p\ge\rho\), the global bonus vanishes and only
the displayed deficit table remains.  If all four have \(p\le\rho\), one
may instead use \(O=E\); the analogous ceiling-hinge table is supported at
\(c,c+1,c+2\).  Only a face meeting the global wall \(p=\rho\) has the
extra bonus curvature.

This proves why \(\langle u,v\rangle\) alone cannot determine overload
curvature.  Even abstract zero-total squarefree faces can have either sign.
No such abstract face is being asserted to be exact-factor realizable.

### Transposition antipodal test

On a transposition component cube, let

\[
h(I)=O(F_I).
\]

Component equivariance and relabelling invariance give the exact symmetry

\[
h(I)=h(I^c).
\tag{7.4}
\]

If \(h\) were submodular, applying submodularity to \(I,I^c\) would give

\[
h(I)\ge h(\varnothing)
\qquad\text{for every }I.
\tag{7.5}
\]

If \(h\) were \(M^\natural\)-convex, applying the direct exchange to the
two antipodal corners would give

\[
h(\{K\})\le h(\varnothing)
\qquad\text{for every component }K.
\tag{7.6}
\]

Thus any nonconstant overload edge would yield orientation-dependent
component obstructions to both signs.  What remains unsupported is the
needed genuine assertion that a prescribed-window MSW overload cube is
nonconstant at a suitable quota wall.  The quadratic fixed-window
obstruction of Theorem Z2.3 does not prove this.

## 8. The correct floor-energy Graver theorem

The floor energy is separable in the load variables, not in the wreath
indicators.  For integer vectors write \(a\sqsubseteq b\) when
\(a_i b_i\ge0\) and \(|a_i|\le|b_i|\) in every coordinate.  For an integer
matrix \(M\), \(\mathcal G(M)\) denotes the nonzero
\(\sqsubseteq\)-minimal vectors in \(\ker_{\mathbb Z}M\).

Introduce

\[
\widehat A_H
=
\begin{pmatrix}
A_m&0\\
B_H&-I
\end{pmatrix},
\qquad
B_Hx=(B_qx)_{q\le H},
\tag{8.1}
\]

and the genuine positive box fibre

\[
\widehat{\mathcal F}_H
=
\left\{
(x,u)\in\mathbb Z:
\widehat A_H(x,u)=\binom{\mathbf1}{0},\quad
0\le x\le1,\quad
0\le u\le W\mathbf1
\right\}.
\tag{8.2}
\]

This fibre is in bijection with exact factors.  The box cannot be omitted:
without it one optimizes on a larger signed integral fibre.

### Theorem Z2.7 — exact lifted local/global optimality

For \(z=(x,u)\in\widehat{\mathcal F}_H\), the following are equivalent:

1. \(z\) globally minimizes \(\Psi_H\);
2. there is no feasible improving augmentation \(\lambda g\), with
   
   \[
   g\in\mathcal G(\widehat A_H),
   \qquad
   \lambda\in\mathbb Z_{>0}.
   \]

Every feasible nonzero scaled augmentation has \(\lambda=1\).

Moreover, if \(z^*=(x^*,u^*)\) is better than \(z\) by gap

\[
G=\Psi_H(z)-\Psi_H(z^*)>0,
\]

then some applicable lifted Graver move improves \(z\) by at least

\[
\frac{G}
{|\operatorname{supp}x\setminus\operatorname{supp}x^*|}
\ge
\frac G{\operatorname{Cat}_m}.
\tag{8.3}
\]

#### Proof

Conformally decompose

\[
z^*-z=g^1+\cdots+g^t,
\qquad
g^j\in\mathcal G(\widehat A_H).
\]

Every individual partial augmentation lies coordinatewise between the two
positive boxed endpoints and is therefore feasible.  For each load
coordinate the univariate objective has nonnegative discrete second
difference.  For conformal increments this gives

\[
\Psi_H\!\left(z+\sum_jg^j\right)-\Psi_H(z)
\ge
\sum_j\bigl(\Psi_H(z+g^j)-\Psi_H(z)\bigr).
\tag{8.4}
\]

A better endpoint therefore forces an improving Graver summand.

Every nonzero projected summand has both wreath signs, because all columns
of \(A_m\) have the same size.  Its negative support consumes at least one
distinct coordinate of
\(\operatorname{supp}x\setminus\operatorname{supp}x^*\).  Conformality and
the binary endpoint difference make these negative supports disjoint, so

\[
t\le
|\operatorname{supp}x\setminus\operatorname{supp}x^*|
\le\operatorname{Cat}_m.
\]

Equation (8.3) follows from (8.4).  Conversely, an improving feasible
Graver augmentation contradicts global optimality.

Finally, a nonzero kernel vector of \(\widehat A_H\) has nonzero wreath
part: zero wreath part forces zero load part.  If both \(x\) and
\(x+\lambda g_x\) are binary, then
\(\lambda|g_{x,C}|\le1\) on a nonzero coordinate, so \(\lambda=1\).  ∎

### Feasible lifted packets between two factors

For a nonempty ownership component union \(J\), put

\[
z_J=\sum_{K\in J}z_K,
\qquad
v_J=B_Hz_J.
\]

Among augmented moves feasible between the two factor vertices,

\[
\boxed{
(z_J,v_J)\in\mathcal G(\widehat A_H)
\iff
\text{there is no nonempty proper }I\subsetneq J
\text{ with }v_I\sqsubseteq v_J.
}
\tag{8.5}
\]

Indeed, a squarefree conformal middle-kernel submove must be constant on
each connected ownership component, hence must be a component union.  The
lower augmented equations then force its load part to be the corresponding
\(v_I\).  This proves (8.5).

Thus every single connected ownership component is a feasible lifted
Graver move, but cancellation-minimal disconnected unions can also be
lifted Gravers.  Formula (8.5) characterizes the Gravers feasible between
the chosen factor vertices, not the entire unrestricted Graver basis.

## 9. A disconnected augmented-Graver packet in every admissible window

The fixed-window pair from Theorem Z2.3 gives an explicit packet.

### Theorem Z2.8 — two-component primitive

Let \(X\) be the MSW factor, and define exact endpoints

\[
F=X+z_1,
\qquad
G=X+z_0,
\qquad
\xi=G-F=z_0-z_1.
\tag{9.1}
\]

For every \(m\ge4\) and \(2\le H\le m-1\), put \(v=B_H\xi\).  Then

\[
(\xi,v)\in\mathcal G(\widehat A_H).
\tag{9.2}
\]

Its wreath projection is disconnected and conformally decomposes in the
ordinary middle kernel as the two connected component moves \(z_0\) and
\(-z_1\).

#### Proof

At the common depth-two core \(K\) in (5.10), the same-oriented effects
\(C_{m-2}z_0\) and \(C_{m-2}z_1\) agree on both coordinates of
\(\partial K\).  In \(v=B_H(z_0-z_1)\), those coordinates cancel to zero,
while each proper component effect is nonzero there.  Hence neither
\(B_Hz_0\) nor \(-B_Hz_1\) is conformal to \(v\).  Appending deeper ranks
cannot remove this zero-coordinate obstruction.

The ownership overlay between \(F\) and \(G\) has exactly these two
connected components.  Every conformal squarefree middle-kernel submove of
\(\xi\) is therefore one of

\[
0,
\quad z_0,
\quad -z_1,
\quad \xi.
\]

The two proper nonzero choices fail lower-load conformality, so (8.5)
proves (9.2).  ∎

This is a genuine fixed-window basis obstruction.  It proves that connected
ownership components are not the full lifted Graver test set.  It does not
by itself exhibit a nonglobal factor that is locally minimal under every
connected component for the particular objective.

## 10. The exact mobile-overload lift

The true overload needs a larger augmentation because the high quota is
chosen jointly with the factor.

For every \(q\le H\), introduce nonnegative integral vectors

\[
h_q,s_q,p_q,d_q
\]

satisfying

\[
h_q+s_q=\mathbf1,
\qquad
\mathbf1^\top h_q=\rho_q,
\tag{10.1}
\]

and

\[
B_qx-h_q-p_q+d_q=c_q\mathbf1.
\tag{10.2}
\]

Integrality in (10.1) makes \(h_q\) the indicator of the \(\rho_q\) high
quotas.  Concatenate the blocks and let \(R\) take the sum of each
\(h_q\)-block.  The full equality matrix, in variable order
\((x,h,s,p,d)\), is

\[
\mathcal A_H^{\mathrm{ov}}
=
\begin{pmatrix}
A_m&0&0&0&0\\
B_H&-I&0&-I&I\\
0&I&I&0&0\\
0&R&0&0&0
\end{pmatrix},
\tag{10.3}
\]

with right-hand side

\[
\left(
\mathbf1,
(c_q\mathbf1)_q,
\mathbf1,
(\rho_q)_q
\right).
\tag{10.4}
\]

Define the linear objective

\[
J(x,h,s,p,d)
=
\sum_{q\le H}\frac{\mathbf1^\top p_q}{c_q}.
\tag{10.5}
\]

### Lemma Z2.9 — exact auxiliary minimization

For every fixed exact factor \(x\),

\[
\min_{h,s,p,d}J(x,h,s,p,d)
=
\overline J_H(x)
:=
\sum_{q\le H}\frac{O_q(B_qx)}{c_q}.
\tag{10.6}
\]

#### Proof

Fix one row and write \(\delta_S=\mu(S)-c\),

\[
T=\sum_{\delta_S\ge1}\delta_S,
\qquad
a=|\{S:\delta_S\ge1\}|.
\]

For fixed high-quota indicator \(h\), (10.2) is minimized by

\[
p=(\delta-h)_+,
\qquad
d=(h-\delta)_+.
\]

Placing a high quota on a positive \(\delta_S\) decreases
\(\mathbf1^\top p\) by one.  Thus

\[
\min\mathbf1^\top p
=T-\min(\rho,a).
\]

Since

\[
D^-=T-\rho,
\qquad
D^+=T-a,
\]

this is

\[
\max(D^-,D^+)=O(\mu).
\]

Summing the rows with weights \(1/c_q\) proves (10.6).  ∎

### Theorem Z2.10 — decorated-Graver local/global theorem

Let the auxiliaries of the current factor \(x\) be chosen optimally, so its
decorated objective is \(\overline J_H(x)\).  If \(x\) is not globally
optimal, then an applicable Graver element of
\(\mathcal A_H^{\mathrm{ov}}\) changes the factor to another exact factor
\(x'\) such that, after auxiliary reoptimization,

\[
\overline J_H(x')-\overline J_H^*
\le
\left(1-\frac1{\operatorname{Cat}_m}\right)
\bigl(\overline J_H(x)-\overline J_H^*\bigr).
\tag{10.7}
\]

A global optimum is reachable through at most
\(\operatorname{Cat}_m\) strict factor-changing decorated-Graver moves.

#### Proof

Let \(z\) be the current auxiliary-optimal decorated state and let \(z^*\)
be a global decorated optimizer.  Take a conformal Graver decomposition

\[
z^*-z=g^1+\cdots+g^t.
\]

All individual and partial augmentations are nonnegative and satisfy the
same equalities.  Since \(J\) is linear, write

\[
\gamma_i=J(z+g^i)-J(z).
\]

Every \(\gamma_i\le0\): if \(\gamma_i>0\), then the feasible point
\(z^*-g^i\) would have objective \(J(z^*)-\gamma_i<J(z^*)\), contradicting
global optimality.

If \(g^i\) has zero wreath part, then \(z+g^i\) is another decoration of
the same current factor.  Current auxiliary optimality gives
\(\gamma_i\ge0\), so every such vertical summand has \(\gamma_i=0\).

Every factor-changing projected summand has both wreath signs.  The
negative supports of their conformal projections are disjoint subsets of
\(\operatorname{supp}x\setminus\operatorname{supp}x^*\).  Hence at most

\[
|\operatorname{supp}x\setminus\operatorname{supp}x^*|
\le\operatorname{Cat}_m
\]

summands change the factor, and all objective decrease comes from them.
One decreases the decorated gap by at least its reciprocal count.  Further
reoptimizing its new factor can only improve the objective, proving
(10.7).

Apply all strictly negative factor-changing summands from one conformal
decomposition toward \(z^*\).  Arbitrary partial conformal sums are
feasible, and the omitted summands have zero objective change.  The result
has global objective after at most \(\operatorname{Cat}_m\) strict factor
changes.  ∎

For \(H=\lceil A\sqrt m\rceil\le m-1\), as holds eventually for every fixed
\(A\), the global value is exactly the fixed-window overload minimum.
Theorem Z2.10 contracts the gap to that minimum; it does not prove that the
minimum is \(o(W)\).

## 11. The fixed-window packet also occurs in the overload Graver basis

Keep \(\xi=z_0-z_1\) and put

\[
v=B_H\xi,
\qquad
v^+=(\max(v_i,0))_i,
\qquad
v^-=(-\min(v_i,0))_i.
\]

### Theorem Z2.11 — overload-lift primitive

For every \(m\ge4\) and \(2\le H\le m-1\),

\[
g^{\mathrm{ov}}
=
(\xi,0,0,v^+,v^-)
\in
\mathcal G(\mathcal A_H^{\mathrm{ov}}).
\tag{11.1}
\]

#### Proof

The kernel equations hold because

\[
B_H\xi-v^++v^-=0.
\]

Let a nonzero kernel vector

\[
g'=(\xi',\eta',\sigma',\pi',\kappa')
\sqsubseteq g^{\mathrm{ov}}.
\]

The zero \(h,s\) coordinates of \(g^{\mathrm{ov}}\) force

\[
\eta'=\sigma'=0.
\]

Ownership connectivity between the two exact endpoints forces

\[
\xi'\in\{0,z_0,-z_1,\xi\}.
\]

The load equation gives

\[
B_H\xi'=\pi'-\kappa',
\qquad
0\le\pi'\le v^+,
\qquad
0\le\kappa'\le v^-.
\]

If \(\xi'=0\), disjointness of the supports of \(v^+,v^-\) forces
\(\pi'=\kappa'=0\).  The two proper component choices are impossible
because the depth-two cancellation coordinate makes neither proper effect
conformal to \(v\).  Finally \(\xi'=\xi\) forces
\(\pi'=v^+\) and \(\kappa'=v^-\).  Thus no proper nonzero conformal kernel
subvector exists.  ∎

This is a strict basis statement, not an optimized-overload curvature
statement.  From any feasible decoration of \(F\), including an
auxiliary-optimal one, adding \(g^{\mathrm{ov}}\) itself pads the
surplus/deficit slacks and is feasible, but this direction increases \(J\).  Its
improving reverse begins at that padded decoration, which need not be
auxiliary-optimal.  Therefore Theorem Z2.11 does not produce a nonglobal
component-local overload factor and does not determine the four optimized
overload values on the component face.

## 12. Exact conclusions and unsupported statements

### Proved

1. Balanced mobile-quota overload is \(M\)-convex on the unrestricted
   fixed-total load lattice, by the integral flow exchange proof of
   Theorem Z2.1.

2. Floor collision energy is separable \(M\)-convex on the same lattice and
   separable \(L^\natural\)-convex before imposing the fixed-total slice.

3. The genuine exact-factor domain is neither \(M\)-,
   \(M^\natural\)-, nor \(L^\natural\)-convex for every \(m\ge2\).

4. Every nonsingleton exact rank-load image has no nontrivial unit target
   exchange because of its fixed point margins.  The depth-one image is
   nonsingleton for every \(m\ge3\).

5. Floor-energy component curvature is the weighted Gram matrix.

6. For every \(m\ge4\), the explicit genuine components (5.1) give a
   fixed-window depth-\(1,2\) face with exact mixed curvature
   \(\pm2/c_2\), yielding orientation-dependent
   \(L^\natural\)- and direct \(M^\natural\)-exchange failures.

7. At actual rank two, no component orientation gives
   \(L^\natural\)-convexity for \(m\ge7\); a direct
   \(M^\natural\)-violating orientation exists for \(m\ge6\).

8. Full augmented-Graver locality is equivalent to global floor-energy
   optimality on the positive exact-factor fibre.

9. Full decorated-Graver locality is equivalent to global optimized
   overload optimality, with the explicit
   \(1/\operatorname{Cat}_m\) gap-contraction constant.

10. For every \(m\ge4\) and \(2\le H\le m-1\), a literal two-component
    disconnected primitive occurs in both the floor lift and the full
    overload lift.

11. Overload component-face curvature obeys the exact quota-wall formula
    (7.3), not the collision Gram formula.

### Not proved

1. No genuine exact factor is shown to be a nonglobal local minimum under
   every connected ownership-component move for either objective.

2. No prescribed-window MSW overload face is proved nonconstant at the
   required quota wall.  The floor-energy obstruction cannot simply be
   transferred to overload.

3. The existence of a disconnected Graver primitive does not by itself
   prove that connected-component local optimality fails for the optimized
   overload objective; it proves that the exact Graver test set is larger.

4. No sub-factor support bound is proved for the relevant augmented Graver
   elements.

5. No estimate here bounds the global minimum by
   
   \[
   O_A(H\operatorname{Cat}_m)
   \quad\text{or}\quad o(W).
   \]

6. Nothing here constructs a literal OR word or a common labelled nested
   owner resolution.  The results are entirely integral and unlabelled
   inside one exact factor at every stage.

## 13. Audit record

The decisive fixed-window calculation was independently rederived from the
MSW flip recursion.  The audit separately checked:

- the lists (5.5)--(5.6);
- the unique common depth-two core for \(m\ge5\);
- the three signed coincidences and total \(2\) at \(m=4\);
- disjointness of the depth-one supports;
- realization of both coordinate orientations by genuine exact factors;
- persistence of the cancellation obstruction after appending all deeper
  ranks;
- exclusion of quota-selector, slack-only, and proper-component conformal
  submoves in the overload lift.

The ambient overload \(M\)-exchange proof was also independently audited at
the chosen-start-row path step and at the lower/upper quota capacities.  No
finite search, certificate data, web source, fractional-factor
substitution, or computation is used in this report.

## Final status

The discrete-convexity lane is exhausted in the following precise sense:

\[
\boxed{
\begin{array}{c}
\text{unrestricted histogram objectives: M-convex;}\\
\text{genuine exact-factor/component geometry: admits M/L obstructions;}\\
\text{full positive augmented-Graver neighborhoods: exact local/global.}
\end{array}
}
\]

The remaining MWB gate is not an exchange-axiom issue.  It is a quantitative
positive-fibre theorem asserting that the global optimized overload in
every fixed Gaussian window is \(o(W)\).  Graver descent reaches that global
value once a better positive endpoint exists, but supplies no bound on the
value itself.
