# Annular cyclic packets: slow bites, the true diagonal gate, and shared leaves

Date: 2026-07-27

Scope: only the first Gaussian-annulus cyclic-packet hypergraph.  This note
does not use the much larger synchronized common-core configuration
hypergraph.

## 0. Verdict

Let

\[
 n=2m,\qquad r=m-q_0,\qquad q_0=a\sqrt m+O(1),\quad a>0,
\]

and let \(\mathcal H_{m,r}\) have vertex set \(\binom{[n]}r\).  Its edges
are the \(n\) length-\(r\) intervals of an unoriented cyclic order.  Then

\[
 K=n=2m,\qquad D={r!(n-r)!\over2},\qquad
 {\Delta _2\over D}={2\over r(n-r)}=(2+o(1))m^{-2}.
\]

The following conclusions are rigorous.

1. Classical Pippenger--Spencer cannot be invoked with \(K=K(m)\): its
   threshold is \(\delta(K,\varepsilon)\), with \(K\) fixed before the
   asymptotics.  Small relative pair codegree alone is not a
   uniform-in-\(K\) theorem.
2. The packet catalogue has substantially more structure than its maximum
   codegree records.  For every packet \(e\),

   \[
   {1\over D}\sum_{\{S,T\}\in\binom e2}d(S,T)
       ={4\over m}+O_a(m^{-2}).                                      \tag{0.1}
   \]

   Consequently one isolated slow bite at marking rate
   \(\gamma/(KD)\) is product-like with relative error \(O_a(m^{-2})\).
3. Under formal product thinning to vertex density \(z\), the two local
   small parameters are

   \[
   \eta(z)=O_a((mz)^{-1}),\qquad
   \alpha(z)=O_a((mz)^{-1}),                                      \tag{0.2}
   \]

   where \(\eta\) is the within-packet collision energy and \(\alpha\)
   is the maximum relative one-edge influence on a vertex link.  Both are
   \(O(m^{-1/2})\) at \(z=m^{-1/2}\).  Thus there is no first-moment or
   maximum-jump obstruction to a leave \(N/\sqrt m\).
4. What is not proved is regeneration of (0.2), together with its mixed
   row--column energy analogues, for \(\Theta(K\log m)\) successive bites.
   This is a catalogue-specific dynamic link-energy theorem, not a
   consequence of Pippenger--Spencer.
5. A common packet leave across all annular depths really can save the
   factor \(\sqrt m\) at the scalar-capacity level.  If
   \(L=N_{q_0}-K|\mathcal M|\asymp N_{q_0}/\sqrt m\), its unavoidable
   aggregate hole contribution is only \(O_a(N_{q_0}/\sqrt m)=o(W)\),
   not \(\Theta(W)\).  The remaining exact obstruction is the aggregate
   repeat excess above the forced floor at the deeper ranks.  A matching at
   rank \(q_0\) alone gives no control of that excess.

Thus the latest favorable audit is half right: the numerical packet
geometry is genuinely favorable, and synchronized leaves are useful.  It
is wrong that classical PS proves the diagonal iteration.

## 1. Exact pair codegrees

For two distinct \(r\)-sets \(S,T\), put

\[
 d=|S\setminus T|=|T\setminus S|.
\]

### Lemma 1.1 (overlapping pair)

If \(1\le d<r\), then

\[
 {d(S,T)\over D}
   ={2\over\binom rd\binom{n-r}d}.                                \tag{1.1}
\]

#### Proof

Write

\[
 A=S\setminus T,\quad C=S\cap T,\quad B=T\setminus S,
 \quad E=[n]\setminus(S\cup T).
\]

Both \(S=A\cup C\) and \(T=C\cup B\) are cyclic intervals precisely
when, up to reversal, the four blocks occur in the order

\[
 A,C,B,E.
\]

Permuting inside the four blocks gives

\[
 d(S,T)=d!^2(r-d)!(n-r-d)!.
\]

Division by \(D=r!(n-r)!/2\) proves (1.1). \(\square\)

### Lemma 1.2 (disjoint pair)

If \(S\cap T=\varnothing\) and \(c=n-2r>0\), then

\[
 {d(S,T)\over D}
 ={r!(c+1)!\over(n-r)!}
 ={c+1\over\binom{n-r}r}.                                         \tag{1.2}
\]

#### Proof

