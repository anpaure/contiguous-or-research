# Lane Z: exact no-go for static orbit averaging and a floor-entropy potential

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver,
certificate, or computational experiment is used.

## 0. Verdict

Static coordinate-orbit averaging cannot bound the positive exact-factor
minimum of the fixed-window floor-corrected energy.  This is an exact
integral obstruction, not merely a failure of a particular estimate.

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=W/n=\operatorname{Cat}_m.
\]

For every exact factor \(F\), the indexed full coordinate orbit

\[
\mathcal U(F)=\biguplus_{\sigma\in S_n}\sigma F
\]

is the same uncoloured wreath multicover:

\[
\boxed{\mathcal U(F)=2W\,\mathbf 1_{\Omega_m}.}
\tag{0.1}
\]

Here \(\Omega_m\) denotes unoriented cyclic orders modulo rotation and
reversal.  At every lower rank its aggregate load is perfectly uniform.
Nevertheless, for every relabelling-invariant functional \(\Phi\),

\[
\boxed{
\min_{\mathscr D\vdash\mathcal U(F)}
 \frac1{n!}\sum_{G\in\mathscr D}\Phi(G)
=
\min_{G\text{ exact}}\Phi(G),
}
\tag{0.2}
\]

where \(\mathscr D\) ranges over decompositions of the multicover into
literal positive exact factors.  The analogous identity with the maximum
over blocks also holds.  Thus exact reblocking of the balanced orbit is
neither a relaxation nor an intermediate theorem: its optimum is exactly
the original one-factor optimum.

There is a universal convex-potential identity behind this obstruction.
For a convex scalar potential \(\varphi\), subtract the chord through the
two integer floor points \(c,c+1\).  The resulting integral floor excess
\(E_{\varphi,q}\) is nonnegative, but full-orbit Jensen averaging has exact
gap

\[
\boxed{
\mathbb E_\sigma E_{\varphi,q}(\sigma F)
-E_{\varphi,q}(\mathbb E_\sigma\mu_q^{\sigma F})
=E_{\varphi,q}(F)+\beta_{\varphi,q},
}
\tag{0.3}
\]

where \(\beta_{\varphi,q}\ge0\) is the compulsory fractional floor gap.
For quadratic energy, \(\beta_{\varphi,q}=N_q\theta_q(1-\theta_q)\).
For the corridor potential it is zero, but the orbit retains the entire
corridor energy exactly.  Hence Jensen convexity points in the wrong
direction for an upper bound.

For entropy this becomes an exact information identity.  If
\(p_q^F=\mu_q^F/W\), \(u_q\) is uniform, \(\Sigma\) is a uniform coordinate
permutation, and \(X\mid\{\Sigma=\sigma\}\sim p_q^{\sigma F}\), then

\[
\boxed{
X\sim u_q,
\qquad
I(X;\Sigma)=D(p_q^F\|u_q).
}
\tag{0.4}
\]

Orbit averaging does not dissipate load entropy; it converts all of it
into information about the coordinate frame.

The floor-corrected entropy itself is a valid alternative discrete
potential.  If \(\eta_c\) is defined in (4.1), then for every integral load
\(t\),

\[
\boxed{
\eta_c(t)\ge \frac1{c+2}
\operatorname{dist}(t,\{c,c+1\}).
}
\tag{0.5}
\]

Consequently, on every fixed Gaussian window,

\[
\mathcal C_H(F)
\le3\sum_{q\le H}\sum_S\eta_{c_q}(\mu_q^F(S)).
\tag{0.6}
\]

Thus an \(o(W)\) entropy-excess factor would prove the fixed-window
overload theorem and hence feed the frozen constant-one diagonalization.
But orbit averaging and augmented-Graver descent do not bound that entropy
minimum: their exact reblocking optimum is again (0.2).

Finally, the canonical common-owner implementation collapses before
reblocking.  For \(S_n\), and already for the point stabilizer
\(S_{n-1}\), the joined owner partition has one block.  The latter group
annihilates every admissible centered lower-rank load, yet its only static
owner-block children are whole relabellings \(gF\), with exactly zero drift
for every relabelling-invariant energy.  This is complete restitution of
perfect coherent smoothing.

