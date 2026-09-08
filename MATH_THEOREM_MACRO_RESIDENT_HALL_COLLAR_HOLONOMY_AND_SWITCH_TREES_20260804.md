# Macro-resident Hall, balanced-collar holonomy, and switch trees

**Date:** 2026-08-04  
**Status:** unconditional abstract selector and splice theorems.  The input is a
literal vertex-disjoint family of resident path blocks, or a literal resident
cycle factor with protected switch ports.  The note does **not** prove that the
all-perfect-pairings construction supplies either input.

## 1. Why the edge-occurrence matching is at the wrong scale

Let `V` be a family of equal-rank Boolean owners.  A directed Johnson edge
`e=(A,B)` has transition support

\[
                         \partial e=A\mathbin\triangle B.
\]

For a directed transition word `e_1,...,e_s`, call it `L`-resident when

\[
 \partial e_i\cap\partial e_j=\varnothing
 \quad\hbox{whenever}\quad 0<|i-j|<L.                 \tag{1.1}
\]

On a cyclic word, distance in (1.1) is cyclic distance.  A perfect matching
in the ordinary successor-occurrence graph chooses one outgoing and one
incoming edge at every owner, but residence couples up to `L` consecutive
chosen edges.  Thus edgewise regularity cannot by itself invoke Hall on the
residence row.

The correct elementary scale is a path long enough that two new seams cannot
interact.

## 2. The exact macro-Hall theorem

Let

\[
 P_i=(v_{i,0},v_{i,1},\ldots,v_{i,\ell_i})
 \qquad(i\in I)                                      \tag{2.1}
\]

be pairwise vertex-disjoint directed simple Johnson paths whose vertex sets
partition `V`.  Assume

\[
                 \ell_i\ge L-1                              \tag{2.2}
\]

and that the internal transition word of every `P_i` is `L`-resident.

For `i,j in I`, a **literal connector** `c_{ij}` is a Johnson edge from
`v_{i,ell_i}` to `v_{j,0}`.  It is **seam-safe** when the word consisting of

* the final `min(L-1,ell_i)` internal edges of `P_i`;
* `c_{ij}`; and
* the first `min(L-1,ell_j)` internal edges of `P_j`

is `L`-resident.  Let `D` be the directed graph on `I` containing precisely
the available seam-safe connectors.  Its bipartite occurrence graph `B_D`
has shores `I_L,I_R` and an edge `i_Lj_R` for every arc `i->j` of `D`.

### Theorem 2.1 (macro-resident Hall equivalence)

The path blocks can be closed into a spanning `L`-resident directed cycle
factor using one available connector after every block if and only if `B_D`
has a perfect matching.  Equivalently, the exact cut condition is

\[
                  |N_D(X)|\ge |X|\qquad(X\subseteq I).       \tag{2.3}
\]

If `B_D` is `a`-regular for some `a>=1`, such a factor exists.

#### Proof

A connector cycle factor induces a permutation `pi` of the blocks: after
`P_i` it uses `c_{i,pi(i)}`.  The edges `i_L pi(i)_R` form a perfect matching.
This proves necessity.

Conversely, a perfect matching defines such a permutation.  Concatenate the
blocks along every orbit of `pi`.  The blocks are vertex-disjoint and cover
`V`, so the result is a spanning directed cycle factor.

Consider two transition edges at cyclic distance less than `L` in one new
cycle.  By (2.2), the interval between them cannot contain two connectors.
They therefore lie either inside one old block or in the defining local word
of one seam.  The first case is safe by internal residence and the second by
the definition of `D`.  Hence the new factor is `L`-resident.  Hall's theorem
gives (2.3).  If `B_D` is regular, counting edges out of a left set and into
its neighbourhood proves Hall. \(\square\)

### Corollary 2.2 (dense one-component version)

Discard every self-connector `i->i` and call the resulting loopless
seam-safe digraph `D^circ`.  If `D^circ` on `n=|I|>=2` blocks satisfies

