# Thread AD: cut-aware chronology trees, foreign-entry TU cuts, and Hall-29 address pins

Date: 2026-07-28

Status: pure-mathematical theorem package.  The residual transportation
criterion, the signed-ledger and two-matroid obstructions, and the
tree-gated sufficient theorem are proved.  A restricted laminar
matroid-intersection regime is proved.  The final \(29\) new
\(k=15\) addresses are characterized as concrete decorated occurrence
pins; they are not constructed here.

## 0. Outcome

The cut-aware joining theorem and the fixed-tree TU theorem compose, but
not as one unrestricted matroid-intersection or branching problem.

There are four exact conclusions.

1. Once a connector tree and concrete named-address traversals have been
   chosen, the remaining successor-pairing problem is still a bipartite
   transportation problem.  Its nonemptiness is not automatic.  Besides
   nonnegative residual margins, the exact missing inequalities are the
   foreign-entry cuts

   \[
   \boxed{
   p(X)+\ell\bigl((L\setminus X)\times N(X)\bigr)
   \le q(N(X))
   \qquad(X\subseteq L).}
   \tag{0.1}
   \]

   Here \(\ell\) is the combined integer lower-bound vector of the
   chronology tree and the named-address pins.

2. The exact joining ledger

   \[
   m_S-d_S+a_S\ge1
   \tag{0.2}
   \]

   is not hereditary.  Two occurrence-disjoint rank-four switches already
   give a support-safe pair for which neither singleton is support-safe.
   Hence the exact signed ledger cannot itself be the second matroid in an
   ordinary graphic-matroid intersection.

3. Even after all additions are ignored, the master is naturally

   \[
   \boxed{
   \text{component graphic base}
   \ \cap\
   \text{physical-port matching}
   \ \cap\
   \text{label \(b\)-matching}
   \ \cap\
   \text{foreign-entry cuts}.}
   \tag{0.3}
   \]

   A four-option occurrence-level example violates \(2\)-extendibility
   even though its component catalogue is itself a tree.  Thus the
   deletion-only system is not the intersection of two matroids on the
   natural option ground set.

4. There is nevertheless a usable positive regime.  Preassign every named
   address witness, contract any mandatory joining forest, and suppose the
   remaining options each force one allowed turn and all occurrence,
   deletion-budget, local-margin, and foreign-entry option classes form one
   laminar family.  Those side conditions form a laminar matroid.  A common
   independent set of size \(c-1\) with the component graphic matroid is a
   safe chronology tree, and (0.1) gives an integral residual flow.

For the peeled Hall-29 kernel, the positive certificate must name one
actual realizing cell for each of the \(35\) residual targets.  At most six
can be old unreserved cells, so at least \(29\) must be genuinely new
physical addresses.  Merely giving a tree edge address weight \(29\), or
appending an arbitrary address-colour row to the transportation matrix,
does not prove this.

## 1. Fixed lower bounds in the allowed-turn transportation graph

Let

\[
B=(L,R;A)
\tag{1.1}
\]

be a finite bipartite graph.  The two shores are source and target copies
of the allowed-turn types.  Let

\[
p=(p_u)_{u\in L},
\qquad
q=(q_v)_{v\in R}
\tag{1.2}
\]

be nonnegative integral margins with

\[
p(L)=q(R).
\tag{1.3}
\]

Forbidden turns have already been deleted from \(A\).  For
\(X\subseteq L\), write

\[
N(X)=\{v\in R:uv\in A\text{ for some }u\in X\}.
\tag{1.4}
\]

Let

\[
\ell=(\ell_{uv})_{uv\in A}\in\mathbb Z_{\ge0}^{A}
\tag{1.5}
\]

be mandatory turn multiplicities.  In the intended application,
\(\ell\) is the union of:

* turns forced by the chosen chronology support tree;
* turns forced by already selected joining operations; and
* concrete decorated traversals which complete named physical cells.

The word “concrete” is essential.  A lower bound is put on one actual
decorated traversal type, including its occurrence anchor or absolute
phase, not on an assertion that some member of an arbitrary colour class
will eventually be used.

### Theorem 1.1 (foreign-entry cut theorem)

There is a nonnegative integral turn vector \(w\) satisfying

\[
w_{uv}\ge\ell_{uv},
\tag{1.6}
\]

\[
\sum_{v:uv\in A}w_{uv}=p_u
\qquad(u\in L),
\tag{1.7}
\]

