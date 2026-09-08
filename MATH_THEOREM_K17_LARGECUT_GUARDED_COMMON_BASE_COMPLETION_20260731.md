# Guarded common-independence completion in the K17 larger-cut regime

Date: 2026-07-31  
Status: exact residual-completion theorem and CEGAR interface; independent
replay of the persisted quick-round incumbent identifies a strict
lower-colour obstruction and incomplete witness export  
Scope: lower-\(q_1\) colour recycling, factor-edge reorientation, extra
ejection cuts, path-cover connectivity, and guarded upper-witness retention.
Residence, staircase compilation, and literal-word verification remain
separate final gates.

## 0. Verdict

There is an exact noncircular completion model which simultaneously allows

1. reselection of safe provider seams;
2. deletion of additional factor edges (ejection cuts);
3. independent reversal of the surviving factor fragments; and
4. retention or reselection of protected upper witnesses.

Its unguarded core is a target-size common-independent-set problem for four
matroids: the tail, head, lower-colour, and graphic matroids.  Upper-witness
and residence choices are guarded disjunctions over directed path blocks.
After fixing the complete collection of seam-collar and target-block
certificates used by a solution, the remaining extension question is exactly
a target-size common-independent-set extension in the four contracted
matroids.

This is implementable in the all-target CEGAR without first guessing a cut
set or fragment orientation.  It is not an ordinary network flow.  Even after
connectivity is dropped, every seam simultaneously occupies a tail, a head,
and a colour; fixed-fragment completion is therefore a three-partition
matching problem.  Connectivity contributes the fourth, graphic, matroid.

For the reported K17 state with 3,636 canonical cuts and 2,320 retained
seams, the only unconditional arithmetic is the edge-count deficit
\(N-1,316\).  If the retained arcs are also independent in the tail, head,
colour, and graphic matroids, Corollary 3.1 turns that deficit into 1,316 free
slots of each kind and a requirement of exactly 1,315 return seams.  The
round-zero selection was not persisted, so those independence hypotheses
cannot be audited from its log.  Under the same hypotheses, \(e\) additional
physical ejection cuts require \(1,315+e\) returns.  Thus extra cuts create
geometric routing choices, not scalar slack.

No equality or K17 word claim follows from this theorem.

## 1. Physical setup

Let \(V\) be the \(N\) rank-\(r\) owners.  Let \(F\) be a spanning physical
Johnson 2-factor whose physical edges use the rank-\((r-1)\) palette
\(\mathcal C\) exactly once.  Thus

\[
                 |V|=|\mathcal C|=|E(F)|=N.
\]

For a directed Johnson arc \(a=(u,v)\), write

\[
                 \partial a=\{u,v\},\qquad
                 \chi(a)=u\cap v.
\]

The ground catalogue \(G\) contains both orientations of every physical
factor edge and every nonfactor directed seam permitted by the current
literal catalogue.  Opposite orientations of one physical edge are parallel
ground elements.  A seam whose safety depends on a collar is not declared
unconditionally safe: its witness state records the complete directed collar
which must survive.

On \(G\), define four matroids:

* \(M_{\rm out}\): capacity one at every tail;
* \(M_{\rm in}\): capacity one at every head;
* \(M_{\rm col}\): capacity one in every colour class; and
* \(M_{\rm gr}\): the graphic matroid after forgetting arc orientation.

## 2. The exact orientation-free system

For every arc \(a\in G\), let \(x_a\in\{0,1\}\).  Let \(h_v,t_v\) identify
the initial and terminal owner, and let \(z_c\) identify the unique omitted
lower colour.  The exact degree and colour equations are

\[
 \sum_{a\in\delta^+(v)}x_a+t_v=1,
 \qquad
 \sum_{a\in\delta^-(v)}x_a+h_v=1                 \tag{2.1}
\]

for every \(v\in V\), and

\[
 \sum_{a:\chi(a)=c}x_a+z_c=1                    \tag{2.2}
\]

for every \(c\in\mathcal C\), with

\[
       \sum_v h_v=\sum_v t_v=\sum_c z_c=1.       \tag{2.3}
\]

Graphic independence is imposed by

\[
 \sum_{a:\partial a\subseteq S}x_a\le |S|-1
       \qquad(\varnothing\ne S\subseteq V).       \tag{2.4}
\]