\[
             d_{D^\circ}^+(i)\ge n/2,\qquad
             d_{D^\circ}^-(i)\ge n/2
             \qquad(i\in I),                                \tag{2.4}
\]

then the blocks concatenate into one spanning `L`-resident directed cycle.

#### Proof

Condition (2.4) makes `D^circ` strongly connected: otherwise a source strongly
connected component and a sink strongly connected component would each have
more than `n/2` vertices.  Also

\[
             d^+_{D^\circ}(i)+d^-_{D^\circ}(i)\ge n.
\]

The Ghouila-Houri directed Dirac theorem gives a
directed Hamilton cycle in `D^circ`.  Use that cyclic block order in
Theorem 2.1.
\(\square\)

The point is not that (2.4) is expected automatically.  It is a concrete
codegree-free sufficient target at the correct, resident-block scale.

## 3. Balanced collars carry a phase, not just a legal edge

The complementary-age theorem gives an exact critical-scale local
certificate.  It also reveals a global compatibility condition that is
invisible in the ordinary successor multigraph.

Suppose an opened resident block has the same support `R_i`, of size `L-1`,
in its two endpoint collars.  Let

\[
 \theta_i:R_i\longrightarrow\{1,\ldots,L-1\}                \tag{3.1}
\]

give the ages at the initial endpoint.  Residence and equality of the two
supports force the terminal age of `x` to be

\[
                             L-\theta_i(x).                  \tag{3.2}
\]

Indeed, each terminal-plus-initial age is at least `L`, and the sum of all
`L-1` such inequalities is exactly `L(L-1)`.

Suppose a candidate seam `i->j` identifies the common collar directions by
a bijection

\[
                         \phi_{ij}:R_i\longrightarrow R_j.   \tag{3.3}
\]

The seam inequalities are

\[
       L-\theta_i(x)+\theta_j(\phi_{ij}(x))\ge L
       \qquad(x\in R_i).                                    \tag{3.4}
\]

Summing (3.4) again forces equality term by term.  Thus a balanced-collar
seam is safe exactly when

\[
              \theta_j\circ\phi_{ij}=\theta_i.              \tag{3.5}
\]

So an available seam transports a collar **phase**.

### Theorem 3.1 (exact collar-holonomy criterion)

More generally, give each block `i` a finite phase set `Omega_i`.  Suppose
every available base arc `i->j` carries a bijection

\[
                         \tau_{ij}:\Omega_i\longrightarrow\Omega_j, \tag{3.6}
\]

and that the seam is resident precisely when its endpoint phases satisfy
`omega_j=tau_ij(omega_i)`.  Fix a directed cycle cover `pi` of the base
digraph.  It admits simultaneous phases at all blocks if and only if, on
every cycle

\[
                 i_0\to i_1\to\cdots\to i_{q-1}\to i_0,
\]

the holonomy

\[
 H_C=\tau_{i_{q-1}i_0}\circ\cdots\circ\tau_{i_0i_1}          \tag{3.7}
\]

has a fixed point in `Omega_{i_0}`.

In particular, if there is one phase set `Omega` and bijections
`g_i:Omega->Omega_i` such that

\[
                         \tau_{ij}=g_j\circ g_i^{-1}          \tag{3.8}
\]

for every available arc, then every base cycle cover lifts.

#### Proof

Choose a phase at one vertex of a base cycle and propagate it around the
cycle using (3.6).  The propagated phase agrees on returning to the first
vertex exactly when it is fixed by (3.7).  Different base cycles are
independent.  Under (3.8), every cyclic product telescopes to the identity.
\(\square\)

For balanced collars, take `Omega_i` to be the possible age bijections in
(3.1), and let (3.6) be the transport in (3.5).  Thus ordinary Hall on the
base seam graph is sufficient only after one proves either the fixed-point
condition (3.7) for the selected cycles or the flat-gauge condition (3.8).
This is the exact phase-coherence row.

## 4. Port-separated switch trees

There is a second route: begin with a literal resident cycle factor and
merge its components by protected two-cycle switches.

