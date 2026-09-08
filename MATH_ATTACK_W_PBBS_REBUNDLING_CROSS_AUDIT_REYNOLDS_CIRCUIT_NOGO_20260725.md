# Lane W: PBBS rebundling cross-audit and a Reynolds necklace-circulation no-go

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, random
experiment, solver, or long-running computation is used.

Source audited:
MATH_ATTACK_R_PBBS_DEPENDENT_BALANCED_REBUNDLING_20260725.md.

## 0. Verdict

The two requested source claims survive, with sharply delimited corrections.

1. The two-piece theorem is correct as a **necessary allocation theorem**.
   Its prose overstates endpoint freedom: equal cores do not make an
   arbitrary permutation feasible. Legal cross-reassembly is governed by
   an exact phase-compatibility digraph. If all cores are distinct, the
   original seams are forced and the operated factor is literally
   unchanged on those wreaths.
2. The abstract Gaussian collision example is correct. For fixed
   \(A,c_0>0\), its precise scale is
   \[
   \Theta_{A,c_0}(W),
   \]
   with the exact leading constant proved in Section 3. It remains an
   abstract affine load system, not a PBBS or exact-factor obstruction.

The new circulation attack studies the full relabeling, or Reynolds, necklace
circulation of one exact factor. It fractionally annihilates every centered
target deviation at every depth. Its normalized complement leaves only a
\((D_m-1)^{-2}\) fraction of every centered quadratic necklace energy,
where
\[
D_m=\frac{m!(m+1)!}{2}.
\]
This is stronger than the required \(1-O(1/q)\) cancellation.

The family nevertheless has an exact one-copy obstruction:

* its nonnegative exact-ownership ray contains no second \(0/1\) point;
* its orbit polytope has the uniform fractional factor as barycentre, but
  every integral point is merely a relabeling of the original factor;
* all integral points have the same collision profile and the same
  optimized common survival-packet LP value.

Thus this concrete maximally nonlocal family supplies ideal necklace
cancellation only fractionally.  The displayed \((D_m-1)\)-copy identity is
only a nonnegative middle multicover identity; it does not prove a
factorization of the complement or endpoint-valid trade reachability.  It
gives no one-factor SPC improvement. This does not obstruct Graver hybrids
outside the relabeling-orbit polytope.

## 1. Corrected two-piece theorem

Put \(n=2m+1\), \(m\ge2\). For a middle-vertex path \(P\), write
\[
\zeta(P)=n\sum_{X\in V(P)}\mathbf1_X-m|V(P)|\mathbf1.
\tag{1.1}
\]

### Theorem 1.1 (closed two-piece allocation rigidity)

Let \(k\) pairwise vertex-disjoint exact \(n\)-wreaths be cut into intact
paths \(S_i,L_i\) satisfying
\[
|S_i|=3,\qquad |L_i|=n-3,
\tag{1.2}
\]
and
\[
\zeta(S_i)=\zeta_{K_i},\qquad
\zeta(L_i)=-\zeta_{K_i},\qquad
\zeta_K=n\mathbf1_K-(m-1)\mathbf1.
\tag{1.3}
\]
Suppose precisely these \(2k\) paths, with no imported pieces and no
subdivision, are resewn into simple point-regular \(n\)-cycles. Then every
output is
\[
S_i\cup L_{\sigma(i)}
\]
for a bijection \(\sigma\), and necessarily
\[
\boxed{K_i=K_{\sigma(i)}.}
\tag{1.4}
\]

#### Proof

If an output contains \(p\) short and \(\ell\) long paths, length gives
\[
3p+(n-3)\ell=n.
\tag{1.5}
\]
For \(n\ge7\), the only possibilities are \((p,\ell)=(1,1)\) and, if
\(3\mid n\), the short-only possibility \((n/3,0)\). Indeed
\(\ell\ge2\) would leave
\[
n-(n-3)\ell\le6-n<0.
\]
For \(n=5\), direct substitution gives only \((1,1)\).

