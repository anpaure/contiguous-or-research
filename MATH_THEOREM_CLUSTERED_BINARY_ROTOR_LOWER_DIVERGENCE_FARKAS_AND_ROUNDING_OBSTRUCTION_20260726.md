# Clustered binary rotors with lower coverage and signed cancellation: exact Farkas dual and an orbit-divisibility rounding obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom n m,\qquad D=m!(m+1)!,
 \qquad H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed and \(m\) is large enough that \(H\le m-1\).
This note replaces the upper-prefix inequalities in the binary-rotor
program by the exact signed Johnson-divergence cancellation equations.

For nonnegative lower-target prices \(u=(u_{q,S})\), a free state
potential \(\phi\), and free divergence prices \(\theta=(\theta_{q,T})\),
define

\[
 U_u(\pi)=\sum_{q=0}^H u_{q,L_q(\pi)},
\]

\[
 \Theta_\theta(\pi)=
 \sum_{q=0}^H
 \left(
  \theta_{q,K_q(\pi)\cup\{x_n\}}
  -\theta_{q,K_q(\pi)\cup\{x_1\}}
 \right)
\]

for \(\pi=(x_1,\ldots,x_n)\), and put

\[
 M_X(\phi,\theta,u)=
 \max_{\pi\in\mathcal F_X}
 \max\left\{
 \begin{array}{l}
 \phi_\pi-\phi_{A\pi}+U_u(\pi)+\Theta_\theta(\pi),\\
 \phi_\pi-\phi_{B\pi}+U_u(\pi)
 \end{array}\right\}.
\tag{0.1}
\]

The exact-cancellation fractional system is feasible if and only if

\[
 \boxed{
 \sum_{q=0}^H\sum_{S\in\binom{[n]}{m-q}}u_{q,S}
 \le
 \sum_{X\in\binom{[n]}m}M_X(\phi,\theta,u)}
\tag{0.2}
\]

for every \(\phi,\theta\) free and every \(u\ge0\). More generally, if
the permitted aggregate divergence is

\[
 \mathfrak D_H(z)=\frac12\sum_{q,T}|\mathcal D_{q,T}(z)|\le\Delta,
\]

the exact Farkas criterion is

\[
 \boxed{
 \sum_{q,S}u_{q,S}-2\Delta\lVert\theta\rVert_\infty
 \le \sum_XM_X(\phi,\theta,u).}
\tag{0.3}
\]

Thus the signed rows introduce free, not nonnegative, multipliers, and an
\(\ell^1\)-cancellation budget introduces precisely the dual
\(\ell^\infty\) penalty in (0.3).

For every \(t\in[0,1]\), the uniform circulation

\[
 z^t_{\pi,A}=\frac tD,\qquad
 z^t_{\pi,B}=\frac{1-t}{D}
\tag{0.4}
\]

has zero signed divergence at every depth and proves the stronger dual
inequality

\[
 \boxed{
 \sum_XM_X(\phi,\theta,u)
 \ge
 \sum_{q=0}^H\lambda_q\sum_Su_{q,S},
 \qquad
 \lambda_q=\frac{W}{\binom n{m-q}}.}
\tag{0.5}
\]

Hence there is no fractional Farkas obstruction. Uniformly at Gaussian
depth,

\[
 \lambda_q=\prod_{j=0}^{q-1}\frac{m+2+j}{m-j},\qquad
 \log\lambda_q=\frac{q(q+1)}m+O_A(m^{-1/2}),
\]

and

\[
 \lambda_H=e^{A^2}\bigl(1+O_A(m^{-1/2})\bigr).
\tag{0.6}
\]

There is nevertheless an exact integral obstruction. On the face
\(z_{\pi,B}=0\), the point (0.4) with \(t=1\) satisfies owner balance,
flow, every lower cover, and exact signed cancellation. Every integral
point on that face is a union of \(A\)-orbits of length \(2m\), and so
requires \(2m\mid W\). For every prime \(m>2\),