Let `C_1,...,C_s` be vertex-disjoint `L`-resident directed cycles.  A switch
between two cycles deletes one directed edge from each and inserts the two
cross edges in the merging orientation.  Call a family of such switches
**globally separated** when

1. no deleted edge is used by two switches;
2. after all deleted edges are removed, every retained old path segment
   between consecutive new seam edges contains at least `L-1` old
   transitions; and
3. the transition word in the `(L-1)`-collar of every new seam is
   `L`-resident.

The third row may be certified by the complementary-age two-seam theorem:
at common dimension `m>=L`, equal two-end collar support is sufficient; for
arbitrary endpoint histories, `m>=2L-1` is sufficient in the worst case.

### Theorem 4.1 (resident switch-tree Hamiltonization)

Suppose the switch graph on `{C_1,...,C_s}` contains a spanning tree whose
switches are globally separated.  Applying those `s-1` switches produces
one spanning `L`-resident directed cycle.

#### Proof

Process the tree edges in any order.  Before a tree edge is processed, its
end cycles lie in different current components: otherwise the already
processed tree edges would contain a path between its endpoints and adding
the current edge would create a cycle in a subgraph of a tree.  A directed
two-cycle switch between distinct directed cycles merges them into one.
After `s-1` switches there is one cycle.

For residence, take two transitions at distance less than `L` in the final
cycle.  By global separation row 2, they cross at most one new seam.  If they
cross none, old residence applies; if they cross one, row 3 applies.  Hence
the final cycle is `L`-resident. \(\square\)

This theorem permits a component to supply several switch ports, but prices
their spacing explicitly.  Merely knowing that every pair of components has
some individually safe switch is not enough.

## 5. Sharp obstruction to owner-level regularity

The all-perfect-pairings theorem proves that the successor-occurrence
bipartite multigraph is regular.  No theorem using only that regularity can
deduce residence.

### Proposition 5.1 (arbitrary multiplicity does not buy memory)

For every `a>=1` and `L>=2`, there is an `a`-regular symmetric successor
occurrence bipartite multigraph with a perfect matching but with no resident
simple directed cycle factor.

#### Proof

Take two owners `u,v` joined by one physical Johnson edge, and put `a`
parallel occurrences of `u_Lv_R` and `a` parallel occurrences of `v_Lu_R`.
Every left and right degree is `a`, and every perfect matching projects to
the antiparallel two-cycle `u->v->u`.  Its two consecutive transition
supports are equal, so it violates (1.1) for every `L>=2`. \(\square\)

The example is deliberately local and occurrence-labelled.  It does not
claim that the full all-pairings host consists of this gadget.  It proves
the precise logical point: arbitrarily large regular occurrence
multiplicity cannot replace a resident macro-selector or a collar phase
condition.

## 6. Revised exact frontier

The all-perfect-pairings construction closes ordinary successor Hall at the
edge-occurrence level.  To turn that result into a resident factor, it is
enough to establish either of the following explicit packages.

### Macro-Hall package

1. partition the owner layer into literal internally resident paths of at
   least `L-1` edges;
2. prove Hall (2.3) for their literal seam-safe connector graph; and
3. when collars are selected only up to relabelling, prove the holonomy
   fixed-point row (3.7), or the stronger flatness row (3.8).

Regularity of the **macro** connector graph closes row 2.  It is this lifted
regularity, not owner-level occurrence regularity, that has the correct
quantifier.

### Switch-tree package

1. first obtain a literal resident cycle factor, for example through a
   seam-free exact cover of good pair cells; and
2. plant a globally separated spanning tree of complementary-age switches.

Theorem 4.1 then gives one resident component.

Neither package is currently supplied by the all-pairings cover theorem.
The new gain is an exact separation of the remaining rows:

\[
 \boxed{\text{macro Hall}\quad+\quad\text{collar holonomy}
        \quad+\quad\text{optional switch-tree topology}.}
\]

There is no longer an ambiguity about whether ordinary edge-occurrence Hall
should somehow remember `L` previous transitions: it cannot, and the two
constructions above are exact ways to add that memory.
