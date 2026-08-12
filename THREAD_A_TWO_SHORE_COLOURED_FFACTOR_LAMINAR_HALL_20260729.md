# Two-shore coloured interval cuts and a laminar Hall theorem

## 1. Scope

This note isolates the exact reconstruction problem which remains after a
residence-motif transversal has been chosen using only same-shore edges.
It proves three statements.

1.  Once the cross-shore edge bank is frozen, degree two and the four
    immediate palettes split exactly into two independent coloured
    `f`-factor problems, one on each shore.
2.  On a bipartite same-shore replacement scaffold, a forced palette bank
    has an exact cut cost.  In the cut `(X,Y)` its entire cost is the number
    of forced edges from `L\X` to `Y`.
3.  A paired-colour Rado--Hall condition in a laminar matroid gives a
    checkable sufficient condition for choosing a palette bank which is
    automatically extendible to an `f`-factor.

None of these statements proves connectivity, unit voltage, absence of new
residence motifs, deeper-shadow coverage, or compiler compatibility.

Throughout, labelled quotient edge orbits are treated as distinct parallel
edges.  A quotient loop has incidence two at its endpoint.  The bipartite
specialization below has no loops.

## 2. Exact coloured `f`-factor normal form

Let the middle-owner vertices be partitioned into shores

\[
 V=V_A\mathbin{\dot\cup}V_B.
\]

Let `K` be a fixed edge bank.  It contains every frozen cross edge, and may
also contain retained same-shore edges which are not being rethreaded.  Put

\[
 b_s(v)=2-d_K(v),\qquad v\in V_s,\quad s\in\{A,B\}.      \tag{2.1}
\]

Necessarily `b_s(v)` is an integer in `{0,1,2}`.  Let `G_s` be the labelled
multigraph of admissible new same-shore edge orbits on `V_s`, disjoint from
`K`.  Every `e=xy` in `G_s` has two immediate palette colours

\[
 \lambda(e)=x\cap y,\qquad \upsilon(e)=x\cup y.          \tag{2.2}
\]

The symbols in (2.2) include the top-coordinate tag, so colours on the two
shores remain distinct.  Let `R_s^-` and `R_s^+` be, respectively, the
lower and upper palette rows assigned to shore `s` which are not already
covered by `K`.

In the even Boolean carrier the assignment is literal: AA supplies lower
without the top and upper without the top; BB supplies lower with the top
and upper with the top; AB can additionally supply lower without the top
and upper with the top.  Hence, after the AB bank is frozen, every residual
row has one and only one same-shore repair channel.

### Theorem 2.1 (frozen-cross two-shore factorization)

There is a degree-two extension

\[
 F=K\cup J_A\cup J_B                                  \tag{2.3}
\]

covering every immediate lower and upper palette row if and only if, for
each \(s=A,B\), there is a set \(J_s\subseteq E(G_s)\) satisfying

\[
 d_{J_s}(v)=b_s(v)\quad(v\in V_s),                     \tag{2.4}
\]

and

\[
 \begin{split}
  &\forall c\in R_s^-\quad
       J_s\cap\{e:\lambda(e)=c\}\ne\varnothing,\\
  &\forall c\in R_s^+\quad
       J_s\cap\{e:\upsilon(e)=c\}\ne\varnothing.
 \end{split}                                           \tag{2.5}
\]

In particular the two shores are completely independent for degree and
immediate-palette feasibility once `K` is fixed.

#### Proof

Every edge outside `K` has both endpoints on one shore.  Hence its incidence
contributes only to the corresponding equation (2.4), and (2.1) shows that
(2.4) is equivalent to total degree two.  After the colours already supplied
by `K` are removed, the top-coordinate tag assigns each remaining palette
row to exactly one shore.  Thus (2.5) is equivalent to completion of all four
immediate palettes.  No equation contains an edge variable from both shores,
which proves both directions.  QED.

The exact residual problem on one shore is therefore the binary system