All \(k\) long paths must be used. Each long-containing output uses one
long path, so there are at least \(k\) such outputs. Total vertex mass is
\(kn\), hence there are exactly \(k\) outputs. The short-only possibility
does not occur.

Point-regularity of \(S_i\cup L_j\) gives
\[
0=\zeta_{K_i}-\zeta_{K_j}.
\]
Coordinatewise expansion forces \(K_i=K_j\). \(\square\)

The source phrase “the only freedom is a permutation inside each
equal-core fibre” is correct only as an allocation restriction. Endpoint
feasibility can remove most or all such permutations.

The source's word “one-cut” means excision of one three-vertex arc, hence
deletion of two seams. It does not mean deletion of one factor edge.

## 2. Exact endpoint phase circuits

Fix a core \(K\in\binom{[n]}{m-1}\), and put
\[
T=[n]\setminus K.
\]
Orient one short path as
\[
S_i=
\bigl(
K\cup\{u_i\},\
T\setminus\{u_i,v_i\},\
K\cup\{v_i\}
\bigr).
\tag{2.1}
\]
The endpoints of its complementary long path have the form
\[
Y_i^u=T\setminus\{u_i,a_i\},\qquad
Y_i^v=T\setminus\{v_i,b_i\},
\tag{2.2}
\]
where \(u_i,v_i,a_i,b_i\) are distinct in a literal wreath. Define
\[
U_i=\{u_i,v_i\},\qquad A_i=\{a_i,b_i\}.
\tag{2.3}
\]

### Theorem 2.1 (equal-core phase-circuit classification)

Let \(i\ne j\) be vertex-disjoint source wreaths with common core \(K\).
Then \(S_i\cup L_j\) can be sewn into a simple point-regular \(n\)-cycle
if and only if
\[
\boxed{U_i=A_j.}
\tag{2.4}
\]
When (2.4) holds, the two seams are forced.

Consequently, nontrivial closed two-piece trades in one equal-core fibre
are exactly the permutations \(\sigma\) whose moved indices satisfy
\[
U_i=A_{\sigma(i)}.
\tag{2.5}
\]
On a moved cycle \((i_0,\ldots,i_{\ell-1})\), this is
\[
A_{i_{s+1}}=U_{i_s}\qquad(s\bmod\ell).
\tag{2.6}
\]
A two-cycle is the common-core alternating \(C_8\).

#### Proof

For \(x,y,z\in T\),
\[
(K\cup\{x\})\cap(T\setminus\{y,z\})=\varnothing
\quad\Longleftrightarrow\quad x\in\{y,z\}.
\tag{2.7}
\]
Since the two sources are vertex-disjoint, \(U_i\cap U_j=\varnothing\).
Thus both endpoints of \(S_i\) can meet the two endpoints of \(L_j\)
exactly when they are the auxiliary labels \(a_j,b_j\), which is (2.4).
The matching is then forced.

The paths are disjoint, have total length \(n\), and have total charge
\(\zeta_K-\zeta_K=0\). The forced seams therefore make a simple
point-regular \(n\)-cycle, hence a literal wreath.

For \(i=j\), the original seams exist. A second crossed seam matching
would make a \(C_4\) in \(KG(2m+1,m)\). This is impossible because two
distinct middle vertices have at most one common Kneser neighbour: the
complement of their union has size at most \(m\). Hence the original seams
are unique. \(\square\)

### Corollary 2.2 (physical obstruction to the advertised relations)

The source's four-core relation
\[
\zeta_A+\zeta_B=\zeta_C+\zeta_D
\]
cannot be implemented by a closed two-piece circuit when
\(A,B,C,D\) are distinct. A separated rotation orbit
\(\{\tau^jK:j\in\mathbb Z_n\}\) likewise contains no nontrivial
two-piece exact circuit because all its cores are distinct.

Thus extra cuts or imported neutral paths are genuinely necessary before
either algebraic relation reaches the necklace-cancellation problem.

