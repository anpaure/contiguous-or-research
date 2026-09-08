# Thread A: budgeted transition trees over a two-sided diamond table

Date: 2026-07-28

Status: unconditional occurrence-level joining theorem for a fixed
nonadaptive catalogue of original pair occurrences, exact integer
certificate formulation, protected-occurrence sufficient condition, and a
weighted cut obstruction.  No Hall-29 or PBBS budgeted spanning tree is
constructed.

## 0. Correction and outcome

The scalar implication

\[
 \min_S m_S\ge2
 \quad\Longrightarrow\quad
 \text{support-preserving transition joining}
\]

is false.  The verified counterexample in
MATH_DEPTH3_LOAD_TWO_JOINING_COUNTEREXAMPLE_20260728.md has minimum load
two, but each connected re-pairing destroys both occurrences of three
critical labels.

The correct object is occurrence-level.  For a proposed joining tree one
must record:

* the two actual transition-pair occurrences consumed by every join;
* the complete (lower-only or signed two-sided) label multiset deleted with
  those occurrences;
* the corresponding label multiset created by the cross-pairing; and
* the fact that no pair occurrence is consumed twice.

For a fixed nonadaptive catalogue of contacts on the original transition
pair occurrences, this note proves the exact tree certificate

\[
 \boxed{
 m_S-\sum_e d_e(S)y_e+\sum_e a_e(S)y_e\ge1
 \quad\text{for every }S,}
\tag{0.1}
\]

together with graphic connectivity and occurrence-packing constraints.
The practical destructive-budget version is

\[
 \sum_e w_e(S)y_e\le m_S-1.
\tag{0.2}
\]

Both are compatible with the two-sided diamond table: local pair switches
leave every \(R\)-row, every \(U\)-column, and every middle degree
unchanged.

The exact signed certificate is a final-state certificate.  If every
intermediate switch state must retain all labels, prefix inequalities are
also required.  The destructive-budget certificate implies those prefix
inequalities automatically.

There is also a degree-two separation.  In every exact owner 2-factor
table, including the PBBS step-two table, each middle state has degree two
and occurs once.  Its local transition pairing is forced, so distinct
table components have no same-owner contact at which re-pairing could join
them.  A degree-two-preserving physical diamond circuit, such as the
literal \(C_6\) in
THREAD_A_PBBS_TWO_SIDED_DIAMOND_MARKOV_FUSION_20260728.md, must fuse
components directly.  A budgeted contact tree becomes available only in a
table with repeated owner incidence, or one must construct a connected
degree-two table from the outset.

## 1. Contact options and their exact labels

Fix a two-sided diamond multigraph \(G_z\) and a safe local transition
system \(\tau\).  In the linear version require exactly two endpoint stubs
in total, of prescribed endpoint types; in the cyclic version require no
stubs.  Thus the transition components are respectively one path and
cycles, or cycles only.  Let

\[
 \mathcal C=\{C_1,\ldots,C_c\}
\]

be the components of its transition graph: one path and the others cycles
in the linear case, and all cycles in the cyclic case.

An incident diamond-edge copy at owner \(A\) has a two-sided port

\[
 (x,y),\qquad x\in A,\quad y\notin A,
\tag{1.0}
\]

meaning that its lower colour is \(A-x\) and its upper colour is \(A+y\).
At \(A\), a transition-pair occurrence \(\alpha\) is one local pairing
edge joining two distinguishable incident copies with ports
\((x_1,y_1),(x_2,y_2)\).  It is two-sided safe precisely when

\[
 x_1\ne x_2,\qquad y_1\ne y_2.
\tag{1.0s}
\]

Two local occurrences at opposite ends of one diamond-edge copy are
distinct occurrences; changing either local pairing does not consume the
other.  The lower and upper three-owner labels of \(\alpha\) are

\[
 S^-_\alpha=A\setminus\{x_1,x_2\},
 \qquad
 S^+_\alpha=A\cup\{y_1,y_2\}.
\]

Let

\[
 \Lambda(\alpha)=
 \{(-,S^-_\alpha),(+,S^+_\alpha)\}
\tag{1.1}
\]

be its signed label multiset.  If only the lower transition layer is under
audit, replace \(\Lambda(\alpha)\) by its negative member.  Every theorem
below is valid for either choice; in its formulas a symbol \(S\) denotes
an element of the chosen (possibly signed) target universe.