\[
 \binom{2m+1}{m}\equiv2\pmod m,
\]

so the face is fractionally feasible and integer-empty. Equivalently,

\[
 \boxed{\sum_{\pi\in S_n}z_{\pi,B}\ge1}
\tag{0.7}
\]

is valid for the integer hull for those \(m\), but is violated by the
exact-cancellation fractional point. Thus generic LP, total-unimodular,
or support-preserving rounding is impossible even after the signed rows
are imposed.

This does not prove the unrestricted integral system infeasible. The
remaining problem is a global owner-simple cycle-semigroup rounding.
The exact reverse two-switch is integrally forbidden, while the first
legal port-preserving move, the incidence \(C_6\), lies inside the kernel
of both lower load and signed divergence and therefore only rethreads a
fixed feasible level set. No coefficient-one conclusion is claimed.

## 1. The clustered lower-divergence system

Let \(\Pi=S_n\). For

\[
 \pi=(x_1,\ldots,x_n)
\]

define the two state rotors

\[
 A\pi=(x_2,\ldots,x_{n-1},x_1,x_n),\qquad
 B\pi=(x_2,\ldots,x_n,x_1).
\tag{1.1}
\]

The middle owner and its state fibre are

\[
 X(\pi)=\{x_1,\ldots,x_m\},\qquad
 \mathcal F_X=\{\pi:X(\pi)=X\}.
\tag{1.2}
\]

Every fibre has size \(D=m!(m+1)!\). For \(0\le q\le H\), set

\[
 r_q=m-q,
 \qquad
 L_q(\pi)=\{x_1,\ldots,x_{r_q}\},
\tag{1.3}
\]

and

\[
 K_q(\pi)=\{x_{n-r_q+1},\ldots,x_{n-1}\}.
\tag{1.4}
\]

Thus \(|K_q(\pi)|=r_q-1\). Define the signed switch incidence

\[
 d_{q,T}(\pi)=
 \mathbf1_{\{T=K_q(\pi)\cup\{x_n\}\}}
 -
 \mathbf1_{\{T=K_q(\pi)\cup\{x_1\}\}},
 \qquad T\in\binom{[n]}{r_q}.
\tag{1.5}
\]

The fractional variables are \(z_{\pi,g}\ge0\), for
\(\pi\in\Pi\) and \(g\in\{A,B\}\). The owner and state-flow equations
are

\[
 \sum_{\pi\in\mathcal F_X}\sum_gz_{\pi,g}=1
 \qquad\left(X\in\binom{[n]}m\right),
\tag{1.6}
\]

\[
 \sum_gz_{\sigma,g}
 -\sum_gz_{g^{-1}\sigma,g}=0
 \qquad(\sigma\in\Pi).
\tag{1.7}
\]

The lower-prefix cover rows are

\[
 \sum_{\pi,g}\mathbf1_{\{L_q(\pi)=S\}}z_{\pi,g}\ge1
 \quad
 \left(0\le q\le H, S\in\binom{[n]}{r_q}\right).
\tag{1.8}
\]

Finally put

\[
 \mathcal D_{q,T}(z)=\sum_{\pi}z_{\pi,A}d_{q,T}(\pi).
\tag{1.9}
\]

The exact signed-cancellation rows are

\[
 \mathcal D_{q,T}(z)=0
 \quad
 \left(0\le q\le H, T\in\binom{[n]}{r_q}\right).
\tag{1.10}
\]

The integral system requires \(z_{\pi,g}\in\{0,1\}\). Equations
(1.6)--(1.7) then describe an owner-transversal clustered injective-de
Bruijn cycle cover: one state over every owner, with the selected states
closed into rotor cycles.

### Lemma 1.1 (the signed rows are exactly upper-minus-lower load)

For every nonnegative \(z\) satisfying state flow (1.7), let

