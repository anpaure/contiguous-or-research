# Compiler deletions as a strict gammoid: the Boolean root-slot reserve and the bounded-depth recursion gate

**Date:** 2026-08-01  
**Status:** exact cell-level and abstract root-slot theorems; exact static
positive-menu corollary; conditional physical lift; exact bounded-depth
counterexample and recursive sufficient state.  No additive-constant word
bound is claimed.

## 0. Outcome

This note closes the purely matching-theoretic part of the supply row left
open in item 2536L.

1. In one fixed complete cap state, the cell sets whose deletion preserves a
   compiler matching are exactly the independent sets of a strict gammoid:
   the dual of the compiler's cell transversal matroid.  This is an exact
   occurrence-labelled statement, not a scalar-capacity surrogate.

2. On the rank-separated Boolean root-slot face, deleting every depth slot
   over any at most \(m+1\) rank-\(m\) roots preserves all high-rank target
   matchings simultaneously.  The uniform number \(m+1\) is sharp: the
   \(m+2\) roots over one rank-\((m-1)\) facet isolate that facet.

3. Under an explicit trace-guarded physical root-slot lift **and** an
   independent nonadjacent-center planting (or another bounded full-conflict
   certificate), bounded prepared ordered-flag lists contain linear-size,
   hence positive-density within the local lists, mutually
   collar-compatible submenus whose **entire union** lies in one
   coindependent compiler reserve.  The static resource-compatible reserve
   is unconditional for the complete/path-splice-complete flag atlas when
   the menus are planted before the flexible flags are completed.

4. The existing ingredients do not prove that physical lift.  Separate
   rankwise matchings have quantifiers \(\forall j\,\exists M_j\), whereas
   the compiler needs one cap state and one occurrence matching after the
   union of all ray cells is deleted.  Ordered-shift endpoints are owner
   transitions, not automatically same-neighbour stutter occurrences.

5. Protected Boolean shadow surplus, private endpoints, nonadjacent collars,
   monotonicity, and even a same-parity recursive realization do not bound
   fixed-matching relocation depth.  A literal declared depth-one catalogue
   has a unique augmentation of length \(m+2\).  The correct recursive state is a
   bounded-depth disjoint-path predicate, with a polynomial gammoid/maxflow
   face on constant-height occurrence funnels.  A zero-stretch lift
   preserves it, while one compulsory new site per induction step does not.

Thus there is a genuine positive supply theorem on a maximal concrete face,
and an exact statement of the one remaining occurrence/transition lift.  It
would be unsound to infer that lift from rankwise surplus alone.

## 1. One fixed compiler: safe deletions are a strict gammoid

Fix one complete cap/trace state \(\theta\), and write its bipartite compiler
graph as

\[
                    G_\theta=({\cal T},{\cal C};E_\theta).
\]

Assume \(G_\theta\) has a matching saturating all targets \({\cal T}\).
Let \(M_\theta\) be the transversal matroid on the **cell ground set**
\({\cal C}\): a cell set is independent when it can be matched into distinct
targets.  Then

\[
                         r_{M_\theta}({\cal C})=|{\cal T}|.
\]

Call \(D\subseteq{\cal C}\) safe when
\(G_\theta[\mathcal T,\mathcal C-D]\) still has a target-saturating
matching.

### Theorem 1.1 (exact dual-transversal identity)

The safe deletion sets are exactly the independent sets of
\(M_\theta^*\):

\[
 \boxed{\quad
 D\text{ is safe}
 \iff r_{M_\theta^*}(D)=|D|.
 \quad}                                                        \tag{1.1}
\]

In particular the safe cell-deletion system is a strict gammoid.

#### Proof

Dual rank gives

\[
 r_{M_\theta^*}(D)
   =|D|-r_{M_\theta}({\cal C})
          +r_{M_\theta}({\cal C}-D)
   =|D|-|{\cal T}|+r_{M_\theta}({\cal C}-D).                  \tag{1.2}
\]