\[
\sum_{u:uv\in A}w_{uv}=q_v
\qquad(v\in R)
\tag{1.8}
\]

if and only if both of the following hold.

First, every residual margin is nonnegative:

\[
\ell(\delta^+(u))\le p_u
\qquad(u\in L),
\tag{1.9}
\]

\[
\ell(\delta^-(v))\le q_v
\qquad(v\in R).
\tag{1.10}
\]

Second, for every \(X\subseteq L\),

\[
\boxed{
p(X)+
\ell\bigl(A\cap((L\setminus X)\times N(X))\bigr)
\le q(N(X)).}
\tag{1.11}
\]

Whenever these conditions hold, the residual polyhedron is integral.
Suppose additionally that \(L,R\) are copies of one type set
\(\mathcal T\), every edge of \(A\) is an allowed successor turn, and,
for fixed first and last types \(e_{\rm in},e_{\rm out}\),

\[
p_t-q_t
=\mathbf1_{\{t=e_{\rm in}\}}-\mathbf1_{\{t=e_{\rm out}\}}
\qquad(t\in\mathcal T),
\tag{1.12}
\]

with zero imbalance in the cyclic case.  If the mandatory support, after
the two copies of each type are identified, connects all positive types,
then every such \(w\) has connected support and spells one Euler
chronology.

#### Proof

Subtract the lower bounds and put

\[
p'_u=p_u-\ell(\delta^+(u)),
\qquad
q'_v=q_v-\ell(\delta^-(v)).
\tag{1.13}
\]

Equations (1.9)--(1.10) say exactly that \(p',q'\) are nonnegative.
Their totals agree because every unit of \(\ell\) is subtracted once from
each shore.

The residual transportation problem on \(B\) is feasible if and only if

\[
p'(X)\le q'(N(X))
\qquad(X\subseteq L).
\tag{1.14}
\]

Indeed, this is the ordinary source-shore max-flow cut criterion.  Its
coefficient matrix is the node-edge matrix of a bipartite graph, so
integral margins give an integral solution.

Every edge leaving \(X\) ends in \(N(X)\).  Therefore

\[
\ell(L\times N(X))-\ell(X\times R)
=
\ell((L\setminus X)\times N(X)).
\tag{1.15}
\]

Substituting (1.13) into (1.14) and applying (1.15) gives exactly
(1.11).

Finally, \(w\ge\ell\).  If the projected support of \(\ell\) connects all
positive types, so does the support of \(w\).  Under the displayed
imbalance hypothesis, the directed Euler-trail criterion then gives one
chronology. \(\square\)

In the linear safe-de-Bruijn application the margins are exactly

\[
p_t=z_t-\mathbf1_{\{t=e_{\rm out}\}},
\qquad
q_t=z_t-\mathbf1_{\{t=e_{\rm in}\}},
\tag{1.16}
\]

while in the cyclic application \(p=q=z\).  Thus the added Euler
hypothesis is part of the audited endpoint ledger, not a new existence
condition.

The left side of (1.11) has a useful interpretation.  Mandatory turns
from \(X\) into \(N(X)\) consume one source and one target unit inside the
same Hall shore, so they cancel.  Only mandatory turns entering \(N(X)\)
from outside \(X\) consume target capacity which \(X\) may need.  They are
the foreign entries.

### Proposition 1.2 (smallest flow-side obstruction)

Let the type set be \(\{1,2\}\), with cyclic margins

\[
p_1=p_2=q_1=q_2=1,
\tag{1.17}
\]

and allowed turns

\[
1\to1,\qquad 1\to2,\qquad 2\to2.
\tag{1.18}
\]

Force the turn \(1\to2\) once:

\[
\ell_{12}=1.
\tag{1.19}
\]

This turn connects the two underlying types and satisfies every local
margin inequality (1.9)--(1.10), but no residual transportation exists.

#### Proof

Take \(X=\{2\}\).  Then \(N(X)=\{2\}\), and the mandatory turn
\(1\to2\) is a foreign entry.  Thus (1.11) reads

\[
1+1\le1,
\]

which is false.  Equivalently, after forcing \(1\to2\), source \(2\)
still needs to send one unit, target \(1\) still needs to receive one unit,
and the forbidden turn \(2\to1\) is the only possible repair.

Among initially feasible allowed-turn systems, one underlying type has no
nontrivial connector choice, and nonnegative residual margins suffice.
Hence two types are minimal in that scope.
\(\square\)