It is enough in a lazy implementation to add (2.4) for each selected directed
cycle found by replay, because (2.1) makes every cyclic component a directed
cycle.

### Guarded seam collars and path-block witnesses

For every context-dependent seam \(a\), let \(\mathcal R(a)\) be its complete
family of certified directed collar realizations.  A realization \(\rho\)
has a directed support \(D(\rho)\subseteq G\).  With guard variables
\(g_\rho\), impose

\[
 g_\rho\le x_a,\qquad
 g_\rho\le x_b\quad(b\in D(\rho)),\qquad
 x_a\le\sum_{\rho\in\mathcal R(a)}g_\rho.          \tag{2.5}
\]

An intrinsically safe seam has one empty-support realization.  Equation
(2.5) is required for return seams as well as service seams; otherwise a
solver could use an uncertified return boundary.

For each required upper target \(T\), let \(\mathcal W(T)\) be a literal
family of directed path blocks.  A block \(w\) consists of a directed arc set
\(B(w)\subseteq G\), already checked to form a path and to have vertex union
\(T\).  It may contain a provider seam, source-factor prefix/suffix arcs, and
all run-safety collar arcs.  Introduce \(y_w\in\{0,1\}\) and impose

\[
 y_w\le x_a\quad(a\in B(w)),
 \qquad
 \sum_{w\in\mathcal W(T)}y_w\ge1.                \tag{2.6}
\]

A banked witness is the special case \(y_w=1\).  Reversed realizations are
distinct blocks.  If \(\mathcal W(T)\) is complete, (2.6) is complete; if it
contains only a selected safe bank, it is a sound but potentially restrictive
protection condition.

### Theorem 2.1 (guarded rainbow Hamilton-path completion)

The system (2.1)--(2.6) is feasible if and only if there is a spanning
directed Johnson path which

1. uses every lower colour except one exactly once; and
2. contains a certified collar for every context-dependent seam and one
   advertised literal directed block for every required target.

More precisely, fix a complete certificate choice \(\Gamma\): it specifies
the seams used by that choice, one collar realization for each such seam, and
one witness block for every target.  Put \(P(\Gamma)\) equal to the union of
all arcs forced by those certificates.  Conditional on \(\Gamma\), feasibility
holds if and only if \(P(\Gamma)\) is independent in all four matroids and
the contractions

\[
 M_{\rm out}/P(\Gamma),\quad M_{\rm in}/P(\Gamma),\quad
 M_{\rm col}/P(\Gamma),\quad M_{\rm gr}/P(\Gamma) \tag{2.7}
\]

have a common independent set of size \(N-1-|P(\Gamma)|\) on the residual
ground consisting of factor arcs and intrinsically safe seams.  Equivalently,
the full problem is the finite guarded disjunction over complete
\(\Gamma\)'s of these conditional target-size common-independence instances.
The unguarded relaxation alone is a four-matroid target-size
common-independent-set problem.

#### Proof

A path with the stated properties gives a feasible assignment directly.
Conversely, summing (2.2) gives exactly \(N-1\) selected arcs.  Equation
(2.4) makes their underlying physical graph a forest.  A forest on \(N\)
vertices with \(N-1\) edges is a spanning tree.  Equations (2.1) bound each
undirected degree by two; hence the tree is a path.  At every internal vertex
one selected arc enters and one leaves, so its orientation is coherent from
the unique initial vertex to the unique terminal vertex.  Equations
(2.2)--(2.3) give distinct lower colours and one omitted colour.  Finally,
(2.5) certifies every selected seam boundary, and (2.6) embeds every chosen
directed target block as a consecutive block of this unique path.  The
conditional contraction statement is the definition of extension of a
prescribed common-independent set. \(\square\)

The theorem permits provider seams to be selected rather than prescribed:
retain (2.6), and let the solver choose the corresponding \(y_w\)'s.  It also
permits one seam to serve several targets.

## 3. The physical ejection ledger

For each colour \(c\), let \(e_c\) be the unique physical factor edge of
colour \(c\).  Write \(e_c^+,e_c^-\) for its two orientations and define the
physical cut variable

\[
             c_c=1-x_{e_c^+}-x_{e_c^-}.           \tag{3.1}
\]

Combining (3.1) with (2.2) gives the orientation-free recycling identity