These theorems close the **static orbit** architecture: aggregate orbit
convexity, static common-owner Haar heat, and coloured full-orbit Graver
reblocking.  They do not rule out adaptively recomputing ownership
components after nontrivial choices or constructing new perfect matchings
inside combined supports.  Such an argument would use information not
present in the orbit barycentre and would constitute a genuine positive
exact-factor theorem.

## 1. Exact-factor notation

Let \(\Omega_m\) be the set of cyclic orders on \([n]\), modulo rotation
and reversal.  For \(C\in\Omega_m\), let \(a_C\) be the incidence vector
of its \(n\) cyclic middle \(m\)-sets.  A positive exact factor is

\[
F\subseteq\Omega_m,
\qquad
\sum_{C\in F}a_C=\mathbf1_{\binom{[n]}m}.
\tag{1.1}
\]

Every factor has exactly \(B\) rows, because every row contains \(n\)
middle sets:

\[
n|F|=W,\qquad |F|=B.
\tag{1.2}
\]

At depth \(q\), put

\[
r_q=m-q,
\qquad
N_q=\binom n{r_q},
\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q,
\tag{1.3}
\]

where \(c_q=\lfloor\lambda_q\rfloor\), \(0\le\theta_q<1\), and

\[
W=c_qN_q+\rho_q,
\qquad
\rho_q=N_q\theta_q\in\mathbb Z.
\tag{1.4}
\]

Let \(\mu_q^F(S)\) count the rows of \(F\) in which \(S\) is a cyclic
rank-\(r_q\) interval.  Then

\[
\sum_S\mu_q^F(S)=W.
\tag{1.5}
\]

All factors, orbit blocks, and reblockings below are squarefree positive
exact factors.  No signed or fractional object is used as an endpoint.

## 2. Full-orbit erasure and exact reblocking

Retain the permutation indices and define the wreath-copy multiset

\[
\mathcal U(F)=\biguplus_{\sigma\in S_n}\sigma F.
\tag{2.1}
\]

### Theorem Z6.1 -- full-orbit erasure

Every \(C\in\Omega_m\) occurs in \(\mathcal U(F)\) exactly \(2W\) times.
Consequently \(\mathcal U(F)\) is independent of \(F\), and

\[
\boxed{
\sum_{\sigma\in S_n}\mu_q^{\sigma F}
=n!\lambda_q\mathbf1
}
\tag{2.2}
\]

at every depth.

#### Proof

The action of \(S_n\) on \(\Omega_m\) is transitive.  The stabilizer of
an unoriented cyclic order is its dihedral group, of order \(2n\).  Hence,
for fixed \(C,D\in\Omega_m\), exactly \(2n\) permutations send \(D\) to
\(C\).  Therefore the multiplicity of \(C\) is

\[
\sum_{D\in F}|\{\sigma:\sigma D=C\}|
=2n|F|=2nB=2W.
\]

This proves (0.1).  The left side of (2.2) is invariant under all coordinate
permutations, hence is constant on the transitive rank-\(r_q\) layer.  Its
total is \(n!W\), so its constant value is \(n!W/N_q\).  \(\square\)

An exact reblocking of \(\mathcal U(F)\) is a multiset
\(\mathscr D=(F_1,\ldots,F_{n!})\) of exact factors satisfying

\[
\sum_{i=1}^{n!}\mathbf1_{F_i}
=\sum_{\sigma\in S_n}\mathbf1_{\sigma F}.
\tag{2.3}
\]

There are necessarily \(n!\) blocks, by total wreath-copy count.

### Theorem Z6.2 -- exact reblocking optimization identity

For every relabelling-invariant real functional \(\Phi\) on exact factors,

\[
\boxed{
\min_{\mathscr D\vdash\mathcal U(F)}
\frac1{n!}\sum_{G\in\mathscr D}\Phi(G)
=\Phi^*,
\qquad
\Phi^*=\min_{G\text{ exact}}\Phi(G),
}
\tag{2.4}
\]