Proposition 1.2 is the smallest reason that “choose any support tree and
invoke TU” is false.  The TU theorem remains exact inside each fixed
nonempty fibre; (1.11) decides whether that fibre is nonempty.

## 2. The faithful tree-to-flow interface

The two tree theorems concern different ledgers and must be joined through
an occurrence-faithful interface.

Start with a finite family

\[
\mathcal C=\{C_1,\ldots,C_c\}
\tag{2.1}
\]

of transition or Euler components.  Initially there is exactly one path
component and the remaining components are cycles, or all components are
cycles in the cyclic case.  Every contact option below is a safe
pair--pair switch between two of these components.  A contact option
\(e\) records:

1. two distinct component endpoints;
2. the actual physical pair occurrences \(P_e\) which it consumes;
3. its exact signed protected-label vector

   \[
   \Delta_e(S)=a_e(S)-d_e(S);
   \tag{2.2}
   \]

4. the resulting fixed decorated type data after the switch is made; and
5. a nonnegative integer lower-bound vector

   \[
   \lambda^e\in\mathbb Z_{\ge0}^{A}
   \tag{2.3}
   \]

   on concrete decorated turns which realizes that contact in the
   successor-pairing graph.

A package is called **faithful** when all five records refer to the same
named physical occurrences, occurrence-disjoint switches commute, the
displayed \(\Delta_e\) is the actual additive final ledger, and every
owner, residence, lower-trace, upper-trace, and endpoint requirement has
already been absorbed into a fixed integral decorated type vector or a
genuine node-split network margin.

All residual connector columns are neutral for this protected-label
ledger.  Any nonneutral owner, trace, or cell emission is placed on a
fixed-count decorated traversal edge before the transportation step.

The post-switch decorated graph must also delete, exhaust, or put
capacity zero on the consumed old named pairings.  A residual flow is not
allowed to reuse a half-edge occurrence already consumed by a selected
switch.

In particular, the last clause forbids appending arbitrary owner,
trace-colour, or address rows to the transportation matrix and then
claiming TU.  Such rows are exactly outside the proved fixed-tree TU
scope.

Let \(\ell^0\) contain all fixed internal turns and all preassigned named
cell witnesses.  For \(Y\) a set of contact options, put

\[
\ell(Y)=\ell^0+\sum_{e\in Y}\lambda^e.
\tag{2.4}
\]

The data are required to distinguish named units whenever two summands in
(2.4) use the same turn type.  Thus the addition counts genuine required
occurrences, not aliases of one occurrence.

### Theorem 2.1 (tree-gated TU occurrence theorem)

Assume a faithful package and a set \(Y\) of contact options satisfying:

1. the component edges of \(Y\) form a spanning tree on \(\mathcal C\);
2. the consumed occurrence sets are disjoint:

   \[
   P_e\cap P_f=\varnothing
   \qquad(e\ne f\in Y);
   \tag{2.5}
   \]

3. every protected label survives:

   \[
   \boxed{
   m_S+\sum_{e\in Y}\Delta_e(S)\ge1
   \qquad(S\text{ protected});}
   \tag{2.6}
   \]

4. the fixed integral decorated type vector has the prescribed owner,
   residence, lower, upper, and endpoint projections;
5. its successor margins are exactly (1.16), or \(p=q=z\) cyclically;
6. the lower bound \(\ell(Y)\) satisfies (1.9)--(1.11); and
7. the fixed internal support together with the connector support selected
   by \(Y\) spans all positive decorated types.

Then there is one integral connected decorated occurrence flow.  Its
Euler order:

* executes the joins on distinct physical occurrences;
* retains every protected label;
* preserves every fixed owner, residence, lower-trace, upper-trace, and
  endpoint multiplicity;
* contains every concrete named-cell witness in \(\ell^0\); and
* spells one literal erosion chronology and its contiguous-OR word.

#### Proof

Root the component tree at the component containing the global path, or at
an arbitrary component in the cyclic case.  Execute its occurrence-level
switches from the leaves inward.  Condition (2.5) ensures that no later
switch asks for an occurrence removed earlier.  The standard pair-switch
topology joins one cycle to the current component at every step and leaves
one path, or one cycle in the cyclic case.

Because the occurrence records are disjoint, their label changes add.
The final multiplicity of \(S\) is the left side of (2.6), so every
protected label remains.