## 3. Gaussian collision audit

Let
\[
N_q=\binom{2m+1}{m-q},\qquad
\rho_{m,q}=\frac W{N_q},\qquad
d_q=\lfloor\rho_{m,q}\rfloor,
\qquad H_m=\lceil A\sqrt m\rceil.
\tag{3.1}
\]

### Proposition 3.1 (Gaussian floor sum)

For fixed \(A>0\),
\[
\boxed{
\frac1m\sum_{q=1}^{H_m}\frac q{d_q}
\longrightarrow
I_1(A):=\int_0^A\frac{x\,dx}{\lfloor e^{x^2}\rfloor}>0.
}
\tag{3.2}
\]
Hence
\[
\sum_{q=1}^{H_m}\frac q{d_q}=\Theta_A(m).
\tag{3.3}
\]

#### Proof

The exact quotient is
\[
\rho_{m,q}=
\prod_{j=1}^q
\left(1+\frac{q+1}{m-q+j}\right).
\tag{3.4}
\]
Uniformly for \(q\le A\sqrt m+1\),
\[
\log\rho_{m,q}=\frac{q^2}{m}+O_A(m^{-1/2}).
\tag{3.5}
\]
Away from arbitrarily small neighbourhoods of the finitely many points
\(\sqrt{\log k}\in[0,A]\), the floored summands converge uniformly.
Those neighbourhoods have arbitrarily small normalized contribution, so
Riemann summation proves (3.2).

For a direct lower bound, put
\[
L_m=\left\lfloor
\min\left\{\frac A2,\frac14\right\}\sqrt m
\right\rfloor.
\]
For all sufficiently large \(m\), \(d_q=1\) on \(q\le L_m\), whence
\[
\sum_{q\le H_m}\frac q{d_q}
\ge\frac{L_m(L_m+1)}2=\Omega_A(m).
\]
The upper bound follows from \(d_q\ge1\). \(\square\)

### Theorem 3.2 (the abstract \(\Theta(W)\) example is sound)

Fix \(A,c_0>0\), and put
\[
P=\lfloor c_0t\rfloor.
\]
For all sufficiently large \(m\), the source construction exists
simultaneously for all \(q\le H_m\), with the same selector indices, and
has
\[
R_q=4q,\qquad L_q=2,\qquad Q_q=Pq
\tag{3.6}
\]
for every integral selector. Consequently
\[
\boxed{
\mathcal G_{H_m}
=P\sum_{q=1}^{H_m}\frac q{d_q}
=\left(\frac{c_0I_1(A)}2+o(1)\right)W.
}
\tag{3.7}
\]

#### Proof

At depth \(q\), one quota class contains at least \(N_q/2\) targets. The
construction needs \(2Pq\) distinct targets in that class. Uniformly over
the Gaussian window, \(\rho_{m,q}=O_A(1)\), and
\[
\frac{2Pq}{N_q}
\le
\frac{2c_0q}{2m+1}\rho_{m,q}
=O_{A,c_0}(m^{-1/2}),
\tag{3.8}
\]
so enough targets exist.

For a same-level pair \((h,h)\), use states
\[
(h-1,h+1),\qquad(h+1,h-1).
\]
Their midpoint is \((h,h)\), they remain nonnegative because \(d_q\ge1\),
and either state contributes exactly one unit to \(Q_q\). One selector
uses \(q\) disjoint pairs, so its full endpoint difference has
\(\ell^1\)-norm \(4q\). Global target disjointness gives congestion two,
and every selector contributes exactly \(q\), independently of all other
selector states. Equation (3.7) follows from Proposition 3.1 and
\(t\sim W/(2m)\). \(\square\)

The exact notation is \(\Theta_{A,c_0}(W)\) unless \(c_0\) is suppressed
as fixed data. More importantly, the selected targets at different depths
are unrelated. Reusing the same selector bit does not provide nested target
flags, common physical owners, endpoint seams, PBBS increments, or an
exact factor. The theorem is a sharp logical obstruction to a
slab-plus-\(R_q=\Theta(q)\) argument, not to \(\mathrm{SPC}_A\).