and

\[
\boxed{
\min_{\mathscr D\vdash\mathcal U(F)}
\max_{G\in\mathscr D}\Phi(G)=\Phi^*.
}
\tag{2.5}
\]

In particular,

\[
\boxed{
\begin{array}{c}
\text{there is an exact reblocking of }\mathcal U(F)
\text{ with average energy}<\Phi(F)
\end{array}
\iff
\begin{array}{c}
\text{there is one exact factor }G
\text{ with }\Phi(G)<\Phi(F).
\end{array}}
\tag{2.6}
\]

#### Proof

Every block in every reblocking is an exact factor, so both left sides in
(2.4)--(2.5) are at least \(\Phi^*\).  Choose a minimizing exact factor
\(G^*\).  Theorem Z6.1 gives

\[
\mathcal U(G^*)=\mathcal U(F).
\]

The indexed orbit \((\sigma G^*)_{\sigma\in S_n}\) is therefore an exact
reblocking of \(\mathcal U(F)\), and every block has value \(\Phi^*\).
This proves (2.4)--(2.5).

If a reblocking has average below \(\Phi(F)\), one of its exact blocks has
value below \(\Phi(F)\).  Conversely, if \(G\) has smaller value, the
orbit reblocking \((\sigma G)_\sigma\) has every block smaller.  This proves
(2.6).  \(\square\)

There is no hidden convex rounding from the orbit barycentre to a new exact
factor.  Indeed, if exact-factor incidence vectors satisfy

\[
\mathbf1_H=\sum_{i=1}^t\alpha_i\mathbf1_{F_i},
\qquad
\alpha_i>0,
\qquad
\sum_i\alpha_i=1,
\]

then \(F_i=H\) for every \(i\).  At a wreath coordinate where
\(\mathbf1_H\) is one (respectively zero), a positive convex combination
of zero--one entries can equal one (respectively zero) only when every
entry is one (respectively zero).  Thus every positive exact factor is a
rigid zero--one vertex of the factor polytope.

### Corollary Z6.3 -- aggregate Graver invisibility

For any two exact factors \(F,G\),

\[
\boxed{
\sum_{\sigma\in S_n}
(\mathbf1_{\sigma G}-\mathbf1_{\sigma F})=0.
}
\tag{2.7}
\]

Thus replacing the orbit decomposition of \(F\) by that of \(G\) is pure
recolouring of a fixed positive multicover.  It is the zero move in the
uncoloured wreath lattice and in every aggregate lower-load image.

For the separable convex floor potentials considered below, full lifted
augmented-Graver locality on the coloured decomposition fibre is an exact
global test.  But its global optimum is \(n!\Phi^*\) by (2.4).  Therefore
such descent proves only convergence to the unknown positive one-factor
optimum; it supplies no independent upper bound on that optimum.

## 3. Universal floor-corrected convex identity

Fix one depth and abbreviate \(N=N_q\), \(c=c_q\),
\(\theta=\theta_q\), \(\lambda=c+\theta\).  Let
\(\varphi:[0,\infty)\to\mathbb R\) be convex.  Put

\[
s_c=\varphi(c+1)-\varphi(c)
\]

and subtract the floor chord:

\[
g_{\varphi,c}(t)
=\varphi(t)-\varphi(c)-s_c(t-c).
\tag{3.1}
\]

Convexity gives

\[
g_{\varphi,c}(t)\ge0
\quad(t\in\mathbb Z_{\ge0}),
\qquad
g_{\varphi,c}(c)=g_{\varphi,c}(c+1)=0.
\tag{3.2}
\]

Indeed, outside the interval \([c,c+1]\), a convex graph lies above the
extension of its secant chord.  Define the integral floor excess

\[
E_{\varphi,q}(F)
=\sum_Sg_{\varphi,c}(\mu_q^F(S)).
\tag{3.3}
\]

Since \(\sum_S\mu_q^F(S)=W=cN+\rho\), the affine terms cancel and

\[
E_{\varphi,q}(F)
=\sum_S\varphi(\mu_q^F(S))
-\bigl[(N-\rho)\varphi(c)+\rho\varphi(c+1)\bigr].
\tag{3.4}
\]