After these discrete choices, all type counts and mandatory decorated
turns are fixed.  Conditions (1.9)--(1.11) and Theorem 1.1 give an integral
residual transportation flow above \(\ell(Y)\).  Condition 7 makes its
support connected.  Euler's theorem therefore orders all occurrences into
one chronology.

Every non-turn projection was frozen in the integral decorated type vector
or on a mandatory node-split traversal edge, so reordering the connector
flow changes none of it.  A named-cell pin records its full bounded memory,
physical identifier, controller footprint, and anchor or absolute phase.
Traversing its pinned edge therefore completes that exact cell.  The
erosion and fixed-skeleton theorems then give the literal word.
\(\square\)

The theorem is a finite certificate theorem.  It does not assert that a
faithful catalogue satisfying its hypotheses exists for the frozen
\(k=15\) carrier.

### Lemma 2.2 (durability of a concrete address pin)

Suppose a decorated turn state retains the entire source interval of a
cell \(c\), its controller footprint, and either its unique owner anchor or
its absolute phase.  If traversing an edge \(g\) emits

\[
(c,S)
\qquad\text{with}\qquad
\rho_Q(c)=S,
\tag{2.7}
\]

then every Euler completion with \(w_g\ge1\) contains the same eligible
physical occurrence \(c\) with value \(S\).

#### Proof

The stored memory fixes every trace \(Q_p\) on the interval of \(c\), so it
fixes their union.  The footprint field verifies controller activity on
that same occurrence.  The anchor or absolute phase prevents another
translation of the same local type from being credited as \(c\).
Additional turns before or after \(g\) cannot alter already stored entries
inside the completed interval. \(\square\)

This lemma is why concrete edge lower bounds preserve the fixed-tree TU
argument.  The weaker row

\[
\sum_{g:\,g\text{ might emit }c}w_g\ge1
\tag{2.8}
\]

is an additional colour row and is not automatically TU.

## 3. The exact signed ledger is not matroidal

At a rank-four owner

\[
A=\{1,2,3,4\},
\tag{3.1}
\]

a transition pair with omitted two-set \(P\) carries label \(A\setminus P\).
Disjoint omitted pairs produce a destructive switch; either cross-pairing
replaces both old labels by two mixed labels.

### Proposition 3.1 (minimal signed-ledger obstruction)

There are two occurrence-disjoint contact options \(e,f\) on the component
path

\[
C_0-C_1-C_2
\tag{3.2}
\]

with ledgers

\[
e:\quad \{12,34\}\longmapsto\{13,24\},
\tag{3.3}
\]

\[
f:\quad \{13,24\}\longmapsto\{12,34\}.
\tag{3.4}
\]

If all four displayed labels initially have multiplicity one, then

\[
\varnothing,\quad\{e,f\}
\tag{3.5}
\]

satisfy every exact support inequality (0.2), while neither singleton
does.

Consequently exact signed-budget feasibility is not hereditary, is not
the intersection of any family of matroid independence systems on the
natural option ground set, and fails branching-greedoid accessibility.
Two options and owner rank four are minimal.

#### Proof

Use four distinct transition-pair occurrences at the same owner \(A\).
Option \(e\) consumes occurrences with omitted pairs \(12,34\);
option \(f\) consumes separate occurrences with omitted pairs \(13,24\).
Choose the indicated cross-pairing for each.  Put the two occurrences for
\(e\) in \(C_0,C_1\), and those for \(f\) in \(C_1,C_2\).  The options
therefore form the component tree (3.2) and consume no common occurrence.

Selecting both options deletes and recreates every displayed label once,
so every final load is one.  Selecting only \(e\) leaves labels \(12,34\)
at load zero; selecting only \(f\) leaves labels \(13,24\) at load zero.
Thus the feasible pair has no feasible one-element deletion.

Every intersection of matroid independence systems is hereditary, and
every greedoid requires a feasible deletion from each nonempty feasible
set.  Finally, a destructive pair switch requires two disjoint omitted
two-sets, impossible in an owner of rank at most three. \(\square\)

Proposition 3.1 does not rule out a larger extended formulation with
auxiliary state.  It rules out treating the exact signed ledger itself as
one matroid or ordinary branching independence constraint.

## 4. The deletion-only relaxation still needs more than two matroids

For a destructive option \(e\), let

\[
w_e(S)=d_e(S)
\tag{4.1}
\]