\[
 \boxed{
  \sum_{a\in G\setminus\vec E(F):\chi(a)=c}x_a
       =c_c-z_c.}                                  \tag{3.2}
\]

Thus every selected seam has the colour of a deleted physical factor edge;
every deleted factor colour except one is used by exactly one seam.  In
particular,

\[
          |\text{physical cuts}|=|\text{seams}|+1. \tag{3.3}
\]

Equation (3.2), rather than a frozen successor-index cut, is the correct
ledger when fragment reversal is allowed.  A prescribed seam \(u\to v\)
forces its *colour-source* factor edge to be physically cut.  It does not by
itself force the old outgoing edge at \(u\), or the old incoming edge at
\(v\), to remain physically cut: one of those edges can survive in reverse
orientation.  This distinction is exactly the reorientation escape missed
by a fixed-frame cut model.

### Corollary 3.1 (reported 3,636/2,320 arithmetic)

Assume the reported 2,320 seams are retained and the complete retained
partial arc set is independent in the tail, head, and colour matroids.  Assume
also that the current canonical opening really deletes 3,636 physical factor
edges and that the retained set is graphic-independent.  It then has

\[
              N-3636+2320=N-1316.
\]

The retained set therefore has 1,316 path components/free tail slots, 1,316 free head
slots, and 1,316 unused cut colours.  Completion needs 1,315 return seams.
After \(e\) additional ejection cuts, all three residual resource counts are
\(1316+e\), and completion needs \(1315+e\) seams.

The assumptions in this corollary must be replayed from the literal artifact.
In particular, a retained directed cycle makes the prescribed partial set
dependent in \(M_{\rm gr}\) and cannot be repaired without releasing at least
one retained arc.

## 4. Three exact implementation levels

### 4.1 Frozen source orientation

Let \(s(i)\) be the source successor and let
\(\lambda(i)=i\cap s(i)\), a bijection from source-edge tails to colours.
For a seam \(a=(u,v)\), put

\[
 \alpha(a)=u,\qquad \beta(a)=s^{-1}(v),\qquad
 \gamma(a)=\lambda^{-1}(u\cap v).
\]

If \(c_i\) cuts the canonical edge \(i\to s(i)\), the exact path-cover
ledgers are

\[
 \sum_{a:\alpha(a)=i}x_a=c_i-t_i,\qquad
 \sum_{a:\beta(a)=i}x_a=c_i-h_i,\qquad
 \sum_{a:\gamma(a)=i}x_a=c_i-z_i,                \tag{4.1}
\]

with one terminal, one initial, and one omitted-colour cut.  These equations
allow arbitrary extra canonical cuts and are exact up to directed-cycle
elimination.  Here \(t_i,h_i,z_i\le c_i\) and each of the three marker
families has sum one.  They do not allow fragment reversal.

### 4.2 Fixed physical cuts, variable fragment orientations

Fix a physical cut set \(K\) meeting every source cycle.  Its deletion gives
fragments \(J\in\mathcal J(K)\).  For each fragment use two state variables
\(u_{J,+},u_{J,-}\) with

\[
                         u_{J,+}+u_{J,-}=1.         \tag{4.2}
\]

A seam option \(a=(J,\sigma;L,\tau;c)\) joins the exit of oriented state
\((J,\sigma)\) to the entry of \((L,\tau)\) and has colour \(c\in\chi(K)\).
With option variables \(x_a\), impose

\[
 \sum_{a\text{ exits }(J,\sigma)}x_a
       =u_{J,\sigma}-t_{J,\sigma},                \tag{4.3}
\]

\[
 \sum_{a\text{ enters }(J,\sigma)}x_a
       =u_{J,\sigma}-h_{J,\sigma},                \tag{4.4}
\]

\[
 \sum_{a:\chi(a)=c}x_a=1-z_c                    \tag{4.5}
\]

for cut colours, together with one initial state, one terminal state, and one
hole colour.  For every proper nonempty fragment set \(S\), add

\[
 \sum_{a:J(a),L(a)\in S}x_a\le |S|-1.            \tag{4.6}
\]

Equations (4.2)--(4.6) are an exact orientation-and-order model for fixed
physical cuts.  Protected blocks simply force compatible orientation states
and link options.

#### Proof of exactness

Every directed path through the fragments chooses one state of each fragment,
one outgoing link except at its terminal fragment, one incoming link except at
its initial fragment, and every cut colour except the lower boundary hole.
It therefore satisfies (4.2)--(4.6).

