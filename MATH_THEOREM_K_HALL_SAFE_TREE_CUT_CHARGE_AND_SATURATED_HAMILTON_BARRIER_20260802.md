# Hall-safe rotor trees: exact cut charge and the saturated Hamilton barrier

**Date:** 2026-08-02  
**Status:** unconditional exact min-cut criterion for a prescribed
distinct-role state tree, a non-matroid obstruction to the naive
base-intersection route, and an exact Hamiltonian reduction on the saturated
one-copy face. This note does not construct the required canonical flag
table.

## 0. Result

Fix an owner/target-exact marked flag table. Role \(i\) has a fixed head
state \(h_i\), a nonempty list \(N(i)\) of legal tail states, and its owner
and named lower-target payload are constant on that list. Put

\[
 a(v)=|\{i:h_i=v\}|.
\]

The lower balance problem assigns every role to one tail in its list, using
tail \(v\) exactly \(a(v)\) times. Suppose a set \(R\) of distinct roles
has already been assigned tails \(t_i\in N(i)\), and its projected state
edges \(t_i h_i\) form a spanning tree. Define, for \(Y\subseteq V\),

\[
 f(Y)=|\{i:N(i)\subseteq Y\}|,\qquad
 \kappa(Y)=a(Y)-f(Y),                                      \tag{0.1}
\]

and define the tree's **escape charge**

\[
 \chi_R(Y)=
 |\{i\in R:t_i\in Y,\ N(i)\not\subseteq Y\}|.             \tag{0.2}
\]

Then \(R\) is Hall-safe if and only if

\[
 b_R(v)\le a(v)\quad(v\in V),\qquad
 \chi_R(Y)\le\kappa(Y)\quad(Y\subseteq V),                \tag{0.3}
\]

where \(b_R(v)=|\{i\in R:t_i=v\}|\). Thus, for a prescribed \(R\),
(0.3), together with the graphic spanning condition, is the weakest exact
cutwise criterion: a reserved tree may enter a tail shore only by spending
that shore's unused Hall slack. In particular it cannot escape from a tight
shore.

The function \(\kappa\) is nonnegative and submodular whenever the original
table has a balanced matching. Its zero sets form a lattice. Hence one
canonical preprocessing is available: forbid every candidate tree
assignment charged across a tight shore.

This exact criterion does **not** become an ordinary two-matroid
intersection. Partial matchings which extend to a perfect matching fail the
matroid augmentation axiom already in \(K_{2,2}\). More decisively, on the
optimal saturated face there are exactly \(dW\) named targets, \(W\)
owners, and at most \(d\) targets per owner. Every role therefore carries
a full \(d\)-chain; its head is rigid and distinct. A Hall-safe spanning
tree exists there if and only if the predecessor digraph has a directed
Hamilton cycle. No generic matroid-base or marginal-degree argument can
eliminate that topology row.

Unordered Boolean containment degrees are also insufficient. State balance
sees ordered length-\((d-1)\) overlap. The standard exact SCD table at
\((k,m,d)=(7,3,3)\) has a root with no legal successor despite exact
coverage of every named target. A positive all-\(k\) theorem must prove
ordered overlap expansion, or directly construct a Hamilton/rectangle
absorbing predecessor graph; raw shadow surplus cannot supply it.

Upper interval decks, residence, exterior opening, and common-cap/compiler
conditions are not included here.

## 1. Fixed-head role--tail balance

Let \(I\) be a finite set of occurrence roles and \(V\) the fixed-head
state bank. Each role \(i\in I\) has

* a fixed head \(h_i\in V\);
* a nonempty legal tail list \(N(i)\subseteq V\); and
* a fixed owner and fixed named-target payload on every choice in \(N(i)\).

Write

\[
 a(v)=|\{i:h_i=v\}|,\qquad
 a(Y)=\sum_{v\in Y}a(v).                                  \tag{1.1}
\]

A balanced selector is a map \(t:I\to V\) satisfying

\[
 t_i\in N(i),\qquad |t^{-1}(v)|=a(v).                     \tag{1.2}
\]

The total supply and demand agree:

\[
 \sum_{v\in V}a(v)=|I|.                                   \tag{1.3}
\]

For \(Y\subseteq V\), define \(f(Y)\) and \(\kappa(Y)\) by
(0.1).

### Lemma 1.1 (closed-shore Hall form)

The role--tail system (1.2) is feasible if and only if