## 4. The Reynolds necklace circulation

Let \(\mathscr W_m\) be the set of all unoriented wreath supports. For
\(0\le q\le m-1\), let \(A_q\) be the incidence matrix between wreaths
and length-\((m-q)\) cyclic intervals; \(A_0\) is middle incidence.

Every middle set belongs to exactly
\[
D=D_m=\frac{m!(m+1)!}{2}
\tag{4.1}
\]
wreaths, and
\[
|\mathscr W_m|=tD,\qquad
A_0\mathbf1_{\mathscr W_m}=D\mathbf1.
\tag{4.2}
\]
Indeed, with a fixed middle set distinguished as one cyclic window, order
its \(m\) elements and the \(m+1\) complementary elements on the two
consecutive arcs. This gives \(m!(m+1)!\) directed cyclic orders; reversal
acts freely and divides the count by two. Double-counting middle-set/wreath
incidences then gives \(|\mathscr W_m|=WD/n=tD\).

Fix an exact factor \(F\), with indicator \(f=\mathbf1_F\), so
\[
A_0f=\mathbf1.
\]
Define
\[
\boxed{
z_F=\mathbf1_{\mathscr W_m}-Df
=\mathbf1_{\mathscr W_m\setminus F}-(D-1)f.
}
\tag{4.3}
\]

### Lemma 4.1 (exact middle kernel and uniform depth load)

For every \(q\),
\[
A_0z_F=0,
\tag{4.4}
\]
and, writing
\[
\lambda_q=\frac W{N_q},
\]
one has
\[
A_q\mathbf1_{\mathscr W_m}=D\lambda_q\mathbf1.
\tag{4.5}
\]

#### Proof

Equation (4.4) follows from (4.2). The symmetric group is transitive on
rank-\((m-q)\) targets, so the left side of (4.5) is constant. The
fractional vector \(D^{-1}\mathbf1_{\mathscr W_m}\) has total wreath mass
\(t\). Every wreath contributes \(n\) targets, hence total load \(nt=W\).
Division by \(N_q\) proves (4.5). \(\square\)

## 5. Exact simultaneous cancellation

Define the exact-ownership affine ray
\[
x(\alpha)=f+\alpha z_F.
\tag{5.1}
\]
Put
\[
\mu_q=A_qf,\qquad e_q=\mu_q-\lambda_q\mathbf1.
\tag{5.2}
\]

### Theorem 5.1 (all depths and all necklace charges scale together)

For every \(q\),
\[
\boxed{
A_qx(\alpha)-\lambda_q\mathbf1
=(1-D\alpha)e_q.
}
\tag{5.3}
\]
In particular,
\[
x_*:=x(1/D)=\frac1D\mathbf1_{\mathscr W_m}
\tag{5.4}
\]
has perfectly uniform loads at every depth, while the normalized complement
\[
y_F:=x(1/(D-1))
=\frac{\mathbf1_{\mathscr W_m}-f}{D-1}
\tag{5.5}
\]
satisfies
\[
\boxed{
A_qy_F-\lambda_q\mathbf1=-\frac1{D-1}e_q.
}
\tag{5.6}
\]

Fix any cyclic ground rotation and any target necklace
\(\mathcal O\subseteq\binom{[n]}{m-q}\). Define its centered charge by
\[
c_{q,\mathcal O}(x)=
\sum_{S\in\mathcal O}
\bigl((A_qx)(S)-\lambda_q\bigr).
\tag{5.7}
\]
Then
\[
\boxed{
c_{q,\mathcal O}(x(\alpha))
=(1-D\alpha)c_{q,\mathcal O}(f).
}
\tag{5.8}
\]

#### Proof