This equals \(|D|\) exactly when
\(r_{M_\theta}({\cal C}-D)=|{\cal T}|\), which is precisely the
existence of a matching saturating \({\cal T}\) after deleting \(D\).
The dual of a transversal matroid is a strict gammoid. \(\square\)

There is a useful literal representation.  Fix a target-saturating matching
\(M\).  Direct every matched edge cell-to-target and every unmatched allowed
edge target-to-cell; the unmatched cells are sinks.  Then \(D\) is safe iff
the members of \(D\) have vertex-disjoint directed alternating linkages to
distinct unmatched-cell sinks (trivial paths are allowed for already
unmatched cells).  This is the occurrence-labelled relocation geometry
hidden by a scalar Hall margin.

### Corollary 1.2 (exact safe radius)

Put

\[
 \sigma_\theta=\min_{\varnothing\ne A\subseteq{\cal T}}
                    \bigl(|N_\theta(A)|-|A|\bigr).
\]

The smallest unsafe cell set has size

\[
 \boxed{\quad g(M_\theta^*)=\sigma_\theta+1.\quad}           \tag{1.3}
\]

Consequently every deletion of at most \(\sigma_\theta\) cells is safe,
and the bound is attained by deleting
\(|N(A)|-|A|+1\) cells from a minimizing neighborhood.

#### Proof

If \(D\) is unsafe, Hall supplies nonempty \(A\) with

\[
 |D\cap N(A)|\ge |N(A)|-|A|+1,
\]

so \(|D|\ge\sigma_\theta+1\).  Conversely, for a minimizing \(A\), delete
any \(|N(A)|-|A|+1\) cells of \(N(A)\); fewer than \(|A|\) neighbors
remain. \(\square\)

For one-cell sites (depth one), after collar conflicts have been removed,
site selection is ordinary matroid intersection.  Give every task a
disjoint labelled copy of each of its candidates, let
\(\rho:E\to{\cal C}\) send a candidate copy to its physical cell, and pull
\(M_\theta^*\) back to \(E\), with copies having the same image parallel.
Let the task-labelled lists be the classes of a partition matroid.  Then
\(H\) tasks can all be served iff

\[
 \min_{X\subseteq E}
 \left(r_{M_\theta^*}(X)+r_{\rm part}(E-X)\right)\ge H,        \tag{1.4}
\]

where \(r_{\rm part}(E-X)\) is the number of task classes meeting \(E-X\),
and the first rank is the rank of the just-defined pullback.
For multi-cell rays, pulling back \(M_\theta^*\) through packets need not be
a matroid; item 2536L's packet-augmentation counterexample is exact.

## 2. The sharp Boolean root-slot co-gammoid

Let

\[
 k=2m+1,\qquad
 {\cal R}=\binom{[k]}m,\qquad
 {\cal L}_j=\binom{[k]}{m-j}\quad(1\le j\le d).
\]

Make a disjoint cell copy of every root at every depth,

\[
              {\cal C}_j=\{(q,j):q\in{\cal R}\},
\]

and join \(S\in{\cal L}_j\) to \((q,j)\) iff \(S\subset q\).
Let \(G_{\rm slot}\) be the direct sum of these \(d\) containment graphs.
For \(P\subseteq{\cal R}\), define its complete diagonal fibre bank

\[
              D(P)=\{(q,j):q\in P,\ 1\le j\le d\}.            \tag{2.1}
\]

### Theorem 2.1 (sharp diagonal reserve)

For every \(P\subseteq{\cal R}\) with \(|P|\le m+1\), deleting \(D(P)\)
leaves a matching saturating every target in every \({\cal L}_j\).
Equivalently, \(D(P)\) is independent in the dual transversal matroid of
\(G_{\rm slot}\).

The uniform threshold is sharp: there is an unsafe set of \(m+2\) root
fibres already at \(j=1\).

#### Proof

A fixed \((m-j)\)-target lies in

\[
                D_j=\binom{m+j+1}{j}                           \tag{2.2}
\]