Contract \(S\) and \(T\) to two blocks.  Together with the \(c\) exterior
points there are \(c+2\) circular objects.  Their unoriented circular
orders number \((c+1)!/2\), while the two internal block orders contribute
\(r!^2\).  Divide by \(D\). \(\square\)

Equation (1.1) is maximal at \(d=1\) in the Gaussian range, and (1.2) is
superpolynomially smaller.  This proves the displayed value of
\(\Delta _2/D\).

## 2. The edge-local collision profile

Fix a packet

\[
 e=\{I_0,I_1,\ldots,I_{n-1}\}.
\]

For two starts at circular separation \(s\le m\), the two intervals have
Johnson distance \(s\) when \(s<r\), and are disjoint when \(s\ge r\).
There are \(n\) unordered pairs at every separation \(s<m\), and \(m\)
pairs at separation \(m\).  Hence, with

\[
 \eta(e):={1\over D}\sum_{\{S,T\}\in\binom e2}d(S,T),
\]

Lemmas 1.1--1.2 give

\[
\begin{aligned}
 \eta(e)
 &=n\sum_{s=1}^{r-1}{2\over\binom rs\binom{n-r}s}
   +\bigl(n(m-r)+m\bigr){c+1\over\binom{n-r}r}.                    \tag{2.1}
\end{aligned}
\]

The \(s=1\) term is

\[
 {2n\over r(n-r)}={4\over m}+O_a(m^{-2}).                         \tag{2.2}
\]

On \(2\le s\le r-1\), log-concavity puts the minimum of
\(\binom rs\binom{n-r}s\) at an endpoint.  The \(s=2\) contribution is
\(O(m^{-3})\), while the other endpoint and the disjoint term are
superpolynomially smaller for \(q_0=a\sqrt m+O(1)\).  Therefore

\[
 \boxed{\eta(e)={4\over m}+O_a(m^{-2}).}                           \tag{2.3}
\]

This average-within-an-edge statistic is much smaller than the crude
\(\binom K2\Delta _2/D=\Theta(1)\).

There is also a useful small-order higher-codegree statement.  If \(j\)
prescribed vertices lie in one packet, two of their packet positions have
circular distance at least \(s=\lceil(j-1)/2\rceil\).  Partitioning the
containing packets according to a witnessing pair and using (1.1) gives,
as long as \(s<r\),

\[
 {\Delta_j\over D}
 \le {2\binom j2\over\binom rs\binom{n-r}s}.                      \tag{2.4}
\]

This is strong time-zero spread.  It does not by itself prove dynamic
regeneration, because generator powers repeat event columns and create
mixed diagrams not encoded by \(\Delta_j\) alone.

## 3. One slow bite, with the correct \(K\)-dependence

For a packet \(e\), let \(c(e)\) be the number of other packets meeting
it.  If \(t_f=|e\cap f|\), then

\[
 \sum_f t_f=KD
\]

and

\[
 0\le\sum_f(t_f-1)_+
 \le\sum_f\binom{t_f}2
 =D\eta(e).
\]

Consequently

\[
 KD-D\eta(e)\le c(e)+1\le KD.                                   \tag{3.1}
\]

Mark every packet independently with probability

\[
 p={\gamma\over KD},\qquad0<\gamma\le1,
\]

and retain it precisely when it is the only marked packet in its conflict
neighbourhood.  Equations (2.3) and (3.1) give, uniformly in \(e\),

