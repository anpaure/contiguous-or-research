# Clustered binary rotors: the signed-divergence Farkas dual and the balanced-missing-label obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
n=2m+1,\qquad N=n-1=2m,\qquad
W=\binom{n}{m}=n\,\operatorname{Cat}_m,
\qquad D=m!(m+1)!.
\tag{0.1}
\]

This note treats the exact clustered binary-rotor system consisting of

1. one unit of state mass over every middle owner;
2. state-flow conservation for the two rotors \(A,B\);
3. lower-prefix coverage through depth \(H\); and
4. exact cancellation of the signed upper--lower Johnson divergence
   through the same depths.

There are three conclusions.

First, Theorem 2.1 gives the complete LP/Farkas dual.  The dual contains
free Johnson potentials, one for every signed-divergence coordinate.
The uniform \(A\)-only circulation proves the stronger dual domination

\[
\sum_X M_X\ge
\sum_{q=0}^{H}\rho_q\sum_S u_{q,S},
\qquad
\rho_q=\frac{W}{\binom n{m-q}}.
\tag{0.2}
\]

Thus the real LP has no separating functional.  At
\(H=\lceil A_0\sqrt m\rceil\), for fixed \(A_0\),

\[
\rho_H=e^{A_0^2}\bigl(1+O_{A_0}(m^{-1/2})\bigr).
\tag{0.3}
\]

Second, this fractional point does not round, even after exact signed
cancellation is imposed.  On the \(A\)-only face, let \(t_c\) be the
number of selected \(A\)-orbits whose fixed missing coordinate is \(c\).
Every integral owner-transversal circulation on that face necessarily
satisfies

\[
\boxed{
t_c=\frac{W}{n(n-1)}=\frac{\operatorname{Cat}_m}{2m}
\quad(c\in[n]).}
\tag{0.4}
\]

The owner equations alone imply (0.4).  Independently, exact signed
divergence at **any one** protected rank implies the same equality by a
coordinate-moment calculation.  Hence

\[
\boxed{2m\mid\operatorname{Cat}_m}
\tag{0.5}
\]

is necessary for an integral point on the \(A\)-only face.  For every
prime \(m=p>2\),

\[
\operatorname{Cat}_p\equiv2\pmod p,
\tag{0.6}
\]

so no integral point exists.  This gives, on infinitely many Gaussian
instances, the valid integer-hull inequality

\[
\boxed{\sum_{\pi\in S_n}z_{\pi,B}\ge1,}
\tag{0.7}
\]

which the feasible uniform \(A\)-only point violates.

Third, neither known exact cancellation primitive removes this gap.
The opposite-switch involution explains the fractional cancellation but
is forbidden integrally at a common de Bruijn head.  The incidence
\(C_6\) directions preserve signed divergence, but no nonzero single
\(C_6\) direction is tangent to the \(A\)-only flow face: every tangent
vector there is constant on complete \(A\)-orbits.

This is an explicit obstruction to integral rounding of the stated LP.
It is not an obstruction to the unrestricted mixed \(A/B\) integer
system, and no coefficient-one conclusion is claimed.

## 1. The exact primal system

For a permutation state

\[
\pi=(x_1,\ldots,x_n)\in S_n
\]

write

\[
A\pi=(x_2,\ldots,x_{n-1},x_1,x_n),
\qquad
B\pi=(x_2,\ldots,x_n,x_1),
\tag{1.1}
\]

and let

\[
X(\pi)=\{x_1,\ldots,x_m\}.
\tag{1.2}
\]

For \(0\le q\le H\), put \(r_q=m-q\) and define

\[
L_q(\pi)=\{x_1,\ldots,x_{r_q}\},
\tag{1.3}
\]

\[
K_q(\pi)=
\{x_{n-r_q+1},\ldots,x_{n-1}\}.
\tag{1.4}
\]

Thus \(|K_q(\pi)|=r_q-1\).  For an \(r_q\)-set \(T\), define the signed
\(A\)-switch coordinate

\[
d_{q,T}(\pi)=
\mathbf 1[K_q(\pi)\cup\{x_n\}=T]
-
\mathbf 1[K_q(\pi)\cup\{x_1\}=T].
\tag{1.5}
\]