A **contact option** \(e\) consists of:

1. two distinct components \(C_i,C_j\);
2. an owner \(A\) occurring in both;
3. one actual pair occurrence \(\alpha\) in \(C_i\) and one
   \(\beta\) in \(C_j\);
4. one of the safe cross-pairings of their four half-edges.

Only pair--pair contacts are included.  Pair--stub moves, endpoint motion,
and endpoint-colour correction require a separate ledger and are not
covered here.

The option deletes the two old pair occurrences and creates two new ones.
It is admitted to the catalogue only if both new pairs satisfy (1.0s).
Let

\[
 d_e(S)=
 \operatorname{mult}_S\bigl(\Lambda(\alpha)\uplus\Lambda(\beta)\bigr),
\tag{1.2}
\]

and let \(a_e(S)\) be the multiplicity of \(S\) in the signed label
multisets of the two new pairs.  Put

\[
 \Delta_e(S)=a_e(S)-d_e(S).
\tag{1.3}
\]

Define the exact destructive charge

\[
 w_e(S)=\max\{d_e(S)-a_e(S),0\}.
\tag{1.4}
\]

On the lower shore alone, intersecting omitted-coordinate pairs admit a
label-preserving cross mode, while disjoint pairs recreate neither old
lower label.  This shortcut is not a two-sided criterion: the lower and
upper preserving modes can disagree, and an opposed port rectangle can
have no two-sided-safe cross mode.  Hence the signed catalogue and the
charges (1.2)--(1.4) must be computed from the actual four ports.

### Lemma 1.1 (opposed-rectangle contact obstruction)

Let \(x_1\ne x_2\) and \(y_1\ne y_2\).  The two individually safe pairs

\[
 \alpha=\{(x_1,y_1),(x_2,y_2)\},\qquad
 \beta =\{(x_1,y_2),(x_2,y_1)\}
\tag{1.5}
\]

have no two-sided-safe cross-pairing.  Thus a shared owner and two safe old
pairs do not by themselves create a contact edge.

#### Proof

One cross mode pairs equal \(x\)-ports and violates the lower inequality
in (1.0s).  The other pairs equal \(y\)-ports and violates the upper
inequality. \(\square\)

### Lemma 1.2 (two-shore point-degree invariance)

Every bi-safe pair--pair contact switch preserves the point-degree vector
of the lower transition-label multiset and, separately, that of the upper
transition-label multiset.

#### Proof

List the four consumed ports, with multiplicity, as
\((x_i,y_i)\), \(1\le i\le4\).  The two old lower labels and two new lower
labels use the same four \(x\)-ports, merely repartitioned into pairs.
Their summed incidence vector is therefore

\[
 2\mathbf1_A-\sum_{i=1}^4\mathbf1_{x_i}
\]

both before and after the switch.  The analogous upper sum is

\[
 2\mathbf1_A+\sum_{i=1}^4\mathbf1_{y_i}.
\]

Thus both point-degree vectors are fixed.  As the verified load-two
counterexample shows on one shore, this marginal invariant does not imply
support. \(\square\)

All data in (1.2)--(1.4) belong to actual pair occurrences, not merely to
their owner and label types.

## 2. Exact budgeted spanning-tree theorem

Let \(\mathcal E\) be any fixed catalogue of contact options on the
original local pair occurrences.  The catalogue is **nonadaptive**: no
option is allowed to consume a new cross-pair produced by an earlier
option.  For a pair occurrence \(\alpha\), write
\(\mathcal E(\alpha)\) for the options which consume it.  Let
\(\delta_{\mathcal E}(I)\) be the options joining a component in
\(I\subset\mathcal C\) to one outside \(I\).

### Theorem 2.1 (exact occurrence-level tree certificate)

Suppose there are variables

\[
 y_e\in\{0,1\}\qquad(e\in\mathcal E)
\]

satisfying

\[
 \sum_{e\in\mathcal E}y_e=c-1,
\tag{2.1}
\]

\[
 \sum_{e\in\delta_{\mathcal E}(I)}y_e\ge1
 \qquad
 (\varnothing\ne I\subsetneq\mathcal C),
\tag{2.2}
\]