Conversely, deleting \(K\) from a union of cycles gives exactly \(|K|\)
fragments.  Summing (4.5) gives \(|K|-1\) links.  Equations (4.3)--(4.4)
bound fragment indegree and outdegree by one, while (4.6) makes the
underlying link graph a forest.  A forest on \(|K|\) fragment vertices with
\(|K|-1\) links is a tree; the degree equations make it a consistently
directed path.  Expanding each chosen state yields the required owner path,
and (4.5) gives exact lower-colour recycling. \(\square\)

### 4.3 Fully coupled cuts and orientations

When ejection cuts are variables, fragment identities depend on the solution.
Pre-enumerating fragments is then unnecessary and awkward.  The owner-arc
system (2.1)--(2.6), with cuts derived by (3.1), is the exact compact logical
model.  Degree equations automatically make every surviving run of factor
edges coherently oriented, so the fragments are recovered after solving.

## 5. Residual Hall and matroid projections

Let \(P\) be a prescribed common-independent directed forest, including all
fixed provider seams and every factor arc needed by its banked blocks.  Put

\[
                    p=|P|,\qquad q=N-1-p.          \tag{5.1}
\]

After contracting \(P\), exactly \(q+1\) tail classes, \(q+1\) head classes,
and \(q+1\) colour classes remain free.  Every residual candidate arc gives
a triple

\[
              (\text{free tail},\text{free head},
               \text{free colour}).               \tag{5.2}
\]

The following tests are rigorous necessary conditions for completion and are
small enough to separate inside an all-target CEGAR.

### 5.1 Exact middle-level incidence-flow theorem

Let

\[
                         B=(U,L;E_0)
\]

be a finite bipartite graph; labelled parallel edges are allowed and are
counted with multiplicity.  Let \(b_v\) be a nonnegative desired degree at
every vertex, and let \(R\subseteq E_0\) be a forced incidence set.

#### Theorem 5.1 (forced bipartite degree completion)

There is an edge set \(S\) such that

\[
                  R\subseteq S\subseteq E_0,\qquad
                  \deg_S(v)=b_v\quad(v\in U\cup L) \tag{5.3}
\]

if and only if

\[
 \deg_R(v)\le b_v\quad(v\in U\cup L),\qquad b(U)=b(L), \tag{5.4}
\]

and, for every \(X\subseteq U\) and \(Y\subseteq L\),

\[
 \boxed{
 b(X)+|R\cap E_0(U\setminus X,Y)|
       \le b(Y)+|E_0(X,L\setminus Y)|.}            \tag{5.5}
\]

#### Proof

Delete \(R\), put \(d_v=b_v-\deg_R(v)\), and give every residual edge
\(E_0\setminus R\) capacity one.  Form the network

\[
s\longrightarrow U\longrightarrow L\longrightarrow t
\]

with capacities \(d_u,1,d_\ell\), respectively.  Conditions (5.4) say that
the residual demands are nonnegative and have equal total.  A set \(S\) in
(5.3) is exactly an integral flow saturating every \(s\to u\) arc.

The cut with source side \(\{s\}\cup X\cup Y\) has enough capacity exactly
when

\[
 d(X)\le d(Y)+|(E_0\setminus R)(X,L\setminus Y)|. \tag{5.6}
\]

Expanding \(d=b-\deg_R\), using

\[
\deg_R(X)=|R(X,Y)|+|R(X,L\setminus Y)|
\]

and

\[
\deg_R(Y)=|R(X,Y)|+|R(U\setminus X,Y)|,
\]

cancels the two other forced-edge terms and turns (5.6) precisely into
(5.5).  Max-flow/min-cut and flow integrality prove both directions.
\(\square\)

For the middle-level incidence graph, \(U\) is the owner shore and \(L\) is
the lower-colour shore.  A physical Johnson edge of colour \(c\), joining
owners \(u,v\), contributes the two incidences \((u,c),(v,c)\).  The factor
case has \(b_v=2\) on both shores.  For a spanning path cover use

\[
       b_u=2-p_u,\qquad b_c=2(1-z_c),\qquad
       \sum_u p_u=2,\quad\sum_c z_c=1,             \tag{5.7}
\]