Lemma 4.1 gives
\[
A_qz_F=D\lambda_q\mathbf1-D\mu_q=-De_q.
\]
Substitution proves (5.3), and summing it on one necklace proves (5.8).
\(\square\)

### Corollary 5.2 (the required \(1-O(1/q)\) cancellation is exceeded)

For nonnegative weights \(w_q\), put
\[
\mathcal E_H(x)=
\sum_{q\le H}w_q
\|A_qx-\lambda_q\mathbf1\|_2^2.
\tag{5.9}
\]
Then
\[
\mathcal E_H(x(\alpha))
=(1-D\alpha)^2\mathcal E_H(f),
\tag{5.10}
\]
and
\[
\boxed{
\mathcal E_H(y_F)=\frac1{(D-1)^2}\mathcal E_H(f).
}
\tag{5.11}
\]
For \(m\ge2\), \(D-1\ge m\). Hence for every \(1\le q\le m-1\),
\[
\frac1{(D-1)^2}\le\frac1q.
\tag{5.12}
\]
Thus the normalized complement cancels at least a \(1-1/q\) fraction of
centered depth-\(q\) energy, simultaneously at every depth. The uniform
point cancels all of it.

This concerns fractional centered energy. If
\(\lambda_q=d_q+\theta_q\) and \(f\) is integral, then
\[
\boxed{
Q_q(A_qf)=
\frac12\left(
\|e_q\|_2^2-N_q\theta_q(1-\theta_q)
\right).
}
\tag{5.13}
\]
The subtracted Bernoulli term is an integrality variance. The polynomial
extension of \(Q_q\) at \(x_*\) can be negative, so fractional energy
cancellation is not an integral collision conclusion.

## 6. Exact one-copy obstruction

### Theorem 6.1 (no nontrivial \(0/1\) point on the ray)

For \(m\ge2\), the nonnegative part of the ray is
\[
0\le\alpha\le\frac1{D-1},
\]
and
\[
\boxed{
x(\alpha)\in\{0,1\}^{\mathscr W_m}
\quad\Longleftrightarrow\quad
\alpha=0.
}
\tag{6.1}
\]

#### Proof

The coordinates are
\[
x(\alpha)(E)=
\begin{cases}
1-(D-1)\alpha,&E\in F,\\
\alpha,&E\notin F.
\end{cases}
\tag{6.2}
\]
This gives the nonnegative interval. An outside coordinate being integral
forces \(\alpha\in\{0,1\}\). Since \(D\ge6\), only \(\alpha=0\) lies in the
nonnegative interval. \(\square\)

Equivalently, the two-level integer kernel vector (4.3) first becomes a
nonnegative integral multicover identity at multiplicity \(D-1\):
\[
(D-1)f+z_F=\mathbf1_{\mathscr W_m\setminus F}.
\tag{6.3}
\]
More generally, a two-level vector
\[
a\mathbf1_{\mathscr W_m\setminus F}-bf
\]
lies in the middle kernel exactly when \(b=a(D-1)\). Thus \(D-1\) is the
exact two-level nonnegativity toll in this family.  This proves neither a
resolution of the complement into exact factors nor reachability by
endpoint-valid trades.

## 7. Orbit-polytope trap

Let
\[
\mathcal O(F)=\{\pi F:\pi\in S_n\},
\qquad
\mathcal P(F)=
\operatorname{conv}\{\mathbf1_G:G\in\mathcal O(F)\}.
\tag{7.1}
\]

### Theorem 7.1 (uniform barycentre and rigid integral points)

\[
\boxed{
\frac1D\mathbf1_{\mathscr W_m}\in\mathcal P(F),
}
\tag{7.2}
\]
but
\[
\boxed{
\mathcal P(F)\cap\{0,1\}^{\mathscr W_m}
=
\{\mathbf1_{\pi F}:\pi\in S_n\}.
}
\tag{7.3}
\]

#### Proof