\[
 \mathcal L_{q,T}(z)=
 \sum_{\pi,g}\mathbf1_{\{L_q(\pi)=T\}}z_{\pi,g}
\]

and let \(\mathcal R_{q,T}(z)\) be the load of the complements of the
rank-\((m+1+q)\) prefixes. Then

\[
 \boxed{\mathcal R_{q,T}(z)-\mathcal L_{q,T}(z)
       =\mathcal D_{q,T}(z).}
\tag{1.11}
\]

Consequently, (1.8) and (1.10) imply both lower and complementary upper
coverage with identical load profiles.

#### Proof

Put \(y_\pi=\sum_gz_{\pi,g}\). If \(f\) is any function of an ordered
\(r\)-block, where \(r\le n-2\), then (1.7) gives

\[
 \begin{aligned}
 \sum_{\sigma}y_\sigma f(\sigma_1,\ldots,\sigma_r)
 &=\sum_{\pi,g}z_{\pi,g}
       f((g\pi)_1,\ldots,(g\pi)_r)\\
 &=\sum_{\pi}y_\pi f(x_2,\ldots,x_{r+1}).
 \end{aligned}
\]

The second equality holds because both successors begin with
\(x_2,\ldots,x_{n-1}\), independently of the rotor choice. Taking
indicator functions and iterating proves that the weighted distribution
of the first \(r_q\)-block equals that of the block in positions
\(n-r_q,\ldots,n-1\).

Now count the last internal \(r_q\)-block of each successor. Stationarity
shows that its load is \(\mathcal L_{q,T}(z)\). A \(B\)-successor
contributes \(K_q(\pi)\cup\{x_n\}\), whereas an \(A\)-successor
contributes \(K_q(\pi)\cup\{x_1\}\). On the other hand,
\(\mathcal R_{q,T}(z)\) counts
\(K_q(\pi)\cup\{x_n\}\) for both rotor types. Subtraction leaves
precisely the \(A\)-terms in (1.9). The argument is linear and therefore
applies to every fractional circulation, not only to integral cycle
covers. \(\square\)

The rows (1.10) are linearly dependent, since
\(\sum_Td_{q,T}(\pi)=0\) for every \(q,\pi\). This causes no difficulty:
their Farkas multipliers are free and are understood modulo the
corresponding constant gauges.

## 2. Exact Farkas dual, including an \(\ell^1\) cancellation budget

For \(u_{q,S}\ge0\), define

\[
 U_u(\pi)=\sum_{q=0}^Hu_{q,L_q(\pi)}.
\tag{2.1}
\]

For free \(\theta_{q,T}\in\mathbb R\), define

\[
 \Theta_\theta(\pi)=\sum_{q=0}^H\sum_T
 \theta_{q,T}d_{q,T}(\pi),
\tag{2.2}
\]

which is the expression displayed before (0.1).

### Theorem 2.1 (exact-cancellation Farkas criterion)

The fractional system (1.6)--(1.10) is feasible if and only if (0.2)
holds for every free \(\phi\in\mathbb R^\Pi\), every free \(\theta\),
and every \(u\ge0\).

#### Proof

Give (1.6) free multipliers \(\alpha_X\), give (1.7) free multipliers
\(\phi_\sigma\), give (1.10) free multipliers \(\theta_{q,T}\), and
give the cover inequalities (1.8) nonnegative multipliers \(u_{q,S}\).
The coefficient of a nonnegative primal variable is

\[
 \alpha_{X(\pi)}+\phi_\pi-\phi_{g\pi}+U_u(\pi)
 +\mathbf1_{\{g=A\}}\Theta_\theta(\pi).
\tag{2.3}
\]

Farkas' lemma says that infeasibility is equivalent to the existence of
these multipliers for which every expression (2.3) is at most zero but

\[
 \sum_X\alpha_X+\sum_{q,S}u_{q,S}>0.
\tag{2.4}
\]