Thus (3.3) is exactly the excess above the integer floor/ceiling profile.
Put

\[
\beta_{\varphi,q}
=-N g_{\varphi,c}(\lambda)\ge0,
\tag{3.5}
\]

where the inequality follows because a convex graph lies below its chord
inside \([c,c+1]\).

### Theorem Z6.4 -- exact orbit Jensen restitution

For every exact factor,

\[
\mathbb E_\sigma E_{\varphi,q}(\sigma F)=E_{\varphi,q}(F),
\tag{3.6}
\]

while

\[
E_{\varphi,q}(\mathbb E_\sigma\mu_q^{\sigma F})
=Ng_{\varphi,c}(\lambda)=-\beta_{\varphi,q}.
\tag{3.7}
\]

Consequently the exact Jensen gap is

\[
\boxed{
E_{\varphi,q}(F)+\beta_{\varphi,q}.
}
\tag{3.8}
\]

#### Proof

Coordinate relabelling only permutes the entries of \(\mu_q^F\), proving
(3.6).  Theorem Z6.1 says that the orbit mean is
\(\lambda\mathbf1\), which gives (3.7) and (3.8).  \(\square\)

For \(\varphi(t)=t^2\),

\[
g_{\varphi,c}(t)=(t-c)(t-c-1),
\qquad
\beta_{\varphi,q}=N\theta(1-\theta).
\tag{3.9}
\]

For the real corridor

\[
\varphi(t)=\operatorname{dist}(t,[c,c+1]),
\]

one has \(g_{\varphi,c}=\varphi\) and \(\beta_{\varphi,q}=0\).  In this
case (3.6)--(3.8) say that fractional orbit averaging releases the whole
corridor defect, while every orbit endpoint retains it exactly.

The theorem is not merely saying that a chosen potential is weak.  It
applies to every scalar convex potential after its exact integer floor is
removed.  Static orbit convexity yields a lower Jensen bound, whereas the
constant-one route requires an upper bound for one positive integral
endpoint.

## 4. Floor-corrected entropy, with constants

Let, with natural logarithms,

\[
\varphi(t)=t\log t,
\qquad
\varphi(0)=0,
\]

and define

\[
\boxed{
\eta_c(t)
=t\log t-c\log c
-(t-c)\bigl[(c+1)\log(c+1)-c\log c\bigr].
}
\tag{4.1}
\]

This is the chord-corrected potential (3.1).  It is nonnegative at every
integer \(t\ge0\) and vanishes at \(c,c+1\).
Its discrete second differences are those of \(t\log t\) and are strictly
positive.  Hence any positive weighted sum of the \(\eta_{c_q}\) is a
separable discrete-convex objective on the ordinary exact load lift
\([A_m\ 0;B_H\ -I]\), so the full lifted-Graver local/global theorem applies
without additional quota variables.

### Lemma Z6.5 -- entropy dominates the corridor

For every integer \(c\ge1\) and \(t\ge0\),

\[
\boxed{
\eta_c(t)
\ge\alpha_c\operatorname{dist}(t,\{c,c+1\})
\ge\frac1{c+2}\operatorname{dist}(t,\{c,c+1\}),
}
\tag{4.2}
\]

where, for \(\phi(j)=j\log j\),

\[
\alpha_c
=\min\{\phi(c+1)-2\phi(c)+\phi(c-1),
          \phi(c+2)-2\phi(c+1)+\phi(c)\}.
\]

The coefficient \(\alpha_c\) is the best uniform coefficient in the first
inequality.

#### Proof

Write \(\phi(t)=t\log t\), and let

\[
a_j=\phi(j+1)-\phi(j),
\qquad
d_j=a_j-a_{j-1}
=\phi(j+1)-2\phi(j)+\phi(j-1).
\]

For \(j\ge1\), the second-difference integral is

\[
d_j
=\int_{j-1}^{j+1}
(1-|x-j|)\frac{dx}{x}.
\tag{4.3}
\]