where the two \(p\)'s mark the owner endpoints and \(z\) marks the omitted
lower colour; all \(p_u,z_c\) are binary.  Both shores then have total demand
\(2N-2\).

If protected/provider choices force incidences, let \(g_e\) be their exact OR
indicator: repeated reasons for forcing one incidence still contribute only
one unit.  Replacing the forced-set cardinality in (5.5) by

\[
              \sum_{e\in E_0(U\setminus X,Y)}g_e
\]

gives a linear, branch-independent Benders row, even with the variable
demands (5.7).  Explicitly, the path-cover row is

\[
 \boxed{
 2|X|-p(X)+\sum_{e\in E_0(U\setminus X,Y)}g_e
 \le 2|Y|-2z(Y)+|E_0(X,L\setminus Y)|.}
\]

This row is exact for the incidence-completion subproblem when \(E_0\) is a
fixed catalogue.  If \(E_0\) has already been filtered by a chosen history or
collar state, the row has only that guarded scope.

An integral solution of (5.3) with (5.7) projects to one undirected Johnson
path component plus zero or more cycle components: every colour node has
degree two or zero, every owner has degree two except the two endpoints, and
all owners occur.  Graphic subtour rows are still required to eliminate the
cycles and obtain a Hamilton path; with incidence variables \(f_e\), the
exact lazy forest rows are

\[
                \sum_{e\in E_0[Z]}f_e\le |Z|-1
\]

for every nonempty active incidence-vertex set \(Z\).  Moreover, the
incidence projection does
not encode which directed seam/collar option realizes an owner--colour pair.

Equivalently, for fixed endpoints and hole, put the upper degree capacities
\(b_u\) and lower degree capacities \(b_c\) into two partition matroids on
the incidence ground, and take the graphic matroid of \(B\).  A forced
target-size common independent set of size \(2N-2\) saturates both degree
systems and, by graphic independence, is exactly the expanded Hamilton path.
Dropping the graphic matroid leaves the two-partition problem solved by
Theorem 5.1; this is precisely where the TU/max-flow reduction ends.

Direction, paired-seam legality, residence, and upper-witness constraints
remain in the full arc lift (2.1)--(2.6).  This distinction is real: on the
restricted owner path \(A-B-C-D\), the directed requirements \(B\to A\) and
\(C\to D\) pass the undirected degree/colour/forest projection, but neither
global orientation of the path retains both.

### 5.2 Eager protected-source colour row

Let \(\kappa_c\) be the OR that at least one selected guard or target block
forces retention of the unique source-factor edge \(e_c\).  Encode the OR
exactly from the relevant \(g_\rho,y_w\) variables.  Colour independence
gives the eager row

\[
 \boxed{\kappa_c+
   \sum_{a\in G\setminus\vec E(F):\chi(a)=c}x_a\le1}
       \qquad(c\in\mathcal C).                    \tag{5.8}
\]

This is stronger and earlier than waiting for the full incidence flow:
banking a source edge of colour \(c\) immediately forbids every service or
return seam of colour \(c\).  It is a central audit row for the reported 512
fragile banks.

### 5.3 Pairwise matching ranks

Project (5.2) onto tail--head, tail--colour, and colour--head.  Each projected
bipartite graph must have a matching of size at least \(q\).  Equivalently,
because each shore has size \(q+1\), every subset \(X\) of either first shore
must satisfy the one-deficient Hall inequalities

\[
                         |N(X)|\ge |X|-1.           \tag{5.9}
\]

A violated row is an exact max-flow/Benders certificate.  Safety filters may
only delete projected incidences, so failure in the unrestricted Johnson
projection is final for that prescribed partial set.

Indeed, a common extension projects to a matching in each graph.  Conversely,
the maximum matching in a bipartite graph with \(q+1\) vertices on the first
shore has size at least \(q\) exactly when its maximum Hall deficiency
\(\max_X(|X|-|N(X)|)\) is at most one, which is (5.9).  The converse here is
only for the individual projection, not for simultaneous realization of all
three projected matchings by the same seams.

### 5.4 Exact colour-connectivity projection

Contract the components of the undirected forest \(P\) and delete its used
colours.  Ignoring tail/head directions, a rainbow spanning-tree extension
exists if and only if every partition \(\Pi\) of the contracted vertices
satisfies