For fixed \((\phi,\theta,u)\), the largest permissible value of
\(\alpha_X\) is \(-M_X(\phi,\theta,u)\). Substitution in (2.4) gives a
certificate exactly when (0.2) fails. \(\square\)

### Theorem 2.2 (budgeted-cancellation Farkas criterion)

Replace (1.10) by

\[
 \mathfrak D_H(z)=\frac12\sum_{q,T}|\mathcal D_{q,T}(z)|\le\Delta.
\tag{2.5}
\]

The resulting fractional system is feasible if and only if (0.3) holds
for every \(\phi,\theta,u\) of Theorem 2.1.

#### Proof

Introduce \(p_{q,T},s_{q,T}\ge0\) and write

\[
 \mathcal D_{q,T}(z)-p_{q,T}+s_{q,T}=0,
 \qquad
 \frac12\sum_{q,T}(p_{q,T}+s_{q,T})\le\Delta.
\tag{2.6}
\]

Use the multiplier \(\theta_{q,T}\) for the equality and a
nonnegative multiplier \(\rho\) for the budget written as

\[
 -\frac12\sum_{q,T}(p_{q,T}+s_{q,T})\ge-\Delta.
\]

The coefficients of \(p_{q,T}\) and \(s_{q,T}\) in a Farkas
certificate are respectively

\[
 -\theta_{q,T}-\rho/2,
 \qquad
 \theta_{q,T}-\rho/2.
\]

They are both nonpositive exactly when
\(\rho\ge2\lVert\theta\rVert_\infty\). The certificate objective is

\[
 \sum_X\alpha_X+\sum_{q,S}u_{q,S}-\rho\Delta.
\]

For fixed \(\theta\), the best choice is
\(\rho=2\lVert\theta\rVert_\infty\). Eliminating \(\alpha\) as in
Theorem 2.1 now gives (0.3). \(\square\)

Thus exact cancellation is the case \(\Delta=0\). The factor two in
(0.3) is forced by the normalization in (2.5), and the signed prices
remain completely free.

## 3. Uniform fractional domination and Gaussian accounting

### Theorem 3.1 (one common fractional point)

For every \(t\in[0,1]\), the vector (0.4) satisfies (1.6)--(1.10), and
every lower target at depth \(q\) has load

\[
 \lambda_q=\frac{W}{\binom n{m-q}}.
\tag{3.1}
\]

Moreover, it proves the dual domination (0.5) for every
\((\phi,\theta,u)\).

#### Proof

The total outgoing mass at every state is \(1/D\). Since \(A\) and
\(B\) are permutations of \(\Pi\), the incoming mass is also \(1/D\),
so flow holds. Every owner fibre has \(D\) states, proving (1.6).

For a fixed \(r_q\)-set \(S\), exactly
\(r_q!(n-r_q)!\) permutations have \(S\) in their first \(r_q\)
positions. Its load is therefore

\[
 \frac{r_q!(n-r_q)!}{D}
 =\frac{W}{\binom n{r_q}}=\lambda_q\ge1.
\tag{3.2}
\]

For every fixed \(q,T\), the coordinate transposition which exchanges
positions \(1,n\) preserves \(K_q(\pi)\) and exchanges the two
indicators in (1.5). Hence
\(\sum_{\pi\in\Pi}d_{q,T}(\pi)=0\), and (1.9) vanishes under (0.4).

For each owner, the maximum in (0.1) is at least its average against the
unit fibre mass (0.4). Summing those averages over the owners makes the
potential term vanish by flow, makes the \(\theta\)-term vanish by exact
signed cancellation, and evaluates the lower-price term by (3.2). This
is exactly (0.5). \(\square\)

### Corollary 3.2 (exact Gaussian margins)

Uniformly for \(0\le q\le H\),

\[
 \lambda_q=
 \prod_{j=0}^{q-1}\frac{m+2+j}{m-j},
\tag{3.3}
\]