\[
                         f(Y)\le a(Y)
                         \qquad(Y\subseteq V).             \tag{1.4}
\]

Equivalently, \(\kappa(Y)\ge0\) for every \(Y\).

#### Proof

Necessity is immediate: every role whose complete list lies in \(Y\) must
consume one of the \(a(Y)\) tail copies in \(Y\).

For sufficiency, clone each state \(v\) into \(a(v)\) tail slots and join a
role to every clone of every state in its list. If ordinary Hall fails for
a role set \(X\), put \(Y=N(X)\). Every role in \(X\) then has its complete
list in \(Y\), so

\[
 f(Y)\ge |X|>a(Y),
\]

contradicting (1.4). Conversely ordinary Hall gives a perfect matching to
the cloned tail bank, hence (1.2). \(\square\)

### Lemma 1.2 (submodular Hall slack)

The function \(f\) is supermodular, and therefore \(\kappa=a-f\) is
submodular. If (1.2) is feasible, the family

\[
 \mathcal T=\{Y\subseteq V:\kappa(Y)=0\}                  \tag{1.5}
\]

is closed under union and intersection.

#### Proof

For one fixed nonempty list \(S=N(i)\), the indicator
\(1_{S\subseteq Y}\) is supermodular in \(Y\). If \(S\) is
contained in both sets, in exactly one, or in neither, the inequality is
immediate; in the remaining case \(S\) is split between the two sets, the
union indicator contributes one while the two individual indicators
contribute zero. Summing over roles proves that \(f\) is supermodular.
Since \(a\) is modular, \(\kappa\) is submodular.

When \(\kappa\ge0\), submodularity gives

\[
 0\le \kappa(A\cap B)+\kappa(A\cup B)
 \le \kappa(A)+\kappa(B)=0
\]

for \(A,B\in\mathcal T\). Thus both new sets are tight.
\(\square\)

## 2. Exact residual Hall charge

Reserve distinct roles \(R\subseteq I\), and choose one legal tail
\(t_i\in N(i)\) for each \(i\in R\). Put

\[
 b_R(v)=|\{i\in R:t_i=v\}|.                               \tag{2.1}
\]

The residual instance has roles \(I-R\) and demand

\[
                         a_R(v)=a(v)-b_R(v).              \tag{2.2}
\]

For \(Y\subseteq V\), let

\[
 r_R(Y)=|\{i\in R:N(i)\subseteq Y\}|.                     \tag{2.3}
\]

Because every reserved tail is legal,

\[
 r_R(Y)\le b_R(Y),\qquad
 b_R(Y)-r_R(Y)=\chi_R(Y).                                 \tag{2.4}
\]

### Theorem 2.1 (Hall-safe cut-charge theorem)

The reserved assignments extend to a balanced selector if and only if

\[
 b_R(v)\le a(v)\quad(v\in V)                              \tag{2.5}
\]

and

\[
                         \chi_R(Y)\le\kappa(Y)
                         \qquad(Y\subseteq V).             \tag{2.6}
\]

If the projected undirected edges

\[
                         \{t_i,h_i\}\qquad(i\in R)         \tag{2.7}
\]

contain a spanning tree of \(V\), the completed selector is one weakly
connected balanced state graph and hence has an Euler circuit. Every role,
owner, and named target is preserved exactly.

#### Proof

Condition (2.5) is precisely nonnegativity of the residual demands. The
roles of \(I-R\) whose complete lists lie in \(Y\) number

\[
                         f(Y)-r_R(Y).                     \tag{2.8}
\]

By Lemma 1.1 the residual instance is feasible exactly when

\[
 f(Y)-r_R(Y)\le a(Y)-b_R(Y)\qquad(Y\subseteq V).          \tag{2.9}
\]

Rearranging (2.9) gives

\[
 b_R(Y)-r_R(Y)\le a(Y)-f(Y),                              \tag{2.10}
\]

which is (2.6) by (0.1), (0.2), and (2.4).

After residual completion, every state \(v\) is used as a tail \(a(v)\)
times and occurs as a head \(a(v)\) times, so the selected directed graph is
balanced. If it contains (2.7)'s spanning tree, its support is weakly
connected. A finite connected balanced directed multigraph is Eulerian.
Payload constancy on each role list preserves all labels. \(\square\)

### Corollary 2.2 (tight-shore no-escape law)

If \(Y\in\mathcal T\), every Hall-safe reserved tree satisfies

