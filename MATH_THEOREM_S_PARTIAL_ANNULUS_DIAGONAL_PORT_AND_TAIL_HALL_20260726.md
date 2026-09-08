# Partial-annulus SCD ports: exact diagonal equations and the outer-tail Hall cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\]

and fix

\[
 0<a<b,\qquad q_0=\lceil a\sqrt m\rceil,
 \qquad H=\lfloor b\sqrt m\rfloor.
\]

The SCD scaffold in
`MATH_THEOREM_S_PARTIAL_ANNULUS_SCD_SCAFFOLD_AND_TOP_TAG_CUT_20260726.md`
is correct: one full SCD supplies exactly \(N_{q_0}\) owner-simple
providers, its tag-\(q\) subfamily supplies every signed depth-\(q\) target
once, and a \(p\)-path radius-\(H\) rotor cover compiles at length
\(W+2Hp\). Its floor-corrected \(2m\)-cycle ledger is also correct.

There is, however, extra freedom which the fixed-collar scaffold does not
use. Since no target at a depth below \(q_0\) is required, the first
\(q_0\) deletion labels of a retained SCD chain may be permuted arbitrarily,
and independently so may its first \(q_0\) insertion labels. More
generally, its SCD annular flag may be rooted at any middle corner of its
depth-\(q_0\) Boolean interval. These changes preserve every designated
target at depths \(q_0,\ldots,H\).

This note proves the exact simultaneous-port equations for that relaxed
problem.  They have three consequences.

1. For a fixed SCD middle owner there are \((q_0!)^2\) annular-compatible
   inner collars, not one.  Allowing all middle corners gives
   \((2q_0)!\) ordered inner ports for one depth-\(q_0\) interval.
2. Every consecutive pair of provider intervals obeys an exact four-label
   boundary recurrence.  It gives a projected Hall obstruction before
   any full collar is chosen.