\[
 \begin{array}{rl}
  \sum_{e\ni v}x_e&=b(v) \quad(v\in V_s),\\[2mm]
  \sum_{e:\lambda(e)=c}x_e&\ge1\quad(c\in R_s^-),\\[2mm]
  \sum_{e:\upsilon(e)=c}x_e&\ge1\quad(c\in R_s^+),\\[2mm]
  x_e&\in\{0,1\}.
 \end{array}                                           \tag{2.6}
\]

Equivalently, a candidate edge is a capacitated hyperedge incident with its
two owner endpoints and its two palette vertices.  Thus (2.6) is a genuine
four-resource `b`-matching problem, not an ordinary marginal Hall problem.

For example, let `G=C_4` with unit vertex demands.  Its two perfect matchings
are `M_0={12,34}` and `M_1={23,41}`.  Give a required lower colour only to
edge `12` and a required upper colour only to edge `41`.  The uncoloured
factor exists and each required colour occurs in some factor, but no factor
contains both required edges because they share vertex `1`.  Hence separate
degree feasibility and separate palette reachability are insufficient.

## 3. General `f`-factor completion after a provider bank

Let \(P\subseteq E(G_s)\) be a set of edges forced in order to provide missing
palette rows.  Put

\[
 f_P(v)=b(v)-d_P(v),\qquad H_P=G_s-P.                  \tag{3.1}
\]

Clearly `P` extends to a coloured `b`-factor if it covers the required rows,
`f_P>=0`, and `H_P` has an `f_P`-factor.  The last assertion has the exact
Tutte test

\[
 f_P(S)+\sum_{v\in T}d_{H_P-S}(v)-f_P(T)
       -q_{H_P,f_P}(S,T)\ge0                          \tag{3.2}
\]

for every pair of disjoint vertex sets `S,T`.  Here
`q_{H_P,f_P}(S,T)` is the number of components `C` of
\(H_P-(S\cup T)\) for which

\[
 f_P(C)+e_{H_P}(C,T)
\]

is odd.  Thus (2.6) has an exact factor oracle even when the same-shore
catalogue is nonbipartite.  Palette coverage remains an additional coupled
condition; (3.2) alone says nothing about it.

## 4. Exact Benders cuts on a bipartite replacement scaffold

The cleanest Hall form occurs when one restricts the candidate catalogue to
a bipartite spanning scaffold

\[
 G=(L,R;E).                                            \tag{4.1}
\]

Parallel labelled edges are allowed.  Write
\(b(X)=\sum_{v\in X}b(v)\) and let
`e(X,Y)` count labelled edges between `X` and `Y`.

For \(X\subseteq L\) and \(Y\subseteq R\), define the unforced cut slack

\[
 \sigma(X,Y)=e(X,R\setminus Y)-b(X)+b(Y).              \tag{4.2}
\]

### Lemma 4.1 (ordinary bipartite `b`-factor cut theorem)

The graph `G` has a `b`-factor if and only if

\[
 b(L)=b(R)                                             \tag{4.3}
\]

and

\[
 \sigma(X,Y)\ge0
 \qquad(X\subseteq L,\ Y\subseteq R).                \tag{4.4}
\]

#### Proof

Direct every edge from `L` to `R`, put an arc of capacity `b(v)` from the
source to each \(v\in L\), an arc of capacity one for every labelled edge,
and an arc of capacity \(b(w)\) from each \(w\in R\) to the sink.  A cut
whose source side contains \(X\subseteq L\) and \(Y\subseteq R\) has capacity

\[
 b(L\setminus X)+e(X,R\setminus Y)+b(Y).
\]

Requiring this to be at least `b(L)` is precisely (4.4).  Integral max flow
then gives a `b`-factor.  QED.

### Theorem 4.2 (exact forced-bank cut cost)

Assume (4.3)--(4.4), and let \(P\subseteq E\).  Then \(P\) is contained in a
`b`-factor of `G` if and only if

\[
 d_P(v)\le b(v)\qquad(v\in L\cup R)                  \tag{4.5}
\]