At \(j=1\) this is interpreted as the convergent improper integral; the
triangular weight cancels the singularity at zero.  The triangular kernel
has integral one and \(x\le j+1\) on its support, so

\[
d_j\ge\frac1{j+1}.
\tag{4.4}
\]

If \(t=c+1+k\), \(k\ge1\), then

\[
\eta_c(t)
=\sum_{h=1}^k(a_{c+h}-a_c).
\]

Every parenthesis contains \(d_{c+1}\), hence is at least
\(d_{c+1}\ge\alpha_c\ge1/(c+2)\).  Therefore
\(\eta_c(t)\ge k\alpha_c\).

If \(t=c-k\), \(k\ge1\), then

\[
\eta_c(t)
=\sum_{h=1}^k(a_c-a_{c-h}).
\]

Every parenthesis contains \(d_c\), hence is at least
\(d_c\ge\alpha_c\), while (4.4) gives
\(d_c\ge1/(c+1)\).  This gives the same bound.  The two remaining values
\(t=c,c+1\) have both sides zero.  Finally, the ratios at \(t=c-1\) and
\(t=c+2\) are respectively \(d_c\) and \(d_{c+1}\), so no uniform
coefficient larger than \(\alpha_c\) is possible.  \(\square\)

Define the entropy excess

\[
\mathsf H_q(F)=\sum_S\eta_{c_q}(\mu_q^F(S)).
\tag{4.5}
\]

Lemma Z6.5 gives

\[
\frac1{c_q}\sum_S
\operatorname{dist}(\mu_q^F(S),\{c_q,c_q+1\})
\le
\frac{c_q+2}{c_q}\mathsf H_q(F)
\le3\mathsf H_q(F).
\tag{4.6}
\]

Summing proves (0.6).  Thus this potential composes quantitatively into the
constant-one route: \(\sum_{q\le H_A}\mathsf H_q(F)=o(W)\) implies the
free-quota corridor is \(o(W)\), hence fixed-window unlabelled overload is
\(o(W)\).

It remains subject to the exact orbit obstruction.  Put

\[
p_q^F(S)=\frac{\mu_q^F(S)}W,
\qquad
u_q(S)=\frac1{N_q}.
\tag{4.7}
\]

The floor entropy divergence is

\[
D_q^{\rm fl}
=\frac1W\left[
(N_q-\rho_q)c_q\log\frac{c_q}{\lambda_q}
+\rho_q(c_q+1)\log\frac{c_q+1}{\lambda_q}
\right].
\tag{4.8}
\]

Direct cancellation of the \(-W\log\lambda_q\) terms gives

\[
\boxed{
\mathsf H_q(F)
=W\bigl[D(p_q^F\|u_q)-D_q^{\rm fl}\bigr].
}
\tag{4.9}
\]

### Theorem Z6.6 -- exact frame-information identity

Let \(\Sigma\) be uniform on \(S_n\).  Conditional on \(\Sigma=\sigma\),
sample a rank-\(r_q\) target \(X\) according to \(p_q^{\sigma F}\).  Then

\[
\boxed{
X\sim u_q,
\qquad
I(X;\Sigma)=D(p_q^F\|u_q).
}
\tag{4.10}
\]

#### Proof

By (2.2),

\[
\mathbb P(X=S)
=\mathbb E_\Sigma p_q^{\Sigma F}(S)
=1/N_q.
\]

The conditional relative entropy formula for mutual information gives

\[
I(X;\Sigma)
=\mathbb E_\Sigma
D(p_q^{\Sigma F}\|u_q).
\]

Every conditional distribution is a coordinate permutation of \(p_q^F\),
so every divergence in the average equals \(D(p_q^F\|u_q)\).  \(\square\)

There is an equally exact chi-square version.  Let

\[
Q_q(F)=\sum_S
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1)
\]

be the unhalved quadratic floor energy and

\[
\beta_q=N_q\theta_q(1-\theta_q).
\]

Then

\[
\boxed{
\chi^2(p_q^F\|u_q)
=\frac{N_q}{W^2}\bigl[Q_q(F)+\beta_q\bigr].
}
\tag{4.11}
\]

