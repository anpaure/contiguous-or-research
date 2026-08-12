# Lane O: exact gates at the singular prefix-freezing boundary

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Exact outcome

Fix \(A>0\), put

\[
n=2m+1,\qquad
W=\binom nm,\qquad
B=\frac Wn=\operatorname{Cat}_m,\qquad
K=\lceil A\sqrt m\rceil,
\]

and, at depth \(q\),

\[
r_q=m-q,\qquad
V_q=\binom{[n]}{r_q},\qquad
N_q=|V_q|,\qquad
W=c_qN_q+\rho_q,\quad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,\quad
0\le\rho_q<N_q.
\]

All asymptotic assertions are for fixed \(A\) as \(m\to\infty\).
Whenever the full window through \(K\) is invoked, \(m\) is sufficiently
large that \(K\le m-1\).

No low-cost balanced literal endpoint factor is constructed here. The
advance is an exact positive/negative boundary package which fixes every
floor baseline, proves mobile one-rank containment integrality, quantifies
the residual point-margin leave, and isolates genuinely stronger
obstructions.

1. **The whole mobile containment-cut system is a matroid.** At one rank,
   the \(0/1\) high-quota families satisfying every upper-shadow
   containment cut are exactly the bases of an explicit
   \(S_n\)-invariant transversal-minor matroid of rank \(\rho_q\).
   Consequently all ordinary containment cuts have an integral mobile
   quota solution. Any additional laminar family of valid caps can be
   imposed integrally by matroid intersection.

2. **One-rank point-regular balance has only a subcritical leave.** A
   negatively correlated base of the containment matroid can be made
   exactly point-regular after at most
   \[
   L_q\le\frac n2\sqrt{d_q},\qquad
   d_q=\frac{r_q\rho_q}{n},
   \]
   changes. All but \(L_q\) middle owners can then be matched integrally
   into the prescribed point-regular balanced quota. Uniformly through
   \(K=O_A(\sqrt m)\),
   \[
   \sum_{q\le K}L_q=o(W/\sqrt m).
   \]
   Thus no critical owner-mass obstruction comes from the one-rank
   maximum-matching deficiency of some regular quota. A zero-leave regular
   matroid base is not proved, and alignment to the prescribed old factor
   can still have critical regular-and-Hall distance. The unmatched choices
   are not proved nested or cyclic.

3. **Exact regular-support completion.** For an old exact factor \(F\),
   distance to a point-regular balanced histogram is a positive support
   trade problem. Its exact value \(O_q^{\rm reg}(F)\) is derived below,
   together with a stronger regular-and-Hall value \(O_q^{\rm RH}(F)\).
   Every literal balanced endpoint satisfies
   \[
   R_q\ge O_q^{\rm RH}(F)\ge O_q^{\rm reg}(F),
   \]
   and the released old/new incidences obey exact zero-margin and
   alternating-cycle laws. These constraints are absent from a generic
   Boolean Hoffman flow.

4. **Cross-depth violation width.** Clone every old lower deficit and
   every old upper excess, ordered by Boolean containment across depths.
   If \(w_t^-\) and \(w_t^+\) are the two prefix widths, every integral
   permanent-prefix completion, Boolean or literal, obeys
   \[
   R_t\ge\max\{w_t^-,w_t^+\},\qquad
   \mathcal C\ge
   \sum_{t=1}^K\frac{\max\{w_t^-,w_t^+\}}{c_t}.
   \]
   The lower-token width is the exact number of abstract nested suffix
   paths required when roots, saturated upper cells, and row packets are
   relaxed.

5. **Literal cyclic high-slot cuts.** A localized release inequality
   counts both mandatory releases above \(c_q+1\) and the further releases
   needed when a target family cannot contain enough endpoint high cells.
   For a \(t\)-star, cyclic row spans give the exact numerical endpoint cap
   \[
   a(L-q)+(b-q)_+,
   \quad
   L=m-t+1,\quad
   \binom{n-t}{m-t}=aL+b.
   \]
   Pairwise-disjoint logarithmic stars at
   \(\Theta_A(\sqrt m)\) depths would force an explicit
   \(\Omega_A(W)\) stopping cost. The required factor-specific defects are
   not proved universally.

6. **A genuine exact-factor basin is closed.** Combining the new
   cross-depth theorem with the audited marked-gap theorem shows that the
   canonical MSW factor, and every factor within row distance
   \((1/8-\varepsilon)B\), has permanent cost
   \(\Omega_{A,\varepsilon}(W\sqrt m)\) to every balanced literal endpoint.
   Thus the canonical MSW basin cannot supply the missing singular
   solution.

The exact surviving gate is now narrower. One must correlate the
subcritical one-rank leaves across all depths into nested owner paths,
make the regular high families satisfy the crossing cyclic caps, and
package the result into literal \(n\)-rows. None of those three steps is
proved here, so no constant-one conclusion is claimed.

## 1. Literal endpoint setup

Let \(F\) be an oriented exact middle wreath factor. For each middle owner
\(X\in\binom{[n]}m\), write its canonical flag

\[
X=L_0^F(X)\supset L_1^F(X)\supset\cdots\supset L_K^F(X),
\]

and its depth-\(q\) load

\[
\mu_q^F(S)=\#\{X:L_q^F(X)=S\}.
\]

A literal endpoint solution consists of another oriented exact factor
\(G\), stopping depths \(a(X)\in\{0,\ldots,K\}\), and

\[
L_q^G(X)=L_q^F(X)\qquad(q\le a(X)).
\tag{1.1}
\]

When a theorem below is stated also for a Boolean endpoint, \(G\) denotes
instead an arbitrary integral nested path system with one path rooted at
each middle owner, balanced as in (1.5); the definitions of
\(\mathcal R_q,R_q\), and \(\mathcal C\) are unchanged. No cyclic-row
conclusion is then intended.

Put

\[
\mathcal R_q=\{X:a(X)<q\},\qquad R_q=|\mathcal R_q|,
\tag{1.2}
\]

and

\[
H_d=\sum_{q=d}^K\frac1{c_q},\qquad H_{K+1}=0.
\tag{1.3}
\]

The exact permanent cost is

\[
\mathcal C(F,G,a)
=\sum_{q=1}^K\frac{R_q}{c_q}
=\sum_XH_{a(X)+1}.
\tag{1.4}
\]

The endpoint is balanced when

\[
\mu_q^G(S)=c_q+\mathbf1_{\{S\in\mathcal H_q\}},
\qquad |\mathcal H_q|=\rho_q.
\tag{1.5}
\]

Every exact factor has the point margin

\[
\sum_{S\ni x}\mu_q^F(S)=Br_q
\qquad(x\in[n]),
\tag{1.6}
\]

because one cyclic row has \(n\) distinct \(r_q\)-intervals and each
coordinate lies in exactly \(r_q\) of them. Hence a literal balanced high
family is necessarily point-regular:

\[
\deg_{\mathcal H_q}(x)
=d_q:=Br_q-c_q\binom{n-1}{r_q-1}
=\frac{r_q\rho_q}{n}.
\tag{1.7}
\]

The last expression is an integer because the first two are integers.

For all sufficiently large \(m\), the safe constant

\[
C_A=\left\lceil e^{\,2(A+1)(A+2)}\right\rceil
\tag{1.8}
\]

satisfies \(c_q\le C_A\) for \(q\le K\).

Indeed,

\[
\log\frac W{N_q}
\le\frac{q(q+1)}{m-q+1}.
\]

For large \(m\), \(q\le K\) implies
\(q\le(A+1)\sqrt m\), \(q+1\le(A+2)\sqrt m\), and
\(m-q+1\ge m/2\). Hence \(W/N_q\le
e^{2(A+1)(A+2)}\), and \(c_q=\lfloor W/N_q\rfloor\le C_A\).

## 2. Mobile containment cuts form an exact matroid

Fix one depth \(q\), abbreviate

\[
r=r_q,\quad E=V_q,\quad N=N_q,\quad c=c_q,\quad\rho=\rho_q,
\]

and for \(\mathcal U\subseteq E\) let

\[
\Gamma(\mathcal U)
=\{X\in\tbinom{[n]}m:\exists S\in\mathcal U,\ S\subseteq X\}
\tag{2.1}
\]

be its upper middle shadow.

### Lemma 2.1 (exact containment cut and normalized slack)

Every exact factor load \(\nu\) satisfies

\[
\boxed{\nu(\mathcal U)\le|\Gamma(\mathcal U)|.}
\tag{2.2}
\]

Moreover, with

\[
\theta=\frac{\rho}{N},\qquad
f(\mathcal U)=|\Gamma(\mathcal U)|-c|\mathcal U|,
\tag{2.3}
\]

one has