rank-\(m\) roots.  The protected rankwise matching theorem says that the
rank-\(j\) containment graph still saturates \({\cal L}_j\) after deleting
any at most \(D_j-1\) roots.  Since

\[
             D_j-1\ge D_1-1=m+1,
\]

every layer remains matchable after deleting \(P\).  The cell layers are
disjoint, so the layer matchings unite into one matching of their direct
sum.

For sharpness, fix \(S\in\binom{[k]}{m-1}\).  Its neighborhood consists of
exactly the \(m+2\) roots \(S+\{x\}\), \(x\notin S\).  Deleting those
fibres isolates \(S\). \(\square\)

If \(P_0\) is an already unavailable protected root bank of size \(h_0\),
then every further root bank of size at most \(m+1-h_0\) lies in the same
coindependent reserve.  The statement is a guaranteed uniform range: some
larger root banks are also safe, but not all \((m+2)\)-banks are.

## 3. The exact physical root-slot lift

The preceding theorem becomes a theorem about an actual compiler only under
the following literal hypothesis.

### Definition 3.1 (trace-guarded root-slot lift)

A cap state \(\theta\) has a root-slot lift through depth \(d\) if:

1. the target set is typed as
   \[
   {\cal T}=\left(\mathop{\dot\bigcup}_{j=1}^d{\cal L}_j\right)
                  \mathbin{\dot\cup}{\cal T}_{\rm rem};
   \]
2. there are injections
   \(\iota_j:{\cal R}\to{\cal C}\), with pairwise disjoint images;
3. for every \(S\in{\cal L}_j\) and every \(q\supset S\), the physical
   trace-guarded edge
   \((S,\iota_j(q))\in E_\theta\);
4. every target in \({\cal T}_{\rm rem}\) has a fixed matching into cells
   disjoint
   from all slot images and from every candidate ray considered below;
5. each candidate ray \(R_p\) has a hazard-root set
   \(H(p)\subseteq{\cal R}\) such that

   \[
   R_p\cap\bigcup_j\iota_j({\cal R})
       \subseteq\{\iota_j(q):q\in H(p),\ 1\le j\le d\}.       \tag{3.1}
   \]

The hazard width is \(a=\max_p|H(p)|\).  The desired diagonal stutter lift
has \(a=1\), but that identification is a hypothesis, not a consequence of
rankwise containment.

### Theorem 3.2 (physical coindependent reserve)

Under Definition 3.1, let \({\cal P}\) be any candidate bank.  If

\[
 \boxed{\quad
   \left|P_0\cup\bigcup_{p\in{\cal P}}H(p)\right|\le m+1,
 \quad}                                                        \tag{3.2}
\]

then the complete ray union \(\bigcup_{p\in{\cal P}}R_p\) is safe in the
actual compiler graph \(G_\theta\).

#### Proof

Use Theorem 2.1 on root slots outside the union in (3.2), and unite those
layer matchings with the fixed matching from Definition 3.1(4).  Candidate
ray cells outside the slot images miss this matching; candidate cells in a
slot image occur only above a deleted hazard root.  Hence the displayed
matching survives the full ray union. \(\square\)

The cap state \(\theta\) is common to the entire bank.  Taking a union of
incidence edges from different cap states would not prove (3.2).

## 4. A linear local menu inside one reserve

The next result combines the root-slot theorem with the ordered-flag/private
endpoint supply and the nonadjacent-center collar theorem.

### Theorem 4.1 (conditional positive local density)

Fix \(H\ge1\) tasks.  Suppose task \(i\) has a candidate list \(V_i\) with
\(|V_i|\ge L_0\), and suppose:

* the cross-task conflict graph records every same-center collision, every
  failed adjacent-center row, and every shared protected endpoint/resource,
  and has maximum degree \(\Delta\);
* every candidate has hazard width at most \(a\ge1\) in one common root-slot
  lift;
* \(h_0\) root fibres are unavailable before these menus are planted.

Put

