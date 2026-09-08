# Ordered Boolean portals: automatic Rado forests and the sharp contraction cut

Date: 2026-08-01

## 1. Scope and outcome

For prospective ordered-shift and pivot connectors on the unmerged symmetric
chain decomposition, the graphic Rado row is automatic: every transversal is
a forest.  This holds for bounded or positive-density task sets, provided
each task has a nonempty menu and no rank-(m) root is used as the tail of two
tasks.

For a bounded prepared task bank, the robust ordered-flag portal theorem gives
nonempty linear menus, so the Rado row closes without the unresolved
multi-order selector.

After SCD chains have already been merged, automatic independence can fail.
The exact obstruction is a graphic-flat/partition cut.  Robust literal portal
degree and pair-codegree one do not control this cut: a large menu can collapse
entirely to loops in one contracted component.

## 2. Monotone Johnson connectors

Fix a total order (prec) on the ground coordinates and let

\[
\phi(X)=\sum_{x\in X}\operatorname{pos}_\prec(x)
\]

for every rank-(m) set (X).

Call a Johnson edge (X,Y=X-a+b) **forward** when (a\prec b), and orient
it (X\to Y).  Then

\[
\phi(Y)-\phi(X)
=\operatorname{pos}_\prec(b)-\operatorname{pos}_\prec(a)>0.
\tag{2.1}
\]

### Theorem 2.1 (monotone one-exit forest)

Let (F) be any set of forward Johnson edges such that every rank-(m)
vertex is the tail of at most one selected edge.  Then the underlying
undirected graph (F) is a forest.

### Proof

Suppose an undirected cycle exists.  Choose on it a vertex (X) minimizing
(phi).  Both neighbours on the cycle have strictly larger potential, so
both cycle edges are oriented out of (X).  This gives two selected outgoing
edges at (X), contradicting the hypothesis.  ∎

This argument permits arbitrarily many incoming edges and does not require
private heads or disjoint connector menus.

## 3. Ordered-shift portals are monotone

At a prepared rank-(m) root (p), write

\[
z_1\prec z_2\prec\cdots\prec z_m.
\]

The robust ordered-flag portal theorem supplies the turns

\[
q_\beta=p-\{z_1\}+\{\beta\},
\qquad z_d\prec\beta,
\tag{3.1}
\]

with owner (p\cup\{\beta\}).  The connector on rank-(m) roots is

\[
p\longrightarrow q_\beta.
\]

Because (z_1\prec\beta), every connector in this menu is forward.
Different (eta)'s give different head roots and owners.

The pivot-rich geodesic has the same form: each step replaces a labelled
(lambda_j) by a later labelled (ho_j).  Any selected exit from such a
prepared geodesic is therefore another forward Johnson connector after the
labels are put in the indicated order.

## 4. SCD contraction does not identify middle roots

Fix any symmetric chain decomposition of the Boolean lattice.  A chain
contains at most one set of each rank.  Consequently distinct rank-(m) sets
belong to distinct SCD chains.

Let (kappa_0(X)) be the SCD chain containing the rank-(m) root (X).
Then

\[
X\ne Y\quad\Longrightarrow\quad\kappa_0(X)\ne\kappa_0(Y).
\tag{4.1}
\]

Thus the graph of Johnson connectors is unchanged when the original SCD
chains are contracted: no two connector endpoints coalesce.

## 5. Automatic Rado theorem on the raw SCD

Let the prepared tasks be indexed by (I).  Task (i) has a distinct tail
root (p_i) and a nonempty menu

\[
\mathcal E_i=
\{\kappa_0(p_i)\kappa_0(q_{i,\beta}):\beta\in B_i\}
\]

of ordered-shift or monotone-pivot connectors.

### Theorem 5.1 (automatic graphic transversal)

For every (J\subseteq I),

\[
\boxed{
r_{\rm gr}\!\left(\bigcup_{i\in J}\mathcal E_i\right)\ge |J|.
}
\tag{5.1}
\]

