# Odd current: socket cost equals the odd-cycle count

**Date:** 2026-08-06  
**Method:** exact cycle decomposition of a deterministic last-intersection
counterflow; no computation or search  
**Status:** unconditional combinatorial theorem.  It converts the labelled
odd paired-basis gate, once a deterministic disjoint counterflow permutation
has been constructed, into an exact socket count.  It does not construct the
counterflow itself.

## 1. Setup

Let

\[
                       A_\partial=\{a_1,\ldots,a_\delta\}
\]

be the aperture basis from the root-clock construction, and let \(b_i\) be
the unique physical boundary partner of \(a_i\).  Let
\(\mathcal P=\{P_i:i\in[\delta]\}\) be the vertex-disjoint source linkage
onto \(A_\partial\).

Assume that a disjoint counterflow bank has the following deterministic
last-intersection form.  For each boundary sink \(b_i\), its counterflow
suffix starts for the last time on exactly one source path

\[
                              P_{\pi(i)},
\]

where \(\pi\) is a permutation of \([\delta]\).  Whenever a set of these
suffixes has distinct starting source paths, the suffixes are pairwise
vertex-disjoint and are disjoint from the source linkage after their stated
last intersections.  This is precisely the hypothesis under which the
last-intersection counterflow lemma applies.

Choose a set \(I\) of boundary pairs and a set \(S\) of exported sockets.
The desired terminal basis is

\[
       U(I,S)=\{a_i,b_i:i\in I\}\ \dot\cup\ \{a_s:s\in S\}.
\tag{1.1}
\]

It has size \(\delta\) exactly when

\[
                              2|I|+|S|=\delta.
\tag{1.2}
\]

## 2. Exact cycle criterion

### Theorem 2.1 (socketed deterministic counterflow)

Under the setup above, the deterministic counterflow realizes the terminal
set \(U(I,S)\) as a surplus basis if

\[
              \pi(I)=[\delta]\setminus(I\cup S).
\tag{2.1}
\]

For a fixed permutation \(\pi\), the minimum possible value of \(|S|\) in
(2.1) is exactly

\[
              o(\pi):=\#\{\text{odd cycles of }\pi\}.
\tag{2.2}
\]

Consequently a deterministic counterflow with \(o(\pi)\le C\) closes the
labelled odd current with at most \(C\) exported sockets.  The exact
one-socket gate closes if and only if \(\pi\) has exactly one odd cycle.

#### Proof

Put

\[
                  J=[\delta]\setminus(I\cup S).
\]

Equation (2.1) says that the counterflow suffixes for sinks indexed by
\(I\) start on the distinct source paths indexed by \(J\).  Retain the
original source paths ending at \(a_i\) for \(i\in I\cup S\), and for each
\(i\in I\) replace the path from source \(\pi(i)\in J\) by its prefix up to
the last intersection followed by the counterflow suffix to \(b_i\).
The deterministic disjointness hypothesis gives a vertex-disjoint linkage
whose terminal set is exactly (1.1).  Hence \(U(I,S)\) is a surplus basis.

It remains to minimize the socket set.  Work on one directed cycle of
\(\pi\).  If the cycle contains no socket, (2.1) forces membership to
alternate

\[
                              I,J,I,J,\ldots,
\]

around the whole cycle: every member of \(I\) has its successor in \(J\),
and every member of \(J=\pi(I)\) has its predecessor in \(I\).  Such an
alternation is possible exactly when the cycle is even.

An odd cycle therefore requires at least one socket.  Conversely, choose
one socket on each odd cycle and none on the even cycles.  On an even cycle
alternate \(I,J\) cyclically.  On an odd cycle delete the chosen socket and
alternate \(I,J\) along the remaining even path, beginning with \(I\) after
the socket and ending with \(J\) before it.  Then every \(I\)-vertex has
successor in \(J\), every \(J\)-vertex has predecessor in \(I\), and (2.1)
holds on every cycle.  Thus one socket per odd cycle is both necessary and
sufficient, proving (2.2).  \(\square\)

### Corollary 2.2 (single-cycle target)

If \(\delta\) is odd and the last-intersection permutation is one
\(\delta\)-cycle, alternating around the cycle after deleting any one
socket gives a paired surplus basis on the remaining boundary edges.

If \(\delta\) is even and the permutation is one \(\delta\)-cycle, no
socket is needed.

## 3. The permutation is unnecessary: exact matching form

The deterministic permutation packages many counterflows which are never
used.  For the additive theorem one only needs a vertex-disjoint set of
source-to-partner counterflows.

Define the **counterflow support graph** \(G_\partial\) on
\([\delta]\) as follows.  An undirected edge \(ij\) is present when at
least one of the following two literal suffixes is available:

\[
                  P_j\leadsto b_i,
       \qquad\hbox{or}\qquad
                  P_i\leadsto b_j,
\tag{3.1}
\]