\[
 \ell=\left\lfloor\min\left\{
       {L_0\over1+\Delta(H-1)},
       {m+1-h_0\over aH}
       \right\}\right\rfloor.                                 \tag{4.1}
\]

Then one can retain \(U_i\subseteq V_i\), \(|U_i|=\ell\), so that:

1. no two candidates in different retained menus conflict;
2. the union of **all** retained ray packets lies in one coindependent
   compiler reserve.

Thus any later one-per-task choice is simultaneously collar-compatible and
compiler-safe.

In particular the retained menu is nonempty whenever

\[
 L_0\ge1+\Delta(H-1)
 \quad\text{and}\quad
 m+1-h_0\ge aH.                                                \tag{4.2}
\]

The case \(H=0\) is vacuous.  If \(a=0\), every ray misses the slot
matching and the second term of (4.1) is interpreted as \(+\infty\).

#### Proof

Process the lists in order.  After \(i-1\) lists have been retained, their
\((i-1)\ell\) vertices forbid at most \(\Delta(i-1)\ell\) vertices of
\(V_i\).  The first bound in (4.1) leaves at least \(\ell\) choices.  At
the end, the union of all hazard-root sets has size at most \(aH\ell\).
The second bound and Theorem 3.2 put the entire retained bank in one safe
reserve. \(\square\)

For the prepared ordered-shift lists, the theorem currently proves only the
**resource-conflict** row

\[
 L_0=m+1-(H-1)d-b,
 \qquad \Delta_{\rm res}\le3(H-1).                            \tag{4.3}
\]

If the candidates are independently planted on one nonadjacent chronology
bank, the adjacent-center rows vanish and the full conflict degree in
Theorem 4.1 is \(\Delta=\Delta_{\rm res}\).  More generally one may use
(4.1) with any separately proved bound on the failed-cross conflicts.
The ordered-flag theorem alone supplies no chronology centers and therefore
does not prove this last planting row.

Under such a nonadjacent or bounded-cross planting, fixed \(H,a,h_0\) and
\(d,b=o(m)\) give \(\ell=\Theta_H(m)\): a positive fraction of each local
linear list, not a positive fraction of all \(\binom{2m+1}m\) roots.  If
the intended ordered endpoints also admit the width-one physical stutter
lift, this is the nonempty/positive-menu theorem requested by item 2536L.

### Theorem 4.2 (unconditional static planted-menu reserve)

There is already an unconditional static version.  Fix \(H\) prepared tail
roots, and use their common robust order.  Let \(L_0\) be as in (4.3), and
put

\[
 \ell_{\rm stat}=\left\lfloor\min\left\{
 {L_0\over1+3(H-1)^2},
 {m+1-H\over H}
 \right\}\right\rfloor.                                      \tag{4.4}
\]

One can retain \(\ell_{\rm stat}\) pairwise **resource-compatible**
ordered-shift heads per tail, freeze every tail and retained head flag, and
then complete all flexible flags so every high lower target has an
occurrence on a flexible root.  Therefore every cell on every prepared flag
belongs to one coindependent reserve of the static occurrence transversal
matroid.  This static statement has no chronology/collar conclusion.

#### Proof

The cross-list resource degree is at most \(3(H-1)\).  Sequential pruning as in
Theorem 4.1 works because

\[
 1+\Delta_{\rm res}(H-1)\le1+3(H-1)^2.
\]

Heads are distinct within one list, and shared head/owner rows were included
as resource conflicts across lists.  There are at most
\(H+H\ell_{\rm stat}\le m+1\) prepared roots.  The protected
complete-atlas theorem then chooses
the other root flags so that all named targets are represented by flexible
tokens alone.  Match each target to its assigned flexible occurrence; this
matching avoids the complete prepared flag bank. \(\square\)

The quantifier order is essential:

\[
 \text{plant tail/head menus first}\quad\longrightarrow\quad
 \text{complete all flexible flags}.                           \tag{4.5}
\]