In fact, choosing an arbitrary one edge from every nonempty menu produces a
forest.

### Proof

Choose one connector for every (i\in J).  The tails (p_i) are distinct,
so every rank-(m) root has selected outdegree at most one.  All connectors
are forward under the same potential (phi).  Theorem 2.1 makes their union
a forest of (|J|) edges.  Equation (4.1) says SCD contraction changes none
of its vertices or edges.  Hence its graphic rank is (|J|), proving (5.1).
∎

This is stronger than Rado's condition: no careful topology choice is needed
once the nonempty menus have been prepared.

## 6. Consequence for bounded robust ordered-flag tasks

For (h) prepared roots and (b) foreign resource rows, the robust
ordered-flag theorem gives

\[
|\mathcal E_i|\ge
L:=m+1-(h-1)d-b.
\tag{6.1}
\]

For fixed (h), (d=O(\sqrt m)), and (b=O(hd)), one has (L>0) for all
sufficiently large (m).  The resource-list LLL from the balanced-turn
theorem can therefore choose mutually compatible literal portals.  Whatever
conflict-free choices it returns, Theorem 5.1 says their connector links are
already graphic-independent.

If each complete protected portal/collar uses (O(d)) incidence edges, a
fixed bank uses (O(hd)=O(\sqrt m)<m-2).  The small protected-factor theorem
then embeds the selected incidence bank in a spanning q1 two-factor.

Hence the following local row is closed:

> A bounded bank of distinct prepared ordered-flag or monotone-pivot tasks
> has conflict-free literal portals whose SCD links are graphic-independent,
> and the chosen protected bank embeds in a q1 factor for all sufficiently
> large (m).

This statement does not choose the flags on the unprepared roots and does not
prove named lower exactness, upper decoration, bounded component count, or the
multi-order selector.

## 7. Positive-density prospective tasks

Theorem 5.1 itself has no boundedness hypothesis.  If a prospective Boolean
or pivot construction supplies nonempty monotone menus at (alpha N)
distinct tail roots, then an arbitrary transversal gives a forest of
(alpha N) connectors.  Thus the prospective graphic rank is
positive-density automatically.

What does not follow is literal realization in one exact factor:

* The bounded prepared-order theorem loses its degree bound when
  (h) is positive-density.
* The protected-factor extension theorem only embeds a bank of at most
  (m-2) incidence edges, not a Catalan/exponential-size bank.
* Named lower exactness still requires the unresolved multi-order flag
  selector.

So for positive density the Rado row is solved **conditional on menu
existence**, while menu production and simultaneous host embedding remain
open.

## 8. Exact Rado obstruction after previous contractions

Let (kappa) now be an arbitrary contraction of rank-(m) roots into current
chronology/SCD components.  Portal menus become edge sets

\[
\overline{\mathcal E}_i=
\{\kappa(p_i)\kappa(q):q\in Q_i\}
\]

in an ambient component graph (K).  Loops are allowed and have graphic rank
zero.

For a graphic flat (F\subseteq E(K)), define

\[
I_F=\{i:\overline{\mathcal E}_i\subseteq F\}.
\]

### Theorem 8.1 (sharp graphic-flat cut)

There is an independent transversal of all portal menus if and only if

\[
\boxed{|I_F|\le r_{\rm gr}(F)
\quad\text{for every graphic flat }F.}
\tag{8.1}
\]

More generally, the exact number of tasks which must remain unserved is