\[
 t_i\in Y\quad\Longrightarrow\quad N(i)\subseteq Y
 \qquad(i\in R).                                          \tag{2.11}
\]

Thus no reserved role may spend a tail inside a tight shore while retaining
an alternative outside it.

#### Proof

For tight \(Y\), (2.6) reads \(\chi_R(Y)=0\). Every summand in
(0.2) is nonnegative, giving (2.11). \(\square\)

This is stronger than saying merely that the selected tree edge stays
inside \(Y\): the charge depends on the role's entire legal list. Tight
sets are therefore functional barriers, not just graphic cuts.

### Corollary 2.3 (exact separation oracle)

For a proposed distinct-role spanning tree \(R\), Hall safety is certified
or refuted by one capacitated bipartite max-flow on the residual instance.
Equivalently, a minimum violating set \(Y\) maximizes

\[
                         \chi_R(Y)-\kappa(Y).             \tag{2.12}
\]

The corresponding minimum cut is a checkable obstruction certificate.

### Corollary 2.4 (protected root)

A prescribed root option may be included among the reserved assignments
\(R\). If (2.5)--(2.6) hold and the reserved projections contain a
spanning tree, the completed Euler circuit contains that option and may be
cyclically rotated to start there. More generally, any distinct-role
protected block is handled by inserting all of its assignments into \(R\)
before computing \(b_R,\chi_R\).

### Theorem 2.5 (tight-shore crossing law)

For a tight shore \(Y\in\mathcal T\), put

\[
 F_Y=\{i:N(i)\subseteq Y\},\qquad
 H_Y=\{i:h_i\in Y\}.                                      \tag{2.13}
\]

Every balanced selector has the following forced cut profile:

1. a role uses a tail in \(Y\) if and only if it belongs to \(F_Y\);
2. the selected arcs leaving \(Y\) are exactly the roles
   \(F_Y\setminus H_Y\);
3. the selected arcs entering \(Y\) are exactly the roles
   \(H_Y\setminus F_Y\); and
4. the two crossing multiplicities agree:

   \[
    |F_Y\setminus H_Y|=|H_Y\setminus F_Y|.                \tag{2.14}
   \]

In particular, if \(Y\) is nonempty and proper and

\[
                         F_Y=H_Y,                          \tag{2.15}
\]

then every balanced selector is disconnected across \(Y\). No Hall-safe
spanning-tree skeleton exists.

#### Proof

Tightness says

\[
                         |F_Y|=f(Y)=a(Y)=|H_Y|.           \tag{2.16}
\]

Every role in \(F_Y\) must use a tail in \(Y\), and these roles already
number all \(a(Y)\) available tail copies there. Hence no role outside
\(F_Y\) can use a tail in \(Y\), proving item 1. Comparing tail membership
with fixed-head membership gives items 2 and 3. Equation (2.14) follows
from (2.16). Under (2.15), no selected arc crosses the cut in either
direction, proving the obstruction. \(\square\)

Thus tight shores expose not only a matching obstruction but an invariant
topological current. A constructive table must avoid every proper
zero-current tight shore before any random-tree or absorber argument can
start.

### Corollary 2.6 (private zero-charge tree absorber)

Assume the original role--tail instance is feasible.  Suppose distinct
roles `R` have singleton legal lists

\[
                         N(i)=\{t_i\}\qquad(i\in R),     \tag{2.17}
\]

their tail uses respect `b_R(v)<=a(v)`, and their projected state edges
contain a spanning tree.  Then `R` is Hall-safe and extends to one connected
balanced selector.

#### Proof

For every shore `Y` and every `i in R`, the implication

\[
                         t_i\in Y\Longrightarrow N(i)\subseteq Y
\]

is automatic from (2.17).  Hence `chi_R(Y)=0` for all `Y`.  Feasibility of
the original instance gives `kappa(Y)>=0`, so Theorem 2.1 applies. \(\square\)

Thus a bank of occurrence-private, singleton-tail sockets is an exact
absorber: it spends no Hall slack at all.  Producing a spanning such bank in
the canonical Boolean flag table remains a structural construction problem;
raw multiplicity of nonfixed leading letters does not produce (2.17).

## 3. Why the extension system is not a matroid

One might hope that the reserved assignments extendable to a perfect
role--tail matching form a matroid and then intersect that matroid with the
graphic matroid. This is false in the smallest complete instance.

### Proposition 3.1 (the \(K_{2,2}\) augmentation obstruction)

