# Independent audit: Hall-safe tree bow-tie, Boolean spine obstruction, and exact cut charge

**Date:** 2026-08-02  
**Status:** proof audit and unconditional counterexamples.  This note checks
the lower labelled rotor row only.  It does not address upper interval
coverage, residence, an exterior opening, or common-cap compilation.

## 0. Conclusions

Fix an owner/target-exact marked flag table.  The proposed
Hall-safe-tree criterion is correct: for a prescribed distinct-role tree
reservation, residual extendability is exactly a family of capacitated
Hall cut inequalities.  There are, however, two independent barriers to
deducing such a tree from coarse expansion.

1. Strict Hall expansion by one on every proper role set, minimum degree
   two on both shores, interval-convex role lists, and a strongly connected
   union digraph still do not force a connected balanced selector.  The
   smallest example has three roles.
2. Literal Boolean leading-letter menus can have arbitrarily large size
   while the ordered predecessor graph is two disjoint directed cycles.
   Exact length-\((d-1)\) spine overlap, not containment menu size, is the
   missing datum.

For a fixed reserved tree \(R\), the weakest exact verifiable expansion
condition is the cut-charge inequality

\[
       \chi_R(Y)\le \kappa(Y)\qquad(Y\subseteq V).
\]

Thus a positive canonical theorem must construct the flag table and tree
correlatively, or construct a cycle cover with a protected rectangle
absorber.  Random-tree, degree-only, and ordinary two-matroid arguments do
not close this row.

## 1. Re-derivation of the cut charge

Let \(I\) be the roles, \(V\) the fixed-head states, \(N(i)\subseteq V\)
the legal tail list of role \(i\), and

\[
 a(v)=|\{i:h_i=v\}|,
 \qquad a(Y)=\sum_{v\in Y}a(v).
\]

Define the number of roles closed in a tail shore \(Y\) by

\[
 f(Y)=|\{i:N(i)\subseteq Y\}|,
 \qquad \kappa(Y)=a(Y)-f(Y).                    \tag{1.1}
\]

The original instance is feasible exactly when \(\kappa(Y)\ge0\) for
all \(Y\).  This is the closed-shore form of capacitated Hall: every role
whose entire list is contained in \(Y\) must be assigned to one of the
\(a(Y)\) copies there, and any ordinary Hall violation \(X\subseteq I\)
is recovered by taking \(Y=N(X)\).

Now reserve distinct roles \(R\), with chosen tails \(t_i\in N(i)\).  Put

\[
 b_R(v)=|\{i\in R:t_i=v\}|,
 \quad
 r_R(Y)=|\{i\in R:N(i)\subseteq Y\}|,
\]

and

\[
 \chi_R(Y)=b_R(Y)-r_R(Y)
 =|\{i\in R:t_i\in Y,\ N(i)\not\subseteq Y\}|. \tag{1.2}
\]

The residual roles closed in \(Y\) number \(f(Y)-r_R(Y)\), while their
residual capacity in \(Y\) is \(a(Y)-b_R(Y)\).  Hence residual Hall is
equivalent to

\[
 f(Y)-r_R(Y)\le a(Y)-b_R(Y)
 \iff
 \chi_R(Y)\le\kappa(Y).                       \tag{1.3}
\]

Together with \(b_R(v)\le a(v)\), (1.3) is necessary and sufficient for
the prescribed reservation to extend.  If its projected state edges span,
the completion is balanced and weakly connected, hence Eulerian.  This
independently verifies the cut-charge theorem in
`MATH_THEOREM_K_HALL_SAFE_TREE_CUT_CHARGE_AND_SATURATED_HAMILTON_BARRIER_20260802.md`.

The indicator of \(N(i)\subseteq Y\) is supermodular, so \(f\) is
supermodular and \(\kappa=a-f\) is submodular.  Under feasibility its zero
sets are closed under union and intersection.  In particular, a reserved
assignment cannot escape from a tight shore: if \(\kappa(Y)=0\) and
\(t_i\in Y\), then (1.3) forces \(N(i)\subseteq Y\).

