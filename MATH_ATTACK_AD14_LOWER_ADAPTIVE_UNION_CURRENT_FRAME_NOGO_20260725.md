# AD14: a current-endpoint no-go for the certified lower adaptive union

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or
long-running job is used.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
t=\operatorname{Cat}_m=\frac Wn,\qquad
H=\lceil L\sqrt m\rceil
\]

for fixed \(L>0\). Fix the ordered pair partition used by the lower
long-interval charts, and denote its unpaired coordinate by \(\star\).

Consider the certified state-adaptive lower menu consisting of:

1. arbitrary successive disjoint adjacent-priority long-interval layers
   from AD12, all of whose coordinate exchanges fix \(\star\); and
2. owner-fixed lower spikes from AD13, charged occurrence by occurrence
   under the audited \(2s\)-run ledger.

There is no universal current-endpoint coercive frame for this menu with
\(s=o(W/H)\) charged spike occurrences. More precisely, there are literal,
lower-saturating and owner-simple token systems \(M_m\) for which the
depth-three doubled floor energy satisfies

\[
\mathcal Q_3^-(M_m)=(1+o(1))W,
\tag{0.1}
\]

but every state obtainable using arbitrary long-layer moves and at most
\(s=o(W/H)\) distinct owner-fixed spike occurrences obeys