\[
 \sum_{e\in\mathcal E(\alpha)}y_e\le1
 \qquad
 (\text{every pair occurrence }\alpha),
\tag{2.3}
\]

and

\[
 \boxed{
 m_S+\sum_{e\in\mathcal E}\Delta_e(S)y_e\ge1
 \qquad(\text{every transition label }S).}
\tag{2.4}
\]

Then the selected local switches join all transition components into one
path in the two-stub version (or one cycle in the zero-stub version),
preserve the complete two-sided diamond table, and retain every transition
label in the final transition system.

Conversely, fix a rigid component-contact tree and require exactly one
catalogued option to be chosen on every mandatory tree edge.  If no other
label-changing re-pairing is allowed, occurrence-disjointness (2.3) and
the final-ledger inequalities (2.4) are necessary and sufficient.

#### Proof

Equations (2.1)--(2.2) say that the selected component-contact graph is a
connected graph with \(c-1\) edges, hence a spanning tree.  In the linear
case root it at the unique path component; in the cyclic case root it at
an arbitrary cycle.  Contract edges from the leaves inward.  A nonroot
subtree is always a cycle component.  The root subtree stays a path in the
linear case and a cycle in the cyclic case.  Every contraction therefore
merges two current components and retains the required global topology.

By (2.3), no later contraction asks for a local pair occurrence removed
earlier.  Selected occurrences at different owners may involve opposite
half-edges of the same diamond-edge copy; this causes no conflict because
the switches change only the independent local pairings.  Since all
switches only re-pair the same diamond-edge copies, the table \(z\), and
therefore both of its colour shores and all middle degrees, remain
unchanged.

The signed final multiplicity of \(S\) is exactly the left side of (2.4),
because distinct consumed occurrences make the individual ledgers
additive.  Thus (2.4) is precisely final-state support preservation.

In the rigid-tree setting every tree edge is mandatory.  Once exactly one
option is chosen on each such edge, the same additive ledger is the actual
final ledger; this proves necessity and sufficiency. \(\square\)

The nonadaptive scope is essential.  A scheme which later consumes a
cross-pair created by an earlier switch requires a time-expanded ledger;
it is not represented by (2.1)--(2.4).

Likewise, (2.4) need not preserve support after every prefix of a
sequential realization.  For a chosen leaf-inward order
\(e_1,\ldots,e_{c-1}\), exact prefix safety is

\[
 m_S+\sum_{j\le t}\Delta_{e_j}(S)\ge1
 \qquad(S\text{ arbitrary},\ 1\le t\le c-1).
\tag{2.4p}
\]

Theorem 2.1 needs only the simultaneous final re-pairing.  If a monotone
physical execution is required, add (2.4p).

### Corollary 2.2 (destructive-budget sufficient condition)

Put

\[
 b_S=m_S-1.
\tag{2.5}
\]

Conditions (2.1)--(2.3), together with

\[
 \boxed{
 \sum_e w_e(S)y_e\le b_S
 \qquad(S\text{ arbitrary}),}
\tag{2.6}
\]

are sufficient for Theorem 2.1.

#### Proof

A free option has zero net label loss.  A destructive option removes the
labels charged in (1.4); all newly created labels add nonnegative slack.
Thus

\[
 \Delta_e(S)\ge-w_e(S),
\]

and (2.6) implies (2.4).  At every prefix, accumulated destructive charge
is at most its total charge, so the same estimate proves (2.4p) for every
execution order. \(\square\)

The verified load-two counterexample has three mandatory bridge options.
For its critical labels \(p,q,r\),

\[
 m_p=m_q=m_r=2,\qquad
 d_p=d_q=d_r=2,\qquad
 a_p=a_q=a_r=0.
\]

Thus (2.4) fails exactly, and (2.6) records demand two against budget one
for each label.

The system is not ordinary matroid intersection.  Occurrence-disjoint
option sets are matchings, and matchings do not form a matroid: for contact
edges \(e_{12},e_{23},e_{34}\) on four occurrence ports,

\[
 I=\{e_{23}\},\qquad J=\{e_{12},e_{34}\}
\]

have \(|I|<|J|\), but neither member of \(J\setminus I\) augments \(I\).
Thus the exact object is a matching-constrained graphic base with label
budgets (or a matroid-parity-type system), not a graphic/partition-matroid
intersection.

