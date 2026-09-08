# Adaptive protected recourse and exact supplier-deficiency contraction

**Date:** 2026-08-03

**Status:** unconditional abstract matching theorem, exact all-shore and
augmentation-surplus criteria, exact deficient-Rado recurrence, and smallest
representation-recourse counterexample.  This note does not assert that the
criterion holds for the
canonical K17 deficiency-21 parent or for any all-dimensional replacement
host.  It makes no computational claim and does not reuse a parent-local
supplier incidence after a representation change.

## 1. Adaptive protected steps

A protected packet state is a digest-bound tuple

\[
 \Pi=(C,S,T,{\cal P},\Omega,{\cal R},{\cal K}),
 \qquad T=\operatorname {Overlay}(C,S),                 \tag{1.1}
\]

with the meanings fixed in the regenerative Hall--Benders theorem.  In
particular, \({\cal R}\) contains the representation/common-basis matching
contract, and \({\cal K}\) contains the complete supplier compiler.

For an authorized root action \(z\), let \({\cal X}_\Pi(z)\) be the set of
all exact recourse completions.  A member \(\xi\in{\cal X}_\Pi(z)\) contains
the newly solved representation/common-basis matching, all released or
retained occurrence choices, and every other choice that is not fixed by
\(z\).  The authenticated child is

\[
                    \Pi'=\Phi_\Pi(z,\xi).              \tag{1.2}
\]

Forming (1.2) means, in this order:

1. replay every protected and frozen row;
2. solve the complete representation/common-basis matching;
3. materialize and canonicalize the child table;
4. recompute all active-head predicates and supplier incidences from that
   child; and
5. compute a fresh maximum supplier matching.

Thus the supplier graph below is a function of the complete pair \((z,\xi)\),
not of the projected root-action bits alone.

Fix an authenticated semantic universe \({\cal H}\) of potential hard heads
and a semantic supplier universe \({\cal U}\) large enough for the parent and
all children under discussion.  A head absent from one state is declared
inactive there.  If such a common semantic identification is unavailable,
only the scalar deficiencies can be compared; instantiated shores, edges,
and DM components cannot be transported.

For a complete state \(\theta\), write

\[
 a_h(\theta)\in\{0,1\},\qquad
 e_{hu}(\theta)\in\{0,1\}.                              \tag{1.3}
\]

Introduce a private dummy supplier \(\bot_h\) for every \(h\in{\cal H}\)
and define the **completed supplier graph**

\[
 \widehat G_\theta=
 \left({\cal H},\ {\cal U}\mathbin{\dot\cup}
             \{\bot_h:h\in{\cal H}\};\ \widehat E_\theta\right),\tag{1.4}
\]

where an inactive head has only the edge \(h\bot_h\), while an active head
has precisely its actual supplier edges:

\[
 \widehat E_\theta=
 \{h\bot_h:a_h(\theta)=0\}
 \ \dot\cup\
 \{hu:a_h(\theta)=1,\ e_{hu}(\theta)=1\}.              \tag{1.5}
\]

For \(Q\subseteq{\cal H}\), put

\[
 g_\theta(Q)=|N_{\widehat G_\theta}(Q)|
 =\sum_{h\in Q}(1-a_h(\theta))
  +\sum_u\bigvee_{h\in Q}
       \bigl(a_h(\theta)\wedge e_{hu}(\theta)\bigr),    \tag{1.6}
\]

\[
 \kappa_\theta(Q)=|Q|-g_\theta(Q),\qquad
 \delta(\theta)=\max_{Q\subseteq{\cal H}}\kappa_\theta(Q). \tag{1.7}
\]

The private-dummy completion is exact.  If \(A\) and \(I\) are the active
and inactive heads, respectively, then

\[
 \nu(\widehat G_\theta)=|I|+\nu(G_\theta[A,{\cal U}]),
 \qquad
 |{\cal H}|-\nu(\widehat G_\theta)
   =|A|-\nu(G_\theta[A,{\cal U}]).                       \tag{1.8}
\]

Indeed all private dummy edges can be added independently, and the remaining
matching is exactly an active-head supplier matching.  Hence (1.7) is the
literal supplier deficiency even when a recourse step activates or retires
heads.

## 2. Exact all-cut exchange--expansion theorem

