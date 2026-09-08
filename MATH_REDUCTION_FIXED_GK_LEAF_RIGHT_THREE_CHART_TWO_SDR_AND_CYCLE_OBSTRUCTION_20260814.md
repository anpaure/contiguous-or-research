# Fixed-GK leaf selectors: the topology-safe three-chart gate

**Date:** 2026-08-14
**Status:** unconditional structural reduction, exact cycle obstruction, and
exact finite Hall obstruction; a self-contained `m=7` minimum-reset forest
certificate identifies the necessary repair atom

## 0. Outcome

Put

\[
 n=2m+1,\qquad
 \mathcal U={ [n]\choose m+2},\quad
 \mathcal M={ [n]\choose m+1},\quad
 \mathcal L={ [n]\choose m}.
\tag{0.1}
\]

Use the linear Greene--Kleitman `10` matching.  For every
`U in mathcal U`, let `p(U)` be its first free `1` and put

\[
 A(U)=U-p(U).
\tag{0.2}
\]

The map `U -> A(U)` is injective.  Given `q in A(U)`, set

\[
 L=U-\{p,q\},\qquad B=U-q=L+p.
\tag{0.3}
\]

A **leaf** of `A` is either a free `1`, or the `1` of an adjacent matched
peak `10`.  This note identifies exactly what the leaf restriction buys.

1. The unrestricted leaf host is not intrinsically acyclic.  It has a
   directed triangle at `m=2`, a lower-rainbow directed `C_5` at `m=3`,
   and the latter extends to a full simultaneous `L/B` SDR.  Therefore
   neither “all leaf edges descend a Tamari potential” nor “two SDRs force
   a forest” is true.
2. The **leaf-right** restriction

   \[
   q>p                                                    \tag{0.4}
   \]

   is topology-safe: every selected edge `A -> B` strictly decreases the
   coordinate-sum potential.  Any simultaneous `L/B` SDR in this host is
   automatically a Catalan linear forest.
3. Every leaf option has an inverse normal form with one of exactly three
   head charts.  In the GK matching of `L`, the coordinate `p` is one of
   its last three free zeros.  If these are indexed from the right, then

   \[
   t\in\{0,1,2\},\qquad B=\tau_t(L):=L+z_t(L).       \tag{0.5}
   \]

   Thus a lower has at most three **distinct heads**, but it can support
   `m+1` raw leaf options and `m` raw leaf-right options.  The frequently
   observed degree-three census is a collapsed head-signature degree, not
   raw option incidence.
4. The leaf-right gate genuinely needs all three charts in finite exact
   tests: the strongest two-chart subhost `t in {0,1}` is already UNSAT at
   `m=4` (and through `m=6`), while the full leaf-right host is SAT and
   independently verified through `m=6`.
5. The hoped-for all-parameter leaf-right theorem is false already at
   `m=7`.  Its upper--head projection has maximum matching `4950<5005`.
   More sharply, the projection has one upper-heavy connected component,
   containing the monotone upper `1^9 0^6`, with `2705` uppers and `2650`
   heads.  This component alone is a Hall cut of deficiency `55`.
6. A full leaf simultaneous SDR at `m=7` exists with exactly `55` left
   options `q<p`, so `55` is the exact minimum number of monotonicity resets.
   Its owner graph is nevertheless a linear forest.  Every reset is in chart
   `t=0`; this gives the exact local atom that any general repair theorem must
   organize.

Consequently no pure descending-potential proof can work in this host.  The
remaining all-`m` statement is a structured three-chart rainbow matching
problem with a necessary bank of chart-zero resets.  It is not ordinary
matroid intersection, not a bounded-degree hypergraph matching instance, and
its natural fibers are not interval-convex in coordinate order.

## 1. Linear GK convention

Read a binary membership word from left to right.  On reading a `1`, push
its position; on reading a `0`, match it to the latest unmatched `1`, if
one exists.  Equivalently, repeatedly erase matched `10` pairs.  The free
positions consist of free zeros followed by free ones.

For a word `X`, write `M(X)` for the matching and `F_0(X),F_1(X)` for its
free zero and free one sets.  Since `U` has excess three,
`p(U)=min F_1(U)` exists.

### Lemma 1.1 (fixed first endpoint)

The map `(0.2)` is a bijection from `mathcal U` onto the rank-`m+1` words
with at least one free zero.  For `A=A(U)`,