\[
\boxed{
\delta_{m gr}
=\max_F\bigl(|I_F|-r_{\rm gr}(F)\bigr)_+.
}
\tag{8.2}

### Proof

Rado's theorem says an independent transversal exists exactly when

\[
r_{\rm gr}\!\left(\bigcup_{i\in J}\overline{\mathcal E}_i\right)
\ge |J|
\quad(J\subseteq I).
\tag{8.3}
\]

Given (J), take the graphic closure
(F=\operatorname{cl}(\bigcup_{i\in J}\overline{\mathcal E}_i)).  Then
(J\subseteq I_F) and the ranks agree, so every violation of (8.3) yields a
violation of (8.1).

Conversely, take (J=I_F).  Its menu union lies in (F), so a violation of
(8.1) violates (8.3).  The same two substitutions applied to the matroidal
Hall-deficiency formula prove (8.2).  ∎

When the ambient component graph is complete, graphic flats correspond to
partitions (Pi) of the component vertices.  Let (Pi(C)) denote the block
containing (C).  A star menu is trapped in the partition flat precisely
when

\[
\kappa(q)\in\Pi(\kappa(p_i))
\quad\text{for every }q\in Q_i.
\]

Thus (8.1) becomes the sharp cut condition

\[
\boxed{
\#\{i:\text{every portal head of }i\text{ lies in the tail block}\}
\le |V(K)|-|\Pi|
\quad\text{for every partition }\Pi.
}
\tag{8.4}

This is the requested exact cut obstruction.

## 9. A private-head theorem under bounded component congestion

Although (8.4) is exact, a simpler sufficient condition is useful for bounded
tasks.  Put

\[
\mu=max_{i,C}
|\{q\in Q_i:\kappa(q)=C\}|,
\tag{9.1}
\]

the maximum number of heads from one menu collapsed into one current
component.

### Theorem 9.1 (bounded private-head selection)

Let there be (h) tasks and suppose every menu has at least (L) literal
heads.  If

\[
\boxed{L\ge2h\mu,}
\tag{9.2}

then the contracted menus have an independent transversal.

### Proof

Let (A) be the set of tail components, so (|A|\le h).  At most (h\mu)
heads of one menu lie in (A).  The remaining heads occupy at least

\[
{L-h\mu\over\mu}\ge h
\]

distinct components outside (A).  Therefore the task-to-outside-component
bipartite graph satisfies Hall: every nonempty task subfamily has a union of
at least (h), hence at least its own cardinality, head components.  Choose
distinct outside head components.  Every chosen head is outside all tail
components and is used once, so it is a leaf of the selected connector graph.
The selected graph is a forest.  ∎

If every current component contains at most (B) rank-(m) roots, then
(mu\le B).  For fixed (h), the robust list size (L=m-O(hd)) therefore
closes the Rado row whenever (B=o(m)).

## 10. Why robust portal degree alone is insufficient after contraction

The ordered-flag theorem proves a linear number of distinct head roots and
pair-codegree one against named foreign resource rows.  It does not bound
(mu).

Indeed, a current component may contain the tail (p_i) and every one of its
(L=\Omega(m)) distinct ordered-shift heads.  After contraction the entire
menu consists of loops and has rank zero.  One task already violates Rado.
More generally, a partition may trap too many whole menus and violate (8.4).

This is sharp: no lower bound on literal menu size, and no resource-row
pair-codegree bound, can rule out the partition obstruction without a
component-scattering or private-endpoint hypothesis.

## 11. Exact remaining host statement

For bounded tasks on unmerged SCD chains, the graphic row is now proved.
For previously merged or recursively regenerated hosts, the remaining
topology assertion can be stated minimally as either:

1. the exact flat inequalities (8.1)/(8.4); or
2. the stronger component-congestion estimate (9.2); or
3. a protected private head component for every prepared packet.

The pivot/collar construction has fresh labelled banks which are natural
private-head candidates.  What is not proved is that the global host
completion leaves their rank-(m) endpoints in private components.  The
small protected-factor theorem preserves the literal paths, but its arbitrary
completion may merge their surrounding SCD chains.

Therefore the unresolved row is no longer an abstract Rado problem.  It is a
host-scattering theorem: preserve enough distinct SCD component endpoints
while completing the named lower/upper factor.  No multi-order selector has
been assumed here.