on its two deleted old labels, and zero on a label-preserving option.  Put

\[
b_S=m_S-1.
\tag{4.2}
\]

The conservative support certificate is

\[
\sum_{e\in Y}w_e(S)\le b_S.
\tag{4.3}
\]

Unlike the exact signed ledger, this family is hereditary.

### Proposition 4.1 (minimal nonmatroid budget exchange)

Let \(p,q,r,s\) be four pairwise disjoint two-sets, and give each displayed
label budget one.  On the three edges of a four-component path, take
occurrence-disjoint destructive options with charge pairs

\[
g:\{p,q\},
\qquad
h:\{p,r\},
\qquad
j:\{q,s\},
\tag{4.4}
\]

where \(g\) is the middle path edge and \(h,j\) are the two outer edges.
Then

\[
I=\{g\},
\qquad
J=\{h,j\}
\tag{4.5}
\]

are budget-feasible forests and \(|I|<|J|\), but neither member of
\(J\setminus I\) augments \(I\).

Thus the deletion-budget independence system is not a matroid.  Three
ground elements are minimal for a hereditary nonmatroid.

#### Proof

The set \(I\cup\{h\}\) uses label \(p\) twice, while
\(I\cup\{j\}\) uses label \(q\) twice.  All other claimed sets respect
every unit budget and are forests.  Hence the matroid augmentation axiom
fails.

Every hereditary independence system on at most two ground elements is a
matroid, which proves minimality in ground-set size. \(\square\)

Physical occurrence packing has the same three-element obstruction.  If
three options consume consecutive pairs

\[
\alpha\beta,\qquad\beta\gamma,\qquad\gamma\delta,
\tag{4.6}
\]

then the middle singleton and the two outer options give the same failed
augmentation.  In graph language, occurrence-disjoint option sets are
matchings in the port-conflict graph.

### Lemma 4.2 (exact matroid boundary for port packing)

Let \(K\) be the conflict graph on contact options, with two options
adjacent exactly when they consume a common physical pair occurrence.
The occurrence-disjoint option sets form a matroid if and only if every
connected component of \(K\) is a clique.

#### Proof

If the components of \(K\) are cliques, an occurrence-disjoint set chooses
at most one option from each component.  This is a rank-one partition
matroid.

Conversely, if one component is not a clique, take a shortest path between
two nonadjacent vertices in it.  Its first three vertices \(x,y,z\)
induce a path.  Then \(\{y\}\) and \(\{x,z\}\) are occurrence-disjoint,
but neither \(x\) nor \(z\) augments \(\{y\}\).  Matroid augmentation
fails. \(\square\)

Thus ordinary matroid branching can absorb the physical-port constraint
only in this cluster-conflict regime.  A general bipartite port matching
is already an intersection of two partition matroids before component
connectivity or label budgets are imposed.

There is a still stronger direct obstruction to using exactly two
matroids.

### Proposition 4.3 (four-option failure of two-matroid intersection)

There is an occurrence-level rank-four catalogue of four options whose
component edges themselves form a tree, but whose conservative feasible
partial joining sets are not the intersection of two matroids on those
four options.

#### Construction

Use components \(C_0,\ldots,C_4\).  At owner

\[
A=\{1,2,3,4\},
\]

take the following pair occurrences:

\[
\begin{array}{c|c|c|c}
\text{occurrence}&\text{component}&\text{omitted pair}&\text{label}\\ \hline
\alpha&C_0&12&34\\
\beta&C_1&34&12\\
\gamma&C_2&13&24\\
\delta&C_3&24&13.
\end{array}
\tag{4.7}
\]

Let

\[
e=(\alpha,\beta),
\qquad
f=(\alpha,\gamma),
\qquad
g=(\beta,\delta).
\tag{4.8}
\]

The option \(e\) is destructive.  Choose the label-preserving crossings
for \(f,g\).

At

\[
A'=\{3,4,5,6\},
\]

take \(\eta\in C_2\) omitting \(56\), hence carrying label \(34\), and
\(\theta\in C_4\) omitting \(34\), hence carrying label \(56\).  Let

\[
h=(\eta,\theta)
\tag{4.9}
\]

be destructive.  The component edges are

\[
e=01,\qquad f=02,\qquad g=13,\qquad h=24,
\tag{4.10}
\]

which together form a tree.

Give label \(34\) exactly its two displayed occurrences
\(\alpha,\eta\), hence budget one.  Pad labels \(12\) and \(56\)
privately so that their destructive uses are affordable.