and, for all \(X\subseteq L\), \(Y\subseteq R\),

\[
 e_P(L\setminus X,Y)\le\sigma(X,Y).                  \tag{4.6}
\]

Consequently a coloured `b`-factor exists if and only if there is a
palette-covering bank `P` satisfying (4.5)--(4.6).

#### Proof

After forcing `P`, the residual demand is `b'=b-d_P` and the residual graph
is `G-P`.  Since every edge of `P` has one endpoint on each side, equality
of the two total residual demands follows from (4.3).  For fixed `X,Y`, put

\[
 \begin{array}{ll}
  a=e_P(X,R\setminus Y),&b_0=e_P(X,Y),\\
  c=e_P(L\setminus X,Y).&
 \end{array}
\]

The residual instance satisfies its cut inequality exactly when

\[
 b(X)-a-b_0-b(Y)+b_0+c
       \le e(X,R\setminus Y)-a.
\]

After cancellation this is `c<=sigma(X,Y)`, namely (4.6).  Lemma 4.1 now
proves the first assertion.  If `P` also covers every required palette row,
any completing residual factor preserves those providers, proving
sufficiency for the coloured problem.  Conversely, take `P` to be a
coloured `b`-factor itself; it plainly satisfies the conditions.  QED.

The cancellation in this proof is useful: forced edges in the other three
quadrants pay for their own degree consumption.  Only edges entering `Y`
from outside `X` consume the slack of cut `(X,Y)`.

Degree safety alone does not imply (4.6).  On the six-cycle with unit
demands, the disjoint forced edges `12` and `45` leave vertices `3` and `6`
unmatchable.  With `L={1,3,5}`, `R={2,4,6}`, `X={3}` and `Y={2,4}`, the
left side of (4.6) is two while `sigma(X,Y)=1`.

For an edge set \(Z\subseteq E\), define its capacitated matching rank by

\[
 \rho_b(Z)=\max\{|I|:I\subseteq Z,\ d_I(v)\le b(v)
                         \text{ for every }v\}.        \tag{4.7}
\]

Because \(Z\) is bipartite, (4.7) is an integral max-flow value.

### Corollary 4.3 (universal provider extendibility)

Assume the base conditions (4.3)--(4.4).  Every endpoint-feasible bank
\(P\subseteq E\) is contained in a \(b\)-factor if and only if

\[
 \rho_b\bigl(E(L\setminus X,Y)\bigr)\le\sigma(X,Y)
 \qquad(X\subseteq L,\ Y\subseteq R).                 \tag{4.8}
\]

In particular, the stronger expansion inequalities

\[
 \sigma(X,Y)\ge
 \min\{b(L\setminus X),b(Y)\}                         \tag{4.9}
\]

imply universal provider extendibility.

#### Proof

If (4.8) holds and \(P\) is endpoint-feasible, then

\[
 e_P(L\setminus X,Y)\le
 \rho_b(E(L\setminus X,Y))\le\sigma(X,Y),
\]

so Theorem 4.2 applies.  Conversely, take for \(P\) an optimizer in (4.7)
inside the indicated reverse quadrant.  It is endpoint-feasible, and
universal extendibility together with (4.6) gives (4.8).  Finally every
endpoint-feasible subgraph of that quadrant has at most
\(b(L\setminus X)\) edges and at most \(b(Y)\) edges, proving that (4.9)
implies (4.8).  QED.

## 5. A paired-colour laminar Hall certificate

Theorem 4.2 reduces the positive construction to selecting a provider bank
which obeys endpoint and cut capacities.  The following condition makes
that selection a single integral flow.

Let \(E_0\subseteq E\) be a provider-edge atlas.  Let \(M\) be a laminar
matroid on \(E_0\): there is a laminar family \(\mathcal L\) of subsets of
\(E_0\) and integer capacities \(\kappa(Q)\) such that

\[
 I\in M
 \quad\Longleftrightarrow\quad
 |I\cap Q|\le\kappa(Q)\quad(Q\in\mathcal L).          \tag{5.1}
\]