The variables are \(z_{\pi,g}\ge0\), where \(g\in\{A,B\}\).  The
owner and flow equations are

\[
\sum_{\pi:X(\pi)=X}\sum_g z_{\pi,g}=1
\qquad\left(X\in\binom{[n]}m\right),
\tag{1.6}
\]

\[
\sum_g z_{\pi,g}
-\sum_g z_{g^{-1}\pi,g}=0
\qquad(\pi\in S_n).
\tag{1.7}
\]

The lower-cover inequalities are

\[
\sum_{\pi:L_q(\pi)=S}\sum_g z_{\pi,g}\ge1
\qquad
\left(0\le q\le H,
S\in\binom{[n]}{r_q}\right).
\tag{1.8}
\]

The exact signed-divergence cancellation equations are

\[
\sum_{\pi\in S_n}z_{\pi,A}d_{q,T}(\pi)=0
\qquad
\left(0\le q\le H,
T\in\binom{[n]}{r_q}\right).
\tag{1.9}
\]

The divergence equations have one redundant constant row at each depth,
but retaining all coordinates is harmless.

### Lemma 1.1 (exact fractional divergence identity)

Under flow conservation, let \(L_{q,T}(z)\) be the lower-prefix load of
the \(r_q\)-set \(T\), and let \(R_{q,T}(z)\) be the load of states for
which

\[
K_q(\pi)\cup\{x_n\}=T.
\]

Then

\[
\boxed{
R_{q,T}(z)-L_{q,T}(z)
=\sum_{\pi}z_{\pi,A}d_{q,T}(\pi).}
\tag{1.10}
\]

Consequently (1.8)--(1.9) imply the complementary upper-prefix cover
system.

#### Proof

Write \(y_\pi=z_{\pi,A}+z_{\pi,B}\).  Flow says that \(y\) is the
state mass induced by incoming as well as outgoing selected transitions.
For every block length \(r\le n-2\), shifting a transition moves the
block in positions \(j,\ldots,j+r-1\) to positions
\(j-1,\ldots,j+r-2\) of the successor whenever both blocks lie among
the first \(n-1\) positions.  Summing against flow and iterating shows
that all internal consecutive \(r\)-block loads equal the first-prefix
load.

The last internal \(r_q\)-block of \(B\pi\) is
\(K_q(\pi)\cup\{x_n\}\), whereas that of \(A\pi\) is
\(K_q(\pi)\cup\{x_1\}\).  Compare their total load with the common
internal-block load.  The \(B\)-terms cancel, and the difference of the
two \(A\)-terms is exactly (1.10).

For \(r_q=m-q\), the set counted by \(R_{q,T}\) is the complement of a
prefix of size \(n-r_q=m+1+q\).  Thus \(R=L\) transfers every lower
cover to the paired upper cover. \(\square\)

For Boolean \(z\), (1.6)--(1.7) are precisely the owner-coloured cycle
cover equations in the injective de Bruijn graph.  In particular, the
word \(\textit{clustered}\) is encoded by (1.6), not by an unclustered
network-flow relaxation.

## 2. The complete Farkas dual

Let

\[
u_{q,S}\ge0
\qquad
\left(S\in\binom{[n]}{r_q}\right)
\tag{2.1}
\]

be lower-cover weights.  Let \(\phi_\pi\in\mathbb R\) be state
potentials and let \(\theta_{q,T}\in\mathbb R\) be free signed-divergence
potentials.  Define

\[
U_u(\pi)=\sum_{q=0}^{H}u_{q,L_q(\pi)},
\tag{2.2}
\]

\[
\Theta_\theta(\pi)=
\sum_{q=0}^{H}\sum_{T\in\binom{[n]}{r_q}}
\theta_{q,T}d_{q,T}(\pi).
\tag{2.3}
\]

For every owner \(X\), put

\[
M_X(\phi,\theta,u)=
\max_{\substack{\pi:X(\pi)=X\\g\in\{A,B\}}}
\left(
\phi_\pi-\phi_{g\pi}
+U_u(\pi)
+\mathbf 1[g=A]\Theta_\theta(\pi)
\right).
\tag{2.4}
\]

### Theorem 2.1 (eliminated Farkas alternative)