Let \(\theta\) be a parent state with \(\delta=\delta(\theta)\ge1\), and let
\(\theta'\) be one fully recomputed protected child.

### Theorem 2.1 (minimal erosion budget)

The following are equivalent.

1. The child contracts supplier deficiency by at least one:

   \[
                         \delta(\theta')\le\delta-1.     \tag{2.1}
   \]

2. Every semantic shore obeys the exact exchange--expansion inequality

   \[
   \boxed{
    g_{\theta'}(Q)-g_\theta(Q)
       \ge \kappa_\theta(Q)-\delta+1
       \qquad(Q\subseteq{\cal H}).}                     \tag{2.2}
   \]

Thus a parent maximum-deficiency shore must gain at least one net Hall
neighbor, a shore of deficiency \(\delta-1\) may lose none, and a shore with
\(t\) units of additional slack may lose at most \(t-1\).

#### Proof

For every \(Q\),

\[
 \kappa_{\theta'}(Q)
 =\kappa_\theta(Q)-
    \bigl(g_{\theta'}(Q)-g_\theta(Q)\bigr).              \tag{2.3}
\]

Inequality (2.2) is therefore equivalent, shore by shore, to
\(\kappa_{\theta'}(Q)\le\delta-1\).  Taking the maximum over \(Q\) proves
the equivalence. \(\square\)

The neighborhood function \(g_\theta\) is submodular, so \(\kappa_\theta\)
is supermodular.  Consequently the family

\[
       {\cal T}_\delta(\theta)
        =\{Q:\kappa_\theta(Q)=\delta\}                  \tag{2.4}
\]

is closed under union and intersection.  This is the exact deficient-shore
lattice.  Representation-dependent edge loss is why the inequalities for
the near-tight shores outside (2.4) remain necessary in (2.2).

Indeed, \(N(A\cup B)=N(A)\cup N(B)\) and
\(N(A\cap B)\subseteq N(A)\cap N(B)\), which proves submodularity of
\(g_\theta\).  If \(A,B\) both maximize the supermodular function
\(\kappa_\theta\), supermodularity and the upper bound \(\delta\) force both
\(A\cup B\) and \(A\cap B\) to attain the same maximum.

### Corollary 2.2 (erosion-free child)

Suppose

\[
                     g_{\theta'}(Q)\ge g_\theta(Q)
                     \qquad(Q\subseteq{\cal H}).        \tag{2.5}
\]

Then (2.1) holds if and only if

\[
       g_{\theta'}(Q)\ge g_\theta(Q)+1
       \qquad(Q\in{\cal T}_\delta(\theta)).             \tag{2.6}
\]

In particular, literal edge addition in the completed supplier graph is one
sufficient way to obtain (2.5).  A recomputed representation generally does
not have this monotonicity.

#### Proof

Under (2.5), (2.2) is automatic when
\(\kappa_\theta(Q)\le\delta-1\); on (2.4) it is exactly (2.6). \(\square\)

Checking only one incumbent maximum shore is not equivalent to (2.6): the
tight lattice may contain several shores.  When incidences may disappear,
even expansion of every previously tight shore is insufficient unless the
near-tight erosion budgets in (2.2) are also checked.

## 3. Exact DM form

Put

\[
                  r=\nu(\widehat G_\theta)
                    =|{\cal H}|-\delta.                 \tag{3.1}
\]

### Theorem 3.1 (rank-preserving recourse plus augmentation)

The child contracts deficiency by at least one if and only if there are

1. a matching \(M_0\subseteq\widehat G_{\theta'}\) of size \(r\); and
2. an \(M_0\)-augmenting path in \(\widehat G_{\theta'}\).

Thus the weakest operational decomposition is:

\[
 \boxed{\text{recompute a child carrying the old matching rank, then expose
 an augmenting path in that same child.}}                \tag{3.2}
\]

#### Proof

The two clauses augment to a child matching of size \(r+1\), which is
equivalent to deficiency at most \(\delta-1\) by (1.8).  Conversely, from a
child matching of size at least \(r+1\), retain \(r+1\) edges and delete one
of them.  The remaining \(r\)-edge matching is \(M_0\), and the deleted edge
itself is an \(M_0\)-augmenting path of length one. \(\square\)

This theorem is deliberately child-local.  An augmenting path in the old
DM digraph has no force if the recomputed representation deletes an edge of
the old matching.

For the useful one-edge specialization, let \(K\) be a child-local baseline
graph with a maximum matching \(M_0\) of size \(r\).  Orient unmatched edges
left-to-right and matched edges right-to-left.  Let \(R_L\) be the left
vertices reachable from an unmatched left vertex, and let \(C_R\) be the
right vertices from which an unmatched right vertex is reachable.  If one
new edge \(hu\) is added to \(K\), it raises the rank if and only if

\[
                         h\in R_L,\qquad u\in C_R.       \tag{3.3}
\]

Indeed a maximum baseline matching has no old augmenting path, so any new
augmenting path uses \(hu\); its prefix and suffix give the two reachability
conditions, and conversely those paths concatenate through \(hu\).

## 4. Smallest representation-recourse counterexample

Let

\[
 {\cal H}=\{a,b\},\qquad {\cal U}=\{1,2\}.              \tag{4.1}
\]

Both heads are active.  The parent and recomputed child supplier graphs are

\[
 E=\{a1,b1\},qquad E'=\{b1,b2\}.                       \tag{4.2}
\]

To make the representation dependence literal, take the representation graph
with left shore \(\{p,q\}\), right shore \(\{P,Q\}\), and all four edges.
Use the feasible perfect matching

\[
 R=\{pP,qQ\}\quad\hbox{in the parent},\qquad
 R'=\{pQ,qP\}\quad\hbox{in the child},                  \tag{4.2a}
\]

and let the complete supplier compiler output \(E\) on \(R\) and \(E'\) on
\(R'\).  The root action releases the second completion and the compiler is
rerun.  All protected rows may be taken empty, so both are valid abstract
protected packets.

The parent has matching rank one and deficiency one.  Its maximum shore
\(Q=\{a,b\}\) has neighborhood \(\{1\}\).  Relative to the old maximum
matching \(\{a1\}\), the newly exposed edge \(b2\) is exactly an old-DM
augmenting bridge from the unmatched left vertex \(b\) to the unmatched
right vertex \(2\).  Moreover the old maximum shore gains the requested net
credit:

\[
              |N_{E'}(\{a,b\})|-|N_E(\{a,b\})|=2-1=1.  \tag{4.3}
\]

Nevertheless the representation recomputation simultaneously deletes
\(a1\).  The child still has matching rank one and deficiency one, now
witnessed by the new shore \(\{a\}\).  In (2.2), that shore had parent
deficiency zero and therefore was allowed no erosion, but

\[
              g_{\theta'}(\{a\})-g_\theta(\{a\})=-1.    \tag{4.4}
\]

This refutes each of the following unrestricted claims:

* one new supplier identity on the incumbent shore forces contraction;
* one edge crossing the old DM frontier forces contraction; and
* positive local edge or degree gain survives arbitrary representation
  recourse.

The example is smallest by left-shore size.  With one potential head, parent
deficiency one means that its only shore has no neighbor; a gain of one on
that shore necessarily makes the child deficiency zero.

There is a separate erosion-free warning.  On
\({\cal H}=\{a,b,c\}\), \({\cal U}=\{1,2,3\}\), take

\[
 E=\{a1,b1,c2\},\qquad E^+=E\cup\{c3\}.                 \tag{4.5}
\]

The parent has deficiency one.  Both \(\{a,b\}\) and
\(\{a,b,c\}\) are tight.  The added edge expands the latter shore from two
neighbors to three, but \(\{a,b\}\) still has only neighbor \(1\), so the
deficiency remains one.  Thus even under literal edge addition, improving
one maximum shore need not improve every member of the tight lattice;
Corollary 2.2 really requires all parent-tight shores, not only the shore
returned by one maximum-matching implementation.

## 5. Adaptive contraction corollary and quantifiers

### Corollary 5.1 (adaptive protected contraction)

Fix a target \(d\).  Suppose that for every authenticated protected state
\(\Pi\) with \(\delta(\Pi)>d\), there are an authorized action \(z\) and an
exact recourse completion \(\xi\in{\cal X}_\Pi(z)\) such that the fully
recomputed child satisfies (2.2), equivalently Theorem 3.1.  Then an adaptive
controller reaches deficiency at most \(d\) in at most
\(\max\{\delta(\Pi_0)-d,0\}\) accepted steps.

#### Proof

Choose the certified pair \((z,\xi)\) at each nonterminal state.  Theorem 2.1
decreases the nonnegative integer deficiency by at least one. \(\square\)

The quantifier in Corollary 5.1 is

\[
                 \forall\Pi\ \exists z\ \exists\xi.    \tag{5.1}
\]

If an action must contract independently of hidden or adversarial recourse,
the required quantifier is instead

\[
                 \forall\Pi\ \exists z\ \forall\xi
                 \in{\cal X}_\Pi(z).                    \tag{5.2}
\]

A deterministic materializer supplies at most one existential witness.  Its
failure neither refutes (5.1) nor licenses a projected no-good without the
universal recourse proof already required by recursive Hall--Benders.

For the canonical K17 deficiency-21 parent, on the frozen face with exactly
\(16{,}898\) active hard heads, a one-step target-20 theorem must therefore
produce, in one freshly authenticated child, either

* a matching of size \(16{,}877\) together with a child-local augmenting path,
  yielding size \(16{,}878\); or
* the complete all-shore inequalities (2.2).

Gaining one net credit on the incumbent `23/2` shore is necessary but not
sufficient when the representation/common-basis matching and supplier graph
are rebuilt.  Nothing here proves that either exact contraction certificate
exists on the 114,594-mode parent-local catalogue.

If a transition changes the active-head set, the numerical form above must be
replaced by the completed-graph statement

\[
 \nu(\widehat G_{\theta'})\ge |{\cal H}|-20,           \tag{5.3}
\]

or, equivalently, by

\[
 \nu(G_{\theta'}[A_{\theta'},{\cal U}])
       \ge |A_{\theta'}|-20.                           \tag{5.4}
\]

It is not sound to keep the denominator \(16{,}898\) after changing that
semantic universe.

## 6. Several units and the exact fixed-fraction target

Theorem 2.1 has the following exact, and useful, multi-unit form.

### Theorem 6.1 (all-shore target criterion)

Let \(D\ge0\) be an integer.  For one fully recomputed child,

\[
 \delta(\theta')\le D                                   \tag{6.1}
\]

if and only if

\[
 \boxed{
 g_{\theta'}(Q)-g_\theta(Q)
       \ge \kappa_\theta(Q)-D
       \quad(Q\subseteq{\cal H}).}                    \tag{6.2}
\]

In particular, contraction by an integer \(0\le c\le\delta(\theta)\) is
obtained by putting \(D=\delta(\theta)-c\).  For \(0<\varepsilon\le1\) and
\(\beta\ge0\), the exact integer fixed-fraction target is

\[
 D=\left\lfloor(1-\varepsilon)\delta(\theta)+\beta
                                            \right\rfloor. \tag{6.3}
\]

When this \(D\) is nonnegative, the exact integer target difference is
\(c=\delta(\theta)-D=
\lceil\varepsilon\delta(\theta)-\beta\rceil\); it is positive only when
\(\varepsilon\delta(\theta)>\beta\).

#### Proof

Equation (2.3) gives

\[
 \kappa_{\theta'}(Q)\le D
 \quad\Longleftrightarrow\quad
 g_{\theta'}(Q)-g_\theta(Q)\ge\kappa_\theta(Q)-D.
\]

Take the maximum over \(Q\). \(\square\)

A stronger but sometimes easier sufficient row is

\[
 g_{\theta'}(Q)-g_\theta(Q)
       \ge \varepsilon\kappa_\theta(Q)-\beta
       \quad(Q\subseteq{\cal H}),                     \tag{6.4}
\]

because then
\(\kappa_{\theta'}(Q)\le(1-\varepsilon)\kappa_\theta(Q)+
\beta\le(1-\varepsilon)\delta(\theta)+\beta\).
This is an all-shore statement in one child, not a sum of marginal credits
certified in different completions.

## 7. Protected matching cores and a capacity-faithful packet gammoid

The all-shore criterion is exact but does not display the packet mechanism.
The following decomposition does.

### Theorem 7.1 (protected-core gain identity)

Let \(K\) be any bipartite graph satisfying

\[
       K\subseteq \widehat G_\theta\cap\widehat G_{\theta'} . \tag{7.1}
\]

Define

\[
 r_0=\nu(K),\qquad
 \ell=\nu(\widehat G_\theta)-r_0,\qquad
 a=\nu(\widehat G_{\theta'})-r_0.                     \tag{7.2}
\]

Then

\[
              \boxed{\delta(\theta')
                      =\delta(\theta)+\ell-a.}         \tag{7.3}
\]

For any maximum matching \(M\) of \(K\), \(a\) is exactly the maximum number
of pairwise vertex-disjoint \(M\)-augmenting paths in
\(\widehat G_{\theta'}\).

#### Proof

The rank identity in (7.3) follows by subtracting both ranks from the same
left-shore size \(|{\cal H}|\).  A family of \(q\) disjoint augmenting paths
raises \(M\)'s size by \(q\), so \(q\le a\).  Conversely, compare \(M\) with
a maximum child matching.  In their symmetric difference, a component with
one more \(M\)-edge than child-matching edge would augment the child matching,
because every \(M\)-edge belongs to \(K\subseteq\widehat G_{\theta'}\).
Hence no such component exists.  The \(a\) units of rank difference are
therefore carried by \(a\) vertex-disjoint \(M\)-augmenting components.
\(\square\)

The number \(\ell\) is the **core loss** paid for representation recourse.
New augmenting paths have force only after this loss is priced.

### Corollary 7.2 (fixed-parent augmentation surplus)

Fix a parent maximum matching \(M\) of rank

\[
                  r=\nu(\widehat G_\theta).
\]

In one fully recomputed child, let

\[
 M_0=M\cap E(\widehat G_{\theta'}),\qquad
 |M_0|=r-q.                                             \tag{7.4}
\]

If the child contains \(p\) pairwise vertex-disjoint
\(M_0\)-augmenting paths, toggling all of them simultaneously gives

\[
 \nu(\widehat G_{\theta'})\ge r-q+p,\qquad
 \boxed{\delta(\theta')\le\delta(\theta)+q-p.}          \tag{7.5}
\]

Thus the certified lower bound on rank gain is the **augmentation surplus**

\[
                               \sigma=p-q.              \tag{7.6}
\]

The paths must be jointly vertex-disjoint in this same materialized child.
A list of paths obtained from different completions, or paths colliding on
an omitted literal resource, supplies no simultaneous value of \(p\).

If \(p\) is the maximum number of pairwise disjoint
\(M_0\)-augmenting paths, equality holds in (7.5), and
\(\sigma=\nu(\widehat G_{\theta'})-r\) is the exact rank gain.  The symmetric
difference
of \(M_0\) with a maximum child matching has no component containing one
more \(M_0\)-edge, since toggling such a component would augment the maximum
child matching.  Its \(p\) augmenting components therefore account for the
entire rank difference.

The displayed \(q\) depends on the chosen parent maximum matching.  Another
parent maximum matching may retain more edges and decrease \(q\), which can
simplify a nonmaximal certificate.  For maximal \(p\), however, \(p\)
decreases by the same amount, so the exact surplus is representation-
independent once the parent and child graphs are fixed.  More
generally, one may maximize the rank of a common protected core as in
Theorem 7.1; and a child-local matching of size \(r\) makes the operational
retention loss zero even if it uses none of the displayed \(M\)'s edges.
Fixed-\(M\) retention is therefore a sufficient certificate, not an
intrinsic obstruction.

For the requested quantitative recurrence, put
\(\Phi_n=\delta(\theta_n)\).  If constants \(a_0,b\ge0\) and
\(0<\eta\le1\) satisfy, at every accepted step,

\[
 q_n\le a_0\Phi_n+b,\qquad
 p_n\ge(a_0+\eta)\Phi_n,                               \tag{7.7}
\]

for jointly disjoint paths in the same child, then

\[
 \boxed{\Phi_{n+1}\le(1-\eta)\Phi_n+b}                 \tag{7.8}
\]

and hence

\[
 \Phi_n\le(1-\eta)^n\Phi_0+
       \frac b\eta\bigl(1-(1-\eta)^n\bigr).            \tag{7.9}
\]

For a complete carried potential, the same proof applies if the separately
verified accounting row is

\[
 \Phi_{n+1}\le\Phi_n+q_n-p_n+c;                        \tag{7.10}
\]

then \(b\) in (7.8)--(7.9) is replaced by \(b+c\).  This
potential-level row is **UNPROVED** by supplier matching alone: reset,
residence, upper, compiler and every other casualty must be priced in it.

This isolates the two inputs needed from packet technology.  A retention
lemma must upper-bound \(q\); a same-child Rado/flow theorem must lower-bound
\(p\).  LLL, Haxell or menu-counting output contributes to \(p\) only after
the selected packets decode to jointly vertex-disjoint augmenting paths in
that one child.  The two linear coefficients must leave the positive surplus
\(\eta\); separate positive marginal gains do not add.

Now fix one child \(\theta'\), one protected core \(K\), and one maximum
matching \(M\) of \(K\).  A **capacity-faithful packet atlas** consists of

* a directed, vertex-split network \(D\) in which every literal
  head, supplier, address, history, reset, residence, compiler and other
  capacity-one resource used by a route has capacity one;
* a ground set \(P\) of selector ports and the unmatched right vertices of
  \(M\) as sinks; and
* for every occurrence-labelled packet \(u\) in the relevant exposure, or
  in the frozen master universe used below, a menu \(P_u\subseteq P\),

such that every vertex-disjoint linkage of selectors to sinks decodes to
the same number of simultaneous \(M\)-augmenting paths in this one child,
without changing its representation or its protected boundary.  Let
\(\Gamma\) be the resulting strict gammoid on \(P\), and write \(r_\Gamma\)
for its rank.  This definition is a hypothesis: it is not obtained by
placing independently materialized packet incidences into one union graph.

### Theorem 7.3 (exact deficient-Rado packet formula)

For a finite exposed packet set \(U\), put

\[
                  P(X)=\bigcup_{u\in X}P_u .           \tag{7.11}
\]

The maximum number \(m^*(U)\) of packets that can choose distinct ports and
be routed simultaneously is

\[
 m^*(U)=\min_{X\subseteq U}
        \bigl(|U\setminus X|+r_\Gamma(P(X))\bigr).     \tag{7.12}
\]

Equivalently, the exact number left unrepaired is

\[
 \boxed{q^*(U)=|U|-m^*(U)
        =\max_{X\subseteq U}
          \bigl(|X|-r_\Gamma(P(X))\bigr).}             \tag{7.13}
\]

Consequently

\[
 q^*(U)\le q
 \quad\Longleftrightarrow\quad
 r_\Gamma(P(X))\ge |X|-q
       \quad(X\subseteq U).                            \tag{7.14}
\]

#### Proof

Apply Rado's matroid transversal theorem to the family
\((P_u:u\in U)\) in the strict gammoid \(\Gamma\), and subtract (7.12)
from \(|U|\).  Capacity faithfulness converts an independent transversal
into simultaneous augmenting paths. \(\square\)

For one already known exposure \(U\), (7.14) with
\(q=\theta|U|+\gamma\) is the weakest exact rank row.  If the host and atlas
must be frozen before the future exposure is known, first fix a finite
occurrence-labelled master packet universe \(\overline U\), including a
separate menu for every occurrence, and require every later exposure to be a
finite subset of this same \(\overline U\).  The hereditary condition is

\[
 r_\Gamma(P(X))\ge (1-\theta)|X|-\gamma
       \quad\hbox{for every finite }X\subseteq\overline U. \tag{7.15}
\]

This is a convenient uniform sufficient condition, and gives

\[
                 q^*(U)\le\theta|U|+\gamma.            \tag{7.16}
\]

The near-perfect row \(r_\Gamma(P(X))\ge|X|-C\) gives the one-step bound
\(q^*(U)\le C\).  Raw menu sizes, degrees, or separately feasible routes do
not imply any of these rank inequalities.  Repeated packets of the same
structural type cannot be identified: their occurrence labels and literal
resource incidences remain distinct in \(\overline U\).

## 8. Two contraction recurrences

There are two distinct ways in which (7.16) can be used.  Confusing them
reverses the required exposure inequality.

### Corollary 8.1 (terminal supplier deficiency)

Suppose that at every nonterminal state there is one fully materialized
child, a protected core with \(\ell\le L\), and a capacity-faithful bank
satisfying (7.15), with

\[
                    |U|\ge\alpha\delta-b              \tag{8.1}
\]

for constants \(\alpha>0\), \(b,L,\gamma\ge0\), and
\(0\le\theta<1\).  Then

\[
 \boxed{
 \delta'\le
   \bigl(1-\alpha(1-\theta)\bigr)\delta
       +L+(1-\theta)b+\gamma .}                        \tag{8.2}
\]

This has a strict affine contraction coefficient whenever
\(0<\alpha(1-\theta)\le1\).  Writing
\(C_{\rm aff}=L+(1-\theta)b+\gamma\), it guarantees an actual decrease
whenever
\(\delta>C_{\rm aff}/(\alpha(1-\theta))\).  In the one-packet-per-defect
case \(\alpha=1,b=0\), the near-perfect rank row with error \(C_{\rm rk}\)
gives directly

\[
                         \delta'\le L+C_{\rm rk}.       \tag{8.3}
\]

#### Proof

Theorem 7.3 supplies at least
\((1-\theta)|U|-\gamma\) disjoint augmentations, so \(a\) is at least this
large.  Substitute (8.1) and \(\ell\le L\) into (7.3). \(\square\)

### Corollary 8.2 (complete carried-state recurrence)

Let \(V_n\) count every inherited obligation represented in a protected
state, not merely supplier deficiency.  Suppose the next transition exposes
a set \(U_n\) with

\[
 |U_n|\le\lambda V_n+b,\qquad
 V_{n+1}\le q^*(U_n)+c,                                \tag{8.4}
\]

where \(\lambda,b,c,\gamma\ge0\) and \(0\le\theta<1\).  At each \(n\),
suppose one fully recomputed child, its protected core and matching, its
capacity-faithful network, port ground, occurrence menus and strict gammoid
are all fixed before the Rado selection, and satisfy (7.15).  Then

\[
 \boxed{V_{n+1}\le\rho V_n+\beta,\qquad
 \rho=\theta\lambda,\quad
 \beta=\theta b+\gamma+c.}                            \tag{8.5}
\]

If \(\rho<1\),

\[
 V_n\le \rho^nV_0+
       \beta\frac{1-\rho^n}{1-\rho},                  \tag{8.6}
\]

so the carried state is eventually at most \(O(\beta/(1-\rho))\).  The
endpoint \(\rho=1\) gives no uniform bound unless \(\beta=0\) and the initial
state was already bounded.

More precisely,

\[
 V_n\le\max\left\{V_0,\frac{\beta}{1-\rho}\right\},
 \qquad
 \limsup_{n\to\infty}V_n\le\frac{\beta}{1-\rho}.       \tag{8.7}
\]

#### Proof

Use (7.16) in (8.4), then iterate the scalar affine recurrence. \(\square\)

Corollary 8.1 needs a lower bound on the number of exposed opportunities,
because each opportunity supplies rank.  Corollary 8.2 needs an upper bound
on newly exposed obligations, because unrepaired obligations are carried.
Neither inequality implies the other.

If a bank has at most \(H\) packets and each packet can mediate at most \(s\)
independent augmentations, then \(a\le sH\).  Under the assumption that every
new rank unit is mediated by this bank, (7.3) gives

\[
                         \delta'\ge\delta-sH.           \tag{8.8}
\]

Thus a bank of bounded **cardinality** and bounded per-packet rank cannot
contract an unbounded deficiency by a fixed fraction.  A valid all-\(k\)
theorem must instead have an extensive bank of bounded-size packets, or a
bounded number of packets with unbounded certified rank.  A bounded carried
interface is compatible with the former; bounded bank cardinality is not.

## 9. Why the action ground is not a weighted matroid

Even with one fixed supplier graph, matching rank as a function of optional
edges is not a matroid rank.  Let

\[
 x=h_0u_0,\qquad y=h_1u_0,\qquad z=h_0u_1,             \tag{9.1}
\]

and put \(f(S)=\nu((\{h_0,h_1\},\{u_0,u_1\});S)\).  Then

\[
 f(xy)=f(xz)=1,qquad f(x)=1,qquad f(xyz)=2.          \tag{9.2}
\]

Hence

\[
 f(xy)+f(xz)=2<3=f(x)+f(xyz),                          \tag{9.3}
\]

which violates submodularity.  Equivalently, the independent edge sets
\(\{x\}\) and \(\{y,z\}\) violate the matroid augmentation axiom.  Transversal
rank is submodular on a fixed **head** ground set; it is not submodular on a
set of optional supplier edges or root actions.

Representation recourse makes the shortcut still less valid.  In a
\(K_{2,2}\) presentation, let completion \(R_0\) compile both selected head
columns to supplier \(u_0\), and completion \(R_1\) compile both to supplier
\(u_1\).  One singleton action priced under \(R_0\) and another priced under
\(R_1\) appear to give the independent edges \(h_0u_0,h_1u_1\).  But either
one common completion makes the two columns parallel and has rank one.
This is the smallest distinct-supplier obstruction to stitching marginal
prices from different representations.

The counterexample of Section 4 also tensors.  The disjoint union of \(m\)
copies has parent deficiency \(m\) and child deficiency \(m\).  Each copy
exposes an old-DM bridge and the old full tight shore gains one neighbor, but
each recomputation deletes one old matching edge and creates a new singleton
shore.  Thus even an extensive bank of \(m\) locally positive packets can
have zero net contraction.  The protected-core loss or, equivalently, the
complete all-shore erosion budget is indispensable.

## 10. The precise reusable hypothesis and current inventory

Call the conjunction of the following rows
\({\rm JRRX}(\alpha,b,L,\theta,\gamma)\), for **joint
representation-stable Rado expansion**.

The parameters are uniform, with \(\alpha>0\), \(b,L,\gamma\ge0\),
\(0\le\theta<1\), and \(0<\alpha(1-\theta)\le1\).  The quantifier is:
for every reachable authenticated parent \(\Pi\), write \(\vartheta\) for
its complete supplier state.  There exist one authorized action \(z\), one
recourse choice \(\xi\), the child
\(\Pi'=\Phi_\Pi(z,\xi)\), its complete supplier state \(\vartheta'\), and
objects

\[
 K,\ M,\ {\cal D},\ P,\ \overline U,\ (P_u:u\in\overline U),\
 \Gamma                                                     \tag{10.1}
\]

such that all of the following hold before any Rado selection.

1. The joint root-action/common-basis matching, the child and every
   advertised packet incidence are simultaneously materialized and fully
   supplier-replayed; the ultimately selected choices stay in this child.
2. \(K\subseteq\widehat G_\vartheta\cap\widehat G_{\vartheta'}\), \(M\) is a
   maximum matching of \(K\), and
   \(\ell=\nu(\widehat G_\vartheta)-\nu(K)\le L\).
3. \({\cal D},P,\overline U,(P_u)\) and \(\Gamma\) form one
   capacity-faithful atlas in this child.  The actual occurrence-labelled
   exposure \(U\subseteq\overline U\) satisfies
   \(|U|\ge\alpha\delta(\vartheta)-b\).
4. With this child, core, matching, network, port ground, menus and gammoid
   fixed, (7.15) holds for every finite \(X\subseteq\overline U\).

By Corollary 8.1, JRRX gives terminal fixed-fraction contraction.  The exact
weakest one-step scalar condition is simply

\[
                         a-\ell\ge\varepsilon\delta-\beta, \tag{10.2}
\]

or equivalently Theorem 6.1.  JRRX is a uniform hereditary packet-level
sufficient formulation.  For one known exposure, replacing item 4 by the
one-shot cut (7.14) is exact and weaker.  Separate witnesses with quantifiers
\(\forall X\,\exists\theta_X\), different guards for different cuts, or
marginal per-action prices do not instantiate it.

The following inventory is proof-safe.

* **PROVED, local/fractional.**  The corrected pull-clock theorem proves its
  symmetric fractional \(q\in ST\) membership, and the independent rotor
  proof confirms it.  Neither constructs the common integral child or the
  gammoid atlas in JRRX.
* **PROVED, bare static rows.**  The odd-central coatom incidence graph is
  regular and has perfect owner allocations.  Pascal aperture accounting,
  the literal monotone pivot/two-ray compiler, aligned birail telescoping,
  zero-block collapse and bounded compiler eviction hold in their stated
  scopes.  They do not prove (7.15) or a bounded protected core loss.
* **PROVED, conditional regenerative architecture.**  The RSB machinery
  gives fixed-segmentation protected-braid equivalences and bounded state
  accounting once left-total regeneration and the complete packet interface
  are supplied.  Those existence clauses remain **UNPROVED**.
* **PROVED, finite K17 state.**  Handoff item 2580D freezes compressed parent
  `e878bf19...`, final parent `fa491882...`, one joint augmented presentation
  completion, supplier rank `16877/16898`, deficiency 21 and shore `23/2`.
  It also freezes 114,594 structural modes and the stated marginal phase
  catalogues.
* **UNPROVED, even at that K17 parent.**  Item 2580D explicitly requires every
  one- or two-mode child to be simultaneously materialized, occurrence-
  priced and fully supplier-replayed.  Its marginal modes therefore are not
  the ground set of a proved gammoid.  On the fixed 16,898-active-head face,
  target 20 needs one authenticated `16878/16898` child, equivalently the
  same fully recomputed child must satisfy the all-shore certificate (6.2).
  If the active-head set changes, use (5.3)/(5.4) instead.  Credit on the
  incumbent `23/2` shore alone is insufficient.
* **PROVED, static replacement-host alternatives.**  The replacement-host
  theorem gives exact phase Hall factors and a common deletion bounded by
  the two phase deficiencies, or by
  \(\lfloor M_0\rfloor+\lfloor M_1\rfloor\) under its collision-energy
  hypotheses.  This yields static independent ticket transversals, not
  supplier augmenting paths.  Even if the deletion is \(O(1)\) and its
  exceptional shore has one joint conjugate completion, the near-perfect
  \(C=O(1)\) row of Theorem 7.3 follows only after an additional
  capacity-faithful decode to jointly vertex-disjoint \(M\)-augmenting paths
  relative to one common core in the same child.  That decode and fusion are
  **UNPROVED**.

Accordingly the first missing clause within this supplier-deficiency
contraction route is not local B5 circuit existence or fractional pull-clock
membership.  It is one same-host, representation-stable repair-rank
expansion (7.14)/(7.15), together with a bounded core-loss row and the
appropriate exposure inequality.  This is strictly stronger than menu
abundance, ordinary codegree bounds, or the existence of separate phase
factors; other global co-instantiation clauses remain open as stated below.

The exact conditional implication to the additive target is now short.
Assume that a complete regenerative potential satisfies (7.10) and (7.7)
with uniform \(a_0,b,c,\eta\), and that after \(n(k)\) transitions

\[
             (1-\eta)^{n(k)}\Phi_0(k)\le C_0.          \tag{10.3}
\]

If the already proved accounting layer can be instantiated on the same
literal spine in the form

\[
       \nu(k)\le B(k)+A\Phi_{n(k)}+C_{\rm term},        \tag{10.4}
\]

with uniform constants, then

\[
 \nu(k)\le B(k)+
 A\left(C_0+\frac{b+c}{\eta}\right)+C_{\rm term}
       =B(k)+O(1).                                     \tag{10.5}
\]

Equations (7.7), (7.10), (10.3), and their realization on one compatible
literal spine are **UNPROVED** all-\(k\).  Therefore (10.3)--(10.5) are an
exact implication chain, not an unconditional bound.

## 11. Scope

This note proves only a supplier-matching contraction theorem.  It does not
construct a root action, a protected occurrence packing, a replacement host,
an integral chronology, residence, upper/source legality, common-cap or
compiler compatibility, or a contiguous-OR word.  In particular it implies
no unconditional `B(k)+O(1)`, `B+1`, or new value of `nu(k)`.

Proof-bearing inputs:

```text
MATH_THEOREM_K17_JOINT27_REGENERATIVE_HALL_BENDERS_20260803.md
MATH_THEOREM_K17_ROOT_SUBSET_RELEASE_HALL_BENDERS_20260803.md
MATH_THEOREM_REPLACEMENT_HOST_ONE_SHORE_HALL_AND_BOUNDED_BOUNDARY_CONJUGACY_20260803.md
MATH_THEOREM_REPLACEMENT_HOST_PHASE_FACTOR_EXPANSION_AND_BOUNDED_ENERGY_BRIDGE_20260803.md
MATH_THEOREM_FRACTIONAL_PULL_CLOCK_PHASE_TICKET_MEMBERSHIP_AND_WEIGHTED_CONFLICT_ROUNDING_20260803.md
MATH_AUDIT_PULL_CLOCK_URGENT_SIGN_RETRACTION_AND_ROTOR_FALLBACK_20260803.md
MATH_THEOREM_K_ONE_APERTURE_PASCAL_PIVOT_BPLUS1_BRIDGE_20260802.md
MATH_THEOREM_SAME_PARITY_PASCAL_COMPOUND_TASK_BUNDLING_AND_PRIVATE_SOCKET_GATE_20260802.md
MATH_THEOREM_ROTOR_ODD_COATOM_ONECOPY_AND_PROTECTED_OWNER_CIRCUITS_20260802.md
MATH_THEOREM_K_RSB_PROTECTED_FACTOR_BRAID_AND_PASCAL_REGENERATION_20260731.md
MATH_THEOREM_BOUNDED_DEFECT_REGENERATIVE_SPINE_AND_EXPLICIT_O1_CONSTANT_20260731.md
MATHEMATICAL_HANDOFF.md, item 2580D
```