\[
\boxed{f(\mathcal U)\ge\theta|\mathcal U|\ge0,\qquad
f(E)=\rho.}
\tag{2.4}
\]

#### Proof

In one cyclic row, count pairs \((S,X)\) in which \(S\in\mathcal U\) is
an \(r\)-interval, \(X\) is an \(m\)-interval, and \(S\subseteq X\).
Every row occurrence of \(S\) has exactly
\(\binom{m-r+1}{1}=q+1\) cyclic \(m\)-interval extensions, while every
row \(m\)-interval has exactly \(q+1\) cyclic \(r\)-subintervals of the
relevant length. Restricting the first coordinate to \(\mathcal U\)
therefore gives no more pairs than restricting the second coordinate to
\(\Gamma(\mathcal U)\). Division by \(q+1\), followed by exact middle
ownership, proves (2.2).

For (2.4), count all containment pairs between \(\mathcal U\) and its
upper shadow. Every \(r\)-set has
\(\binom{n-r}{m-r}\) middle supersets, and every middle set contains at
most \(\binom mr\) members of \(\mathcal U\). Hence

\[
\frac{|\Gamma(\mathcal U)|}{W}
\ge\frac{|\mathcal U|}{N}.
\]

Since \(W/N=c+\theta\), this proves
\(|\Gamma(\mathcal U)|\ge(c+\theta)|\mathcal U|\).
Finally \(\Gamma(E)=\binom{[n]}m\), so \(f(E)=W-cN=\rho\).
\(\square\)

### Theorem 2.2 (shadow-quota matroid)

The set system

\[
\mathcal I_q=
\left\{
I\subseteq E:
|I\cap\mathcal U|\le f(\mathcal U)
\text{ for every }\mathcal U\subseteq E
\right\}
\tag{2.5}
\]

is the independent-set family of an \(S_n\)-invariant matroid
\(\mathsf M_q\) of rank \(\rho\). Consequently there exists a
\(\rho\)-element high family \(\mathcal H\) satisfying every containment
cut

\[
c|\mathcal U|+|\mathcal H\cap\mathcal U|
\le|\Gamma(\mathcal U)|.
\tag{2.6}
\]

A prescribed one-rank high-cell subset \(Z\subseteq E\) extends to such a high
family if and only if \(Z\in\mathcal I_q\).

#### Proof

Make \(c\) mandatory clones and one optional clone of every \(S\in E\).
Join every clone of \(S\) to all middle sets \(X\supseteq S\). The
transversal matroid on these left clones is denoted \(\mathsf T\), and
\(\mathcal C\) denotes the set of all mandatory clones.

The set \(\mathcal C\) is independent. Indeed, Hall for a family
\(\mathcal U\) of underlying \(r\)-sets is
\[
c|\mathcal U|\le|\Gamma(\mathcal U)|,
\]
which follows from (2.4). Contract \(\mathcal C\) in \(\mathsf T\) and
restrict to the optional clones. Call the resulting matroid
\(\mathsf M_q\).

For \(I\subseteq E\), the set \(\mathcal C\cup I\) is matchable exactly
when every underlying family \(\mathcal U\) obeys

\[
c|\mathcal U|+|I\cap\mathcal U|
\le|\Gamma(\mathcal U)|.
\]

Necessity is Hall applied to all selected clones over \(\mathcal U\).
For sufficiency, an arbitrary clone subfamily supported on
\(\mathcal U\) has cardinality at most the displayed left side, so the
same inequalities are every Hall cut. This proves (2.5).

It remains to compute the rank. The transversal matroid on all mandatory
and optional clones has rank \(W\). To see this, match the \(W\) right
middle sets into left clones. For a right family \(\mathcal X\), normalized
lower-shadow counting gives

\[
\frac{|\partial\mathcal X|}{N}\ge\frac{|\mathcal X|}{W}.
\]

There are \(c+1\) clones over every member of \(\partial\mathcal X\), and
\((c+1)N\ge W\); hence

\[
(c+1)|\partial\mathcal X|\ge|\mathcal X|.
\]

Hall gives a matching saturating all right vertices. Therefore

\[
\operatorname{rk}(\mathsf M_q)
=W-|\mathcal C|
=W-cN=\rho.
\]

The construction is coordinate-equivariant, proving \(S_n\)-invariance.
The basis-extension assertion is the ordinary matroid basis theorem.
\(\square\)

This theorem proves that ordinary mobile containment cuts have no
integrality gap. It does not impose the point equalities (1.7).

### Corollary 2.3 (laminar caps remain integral)

Let \(\mathscr L\) be a laminar family of subsets of \(E\), containing
\(E\), and let integer caps \(b_L\) satisfy

\[
b_E=\rho,\qquad \theta|L|\le b_L\quad(L\in\mathscr L).
\tag{2.7}
\]

Then \(\mathsf M_q\) has a base \(\mathcal H\) satisfying

\[
|\mathcal H\cap L|\le b_L\qquad(L\in\mathscr L).
\tag{2.8}
\]

#### Proof

The caps define a laminar matroid. The matroid \(\mathsf M_q\) has a base
by Theorem 2.2. Average the indicator of one base under \(S_n\). Since
\(S_n\) is transitive on the \(r\)-sets, the average is exactly
\(\theta\mathbf1_E\), so this vector lies in the base polytope of
\(\mathsf M_q\). It lies in the laminar base polytope by (2.7). The
matroid-intersection polytope is integral, so the nonempty common-base
face contains an integral common base. \(\square\)

Crossing point-star equalities and the full family of cyclic star caps are
not laminar, so Corollary 2.3 does not settle them.

## 3. A subcritical one-rank point-regular leave

### Lemma 3.1 (near-regular containment base)

The matroid \(\mathsf M_q\) has a random base \(\mathcal H\) with

\[
\mathbb P(S\in\mathcal H)=\theta
\tag{3.1}
\]

for every \(S\in E\), and

\[
\mathbb E[
\mathbf1_{\{S\in\mathcal H\}}
\mathbf1_{\{T\in\mathcal H\}}]
\le\theta^2
\qquad(S\ne T).
\tag{3.2}
\]

Consequently, if \(D_x=\deg_{\mathcal H}(x)\), then

\[
\mathbb ED_x=d:=\frac{r\rho}{n},\qquad
\operatorname{Var}D_x\le d,
\tag{3.3}
\]

and some base satisfies

\[
\boxed{
\sum_{x=1}^n(D_x-d)^2\le nd,\qquad
\sum_x|D_x-d|\le n\sqrt d.}
\tag{3.4}
\]

#### Proof

Average any base under the transitive \(S_n\)-action, as in Corollary 2.3.
This proves that \(\theta\mathbf1_E\) lies in the base polytope. Apply
pipage rounding inside that base polytope. On a
two-coordinate exchange line,

\[
x_S\mapsto x_S+t,\qquad x_T\mapsto x_T-t,
\]

move randomly to the two maximal endpoints with expectation \(t=0\).
The minimal face dimension drops, so iteration ends at a base while
preserving every coordinate expectation. The product

\[
(x_S+t)(x_T-t)
\]

is concave in \(t\), and every product involving a third unchanged
coordinate is affine. Thus every pair product has nonincreasing
expectation, proving (3.2). The needed exchange lines exist because every
edge of a matroid base polytope is parallel to
\(\mathbf e_S-\mathbf e_T\).

Now

\[
D_x=\sum_{S\ni x}\mathbf1_{\{S\in\mathcal H\}}.
\]

The marginal gives

\[
\mathbb ED_x
=\theta\binom{n-1}{r-1}
=\frac{r\rho}{n}=d.
\]

Pairwise nonpositive covariance gives

\[
\operatorname{Var}D_x
\le
\theta(1-\theta)\binom{n-1}{r-1}
\le d.
\]

Sum over \(x\), then choose one outcome no larger than the expectation.
Cauchy--Schwarz gives the second inequality in (3.4). \(\square\)

### Lemma 3.2 (exact regularization)