with the stated source path being the last source-linkage path met by the
suffix.  Call the atlas **matching-faithful** if every matching in
\(G_\partial\) can be oriented edge by edge so that the corresponding
suffixes are pairwise vertex-disjoint and, after their last intersections,
avoid the whole original linkage \(\mathcal P\).

### Theorem 3.1 (exact counterflow-matching deficiency)

For a matching-faithful counterflow atlas, a matching \(M\) in
\(G_\partial\) produces a surplus basis with exactly

\[
                              \delta-2|M|
\tag{3.2}
\]

exported sockets.  Consequently the minimum socket number obtainable from
the atlas is

\[
                    \boxed{\delta-2\nu(G_\partial)},
\tag{3.3}
\]

where \(\nu\) is ordinary matching number.

In particular, the labelled central current is sharp as soon as
\(G_\partial\) has a near-perfect matching, and it has additive defect at
most \(C\) as soon as

\[
                         \delta-2\nu(G_\partial)\le C.
\tag{3.4}
\]

#### Proof

Orient every edge \(ij\in M\) according to an available suffix, say from
source path \(P_j\) to partner \(b_i\).  Retain the original path \(P_i\)
to \(a_i\), and replace \(P_j\) after its last intersection by the chosen
suffix to \(b_i\).  Because \(M\) is a matching, no source index and no
pair index is used twice.  Matching-faithfulness makes all resulting paths
vertex-disjoint.  For every vertex not covered by \(M\), retain its
original path and export its terminal \(a_s\) as a socket.

The terminal set therefore consists of both endpoints \(a_i,b_i\) for one
orientation-tail \(i\) of each matched edge, and one aperture terminal for
every unmatched index.  It has \(2|M|+(\delta-2|M|)=\delta\) elements and
is linked from all \(\delta\) sources, hence is a surplus basis.  Maximizing
\(|M|\) gives the upper bound in (3.3).

Conversely, any construction using one suffix of the atlas for each chosen
boundary pair uses two distinct indices: the retained pair index and the
rerouted source index.  Vertex-disjointness forbids either index from being
used by another chosen pair, and an index cannot simultaneously be a
retained pair endpoint and a rerouted source.  Hence the chosen suffixes
project to a matching in \(G_\partial\).  At most \(\nu(G_\partial)\)
pairs can be used, leaving at least \(\delta-2\nu(G_\partial)\) sockets.
This proves equality.  \(\square\)

### Corollary 3.2 (cycle criterion recovered)

If the only available suffixes are the arcs of a permutation \(\pi\), then
the underlying support pseudograph is obtained from the cycles of \(\pi\):
a fixed point becomes an isolated vertex and a two-cycle becomes one
ordinary edge.  Its maximum matching leaves no vertex on an even cycle and
one vertex on an odd cycle (including one fixed point).  Therefore (3.3)
is exactly the odd-cycle count \(o(\pi)\) from Theorem 2.1.

This is the useful proof target: one need not construct every entry of the
fundamental matrix or a full deterministic counterflow.  It is enough to
plant a matching-faithful physical support graph with matching deficiency
\(O(1)\), ideally one.

## 4. The central labelled residue is odd

At central odd mass, the quiet source set is

\[
       Q\cong\mathcal T_{m,m}
        =\{u\in\{0,1,2\}^m:\sum_i u_i=m\}.
\tag{4.1}
\]

### Proposition 4.1 (central-trinomial parity)

\[
                              |Q|\equiv1\pmod2.
\tag{4.2}
\]

#### Proof

The complement involution

\[
                         (u_1,\ldots,u_m)
                    \longmapsto
                         (2-u_1,\ldots,2-u_m)
\]

preserves (4.1).  Its only fixed point is \((1,\ldots,1)\).  Every other
source belongs to a two-element orbit, proving (4.2).  \(\square\)

### Corollary 4.1a (complement is already parity-perfect)

The complement permutation `mathsf c(u)=2-u` is an automorphism of the
cyclic nearest-neighbour capacity-two token graph on `mathcal T_(m,m)` and
has exactly one odd orbit: the fixed all-ones source.  Every other orbit is
a two-cycle.  Consequently a physical counterflow with last-intersection
permutation `mathsf c` closes the odd current with exactly one socket.

#### Proof

Complement reverses the direction of every unit transfer and hence
preserves the undirected token graph.  Proposition 4.1 identifies its sole
fixed source; all other orbits of an involution have length two.  Apply
Theorem 2.1.  \(\square\)

Thus the rotation factor below is not needed for cycle parity.  It remains
useful only if the literal physical transporter naturally exports that
rotation.

There is also a complement-rotation permutation with the optimal cycle
parity.  Write
Write

\[
                              m=2^a\ell,
                 \qquad      \ell\text{ odd},
\tag{4.3}
\]

and let \(R\) be cyclic rotation of the \(m\) compressed coordinates.
Put

\[
             J=\mathsf c R^{2^a},
 \qquad      \mathsf c(u_1,\ldots,u_m)
                 =(2-u_1,\ldots,2-u_m).
\tag{4.4}
\]