Indeed, \(Q_q=\|\mu_q^F-\lambda_q\mathbf1\|_2^2-\beta_q\), and
the chi-square divergence is \(N_q/W^2\) times the squared norm.  The full
orbit has uniform marginal but preserves the left side conditionally.  In
particular, quadratic orbit smoothing releases not just the desired
floor-energy excess but also the compulsory variance \(\beta_q\).

Equivalently, for independent uniform \(\Sigma,\Tau\in S_n\),

\[
\mathbb E_\Sigma
\|\mu_q^{\Sigma F}-\lambda_q\mathbf1\|_2^2
=Q_q(F)+\beta_q,
\qquad
\mathbb E_{\Sigma,\Tau}
\|\mu_q^{\Sigma F}-\mu_q^{\Tau F}\|_2^2
=2[Q_q(F)+\beta_q].
\tag{4.12}
\]

The second identity follows by expanding the square and using the zero
orbit mean of the centered loads.  Thus even the complete pairwise orbit
Dirichlet ledger measures the unknown energy plus its integer baseline; it
does not furnish an upper anchor.

## 5. Static common-owner heat collapses

The preceding obstruction permits arbitrary exact reblocking.  The
canonical common-owner implementation is even more rigid.

For an exact factor \(F\), let \(o_F(A)\) be the unique row owning the
middle set \(A\).  For a coordinate transposition \(\tau\), contract the
usual overlay between \(F\) and \(\tau F\) back onto the rows of \(F\).
Its row relation is generated by

\[
o_F(A)\sim o_F(\tau A).
\tag{5.1}
\]

To justify the contraction, write \(\tau=(x\ y)\).  In any cyclic row,
each of \(x,y\) lies in exactly \(m\) middle windows.  Their total incidence
is \(2m=n-1\); if every middle window contained exactly one of them, the
total would be \(n\).  Hence some middle window contains both or neither,
is fixed by \(\tau\), and joins a row to its \(\tau\)-image inside the
overlay.

Let \(T\) be a family of transpositions, \(G=\langle T\rangle\), and join
the relations (5.1).  Form the bipartite graph whose left vertices are rows
of \(F\), whose right vertices are the \(G\)-orbits on middle sets, and
where a row is incident with an orbit when it owns a set in that orbit.

### Lemma Z6.7 -- owner--orbit quotient

The joined owner blocks are exactly the sets of row vertices in the
connected components of this bipartite graph.

#### Proof

The Schreier graph generated by \(T\) is connected on each \(G\)-orbit.
Relation (5.1) therefore joins all owners of sets in one orbit.  Conversely,
every generator (5.1) stays inside one orbit.  Thus a chain in the joined
row relation is exactly an alternating row--orbit path in the bipartite
graph.  \(\square\)

For \(G=S_n\), there is one middle-set orbit, incident with every row, so
there is one owner block.  A sharper obstruction uses a proper subgroup.

### Theorem Z6.8 -- point-stabilizer perfect smoothing with total restitution

Fix a coordinate \(x\), and let

\[
G_x=S_{[n]\setminus\{x\}}.
\]

Then:

1. the joined owner partition of every exact factor has one block;
2. at every lower rank, averaging over \(G_x\) annihilates the centered
   load \(f_q=\mu_q^F-\lambda_q\mathbf1\);
3. the only static owner-block Haar children are whole relabellings \(gF\),
   and every relabelling-invariant floor potential has exactly zero drift.

#### Proof

The group \(G_x\) has two middle-set orbits: sets containing \(x\), and
sets avoiding \(x\).  Every cyclic row has exactly \(m\) middle windows
containing \(x\) and \(m+1\) avoiding it.  Hence every row vertex in the
bipartite graph of Lemma Z6.7 meets both orbit vertices.  The graph is
connected, proving part 1.

At rank \(r=r_q\), the two target orbits are again determined by membership
of \(x\).  Every cyclic row has exactly \(r\) rank-\(r\) intervals through
\(x\).  Since \(F\) has \(B\) rows,

\[
\sum_{S\ni x}\mu_q^F(S)=rB.
\tag{5.2}
\]