Every simple \(r\)-family \(\mathcal H\) of size \(\rho\) can be changed
into a simple \(d\)-regular \(r\)-family \(\mathcal H'\) using at most

\[
\frac12\sum_x|\deg_{\mathcal H}(x)-d|
\tag{3.5}
\]

one-point exchanges.

#### Proof

If the degrees are not all \(d\), choose \(a,b\) with
\(D_a>d>D_b\). There is an \(S\in\mathcal H\) with
\(a\in S,b\notin S\), but

\[
S-a+b\notin\mathcal H.
\]

Otherwise \(S\mapsto S-a+b\) injects every member containing \(a\) but
not \(b\) into a member containing \(b\) but not \(a\), contradicting
\(D_a>D_b\). Replace \(S\) by \(S-a+b\). The \(\ell^1\) degree error
drops by two. Iterate. The average degree is
\(r\rho/n=d\), so termination gives exact regularity. \(\square\)

### Theorem 3.3 (point-regular balanced owner assignment with small leave)

At every rank \(q\), there are

- a point-regular \(\rho_q\)-element high family \(\mathcal H'_q\);
- a set of \(W-L_q\) distinct middle owners; and
- an integral assignment of those owners to contained \(r_q\)-sets,

such that every cell \(S\) is used at most

\[
c_q+\mathbf1_{\{S\in\mathcal H'_q\}}
\]

times, and

\[
\boxed{L_q\le\frac n2\sqrt{d_q}.}
\tag{3.6}
\]

Uniformly for \(q\le K\),

\[
\boxed{
\sum_{q=1}^KL_q
\le\frac{nK}{2}\sqrt W
=o(W/\sqrt m).}
\tag{3.7}
\]

Every containment-Hall cut for the completed regular quota is violated by
at most \(L_q\).

#### Proof

Take the base \(\mathcal H\) from Lemma 3.1 and regularize it to
\(\mathcal H'\) by Lemma 3.2. Put

\[
L=|\mathcal H\setminus\mathcal H'|.
\]

The number \(L\) is no larger than the number of exchanges, so (3.4)
gives \(L\le n\sqrt d/2\). The intersection
\(I=\mathcal H\cap\mathcal H'\) is independent in \(\mathsf M_q\).
In the transversal presentation of Theorem 2.2, all \(cN\) mandatory
clones together with the \(|I|=\rho-L\) optional clones in \(I\) therefore
match into distinct middle owners. This matches

\[
cN+\rho-L=W-L
\]

owners into the point-regular quota
\(c+\mathbf1_{\mathcal H'}\), leaving \(L\) owners and exactly the
\(L\) bonus clones in \(\mathcal H'\setminus I\) unmatched. Changing
\(\mathcal H\) to \(\mathcal H'\) increases the left side of every Hall
cut by at most \(L\); the displayed partial matching leaves exactly
\(L\) owners and \(L\) bonus slots unmatched. This gives the final
assertion.

Since \(d_q\le W\), summing (3.6) gives the first bound in (3.7). Finally
\[
\frac{nK\sqrt W}{W/\sqrt m}
=O_A\left(\frac{m^2}{\sqrt W}\right)\longrightarrow0.
\]
\(\square\)

The assignments supplied independently at different ranks need not be
nested. Even if nested, they need not decompose into cyclic wreath rows.
Those are exactly the two unsolved positive couplings.

Symmetry and transversality alone cannot improve the small leave in
Theorem 3.3 to zero. Here is a finite abstract obstruction; it is not
claimed to occur in the specific shadow-quota matroid.

Let the ground set be the six edges of \(K_4\), partitioned into its three
perfect matchings

\[
P_1=\{12,34\},\quad P_2=\{13,24\},\quad P_3=\{14,23\}.
\]

Give an edge in \(P_i\) the two transversal neighbors \(\{0,i\}\). The
resulting transversal matroid has rank four, and a four-edge set is a base
if and only if it meets all three \(P_i\): its profile is then
\((2,1,1)\), which matches to the four slots; if it misses one class, its
four elements have only three neighbors. This base criterion is
\(S_4\)-invariant. Averaging any base gives the uniform base-polytope
point \((2/3)\mathbf1\), whose target point degree is the integer two.
Nevertheless, a four-edge family with every vertex degree two is a
Hamilton four-cycle, and each Hamilton four-cycle is the complement of
one \(P_i\), hence is a nonbase. Thus an invariant transversal matroid
with an integral regular barycenter need not have a regular base.

There is an exact simultaneous construction when the natural coordinate
cycle acts freely at every controlled rank.

### Theorem 3.4 (cyclic-quotient point-regular balanced resolution)

Assume

\[
\gcd(n,m-q)=1\qquad(0\le q\le K).
\tag{3.8}
\]

Equivalently,

\[
\gcd(n,2q+1)=1\qquad(0\le q\le K).
\tag{3.9}
\]

Then there is an integral balanced nested Boolean resolution through
depth \(K\) which is equivariant under one \(n\)-cycle on the coordinates.
At every depth its high family is a union of full coordinate-cycle orbits
and is therefore exactly point-regular.

In particular, the theorem applies when \(n\) is prime, and more generally
when the least prime divisor of \(n\) exceeds \(2K+1\).

#### Proof

Fix a cyclic permutation \(\tau\) of \([n]\). Its action on \(k\)-sets is
free whenever \(\gcd(n,k)=1\): a set fixed by a nontrivial subgroup is a
union of equal subgroup orbits, so its cardinality has a nontrivial common
divisor with \(n\). Thus (3.8) makes every Boolean-layer orbit through
depth \(K\) have size \(n\). The equivalence (3.9) follows from

\[
n-2(m-q)=2q+1
\]

and the oddness of \(n\).

Quotient the layered Boolean deletion DAG by
\(\langle\tau\rangle\). At level \(q\) it has \(N_q/n\) quotient nodes.
Give every level-\(q\) node a through-arc with lower and upper capacities

\[
[c_q,c_q+1].
\]

Every middle quotient node has source supply one. For the uniform
fractional flow, every original level-\(q\) node has load

\[
\lambda_q=\frac W{N_q},
\]

and a node of size \(m-q\) splits this load equally among all of its
deletion arcs. Since

\[
\frac{\lambda_{q+1}}{\lambda_q}
=\frac{N_q}{N_{q+1}}
=\frac{n-(m-q)+1}{m-q},
\]

the incoming load at level \(q+1\) is exactly \(\lambda_{q+1}\).
This flow is \(\tau\)-invariant and descends to the quotient. Also
\(\lambda_q\in[c_q,c_q+1]\), so it respects every through-capacity.
Join every level-\(K\) through-arc to a common sink of total demand \(B\);
the displayed fractional flow supplies that demand.

The quotient is an ordinary lower/upper-capacitated network; parallel edge
orbits are retained. Integral supplies and capacities therefore give an
integral quotient flow. Decompose this quotient flow into unit quotient
paths before lifting. Every edge orbit between two free node orbits is a
perfect matching: from a fixed physical tail there is exactly one edge in
that orbit. Hence, after fixing one physical representative of the root
orbit of a quotient path, that path has a unique physical lift. Taking all
\(n\) translates of the lift gives one path from every physical root in
that root orbit. Doing this for every quotient path gives the required
equivariant nested resolution. Equivalently, a quotient arc of value
\(k\) lifts to value \(k\), not \(k/n\), on every physical arc in its
orbit.

The high nodes are whole free \(\tau\)-orbits. Since both \(W\) and
\(N_q\) are divisible by \(n\), so is \(\rho_q\). Every orbit of an
\(r_q\)-set contains each coordinate exactly \(r_q\) times. Hence the
union of \(\rho_q/n\) high orbits has degree

\[
\frac{\rho_q}{n}r_q=d_q
\]

at every coordinate. \(\square\)

At one rank the same proof is a biregular quotient
\(b\)-matching. The quotient degrees are

\[
\binom m q
\quad\text{and}\quad
\binom{m+q+1}q,
\]

whose ratio is \(W/N_q\); selecting quotient edges with left degree one
and right degree \(c_q\) or \(c_q+1\) lifts to an exact owner assignment.

Theorem 3.4 does not align to a prescribed factor. A translation orbit of
an arbitrary middle set need not be the \(m\)-window packet of any cyclic
coordinate order. Thus the theorem settles simultaneous nesting and exact
point margins in the coprime regime, but not literal wreath packetization
or low-cost common prefixes.

There is also an exact arithmetic reason that full coordinate-cycle
equivariance cannot be used as a universal literal packetization device.

### Theorem 3.5 (full-cycle literal-factor obstruction)

Let \(m\ge3\) be odd, let \(n=2m+1\) be prime, and let \(\tau\) be an
\(n\)-cycle on \([n]\). No exact oriented or unoriented wreath factor is
setwise invariant under \(\tau\).

#### Proof

For a cyclic coordinate order

\[
C=(z_0,z_1,\ldots,z_{n-1}),
\]

write

\[
X_i=\{z_i,z_{i+1},\ldots,z_{i+m-1}\},\qquad
\mathcal M(C)=\{X_i:i\in\mathbb Z_n\}.
\tag{3.10}
\]

First, \(\mathcal M(C)\) determines \(C\) up to rotation and reversal.
Indeed, for cyclic distance \(1\le s\le m\),

\[
|X_i\cap X_{i+s}|=m-s.
\]

For separations \(s>m\), use the reverse cyclic distance \(n-s\le m\).
Thus the graph on the packet vertices joining pairs with intersection
size \(m-1\) is exactly the cycle
\(X_0X_1\cdots X_{n-1}X_0\). Traversing either orientation of this
recovered cycle, the unique leaving label

\[
X_i\setminus X_{i+1}=\{z_i\}
\]

recovers the coordinate order. This proves the rigidity assertion.

Now suppose that an underlying packet is fixed by \(\tau\). The induced
action of \(\tau\) on its recovered \(n\)-cycle is nontrivial. Otherwise
every \(X_i\) would be fixed setwise, impossible because a nontrivial
power of a prime \(n\)-cycle has no nonempty proper invariant subset.
The induced automorphism has order \(n\), so in the dihedral group of the
recovered cycle it is a nontrivial rotation, say

\[
\tau(X_i)=X_{i+s},\qquad s\ne0.
\]

The leaving labels then give

\[
\tau(z_i)=z_{i+s}.
\]

Writing \(a=s^{-1}\pmod n\), the order is therefore, up to rotation,

\[
z_i=\tau^{ai}(z_0).
\tag{3.11}
\]

Conversely every \(a\in\mathbb Z_n^*\) gives a fixed packet of this form.
The parameters \(a\) and \(-a\) give the two reversals of the same packet,
and rigidity shows that there are no further coincidences. Hence exactly

\[
\frac{n-1}{2}=m
\tag{3.12}
\]

underlying packets are \(\tau\)-fixed. The induced action is a rotation,
not a reflection, so it preserves both orientations separately; however,
an exact factor can use at most one of the two orientations because they
have the same \(n\) middle owners.

If an exact factor \(F\) were \(\tau\)-invariant, \(\tau\) would permute
its \(B=\operatorname{Cat}_m\) rows in orbits of sizes \(1\) and \(n\).
If \(f\) rows were fixed, then

\[
B=f+nt,qquad 0\le f\le m.
\tag{3.13}
\]

Modulo the prime \(n\),

\[
\binom{n-1}{m}
=\prod_{j=1}^m\frac{n-j}{j}
\equiv(-1)^m,
\]

and \(2(m+1)=n+1\equiv1\pmod n\). Therefore

\[
B=\frac1{m+1}\binom{n-1}{m}
\equiv2(-1)^m
\equiv n-2=2m-1\pmod n.
\tag{3.14}
\]

For odd \(m\ge3\), the least nonnegative residue \(2m-1\) is larger
than \(m\), contradicting (3.13). \(\square\)

At \(m=1,n=3\), the residue equals \(m\) and the trivial fixed packet
exists, so the lower bound on \(m\) is necessary. For even \(m\), the
residue is \(2\), so this congruence alone does not decide existence.
Packet rigidity itself is unconditional for \(m\ge2\). Primality is used
in the stated obstruction to obtain row-orbit sizes \(1,n\) and the
modulo-\(n\) Catalan contradiction; no composite-\(n\) obstruction is
asserted. The theorem obstructs only full \(C_n\)-equivariance; it does
not obstruct a non-equivariant exact factor or a low-cost endpoint by a
different construction.

## 4. Exact regular-support completion and zero-margin laws

Fix a rank \(q\) and abbreviate \(r,N,c,\rho\) as in Section 2. Put

\[
\mu(S)=\mu_q^F(S),\qquad z(S)=\mu(S)-c,
\]

\[
\mathcal A=\{S:z(S)\ge1\},
\tag{4.1}
\]

and define two multisets on \(E\):

\[
P(S)=(z(S)-1)_+,\qquad
N^-(S)=(-z(S))_+.
\tag{4.2}
\]

Write

\[
p=\sum_SP(S),\qquad h=\sum_SN^-(S).
\tag{4.3}
\]

Then

\[
z=\mathbf1_{\mathcal A}+P-N^-,
\qquad
|\mathcal A|+p-h=\rho.
\tag{4.4}
\]

Taking point degrees in (4.4) and using (1.7) gives

\[
\deg\mathcal A+\deg P-\deg N^-=d\mathbf1.
\tag{4.5}
\]

### Theorem 4.1 (positive support-completion identity)

Let \(\mathcal H\subseteq E\), put

\[
Q=\mathcal A\setminus\mathcal H,\qquad
R=\mathcal H\setminus\mathcal A.
\tag{4.6}
\]

Then \(c+\mathbf1_{\mathcal H}\) is a point-regular balanced histogram if
and only if

\[
Q\subseteq\mathcal A,\qquad R\subseteq E\setminus\mathcal A,
\]

and

\[
\boxed{\deg(P\uplus Q)=\deg(N^-\uplus R).}
\tag{4.7}
\]

For every such completion,

\[
\boxed{
p+|Q|=h+|R|
=\frac12\|\mu-(c+\mathbf1_{\mathcal H})\|_1.}
\tag{4.8}
\]

Consequently the exact distance to a point-regular balanced histogram is

\[
\boxed{
O_q^{\rm reg}(F)
=p+\min\left\{
|Q|:
\begin{array}{l}
\text{there exists }R\subseteq E\setminus\mathcal A
\text{ with }Q\subseteq\mathcal A,\\
\deg(P\uplus Q)=\deg(N^-\uplus R)
\end{array}
\right\}.}
\tag{4.9}
\]

By contrast, the ordinary mobile overload, with no point-margin
requirement, is exactly

\[
\boxed{O_q(F)=\max\{p,h\}.}
\tag{4.10}
\]

#### Proof

For \(\mathcal H=(\mathcal A\setminus Q)\cup R\),

\[
z-\mathbf1_{\mathcal H}
=P+\mathbf1_Q-N^--\mathbf1_R.
\tag{4.11}
\]

The positive and negative supports in (4.11) are disjoint. If
\(\mathcal H\) is regular, subtracting its degree \(d\mathbf1\) from
(4.5) gives (4.7). Conversely, (4.7) and (4.11) give
\(\deg\mathcal H=d\mathbf1\). Summing all coordinate degrees in (4.7)
and using \(r>0\) gives

\[
p+|Q|=h+|R|.
\]

Together with (4.4), this implies
\[
|\mathcal H|
=|\mathcal A|-|Q|+|R|=\rho.
\]

Thus the completion is balanced and regular. Equation (4.11) now proves
(4.8) and (4.9).

For (4.10), if \(|\mathcal A|\ge\rho\), remove
\(|\mathcal A|-\rho=h-p\) cells of \(\mathcal A\), giving distance
\(h\). If \(|\mathcal A|<\rho\), add
\(\rho-|\mathcal A|=p-h\) outside cells, giving distance \(p\).
No smaller value can beat either the positive or negative mass.
\(\square\)

A simple regular \(r\)-family of size \(\rho\) always exists here. Indeed,
among all such simple families minimize the sum of squared point degrees.
If two degrees differ by at least two, the one-point exchange used in
Lemma 3.2 decreases that sum. Since the average \(r\rho/n=d\) is an
integer, every degree equals \(d\).

### Corollary 4.2 (explicit regularity lower and upper brackets)

Put

\[
w=\deg\mathcal A-d\mathbf1
=\deg N^--\deg P.
\tag{4.12}
\]

Then

\[
\boxed{
O_q^{\rm reg}(F)
\ge
\max\left\{
\max(p,h),
\frac{p+h}{2}+\frac{\|w\|_1}{2r}
\right\}.}
\tag{4.13}
\]

Also

\[
\boxed{
O_q(F)\le O_q^{\rm reg}(F)\le(r+2)O_q(F).}
\tag{4.14}
\]

#### Proof

Equation (4.7) gives

\[
\deg Q-\deg R=w.
\]

Write \(s=|Q|\). From (4.8),
\[
|R|=p+s-h.
\]

Therefore

\[
\|w\|_1
\le r(|Q|+|R|)
=r(2s+p-h).
\]

Since \(O_q^{\rm reg}=p+s\), this proves the second term in (4.13);
(4.10) gives the first.

For the upper bound, first add or remove \(|p-h|\le O_q(F)\) arbitrary
cells so that \(\mathcal A\) has size \(\rho\). The resulting degree
vector has \(\ell^1\)-distance at most \(2rO_q(F)\) from
\(d\mathbf1\): the corresponding balanced histogram is an ordinary
minimizer at half-\(\ell^1\) distance \(O_q(F)\) from \(\mu\), and taking
point degrees multiplies its full \(\ell^1\) distance by at most \(r\).
Lemma 3.2 regularizes it using at most \(rO_q(F)\)
exchanges. The final regular family differs from \(\mathcal A\) in at
most \((r+1)O_q(F)\) removals, so (4.9) gives
\(O_q^{\rm reg}\le(r+2)O_q(F)\). \(\square\)

The factor \(r\) in (4.14) is a real unresolved positivity gap; no exact
factor is proved to attain it at critical scale.

### Proposition 4.2A (coordinate-price support certificate)

For \(y\in\mathbb R^n\), write

\[
y(S)=\sum_{x\in S}y_x.
\]

Let \(A_s^{\min}(y)\) and \(A_s^{\max}(y)\) be respectively the sum of
the \(s\) smallest and \(s\) largest values \(y(S)\) over
\(S\in\mathcal A\). Define \(C_t^{\min}(y),C_t^{\max}(y)\) analogously
over \(E\setminus\mathcal A\), with the empty sum equal to zero. If a
support completion has \(|Q|=s\), then, with

\[
t=p+s-h,
\tag{4.15}
\]

one necessarily has, for every \(y\in\mathbb R^n\),

\[
\boxed{
A_s^{\min}(y)-C_t^{\max}(y)
\le \langle y,w\rangle
\le A_s^{\max}(y)-C_t^{\min}(y).}
\tag{4.16}
\]

Consequently, suppose that for every integer \(s<L\) satisfying

\[
0\le s\le|\mathcal A|,qquad
0\le p+s-h\le|E\setminus\mathcal A|,
\tag{4.17}
\]

there is a coordinate price \(y\) for which (4.16) fails. Then

\[
\boxed{O_q^{\rm reg}(F)\ge p+L.}
\tag{4.18}
\]

#### Proof

Equation (4.7) is equivalent to

\[
\deg Q-\deg R=w,
\]

and (4.8) gives \(|R|=p+s-h=t\). Pairing the degree identity with
\(y\) gives

\[
\langle y,w\rangle
=\sum_{S\in Q}y(S)-\sum_{S\in R}y(S).
\]

The first sum lies between the two \(A_s\) extrema and the second between
the two \(C_t\) extrema, proving (4.16). Excluding every admissible
\(s<L\) proves (4.18) from (4.9). \(\square\)

This is a necessary support-selection dual, not a sufficient theorem:
simultaneous simple \(0/1\) selection may have higher-order obstructions
not detected by coordinate prices.

### Theorem 4.3 (regular-and-Hall static obstruction)

Let \(\mathsf M_q\) be the shadow-quota matroid of Theorem 2.2, and define

\[
\mathfrak B_q^{\rm reg}
=\{\mathcal H:
\mathcal H\text{ is a base of }\mathsf M_q,\ 
\deg\mathcal H=d\mathbf1\}.
\tag{4.19}
\]

Put

\[
O_q^{\rm RH}(F)
=
\min_{\mathcal H\in\mathfrak B_q^{\rm reg}}
\frac12\|\mu-(c+\mathbf1_{\mathcal H})\|_1,
\tag{4.20}
\]

with value \(+\infty\) if the family is empty. Then

\[
\boxed{
O_q^{\rm RH}(F)
=p+|\mathcal A|
-\max_{\mathcal H\in\mathfrak B_q^{\rm reg}}
|\mathcal A\cap\mathcal H|
\ge O_q^{\rm reg}(F).}
\tag{4.21}
\]

Here the maximum over the empty family is \(-\infty\), so the displayed
identity retains the declared value \(+\infty\).

Every balanced literal endpoint solution satisfies

\[
\boxed{
R_q\ge O_q^{\rm RH}(F),\qquad
\mathcal C\ge H_qO_q^{\rm RH}(F).}
\tag{4.22}
\]

#### Proof

An actual literal endpoint high family is regular by (1.7), and satisfies
every containment cut by Lemma 2.1, hence lies in
\(\mathfrak B_q^{\rm reg}\). For two owner histograms, changing one
owner changes at most one old and one new cell, so

\[
\frac12\|\mu_q^F-\mu_q^G\|_1
\le
\#\{X:L_q^F(X)\ne L_q^G(X)\}
\le R_q.
\]

Minimize over the necessary endpoint family. The identity in (4.21) is
(4.8) with \(Q=\mathcal A\setminus\mathcal H\). Monotonicity of \(R_t\) gives
\(\mathcal C\ge R_qH_q\). \(\square\)

In particular, if \(q\le(A-\delta)\sqrt m\) for fixed
\(\delta>0\), and

\[
O_q^{\rm RH}(F)\ge\varepsilon W/\sqrt m,
\]

then

\[
\boxed{
\mathcal C
\ge
\left(\frac{\varepsilon\delta}{C_A}+o_A(1)\right)W.}
\tag{4.23}
\]

Appending the point-degree rows to a naive incidence matrix does not
preserve total unimodularity. For \(r\ge2\), fix an \((r-2)\)-set \(Z\)
and distinct \(a,b,c\notin Z\). On the three columns

\[
Z+ab,\qquad Z+bc,\qquad Z+ca
\]

and the point rows \(a,b,c\), the minor is

\[
\begin{pmatrix}
1&0&1\\
1&1&0\\
0&1&1
\end{pmatrix},
\]

whose determinant is \(2\). This is not an infeasibility theorem; it
only rules out the naive TU extension.

### Theorem 4.4 (zero-margin residual and alternating cycles)

For exact oriented factors \(F,G\) and stops satisfying (1.1), one has,
for every coordinate \(x\),

\[
\boxed{
\sum_{X\in\mathcal R_q}
\mathbf1_{\{x\in L_q^F(X)\}}
=
\sum_{X\in\mathcal R_q}
\mathbf1_{\{x\in L_q^G(X)\}}.}
\tag{4.24}
\]

For a deletion position \(1\le j\le K\), let

\[
\delta_j^F(X)=L_{j-1}^F(X)\setminus L_j^F(X)
\]

and similarly for \(G\). Then

\[
\boxed{
\#\{X\in\mathcal R_j:\delta_j^F(X)=x\}
=
\#\{X\in\mathcal R_j:\delta_j^G(X)=x\}.}
\tag{4.25}
\]

After cancelling common incidences, both the rank-\(q\) old/new cell
difference and every fixed-\(j\) deleted-letter difference decompose
integrally into alternating even cycles in the owner--coordinate
bipartite graph.

#### Proof

Both exact factors have point margin \(Br_q\mathbf1\). Owners outside
\(\mathcal R_q\) agree at depth \(q\); subtract their common contribution
to obtain (4.24).

In one oriented row, as its \(n\) phases vary, the \(j\)-th deleted
coordinate runs once through \([n]\). Thus globally every coordinate is
the \(j\)-th deletion letter exactly \(B\) times in either factor. Owners
outside \(\mathcal R_j\) have identical prefixes through \(j\), hence
identical \(j\)-th letters. Cancelling them proves (4.25).

For the rank-\(q\) statement, color an edge \((X,x)\) red when
\(x\in L_q^F(X)\setminus L_q^G(X)\), and blue for the reverse
difference. Every owner has equal red and blue degree because the two
cells have equal size; (4.24) gives equal red and blue degree at every
coordinate. The bipartite colored multigraph therefore decomposes into
alternating even cycles. At fixed \(j\), direct the arc
\(\delta_j^F(X)\to\delta_j^G(X)\); (4.25) makes the coordinate
multigraph Eulerian, and its directed cycles lift to alternating
owner--coordinate cycles. \(\square\)

These are necessary literal endpoint constraints. They do not apply to
an arbitrary Boolean Hoffman completion, and the cycle decomposition by
itself gives no numerical lower bound without an additional restriction
coupling the cycles across depths.

### Proposition 4.5 (componentwise packet localization)

Form the bipartite overlap multigraph whose left vertices are the rows of
\(F\), whose right vertices are the rows of \(G\), and whose edge labelled
\(X\) joins the two rows owning the middle set \(X\). Every vertex has
degree \(n\). Consequently every connected component contains the same
number \(p\) of old and new rows. Within each such component, and at each
deletion position \(j\), the old deleted-letter multiset and the new
deleted-letter multiset both contain every coordinate exactly \(p\)
times. At rank \(q\), both sides likewise have point degree \(pr_q\) at
every coordinate. Hence both cycle decompositions in Theorem 4.4 localize
inside overlap components; cancellation cannot pass between them.

If \(p=1\), the old and new rows have the same middle packet. For
\(m\ge2\), packet rigidity implies that their orientations are either the
same, in which case every owned flag is unchanged, or reversed, in which
case all \(n\) owned flags already differ at depth one.

#### Proof

If a component contains \(u\) old and \(v\) new rows, counting its edges
from the two sides gives \(nu=nv\), hence \(u=v=p\). At a fixed deletion
position, one oriented row uses every coordinate exactly once as its phase
runs through the row. Thus either side of the component uses each
coordinate exactly \(p\) times. Likewise its \(n\) rank-\(q\) intervals
give point degree \(r_q\), so either side has componentwise point degree
\(pr_q\). Subtracting owners frozen through the relevant depth preserves
both equalities. The cycle decomposition proof of Theorem 4.4 can
therefore be performed independently in every component.

For \(p=1\), the unique old and new rows own the same \(n\) middle sets.
The packet-rigidity argument in Theorem 3.5 recovers the cyclic coordinate
order up to reversal. Equal orientation gives equal flags. Under reversal,
the two possible first deletions from any \(m\)-window are its two distinct
endpoints, proving the last assertion. \(\square\)

This localization is stronger than the global zero-margin law, but gives
no critical numerical bound without information on the overlap-component
sizes or on admissible cycles inside them.

## 5. Cross-depth violation-token posets

For every depth \(q\) and cell \(S\in V_q\), define the lower-deficit and
upper-excess multiplicities

\[
d_q^-(S)=(c_q-\mu_q^F(S))_+,
\qquad
d_q^+(S)=(\mu_q^F(S)-c_q-1)_+.
\tag{5.1}
\]

Replace each multiplicity by that many distinguishable cloned tokens. For
either sign, order the tokens by

\[
(q,S,i)<(s,T,j)
\quad\Longleftrightarrow\quad
q<s\ \hbox{ and }\ T\subset S.
\tag{5.2}
\]

Tokens in the same layer are incomparable, including distinct clones at
the same cell. Let \(\mathcal P_t^-\) and \(\mathcal P_t^+\) be the two
posets restricted to depths at most \(t\), and let their widths be
\(w_t^-\) and \(w_t^+\).

### Theorem 5.1 (exact permanent-release width obstruction)

Every integral balanced permanent-prefix completion, Boolean or literal,
satisfies, for \(1\le t\le K\),

\[
\boxed{R_t\ge\max\{w_t^-,w_t^+\}.}
\tag{5.3}
\]

Consequently,

\[
\boxed{
\mathcal C(F,G,a)
\ge
\sum_{t=1}^K\frac{\max\{w_t^-,w_t^+\}}{c_t}.}
\tag{5.4}
\]

#### Proof

Fix the completion and let

\[
g_q(S)=\#\{X\notin\mathcal R_q:L_q^F(X)=S\}
\]

be the frozen load. The residual endpoint load is

\[
h_q(S)=\mu_q^G(S)-g_q(S).
\]

Since \(\mu_q^G(S)\ge c_q\) and \(g_q(S)\le\mu_q^F(S)\),

\[
h_q(S)\ge(c_q-g_q(S))_+
\ge(c_q-\mu_q^F(S))_+=d_q^-(S).
\tag{5.5}
\]

Assign the lower tokens at \((q,S)\) injectively to residual endpoint
occurrences at \(S\). Tokens assigned to one owner lie on that owner's
nested endpoint suffix, hence form a chain in (5.2).

For the upper tokens, let

\[
e_q(S)=\mu_q^F(S)-g_q(S)
\]

be the number of released old occurrences. Upper safety gives
\(g_q(S)\le\mu_q^G(S)\le c_q+1\), whence

\[
e_q(S)\ge(\mu_q^F(S)-c_q-1)_+=d_q^+(S).
\tag{5.6}
\]

Assign the upper tokens injectively to these released old occurrences.
Tokens assigned to one owner lie on its old canonical flag and again form
a chain. Every owner receiving a token of depth at most \(t\) belongs to
\(\mathcal R_t\). Thus \(R_t\) chains cover either prefix poset. Dilworth's
theorem proves (5.3), and summing \(R_t/c_t\) proves (5.4). \(\square\)

The weighted form retains the depths of an antichain rather than replacing
them by one prefix width.

### Theorem 5.2 (weighted chain dual)

Fix one sign and assign a nonnegative price \(y_v\) to each of its tokens.
Suppose that every chain \(C\) in the token poset satisfies

\[
\sum_{v\in C}y_v
\le H_{\min\{\operatorname{depth}(v):v\in C\}}.
\tag{5.7}
\]

Then every permanent-prefix completion obeys

\[
\boxed{\mathcal C(F,G,a)\ge\sum_vy_v.}
\tag{5.8}
\]

In particular, every antichain \(\mathcal D\) of either sign gives

\[
\boxed{
\mathcal C(F,G,a)
\ge\sum_{v\in\mathcal D}H_{\operatorname{depth}(v)}.}
\tag{5.9}
\]

#### Proof

Use the owner assignments in the proof of Theorem 5.1. The tokens assigned
to an owner \(X\) form a chain whose minimum depth is larger than
\(a(X)\). Since \(H_d\) is nonincreasing in \(d\), (5.7) charges that
chain at most \(H_{a(X)+1}\). Summing over owners gives (5.8). For an
antichain, set \(y_v=H_{\operatorname{depth}(v)}\) on \(\mathcal D\) and
zero elsewhere; every chain meets \(\mathcal D\) at most once, proving
(5.9). \(\square\)

### Proposition 5.3 (sharpness of lower width in the suffix relaxation)

If distinct middle roots, upper capacities, and cyclic row packaging are
discarded, then \(w_t^-\) is exactly the minimum number of nested Boolean
suffix paths needed to carry every lower token through depth \(t\).

#### Proof

The lower bound is Theorem 5.1. Conversely, Dilworth partitions
\(\mathcal P_t^-\) into \(w_t^-\) chains. Every chain consists of nested
sets at strictly increasing depths. Insert arbitrary intermediate sets,
extend its largest set upward to an \(m\)-set, and extend its smallest
designated set downward through depth \(t\). This gives one full Boolean
deletion path carrying the chain. \(\square\)

Thus chain condensation is the exact relaxed gate, but is not sufficient
for the verified staircase ILP: roots may collide, an upper-saturated cell
may block a path, and the paths may not assemble into literal rows.

There is also a useful purely combinatorial certificate. If a finite
violation poset has \(M\) cloned tokens and \(E_{\rm comp}\) unordered
comparable pairs, then its comparability graph has average degree
\(2E_{\rm comp}/M\). The Caro--Wei bound and Cauchy--Schwarz give

\[
\boxed{
w\ge\sum_v\frac1{1+\deg(v)}
\ge\frac{M^2}{M+2E_{\rm comp}}.}
\tag{5.10}
\]

Hence total mass \(M=\Omega(B\sqrt m)\)—equivalently, Catalan-scale mass
per layer across \(\Theta(\sqrt m)\) layers—with bounded average
cross-rank comparability forces a critical antichain.

### Corollary 5.4 (exact Gaussian-window thresholds)

Define

\[
\xi_A=\min\left\{\frac A4,\frac{\sqrt{\log2}}2\right\},
\qquad
I_m(A)=\left[
\left\lceil\frac{\xi_A}2\sqrt m\right\rceil,
\left\lfloor\xi_A\sqrt m\right\rfloor
\right]\cap\mathbb Z.
\tag{5.11}
\]

For all sufficiently large \(m\), one has \(c_q=1\) throughout
\(I_m(A)\), so lower tokens there are exactly holes and upper tokens are
exactly occurrences above load two.

Let \(w_I^\pm\) be the width of either sign restricted to this band. If,
for fixed \(\alpha>0\),

\[
\liminf_{m\to\infty}\frac{w_I^\pm}{B\sqrt m}\ge\alpha,
\]

then

\[
\boxed{
\liminf_{m\to\infty}\frac{\mathcal C}{W}
\ge\frac{\alpha(A-\xi_A)}{2C_A}.}
\tag{5.12}
\]

More sharply, suppose that for one fixed sign and every
\(q\in I_m(A)\) one can choose at least \(\eta B\) tokens in layer \(q\),
and that the union of all chosen tokens is an antichain. Then

\[
\boxed{
\liminf_{m\to\infty}\frac{\mathcal C}{W}
\ge
\frac{\eta\xi_A(A-3\xi_A/4)}{4C_A}.}
\tag{5.13}
\]

In particular, \(\mathcal C=o(W)\) forces

\[
\boxed{w_I^-=o(B\sqrt m),\qquad w_I^+=o(B\sqrt m).}
\tag{5.14}
\]

#### Proof

For \(q\le\xi_A\sqrt m\),

\[
\frac W{N_q}
=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}
\]

and

\[
\log\frac W{N_q}
\le\sum_{i=0}^{q-1}\frac{2(i+1)}{m-i}
\le\frac{q(q+1)}{m-q+1}
\le\xi_A^2+o_A(1)<\log2.
\]

Thus \(1<W/N_q<2\), proving \(c_q=1\).

Put \(Q=\lfloor\xi_A\sqrt m\rfloor\). Every band antichain has price at
least \(H_Q\) per token, and

\[
H_Q\ge\frac{K-Q+1}{C_A}
=\left(\frac{A-\xi_A}{C_A}+o_A(1)\right)\sqrt m.
\]

Since \(W=(2m+1)B\), (5.12) follows from (5.9). For the layerwise
antichain, use its actual depths and

\[
\begin{aligned}
\sum_{q\in I_m(A)}H_q
&\ge\frac1{C_A}\sum_{q\in I_m(A)}(K-q+1)\\
&=\left(
\frac{\xi_A}{2C_A}
\left(A-\frac{3\xi_A}{4}\right)+o_A(1)
\right)m.
\end{aligned}
\]

Equation (5.13) follows from (5.9). Finally (5.12), applied contrapositively
at every fixed positive \(\alpha\), gives (5.14). \(\square\)

## 6. Localized literal cyclic high-slot cuts

For an oriented row \(\rho\), let \(I_\rho(j,s)\) be its cyclic interval
of \(s\) consecutive coordinates starting at phase \(j\). For a nonempty
\(t\)-set \(T\), put

\[
h_s^\rho(T)=\#\{j:T\subseteq I_\rho(j,s)\}.
\]

### Lemma 6.1 (exact row-span truncation)

If \(1\le t\le m-q\), then

\[
\boxed{h_{m-q}^\rho(T)=(h_m^\rho(T)-q)_+.}
\tag{6.1}
\]

Moreover

\[
0\le h_m^\rho(T)\le L:=m-t+1.
\tag{6.2}
\]

#### Proof

Let \(d_1,\ldots,d_t\) be the clockwise gaps between consecutive points
of \(T\), so \(\sum_i d_i=n\), and put \(D=\max_i d_i\) and
\(\ell=n-D+1\). A cyclic \(s\)-interval contains \(T\) exactly when its
complementary \((n-s)\)-interval lies inside one of these empty gaps.
Thus

\[
h_s^\rho(T)=\sum_i(d_i-(n-s))_+.
\]

Since \(s\le m<n/2\), at most one summand is positive, giving

\[
h_s^\rho(T)=(s-\ell+1)_+.
\]

Taking \(s=m\) and \(s=m-q\) proves (6.1). The shortest linear span of
\(t\) distinct points has length at least \(t\), proving (6.2).
\(\square\)

For an exact middle factor, every middle set containing \(T\) occurs in
exactly one row, so

\[
\sum_{\rho}h_m^\rho(T)
=G_t:=\binom{n-t}{m-t}.
\tag{6.3}
\]

Write the Euclidean division

\[
G_t=aL+b,qquad 0\le b<L.
\tag{6.4}
\]

### Lemma 6.2 (exact numerical cyclic star cap)

For every exact endpoint factor,

\[
\boxed{
\sum_\rho h_{m-q}^\rho(T)
\le M_{q,t}^{\rm cyc}:=a(L-q)+(b-q)_+.}
\tag{6.5}
\]

This is the exact maximum over all integer \(B\)-tuples
\(0\le x_\rho\le L\) with \(\sum x_\rho=G_t\). Here \(G_t\le BL\), so
\(a\le B\), and \(a=B\) forces \(b=0\). It is not asserted that every
maximizing tuple is realized by an exact factor.

#### Proof

By Lemma 6.1 the left side is \(\sum_\rho(x_\rho-q)_+\), where
\(x_\rho=h_m^\rho(T)\). Concentrating mass into as few positive entries
as the cap \(L\) permits can only increase this convex piecewise-linear
sum. Explicitly, if \(0<x\le y<L\), moving
\(\min\{x,L-y\}\) units from \(x\) to \(y\) does not decrease
\((x-q)_++(y-q)_+\). Iteration leaves at most one nonzero entry below
\(L\). Thus a maximum has \(a\) entries equal to \(L\), one entry equal to
\(b\) when \(b>0\), and all others zero, which gives (6.5). \(\square\)

Now return to an arbitrary target family \(\mathcal U\subseteq V_q\).
Let \(M(\mathcal U)\) be any valid upper bound on the total number of
endpoint occurrences in \(\mathcal U\), and put

\[
\kappa(\mathcal U)=M(\mathcal U)-c_q|\mathcal U|.
\tag{6.6}
\]

For the old factor define

\[
U_q^F(\mathcal U)
=\sum_{S\in\mathcal U}(\mu_q^F(S)-c_q-1)_+,
\]

\[
P_q^F(\mathcal U)
=\#\{S\in\mathcal U:\mu_q^F(S)\ge c_q+1\}.
\tag{6.7}
\]

### Theorem 6.3 (excess-plus-high-slot release cut)

If a balanced endpoint with occurrence cap \(M(\mathcal U)\) exists, then
\(\kappa(\mathcal U)\ge0\), and the number

\[
e_q(\mathcal U)
=\#\{X\in\mathcal R_q:L_q^F(X)\in\mathcal U\}
\]

of released old occurrences in \(\mathcal U\) satisfies

\[
\boxed{
e_q(\mathcal U)
\ge U_q^F(\mathcal U)
+\bigl(P_q^F(\mathcal U)-\kappa(\mathcal U)\bigr)_+.}
\tag{6.8}
\]

#### Proof

At a cell \(S\), upper safety forces at least
\((\mu_q^F(S)-c_q-1)_+\) old occurrences to be released. If
\(\mu_q^F(S)\ge c_q+1\) and exactly this mandatory number is released,
the frozen load remains \(c_q+1\), so that cell is necessarily an endpoint
high cell. Every further release can desaturate at most one such cell.
Thus, after \(U_q^F(\mathcal U)\) mandatory releases, at least

\[
P_q^F(\mathcal U)
-\bigl(e_q(\mathcal U)-U_q^F(\mathcal U)\bigr)
\]

members of \(\mathcal U\) remain forced high. But a balanced endpoint has
at most \(M(\mathcal U)-c_q|\mathcal U|=\kappa(\mathcal U)\) high cells
there. Rearrangement proves (6.8). \(\square\)

For the full \(t\)-star, still assuming \(1\le t\le m-q\),

\[
\mathcal U_q(T)=\{S\in V_q:T\subseteq S\},
\qquad
N_{q,t}=|\mathcal U_q(T)|=\binom{n-t}{m-q-t},
\tag{6.9}
\]

the owner containment cap is \(G_t\), while Lemma 6.2 gives the stronger
literal-row cap \(M_{q,t}^{\rm cyc}\). Their exact difference is

\[
\boxed{
G_t-M_{q,t}^{\rm cyc}=aq+\min\{b,q\}.}
\tag{6.10}
\]

Define

\[
\kappa_{q,t}^{\rm cyc}
=M_{q,t}^{\rm cyc}-c_qN_{q,t},
\tag{6.11}
\]

\[
U_{q,T}=\sum_{S\supseteq T}(\mu_q^F(S)-c_q-1)_+,
\qquad
P_{q,T}=\#\{S\supseteq T:\mu_q^F(S)\ge c_q+1\},
\tag{6.12}
\]

and

\[
\delta_{q,T}^{\rm cyc}
=U_{q,T}
+(P_{q,T}-\kappa_{q,t}^{\rm cyc})_+.
\tag{6.13}
\]

Every literal balanced endpoint therefore satisfies

\[
\boxed{
|\mathcal R_q\cap\mathcal G(T)|
\ge\delta_{q,T}^{\rm cyc},
\qquad
\mathcal G(T)=\{X\in\tbinom{[n]}m:T\subseteq X\}.}
\tag{6.14}
\]

Indeed, (6.8) counts released owners whose old depth-\(q\) cell contains
\(T\); their middle root also contains \(T\). Formula (6.10) follows
immediately from \(G_t=aL+b\) and (6.5). A negative value of
\(\kappa_{q,t}^{\rm cyc}\) itself certifies that no balanced literal
endpoint exists.

The localized constraints admit the following valid fractional packing
dual. Completeness for the full row-state ILP is not asserted.

### Theorem 6.4 (multilevel localized-release dual)

Let tests be indexed by \(i\), with a depth \(q_i\), an owner family
\(\Gamma_i\), and a proved demand

\[
|\mathcal R_{q_i}\cap\Gamma_i|\ge\delta_i.
\]

If weights \(\lambda_i\ge0\) satisfy, for every owner \(X\) and every
\(d\in\{0,\ldots,K\}\),

\[
\sum_{i:q_i>d,\ X\in\Gamma_i}\lambda_i
\le H_{d+1},
\tag{6.15}
\]

then

\[
\boxed{\mathcal C\ge\sum_i\lambda_i\delta_i.}
\tag{6.16}
\]

#### Proof

Multiply the demand inequalities by \(\lambda_i\) and sum. An owner with
stopping depth \(a(X)\) appears precisely in tests with
\(q_i>a(X)\). Its total dual charge is at most \(H_{a(X)+1}\) by
(6.15). Summing over owners proves (6.16). \(\square\)

For a simpler integral consequence, let \(T_1,\ldots,T_p\) be pairwise
disjoint \(t\)-sets with \(2t\le m\), let \(q_i\le Q\), and let
\(\delta_i=\delta_{q_i,T_i}^{\rm cyc}\). Bonferroni and (6.14) give

\[
\boxed{
R_Q\ge
\left(
\sum_{i=1}^p\delta_i-\binom p2G_{2t}
\right)_+,
\qquad
G_{2t}=\binom{n-2t}{m-2t},}
\tag{6.17}
\]

and hence

\[
\boxed{
\mathcal C\ge H_Q
\left(
\sum_{i=1}^p\delta_i-\binom p2G_{2t}
\right)_+.}
\tag{6.18}
\]

### Corollary 6.5 (critical logarithmic-star criterion)

Let \(t=\lfloor\log_2n\rfloor\). For each
\(q\in I_m(A)\), choose a different \(t\)-set \(T_q\), with all the
\(T_q\) pairwise disjoint. If, for some fixed \(\eta>0\),

\[
\delta_{q,T_q}^{\rm cyc}\ge\eta B
\qquad(q\in I_m(A)),
\tag{6.19}
\]

then every literal balanced endpoint has

\[
\boxed{
\liminf_{m\to\infty}\frac{\mathcal C}{W}
\ge
\frac{\eta\xi_A(A-\xi_A)}{4C_A}.}
\tag{6.20}
\]

#### Proof

There are \((\xi_A/2+o_A(1))\sqrt m\) tests and their total coordinate
support is \(O_A(\sqrt m\log m)=o(n)\), so the disjoint choice is
possible. Since each factor in

\[
\frac{G_{2t}}B
=n\prod_{i=0}^{2t-1}\frac{m-i}{n-i}
\]

is smaller than \(1/2\), and \(2^t>n/2\),

\[
G_{2t}<\frac{4B}{n}.
\]

Thus the overlap term in (6.18) is \(O_A(B)\), whereas the main demand
is

\[
\left(\frac{\eta\xi_A}{2}+o_A(1)\right)B\sqrt m.
\]

Take \(Q=\lfloor\xi_A\sqrt m\rfloor\) and use
\(H_Q\ge((A-\xi_A)/C_A+o_A(1))\sqrt m\). Division by
\(W=(2m+1)B\) proves (6.20). \(\square\)

Condition (6.19) is not proved for every exact factor. Exact individual
middle-star counts and the row-span identity alone have a zero lower
envelope at logarithmic \(t\) for \(q\ge2\); known mixed-star constraints
are subcritical. Thus Corollary 6.5 is an explicit conditional literal cut,
not a universal counterexample.

## 7. A closed exact-factor basin

For \(m\ge3\), the following independently audited input concerns the
canonical MSW exact factor \(F_m^{\rm MSW}\). Let

\[
J_m=(2m-3)\operatorname{Cat}_{m-2},
\qquad
\rho_1=\frac{2W}{m+2}.
\tag{7.1}
\]

Its number \(M_1\) of empty first-shadow cells satisfies

\[
\boxed{M_1(F_m^{\rm MSW})\ge J_m-\rho_1.}
\tag{7.2}
\]

More generally, if an exact factor \(F'\) has row distance

\[
b=\frac12|F'\triangle F_m^{\rm MSW}|,
\]

then

\[
\boxed{
M_1(F')\ge[J_m-(m-1)b-\rho_1]_+.}
\tag{7.3}
\]

For completeness, the certificate count behind this input is exact. Insert
either \(1100\) or \(1010\) into any of the \(2m-3\) gaps of a Dyck word
of semilength \(m-2\). The two resulting MSW rows have one common pointed
first shadow; the pointed slots are disjoint across the
\(J_m\) certificates. Hence

\[
J_m\le\sum_S\left\lfloor\frac{\mu_1(S)}2\right\rfloor
\le\sum_S(\mu_1(S)-1)_+.
\]

Since \(c_1=1\), total mass \(W\), and
\(N_1=W-\rho_1\), the last sum is \(\rho_1+M_1\), proving (7.2).
One canonical row occurs in at most \(m-1\) certificate pairs, so deleting
\(b\) rows proves (7.3). The contextual insertion identity and this
maximum certificate degree were independently audited in
`MATH_ATTACK_I_MARKED_GAP_COLLISION_INDEPENDENT_AUDIT_20260725.md`.

### Theorem 7.1 (permanent-cost exclusion of the canonical basin)

For every balanced permanent-prefix endpoint, Boolean or literal,

\[
\boxed{
\mathcal C(F',G,a)
\ge H_1[J_m-(m-1)b-\rho_1]_+.}
\tag{7.4}
\]

In particular,

\[
\boxed{
\mathcal C(F_m^{\rm MSW},G,a)
\ge
\left(\frac{A}{16C_A}+o_A(1)\right)W\sqrt m.}
\tag{7.5}
\]

For every fixed \(0<\varepsilon<1/8\), uniformly over factors satisfying

\[
b\le(1/8-\varepsilon)B,
\]

one has

\[
\boxed{
\mathcal C(F',G,a)
\ge
\left(\frac{A\varepsilon}{2C_A}+o_A(1)\right)W\sqrt m.}
\tag{7.6}
\]

#### Proof

At depth one, every hole is one lower token, and all such tokens are
pairwise incomparable. Theorem 5.2 with this antichain gives
\(\mathcal C\ge H_1M_1(F')\), proving (7.4). Also

\[
\frac{J_m}{W}
=\frac{m(m+1)}{4(2m-1)(2m+1)}
\longrightarrow\frac1{16},
\qquad
\frac{\rho_1}{W}\longrightarrow0,
\tag{7.7}
\]

and \(H_1\ge K/C_A=(A/C_A+o_A(1))\sqrt m\), proving (7.5).
Finally, if \(b\le(1/8-\varepsilon)B\), then

\[
J_m-(m-1)b-\rho_1
\ge(\varepsilon/2+o(1))W,
\]

which proves (7.6). \(\square\)

This closes the canonical MSW factor and its fixed positive row-distance
basin for permanent prefix freezing. It says nothing about factors beyond
that basin, and it is not a lower bound for repair models in which an
owner may leave and later rejoin its old flag.

## 8. Precise proved and conditional boundary

The singular boundary has not been solved positively: this report does
not construct a low-cost balanced literal endpoint factor. Nor does it
prove that no such factor exists for every possible starting exact factor.
The exact advance is the following separation.

### Unconditional statements proved here

1. At one rank, every mobile containment Hoffman cut is represented by the
   rank-\(\rho_q\) shadow-quota matroid (Theorem 2.2). Containment
   integrality is therefore not the missing gate.
2. Some point-regular quota can be imposed with at most
   \(n\sqrt{d_q}/2\) unmatched owners, whose total through every fixed
   Gaussian window is \(o(W/\sqrt m)\) (Theorem 3.3). Zero leave is not a
   consequence of symmetry or transversality, and alignment to a
   prescribed old histogram can still be costly.
3. In the coprime regime there is a simultaneous integral, balanced,
   point-regular nested Boolean resolution (Theorem 3.4). It is not a
   literal row factor; for prime \(n\equiv3\pmod4\), \(n\ge7\), full coordinate-cycle
   equivariance of an exact factor is arithmetically impossible (Theorem
   3.5).
4. Literal endpoints must solve the exact positive support equation, the
   regular shadow-matroid base problem, and componentwise zero-margin cycle
   laws (Section 4).
5. Every \(o(W)\)-cost permanent-prefix solution must condense both signs
   of all cross-depth violation tokens into \(o(B\sqrt m)\) chains in the
   fixed Gaussian band (Section 5).
6. Literal rows obey the exact excess-plus-cyclic-high-slot cuts and their
   multilevel packing dual (Section 6).
7. The canonical MSW basin has cost \(\Omega_{A,\varepsilon}(W\sqrt m)\),
   so it cannot contain the desired singular solution (Section 7).

### Conditional statements only

- A critical violation antichain, an \(\Omega(B\sqrt m)\)-mass
  bounded-comparability token family, or
  regular-and-Hall distance of order \(W/\sqrt m\) yields an explicit
  \(\Omega_A(W)\) obstruction, but no such defect is proved for every exact
  factor.
- Logarithmic cyclic stars with
  \(\delta_{q,T_q}^{\rm cyc}\ge\eta B\) across the Gaussian band yield the
  constant in (6.20), but existence of those defects is not universal.
- The one-rank small leaves are not proved alignable into nested paths, and
  the coprime quotient paths are not proved packageable into exact wreath
  rows or close to any prescribed factor.

Therefore the remaining low-cost singular gate is exact and threefold:
choose point-regular shadow-matroid bases with negligible regular-and-Hall
distance, correlate them across depths so both violation-token posets have
small chain covers while all upper capacities hold, and realize the
resulting owner paths as literal cyclic rows without violating the
localized high-slot cuts. A theorem accomplishing those three operations,
or a universal exact-factor violation of one of the displayed necessary
conditions, is still unproved. No constant-one conclusion follows from
this report.