#### Proof

Put

\[
B=\{f,g,h\},
\qquad
A_0=\varnothing.
\tag{4.11}
\]

Both \(B\) and \(A_0\cup\{e\}\) are feasible.  The options \(f,g\) are
label-preserving and use different ports; \(h\) spends only one of the two
\(34\)-occurrences.

For \((B\setminus Y)\cup\{e\}\) to be feasible, \(Y\) must contain:

* \(f\), because \(e,f\) both consume \(\alpha\);
* \(g\), because \(e,g\) both consume \(\beta\); and
* \(h\), because \(e,h\) together consume both occurrences of label \(34\).

Thus every such \(Y\) has size at least three.

An intersection of two matroids is \(2\)-extendible.  Indeed, if
\(A_0\subseteq B\) are common independent sets and
\(A_0\cup\{e\}\) is common independent, then in each matroid either
\(B\cup\{e\}\) is independent or its fundamental circuit contains an
element of \(B\setminus A_0\).  Removing at most one such element for each
of the two matroids makes \(B\cup\{e\}\) common independent.

Our catalogue requires three removals, so its feasible partial sets cannot
be the intersection of two matroids. \(\square\)

Four options are minimal for a \(2\)-extendibility witness, since the
witness requires one inserted option and at least three options which must
be removed.

Propositions 4.1 and 4.3 are independent of the component branching
difficulty: the entire component option graph in Proposition 4.3 is
already a tree.  The obstruction lies in the two matching ledgers.

## 5. A restricted positive matroid-intersection theorem

The preceding obstructions identify a sharp useful restriction.  Fix all
mandatory joining switches and named address witnesses first.  Execute the
mandatory switches, contract their component forest, update every label
multiplicity, and put their concrete turn lower bounds into
\(\ell^0\).

Let the remaining component set have size \(c_0\), and let
\(\mathcal E\) be a catalogue of optional contact operations.  Assume each
\(e\in\mathcal E\):

1. is one edge of the contracted component-contact multigraph;
2. consumes a listed set of physical pair occurrences;
3. forces exactly one unit on one allowed decorated turn which, in the
   inherited faithful sense of Section 2, is the complete
   occurrence-faithful pin for this contact and joins the two support
   components represented by its component edge,

   \[
   a(e)=u_ev_e\in A;
   \tag{5.1}
   \]

4. has conservative net-loss indicator

   \[
   c_e(S)=\max\{d_e(S)-a_e(S),0\}\in\{0,1\}.
   \tag{5.2}
   \]

Positive gains from one optional operation are not credited against a
different operation.  This makes the theorem sufficient even when the
exact ledger is signed.

All standing faithful-package, safe-switch, endpoint-margin, and
occurrence-exhaustion hypotheses of Section 2 remain in force.

For a physical occurrence \(\alpha\), a protected label \(S\), and turn
types \(u,v\), define

\[
E_\alpha=\{e:\alpha\in P_e\},
\qquad b_\alpha=1,
\tag{5.3}
\]

\[
E_S=\{e:c_e(S)=1\},
\qquad b_S=m_S^0-1,
\tag{5.4}
\]

\[
E_u^+=\{e:u_e=u\},
\qquad
b_u^+=p_u-\ell^0(\delta^+(u)),
\tag{5.5}
\]

\[
E_v^-=\{e:v_e=v\},
\qquad
b_v^-=q_v-\ell^0(\delta^-(v)).
\tag{5.6}
\]

For \(X\subseteq L\), put

\[
E_X^\times
=
\{e:u_e\notin X,\ v_e\in N(X)\},
\tag{5.7}
\]

\[
b_X^\times
=
q(N(X))-p(X)
-\ell^0\bigl((L\setminus X)\times N(X)\bigr).
\tag{5.8}
\]

Discard redundant sets and constraints.  Assume every remaining capacity
is a nonnegative integer.

### Theorem 5.1 (unit-laminar common-base theorem)

Suppose the family

\[
\mathscr L=
\{E_\alpha\}\cup\{E_S\}\cup\{E_u^+\}
\cup\{E_v^-\}\cup\{E_X^\times\}
\tag{5.9}
\]

is laminar: any two of its members are disjoint or one contains the other.
Then the inequalities

\[
|Y\cap F|\le b_F
\qquad(F\in\mathscr L)
\tag{5.10}
\]