This theorem does not identify an ordered-shift owner transition with a
same-neighbour stutter ray, and it does not place the static occurrence
matching inside one transition-compatible physical cap state.  Those two
identifications are exactly the live lift.

## 5. The exact laminar face

The strict-gammoid statement also yields a useful interval/laminar
criterion.  Suppose a cut-complete laminar cell family \({\cal J}\) has the
property that compiler Hall after deletion of \(D\) is equivalent to

\[
 |D\cap J|\le s(J),\qquad
 s(J)=|J|-\#\{t:N(t)\subseteq J\},
 \qquad J\in{\cal J}.                                        \tag{5.1}
\]

For occurrence-disjoint ray packets, this is exactly

\[
 \boxed{\quad
   \sum_{p\in P}|R_p\cap J|\le s(J)
       \qquad(J\in{\cal J}).
 \quad}                                                        \tag{5.2}
\]

If additionally

* \(|R_p\cap J|\in\{0,1\}\) for every site \(p\) and cut \(J\); and
* the site sets \(E_J=\{p:R_p\cap J\ne\varnothing\}\) form a laminar
  family on the site ground set,

then (5.2) is a laminar matroid.  Task lists \(V_i\) have an independent
representative system iff the exact Rado cuts

\[
 r_{\cal J}\!\left(\bigcup_{i\in I}V_i\right)\ge |I|
       \qquad(I\subseteq[H])                                  \tag{5.3}
\]

hold.  This is one exact ordinary-matroid face of the packet problem.  A
coefficient two in (5.2) creates a laminar knapsack for which the matroid
conclusion **can** fail.  Laminar cell intervals alone are therefore not
enough; the 0/1 branch profile is load-bearing.

For an uncontracted nonempty depth-\(d>1\) ray, a cut-complete connected
compiler normally includes the full cell cut \(J={\cal C}\), and then
\(|R_p\cap J|=d\).  Thus the 0/1 face is useful only after a certified packet
contraction, at depth one, or when the cut decomposition splits every ray
so that it meets each relevant component in at most one cell.  It is not a
generic solution for raw full rays.

## 6. Why the current ingredients do not imply the lift

### 6.1 Separate rank surplus is not a common compiler matching

Take two target layers with targets \(x,y\) and two physical cells \(u,v\),
with

\[
                   N(x)=\{u,v\},\qquad N(y)=\{u\}.             \tag{6.1}
\]

Before deletion, use \(y-u,x-v\).  After deleting \(v\), the \(x\)-layer
alone matches through \(u\), and the \(y\)-layer alone also matches through
\(u\); jointly they do not.  Distinct abstract roots, owners, or endpoint
labels do not create a second physical cell.  This is the quantifier gap

\[
        \forall j\ \exists M_j
        \quad\not\Longrightarrow\quad
        \exists M\ \forall j.                                 \tag{6.2}
\]

The determinant-two two-rank flag minor in the protected multi-order note
is the Boolean chain-correlated version of the same obstruction.

Even the full-set Hall row supplies a physical condition absent from a
rankwise shadow estimate.  If \(h\) contracted targets are removed while
\(h\) disjoint depth-\(d\) rays delete \(hd\) cells, then

\[
              |{\cal C}|-|{\cal T}|\ge h(d-1)                 \tag{6.3}
\]

is necessary just by applying Hall to all residual targets.

### 6.2 Ordered endpoints are not stutter occurrences

An ordered-shift portal is the nonloop owner transition

\[
                       p\longrightarrow p-z_1+\beta.
\]

A continuation edge of the fixed-matching relocation network needs more:
a literal same-neighbour stutter at an occurrence \(\lambda\), the identity
\(\lambda=M(Q^-)\) (or a free root port), a second target \(Q^+\), and all
shorter ray cells free from the retained matching.  Protected containment
Hall supplies none of these occurrence labels or cross-return transitions.
Thus the robust endpoint theorem and Theorem 2.1 do not by themselves
produce even one edge of the relocation network.

## 7. Rank surplus does not bound relocation depth