## 2. The three-role bow-tie

### Proposition 2.1 (strict Hall expansion does not force a tree)

Let \(I=V=\{1,2,3\}\), let every state have capacity one, and let role
\(i\) have fixed head \(i\).  Take the interval lists

\[
 N(1)=\{1,2\},\qquad
 N(2)=\{1,2,3\},\qquad
 N(3)=\{2,3\}.                                  \tag{2.1}
\]

Then all of the following hold.

1. For every nonempty proper \(X\subset I\),
   \( |N(X)|\ge |X|+1\).
2. Every role and tail state has degree at least two.
3. The allowed projected digraph is the reflexive bidirected path
   \(1\leftrightarrow2\leftrightarrow3\), and is strongly connected.
4. No balanced selector is connected, and no Hall-safe spanning-tree
   skeleton exists.

#### Proof

The singleton and two-role cases directly give statements 1 and 2, and
statement 3 follows by projecting a role--tail incidence \(iv\) to
\(v\to i\).

A perfect matching using tail 1 for role 1 is either the identity or the
transposition of roles 2 and 3.  A perfect matching using tail 2 for role 1
forces tail 3 for role 3 and tail 1 for role 2.  These are all matchings.
Their projected cycle profiles are therefore three loops or one directed
2-cycle plus one loop.  None is connected.

The escape charge exposes the same failure without enumerating final
matchings.  A spanning tree must use one projected edge on each arm of the
path.  The only role-distinct, capacity-feasible choice oriented
\(1\to2\) and \(2\to3\) reserves roles 2 and 3 at tails 1 and 2.  For
\(Y=\{1,2\}\), one has

\[
 \kappa(Y)=2-1=1,
 \qquad \chi_R(Y)=2.
\]

The opposite viable orientation gives the symmetric violation on
\(Y=\{2,3\}\).  The two remaining arm-pairs either repeat role 2 or use
tail 2 twice.  Thus no prescribed spanning tree is Hall-safe. \(\square\)

This example also rules out a random-tree conclusion based only on
negative dependence: the support contains no acceptable tree at all.
It is minimal under the stated strict-Hall hypothesis: with two roles and
two unit-capacity tails, strict Hall on both singleton role sets forces the
complete bipartite graph, whose transposition is a connected directed
2-cycle.

## 3. A literal Boolean family with exponentially large menus

The bow-tie is abstract.  The next construction shows, literally, why
large Boolean containment menus do not control the ordered predecessor
graph.

### Proposition 3.1 (large-menu two-cycle obstruction)

For every integer \(s\ge0\), there is a depth-two static Boolean flag table
with eight distinct rank-\((s+3)\) owners and two distinct marked lower
targets per owner such that

* every leading-letter menu has size \(2^{s+2}\); but
* the ordered role--head graph is exactly two disjoint directed 4-cycles.

Consequently its unique balanced selector has two Euler components and no
Hall-safe spanning-tree skeleton.

#### Construction and proof

Let \(K\) be a fixed set of size \(s\).  For
\(\epsilon\in\{0,1\}\), take four further coordinates

\[
 x_{\epsilon,0},x_{\epsilon,1},x_{\epsilon,2},x_{\epsilon,3},
\]

with the two four-sets and \(K\) pairwise disjoint.  Indices below are
modulo four.  For role \((\epsilon,i)\), set

\[
\begin{aligned}
 A_{\epsilon,i,1}&=K\cup\{x_{\epsilon,i}\},\\
 A_{\epsilon,i,2}&=K\cup\{x_{\epsilon,i+1}\},\\
 T_{\epsilon,i}&=K\cup
 \{x_{\epsilon,i-1},x_{\epsilon,i},x_{\epsilon,i+1}\}.
                                                        \tag{3.1}
\end{aligned}
\]

The fixed head is

\[
 h_{\epsilon,i}=(A_{\epsilon,i,1},A_{\epsilon,i,2}).
\]

Its marked suffix targets may be taken as