On the other hand,

\[
\lambda_q\binom{n-1}{r-1}
=\frac W{N_q}\frac r nN_q
=rB.
\tag{5.3}
\]

Thus \(f_q\) sums to zero on the orbit through \(x\), and hence also on
its complement.  The group average, which is constant on each orbit, is
therefore zero.  This proves part 2.

By part 1, independent Haar relabelling of joined owner blocks has only one
block to relabel.  Every child is consequently \(gF\), not a recombination
of different rows.  Coordinate relabelling only permutes every lower-load
vector, so every relabelling-invariant potential is unchanged.  This proves
part 3.  \(\square\)

The theorem gives perfect coherent lower-load smoothing and complete exact
restitution in the same positive factor cell.  Therefore no spectral,
variance, entropy, or convexity estimate on the coherent group average can
upper-bound the integral child energy without an additional theorem that
breaks the one-block owner geometry.

## 6. Consequences for constant one and exact scope

Take

\[
H_A=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\), and let \(\Phi\) be any of:

\[
\mathcal C_{H_A},
\qquad
\sum_{q\le H_A}\frac{Q_q}{c_q},
\qquad
\sum_{q\le H_A}\mathsf H_q,
\]

or any nonnegative combination of the convex floor excesses (3.3).
All are relabelling invariant.  Theorems Z6.1--Z6.8 prove the following.

1. The full orbit has perfect fractional lower-rank balance but its natural
   exact blocks all retain \(\Phi(F)\).
2. Every uncoloured orbit statistic is independent of \(F\), and every
   aggregate load statistic is already perfectly balanced.
3. Optimizing over all positive exact reblockings of that same multicover
   has value exactly the unknown one-factor optimum.
4. Allowing full coloured augmented-Graver moves gives a correct descent
   algorithm to this optimum, but not an upper bound on it.
5. Static common-owner group heat cannot realize the fractional smoothing:
   for \(S_n\), and already for \(G_x\), its cell consists only of whole
   relabellings.

Accordingly, a proof based solely on static group-orbit barycentres,
convexity of a floor-corrected potential, or Graver descent on an orbit
reblocking fibre is circular at the decisive point.  It proves the
constant-one theorem only after supplying an independent positive
reblocking whose energy is \(o(W)\); by (2.6), such a reblocking already
contains the desired low-energy exact factor.

This is a no-go for the stated architecture, not a counterexample to MWB
or to the contiguous-OR conjecture.  It leaves two mathematically distinct
escapes:

- recompute ownership components adaptively after earlier nontrivial exact
  choices; or
- construct additional perfect exact-factor matchings inside a union of
  orbit supports, using incidence information not encoded by the orbit
  barycentre.

Either escape must control a genuine positive integral factor.  Fractional
orbit balance, signed lattice saturation, and convergence to an unknown
global minimum do not preserve the literal contiguous-OR conclusion on
their own.

## 7. Independent audit of the decisive steps

The two numerical steps on which the no-go depends were independently
reproved.

1. Under the unoriented convention the stabilizer of a cyclic order has
   order \(2n\), so its full-orbit multiplicity is exactly
   \(2nB=2W\), not \(W\) or \(nW\).  Total copy count then forces exactly
   \(n!\) blocks in every reblocking.  Comparing each block with the global
   one-factor minimum and using the orbit of a minimizing factor proves
   both (2.4) and (2.5), with no missing normalization.
2. In Lemma Z6.5, the \(j=1\) integral in (4.3) is convergent because the
   triangular weight is \(x\) at the origin.  Every upper-tail increment
   contains \(d_{c+1}\ge1/(c+2)\), while every lower-tail increment contains
   \(d_c\ge1/(c+1)\).  Thus the constant \(1/(c+2)\) holds also at
   \(t=0\), and the factor three in (4.6) follows exactly from \(c\ge1\).

No audit correction was required.  The audit also confirms the stated
scope: the theorem rules out static orbit aggregation/reblocking and
canonical joined-owner heat, but makes no assertion against adaptive
component recomputation or newly constructed exact matchings.