Let roles be \(1,2\), tail states be \(a,b\), and every role be adjacent to
both states, each of capacity one. Denote the four assignment edges by

\[
 e_{1a},e_{1b},e_{2a},e_{2b}.
\]

Let \(\mathcal E\) consist of the partial matchings contained in some
perfect matching. Then \(\mathcal E\) is not the independent-set family
of a matroid.

#### Proof

The perfect matchings are

\[
 A=\{e_{1a},e_{2b}\},\qquad
 A'=\{e_{1b},e_{2a}\}.
\]

Take \(B=\{e_{1b}\}\). Both \(A\) and \(B\) lie in
\(\mathcal E\), with \(|A|>|B|\). But \(B+e_{1a}\)
repeats role \(1\), while \(B+e_{2b}\) repeats tail \(b\).
Neither is a partial matching, hence neither is extendable. The augmentation
axiom fails. \(\square\)

Consequently the Hall-safe tree problem is not ordinary graphic--matching
matroid intersection. The exact extension object is a matching
delta-system; adding the graphic row does not acquire a two-matroid rank
formula for free.

## 4. The saturated face is exactly Hamiltonian

Suppose the residual bank contains exactly \(dW\) named targets, there are
\(W\) owner roles, and one literal trace can mark at most \(d\) targets.
Any owner/target-exact table must then mark exactly \(d\) targets at every
role. In the strict nested-chain realization, every head is the ordered
difference word of its chain. Distinct target chains give distinct heads.
Thus

\[
                         a(v)=1\quad(v\in V),\qquad |V|=W. \tag{4.1}
\]

Define the predecessor digraph \(\Gamma\) on \(V\) by

\[
                         u\longrightarrow v
 \quad\Longleftrightarrow\quad
 \text{the role headed at \(v\) admits tail \(u\)}.       \tag{4.2}
\]

### Theorem 4.1 (saturated Hall-safe tree equivalence)

The following are equivalent.

1. The table has a Hall-safe distinct-role spanning-tree skeleton.
2. The table has a connected balanced one-copy selector.
3. The predecessor digraph \(\Gamma\) has a directed Hamilton cycle.

#### Proof

Theorem 2.1 proves \(1\Rightarrow2\). Conversely, a connected balanced
selector contains an undirected spanning tree, and deleting its labelled
tree arcs leaves the other selected assignments as an exact residual
matching, so \(2\Rightarrow1\).

Under (4.1), balance gives every vertex indegree and outdegree one. Hence
every balanced selector is a directed cycle cover of \(\Gamma\), and it is
weakly connected exactly when it is one directed Hamilton cycle. This
proves \(2\Longleftrightarrow3\). \(\square\)

In this face the skeleton itself has \(W-1\) assignments and leaves one
closing assignment. It is therefore a Hamilton path plus its closing arc,
not a sparse perturbation which robust Hall slack can absorb.

### Corollary 4.2 (exact rectangle absorber condition)

Assume \(\Gamma\) has a cycle cover. If every non-Hamiltonian cycle cover
contains arcs

\[
 x\to y,\qquad u\to v
\]

in two different cycles for which the crossed arcs

\[
 x\to v,\qquad u\to y                                   \tag{4.3}
\]

also lie in \(\Gamma\), then \(\Gamma\) has a Hamilton cycle.

#### Proof

Replace the two old arcs by (4.3). Indegree and outdegree one are
preserved, and the two old cycles merge into one. Repeating decreases the
number of cycles until one remains. \(\square\)

This is a useful Boolean-specific target: prove a crossing rectangle in the
ordered predecessor graph, not expansion only in the underlying containment
lattice.

### Proposition 4.3 (one-unit Hall expansion is still insufficient)

Even on the saturated distinct-head face, strict Hall expansion on every
proper role set, minimum role and tail degree two, and strong connectivity
of the union digraph do not imply a Hall-safe tree.

#### Proof

Take three roles with heads \(1,2,3\), unit tail capacities, and lists

\[
 N(1)=\{1,2\},\qquad
 N(2)=\{1,2,3\},\qquad
 N(3)=\{2,3\}.                                             \tag{4.4}
\]

For every nonempty proper role set \(X\),

\[
                         |N(X)|\ge |X|+1.                  \tag{4.5}
\]

Every role and every tail has degree at least two. The projected allowed
digraph is the reflexive bidirected path
\(1\leftrightarrow2\leftrightarrow3\), hence is strongly connected.