## 3. Protected occurrences

The budget condition has a useful certificate form.

### Corollary 3.1 (protected-occurrence spanning tree)

Choose one protected pair occurrence for every initially supported label;
the same occurrence may protect both of its signed labels, so this choice
need not be injective.  Let \(P\) be the union of the chosen occurrences.
Delete from the contact catalogue every destructive option which consumes a
protected occurrence.  If the remaining catalogue contains a spanning tree
whose options use pair occurrences distinctly, then support-preserving
joining is possible.

#### Proof

Every destructive selected option consumes only unprotected occurrences.
For each protected label, either its protected occurrence is unused, or a
selected label-preserving option consumes it and recreates the same old
label multiset.  Because the catalogue is nonadaptive, such a newly
created occurrence is never consumed later.  Thus every label survives.
Equations (2.1)--(2.3) hold for the selected tree, and Theorem 2.1 applies.
\(\square\)

This is stronger than necessary because a free join may safely replace the
identity of a protected occurrence, and labels created earlier may pay for
later joins.  Its virtue is that it is noncircular and directly
certifiable.

There is a genuine expansion theorem which produces the required protected
tree.

Fix such a protected occurrence set \(P\).  Let \(H_P\) be the graph
whose vertices are the unprotected pair occurrences and whose edges are
safe contact options between occurrences in distinct initial transition
components.  Parallel cross-pairing modes may be retained as parallel
options, but they use the same two occurrence vertices.

For a partition \(\Pi\) of the \(c\) transition components into \(b\)
blocks, let \(H_P(\Pi)\) retain only options whose component endpoints lie
in different blocks.  Write \(\nu\) and \(\tau\) for matching and minimum
vertex-cover numbers.

### Theorem 3.2 (identity-protected contact-expansion theorem)

A spanning tree contained in \(H_P\), and hence using no protected
occurrence at all, necessarily satisfies

\[
 \nu(H_P(\Pi))\ge b-1
 \qquad(\text{every partition }\Pi\text{ into }b\text{ blocks}).
\tag{3.1}
\]

Conversely, the stronger inequalities

\[
 \boxed{
 \tau(H_P(\Pi))\ge2(c-b)+1
 \qquad(2\le b\le c)}
\tag{3.2}
\]

imply that such an identity-protected, occurrence-disjoint spanning tree
exists.  It is enough to replace \(\tau\) by the stronger hypothesis
\(\nu(H_P(\Pi))\ge2(c-b)+1\).

#### Proof

Any spanning tree has at least \(b-1\) edges crossing a partition into
\(b\) blocks.  If its contact options use occurrences distinctly, those
crossing edges form a matching in \(H_P(\Pi)\), proving (3.1).

For sufficiency, build a matching forest greedily.  Suppose it currently
has \(b\) macro blocks.  It has used \(c-b\) contact options and therefore
exactly \(2(c-b)\) occurrence vertices.  If no unused option crossed the
current partition, those used vertices would meet every edge of
\(H_P(\Pi)\), forming a vertex cover of size \(2(c-b)\), contrary to
(3.2).  Add an unused crossing option.  It joins two forest blocks and
preserves the occurrence matching.  After \(c-1\) steps the quotient is a
spanning tree.  Corollary 3.1 preserves every label.

Finally \(\tau(G)\ge\nu(G)\) for every graph, so the displayed matching
lower bound implies (3.2). \(\square\)

The condition is deliberately strong.  Corollary 3.1 also permits a
label-preserving option to consume a protected occurrence and recreate its
label, whereas \(H_P\) excludes that option.  Thus (3.1) is necessary only
for the stricter identity-protected architecture, not for every
Corollary 3.1 certificate.  Unlike a scalar load floor, (3.2) tests every
macro partition and the actual reusable occurrence ports.

### Corollary 3.3 (private-bank zero-cost theorem)

Fix a spanning tree \(T\) on the \(c\) initial transition components.
Suppose every edge of \(T\) has at least \(L\) label-preserving contact
options, and for a fixed tree edge any one pair occurrence belongs to at
most \(\Delta\) of its candidate options.  If

\[
 L>2\Delta(c-2),
\tag{3.3}
\]