\[
 \log\lambda_q=\frac{q(q+1)}m
 +O_A\left(\frac{(q+1)^3}{m^2}\right),
\tag{3.4}
\]

and (0.6) holds. In particular,

\[
 \lambda_0=1,\qquad \lambda_1=1+\frac2m.
\tag{3.5}
\]

For the unweighted lower functional \(u_{q,S}=1\), its exact total
fractional surplus over the required right-hand side is

\[
 \sum_{q=0}^H\left(W-\binom n{m-q}\right)
 =W\sqrt m\left(A-\int_0^Ae^{-x^2}\,dx\right)+O_A(W).
\tag{3.6}
\]

#### Proof

Factorial cancellation gives (3.3). For
\(q\le A\sqrt m+1\), Taylor expansion of each logarithm in (3.3), with
the remainders summed uniformly, gives (3.4). At
\(H=\lceil A\sqrt m\rceil\), this yields (0.6).

Writing \(N_q=\binom n{m-q}=W/\lambda_q\), (3.4) gives uniformly

\[
 \frac{N_q}{W}=e^{-q^2/m}+O_A(m^{-1/2}).
\]

A Riemann sum then gives

\[
 \sum_{q=0}^H\frac{N_q}{W}
 =\sqrt m\int_0^Ae^{-x^2}\,dx+O_A(1),
\]

which proves (3.6). \(\square\)

The only tight fractional depth is \(q=0\), where the lower cover is
already the owner equation. Exact signed cancellation has not consumed
any of the positive Gaussian margin.

## 4. Exact cycle-master form

Let \(\mathscr C\) be the directed simple cycles of the rotor state
digraph. For \(C\in\mathscr C\), define

\[
 a_X(C)=\#\{\pi\in C:X(\pi)=X\},
\]

\[
 \ell_{q,S}(C)=\#\{\pi\in C:L_q(\pi)=S\},
\]

and

\[
 \delta_{q,T}(C)=
 \sum_{(\pi,g)\in C}\mathbf1_{\{g=A\}}d_{q,T}(\pi).
\tag{4.1}
\]

The exact integral master is

\[
 \begin{aligned}
 &\sum_{C\in\mathscr C}a_X(C)\xi_C=1
 &&\left(X\in\binom{[n]}m\right),\\
 &\sum_C\ell_{q,S}(C)\xi_C\ge1
 &&\left(0\le q\le H, S\in\binom{[n]}{r_q}\right),\\
 &\sum_C\delta_{q,T}(C)\xi_C=0
 &&\left(0\le q\le H, T\in\binom{[n]}{r_q}\right),\\
 &\xi_C\in\mathbb Z_{\ge0}.
 \end{aligned}
\tag{4.2}
\]

The owner equations automatically exclude a cycle which repeats an
owner and make two selected cycles owner-disjoint. Therefore (4.2) is
exactly the Boolean clustered rotor problem, not merely a relaxation.
Dropping integrality gives the fractional arc system by ordinary cycle
decomposition of a nonnegative circulation.

Its Farkas form is the following: for every free \(\alpha_X\), every
free \(\theta_{q,T}\), and every \(u_{q,S}\ge0\),

\[
 \left[
 \sum_Xa_X(C)\alpha_X+
 \sum_{q,S}\ell_{q,S}(C)u_{q,S}+
 \sum_{q,T}\delta_{q,T}(C)\theta_{q,T}\le0
 \quad\forall C\in\mathscr C
 \right]
\]

implies

\[
 \boxed{\sum_X\alpha_X+\sum_{q,S}u_{q,S}\le0.}
\tag{4.3}
\]

Indeed, (4.3) is Farkas' lemma applied directly to (4.2) without its
integrality row. The state potentials in (0.1) are the finite-arc
reduced-cost form of these cycle inequalities.

## 5. The integral rounding obstruction survives exact cancellation

### Theorem 5.1 (prime \(A\)-orbit obstruction)

Add the face equations