Average \(\mathbf1_{\pi F}\) over \(S_n\). Transitivity on wreaths makes
every inclusion probability equal. The average selects \(t\) of the
\(tD\) wreaths, so that probability is \(1/D\), proving (7.2).

Let a \(0/1\) vector \(y\) be a convex combination of orbit indicators.
At a coordinate where \(y=1\), every positively weighted summand must be
one; where \(y=0\), every such summand must be zero. Hence every positive
summand equals \(y\), proving (7.3). \(\square\)

### Corollary 7.2 (no collision or packet gain in the orbit)

For every \(\pi\in S_n\),
\[
Q_q(\pi F)=Q_q(F).
\tag{7.4}
\]
For \(K\le m-1\), define the optimized common packet value
\[
\Theta_K(F)=
\min_{\beta\ {\rm balanced}}\vartheta_K(F,\beta).
\tag{7.5}
\]
Then
\[
\boxed{\Theta_K(\pi F)=\Theta_K(F).}
\tag{7.6}
\]

#### Proof

A coordinate permutation only permutes target labels and owner rows, so it
preserves every load histogram. Transporting quota positions and packet
weights gives a cost-preserving bijection between the packet LPs of
\(F\) and \(\pi F\). \(\square\)

Thus arbitrary dependent rounding confined to \(\mathcal P(F)\) can only
return a relabeling with exactly the original integral collision and packet
value, despite the perfectly balanced fractional barycentre.

The Reynolds circulation is genuinely in the span of exact-factor
differences. If the distinct orbit has size \(M\), then
\[
\sum_{G\in\mathcal O(F)}\mathbf1_G
=\frac MD\mathbf1_{\mathscr W_m},
\]
and
\[
\sum_{G\in\mathcal O(F)}(\mathbf1_G-f)
=\frac MDz_F.
\tag{7.7}
\]
The failure is therefore not linear ownership feasibility; it is the lack
of a nontrivial one-copy \(0/1\) endpoint inside this circulation family.
Here \(z_F\) is a Reynolds kernel direction.  It is not claimed to be a
support-minimal circuit or a Graver move.  Also, only the uniform point
\(D^{-1}\mathbf1\) is proved to lie in the orbit polytope; the normalized
complement point need not lie there.

## 8. Final proved and unproved boundary

### Proved

1. The source's two-piece length-and-core rigidity is correct.
2. Equal core is only a necessary allocation condition; legal outputs are
   exactly the phase circuits (2.5)--(2.6).
3. Distinct-core two-piece reassembly is literally unchanged.
4. The abstract Gaussian example has exact asymptotic (3.7), with constants
   depending on \(A,c_0\), and has no PBBS/exact-factor implication.
5. The Reynolds circulation preserves exact middle ownership and scales
   every centered load and necklace charge by one common scalar.
6. It fractionally achieves at least the required \(1-1/q\) cancellation
   throughout the whole proper depth range.
7. Its one-copy nonnegative ray has no second integral point.
8. Its orbit polytope has a perfectly balanced fractional barycentre, but
   every integral point is a relabeling with unchanged collision and
   optimized packet LP.

### Not proved

1. No exact factor with common packet LP \(O_A(t/m)\) is constructed.
2. The Reynolds no-go does not apply to support-feasible Graver hybrids
   that leave the orbit polytope.
3. Extra-cut cross-core circuits with mixed necklace-charge covariance are
   not ruled out.
4. Fractional centered-energy cancellation is not a literal contiguous-OR
   construction.
5. The \((D_m-1)\)-fold complement identity is not a resolution into exact
   factors and supplies no endpoint-valid trajectory.
6. The Reynolds direction is not proved support-minimal or Graver-primitive.

This concrete circulation family is exhausted: Reynolds averaging gives ideal
simultaneous necklace cancellation, but exact integrality collapses every
permitted one-factor endpoint to the original relabeling orbit. A successful
\(\mathrm{SPC}_A\) circuit must leave that polytope and use endpoint-valid
ownership-component hybrids with extra cuts.