The real system (1.6)--(1.9), with \(z\ge0\), is feasible if and only if
for every \((\phi,\theta,u)\) as above,

\[
\boxed{
\sum_{q=0}^{H}\sum_{S\in\binom{[n]}{r_q}}u_{q,S}
\le
\sum_{X\in\binom{[n]}m}M_X(\phi,\theta,u).}
\tag{2.5}
\]

Equivalently, infeasibility is certified by free numbers \(\alpha_X\),
\(\phi_\pi\), \(\theta_{q,T}\), and nonnegative \(u_{q,S}\), satisfying

\[
\alpha_{X(\pi)}+\phi_\pi-\phi_{g\pi}
+U_u(\pi)+\mathbf 1[g=A]\Theta_\theta(\pi)
\le0
\tag{2.6}
\]

for all \((\pi,g)\), and

\[
\sum_X\alpha_X+\sum_{q,S}u_{q,S}>0.
\tag{2.7}
\]

#### Proof

Apply the Farkas alternative to the equality rows (1.6), (1.7), (1.9),
the covering rows (1.8), and nonnegativity of \(z\).  The coefficient
of column \((\pi,g)\) in the resulting linear combination is exactly
the left side of (2.6): the flow potentials contribute
\(\phi_\pi-\phi_{g\pi}\), and the divergence term occurs only for
\(g=A\).  The right-hand sides contribute (2.7).  This proves the
uneliminated alternative.

For fixed \((\phi,\theta,u)\), (2.6) is equivalent to

\[
\alpha_X\le-M_X(\phi,\theta,u)
\qquad(X\in\tbinom{[n]}m).
\]

Hence some \(\alpha\) can also satisfy (2.7) exactly when

\[
\sum_{q,S}u_{q,S}>\sum_XM_X(\phi,\theta,u).
\]

Negating this strict separation gives (2.5). \(\square\)

There is also a direct check of necessity.  Multiply the expression in
(2.4) by a feasible \(z_{\pi,g}\) and sum.  Owner mass bounds it above
by \(\sum_XM_X\); flow and signed divergence cancel the free-potential
terms; and lower coverage bounds the remaining sum below by
\(\sum_{q,S}u_{q,S}\).

### Theorem 2.2 (equivalent clustered cycle master)

Let \(\mathscr C\) be the directed simple cycles in the binary-rotor
state graph.  For \(C\in\mathscr C\), define

\[
a_X(C)=\#\{(\pi,g)\in C:X(\pi)=X\},
\]

\[
b_{q,S}(C)=\#\{(\pi,g)\in C:L_q(\pi)=S\},
\]

and

\[
\delta_{q,T}(C)=
\sum_{(\pi,A)\in C}d_{q,T}(\pi).
\]

Then the exact integral minimum-component problem is

\[
\begin{aligned}
\min\quad &\sum_{C\in\mathscr C}\xi_C,\\
\text{subject to}\quad
&\sum_Ca_X(C)\xi_C=1 &&(X\in\tbinom{[n]}m),\\
&\sum_Cb_{q,S}(C)\xi_C\ge1 &&(0\le q\le H,\ |S|=r_q),\\
&\sum_C\delta_{q,T}(C)\xi_C=0
  &&(0\le q\le H,\ |T|=r_q),\\
&\xi_C\in\mathbb Z_{\ge0}.
\end{aligned}
\tag{2.8}
\]

Its fractional dual is

\[
\boxed{
\begin{aligned}
\max\quad
&\sum_X\alpha_X+\sum_{q,S}u_{q,S},\\
\text{subject to}\quad
&\sum_Xa_X(C)\alpha_X
 +\sum_{q,S}b_{q,S}(C)u_{q,S}
 +\sum_{q,T}\delta_{q,T}(C)\theta_{q,T}
 \le1 &&(C\in\mathscr C),\\
&\alpha_X,\theta_{q,T}\in\mathbb R,
\qquad u_{q,S}\ge0.
\end{aligned}}
\tag{2.9}
\]

#### Proof

Every nonnegative integral circulation decomposes into directed simple
cycles.  The owner equation excludes a cycle which repeats an owner and
excludes two chosen cycles which meet one owner.  Conversely, a family
of cycles satisfying the owner rows is an owner-transversal rotor
circulation; the remaining two ledgers add cyclewise.  This proves exact
equivalence of (2.8) with the Boolean problem.