The alternative route in item 2536L was a bounded-depth fixed-matching
relocation theorem.  The natural candidate hypotheses still do not imply
one.

### Theorem 7.1 (literal recursively growing route)

For every \(m\ge3\), put \(k=2m+1\).  Partition the letters into a fixed
set \(K\), \(|K|=m-2\), and indices \(0,1,\ldots,N\), where \(N=m+2\).
Set

\[
                         q_i=K+\{i\}.
\]

For \(0\le i<N\), define depth-one states

\[
\begin{aligned}
 Z_i&=(\{i,i+1\}\mid K),\\
 X_i&=(K+\{i\}\mid\{i+1\}),\\
 X_i^+&=(K+\{i+1\}\mid\{i\}),\\
 A_i&=(K\mid\{i,i+1\}).
\end{aligned}                                                   \tag{7.1}
\]

For \(0\le i<N\), the two bay transitions

\[
 Z_i\to X_i\to Z_i,\qquad
 Z_i\to X_i^+\to Z_i
                                                                    \tag{7.2}
\]

are literal.  For \(0\le i<N-1\), so is the connector
\[
                         Z_i\to A_i\to Z_{i+1}.                \tag{7.3}
\]

There is an open chronology with nonadjacent centers, occurrence-private
rays, and pairwise distinct rank-\(m\) **site-owner** endpoints for which
the declared globally compatible site catalogue's fixed-matching relocation
network is the unique directed path

\[
                       q_0\to q_1\to\cdots\to q_N.             \tag{7.4}
\]

Its unique augmentation uses \(N=m+2\) sites.  Meanwhile the full Boolean
rank-\((m-1)\)-to-rank-\(m\) containment graph has the protected
\(m+1\)-root surplus of Theorem 2.1.  The construction embeds under
\(k\mapsto k+2\) by adding one fixed letter to \(K\) and one terminal
index, increasing the unique route by one.

#### Proof

Equations (7.2)--(7.3) follow by direct comparison of the displayed blocks;
the fixed block \(K\) is carried unchanged.  Concatenate two \(X_0\) bays,
then the connector and bay blocks for \(i=1,\ldots,N-1\), exactly as in the
depth-one construction of item 2536L.  Match \(q_0\) at the first \(X_0\),
leave the second \(X_0\) port free, match \(q_i\) at \(X_i\) for
\(1\le i<N\), and leave \(q_N\) unmatched.  Each freed matched occurrence
has only the next continuation in the declared catalogue, so (7.4) is its
complete reachable network.  The connector bays separate centers and the
site owners \(K+\{i,i+1\}\) are distinct.

The retained \(q_0\) provider and the root site are two occurrences of the
same \(X_0\) owner.  Thus this theorem asserts site-owner distinctness and
ray occurrence privacy, not privacy of every background provider endpoint.
Nor does it classify every other individually legal stutter that might
exist in the ambient chronology; the obstruction is exact for the declared
catalogue.

Adding one new fixed letter to every block and appending the next terminal
block preserves all old incidences.  This proves the recursive statement.
The protected shadow surplus belongs to the ambient Boolean containment
graph and is unaffected by this unique occurrence routing. \(\square\)

Thus monotone site-owner endpoint supply, occurrence-private rays, and
rankwise expansion do not control alternating distance.  In fact \(q_0\)
and \(q_N\) are Johnson-adjacent, so even bounded target metric does not
control it.  Occurrence-labelled port alignment is essential.  The relevant
local degree is

\[
 \deg_{{\rm cont},M}(q)=
 |\{p:Q^-(p)=q,\ \lambda_p=M(q),\
       p\text{ is collar/cap eligible}\}|,                    \tag{7.5}
\]

not the number \(m+2\) of Boolean owners containing \(q\).  In the
construction, every internal continuation degree is one.

### Definition 7.2 (bounded-depth relocation state)