\[
 z_{\pi,B}=0\qquad(\pi\in\Pi).
\tag{5.1}
\]

The resulting face of the exact-cancellation system is fractionally
nonempty for every \(0\le H\le m-1\). If it contains an integral point,
then

\[
 2m\mid W.
\tag{5.2}
\]

For every prime \(m>2\), the face is therefore fractionally feasible
but integer-empty, including at \(H=\lceil A\sqrt m\rceil\).

#### Proof

Take \(t=1\) in Theorem 3.1. This proves fractional feasibility of the
face, including exact cancellation.

Suppose now that \(z\) is integral on the face. If
\(z_{\pi,A}=1\), flow at \(A\pi\) forces
\(z_{A\pi,A}=1\); continuing forces the complete \(A\)-orbit. The
position permutation \(A\) is a cycle on the first \(n-1=2m\)
positions and fixes the last position. Since all labels are distinct,
every state has an \(A\)-orbit of exactly \(2m\) states. Thus the total
number of selected states is divisible by \(2m\).

Summing the owner equations gives exactly \(W\) selected states, proving
(5.2). If \(m=p>2\) is prime, then

\[
 (1+x)^{2p+1}
 =(1+x)((1+x)^p)^2
 \equiv(1+x)(1+x^p)^2\pmod p.
\]

The coefficient of \(x^p\) on the right is two. Hence
\(W=\binom{2p+1}{p}\equiv2\pmod p\), so \(2p\nmid W\). \(\square\)

### Corollary 5.2 (an explicit integer-hull cut)

For every prime \(m>2\), every integral feasible point of the
unrestricted exact-cancellation system satisfies (0.7), while the
fractional point \(z^1\) violates it.

#### Proof

An integral point violating (0.7) would have zero \(B\)-mass and hence
would lie on the empty face (5.1). Nonnegativity makes the same argument
valid for convex combinations: a convex combination with zero
\(B\)-mass can use only zero-\(B\)-mass integral points. \(\square\)

Thus the exact fractional polytope is not the convex hull of its integral
points. The assertion remains valid if the unrestricted integral system
happens to be empty; in that case its integer hull is empty and every
linear inequality is vacuously valid. What is proved non-vacuously is
that the displayed full-right-hand-side face has a fractional point and
no integral point.

### Corollary 5.3 (growing non-total-unimodularity remains)

For every \(m\ge2\), the coefficient matrix of (1.6)--(1.10) contains a
square minor of determinant \(k\) with \(k\ge m\).

#### Proof

Choose a state \(h_0\), put \(h_j=A^{-j}h_0\) for
\(j\in\mathbb Z_{n-1}\), and use the identity

\[
 B^{-1}AB^{-1}=A^{-1}.
\]

For each \(j\), traverse

\[
 Bh_j,B^2h_j,\ldots,B^{-1}h_j
\]

by \(n-2\) \(B\)-moves and then take the \(A\)-move to \(Bh_{j+1}\).
This is the genuine rotor cycle with control word

\[
 (B^{n-2}A)^{n-1}
\]

and it has \((n-1)^2\) states. To see that it is simple and count its
owners, write

\[
 h_0=(c_1,\ldots,c_{n-1},z).
\]

The \(h_j\)'s rotate the first \(n-1\) labels and fix \(z\). Their
\(B\)-orbits are the cyclic orders obtained by inserting \(z\) in the
\(n-1\) gaps of the fixed cycle on the \(c_i\)'s; distinct gaps give
distinct \(B\)-orbits. A middle interval either avoids \(z\), giving one
of at most \(n-1\) length-\(m\) intervals of the fixed cycle, or contains
\(z\), in which case deleting \(z\) gives one of at most \(n-1\)
length-\((m-1)\) intervals. The cycle therefore uses at most
\(2(n-1)\) distinct middle owners.