define a laminar matroid \(M_{\mathscr L}\) on \(\mathcal E\).

Let \(M_G\) be the graphic matroid of the contracted component-contact
multigraph.  A support-preserving chronology tree with an integral residual
occurrence flow exists whenever

\[
\boxed{
r_{M_G}(Z)+r_{M_{\mathscr L}}(\mathcal E\setminus Z)
\ge c_0-1
\qquad(Z\subseteq\mathcal E).}
\tag{5.11}
\]

#### Proof

A laminar family with integral upper capacities defines a laminar matroid,
so (5.10) is one matroid independence system.  The matroid-intersection
min--max theorem says that (5.11) is equivalent to a common independent
set \(Y\) of size \(c_0-1\).

Independence in \(M_G\) makes \(Y\) a forest.  A forest of size
\(c_0-1\) on \(c_0\) component vertices is a spanning tree.
The \(E_\alpha\) inequalities give physical-port disjointness.  The
\(E_S\) inequalities give

\[
m_S^0-\sum_{e\in Y}c_e(S)\ge1,
\tag{5.12}
\]

which implies the exact signed support inequality because all ignored
gains are nonnegative.

The \(E_u^+\) and \(E_v^-\) inequalities are exactly the local residual
margin conditions for

\[
\ell(Y)=\ell^0+\sum_{e\in Y}\mathbf1_{a(e)}.
\tag{5.13}
\]

For every \(X\), the \(E_X^\times\) inequality is exactly (1.11) after the
fixed contribution of \(\ell^0\) is moved to the right side.  Theorem 1.1
therefore supplies an integral residual transportation flow, and the
component tree makes its support connected.  Theorem 2.1 completes the
literal chronology. \(\square\)

If every optional signed coordinate already belongs to
\(\{0,-1\}\), the \(E_S\) constraints are the exact label ledger rather
than a conservative one.

The unit and laminar assumptions are substantive:

* a two-turn bundle gives weighted cut coefficients rather than matroid
  cardinalities;
* two crossing occurrence blocks give the matching obstruction (4.6);
* two crossing label blocks give Proposition 4.1; and
* crossing foreign-entry blocks need not define a matroid.

Thus Theorem 5.1 is a genuine positive regime, not a reformulation of the
general problem.

There is a simple stronger alternative to all foreign-entry bookkeeping.
If one integral reserve transportation \(w^\star\) satisfies the
coordinatewise inequalities

\[
w^\star_{uv}
\ge
\ell^0_{uv}
+|\{e\in\mathcal E:a(e)=uv\}|
\qquad(uv\in A),
\tag{5.14}
\]

then every selected tree lies in a nonempty fixed-tree fibre.  The count
is over genuine named mandatory units; two roles may be coalesced only
when they are literally the same physical occurrence.  This reservoir
hypothesis is usually wasteful but is exact and easy to audit.

## 6. The \(k=15\) Hall-29 address certificate

Retain the peeled architecture of
THREAD_H_SHORTEST_BULK_SKELETON_AND_K15_RESIDUAL_CERTIFICATE_20260728.md.
Require the \(1,489\) previously selected target--cell occurrences to be
durable fixed projections or, equivalently for this theorem, include
their concrete named witness traversals among the protected pins in
\(\ell^0\).  Thus rethreading is not allowed to repair \(R_{29}\) by
silently destroying a peeled occurrence.
Its residual target set is

\[
\begin{split}
R_{29}=\{&
89,311,449,960,1103,1920,2420,2575,2676,2932,4213,\\
&4877,4909,5801,6308,7504,8217,8218,9524,9588,10868,\\
&13616,13620,16422,17683,17738,18272,18970,19568,20516,\\
&21641,21779,24610,27760,29776\}.
\end{split}
\tag{6.1}
\]

The six old unreserved cells are

\[
C_6=
\{15899,16597,18079,18088,18090,18985\}.
\tag{6.2}
\]

Each is a length-three cell and can take only one final interval-union
value in a fixed controller word.

### Corollary 6.1 (exact 29-address co-design certificate)

Suppose a faithful decorated package chooses an injective map

\[
\psi:R_{29}\longrightarrow\mathcal C_{\rm avail}
\tag{6.3}
\]

where \(\mathcal C_{\rm avail}\) is the set of unreserved available
physical cells in the final rethreaded package; in particular the
\(1,489\) peeled reservations remain unavailable.  Suppose, for every
\(S\in R_{29}\):