\[
 |\{\text{unused colours on candidate edges crossing }\Pi\}|
                         \ge |\Pi|-1.               \tag{5.10}
\]

This is the graphic/colour matroid-intersection theorem.  It is exact for
rainbow connectivity, but only necessary for a directed Hamilton path.

### 5.5 Four-rank cuts

For every partition of the residual candidate ground set

\[
 A=A_{\rm out}\mathbin{\dot\cup}A_{\rm in}
   \mathbin{\dot\cup}A_{\rm col}\mathbin{\dot\cup}A_{\rm gr},
\]

a common extension of size \(q\) requires

\[
 r_{\rm out}(A_{\rm out})+r_{\rm in}(A_{\rm in})+
 r_{\rm col}(A_{\rm col})+r_{\rm gr}(A_{\rm gr})\ge q. \tag{5.11}
\]

Neither all three pairwise matchings nor (5.10)--(5.11) are sufficient for
the four-way problem.  They are proof-safe filters, not a replacement for
the common-independence recourse.

## 6. Why an ordinary flow is not the exact theorem

For fixed fragments, each seam column has one coefficient in an exit row,
one in an entry row, and one in a colour row.  Deleting the colour rows gives
a bipartite matching/flow; deleting either endpoint family gives another
bipartite matching.  Retaining all three is a three-partition matching
problem.  The graphic rows then exclude directed cycle components.

All four resources are physically necessary:

* without the colour rows, endpoint-disjoint seams may repeat one lower
  colour;
* without one endpoint family, branching or coalescing is possible; and
* without graphic independence, a rainbow degree cover may contain a
  directed cycle.

No claim is made here that a particular determinant-two minor occurs in the
Johnson catalogue.  The proved obstruction is structural: an exact directed
seam column simultaneously consumes three partition resources, and degree
feasibility does not imply connectivity.  Theorem 5.1 is an exact flow only
for the undirected incidence-degree projection.  A flow reduction of the
directed seam problem becomes exact only under an additional factorization
hypothesis, for example full safe rectangles \(L_c\times R_c\) for every
residual colour plus a separately certified colour-preserving splice tree.

## 7. A proof-safe all-target CEGAR

The following loop is exact when the arc and witness catalogues are complete.
Before running it, the present provider-only seam master needs the following
explicit strengthenings.

* **Complete return domain.** Retain every certified safe Johnson seam which
  may be used for completion, including seams with zero immediate upper-target
  gain.  A positive-gain provider catalogue alone cannot certify recourse.
* **Lower-colour injection.** For every colour \(c\), impose
  \[
       \sum_{a\text{ seam}:\chi(a)=c}x_a\le1,
       \qquad
       \sum_{a\text{ seam}:\chi(a)=c}x_a\le c_c.   \tag{7.1}
  \]
  If a banked block protects the source edge of colour \(c\), use the stronger
  OR-row (5.8).  In the final completion these inequalities tighten to (3.2).
* **Physical-edge antisymmetry.** Treat the two orientations of one physical
  edge as parallel choices and impose
  \(x_{u\to v}+x_{v\to u}\le1\).  Every forced-incidence guard is the OR of
  physical requirements, not their arithmetic sum.
* **Ejection permission.** In a frozen-orientation master, selected seams
  imply their endpoint cuts, but one must not impose an upper bound saying
  that every cut is caused by an already selected provider endpoint.  Such an
  upper bound forbids extra ejection cuts by construction.
* **Reorientation permission.** To expose the full escape, include both
  orientations of every optional factor edge and derive physical cuts by
  (3.1).  A canonical-successor-only master proves results only in the frozen
  orientation.
* **Complete target alternatives.** A casualty row must allow every certified
  old surviving interval and every enumerated new seam/compound interval.
  Requiring one old factor witness is a sound restricted bank, not a complete
  all-target row.  A target automaton or a whole-candidate no-good is the
  fail-closed fallback.
* **Literal bank export.** Persist the identity of every banked target, the
  selected witness column, and the exact OR-union of all forced physical
  incidences.  A count of banked rows is not a recourse certificate.
* **Upper-\(q_1\) persistence.** Either export one selected physical witness
  for every rank-\((r+1)\) target or retain the exact pair/union rows in the
  completion model.  A current uncut-edge BoolOr does not survive an arbitrary
  downstream b-flow.