\[
\begin{aligned}
 \Pr(e\text{ retained})
 &=p(1-p)^{c(e)}\\
 &={\gamma e^{-\gamma}\over KD}
   \left(1+O_a(m^{-2})+o(D^{-1})\right).                           \tag{3.2}
\end{aligned}

For a fixed target \(S\), the retention events of its \(D\) incident
packets are mutually exclusive.  Therefore

\[
 \boxed{
 \Pr(S\text{ covered in the bite})
 ={\gamma e^{-\gamma}\over K}
   \left(1+O_a(m^{-2})\right).}                                   \tag{3.3}
\]

This is the correct uniform growing-\(K\) one-bite statement.  It covers
only \(\Theta(N/K)\) vertices.  Reaching density \(m^{-1/2}\) requires
\(\Theta(K\log m)\) regenerated bites.

### 3.1 Collision waste can be made negligible

There is a useful version which separates collision waste from residual
regeneration.  In a current residual hypergraph let \(\Delta\) be its
maximum vertex degree.  Mark every current edge with probability

\[
 p={\gamma\over K\Delta}.
\]

Put every isolated marked edge into the matching, but delete **all**
vertices belonging to any marked edge.  The nonisolated marked edges are
discarded as waste.  The residual is therefore induced by vertices which
were untouched by every mark, and matching integrality is automatic.

Let \(M,I,C\) be respectively the numbers of marked, isolated marked, and
nonisolated marked edges in this bite.  Every edge conflicts with at most
\(K\Delta\) edges, so, conditionally on the current residual,

\[
 \mathbb E C\le\gamma\,\mathbb E M,
 \qquad
 \mathbb E I\ge(1-\gamma)\,\mathbb E M.                           \tag{3.4}
\]

Hence

\[
 \mathbb E C\le {\gamma\over1-\gamma}\mathbb E I.                \tag{3.5}
\]

An isolated marked edge is disjoint from every other marked edge.  Thus
the matching gains exactly \(KI\) vertices in the bite, while the union of
the nonisolated marked edges wastes at most \(KC\) vertices.  Summing
(3.5) over an arbitrary adaptive sequence of bites and using that the
total matching coverage is at most \(N\) gives the unconditional bound

\[
 \boxed{
 \mathbb E(\text{total collision waste})
 \le {\gamma\over1-\gamma}N.}                                    \tag{3.6}
\]

For example, \(\gamma=m^{-1}\) makes the expected waste \(O(N/m)\), and
Markov's inequality makes it \(o(N/\sqrt m)\) with probability
\(1-o(1)\).  The price is \(\Theta(m^2\log m)\) very small bites to reach
density \(m^{-1/2}\).  Since the total reference hazard is unchanged by
this time subdivision, (3.6) shows that packet collisions themselves do
not force the critical leave.  The unresolved event is early stall or
loss of residual link regularity.

## 4. Formal trajectory scales and the exact dynamic gate

Under independent thinning to vertex density \(z\), the reference degree
and pair codegree are

\[
 d_z(S)=Dz^{K-1},\qquad
 d_z(S,T)=d(S,T)z^{K-2}.                                           \tag{4.1}
\]

Thus the edge-local collision energy becomes

\[
 \eta_z(e)={\eta(e)\over z}=O_a((mz)^{-1}).                       \tag{4.2}
\]

If one selected packet \(g\) avoids a live target \(S\), the number of
options through \(S\) which it destroys is at most

\[
 a_S(g)\le\sum_{T\in g}d_z(S,T).
\]

Using the maximum pair codegree gives

\[
 {a_S(g)\over d_z(S)}
 \le {K\Delta_2\over Dz}
 =O_a((mz)^{-1}).                                                   \tag{4.3}
\]

At \(z=m^{-1/2}\), both (4.2) and (4.3) are \(O(m^{-1/2})\), and

\[
 \log(Dz^{K-1})=(1+o(1))m\log m,                                 \tag{4.4}
\]

so the reference degrees remain factorially large.

The same-packet correction accumulated along the reference trajectory is
also small.  A bite contributes

\[
 O\left({\gamma\over K}\eta_z(e)\right).
\]

Since the number of bites per unit \(d\log(1/z)\) is \(\Theta(K/\gamma)\),
the cumulative correction down to density \(z\) is

\[
 O\left(\int_z^1{1\over m u}\,{du\over u}\right)
 =O((mz)^{-1}).                                                     \tag{4.5}
\]

Thus (4.5) is \(o(1)\) at the proposed stopping density.

What (4.1)--(4.5) do **not** prove is that the random residual actually
has these reference link profiles.  A valid diagonal theorem must
regenerate, uniformly to \(z=m^{-1/2}\), at least:

\[
 d_t(S)=(1+o(1))Dz^{K-1},                                         \tag{4.6}
\]

\[
 \max_{S,g}{a_{S,t}(g)\over d_t(S)}
       \le {m^{o(1)}\over mz},                                    \tag{4.7}
\]

and the mixed row--column energy inequalities produced when powers of
\(a_{S,t}(g)\) are put through the stopped generator.  Time-zero
higher-codegrees (2.4) control the tree diagrams, but repeated event
columns create cyclic/coherent diagrams.  Bounding those dynamically is
the exact catalogue-specific ACLE/MDLE gate.

Conditional on (4.6)--(4.7) and that mixed hierarchy, the standard stopped
generator argument runs for \(\Theta(K\log m)\) bites and leaves
\((m^{-1/2}+o(1))N\) targets.  Without that hierarchy, the assertion is
not a theorem.

### 4.1 A literal dense edge-free residual

There is an exact reason the regeneration theorem must be
trajectory-specific.  Fix an \(m\)-set \(A\subset[n]\), and define the
central hypergeometric slice

\[
 \mathcal B_A=
 \left\{S\in\binom{[n]}r:
 |S\cap A|\in
 \left\{\left\lfloor{r\over2}\right\rfloor,
             \left\lceil{r\over2}\right\rceil\right\}\right\}.   \tag{4.8}
\]

Every cyclic packet meets \(\mathcal B_A\).  Indeed, for its consecutive
windows put \(x_j=|I_j\cap A|\).  Then

\[
 x_{j+1}-x_j\in\{-1,0,1\},
 \qquad {1\over n}\sum_jx_j={r|A|\over n}={r\over2}.              \tag{4.9}
\]

If the walk \((x_j)\) avoided both central integer values, its average
could not be \(r/2\); the unit-step property prevents a jump from below to
above them.  Thus (4.8) is a transversal of the packet hypergraph.

The local central limit estimate for
\(\operatorname{Hyp}(2m,m,r)\) gives

\[
 {|\mathcal B_A|\over\binom nr}=\Theta_a(m^{-1/2}).               \tag{4.10}
\]

Consequently

\[
 \mathcal U_A=\binom{[n]}r\setminus\mathcal B_A
\]

has density \(1-\Theta_a(m^{-1/2})\) and contains no packet at all.
This does not show that the random slow-bite trajectory approaches
\(\mathcal U_A\).  It does rule out every proposed regeneration statement
for **all** dense residuals, and it identifies a concrete family of
hypergeometric-slice barriers which a trajectory proof must avoid.

## 5. Why Pippenger--Spencer is not the missing citation

The classical statement has quantifiers

\[
 \text{fix }K,\varepsilon;\qquad
 \text{choose }\delta(K,\varepsilon),D_0(K,\varepsilon);\qquad
 D\to\infty.
\]

It does not assert

\[
 m^{-2}<\delta(2m,m^{-1/2}).
\]

Uniformity cannot be absent from a general theorem.  The line hypergraph
of a projective plane of order \(q\) is

\[
 K=D=q+1,\qquad\Delta_2=1,
\]

so \(\Delta_2/D\to0\), but every two edges meet and its matching number is
one.  The packet catalogue evades this example through (2.3)--(2.4), not
through the classical quantifiers.

In particular, the max-based variable-rank expression is critical:

\[
 K{\Delta_2\over D}\log N_{q_0}=8\log2+o(1).                      \tag{5.1}
\]

The edge-local profile (2.3) shows why a packet-specific theorem may still
hold; it does not turn (5.1) into an existing black-box application.

## 6. Shared leaves across the annulus

Let \(\mathcal M\) be a matching of \(s\) rank-\(q_0\) packets.  Use the
same cyclic orders at every deeper depth.  At depth \(q\), let
\(\mu_q(T)\) be the resulting target load, and put

\[
 E_q=\sum_T(\mu_q(T)-1)_+.
\]

Every selected packet supplies exactly \(K=2m\) occurrences at every
depth, so

\[
 \sum_T\mu_q(T)=Ks.
\]

Therefore the hole count has the exact identity

\[
 H_q=N_q-Ks+E_q.                                                   \tag{6.1}
\]

Define the forced duplicate floor and the excess above it by

\[
 F_q=(Ks-N_q)_+,
 \qquad \widetilde E_q=E_q-F_q\ge0.
\]

Then

\[
 \boxed{H_q=(N_q-Ks)_++\widetilde E_q.}                           \tag{6.2}
\]

This separates exactly what leave correlation buys from what it does not.

Put

\[
 N_0=N_{q_0},\qquad L=N_0-Ks,\qquad\delta=L/N_0.
\]

For \(q=q_0+d\), uniformly for \(d=o(\sqrt m)\),

\[
 {N_{q_0+d}\over N_0}
 =\exp\left(-{2q_0d+d^2\over m}+O_a(m^{-1/2}+d/m)\right).          \tag{6.3}
\]

Consequently the scalar leave floor

\[
 B(L):=\sum_{q=q_0}^{b\sqrt m}(N_q-N_0+L)_+
\]

satisfies

\[
 B(L)=O_a\left(L+{L^2\sqrt m\over N_0}\right).                   \tag{6.4}
\]

Indeed, (6.3) shows that the positive summands occur for only
\(O_a(1+\delta\sqrt m)\) depths, and each is at most \(L\).

In particular,

\[
 L=O(N_0/\sqrt m)\quad\Longrightarrow\quad
 B(L)=O_a(N_0/\sqrt m)=o(W).                                     \tag{6.5}
\]

For \(\delta\sqrt m\to\infty\), the linear expansion in (6.3) also gives

\[
 B(L)=\left({1\over4a}+o(1)\right)N_0\delta^2\sqrt m.             \tag{6.6}
\]

Thus a generic \(o(N_0)\) leave is not enough for the annulus: at the
scalar level one needs \(\delta=o(m^{-1/4})\).  The formal
\(N_0/\sqrt m\) leave is comfortably sufficient.

Finally, summing (6.2) gives the exact aggregate criterion

\[
 \boxed{
 \sum_{q=q_0}^{b\sqrt m}H_q
 =B(L)+\sum_{q=q_0}^{b\sqrt m}\widetilde E_q.}                    \tag{6.7}
\]

Separate rankwise matchings with leaves \(N_q/\sqrt m\) have aggregate
leave \(\Theta(W)\).  One synchronized packet matching has scalar floor
\(o(W)\) by (6.5), but it succeeds only if

\[
 \sum_q\widetilde E_q=o(W).                                      \tag{6.8}
\]

Rank-\(q_0\) matching proves \(\widetilde E_{q_0}=0\) and says nothing
about (6.8).  The hereditary path-colour/trace theorem is exactly the
missing correlated-repeat assertion.

There is an exact local reason not to expect an ordinary rank-\(q_0\)
nibble to give (6.8) for free.  Fix an \((r-1)\)-set \(T\).  In every
packet containing \(T\), its two rank-\(r\) extensions are obtained by
adjoining the two immediate exterior neighbours of the interval \(T\).
Conditional on containing \(T\), this unordered endpoint pair is uniform
in

\[
 \binom{[n]\setminus T}{2},
 \qquad |[n]\setminus T|=n-r+1=m+q_0+1.                            \tag{6.9}
\]

For two independently chosen packets through \(T\), their two extension
pairs are disjoint with probability

\[
 {\binom{n-r-1}{2}\over\binom{n-r+1}{2}}
 =1-{4\over n-r+1}+O(m^{-2})=1-O(m^{-1}).                         \tag{6.10}
\]

Thus almost every pairwise collision at depth \(q_0+1\) is **locally
compatible** with disjointness of the rank-\(q_0\) extensions of that same
target.  This local part of the matching constraint removes only an
\(O(1/m)\) fraction of the collision pairs.  The two packets could still
share some rank-\(q_0\) target elsewhere, so (6.10) is not a lower bound for
collisions inside an actual matching.  It does prove that avoiding a
linear depth-\(q_0+1\) repeat excess requires genuinely global packet
geometry; it is not forced by the immediate extension rule.

This must not be conflated with the synchronized common-core
configuration hypergraph.  In that larger hypergraph one omitted root
literally omits \(\Theta(m^{3/2})\) separately represented target
resources, giving an identity of the form \(\Delta+kL\).  In the ordinary
packet hypergraph, the decreasing layer sizes provide the free surplus in
(6.2), and a shared leave is genuinely cheaper.

## 7. Exact remaining theorem

One sufficient diagonal theorem for the annulus is now completely explicit:

> Run the rank-\(q_0\) packet slow bite to a leave
> \(L=O(N_{q_0}/\sqrt m)\), while regenerating (4.6)--(4.7) and the mixed
> link-energy hierarchy, and prove for the selected packet family the
> hereditary repeat estimate (6.8).

The first clause is a growing-uniformity dynamic matching theorem.  The
second is a simultaneous path-colour theorem.  Neither follows from
Pippenger--Spencer, but (2.3), (4.2)--(4.5), and (6.5) show that neither is
ruled out by the first-order arithmetic.