\[
 p(U)=\max F_0(A).                                  \tag{1.1}
\]

The omitted owners are the words with no free zero; their number is
`Cat_(m+1)`.

#### Proof

This is the standard adjacent-rank GK chain matching: moving one step down
changes the first free one to zero, and the inverse changes the last free
zero to one.  The unmatched rank difference is

\[
 {2m+1\choose m+1}-{2m+1\choose m+2}
 =\operatorname {Cat}_{m+1}. \qquad\square          \tag{1.2}
\]

## 2. Direct leaf normal form

Delete all matched `10` pairs from `A`.  Because `A` has excess one and is
in the image of Lemma 1.1, its reduced word is

\[
 0^a1^{a+1}\qquad(a\ge1),                           \tag{2.1}
\]

and `p` is the last displayed zero.  Restoring the erased pairs gives a
unique noncrossing-parenthesis decoration of `(2.1)`.

### Lemma 2.1 (leaf catalogue)

The legal leaf coordinates `q in A` are exactly:

* a displayed free `1` of `(2.1)`; or
* the opening `1` of a restored primitive whose interior is empty, namely
  a literal adjacent matched `10`.

For every such `q`, `(0.3)` is a valid diamond with upper `U=A+p`.  The
leaf-right subcatalogue consists exactly of these leaves occurring to the
right of the distinguished last free zero `p`.

This is simply the definition of a free one or adjacent matched peak in
the noncrossing matching.  It is useful because all later claims refer to
this literal finite catalogue, not to arbitrary Tamari rotations.

### Corollary 2.2 (exact upper degrees)

Every upper has between `3` and `m+1` leaf options.  Every upper has
between `2` and `m+1` leaf-right options.

The degree is the number of free ones plus the number of adjacent matched
peaks, with the additional cut `q>p` in the leaf-right case.  In `(2.1)`
there are `a+1>=2` free ones, all to the right of `p`.  If `a=1`, the
remaining matched word is nonempty for `m>=2` and contains an adjacent peak;
if `a>=2`, there are already at least three free-one leaves.  This gives the
two lower bounds.  The number of free-one leaves plus adjacent peaks is at
most `(a+1)+(m-a)=m+1`.

## 3. Inverse three-chart normal form

The following is the structural core.

### Theorem 3.1 (last-three-free-zero theorem)

Let `(U,p,q,A,L,B)` be a leaf option.  List the free zeros of `L` as

\[
 z_0<z_1<\cdots<z_s.
\tag{3.1}
\]

Then

\[
 p\in\{z_s,z_{s-1},z_{s-2}\}.                      \tag{3.2}
\]

Writing `t=s-j` when `p=z_j`, one has

\[
 t\in\{0,1,2\},\qquad B=L+p=\tau_t(L).             \tag{3.3}
\]

Conversely, the complete inverse catalogue is obtained as follows.  Pick
`L`, choose one of its last three free zeros `p`, and choose `q != p` with
`q notin L`.  Put

\[
 A=L+q,\qquad U=L+p+q.                              \tag{3.4}
\]

This triple is a leaf option exactly when

1. `p` is the first free one of `U`; and
2. in `A`, `q` is free or is matched to `q+1`.

It is leaf-right exactly when, additionally, `q>p`.

#### Proof

Passing from `A` to `L=A-q` changes one `1` to `0`.  In the stack path,
this either exposes `q` itself as a new free zero or shifts the mate chain
starting at `q`; because `q` is free or has the immediate mate `q+1`, that
chain can cross at most two record-minimum levels beyond the old last free
zero `p`.  Thus at most two free zeros of `L` can lie to the right of `p`,
proving `(3.2)`.  This is the usual parenthesis-stack deletion lemma in
the special cases “unmatched close” and “empty primitive.”

Equation `(3.3)` is `(0.3)`.  Conversely `(3.4)` reconstructs the unique
candidate, and the two stated GK tests are precisely `p=p(U)` and the leaf
condition. `square`

### Corollary 3.2 (exact incidence bounds)

For each lower `L`, the set of possible second owners is contained in

\[
 \{\tau_0(L),\tau_1(L),\tau_2(L)\}.                 \tag{3.5}
\]

Hence the collapsed distinct-head degree is at most three.  In contrast,
the maximum number of raw upper-labelled options at one lower is exactly