3. Inner reordering does not alter the fixed outer SCD tails.  Hence every
   top-to-top rotor edge \(C\to C'\) must satisfy
   
   \[
    \delta_j(C')=\delta_{j+1}(C),\qquad
    \eta_j(C')=\eta_{j+1}(C)
    \quad(q_0+1\le j\le H-1).
   \]
   The maximum linear-forest size in this outer-tail overlap graph may
   replace the fixed-collar top statistic in the narrow-annulus run cut.

The resulting theorem is an exact corrected gate, not a positive
construction.  No SCD is proved to have the required Hall expansion.

## 1. SCD providers and their annular data

Fix a full SCD \(\mathcal D\) of \(B_{2m}\). A chain \(C\) of radius
\(d\) has members

\[
 D_d(C)\subset\cdots\subset D_1(C)\subset D_0(C)=X(C)
 =E_0(C)\subset E_1(C)\subset\cdots\subset E_d(C),
\]

where \(|D_j|=m-j\) and \(|E_j|=m+j\).  Put

\[
 \delta_j(C)=D_{j-1}(C)\setminus D_j(C),\qquad
 \eta_j(C)=E_j(C)\setminus E_{j-1}(C).
\tag{1.1}
\]

Retain

\[
 \Omega=\{C\in\mathcal D:\rho(C)\ge q_0\}.
\tag{1.2}
\]

Then \(|\Omega|=N_{q_0}\). At each \(q_0\le q\le H\), the chains
of radius at least \(q\) biject by \(C\mapsto D_q(C)\) and
\(C\mapsto E_q(C)\) onto the two signed target layers. Thus it is enough
to realize the prescribed annular flags of these providers; the other
\(W-N_{q_0}\) middle masks may remain singleton repairs.

For \(C\in\Omega\), set

\[
 h(C)=\min\{\rho(C),H\},\qquad
 D(C)=D_{q_0}(C),\qquad E(C)=E_{q_0}(C),
\]

and

\[
 F(C)=E(C)\setminus D(C),\qquad |F(C)|=2q_0.
\tag{1.3}
\]

## 2. Exact annular-port normal form

Choose a middle root \(X\) for \(C\) satisfying

\[
 D(C)\subset X\subset E(C),\qquad |X|=m.
\tag{2.1}
\]

Put

\[
 A=X\setminus D(C),\qquad B=E(C)\setminus X.
\tag{2.2}
\]

Both have size \(q_0\). Choose arbitrary orderings

\[
 (a_1,\ldots,a_{q_0})\text{ of }A,
 \qquad
 (b_1,\ldots,b_{q_0})\text{ of }B.
\tag{2.3}
\]

For \(q_0<j\le h(C)\), extend these words by the forced labels

\[
 a_j=\delta_j(C),\qquad b_j=\eta_j(C).
\tag{2.4}
\]

If a complete radius-\(H\) collar is wanted and \(h(C)<H\), complete the
two words arbitrarily by distinct labels from \(D_{h(C)}(C)\) and from
the complement of \(E_{h(C)}(C)\), respectively. The number of such
ordered completions is

\[
 \bigl((m-h(C))_{H-h(C)}\bigr)^2>0.
\tag{2.5}
\]

For the original SCD root \(X=X(C)\), (2.3) gives exactly
\((q_0!)^2\) annular-compatible inner collars. If every middle corner in
(2.1) is allowed, the number of choices through (2.3) is

\[
 \binom{2q_0}{q_0}(q_0!)^2=(2q_0)!.
\tag{2.6}
\]

### Theorem 2.1 (exact diagonal annular-port equations)

Let \(X_t\) be a directed middle route, with

\[
 X_{t+1}=X_t-\alpha_t+\beta_t,
 \qquad \alpha_t\in X_t,\quad \beta_t\notin X_t.
\tag{2.7}
\]

Assign a provider \(C_t\in\Omega\) to root \(t\). Assume the route is
geodesic through every depth which is claimed.  Then the windows rooted at
\(t\) reproduce every prescribed SCD target

\[
 \bigcap_{i=0}^qX_{t+i}=D_q(C_t),\qquad
 \bigcup_{i=0}^qX_{t+i}=E_q(C_t)
 \quad(q_0\le q\le h(C_t))
\tag{2.8}
\]

if and only if all of the following hold:

\[
 D(C_t)\subset X_t\subset E(C_t),
\tag{2.9}
\]

\[
 \{\alpha_t,\ldots,\alpha_{t+q_0-1}\}
   =X_t\setminus D(C_t),
\tag{2.10-}
\]

\[
 \{\beta_t,\ldots,\beta_{t+q_0-1}\}
   =E(C_t)\setminus X_t,
\tag{2.10+}
\]

and, for every \(q_0<j\le h(C_t)\),

\[
 \alpha_{t+j-1}=\delta_j(C_t),\qquad
 \beta_{t+j-1}=\eta_j(C_t).
\tag{2.11}
\]

For a cycle the indices are cyclic.  For a path they apply at roots whose
required windows lie inside the route; the hard-start collar supplies the
endpoint windows.

#### Proof

On a geodesic route, the first \(q\) swaps delete distinct coordinates
\(\alpha_t,\ldots,\alpha_{t+q-1}\) from \(X_t\) and insert distinct
coordinates \(\beta_t,\ldots,\beta_{t+q-1}\). Therefore

\[
 \bigcap_{i=0}^qX_{t+i}
 =X_t\setminus\{\alpha_t,\ldots,\alpha_{t+q-1}\},
\tag{2.12-}
\]

\[
 \bigcup_{i=0}^qX_{t+i}
 =X_t\cup\{\beta_t,\ldots,\beta_{t+q-1}\}.
\tag{2.12+}
\]

At \(q=q_0\), equations (2.12) are equivalent to (2.9)--(2.10).
For \(q>q_0\), compare the equations at \(q-1\) and \(q\). The lower
target drops the unique label \(\delta_q(C_t)\), and the upper target gains
the unique label \(\eta_q(C_t)\).  This is exactly (2.11).  The same
comparison in reverse proves sufficiency. \(\square\)

The theorem is deliberately rooted.  It does not require the provider at
time \(t+1\) to carry the residual tail of the provider at time \(t\).
Such hereditary shift consistency is stronger than literal reproduction
of all rooted annular flags.

## 3. Boundary recurrence and a projected Hall obstruction

Suppose every root has a depth-\(q_0\) provider and abbreviate

\[
 D_t=D(C_t),\qquad E_t=E(C_t),\qquad F_t=E_t\setminus D_t.
\]

### Lemma 3.1 (four-label boundary recurrence)

Every consecutive pair in a route satisfying Theorem 2.1 obeys

\[
 \boxed{D_{t+1}=D_t-\alpha_{t+q_0}+\beta_t,}
\tag{3.1-}
\]

\[
 \boxed{E_{t+1}=E_t-\alpha_t+\beta_{t+q_0}.}
\tag{3.1+}
\]

Consequently

\[
 \boxed{
 F_{t+1}=F_t-\{\alpha_t,\beta_t\}
             +\{\alpha_{t+q_0},\beta_{t+q_0}\}.}
\tag{3.2}
\]

If the route is geodesic through \(q_0+1\), the four displayed labels are
distinct.  In particular

\[
 |D_t\triangle D_{t+1}|=|E_t\triangle E_{t+1}|=2,
 \qquad |F_t\triangle F_{t+1}|=4.
\tag{3.3}
\]

#### Proof

Let

\[
 A_t=\{\alpha_t,\ldots,\alpha_{t+q_0-1}\},\qquad
 B_t=\{\beta_t,\ldots,\beta_{t+q_0-1}\}.
\]

Then \(X_t=D_t\mathbin{\dot\cup}A_t\) and
\(E_t=X_t\mathbin{\dot\cup}B_t\). Moreover

\[
 A_{t+1}=A_t-\alpha_t+\alpha_{t+q_0},
 \qquad
 B_{t+1}=B_t-\beta_t+\beta_{t+q_0}.
\]

Substitute these identities and (2.7) into
\(D_{t+1}=X_{t+1}\setminus A_{t+1}\) and
\(E_{t+1}=X_{t+1}\cup B_{t+1}\). This gives (3.1), and subtraction gives
(3.2). Geodesicity through \(q_0+1\) makes all support labels in that
window distinct. \(\square\)

Define the **boundary transition graph** \(\mathcal B_{q_0}(\mathcal D)\)
on \(\Omega\) by placing an arc \(C\to C'\) when there are four distinct
labels \(a,b,u,v\) such that

\[
 D(C')=D(C)-u+b,qquad E(C')=E(C)-a+v,
\tag{3.4}
\]

with

\[
 a,b\in F(C),\qquad u\in D(C),\qquad v\notin E(C).
\tag{3.5}
\]

Equations (3.1) show that every successor in a middle-window route, in
particular every genuine-rotor successor in the SCD path-forest model,
lies in this graph. This assertion is not made for a general promotion
bridge, whose useful-state realization need not identify the provider
flags with forward windows of the successive middle owners.  The graph is
only a projection even in the rotor model: a sequence of its arcs need not
admit globally consistent ordered port blocks.

### Corollary 3.2 (projected Hall cut)

If a vertex set \(V\subseteq\Omega\) has an annular-compatible directed
middle-window (in particular, genuine-rotor) path cover with \(p\) paths,
then

\[
 \boxed{
 p\ge |V|-\nu(\mathcal B_{q_0}[V])
 =\max_{S\subseteq V}
   \bigl(|S|-|N_{\mathcal B_{q_0}[V]}(S)|\bigr).}
\tag{3.6}
\]

Here \(\nu\) is maximum split-bipartite matching size.  A forward-order
version is obtained by retaining only arcs increasing in the chosen order.

#### Proof

The \(|V|-p\) path arcs have pairwise distinct tails and heads, hence
form a split-bipartite matching.  Lemma 3.1 puts every one in
\(\mathcal B_{q_0}[V]\).  Thus
\(|V|-p\le\nu(\mathcal B_{q_0}[V])\). Hall's deficiency identity gives
the second equality. \(\square\)

This is a genuine obstruction test, but no universal lower bound for its
deficiency is proved here.

## 4. The outer-tail overlap graph

Let

\[
 \Omega_H=\{C\in\mathcal D:\rho(C)\ge H\},
 \qquad |\Omega_H|=N_H.
\]

For \(C,C'\in\Omega_H\), put an arc \(C\to C'\) in the
**outer-tail overlap graph** \(\mathcal T_{q_0,H}(\mathcal D)\) when

\[
 \delta_j(C')=\delta_{j+1}(C),\qquad
 \eta_j(C')=\eta_{j+1}(C)
 \quad(q_0+1\le j\le H-1).
\tag{4.1}
\]

When \(H=q_0+1\), (4.1) is vacuous; for the fixed annulus \(a<b\), its
length is \((b-a)\sqrt m+O(1)\).

### Lemma 4.1 (inner reordering cannot repair the outer tail)

Every genuine radius-\(H\) rotor edge between two top providers, under any
annular-compatible choices of middle corners and inner block orderings,
projects to an arc of \(\mathcal T_{q_0,H}(\mathcal D)\).

#### Proof

Let \(a_j(C),b_j(C)\) be the forward deletion and insertion words of the
chosen full port. Consecutive full radius-\(H\) rotor states are one-step
shifts of the same physical route, so

\[
 a_j(C')=a_{j+1}(C),\qquad b_j(C')=b_{j+1}(C)
 \quad(1\le j\le H-1).
\tag{4.2}
\]

For \(j>q_0\), annular compatibility forces

\[
 a_j(C)=\delta_j(C),\qquad b_j(C)=\eta_j(C).
\]

Substitution in (4.2) for \(q_0+1\le j\le H-1\) gives (4.1).
\(\square\)

Let \(\lambda_H^{\rm tail}(\mathcal D)\) be the largest number of edges
in a vertex-disjoint directed linear forest in
\(\mathcal T_{q_0,H}(\mathcal D)\).

### Theorem 4.2 (annular-compatible top-run cut)

Every annular-compatible bridge-one path cover of the \(N_{q_0}\)
providers with \(p\) paths satisfies

\[
 \boxed{
 p\ge
 \bigl(2N_H-N_{q_0}-\lambda_H^{\rm tail}(\mathcal D)\bigr)_+.}
\tag{4.3}
\]

Put

\[
 K=\left\lfloor\frac{N_{q_0}}{2m}\right\rfloor,\qquad
 \rho=N_{q_0}-2mK<2m.
\tag{4.4}
\]

If all but the \(\rho\) residual providers lie in \(K\) radius-\(H\)
rotor cycles of length \(2m\), then

\[
 \boxed{
 \lambda_H^{\rm tail}(\mathcal D)
 \ge 2N_H-N_{q_0}-\rho-K.}
\tag{4.5}
\]

#### Proof

In a path cover, mark top providers by \(\mathsf H\) and all other
providers by \(\mathsf O\).  The number of nonempty \(\mathsf H\)-runs is
at most

\[
 (N_{q_0}-N_H)+p.
\]

Hence at least \(2N_H-N_{q_0}-p\) selected arcs have both ends in
\(\Omega_H\).  These arcs form a directed linear forest and, by Lemma
4.1, lie in the tail graph.  This proves (4.3).

For the cycle statement, omit the \(\rho\) unused providers and cut one
edge in each of the \(K\) cycles. At most \(\rho\) top providers and at
most \(K\) top-to-top edges are thereby lost. Apply the same run count.
\(\square\)

Using \(N_{q_0}/W=e^{-a^2+o(1)}\) and
\(N_H/W=e^{-b^2+o(1)}\), (4.3) forces a positive-density tail-overlap
forest when

\[
 b^2-a^2<\log2.
\tag{4.6}
\]

This is the corrected version of the narrow-annulus top cut which remains
valid after all invisible inner collars are optimized.  It gives no
conclusion until \(\lambda_H^{\rm tail}\) is estimated for the chosen
noncanonical SCD.

The extension-independent full-top fibre inequality from the audited
scaffold also survives unchanged:

\[
 p+r_{\rm full}\ge N_H,
\tag{4.7}
\]

where \(r_{\rm full}\) is the number of full rotor arcs.  Its proof uses
only the \(N_H\) distinct rank-\((m+H)\) top fibres and is unaffected by
permuting the invisible inner blocks.

## 5. Exact optimized Hall gate

For each provider \(C\), let \(\mathcal P(C)\) be its complete menu of
annular-compatible radius-\(H\) ports from Section 2. A **port
transversal** chooses one member of each \(\mathcal P(C)\), with all chosen
middle roots distinct.  Such a transversal always exists: choosing the
original SCD middle owner for every chain already gives distinct roots.

For a fixed transversal \(\tau\) and total order \(\prec\), make the split
bipartite graph \(G(\tau,\prec)\) whose forward edges are literal
bridge-one, or more restrictively genuine-rotor, transitions between the
chosen ports.  Then the exact path-cover optimum in this model is

\[
 \boxed{
 p_{\rm ann}(\mathcal D)
 =\min_{\tau}\min_{\prec}
   \max_{S\subseteq\Omega}
   \bigl(|S|-|N_{G(\tau,\prec)}(S)|\bigr).}
\tag{5.1}
\]

Indeed, for fixed \((\tau,\prec)\), this is precisely the split-copy
ordered-Hall theorem.  The two outer minima express the genuinely coupled
collar-transversal choice; ordinary Hall applied before choosing one port
per provider is not sufficient.

If (5.1) is \(o(W/H)\), the SCD provider census and hard-start compiler
give length \(W+o(W)\) for the fixed annulus. A factor into length-\(2m\)
cycles is stronger than (5.1), but it is not arithmetically necessary.

There is also an exact packetization of any positive path-cover result.
Cut each of its paths after every \(2m\) states. If the original cover has
\(p\) paths, the number \(B\) of resulting path packets satisfies

\[
 B\le \sum_P\left\lceil\frac{|P|}{2m}\right\rceil
 \le \frac{N_{q_0}}{2m}+p.
\tag{5.2}
\]

Hard-start every packet.  No provider is omitted, so no target repair is
needed, and the total length is at most

\[
 \boxed{
 W+2HB
 \le W+\frac{H}{m}N_{q_0}+2Hp.}
\tag{5.3}
\]

Thus \(p=o(W/H)\) already gives a family of length-at-most-\(2m\) path
packets at total cost \(W+o(W)\). Closing those packets into literal
\(2m\)-cycles is an additional factorization demand, not a requirement of
the annulus compiler.

## 6. Floor-corrected cycle scope

Suppose \(2mK=N_{q_0}-\rho\) providers, with \(0\le\rho<2m\), are assigned
distinct middle roots and partitioned into \(K\) annular-compatible
radius-\(H\) rotor cycles of length \(2m\). Cut and hard-start every cycle.
The packet words cost

\[
 (2m+2H)K.
\]

Append the other \(W-2mK\) middle masks as singletons. At a signed depth
\(q\), only an omitted designated SCD provider can create a new hole, so
there are at most \(\rho\) lower and \(\rho\) upper holes.  Therefore the
exact length bound is

\[
 \boxed{
 W+2HK+2\rho(H-q_0+1).}
\tag{6.1}
\]

Here

\[
 2HK=O(W/\sqrt m),\qquad
 2\rho(H-q_0+1)=O(m^{3/2})=o(W).
\]

Thus no divisibility hypothesis \(2m\mid N_{q_0}\) is needed. Equation
(6.1) is sufficient only after owner simplicity and literal port
compatibility have been proved.

## 7. Audit boundary

The following parts of the fixed-collar SCD scaffold are correct.

1. A tag-\(d<H\) chain has exactly the positive extension menu in (2.5).
2. The retained SCD providers give exact one-copy target support at every
   annular depth.
3. A \(p\)-path rotor cover compiles at \(W+2Hp\).
4. The omitted-provider and floor-corrected cycle ledgers are exact.
5. The full-top fibre cut (4.7) is extension-independent.
6. The assertion that the clipped BTK rotor graph is empty must not be
   used; explicit clipped BTK rotor edges are known.

The necessary qualification is that a unique clipped top state exists
only if all inner SCD flags are frozen.  In the minimal annulus problem,
the block permutations (2.3), and optionally the alternate middle corners
(2.1), are legal.  A top statistic computed in one fixed collar
transversal therefore does not obstruct all partial-annulus designs.
The outer-tail graph and (4.3) are invariant under this relaxation.

No construction of the required port transversal, long path cover, or
\(2m\)-cycle factor is proved. The exact surviving task is either

\[
 p_{\rm ann}(\mathcal D)=o(W/H)
\]

for one noncanonical SCD, or a direct cycle factor satisfying (6.1).  The
new equations show precisely what the singleton slack removes (the inner
\(q_0\) order) and what it does not remove (the moving boundary recurrence,
the outer SCD tails, and the coupled owner-transversal Hall problem).