We may, and do, adjoin \(E_0\) itself as a root of capacity \(|E_0|\), so
every element lies below a laminar root.

Write `r_M` for its rank function.

Partition the residual palette rows into requests \(\mathcal R\), every request
containing at most one lower and at most one upper row.  Thus a request may
be a lower--upper pair or a singleton.  For \(\rho\in\mathcal R\), let

\[
 N(\rho)=\{e\in E_0:e\hbox{ supplies every row in }\rho\}.  \tag{5.2}
\]

Pairing lower and upper rows in this way is where the two-colour output of
one Johnson edge is used.  Using all singleton requests remains valid but is
usually wasteful.

### Theorem 5.1 (laminar paired-palette Hall theorem)

Assume first that the two total endpoint demands balance:

\[
 b(L)=b(R).                                             \tag{5.3a}
\]

Suppose in addition that the following three conditions hold.

**Endpoint safety.**  For every vertex `v`,

\[
 r_M(E_0\cap\delta(v))\le b(v).                       \tag{5.3}
\]

**Benders safety.**  For every \(X\subseteq L\), \(Y\subseteq R\),

\[
 r_M\bigl(E_0\cap E(L\setminus X,Y)\bigr)
       \le\sigma(X,Y).                                \tag{5.4}
\]

**Paired Hall.**  For every subfamily
\(\mathcal Q\subseteq\mathcal R\),

\[
 r_M\left(\bigcup_{\rho\in\mathcal Q}N(\rho)\right)
       \ge |\mathcal Q|.                              \tag{5.5}
\]

Then `G` has a coloured `b`-factor covering every residual lower and upper
palette row.

#### Proof

The matroidal Hall theorem applied to the families \(N(\rho)\) says that (5.5)
is equivalent to the existence of distinct representatives

\[
 e_\rho\in N(\rho)\quad(\rho\in\mathcal R)
\]

whose set \(P=\{e_\rho:\rho\in\mathcal R\}\) is independent in \(M\).
For completeness, in the
laminar case this is ordinary integral max flow: make one unit-demand source
node for each request, join it to its candidate edge-elements, attach each
element to the smallest laminar node containing it by an arc of capacity
one, direct the laminar tree toward its root, and give the arc leaving a
laminar node capacity \(\kappa\) of that node.  The source-to-request arcs
also have capacity one.  Max-flow/min-cut is exactly (5.5).

Every required row lies in one request and is supplied by its representative,
so `P` is palette-covering.  Independence and (5.3) imply (4.5).  Likewise,
independence and (5.4) imply (4.6).  Theorem 4.2 extends `P` to a `b`-factor,
which remains palette-covering because none of the forced edges is removed.
QED.

### Corollary 5.2 (robust-expansion form)

If \(b(L)=b(R)\) and \(G\) satisfies (4.8), then Benders safety (5.4) may
be deleted from Theorem 5.1: endpoint safety (5.3) and paired Hall (5.5)
suffice.  In particular balance and the elementary margins (4.9), together
with (5.3) and (5.5), are a self-contained sufficient condition for
coloured completion.

#### Proof

The Rado--Hall representatives form an endpoint-feasible bank by (5.3),
and Corollary 4.3 extends every such bank.  QED.

All hypotheses are finite and independently checkable.  Laminar ranks are
computed bottom-up on the laminar tree; (5.5) is one max-flow computation.
Conditions (5.3)--(5.4) may either be checked directly, or certified by
covering each endpoint star and each reverse cut quadrant by an antichain of
laminar nodes whose total capacity is at most the displayed bound.

The deliberately strong part is (5.4): it asks the whole laminar atlas to be
safe for every degree cut, not merely the eventually selected bank.  A less
uniform but still exact certificate is to obtain `P` from (5.5) and then
check (4.5)--(4.6) for that one `P`.  Failure returns the explicit pair
`(X,Y)` as a Benders cut which can be added to the next provider-flow round.

## 6. Alternating-circuit version