1. **Master/provider layer.** Choose provider and banked-witness variables
   \(y_w\).  Do not freeze every currently uncut factor edge; doing so would
   remove the ejection/reorientation escape.
2. **Common-independence recourse.** Solve (2.1)--(2.3) and (2.5)--(2.6),
   initially omitting (2.4), and separate the graphic rows lazily.
   Incidence-flow rows (5.5), pairwise matching ranks (5.9), and
   coloured partition rows (5.10) are useful eager or separated cuts.
3. **Connectivity separation.** Replay the selected arcs.  For each directed
   cycle \(C\), add
   \[
                         \sum_{a\in C}x_a\le |C|-1.
   \]
   A cyclic solution of the incidence-flow projection alone does not justify
   a no-good on its provider selection: another incidence completion may be
   acyclic.  Promote the completion variables and add lazy forest rows, or
   prove exact connected recourse before cutting the master.
4. **Upper separation.** Replay arbitrary-width consecutive unions on the
   completed path.  For every missing target \(T\), add its complete guarded
   row (2.6), or a sound candidate no-good if complete block enumeration is
   deferred.
5. **Residence separation.** Replay coordinate runs.  A failed run yields a
   forbidden directed-block row or a guarded collar requirement.  Arc-local
   safety without its collar is not sufficient.
6. **Proof replay.** Only a connected literal path passing all upper/lower,
   residence, staircase/compiler, and final word audits is a positive
   certificate.

If a fixed selected witness subset \(Y_0\) already has no four-matroid
extension, extension feasibility is monotone under prescribing more arcs.
Hence

\[
                       \sum_{w\in Y_0}y_w\le |Y_0|-1 \tag{7.2}
\]

is a valid master no-good, provided the recourse proof used the global fixed
arc catalogue rather than a cut-dependent restricted catalogue and proved
failure of the full connected recourse—not merely cyclicity of one b-flow
solution.  Deletion-minimal assumption cores give the strongest rows of this
form.

## 8. Consequence for the reported all-target incumbent

### 8.1 The 2,320-seam round is metrics-only

The frozen run log reports for round zero:

```text
2320 run-safe seams
3636 canonical cuts
all 1838 original holes served
reported upper holes 1121 = rank11^818 rank12^290 rank13^13
no rank10 loss
512 old-witness rows added before round 1
```

The producer did not persist the round-zero seam, cut, witness, or hole
arrays.  Those figures are therefore authenticated solver-log metrics, not a
literal incumbent certificate.  Their edge-count identity is

\[
 (N-3636)+2320=N-1316,
\]

so any such partial cover satisfies \(H-E=1316\), not lower-\(q_1\)
exactness.  The phrase “\(q_1\) exact” in this lane means **upper** rank-ten
coverage.  The conditional 1,315-return conclusion of Corollary 3.1 applies
only if the unexported retained set is already tail-, head-, colour-, and
graphic-independent.  That cannot be audited from the log.

### 8.2 Independent replay of the persisted round-three selection

The final quick-four-round artifact is available and was replayed without
the producer or OR-Tools.  Its frozen provenance is

```text
source components SHA-256
  3f663cd2117ad6096b4cc9e6bc9d6fcf881382b4ee546dc64219bf94aafd5f2e
producer SHA-256
  e31d0a52416e9f61e01daa80dda1b9f64ae7222519428d61eb387879a39fac7d
result SHA-256
  d439747e96c4ae1609d0b3f3c4a4e96c116a6ec478dbba7eb740ff2a327d2b39
result payload
  574e89a01e53a934a243502682289b37e49d60af873cca1f05de89743b960d11
run-log SHA-256
  e30b9f178d873c0445d37fc2506e1e6999bb01010203fa9b04aa1443927f6e0c
```

The persisted selection has 1,813 locally run-safe Johnson seams, 2,748
canonical cuts, and 6,758 exported protected source tails.  Its literal
partial successor graph consists of 935 paths and the untouched source
3-cycle

\[
                  (59957,92725,125489).
\]

All 1,838 original holes are served.  Unlimited-width interval replay agrees
exactly with the producer's capped replay and leaves 650 upper holes,

\[
                       11^{474}12^{167}13^9,
\]

with zero rank-ten holes.  Thus the upper statement is genuine for this
persisted partial graph.

The lower ledger is not close to a retained common-independent set.  Its
23,375 partial edges use only 22,177 colours:

\[
             H=2133,\qquad E=1198,\qquad H-E=935.
\]

The selected seams alone use only 1,766 colours for 1,813 arcs, forcing 47
repeats.  More strongly, the exported forced bank—those seams plus the 6,758
protected source edges—is an 8,571-edge owner-degree-two graphic forest but
has 432 overfull lower colours and colour-repeat excess 435.  Its exact
collision profile

\[
 (\text{seam multiplicity},\text{protected-source multiplicity})
   =(1,1)^{387}(2,0)^{42}(2,1)^1(3,0)^2.          \tag{8.1}
\]

Consequently no lower-rainbow factor or path can contain that whole exported
bank.  At least 435 forced physical edges must be released merely to make the
bank colour-simple.  For the entire current partial graph the incidence
ledger requires at least 1,198 deletions and 2,132 missing-colour additions;
the untouched 3-cycle adds one topology cut, giving the audit's combined
lower bounds 1,199 deletions and 2,133 additions.  These are necessary
incidence/topology counts, not a constructive repair.

### 8.3 Export and model gaps exposed by the replay

The quick run records 2,048 added casualty targets, but the final solve had
enforced only the first 1,536; the last 512 were added after round three and
never solved.  More importantly, the producer never decodes or exports the
selected `retain_*` old-witness columns.  Its `protected_tails` field contains
only original-hole witness tails and local seam-run supports, not the banked
old-target intervals.  The downstream forced-incidence set is therefore
incomplete.

Likewise, the eager upper-\(q_1\) BoolOr rows do not export which physical
rank-ten witnesses must survive a later b-flow.  Casualty rows allow only old
factor witnesses, although a new seam/compound interval might re-cover the
same target; that banking is sound but not complete.  Finally, the producer
contains neither lower-colour rows nor reverse factor arcs, deletes every
zero-gain return seam, and imposes `cut <= sum(cutters)`, which forbids extra
ejection cuts.  It also lacks an explicit opposite-orientation physical-edge
AMO, although the persisted round-three selection happens to contain no such
pair.

The first exact next CEGAR step is therefore not a blind completion of either
logged partial state.  It is to add (5.5) and (5.8) over exact OR guards,
persist every selected bank, retain upper-\(q_1\) pair witnesses, and allow
zero-gain returns, ejections, and reverse factor arcs.  The current round-three
bank itself must be released or reselected because (8.1) is already a strict
lower-colour obstruction.

## 9. Reproducible audit artifacts

```text
scratch/threadD_k17_alltarget_residual_completion_20260731/producer.py
  SHA-256 e31d0a52416e9f61e01daa80dda1b9f64ae7222519428d61eb387879a39fac7d
scratch/threadD_k17_alltarget_residual_completion_20260731/result_quick.json
  SHA-256 d439747e96c4ae1609d0b3f3c4a4e96c116a6ec478dbba7eb740ff2a327d2b39
  payload 574e89a01e53a934a243502682289b37e49d60af873cca1f05de89743b960d11
scratch/threadD_k17_alltarget_residual_completion_20260731/run_quick.log
  SHA-256 e30b9f178d873c0445d37fc2506e1e6999bb01010203fa9b04aa1443927f6e0c
scratch/audit_k17_fragment_seam_setcover_incumbent_independent_20260731.py
  SHA-256 1b836aaa2061672afc8b64de899f904f41d308209ad86eea66ba9eb751f82a3f
scratch/threadD_k17_alltarget_residual_completion_20260731/independent.audit.json
  SHA-256 c71959e0c509f77b31d2063ef26b7cbacb34e10d5b2f23f247032f2ecf546a0e
  payload bbd642c5397fec16b94ec3d089a596e56c721fdaa708d7446c0dda924e43737e
```

The independent replay runs in under one second and below 100 MB resident
memory.  It imports neither the producer nor a solver.

## 10. Sharp remaining theorem gate

The uniform missing lemma is not a scalar “many providers” statement.  It is
a guarded four-matroid extension theorem guaranteeing a target-size common
independent set after simultaneous provider selection, ejection closure, and
fragment reorientation, with enough literal Johnson expansion to pass
(5.5), (5.8)--(5.11), and the final subtour rows.  The current K17 data do
not prove such a lemma, and this note makes no claim that
\(\nu(17)=B(17)\).