then \(T\) has a choice of pair-occurrence-disjoint, zero-label-cost
contacts.  Hence all components can be joined without changing the
transition-label multiset.

#### Proof

Process the \(c-1\) tree edges in any order.  Before the last choice, fewer
than \(c-1\) contacts have been chosen, so at most \(2(c-2)\) pair
occurrences are unavailable.  Each invalidates at most \(\Delta\)
candidates for the current tree edge.  Inequality (3.3) leaves an
available label-preserving option.  Induction gives distinct occurrences
on every tree edge, and Theorem 2.1 applies with \(\Delta_e=0\).
\(\square\)

## 4. A weighted contact-cut obstruction

For nonnegative label weights

\[
 \lambda=(\lambda_S)_{S},
\]

give a contact option the destructive cost

\[
 \operatorname{cost}_\lambda(e)
 =\sum_S\lambda_Sw_e(S).
\tag{4.1}
\]

Ignore occurrence collisions temporarily, and let

\[
 \operatorname{MST}_\lambda(\mathcal E)
\]

be the minimum cost of a spanning tree in the component-contact
multigraph, with value \(+\infty\) if it is disconnected.

### Proposition 4.1 (weighted necessary condition)

If the destructive-budget certificate (2.1)--(2.3), (2.6) exists, then

\[
 \boxed{
 \operatorname{MST}_\lambda(\mathcal E)
 \le\sum_S\lambda_S(m_S-1)
 \qquad(\lambda\ge0).}
\tag{4.2}
\]

#### Proof

The selected tree has weighted cost

\[
 \sum_e y_e\operatorname{cost}_\lambda(e)
 =\sum_S\lambda_S\sum_ew_e(S)y_e
 \le\sum_S\lambda_S(m_S-1).
\]

Removing the occurrence restrictions can only decrease the minimum
spanning-tree cost, proving (4.2). \(\square\)

For the verified counterexample, take

\[
 \lambda_p=\lambda_q=\lambda_r=1
\]

and all other weights zero.  Its rigid contact path has three mandatory
edges, each of cost two.  Hence

\[
 \operatorname{MST}_\lambda=6
 >3=(m_p-1)+(m_q-1)+(m_r-1),
\]

which detects the obstruction without enumerating the \(27\) local pairing
states.

Condition (4.2) is necessary only for the destructive-budget certificate,
not for a general sequence which deliberately creates labels before
reusing them.  The exact final-ledger system remains (2.1)--(2.4).

## 5. Coupling to the two-sided diamond variables

For a two-sided table \(z\), the number of incident copies at owner \(A\)
having port \((x,y)\) is exactly

\[
 h_{A;x,y}=z_{A-x,A+y}.
\tag{5.1}
\]

Let \(\mathcal P_A\) be the set of unordered two-sided-safe pairs

\[
 \pi=\{(x,y),(x',y')\},
 \qquad x\ne x',\quad y\ne y'.
\]

Choose port-resolved pair counts \(p_{A,\pi}\) and stub counts
\(u_{A;x,y}\) satisfying the exact incidence equations

\[
 \sum_{\substack{\pi\in\mathcal P_A\\(x,y)\in\pi}}p_{A,\pi}
 +u_{A;x,y}
 =z_{A-x,A+y}
 \qquad(A,x,y\text{ arbitrary}).
\tag{5.2}
\]

For \(\pi=\{(x,y),(x',y')\}\), write