Dropping integrality gives a covering/set-partitioning LP.  The owner
and divergence rows are equalities and therefore have free dual
variables \(\alpha\) and \(\theta\); the lower-cover rows are
greater-than inequalities in a minimization problem and therefore have
nonnegative variables \(u\).  The cost of every cycle is one, giving
the inequalities in (2.9). \(\square\)

The state-potential form (2.5) and the cycle-master form (2.9) encode the
same fractional obstruction.  The former retains flow explicitly; the
latter eliminates flow but exposes the integral grouping into
owner-disjoint cycles.

## 3. The uniform \(A\)-face defeats every real separator

Set

\[
z^*_{\pi,A}=\frac1D,
\qquad z^*_{\pi,B}=0.
\tag{3.1}
\]

### Lemma 3.1

The point \(z^*\) satisfies (1.6)--(1.9) for every \(H\le m-1\).
At depth \(q\), every lower target has load

\[
\rho_q=
\frac{(m-q)!(m+1+q)!}{m!(m+1)!}
=\frac{W}{\binom n{m-q}}
=\prod_{j=0}^{q-1}\frac{m+2+j}{m-j}.
\tag{3.2}
\]

#### Proof

There are \(D\) states above every owner, proving (1.6).  Since \(A\)
permutes \(S_n\), (1.7) holds.

For signed divergence, swap positions \(1\) and \(n\) in \(\pi\).
This involution leaves \(K_q(\pi)\) fixed and interchanges the two sets
in (1.5).  Uniform state mass therefore gives zero in every coordinate
of (1.9).

A fixed \(r_q\)-set occurs as the first \(r_q\) coordinates of exactly
\(r_q!(n-r_q)!=(m-q)!(m+1+q)!\) permutations.  Division by \(D\) proves
(3.2).  Its factors are all at least one, so (1.8) holds. \(\square\)

### Corollary 3.2 (quantitative dual domination)

For every \((\phi,\theta,u)\),

\[
\boxed{
\sum_XM_X(\phi,\theta,u)
\ge
\sum_{q=0}^{H}\rho_q\sum_Su_{q,S}.}
\tag{3.3}
\]

#### Proof

For every owner, its maximum in (2.4) is at least the average of the
\(A\)-column expression over its \(D\) states.  Sum these ownerwise
averages.  The \(\phi\)-sum telescopes because \(A\) is a permutation;
the \(\theta\)-sum vanishes by Lemma 3.1; and (3.2) evaluates the
\(u\)-sum. \(\square\)

For fixed \(A_0\), uniformly for \(q\le A_0\sqrt m+1\),

\[
\log\rho_q
=\sum_{j=0}^{q-1}\log\left(1+\frac{2j+2}{m-j}\right)
=\frac{q(q+1)}m+O_{A_0}(m^{-1/2}).
\tag{3.4}
\]

Indeed the sum of the quadratic Taylor remainders and the denominator
corrections is \(O(q^3/m^2)=O_{A_0}(m^{-1/2})\).  Equation (0.3)
follows for \(H=\lceil A_0\sqrt m\rceil\).  Thus imposing signed
divergence cancellation removes none of the Gaussian fractional margin.

## 4. Exact integral obstruction on the \(A\)-only face

Suppose now that \(z\) is Boolean and \(z_{\pi,B}=0\) for every state.
Write \(y_\pi=z_{\pi,A}\).  Flow becomes

\[
y_\pi=y_{A^{-1}\pi}.
\tag{4.1}
\]

The action of \(A\) freely rotates the first \(N=2m\) distinct entries
and fixes the last entry.  Hence every \(A\)-orbit has exactly \(N\)
states, and the selected states are a union of complete \(A\)-orbits.
Let \(t\) be the number of selected orbits and \(t_c\) the number whose
fixed last, or missing, coordinate is \(c\).  Summing the owner equations
gives

\[
t=\frac{W}{N}.
\tag{4.2}
\]

### Lemma 4.1 (rank-independent coordinate projection)

At any one depth \(q\), the signed-divergence equations imply, for
every coordinate \(c\),