\[
 K\cup\{x_{\epsilon,i+1}\},
 \qquad
 K\cup\{x_{\epsilon,i},x_{\epsilon,i+1}\}.             \tag{3.2}
\]

All sixteen targets in (3.2) are distinct, and all eight owners in (3.1)
are distinct and have the same rank.

The owner condition for the leading letter is

\[
 \{x_{\epsilon,i-1}\}\subseteq B\subseteq T_{\epsilon,i},
                                                               \tag{3.3}
\]

so there are \(2^{s+2}\) literal choices for \(B\).  However, a tail
\((B,A_{\epsilon,i,1})\) equals a fixed head
\(h_{\epsilon',j}\) only if

\[
 A_{\epsilon',j,2}=A_{\epsilon,i,1}.
\]

Disjointness of the named coordinates forces
\(\epsilon'=\epsilon\) and \(j=i-1\).  The corresponding leading letter
is \(B=K\cup\{x_{\epsilon,i-1}\}\), which satisfies (3.3).  Thus each
role has exactly one neighbour in the fixed-head bank, namely the preceding
head on its own four-cycle.  No other literal menu choice can be used in a
balanced selector, because its tail state has head demand zero.  The claim
follows. \(\square\)

The family separates two notions which must not be conflated:

* the number of Boolean letters satisfying the owner containment interval;
* the number of those letters occurring at a fixed head with the required
  ordered one-step spine overlap.

Only the second enters Hall and topology.

## 4. The exact positive condition and a private absorber face

Equation (1.3) is the weakest cutwise condition for a **specified** tree.
It suggests two proof-safe positive routes.

### Corollary 4.1 (Hall-slack tree certificate)

Suppose distinct reserved roles and legal tails project to a spanning tree,
respect capacities, and satisfy

\[
 |\{i\in R:t_i\in Y,\ N(i)\not\subseteq Y\}|
       \le a(Y)-|\{i:N(i)\subseteq Y\}|                 \tag{4.1}
\]

for every tail shore \(Y\).  Then they extend to a connected balanced
selector preserving every owner and named target.

This is immediate from Section 1, but (4.1) is materially stronger than a
degree or neighbourhood-size bound: it prices each selected tree edge by
the exact Hall shore from which its role can escape.

### Corollary 4.2 (singleton-tail private tree bank)

Assume the original role--tail system is feasible.  If there are distinct
roles \(R\) with singleton lists \(N(i)=\{t_i\}\), their selected tails
respect capacities, and their projected state edges contain a spanning
tree, then \(R\) is Hall-safe.

#### Proof

For every \(Y\), \(t_i\in Y\) is equivalent to
\(N(i)\subseteq Y\).  Hence \(\chi_R(Y)=0\), so (1.3) follows from
\(\kappa(Y)\ge0\). \(\square\)

In the Boolean table, singleton-tail status is a literal protected-socket
condition: after all guards are imposed, the role has one surviving fixed
head with the required ordered spine.  A bank of such sockets is an exact
zero-charge absorber.  More flexible banks are allowed, but their escape
charges must be paid by (4.1); merely having many containing letters does
not help.

## 5. Minimal remaining lower-side lemma

On the full-depth distinct-head face, a balanced selector is a directed
cycle cover, and connectedness is exactly Hamiltonicity.  The weakest
remaining Boolean-specific assertion can therefore be stated in either of
two equivalent constructive forms:

1. choose the canonical owner/target-exact flag table together with a
   spanning tree satisfying (4.1); or
2. choose a cycle cover and a protected sequence of payload-transparent
   alternating rectangles which merges all of its cycles.

The three-role bow-tie shows that strict Hall expansion and strong
connectivity do not imply either form.  Proposition 3.1 shows that raw
Boolean containment degrees do not even control the ordered graph in which
the assertion lives.  What remains to be proved from the canonical
Boolean construction is consequently an **ordered spine-spread/absorber
property**, not another marginal shadow inequality.

All conclusions here stop before upper shadows, residence, exterior
cross-windows, and common-cap/compiler feasibility.