When \(\ell=1\), interpret \(R^{2^a}=R^m\) as the identity.

### Theorem 4.2 (one-odd-orbit complement rotation)

The permutation \(J\) preserves \(\mathcal T_{m,m}\), is an automorphism
of its cyclic nearest-neighbour capacity-two token graph, and has exactly
one odd orbit, namely the fixed point

\[
                              (1,\ldots,1).
\tag{4.5}
\]

Every other \(J\)-orbit is even.

#### Proof

Rotation preserves total mass and cyclic adjacency.  Complement preserves
total mass on the central layer and sends a directed unit transfer to the
same undirected token edge with its direction reversed.  Hence \(J\) is a
token-graph automorphism.

The rotation \(R^{2^a}\) has odd order \(\ell\), and it commutes with
\(\mathsf c\).  Suppose a state \(u\) lies in an odd \(J\)-orbit, of
length \(t\).
Then

\[
             u=J^t u=\mathsf c R^{2^a t}u,
\tag{4.6}
\]

because \(t\) is odd.  Every cycle of the coordinate permutation
\(R^{2^a t}\) has odd length: its order divides the odd integer \(\ell\).
Along such a coordinate cycle, (4.6) alternates a digit with its complement
\(2-x\).  Closing after an odd number of steps forces \(x=1\).  Thus every
coordinate of \(u\) equals one.

The all-ones state is visibly fixed by \(J\).  It is therefore the unique
state in an odd orbit, and that orbit has length one.  \(\square\)

### Corollary 4.3 (canonical sharp counterflow target)

If the aperture counterflow can be chosen with last-intersection
permutation \(J\), Theorem 2.1 closes the labelled central odd current with
the unique all-ones source as its single socket.

This corollary does not assert that the root-clock aperture is
\(J\)-equivariant.  It identifies a parity-perfect physical automorphism
of the compressed source layer which the handoff construction should
realize.

### Lemma 4.4 (odd quotient preserves the unique odd orbit)

Let a finite group \(H\) of odd order act on a finite set \(X\), and let
\(J\) be a permutation of \(X\) commuting with \(H\).  Suppose the only
odd \(J\)-orbit is one fixed point \(x_0\), and suppose \(x_0\) is
\(H\)-fixed.  Then the permutation induced by \(J\) on \(X/H\) also has
exactly one odd orbit, the fixed orbit \([x_0]\).

#### Proof

Let \([x]\) lie in an induced \(J\)-orbit of odd length \(t\).  Then

\[
                            J^t x=h x
\tag{4.7}
\]

for some \(h\in H\).  If \(r\) is the order of \(h\), then \(r\) is odd;
commutation gives

\[
                            J^{tr}x=x.
\tag{4.8}
\]

Thus the ordinary \(J\)-orbit of \(x\) has odd length.  By hypothesis
\(x=x_0\), proving uniqueness.  The orbit \([x_0]\) is fixed.  \(\square\)

### Corollary 4.5 (source-level stabilizer descent)

For every odd rotation subgroup \(H\le\langle R\rangle\), the permutation
\(J=\mathsf c R^{2^a}\) induces on
\(\mathcal T_{m,m}/H\) a permutation with exactly one odd orbit.

Indeed \(\mathsf c\), \(R\), and \(H\) commute, \(|H|\) is odd, and the all-ones
source is \(H\)-fixed.  This closes the **cycle-parity** part of stabilizer
descent.  It does not construct an orbit-clock aperture or prove
orbit-injectivity of the physical hub signatures.

Thus the exact central labelled theorem naturally has one socket.  By
Theorem 2.1, the deterministic-counterflow route to an additive constant
does not require an even-cycle permutation: it requires only

\[
             \boxed{o(\pi)=O(1).}
\tag{4.9}
\]

The sharp exact target is \(o(\pi)=1\), and a single cyclic Gray ordering
of the quiet sources would have precisely the required parity profile.
Theorem 4.2 supplies an even more canonical target permutation with that
profile.

## 5. Scope

Proved here:

1. the exact basis linkage obtained from a socketed deterministic
   counterflow;
2. the exact minimum number of sockets, equal to the odd-cycle count of
   the last-intersection permutation;
3. the more general exact matching-deficiency formula for a
   matching-faithful counterflow support graph;
4. oddness of the central labelled quiet residue;
5. a cyclic token-graph automorphism of that residue with exactly one odd
   orbit;
6. preservation of that one-odd-orbit property under every commuting odd
   rotational quotient.

Not proved here:

1. existence of a matching-faithful physical counterflow atlas;
2. a bound on the matching deficiency of its support graph;
3. compatibility with the nonwrap fan/receiver bank;
4. descent through a nontrivial rotational stabilizer.

The next positive target is therefore narrower than arbitrary matroid
parity: construct long-way counter-circulations whose matching-faithful
support graph has \(O(1)\) unmatched vertices, ideally one.