\[
\mathcal Q_3^-(M')
\ge \mathcal Q_3^-(M_m)-o(Ht).
\tag{0.2}
\]

Consequently, for no fixed \(\eta_L>0,C_L<\infty\) can one have

\[
\mathcal Q_3^-(M)-
\mathbb E\mathcal Q_3^-(M')
\ge
\eta_L\bigl(\mathcal Q_3^-(M)-C_LHt\bigr)
\tag{0.3}
\]

for every current token system \(M\), when \(M'\) is required to come from
this certified union with \(s=o(W/H)\). The same conclusion holds with an
optimal deterministic corner in place of the expectation.

This is a rankwise statement, equivalently a weighted lower-sector
statement for the admissible nonnegative weight vector supported at
\(q=3\). It therefore refutes any charged-frame assertion claimed
uniformly over the depth weights. It does not by itself refute a theorem
for one separately fixed weight vector having unavoidable mass on other
depths.

The obstruction is an exact coordinate-subtotal wall. Long layers preserve
the \(\star\)-subtotal. One activated spike occurrence changes it by at
most one. The current profile below has zero mass on every depth-three
target containing \(\star\), while remaining uniformly bounded on the
other half of the layer.

This is a same-current-state and same-charged-occurrence-quantifier no-go.
Its scope is important: the constructed current token system uses
singleton labelled row pieces. Thus it does not refute a theorem whose
hypotheses already require the current state itself to have
\(o(W/H)\) runs. Nor does it refute a new packetization theorem which
places \(\Theta(W)\) occurrence-specific spike conjugacies into
\(o(W/H)\) final runs; AD13 proves no such packetization.

There is also a sharp predecessor-graph obstruction. At every depth
\(q\ge3\), central saturation permits a physical token system in which
all rank-\((m-q)\) targets containing one fixed coordinate pair are
isolated vertices of the full AD13 predecessor graph. This strengthens
the one-isolated-target example to a positive-density isolated family.

For the autonomous selected-token ledger of the canonical PBBS seed,
however, the unpaired-coordinate wall can be made cheap. A joint choice
of the unpaired coordinate and the ordered pair matching gives,
simultaneously at every \(q\le H\), point-subtotal error \(O_L(Ht)\) and
the existing \(O(W\log ^2m/m)\) phase-component ledger. This statement
does not count additional literal windows created by endpoint collars.
The exact unresolved nullspace is therefore the span of the other
predecessor-component indicators, together with the endpoint-orientation
term in the heat identity.

## 1. The depth-three wall

Set

\[
r=m-3,\qquad
\Omega=\binom{[n]}r,
\]

and split

\[
\mathcal A=\{S\in\Omega:\star\in S\},
\qquad
\mathcal C=\Omega\setminus\mathcal A.
\tag{1.1}
\]

Write

\[
A=|\mathcal A|=\binom{2m}{m-4},
\qquad
C=|\mathcal C|=\binom{2m}{m-3}.
\tag{1.2}
\]

The global depth-three load ratio is

\[
\lambda_3
=\frac{W}{\binom{2m+1}{m-3}}
=\frac{(m+2)(m+3)(m+4)}
       {m(m-1)(m-2)}
=1+O(m^{-1}).
\tag{1.3}
\]

Hence \(c_3=\lfloor\lambda_3\rfloor=1\) for all sufficiently large
\(m\). The doubled floor polynomial is therefore

\[
Q_3(\mu)
=\sum_{S\in\Omega}(\mu(S)-1)(\mu(S)-2).
\tag{1.4}
\]

Also

\[
\frac AC=\frac{m-3}{m+4},
\qquad
\frac WC
=\frac{(2m+1)(m+2)(m+3)}
       {m(m-1)(m-2)}
=2+O(m^{-1}),
\tag{1.5}
\]

so

\[
2A=(1+o(1))W.
\tag{1.6}
\]

## 2. A bounded integral central token system supported on
\(\mathcal C\)

Let

\[
\mathcal R=\binom{[n]}{m-1},
\qquad
T=|\mathcal R|.
\]

Join a root \(R\in\mathcal R\) to a target
\(S\in\mathcal C\) when \(S\subset R\).

### Lemma 2.1

For all sufficiently large \(m\), there is an integral assignment

\[
R\longmapsto S(R)\in\mathcal C,\qquad S(R)\subset R,
\tag{2.1}
\]

whose target loads all belong to \(\{2,3\}\).

#### Proof

The subgroup \(S_{[n]\setminus\{\star\}}\) is transitive on
\(\mathcal C\) and separately transitive on the roots containing
\(\star\) and those avoiding it. Give each root one unit and split that
unit uniformly among its neighbors. The inflow is constant on
\(\mathcal C\), hence equals \(T/C\). Direct calculation gives

\[
\frac TC
=\frac{(2m+1)(m+3)}{(m-1)(m-2)}
=2+O(m^{-1}),
\tag{2.2}
\]

and it lies strictly between \(2\) and \(3\) for all sufficiently large
\(m\).

Use a bipartite flow network with unit source capacity at every root and
target-to-sink bounds \([2,3]\). The uniform fractional flow is feasible.
All capacities are integral and the node-arc incidence matrix is totally
unimodular, so an integral flow exists. \(\square\)

Match all roots injectively to rank-\(m\) owners containing them. Hall's
condition follows directly by edge counting: a root has \(m+2\) owner
neighbors and an owner has \(m\) root facets, so for every root family
\(\mathcal X\),

\[
(m+2)|\mathcal X|\le m|N(\mathcal X)|.
\tag{2.3}
\]

Let \(d=W-T=2W/(m+2)\) be the number of unused owners.

### Lemma 2.2

The \(d\) unused owners can each be assigned a contained target in
\(\mathcal C\) so that no target receives more than three completion
occurrences.

#### Proof

Let \(\mathcal U\) be any family of unused owners and split it according
as \(\star\) is absent or present. After deleting \(\star\) from the
second class, these are families in
\(\binom{[2m]}m\) and \(\binom{[2m]}{m-1}\), respectively.

The normalized matching property of the Boolean lattice gives, for
\(k\in\{m-1,m\}\),

\[
\frac{|\partial_r\mathcal F|}{\binom{2m}r}
\ge
\frac{|\mathcal F|}{\binom{2m}k}.
\tag{2.4}
\]

Put

\[
\rho_m=
\min\left\{
\frac{\binom{2m}r}{\binom{2m}m},
\frac{\binom{2m}r}{\binom{2m}{m-1}}
\right\}.
\]

Then \(\rho_m\to1\). If the two owner classes in \(\mathcal U\) have
sizes \(u_0,u_1\), their union of available targets has size at least

\[
\max\{\rho_mu_0,\rho_mu_1\}
\ge\frac{\rho_m}{2}(u_0+u_1).
\]

For large \(m\), this is at least \(|\mathcal U|/3\). Capacitated Hall,
with capacity three at each target, proves the assertion. \(\square\)

For every matched root-owner edge, order the two deletions from \(R\) so
that its depth-three lower flag is \(S(R)\). Complete every unused owner
by an isolated nested flag having its assigned target at depth three.
Every depth-three target avoids \(\star\).

These flags are literal. For each prescribed incident pair and deletion
order, choose an omitted pair outside the owner and relabel one row of an
exact local factor so that the row supplies that central incidence and
the two prescribed deletions. Treating the rows as labelled singleton
pieces gives one integral, lower-saturating, owner-simple token system.
This is the same literal realization used in the physical part of AD13.

Let \(\mu^0\) be its completed depth-three load. Before completion, every
load on \(\mathcal C\) is \(2\) or \(3\). After Lemma 2.2,

\[
\mu^0(S)\le6\quad(S\in\mathcal C),
\qquad
\mu^0(S)=0\quad(S\in\mathcal A).
\tag{2.5}
\]

If

\[
e=T-2C,
\tag{2.6}
\]

then exactly \(e=O(W/m)\) principal targets have load three. A completion
unit added to a load at most five raises (1.4) by at most eight. Therefore

\[
\boxed{
2A\le Q_3(\mu^0)
\le2A+2e+8d
=2A+O(W/m).}
\tag{2.7}
\]

Together with (1.6), this proves (0.1).

## 3. What the adaptive union can change

Every adjacent pair exchange in AD12 fixes \(\star\). Therefore every
token innovation in every disjoint long-interval layer preserves the
subtotal

\[
M_{\mathcal A}(\mu)=\sum_{S\in\mathcal A}\mu(S).
\tag{3.1}
\]

This remains true under arbitrary packet choices, arbitrary disjoint
layers, and arbitrary successive recomputation using the same fixed pair
partition.

An owner-fixed spike changes the flag carried by one owner occurrence.
No matter how many legal spike transpositions are composed on that same
occurrence, its contribution to (3.1) changes by at most one. Hence if
\(s\) distinct occurrences are activated, every resulting profile
\(\mu'\) obeys

\[
M_{\mathcal A}(\mu')\le s,
\tag{3.2}
\]

because \(M_{\mathcal A}(\mu^0)=0\).

For an integer \(x\ge0\),

\[
(x-1)(x-2)=x^2-3x+2\ge2-3x.
\]

Consequently

\[
\boxed{
Q_3(\mu')
\ge2A-3M_{\mathcal A}(\mu')
\ge2A-3s.}
\tag{3.3}
\]

Combining (2.7) and (3.3) gives the exact current-endpoint bound

\[
\boxed{
Q_3(\mu^0)-Q_3(\mu')
\le2e+8d+3s.}
\tag{3.4}
\]

At \(H=\lceil L\sqrt m\rceil\),

\[
Ht=\left(\frac L2+o(1)\right)\frac W{\sqrt m},
\qquad
\frac WH=\Theta_L(Ht).
\tag{3.5}
\]

Thus \(e,d=O(W/m)=o(Ht)\), and \(s=o(W/H)\) implies

\[
\sup_{\mu'}\bigl(Q_3(\mu^0)-Q_3(\mu')\bigr)=o(Ht).
\tag{3.6}
\]

Since \(Q_3(\mu^0)=(1+o(1))W\), equations (3.5)--(3.6) prove the no-go
(0.3).

The argument grants the long layers every algebraically possible corner
and grants arbitrary adaptive compositions of spikes on each activated
occurrence. It uses only the two exact facts that the long generators fix
\(\star\), and that one occurrence carries one unit of rank-three mass.

## 4. Endpoint imbalance is the whole loss

For one chart with current coherent endpoint \(f^0\), opposite coherent
endpoint \(f^1\), coherent displacement \(A\), and independent-component
variance \(V\), the exact doubled-floor Haar identity is

\[
\mathbb E Q(f^\varepsilon)
=\frac{Q(f^0)+Q(f^1)}2-\frac{A-V}{4}.
\tag{4.1}
\]

Therefore the descent from the current endpoint is

\[
\boxed{
Q(f^0)-\mathbb E Q(f^\varepsilon)
=\frac{Q(f^0)-Q(f^1)}2+\frac{A-V}{4}.}
\tag{4.2}
\]

Positive cross-Gram controls only the second term. In the construction
above, both coherent long-layer endpoints remain in the same
\(\star\)-subtotal wall. Spike endpoints leave that wall by at most one
unit per activated occurrence. Equation (3.4) shows that the first term
in (4.2) cancels all but \(o(Ht)\) of any apparent frame curvature.

Thus a theorem relative to the higher of two coherent endpoints is not a
current-state theorem. The missing orientation term is not a technical
floor error; on this family it is the dominant term of order \(W\).

## 5. A positive-density predecessor-graph disconnection

The isolated-target construction in AD13 can be amplified.

### Theorem 5.1

Fix \(q\ge3\), put \(r=m-q\), and fix a two-set
\(D=\{u,v\}\). There is a lower-saturating, owner-simple literal token
system for which every target

\[
Z\in\binom{[n]}r,\qquad D\subset Z,
\tag{5.1}
\]

is an isolated vertex of the full predecessor graph
\(\widehat\Gamma_q^-\). In particular, the number of isolated vertices is

\[
\boxed{\binom{n-2}{r-2}=\Theta_L(W)}
\tag{5.2}
\]

uniformly for \(q\le L\sqrt m\).

#### Proof

For every rank-\((m-1)\) root \(R\supset D\), choose its depth-\(q\)
flag \(F(R)\) inside \(R\setminus D\). This is possible because

\[
|R\setminus D|=m-3\ge m-q=r.
\]

For roots not containing \(D\), choose any \(r\)-subset. Order the
\(q-1\) deletions from each root so that the prescribed flag is last.
As in AD13, first match all roots injectively to containing owners, then
realize every prescribed token by a relabelled row of a labelled exact
local factor. This gives a physical lower-saturating, owner-simple token
system.

Every rank-\(r\) projection of every lower owner-fixed spike from the
token rooted at \(R\) is either zero or a Johnson edge from \(F(R)\) to
one of its distance-one neighbors inside \(R\). If such an edge were
incident with a target \(Z\supset D\), then \(R\supset Z\supset D\).
But for this root, \(F(R)\cap D=\varnothing\), whereas \(D\subset Z\).
Thus

\[
d_J(F(R),Z)\ge2,
\]

so no one-edge spike projection reaches \(Z\). Also \(F(R)\ne Z\).
Therefore \(Z\) is isolated.

Finally,

\[
\frac{\binom{n-2}{r-2}}{\binom nr}
=\frac{r(r-1)}{n(n-1)}
=\frac14+o_L(1),
\]

while \(\binom nr=\Theta_L(W)\) on the fixed Gaussian window. This
proves (5.2). \(\square\)

Theorem 5.1 is a one-menu obstruction. Adaptive repeated spikes on one
occurrence may compose several Johnson steps, so disconnectedness alone
is not a multistep invariant. The occurrence-capacity wall in Section 3
is the robust adaptive obstruction.

The construction in Theorem 5.1 uses singleton labelled rows. It proves
that central saturation and owner injectivity alone do not imply even
approximate predecessor expansion. A positive low-run theorem must use
the correlated-row hypothesis quantitatively.

## 6. Exact combined graph nullspace and component floor

Fix one lower depth \(q\ge2\), and let \(\Omega_q\) be its target layer.
Form the graph \(\mathcal G_q\) on \(\Omega_q\) whose edges are all
individual rank-\(q\) atomic moves available from:

1. the occurrence-level differences underlying the permitted long
   interval charts; and
2. all legal owner-fixed lower spike projections.

The PBBS \(q=1\) repair contributes no edge to \(\mathcal G_q\) when
\(q\ge2\). Packet columns are sums of the long occurrence edges; granting
the individual edges can only enlarge the physical span.

### Theorem 6.1 (exact residual nullspace)

If \(C\) runs through the connected components of \(\mathcal G_q\), then

\[
\boxed{
\operatorname{span}\{\delta_Y-\delta_X:XY\in E(\mathcal G_q)\}
=
\left\{
z:\sum_{X\in C}z_X=0\text{ for every component }C
\right\}.}
\tag{6.1}
\]

Consequently its orthogonal nullspace is

\[
\boxed{
\ker_{\rm frame}(\mathcal G_q)
=\operatorname{span}\{\mathbf1_C:C\in\operatorname{Comp}(\mathcal G_q)\}.}
\tag{6.2}
\]

The actual packetized catalog can have a larger nullspace, never a
smaller one.

#### Proof

Every edge incidence has zero sum on each component, proving one
inclusion in (6.1). In a connected component, the edge incidences of any
spanning tree generate every difference
\(\delta_X-\delta_{X_0}\), and these differences span its zero-sum
subspace. Components have disjoint supports. Orthogonal complementation
gives (6.2). \(\square\)

The integer floor retained by this nullspace is also exact. Suppose a
component \(C\) has size \(N_C\), invariant mass

\[
M_C=N_Ca_C+s_C,\qquad0\le s_C<N_C.
\]

For a global doubled-floor quotient \(c_q\), the minimum component
contribution is

\[
\boxed{
Q_{q,C}^{\min}
=
2\left[N_C\binom{a_C}{2}+s_Ca_C\right]
-2c_qM_C+c_q(c_q+1)N_C.}
\tag{6.3}
\]

Indeed, discrete convexity puts load \(a_C+1\) on \(s_C\) cells and
load \(a_C\) on the others; substituting into
\(Q_q=2\sum\binom{\mu}{2}-2c_qM+c_q(c_q+1)N\) gives (6.3).
Summing (6.3) is the exact residual floor wall of the combined formal
menu.

Theorem 5.1 supplies components of size one for a positive-density
family. Conversely, connectivity of every \(\mathcal G_q\) would remove
the component-total nullspace but would still not prove a charged frame:
packet correlation, current-endpoint orientation, and the number of
activated occurrence rows remain quantitative constraints.

## 7. The PBBS selected-token ledger makes the coordinate wall cheap

The counterexample in Sections 1--3 is uniform over all literal central
token systems. It is not an endpoint obstruction for the autonomous
selected-token ledger of the canonical PBBS seed. In fact the unpaired
coordinate and the ordered pair partition can
be chosen so that its entire deeper point-subtotal error is
\(O_L(Ht)\), while retaining the already proved low-component ledger.

The elementary departure bound alone does not show this. On uncut
transition cycles, if \(\chi_x\) is the number of selected departures of
\(x\), then

\[
0\le M_{1,x}-M_{q,x}\le(q-1)\chi_x
\tag{7.1}
\]

apart from exceptional released or completion occurrences. Even choosing
a coordinate whose one-factor departure count is \(O(W/m)\), crude
replication through the \(O(\log m)\) processed phases leaves an unwanted
factor \(\log m\) after (7.1). Moreover the full phase predicates are nested;
only the adjacent-carrier predicates with the additional condition
\(S\cap P_{j+1}=\varnothing\) are disjoint. The following joint choice of
the unpaired coordinate and the ordered matching removes that loss.

Put

\[
A_0=\binom{2m-1}{m-1},\qquad
\ell_0=\lceil20\log m\rceil.
\]

Fix the first omitted pair \(P_1\), put
\(Q_1=[n]\setminus P_1\), and orient every cycle of one PBBS transition
factor \(\mathcal D_1\) on \(Q_1\). Write its successive states as
\(X_i,X_{i+1}\) and its lower label as

\[
S_i=X_i\cap X_{i+1}.
\]

There are \(A_0\) principal starts. Once nested physical flags have been
chosen, put

\[
R_i=S_i\setminus L_{i,H}.
\tag{7.2}
\]

This includes starts next to physical cuts: it uses the actual supplied
nested flag rather than the uncut cyclic continuation. Since
\(|S_i|=m-1\) and \(|L_{i,H}|=m-H\),

\[
|R_i|=H-1,qquad
\sum_i|R_i|=(H-1)A_0.
\tag{7.3}
\]

Let \(f(x)\) denote the lower-label flip count used in the PBBS
component proof. Thus

\[
\sum_{x\in Q_1}f(x)=2A_0.
\tag{7.4}
\]

### Theorem 7.1 (simultaneous PBBS coordinate and component choice)

There are a coordinate \(\star\in Q_1\) and an ordered perfect matching

\[
Q_1\setminus\{\star\}=P_2\sqcup\cdots\sqcup P_m
\tag{7.5}
\]

such that the following two assertions hold.

First, among all principal first-avoided PBBS copies in phases
\(1\le j\le\ell_0\),

\[
\boxed{
D^{\rm prin}_{H,\star}
:=M^{\rm prin}_{1,\star}-M^{\rm prin}_{H,\star}
\le {8HA_0\over2m-1}=O(Ht).}
\tag{7.6}
\]

Here the accounting is exact:

\[
t={2A_0\over m+1},\qquad
{8HA_0\over2m-1}
=4Ht\,{m+1\over2m-1}=(2+o(1))Ht.
\]

Second, if

\[
F_j=\sum_{x\in P_2\cup\cdots\cup P_{j+1}}f(x),
\]

then

\[
\boxed{
\sum_{j=1}^{\ell_0}F_j
\le {2A_0\ell_0(\ell_0+1)\over m-1}
=O(A_0\log ^2m/m).}
\tag{7.7}
\]

Consequently this choice gives exactly the same
\(O(A_0\log ^2m/m)\) category-component bound as the sorted-flip choice.
This is an algebraic PBBS phase-selection statement. Turning the selected
cycles into \(H\)-physical low-run pieces still requires the previously
isolated residence-cut hypothesis \((PR_H)\); Theorem 7.1 adds no new cut
requirement and survives any such transported cuts.

#### Proof

For all sufficiently large \(m\), so that \(\ell_0\le m-2\), choose
\(x\) uniformly from \(Q_1\), and conditional on \(x\), choose a uniform
random ordered perfect matching of \(Q_1\setminus\{x\}\).
For a base start \(i\) with \(x\in S_i\), let

\[
h_i=\#\{1\le j\le\ell_0:
S_i\cap P_k\ne\varnothing\text{ for every }2\le k\le j\}.
\tag{7.8}
\]

This is exactly the number of processed first-avoided phases in which the
pullback of start \(i\) is retained. The compatibility construction
transports the same actual flag by \(\phi_j\), and every \(\phi_j\) fixes
the unpaired coordinate \(x\). For the chosen outcome, the principal
depth-\(H\) loss is therefore exactly

\[
D^{\rm prin}_{H,x}
=\sum_i\mathbf1_{\{x\in R_i\}}h_i.
\tag{7.9}
\]

Fix a pair \((x,i)\) with \(x\in R_i\). Since
\(|Q_1\setminus S_i|=m\) and
\(x\in S_i\), the complement
\(B_i=Q_1\setminus S_i\) is an \(m\)-set inside the \(2m-2\) matched
coordinates. Conditional on the first \(k\) pairs meeting \(S_i\), those
pairs have consumed at most \(k\) points of \(B_i\). The next random pair
therefore lies wholly in \(B_i\) with conditional probability at least

\[
{\binom{m-k}{2}\over\binom{2m-2-2k}{2}}
={m-k\over2(2m-2k-3)}>{1\over4}.
\tag{7.11}
\]

Thus

\[
\Pr(h_i\ge k+1)\le(3/4)^k,
\qquad
\mathbb E(h_i\mid x)\le4.
\tag{7.12}
\]

Average (7.9) first over the ordered matching and then over uniform
\(x\in Q_1\). By (7.3) and (7.12),

\[
\mathbb E_{x,P}D^{\rm prin}_{H,x}
\le {4(H-1)A_0\over2m-1}.
\tag{7.13}
\]

On the other hand, conditional on \(x\), the first \(j\) matching pairs
are a uniform \(2j\)-subset of the remaining coordinates. Equations
(7.4) and linearity of expectation give

\[
\mathbb E_{x,P}\sum_{j=1}^{\ell_0}F_j
\le {A_0\ell_0(\ell_0+1)\over m-1}.
\tag{7.14}
\]

Normalize the two nonnegative random variables in (7.13)--(7.14) by
their displayed upper bounds. Their normalized sum has expectation at
most two. Some outcome has normalized sum at most two, and therefore
obeys both (7.6) and (7.7). The standard component proof bounds the sum
of the phase boundary counts by the cycle/cut terms plus
\(O(\sum_jF_j)\); hence (7.7) preserves that proof. \(\square\)

The theorem is stable under the usual autonomous PBBS exceptional ledger.
From this point through (7.20), \(M_q\) counts the completed family of
exactly \(W\) selected token occurrences; it does not count additional
literal windows created solely by initialization or terminal collars. Let
\(R_{\rm exc}\) be the total number of tail releases, optional
upper-colour deletions, and arithmetic completion occurrences. Combining
the PBBS two-sided \(q=1\) colour theorem with the arithmetic completion
ledger gives

\[
R_{\rm exc}=O(W\log m/m)=o(Ht)
\tag{7.15}
\]

when \(H=\lceil L\sqrt m\rceil\). Physical cuts supplied with their
standard collars do not delete principal \(q=1\) starts; their possibly
altered endpoint flags were already included through \(R_i\) in (7.2).
Each genuinely exceptional selected occurrence changes a fixed point
subtotal, or its \(q=1\)-to-\(q\) loss, by at most one. Since lower intersections shrink
with \(q\), Theorem 7.1 therefore gives, simultaneously for every
\(1\le q\le H\),

\[
0\le M_{1,\star}-M_{q,\star}=O_L(Ht).
\tag{7.16}
\]

Indeed,

\[
{W\log m/m\over Ht}
=O_L\!\left({\log m\over\sqrt m}\right)=o(1).
\]

Also the complete rank-\((m-1)\) layer has the uniform point count, so
the same exceptional ledger gives

\[
\varepsilon_{1,\star}
:=M_{1,\star}-{m-1\over n}W=o(Ht).
\tag{7.17}
\]

Explicitly, if \(B=\binom n{m-1}\), one copy of the complete layer has
point count \((m-1)B/n\). Its difference from
\((m-1)W/n\) is at most \(W-B=O(W/m)\), while changing
\(R_{\rm exc}\) occurrences changes a fixed point count by at most
\(R_{\rm exc}\). This proves (7.17).

Using \(t=W/n\), the exact identity

\[
M_{q,\star}-{m-q\over n}W
=\varepsilon_{1,\star}+(q-1)t
 -(M_{1,\star}-M_{q,\star})
\tag{7.18}
\]

now yields

\[
\boxed{
\max_{1\le q\le H}
\left|M_{q,\star}-{m-q\over n}W\right|
=O_L(Ht).}
\tag{7.19}
\]

There is no corresponding conclusion here for the ledger which counts
every extra collar-induced literal window. Its presently proved size is
only \(O(HJ_0)=o(W)\), which need not be \(O(Ht)\). Closing that stronger
literal-collar version requires an additional collar-discrepancy estimate.

This also makes the two-component floor associated with the
\(\star\)-cut cheap. Indeed, there is a globally floor-balanced integral
profile whose \(\star\)-subtotal differs from
\((m-q)W/n\) by at most one. Here is the exact integer argument. Write

\[
N=N_0+N_1=|\Omega_q|,\qquad W=c_qN+s,\quad0\le s<N,
\]

where \(N_1\) is the size of the \(\star\)-side. The possible numbers of
\((c_q+1)\)-loads on that side form the integer interval

\[
I=[\max(0,s-N_0),\min(s,N_1)]\cap\mathbb Z.
\]

The real number \(sN_1/N\) lies in the corresponding real interval, so
some \(y_0\in I\) differs from it by at most one. The resulting globally
floor-balanced profile has \(\star\)-subtotal
\(M_0=c_qN_1+y_0\) and

\[
\left|M_0-{N_1\over N}W\right|\le1,
\qquad {N_1\over N}={m-q\over n}.
\]

If the required subtotal differs from \(M_0\) by \(k\), transfer \(k\)
units across the cut using distinct vertices on both sides. Each receiving
load changes from \(c_q\) or \(c_q+1\) to its successor, and each donating
load to its predecessor. For the doubled floor polynomial
\((u-c_q)(u-c_q-1)\), the total cost of one such transfer is at most four.
By (7.19), \(k=O_L(Ht)=o(\min(N_0,N_1))\), so distinct vertices are
available. Therefore the constrained minimum is

\[
\boxed{Q^{\min}_{q,\star\text{-cut}}=O_L(Ht).}
\tag{7.20}
\]

Thus the canonical diffuse coordinate obstruction from Sections 1--3 is
absorbed by the allowed \(C_LHt\) baseline for a suitably labelled PBBS
seed. Precisely one linear functional has been controlled: the total mass
on targets containing the selected \(\star\). Owner-fixed spikes can cross
this cut, so its two sides need not even be components of the full combined
graph. If the actual components refine either side, (7.19) gives no bound
on their separate masses and their sum in (6.3) can still be macroscopic.
No analogue of the geometric first-omitted-pair estimate (7.11) is
presently known for an arbitrary predecessor-graph component.

## 8. Exact scope and next statement

The proved no-go applies to the current certified architecture:

* one fixed pair partition and any disjoint adjacent-priority long layers;
* owner-fixed spikes charged by the number of activated occurrences, using
  the audited \(O(s)\) run ledger;
* arbitrary state-adaptive ordering and arbitrary spike compositions on
  those occurrences; and
* a current-state coercive inequality uniform over literal
  lower-saturating, owner-simple token systems.

It does not rule out:

1. changing the leftover coordinate or the entire pair partition between
   adaptive stages;
2. a theorem restricted from the outset to current states already having
   \(o(W/H)\) row runs;
3. packetizing a linear number of occurrence-specific spike conjugacies
   into \(o(W/H)\) physical runs; or
4. a factor-specific theorem forcing expansion of
   \(\widehat\Gamma_q^-\) for low-run correlated states.

Theorem 7.1 closes the particular unpaired-coordinate mode for the
canonically relabelled PBBS seed. It does not close the exact component
nullspace of Theorem 6.1. To state the remaining assertion without hiding
that nullspace, define

\[
\mathfrak F_q(M)
=\sum_{C\in\operatorname{Comp}(\mathcal G_q(M))}
Q^{\min}_{q,C}(M_C),
\tag{8.1}
\]

with \(Q^{\min}_{q,C}\) given by (6.3). This is the exact floor energy
which no linear combination of the granted atomic moves can remove.

The next lower-sector theorem must prove, for the actual PBBS-reachable
low-run states, both a component-wall estimate

\[
\boxed{\mathfrak F_q(M)=O_L(Ht)\quad(2\le q\le H)}
\tag{8.2}
\]

(or its required weighted sum over \(q\)), and an endpoint-aware frame on
the component-mean-zero complement. In the notation of Section 4, the
latter has the exact form

\[
\boxed{
{\mathcal Q^-(M)-\mathcal Q^-(M^{\rm opp})\over2}
+{A_H(M)-V_H(M)\over4}
\ge
\eta_L\bigl(\mathcal Q^-(M)-\mathfrak F(M)-C_LHt\bigr),}
\tag{8.3}
\]

for some legal chart or disjoint layer costing \(o(W/H)\) added runs.
Equation (4.2) shows that (8.3), rather than a bare positive-Gram bound,
is exactly the current-endpoint statement.

What is now decided is sharp. Central legality and ownership do not imply
(8.2), by Theorem 5.1. PBBS relabelling and the low-component ledger do
imply the coordinate instance (7.20), by Theorem 7.1. They presently give
neither (8.2) for arbitrary components nor the oriented inequality (8.3).
Thus the residual lane is precisely a PBBS low-run predecessor-component
theorem together with the endpoint imbalance term; another point-subtotal
or \(q=1\) ledger estimate cannot finish it.