Nevertheless the only perfect role--tail matchings are the identity and
one of the two adjacent transpositions. Their projected cycle profiles are
three loops or one directed \(2\)-cycle plus one loop. A directed
\(3\)-cycle would require either tail \(3\) for role \(1\), or tail \(1\)
for role \(3\), both forbidden by (4.4). Theorem 4.1 therefore rules out a
Hall-safe spanning tree. \(\square\)

Thus even the natural \(+1\) strengthening on every proper Hall cut is not
the missing theorem. The expansion must control ordered cyclic
correlation, for example through the rectangle absorber condition, rather
than only neighbourhood cardinalities.

## 5. Why raw Boolean containment expansion does not close the gate

A legal role--tail incidence is not merely a containment. If role \(i\)
has fixed suffix word

\[
 (A_{i,1},\ldots,A_{i,d}),
\]

then a fixed head \(h_j=(A_{j,1},\ldots,A_{j,d})\) can be
its tail only if

\[
 (A_{j,2},\ldots,A_{j,d})
       =(A_{i,1},\ldots,A_{i,d-1})                       \tag{5.1}
\]

and the leading letter \(A_{j,1}\) satisfies the owner containment for
role \(i\). The large Boolean menu of possible leading letters is useless
if none is the first letter of a fixed head with overlap (5.1).

The standard recursive SCD gives an exact literal witness. At

\[
                         (k,m,d)=(7,3,3),                 \tag{5.2}
\]

take

\[
 p=\{0,1,6\},\qquad f_p=(p;1,0),\qquad B(f_p)=\{6\}.      \tag{5.3}
\]

Its possible successor roots by unordered Johnson containment are

\[
 q_\beta=\{0,6,\beta\},\qquad
 \beta\in\{2,3,4,5\}.                                    \tag{5.4}
\]

But the fixed SCD flags there are

\[
                         f_{q_\beta}=(q_\beta;0,\beta).   \tag{5.5}
\]

The overlap requires their final deletion letter to lie in
\(B(f_p)=\{6\}\), whereas it equals \(\beta\). Thus this role has no
legal successor. The same table nevertheless covers every named high
target exactly once.

Therefore no inequality using only Boolean shadow sizes or unordered
containment degrees can imply even the base Hall condition, much less the
Hall-safe tree condition. The weakest exact verifiable expansion is (0.3)
on the **ordered role--tail graph**. On the saturated face, the remaining
genuinely constructive alternatives are:

1. build a Hamilton predecessor cycle directly; or
2. build one cycle cover and prove the rectangle absorber condition of
   Corollary 4.2.

## 6. Precise remaining lemma and scope

The lower rotor-fusion problem is now reduced to the following statement.

> **Ordered triangular Hall-tree lemma.** Choose an owner/target-exact
> full-chain table and, in its ordered predecessor graph, either a directed
> Hamilton cycle or a cycle cover satisfying the protected rectangle
> absorber condition. Equivalently, choose a spanning tree whose escape
> charge obeys (0.3) on every tail shore.

The corrected stationary pull clock proves only fractional trace balance.
The SCD theorem proves only the exact static owner/target marginal. Neither
proves the ordered overlap expansion in this lemma. The explicit SCD
example shows that the two facts cannot simply be combined after the table
is frozen.

On a balanced **complete** rank-\(a\)/rank-\(b\) Boolean containment
fibre, the companion theorem
MATH_THEOREM_K_BOOLEAN_INTERVAL_FIBRE_HALL_AND_SHADOW_RESERVED_TREE_20260802.md
computes \(\kappa\) as an exact normalized edge boundary and proves
\(\kappa(Y)\ge1\) on every nontrivial shore. That is the strongest
unconditional containment-degree input currently available. It does not
finish this lemma: the canonical head bank is sparse after ordered-spine
conditioning, and Proposition 4.3 shows that even strict one-unit Hall
expansion does not force a Hamilton selector.

All claims in this note concern the lower labelled rotor row. They do not
prove upper interval-union coverage, residence, component opening in an
ambient word, or common-cap/compiler feasibility. Those remain separate
guards on the role lists or separate downstream theorems.

An independent proof replay and literal Boolean two-cycle family are in
MATH_AUDIT_K_HALL_SAFE_TREE_BOWTIE_BOOLEAN_SPINE_AND_CUT_CHARGE_20260802.md.