For a fixed matching \(M\), let \(\Gamma_M\) be item 2536L's
node-capacitated relocation network.  Write \({\rm BD}(H,L,B)\) when, after
every allowed deletion of at most \(B\) protected resource vertices and for
every at most \(H\) designated holes, there are that many mutually
site- and target-disjoint root-to-hole paths in \(\Gamma_M\), each using at
most \(L\) site vertices.

This definition is deliberately a path-packing predicate, not an ordinary
time-expanded maxflow claim.  Duplicating a physical vertex at several time
layers loses its shared capacity; forcing all copies through one common gate
can permit an invalid jump between time layers.  Thus a general
length-bounded disjoint-path instance is not certified here as a gammoid or
as a polynomial maxflow problem.

For \(H=1\), the state can be read without time expansion.  If
\(R_0\) is the set of targets reached by root-eligible sites, define

\[
 R_{\ell+1}=R_\ell\cup
 \{Q^+(p):Q^-(p)\in R_\ell, M(Q^-(p))=\lambda_p\}.            \tag{7.6}
\]

A hole has an augmentation using at most \(L\) sites exactly when it lies
in the corresponding \(R_{L-1}\), with the direct-site convention at
\(L=1\).

There is, however, an exact integral face.  Call a catalogue an
\(L\)-**funnel** when its reachable targets have levels
\(\ell(q)\in\{0,\ldots,L-1\}\), every root site enters level zero, and every
continuation arc strictly increases the level.  Then every directed path
has at most \(L\) sites, so ordinary node-capacitated maxflow in
\(\Gamma_M\) is exactly the bounded-depth packing.  Equivalently its
terminal-linkage system is the usual strict gammoid of this acyclic funnel.

### Proposition 7.3 (zero-stretch recursion)

Suppose a same-parity child construction injects every inherited root and
continuation site, target, matching port, and protected resource into the
child without increasing site length.  Require additionally that:

1. for every allowed child deletion \(F'\) of size at most \(B\), its
   pullback on the inherited image is an allowed parent deletion of size at
   most \(B\);
2. inherited holes map to the same targets; and
3. every genuinely new hole has a direct root bay, with those bays pairwise
   disjoint, disjoint from all inherited path images, and surviving every
   allowed \(F'\).

Then

\[
                 {\rm BD}(H,L,B)\Longrightarrow
                 {\rm BD}(H,\max\{L,1\},B).                   \tag{7.7}
\]

If instead every lift inserts \(c\) compulsory terminal sites on inherited
paths, the only general conclusion is \(L_{t+1}\le L_t+c\).  Iteration gives
\(L_t\le L_0+ct\), so an all-dimensional constant needs \(c=0\) or an
explicit bounded reset.

#### Proof

Inject a witnessing disjoint path family path-by-path.  The hypotheses
preserve all vertex capacities and all forbidden-resource avoidance; append
the disjoint direct bays for new holes.  This proves (7.7).  On an
\(L\)-funnel the same argument is an ordinary integral maxflow proof, and a
zero-stretch lift preserving the level function preserves the funnel face.
With \(c\)
mandatory sites, appending them proves only the displayed additive
recurrence.  The chain in Theorem 7.1 attains the \(c=1\) accumulation.
\(\square\)

## 8. Exact remaining theorem

There are now two proof-safe ways to close the supply row.

1. **Physical root-slot lift.**  Realize the prepared ordered endpoint
   submenus of Theorem 4.1 as width-one same-neighbour stutter rays in one
   cap state satisfying Definition 3.1.  The whole linear menu bank is then
   coindependent before any one-per-task selection.

2. **Zero-stretch bounded-depth lift.**  Export the full state
   \({\rm BD}(H,L,B)\), not merely rank Hall or strong connectivity, through
   the same-parity recursion of Proposition 7.3.

The unconditional static theorem 4.2 proves that the first route has enough
abstract flags and endpoints.  Theorem 7.1 proves that neither protected
rankwise matching surplus nor ordered/private endpoint data supplies the
missing occurrence realization.  This is the exact scope boundary; no
\(O(1)\) sidecar or \(B(k)+O(1)\) conclusion is asserted without one of
these two lifts.