\[
 m+1\quad\hbox{in the leaf host},\qquad
 m\quad\hbox{in the leaf-right host}.               \tag{3.6}

Within one signature `(L,t,B)`, as many as `m` different upper labels can
occur.  Thus collapsing to `(L,B)` loses the upper-colour constraint and
cannot justify a bounded-degree matching theorem.

### Corollary 3.3 (exact reset atom)

If a leaf option is not leaf-right, so `q<p`, then its inverse chart is
necessarily

\[
 t=0,\qquad p=\max F_0(L).                         \tag{3.7}
\]

Moreover `q(q+1)=10` is a literal adjacent matched peak of `A`.  Thus every
left option has the single normal form

\[
 A=L+q\longrightarrow B=L+p,qquad q<p,            \tag{3.8}
\]

where `p` is the rightmost free zero of `L`.  It raises the potential by

\[
 \Phi(B)-\Phi(A)=p-q>0.                            \tag{3.9}
\]

#### Proof

In `(2.1)`, all free ones of `A` lie to the right of its last free zero `p`.
Hence a leaf `q<p` cannot be free; it is the opening coordinate of an empty
primitive, i.e. the literal peak `10`.  Deleting that opening one creates a
free zero to the left of `p` and creates none to its right.  Therefore `p`
remains the rightmost free zero of `L`, which is chart zero in `(3.3)`.
Equations `(3.8)--(3.9)` are immediate. `square`

## 4. Topology: the exact positive cut and exact no-go

Orient every option from `A` to `B`.  Put

\[
 \Phi(X)=\sum_{i\in X}i.                            \tag{4.1}
\]

### Theorem 4.1 (leaf-right SDR implies a Catalan linear forest)

Suppose one leaf-right option is chosen for every `U in mathcal U`, and
the chosen `L` and `B` labels are each pairwise distinct.  Then the owner
edges `AB` form a linear forest with exactly `Cat_(m+1)` components.

#### Proof

The tails `A(U)` are pairwise distinct.  Distinct heads `B` give directed
indegree at most one, and fixed tails give directed outdegree at most one.
Therefore the undirected owner degree is at most two.  Moreover

\[
 \Phi(B)-\Phi(A)=p-q<0                             \tag{4.2}
\]

by `q>p`, so there is no directed cycle.  In a finite graph with directed
indegree and outdegree at most one, every undirected cycle is directed.
Thus the graph is a linear forest.  It has
`|mathcal M|` vertices and `|mathcal U|` edges, hence

\[
 c=|\mathcal M|-|\mathcal U|=\operatorname {Cat}_{m+1}.
 \qquad\square                                      \tag{4.3}
\]

### Proposition 4.2 (the full leaf host is cyclic)

At `m=2`, in left-to-right word notation, the allowed owner arcs include

\[
 01011\to10011\to00111\to01011.                    \tag{4.4}
\]

At `m=3`, they include the lower-rainbow directed cycle

\[
\begin{split}
1100011&\to1000111\to0001111\to0011011\\
       &\to0110011\to1100011.                       \tag{4.5}
\end{split}
\]

Its five lower labels are respectively

\[
1000011,\ 0000111,\ 0001011,\ 0010011,\ 0100011.  \tag{4.6}
\]

Moreover `(4.5)` extends to a full choice with all uppers exact and both
`L` and `B` injective.  The full selected graph has one cycle.

Thus all three stronger statements are false:

* every leaf edge descends one common potential;
* lower injectivity kills all cycles;
* every simultaneous leaf `L/B` SDR is a forest.

The leaf-right cut removes `(4.4)--(4.5)` and proves topology by `(4.2)`.

## 5. The exact matching problem and the right-head Hall cut

Create one variable for each inverse-normal-form option `(U,L,t)` and
require

\[
 \sum_{(L,t)\in N(U)}x_{U,L,t}=1\qquad(U\in\mathcal U),
\tag{5.1}
\]

\[
 \sum_{U,t}x_{U,L,t}\le1\qquad(L\in\mathcal L),
\tag{5.2}
\]

and

\[
 \sum_{U,L:\tau_t(L)=B}x_{U,L,t}\le1
 \qquad(B\in\mathcal M).                            \tag{5.3}
\]

For the leaf-right theorem, retain only options with `q>p`.

This is an intersection of three partition constraints: upper exactness,
lower injectivity, and head injectivity.  In a general catalogue this is
three-dimensional matching, not ordinary two-matroid intersection.
The special Boolean structure is exactly `(2.1)--(3.4)`.

### Proposition 5.1 (all three charts are needed)

In the leaf-right host, exact SAT gives:

\[
\begin{array}{c|ccccc}
\text{allowed types}&m=2&m=3&m=4&m=5&m=6\\ \hline
\{0,1\}&\mathrm{SAT}&\mathrm{SAT}&\mathrm{UNSAT}&\mathrm{UNSAT}&\mathrm{UNSAT}\\
\{0,2\}&\mathrm{SAT}&\mathrm{UNSAT}&\mathrm{UNSAT}&\mathrm{UNSAT}&\mathrm{UNSAT}\\
\{1,2\}&\mathrm{UNSAT}&\mathrm{UNSAT}&\mathrm{UNSAT}&\mathrm{UNSAT}&\mathrm{UNSAT}.
\end{array}                                         \tag{5.4}
\]

Thus no fixed pair of the inverse GK charts supports an all-parameter
proof.  The full three-chart leaf-right host has independently checked
SAT certificates for `2<=m<=6`:

\[
\begin{array}{c|rrrrr}
m&2&3&4&5&6\\ \hline
|\mathcal U|&5&21&84&330&1287\\
\text{forest components}&5&14&42&132&429.
\end{array}                                         \tag{5.5}
\]

An `m=7` CP-SAT run returned `UNKNOWN` after 240 seconds and a long Kissat
run did not resolve the three-constraint CNF.  The projection obstruction
below settles the instance without relying on either run.

### Proposition 5.2 (not an interval shortcut)

For fixed `(L,t)`, the legal `q` positions need not be consecutive either
in coordinate order or among the zero positions of `L`.  Nonconvex fibers
occur already at `m=4` and proliferate thereafter.  Hence the literal
catalogue is not an interval/convex bipartite matching instance under the
natural linear coordinate order.

Reindexing a type-`1` head through the bijective type-`0` chart does produce
a rooted Catalan forest of depth at most `m+1` on lower words in exact
finite census.  However the type-`1` map has indegree growing to `m`, and
upper-labelled parallel options remain.  This is a plausible peeling or
finite-state recursion scaffold, not yet a matching proof.

### Theorem 5.3 (the leaf-right theorem fails at `m=7`)

Let `G_B^>(m)` be the bipartite projection whose left shore is `mathcal U`,
whose right shore consists of second owners `B`, and where `U B` is an edge
when some leaf-right option for `U` has head `B`.  At `m=7`,

\[
 |\mathcal U|=5005,
 \qquad \nu(G_B^>(7))=4950.                         \tag{5.6}
\]

In particular, even the upper--head projection violates Hall, so the full
system `(5.1)--(5.3)` is impossible.

There is a canonical cut not depending on a chosen maximum matching.  The
graph `G_B^>(7)` has exactly `66` connected components.  The component
containing the monotone upper

\[
 U_*=1^9 0^6                                       \tag{5.7}
\]

has `2705` upper vertices and `2650` head vertices.  It is the unique
upper-heavy component.  The other `65` components are head-heavy.  Hence
this one component has Hall deficiency `55`, and exact matching saturates
the smaller shore in every component.

The lower projection behaves differently:

\[
 \nu(G_L^>(7))=5005.                               \tag{5.8}
\]

Thus the failure is an exact second-owner correlation, not shortage of
distinct lower labels.

#### Proof

The verifier constructs the complete leaf catalogue from the stack
definition, collapses parallel options only for each named projection, and
runs an exact augmenting-path algorithm.  It independently constructs all
bipartite connected components.  Its asserted output is `(5.6)--(5.8)` and
the component counts above.  No SAT status is used. `square`

### Corollary 5.4 (unavoidable reset bank)

Let

\[
 \delta_m=|\mathcal U|-\nu(G_B^>(m)).              \tag{5.9}
\]

Every full-leaf simultaneous `L/B` SDR uses at least `delta_m` left options
`q<p`.  In particular every such selector at `m=7` uses at least `55` reset
atoms `(3.8)`.

#### Proof

If a selector uses `r` left options, its remaining `|mathcal U|-r` options
are leaf-right and have distinct heads.  They form a matching in
`G_B^>(m)`, so `|mathcal U|-r<=nu(G_B^>(m))`. `square`

For orientation, exact independent projection census gives

\[
\begin{array}{c|rrr}
m&7&8&9\\ \hline
|\mathcal U|&5005&19448&75582\\
\nu(G_B^>(m))&4950&18955&72905\\
\delta_m&55&493&2677.
\end{array}                                        \tag{5.10}
\]

Thus `55` exceptions are already necessary at the first failed parameter,
and the next two finite defects are larger.  These three values alone do
not prove that `delta_m` is unbounded.  Only the `m=7` row is needed for the
unconditional no-go in Theorem 5.3; the larger rows are exact finite
orientation data, not an asymptotic extrapolation.

## 6. Exact minimum repair at `m=7`

### Theorem 6.1 (55 chart-zero resets suffice, with forest topology)

At `m=7` there is a full-leaf integral solution of `(5.1)--(5.3)` with
exactly `55` left options.  Consequently `55` is the exact minimum number
of left options.  In this solution:

* every reset is the chart-zero atom `(3.8)`;
* all `5005` uppers occur once, and the selected lowers and heads are each
  pairwise distinct;
* the selected owner graph has `6435` vertices, `5005` edges, `1430`
  components, maximum degree two, and cycle rank zero; hence it is a linear
  forest;
* the `55` reset edges occur in `50` owner-tree components: `46` components
  contain one reset, `3` contain two, and `1` contains three.

#### Proof

The accompanying verifier embeds the certificate as the byte stream `q(U)`
in increasing integer order of the uppers.  It reconstructs every option
from the independent catalogue rather than trusting derived certificate
fields.  It then checks upper exactness, lower and head injectivity, the
owner degrees, component counts, and cycle rank.  The embedded stream has

\[
 \operatorname {SHA256}=
 \texttt{f5a81c28a57f5eddbd3dadea3d206d3e72644d53959d278bf533529a4125e421}.
\tag{6.1}
\]

It contains exactly `55` choices with `q<p`.  Corollary 5.4 supplies the
matching lower bound `55`, so the certificate is minimum without appealing
to a solver optimality claim. `square`

### Exact repair interface

Theorems 5.3 and 6.1 isolate the smallest structural host that survives the
topology obstruction:

1. use the descending leaf-right three-chart host away from a reset bank;
2. admit only the chart-zero atom `(3.8)` in that bank;
3. solve the joint `L/B` rainbow matching while controlling the owner paths
   joined by those resets.

The finite certificate shows that multiple resets may lie on one owner
tree, so a theorem requiring one reset per component is too strong.  It also
shows that potential-increasing atoms do not themselves force cycles.  What
remains open is an all-`m` deterministic alternating repair theorem that
builds a sufficiently large reset bank and proves forest topology at the
same time.

## 7. Consequences and remaining all-parameter target

The pure leaf-right three-chart theorem is false.  The viable target is a
**three-chart plus chart-zero-reset theorem**: select one leaf option per
upper with distinct lower and head labels, use at least the projection
defect `(5.9)` resets, and choose the reset locations so that the owner graph
is acyclic.  Theorem 6.1 proves exactly this target at the first obstructed
parameter.

The bare owner/lower/upper synchronization is already available by the
double-turn theorem in the repository.  The value of the present route is
precisely the fixed-GK/Catalan topology.  No chronology or wreath ordering
is asserted here.

## 8. Reproducibility and scope

The frozen self-contained verifier is

`verify_fixed_gk_leaf_right_hall_and_reset.py`.

It reconstructs the complete catalogue, checks the last-three-chart and
left-reset normal forms, computes both projection matchings, constructs the
head-projection components, and verifies the embedded `m=7` minimum-reset
forest certificate.  Its H100 SHA and output SHA are

\[
\begin{split}
\text{verifier: }&
\texttt{26e1f7d784b422d24e97d3acb534d5616b348bd274a041426b63f2da0e03bf5f},\\
\text{output: }&
\texttt{5421d5d33139b29c98a1d782164d56d97fda5c3898fe9032b2566a831a22ddb4}.
\end{split}                                        \tag{8.1}
\]

The two exploratory structural cross-checks were
`scratch/audit_gk_leaf_exact_structure_20260814.py` and
`scratch/verify_gk_leaf_inverse_normal_form_20260814.py`.  They are not part
of the frozen staging scope.

All executions and hashes were performed on H100.  The finite SAT results
are evidence only where explicitly labelled; the structural theorems do
not depend on solver extrapolation.