Some owner therefore appears \(k\ge m\) times. Restrict to the cycle's
arc columns, take all but one state-incidence row, and append that repeated
owner row. The reduced directed-cycle incidence matrix has cofactor
vector equal, up to signs, to the all-ones vector. Expansion in the owner
row gives determinant \(k\). These are owner and flow rows already
present in (1.6)--(1.7); adding lower and divergence rows cannot remove
the minor. \(\square\)

Corollary 5.3 rules out total-unimodular rounding, but unlike Theorem 5.1
it is only a matrix obstruction: the repeated-owner cycle itself is not
an admissible integral clustered component.

## 6. Audit against the two-switch and \(C_6\) structures

The Farkas dual makes the fractional/integral split visible but does not
by itself provide an integral cancellation primitive.

### Proposition 6.1 (the exact reverse pair is fractional only)

For a de Bruijn state arc

\[
 e=(x_1,x_2,\ldots,x_{n-1})
\]

with missing label \(x_n\), replace \(x_1\) by \(x_n\), keeping the
middle word fixed. The two \(A\)-switches have opposite vectors
\((d_{q,T})_{q,T}\), but they cannot both occur in an integral
owner-transversal circulation.

#### Proof

The replacement fixes every \(K_q\) and exchanges \(x_1,x_n\), so
(1.5) changes sign at every depth. The two de Bruijn arcs have the same
head \((x_2,\ldots,x_{n-1})\). A Boolean cycle cover has selected
indegree at most one there, so it cannot contain both. The shuffled
reverse variant avoids this head collision, but its two forced
\(A\)-successors have the same middle owner and is excluded by (1.6).
\(\square\)

### Proposition 6.2 (the incidence hexagon is a level-set move)

Every legal incidence-\(C_6\) flip preserves all lower-prefix loads and
all signed-divergence rows through \(H\le m-2\).

#### Proof

The two alternating matchings in an incidence hexagon use the same tail
multiset, the same head multiset, and the same first \(n-2\) prefix
words. Hence they preserve flow, owners, and every lower-prefix load.
They also preserve every upper prefix of length at most \(n-2\). By
Lemma 1.1, signed divergence is upper-minus-lower load, so it is
preserved as well. \(\square\)

Thus a \(C_6\) can merge three already active support cycles without
leaving the feasible lower-divergence level set, but it cannot turn a
nonzero divergence vector into zero. Activating enough such cells is a
separate integral grouping problem; the known depth-one capacity cut
shows that its naive local LP has an integrality gap of at least
\((m+2)/3\).

## 7. Exact proved boundary

The following are proved.

1. Equations (1.6)--(1.10) are the exact fractional clustered
   owner/flow/lower-prefix/exact-divergence system.
2. Formula (0.2) is its complete arc-potential Farkas criterion, with
   free divergence multipliers and nonnegative coverage multipliers.
3. Formula (0.3) is the corresponding complete criterion for the
   aggregate budget \(\mathfrak D_H\le\Delta\).
4. The common uniform circulation has exact zero divergence and proves
   the stronger domination (0.5). At \(H=A\sqrt m+O(1)\), its endpoint
   lower-cover margin is \(e^{A^2}(1+O_A(m^{-1/2}))\).
5. For infinitely many \(m\), the complete \(A\)-only face is
   fractionally feasible but integer-empty. Hence neither
   support-preserving nor total-unimodular rounding can solve the system.
6. Exact two-switch cancellation is integrally forbidden. The first
   legal port-preserving cocycle is the incidence \(C_6\), which stays
   inside every lower-divergence level set.

What is not proved is either feasibility or infeasibility of the
unrestricted integral system (4.2), a construction with \(o(W/m)\)
support cycles, or the coefficient-one theorem. The surviving exact
problem is an owner-simple cycle-semigroup selection whose lower loads
cover every target and whose signed cycle vectors sum to zero (or to
\(o(W)\) in \(\ell^1\)). Fractional Farkas weights cannot obstruct it;
an additional congruence/odd-set inequality or a genuinely global
dependent rounding is required.