\[
\boxed{
\sum_{\pi\in S_n}z_{\pi,A}
\bigl(\mathbf 1[x_n=c]-\mathbf 1[x_1=c]\bigr)=0.}
\tag{4.3}
\]

#### Proof

Sum (1.9) over all \(r_q\)-sets \(T\) containing \(c\).  Neither
\(x_1\) nor \(x_n\) belongs to \(K_q(\pi)\), so the contribution of
one \(A\)-column is

\[
\bigl(\mathbf 1[c\in K_q(\pi)]+\mathbf 1[x_n=c]\bigr)
-
\bigl(\mathbf 1[c\in K_q(\pi)]+\mathbf 1[x_1=c]\bigr).
\]

The two core terms cancel, giving (4.3).  The resulting row is
independent of \(q\). \(\square\)

This coordinate projection is in fact redundant once the owner and flow
rows are present.  To see this, let \(N_j(c)\) be the total selected
state mass with coordinate \(c\) in position \(j\).  Both rotors shift
position \(j+1\) to position \(j\) for \(j\le n-2\), so flow gives

\[
N_1(c)=\cdots=N_{n-1}(c).
\]

The owner equations give

\[
\sum_{j=1}^{m}N_j(c)=\binom{n-1}{m-1}=\frac mnW,
\]

hence every \(N_j(c)=W/n\) for \(j<n\).  Since every selected state
contains \(c\) exactly once, also \(N_n(c)=W/n\).  Stationarity in the
last position says

\[
N_n(c)=
\sum_\pi z_{\pi,A}\mathbf 1[x_n=c]
+\sum_\pi z_{\pi,B}\mathbf 1[x_1=c],
\]

whereas

\[
N_1(c)=
\sum_\pi z_{\pi,A}\mathbf 1[x_1=c]
+\sum_\pi z_{\pi,B}\mathbf 1[x_1=c].
\]

Their equality is (4.3).  Thus genuine signed-divergence content starts
above its one-coordinate marginal.

### Theorem 4.2 (balanced missing-label theorem)

Every integral \(A\)-only owner-transversal circulation satisfies

\[
t_c=\frac{t}{n}=\frac{W}{nN}
=\frac{\operatorname{Cat}_m}{2m}
\qquad(c\in[n]).
\tag{4.4}
\]

Moreover, if an integral union of \(A\)-orbits satisfies the signed
divergence equations at any single rank \(1\le r\le m\), then it also
satisfies \(t_c=t/n\), even without using the owner-incidence equations.

#### Proof from owner incidence

Fix \(c\in[n]\).  An \(A\)-orbit with missing label \(c\) contributes
no owner containing \(c\).  In an orbit with a different missing label,
the coordinate \(c\) occupies each of the \(N\) cyclic positions once,
and belongs to exactly \(m\) of the length-\(m\) cyclic owner windows.
Thus the total number of selected owners containing \(c\) is

\[
m(t-t_c).
\tag{4.5}
\]

Owner transversality says that this is the number of all \(m\)-subsets
containing \(c\):

\[
m(t-t_c)=\binom{n-1}{m-1}=\frac mn W.
\tag{4.6}
\]

Substitute \(t=W/N\).  Since \(N=n-1\),

\[
t_c=\frac{W}{N}-\frac Wn=\frac{W}{nN},
\]

which is (4.4).

#### Independent proof from signed divergence

Fix a protected rank \(r\), a coordinate \(c\), and sum the divergence
coordinates over all \(r\)-sets \(T\) containing \(c\).  Consider one
complete \(A\)-orbit, with missing label \(a\).

If \(a=c\), all \(N\) positive endpoints \(K_r\cup\{a\}\) contain
\(c\), while no negative endpoint \(K_r\cup\{x_1\}\) does.  Its
coordinate-moment contribution is \(N\).

If \(a\ne c\), the coordinate \(c\) occurs in the rotating
\((r-1)\)-block \(K_r\) exactly \(r-1\) times.  It therefore occurs in
\(r-1\) positive endpoints.  It occurs in a negative endpoint either
through \(K_r\), in those \(r-1\) rotations, or as \(x_1\), in one
further rotation.  These cases are disjoint, so it occurs in \(r\)
negative endpoints.  This orbit contributes \(-1\).

The total coordinate moment is consequently