\[
 S^-(A,\pi)=A\setminus\{x,x'\},
 \qquad
 S^+(A,\pi)=A\cup\{y,y'\}.
\]

The exact signed transition-load equations are

\[
 \sum_{A\in\mathcal A}
 \sum_{\substack{\pi\in\mathcal P_A\\S^\sigma(A,\pi)=T}}
 p_{A,\pi}=m_T^\sigma
 \qquad(\sigma\in\{-,+\},\ T\text{ of the corresponding rank}).
\tag{5.3}
\]

If only the lower layer is prescribed, retain only the \(\sigma=-\)
equations.  The aggregate lower equations using
\(h_{A,x}=\sum_{y\notin A}z_{A-x,A+y}\) are necessary projections of
(5.2), but are not sufficient for a two-sided transition system.

For a prescribed linear endpoint-owner vector
\(\epsilon_A\in\{0,1,2\}\), the endpoint conditions are

\[
 \sum_{x\in A,\ y\notin A}u_{A;x,y}=\epsilon_A
 \quad(A\text{ arbitrary}),
 \qquad
 \sum_A\epsilon_A=
 \sum_A\sum_{x\in A}\sum_{y\notin A}u_{A;x,y}=2.
\tag{5.2e}
\]

The actual nonzero \(u_{A;x,y}\) record the endpoint port types and must be
fixed as well when endpoint flags are prescribed.  For the cyclic version,
all \(u_{A;x,y}=0\).  No pair--stub joining move is part of the contact
catalogue.  If start and finish are distinguished, the two stub occurrence
IDs must also be marked (equivalently use oriented start/finish stub
variables) and the final path oriented accordingly.  Full rooted endpoint
collars are additional data beyond these ports.

The labels in (5.3) lie two ranks below or above their owner.  They record
the two signed three-owner, trace-\(q=2\) layers.  They do not record the
four-owner, trace-\(q=3\) layers, which need separate collar/transition
checks.

The aggregate counts \((z,p,u)\) do not determine a transition system.
One must also identify the distinguishable parallel copies of every
\(z\)-cell at both endpoints and give a local pairing \(\tau\) realizing
the counts.  The data \((z,p,u,\tau)\) determine the transition components
and the literal safe contact catalogue \(\mathcal E(z,p,u,\tau)\).

### Theorem 5.1 (budgeted two-sided diamond sufficient theorem)

Assume every required signed target has prescribed load
\(m_T^\sigma\ge1\).
A literal common order with complete two-sided diamond margins and complete
support for both signed three-owner, trace-\(q=2\) layers follows from
either of the following.  In the linear case impose (5.2e) with the
prescribed endpoint ports; in the cyclic case impose \(u=0\).

1. The data \((z,p,u,\tau)\) satisfy the two-sided table equations,
   the port-resolved equations (5.2)--(5.3), the applicable endpoint
   equations, and their transition graph is connected from the outset.
2. They satisfy those equations and the derived catalogue
   \(\mathcal E(z,p,u,\tau)\) admits the exact tree certificate
   (2.1)--(2.4) on the signed target universe, or the stronger budget
   certificate (2.6).

#### Proof

In the first case the connected transition graph itself spells the common
Euler order.  In the second, Theorem 2.1 joins it without changing \(z\)
or losing any signed transition label. \(\square\)

The theorem is an exact finite target for selecting a new two-sided table:
rankwise histogram data alone do not specify \(\tau\), the components, or
\(\mathcal E(z,p,u,\tau)\).

### Proposition 5.2 (degree-two factor tables have no contact repair)

In any exact owner 2-factor table,

\[
 d_A(z)=2
\qquad(A\in\mathcal A).
\]

Hence every owner has exactly one transition pair, belonging to exactly one
transition component.  Distinct components share no owner occurrence and
the intercomponent contact catalogue is empty.

Therefore no disconnected owner 2-factor table, including the fixed PBBS
table, can be connected by transition re-pairing alone.  A physical
factor circuit which preserves \(d_A=2\) may fuse components directly, but
it cannot unlock a later contact tree.  Theorem 2.1 becomes nonvacuous only
after introducing repeated-owner incidence (some \(d_A\ge4\)) or a
non-factor auxiliary table, unless the degree-two table is made connected
directly.

#### Proof

The two incident edge copies at an owner are forced to pair with one
another.  There is no second pair occurrence at that owner with which a
cross-pairing could be made.  Since every owner appears once, another
component has no copy of the same owner. \(\square\)

### Proposition 5.3 (owner occurrence-capacity partition obstruction)

Let \(\Pi=\{B_1,\ldots,B_b\}\) be any partition of the transition
components.  At owner \(A\), let \(t_{A,j}\) be the number of original
pair occurrences lying in components in block \(B_j\), and put

\[
 t_A=\sum_jt_{A,j},\qquad
 \kappa_A(\Pi)=
 \min\left\{\left\lfloor\frac{t_A}{2}\right\rfloor,
             t_A-\max_jt_{A,j}\right\}.
\tag{5.4}
\]

If an occurrence-disjoint contact spanning tree exists, then

\[
 \boxed{
 b-1\le\sum_A\kappa_A(\Pi)
 \qquad(\Pi\text{ arbitrary}).}
\tag{5.5}
\]

This remains only a necessary condition: safety and label budgets may
delete further contacts.

#### Proof

At least \(b-1\) edges of any component spanning tree cross \(\Pi\).  The
crossing contacts selected at one owner use distinct pair occurrences
whose component blocks differ.  Before imposing two-sided safety, the
largest block-crossing matching on \(t_{A,j}\) pair occurrences of each
block colour has size exactly

\[
 \min\left\{\lfloor t_A/2\rfloor,
             t_A-\max_jt_{A,j}\right\}.
\]

The actual bi-safe contact matching is a submatching of this complete
multipartite relaxation.  For the relaxed problem, the two displayed
quantities are upper bounds.  If one colour occupies more than half the
pair occurrences, pair every nonmajority occurrence with a majority
occurrence.  Otherwise the occurrences can be successively paired across
two currently largest colour classes, leaving at most one occurrence, and
the first bound is attained.  Summing the ownerwise maxima bounds all
crossing tree edges and proves (5.5). \(\square\)

For an owner 2-factor, \(t_A=1\) and hence \(\kappa_A(\Pi)=0\) for every
\(A\).  Thus Proposition 5.2 is also the extremal zero-capacity case of
(5.5).

This separates two operations in the PBBS lane:

1. a degree-two-preserving physical flag circuit may fuse components
   directly while retaining the \(R/U\) ledgers; or
2. a construction with repeated owner incidence may be paired by \(\tau\)
   and then certified by a budgeted contact tree.

In either case one must separately audit the four-owner \(q=3\) and longer
collars and the compiler owner-Hall extension.

## 6. Exact remaining search target

The scalar histogram, including the pattern \(2^{2577}3^{426}\), is not a
joining certificate.  The proof-safe target is one of:

* a two-sided diamond table with a connected support-safe transition
  system from the outset; or
* explicit data

  \[
  (z,p,u,\tau,\mathcal E,y)
  \]

  satisfying the table equations, (5.2)--(5.3), and
  (2.1)--(2.4).

A proof-safe finite search can therefore be staged without any histogram
shortcut:

1. certify the \(R/U\) margins of \(z\), then the full port equations
   (5.2), signed loads (5.3), and endpoint data;
2. instantiate distinguishable cell copies and \(\tau\), and compute the
   initial transition components;
3. catalogue only literal bi-safe cross modes on original pair
   occurrences, rejecting opposed rectangles by Lemma 1.1;
4. reject any owner occurrence-capacity partition violating (5.5), then
   solve the exact binary system (2.1)--(2.4) (or its
   protected/budgeted specialization);
5. replay the selected local pairings on copies, verify the final single
   path/cycle and both signed supports, and only then test the ordered
   four-owner and longer collars.

Every successful output is the finite certificate
\((z,p,u,\tau,\mathcal E,y)\); every rejection in steps 1, 3, or 4 has a
displayed algebraic witness.

For the PBBS starting table, Proposition 5.2 forces any positive route to
use direct physical component fusion, or first create repeated owner
incidence before a budgeted-tree stage can exist.  The minimum literal
degree-two-preserving fusion circuit currently available is the
common-retained-label odd \(C_6\) of
THREAD_A_PBBS_TWO_SIDED_DIAMOND_MARKOV_FUSION_20260728.md.  Its cumulative
three-owner target ledger must be audited directly.  Since it preserves
\(d_A=2\), it does not itself create a catalogue to which Theorem 2.1
could later be applied.

No existence theorem for the required connected table or budgeted tree is
proved here.  Within the finite static transition-tree subproblem, the
exact missing inequality is the feasibility of the occurrence-level
system (2.1)--(2.4), not any scalar minimum-load bound.  This is not itself
the asymptotic coefficient-one gate: opening the
\(O(\!\operatorname{Cat}_m)\) PBBS cycles costs
\(O(H\operatorname{Cat}_m)=o(W)\) in the known regime, and
\(O(\operatorname{Cat}_m)\) local joins change \(\nu_H\) by only
\(O(\operatorname{Cat}_m)\).  Residence intervals and compatible
owner-Hall extension remain separate and potentially decisive.