1. \(\psi(S)\) is base-eligible and available;
2. its controller footprint is contained in that same physical occurrence;
3. the completed decorated memory gives

   \[
   \rho_Q(\psi(S))=S;
   \tag{6.4}
   \]

4. its owner anchor or absolute phase is recorded; and
5. a concrete traversal emitting \((\psi(S),S)\) is included in
   \(\ell^0\).

Assume also that the joining and flow hypotheses of Theorem 2.1 hold, or
that the restricted hypotheses of Theorem 5.1 hold.

Then the resulting literal word realizes every target in \(R_{29}\).
Moreover,

\[
|\psi(R_{29})\setminus C_6|\ge35-6=29.
\tag{6.5}
\]

Thus the package exposes at least \(29\) genuinely new unreserved physical
cell addresses relative to the peeled six-cell graph.

#### Proof

Theorems 2.1 or 5.1 give one integral connected decorated chronology
containing every pinned traversal.  Lemma 2.2 makes each cell
\(\psi(S)\) durable and gives its exact interval-union value \(S\).

The cells are physically distinct by injectivity.  Conversely, even
without assuming injectivity, two distinct target values could not use one
fixed cell because that cell has the unique value \(\rho_Q(c)\).  Hence
there is no residual cross-target Hall choice after the word is fixed.

Only the six cells in (6.2) are old unreserved candidates.  An injection
from \(35\) targets therefore uses at least \(29\) cells outside \(C_6\),
proving (6.5). \(\square\)

For the unpeeled Hall shore, replace (6.3) by an injection from all
\(1,524\) targets to realizing cells.  Since its old neighbourhood has
size \(1,495\), at least \(29\) selected cells must lie outside that old
neighbourhood.

Several named cells may be completed by one decorated traversal.  The
number \(29\) counts distinct physical cell identifiers, not flow units.
Conversely, \(29\) arbitrary new cells do not suffice: their exact values
must cover the targets left outside the six old cells.

No map \(\psi\) satisfying (6.3)--(6.4) is constructed here.  Corollary 6.1
turns the Hall-29 repair into a finite occurrence certificate without
claiming that certificate exists.

## 7. Precise proved boundary

The general co-design problem is not ordinary matroid intersection:

* exact signed label replenishment is nonhereditary;
* physical pair occurrences form a matching system;
* destructive labels form a second \(b\)-matching system;
* component connectivity is graphic; and
* a chosen connector tree must satisfy the foreign-entry cuts (1.11).

The strongest unconditional positive theorem in this note is Theorem 2.1:
an occurrence-disjoint support-safe tree plus all foreign-entry cuts and
concrete address pins gives one integral connected literal chronology.

Theorem 5.1 identifies a checkable ordinary matroid-intersection regime,
but its unit-laminar hypotheses are not proved for the current \(k=15\)
catalogue.  Corollary 6.1 is the exact \(29\)-address completion
certificate, not a construction of the addresses.

No Hall-zero \(k=15\) compiler, no universal length-\(6,438\) word, and no
coefficient-one theorem follows from this note.

## 8. Independent audit

Two independent audits checked the theorem package after drafting.  They
verified the foreign-entry algebra, both smallest obstructions, the
\(2\)-extendibility argument, the laminar capacities, the
matroid-intersection rank criterion, and the two Hall-29 scopes.

The audits required the following corrections, all now incorporated:

1. Connected transportation support yields an Euler chronology only with
   the exact successor-margin imbalance (1.12), or balanced cyclic
   margins.
2. The joining theorem explicitly starts with one path plus cycles, or all
   cycles, and every option is a safe pair--pair switch on named physical
   occurrences.
3. Consumed old pairings are unavailable to the residual flow, and all
   residual connector columns are neutral for the protected-label ledger.
4. The unit-laminar theorem inherits the complete faithful interface and
   requires its single pinned turn to realize the stated component contact.
5. The reserve transport must dominate the sum of all potentially
   coincident mandatory units, as in (5.14), not merely each role
   separately.
6. The peeled \(29\)-address conclusion protects all \(1,489\) earlier
   occurrences and counts addresses outside the old six-cell residual
   graph.  The stronger old-\(1,495\)-neighbourhood statement is reserved
   for the separately stated unpeeled shore.

After these corrections, neither audit found a remaining theorem-level
defect.  The audit does not assert existence of the faithful \(k=15\)
package.