\[
Nt_c-(t-t_c)=nt_c-t.
\tag{4.7}
\]

Equivalently, this is obtained by summing the rank-independent row
(4.3) around the selected orbits.  Exact signed cancellation makes
(4.7) zero, and hence \(t_c=t/n\).
This completes both proofs. \(\square\)

### Corollary 4.3 (Catalan divisibility and a prime subsequence)

An integral point on the \(A\)-only face of (1.6)--(1.9) can exist only
if

\[
2m\mid\operatorname{Cat}_m.
\tag{4.8}
\]

For every prime \(m=p>2\), no such point exists.

#### Proof

The integer \(t_c\) in (4.4) proves (4.8).  For a prime \(p\), the
coefficient of \(x^p\) in

\[
(1+x)^{2p}\equiv(1+x^p)^2\pmod p
\]

gives

\[
\binom{2p}{p}\equiv2\pmod p.
\]

Since \(p+1\equiv1\pmod p\),

\[
\operatorname{Cat}_p=\frac1{p+1}\binom{2p}{p}
\equiv2\pmod p.
\]

Thus \(p\nmid\operatorname{Cat}_p\), so (4.8) fails. \(\square\)

For every fixed \(A_0>0\), sufficiently large primes have
\(H=\lceil A_0\sqrt p\rceil\le p-1\).  Lemma 3.1 supplies a feasible
fractional point on this face, including exact signed cancellation at
all these depths, while Corollary 4.3 proves that the face contains no
integral point.  Therefore every integral point of the unrestricted
mixed system obeys (0.7).  This is a genuine integer-hull cut, not a
failure caused by insufficient Gaussian cover margin.

## 5. Why the known cancellation kernels do not repair the face

### 5.1 Opposite switch pairs

For an injective de Bruijn arc

\[
e=(x_1,x_2,\ldots,x_{n-1})
\]

with missing coordinate \(x_n\), swapping positions \(1,n\) gives the
opposite divergence flag at every rank.  The uniform \(A\)-only point
puts equal mass on the two members of every such pair, which is a
statewise explanation of Lemma 3.1.  But the two de Bruijn arcs have the
same head \((x_2,\ldots,x_{n-1})\); an integral clustered cycle cover
cannot select both.  Shuffling their middle blocks separates the heads
but forces the two \(A\)-successors into one owner fibre.  Hence the
fractional pair cancellation is not an integral rounding operation.

### 5.2 Incidence \(C_6\) cocycles

An incidence-hexagon flip preserves every prefix ledger and therefore
preserves the signed divergence equations.  It does not, however,
supply a direction inside the \(A\)-only flow face.

Indeed, let \(h_{\pi,A}\) be any signed tangent vector supported on this
face and satisfying homogeneous flow.  Then

\[
h_{\pi,A}=h_{A^{-1}\pi,A},
\tag{5.1}
\]

so \(h\) is constant on each complete \(N\)-state \(A\)-orbit.  A
single incidence-hexagon vector has support on six de Bruijn arcs.  For
the asymptotic range \(m\ge4\), \(N=2m>6\), so a nonzero such vector
cannot satisfy (5.1).  More invariantly, every move confined to the
\(A\)-only face changes whole \(A\)-orbit multiplicities and remains
subject to the balance law (4.4).  The all-rank \(C_6\) kernel becomes
available only after leaving this face and activating a genuinely mixed
state change.

## 6. Exact boundary

The following are proved.

* The owner--flow--lower-cover--signed-cancellation LP has the exact
  Farkas dual (2.5).
* It is fractionally feasible with the Gaussian margin (3.2)--(3.4),
  even on the \(A\)-only face.
* That face has an exact missing-label balance law and is integer-empty
  whenever \(2m\nmid\operatorname{Cat}_m\), in particular for every
  prime \(m>2\).
* Opposite switch pairs and isolated incidence \(C_6\) cocycles do not
  round this face.

What is not proved is infeasibility of the mixed \(A/B\) integer system.
A successful theorem must leave the obstructed face, use both rotor
types, and correlate the resulting higher cancellation circuits with
the lower-prefix transversal.  Ordinary fractional Farkas feasibility,
including its constant Gaussian surplus, cannot supply that rounding.