When no useful bipartite raw-edge scaffold exists, degree feasibility can be
built into the provider atlas.  Start from any same-shore `b`-factor `J_0`.
A port is a balanced signed switch

\[
 \Sigma=(A_\Sigma,D_\Sigma),\qquad
 A_\Sigma\subseteq E\setminus J_0,\qquad
 D_\Sigma\subseteq J_0,\qquad
 d_{A_\Sigma}=d_{D_\Sigma}.                           \tag{6.1}
\]

An alternating even circuit is the basic example.  Suppose a laminar
matroid on such ports has the certified property that every independent port
set has compatible `0/1` supports, preserves one locked witness for every
already covered palette row, and that its simultaneous switch is therefore
a `b`-factor.  Define \(N(\rho)\) by the palette rows gained by a port.  Then the
same rank inequalities (5.5) produce a simultaneous factor-preserving,
palette-covering switch family.  This is a convenient PBBS implementation
target: local rectangles or longer alternating circuits are the ports,
rather than naked replacement edges.

The compatibility and locked-witness assertions in this paragraph are
essential.  Individually safe alternating circuits can jointly delete all
providers of a colour, and overlapping circuits need not commute.

## 7. Application boundary at `k=16`

For the compiler-eligible `k=16` Hamilton carrier, the exact residence
interval hypergraph has a packing of `147` pairwise edge-disjoint motifs and
a transversal of `147` edge orbits.  Hence `tau=nu=147`.  One minimum
transversal contains

\[
 87\ \mathrm{AA},\qquad 0\ \mathrm{AB},\qquad
 60\ \mathrm{BB}.                                      \tag{7.1}
\]

The retained finite certificates are
`scratch/k16_residence_motif_matching147_20260729.json` for the packing and
`scratch/k16_residence_motif_minholes_same_shore_r147_20260729.json` for a
same-shore transversal.

The packing and transversal are mutually certifying: every transversal has
size at least the packing size, while (7.1) attains it.  Therefore the cross
bank can be frozen at the residence-cut stage without paying more than the
unrestricted minimum.  Theorem 2.1 then turns any *fixed-cut*
reconstruction into two independent coloured `f`-factor instances.

The canonical `87/60` cut fails even the singleton endpoint-accessibility
rows: four lost lower colours and five lost upper colours have no same-shore
provider on exposed endpoints.  More decisively, the joint radius-`147`
model varies the cut over the complete union of the `147` packed motifs,
fixes all `80` old `AB` edge orbits, allows every off-seed nonloop `AA/BB`
seam, and enforces exact degree two plus both q1 palettes.  It is
`INFEASIBLE`.  Hence the zero-cross minimum-radius face is closed: a viable
minimum-distance rethread must change the cross pattern, or else use more
than `147` deletions.  The two-shore factorization remains the exact
conditional theorem after a viable cross/cut bank is fixed.

This is a structural reduction, not a completed rethread.  A successful
application still has to exhibit either

* a same-shore provider bank satisfying Theorem 4.2, or
* a laminar provider/switch atlas satisfying Theorem 5.1 or Section 6,

on both shores.  Afterward one must separately verify:

1. connectivity of the combined degree-two factor;
2. unit voltage of every required developed component;
3. the boundary traces at the newly inserted edges, hence absence of new
   residence motifs;
4. deeper lower/upper shadows and the common compiler.

Thus the exact new target is not another residence hitting set on the fixed
cross face.  It is a joint cross/cut choice carrying endpoint-accessibility
clauses, followed by paired-colour provider flow inside the cut slacks (4.2)
and then a topological and chronological audit.

The finite no-go is recorded in

```text
scratch/k16_residence_fixed_cross_same_shore_transversal_barrier_20260729.json
scratch/k16_same_shore_radius147_noab_cegar_20260729.json
```

The second JSON is a trusted exact CP-SAT `INFEASIBLE` record and does not
contain a standalone proof log; the nine singleton endpoint obstructions in
the first JSON are directly replayable.
