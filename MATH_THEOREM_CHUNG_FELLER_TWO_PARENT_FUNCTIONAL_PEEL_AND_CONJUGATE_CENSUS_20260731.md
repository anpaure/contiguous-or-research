# The Chung--Feller two-parent union is a functional pseudoforest

Date: 2026-07-31  
Status: exact all-\(m\) reduction; exact finite censuses through the stated
dimensions; no bounded-conjugate all-\(m\) construction is claimed

## 1. Setup

Let \(|\Omega|=2m\), and write

\[
 \mathcal L=\binom{\Omega}{m-1},\qquad
 \mathcal X=\binom{\Omega}{m},\qquad
 \mathcal U=\binom{\Omega}{m+1}.
\]

The canonical Mütze--Standke--Wiechert Chung--Feller factor
\(F_m\) consists of \(\operatorname {Cat}_m\) paths through the flaw layers.
It partitions \(\mathcal X\). Its \(m\operatorname {Cat}_m\) adjacent
edges have pairwise distinct upper colours, hence enumerate
\(\mathcal U\).

For \(U\in\mathcal U\), let \(e_U\) be the unique edge of \(F_m\) with
union \(U\), and define

\[
                         p(U)=\bigcap e_U\in\mathcal L.       \tag{1.1}
\]

Let \(c\) denote complementation in \(\Omega\), and let
\(\tau\in S_\Omega\). The second parent is the coordinate conjugate
\(\tau cF_m\). Its lower colours are pairwise distinct and enumerate
\(\mathcal L\). If \(L\in\mathcal L\), its upper colour is

\[
             q_\tau(L)=\tau c p(c\tau^{-1}L).                 \tag{1.2}
\]

The sparse diamond-colour union is therefore

\[
 H_\tau=
 \{(p(U),U):U\in\mathcal U\}
 \cup
 \{(L,q_\tau(L)):L\in\mathcal L\}.                          \tag{1.3}
\]

Parallel copies in (1.3) may either be retained as labelled edges or
identified. This does not affect perfect-matching existence or the
physical Johnson edge selected by a matching.

## 2. Exact matching criterion

### Theorem 2.1 (two functions and forced peeling)

For every \(m\) and every coordinate permutation \(\tau\), the following
are equivalent.

1. \(H_\tau\) has a perfect matching.
2. There are binary variables \(x_U\), \(U\in\mathcal U\), and \(y_L\),
   \(L\in\mathcal L\), satisfying
   \[
   y_L+\sum_{U:p(U)=L}x_U=1\quad(L\in\mathcal L),             \tag{2.1}
   \]
   \[
   x_U+\sum_{L:q_\tau(L)=U}y_L=1\quad(U\in\mathcal U).       \tag{2.2}
   \]
3. Orient the first edge in (1.3) from \(U\) to \(p(U)\), and the second
   from \(L\) to \(q_\tau(L)\). Repeatedly match every degree-one vertex
   to its unique neighbour and delete both. This process creates no
   isolated vertex; after it stops, the residual graph is a disjoint union
   of even cycles.

Moreover, the same leaf algorithm is a maximum-matching algorithm. If
it creates \(z\) isolated vertices in total, the Hall deficiency is
\(z/2\). Every perfect matching consists of the forced leaf edges and one
of the two alternating matchings on each residual cycle.

### Proof

Every upper vertex has exactly one outgoing first-parent edge and every
lower vertex exactly one outgoing second-parent edge. Thus the directed
labelled graph is a functional digraph. Each weak component has one
directed cycle with in-arborescences attached; after parallel opposite
arcs are identified, its underlying graph is a tree or a unicyclic
bipartite graph.

Let \(x_U=1\) mean that the first-parent edge out of \(U\) is selected, and
let \(y_L=1\) mean that the second-parent edge out of \(L\) is selected.
The condition that a lower vertex \(L\) is used exactly once is (2.1), and
the corresponding upper condition is (2.2). This proves \(1\iff2\).

In a tree or unicyclic graph, the edge at a leaf belongs to every perfect
matching. Delete that edge and its endpoints. If an isolated vertex is
created, no perfect matching exists. If no leaf remains, minimum degree
is at least two; a pseudoforest with this property is a cycle. It is even
because the graph is bipartite, and it has exactly its two alternating
perfect matchings. The same forced-leaf induction is the standard exact
maximum-matching recursion on a pseudoforest. Since the two shores have
equal size, unmatched vertices occur equally on both shores, proving the
deficiency formula. \(\square\)

This is substantially sharper than invoking Hall abstractly: the entire
two-parent palette gate is Boolean unit propagation followed by independent
cycle bits.

## 3. Exact physical criterion

For a selected diamond \(e=(L,U)\), let

\[
 \psi(e)=\{L+a,L+b\},\qquad U\setminus L=\{a,b\},             \tag{3.1}
\]

be its Johnson edge. For \(X\in\mathcal X\), put

\[
 \mathcal R_X=\{(L,U):L\subset X\subset U\}.                 \tag{3.2}
\]

### Theorem 3.1 (palette matching versus a Catalan path forest)

Let \(P\) be a perfect matching of \(H_\tau\). Its Johnson lift is a
spanning linear forest of exactly \(\operatorname {Cat}_m\) paths if and
only if

\[
               |P\cap\mathcal R_X|\le2
               \quad\hbox{for every }X\in\mathcal X,          \tag{3.3}
\]

and \(\Psi(P)\) is acyclic.

Equivalently, split the chosen edges according to their two parents,
contract every component of the selected first-parent subforest, and
insert the selected second-parent edges. Besides (3.3), the resulting
attachment multigraph must be loopless and acyclic.

### Proof

Equation (3.3) is exactly the degree bound in the Johnson lift. Each
parent is a path forest, so each selected parent subgraph is a forest.
The union of two forests is acyclic exactly when, after contracting the
components of the first, the second creates neither a loop nor a cycle
(parallel edges count as a two-cycle). Finally

\[
 |P|=|\mathcal L|=m\operatorname {Cat}_m
     =|\mathcal X|-\operatorname {Cat}_m.
\]

Hence an acyclic spanning graph with these many edges has exactly
\(\operatorname {Cat}_m\) components. Degree at most two makes all of them
paths, with isolated vertices admitted. \(\square\)

Theorem 3.1 separates two genuinely different questions. A perfect colour
matching can still overload a middle vertex or close a physical cycle.

## 4. Exact same-frame and dihedral census

The canonical maps in **msw_shadow_test.cpp** were independently
reimplemented. For every dihedral coordinate conjugate, Hopcroft--Karp and
the forced-peeling algorithm of Theorem 2.1 agree exactly.

For \(m\ge2\), the results are:

| \(m\) | shore size \(m\operatorname {Cat}_m\) | same-frame deficiency | best one-dihedral-copy deficiency | perfect dihedral copies |
|---:|---:|---:|---:|:---|
| 2 | 4 | 0 | 0 | all |
| 3 | 15 | 1 | 0 | rotation 3, reflection 2 |
| 4 | 56 | 4 | 2 | none |
| 5 | 210 | 14 | 14 | none |
| 6 | 792 | 64 | 64 | none |
| 7 | 3003 | 251 | 251 | none |
| 8 | 11440 | 1020 | 1020 | none |
| 9 | 43758 | 4086 | 4086 | none |

Thus, in the audited range, the same-frame pair matches fully only at
\(m=2\), and the cyclic/dihedral shift repairs the palette only at \(m=3\).
At \(m=3\) each successful dihedral graph has a **unique** perfect
matching. Its lift has maximum degree two but contains two six-cycles.
For rotation 3 their vertex masks are

\[
 \{07,13,19,1c,25,34\},\qquad
 \{0b,0e,26,29,32,38\},                              \tag{4.1}
\]

in hexadecimal. Hence the shifted \(m=3\) palette repair is not a
Catalan Linear Matching solution.

This proves a sharp scoped no-go:

> The canonical parent plus one same-frame or dihedral complementary
> parent does not supply the required physical forest for any
> \(3\le m\le9\); for \(m\ge4\) it already fails Hall.

It is a finite theorem, not an asymptotic claim.

## 5. Arbitrary coordinate conjugacy is strictly stronger

The preceding no-go must not be stated for arbitrary \(\tau\in S_{2m}\).
All coordinate permutations can be exhaustively checked at \(m=3,4\),
because Theorem 2.1 enumerates every perfect matching without a SAT solver.

| \(m\) | permutations | Hall-perfect conjugates | conjugates admitting a linear-forest matching |
|---:|---:|---:|---:|
| 3 | 720 | 322 | 172 |
| 4 | 40320 | 108 | **2** |

The complete Hall-deficiency histograms are

\[
 m=3:\quad 0^{322},1^{394},2^4,                      \tag{5.1}
\]

\[
 m=4:\quad
 0^{108},1^{884},2^{5662},3^{13008},4^{13050},
 5^{6000},6^{1472},7^{116},8^{20}.                   \tag{5.2}
\]

The two physical \(m=4\) permutations, in zero-based image notation, are

\[
 (0,4,5,6,1,2,3,7),\qquad(7,3,2,1,6,5,4,0).          \tag{5.3}
\]

The first fixes the two endpoints and swaps the two interior blocks of
length three; the second is its reversal. The audit artifact contains an
explicit 56-diamond perfect matching for the first. This gives a new
two-parent realization of the \(m=4\) Catalan linear forest and shows that
the useful symmetry is not dihedral.

The visually natural extrapolation of (5.3) is nevertheless false. Let
\(\tau_m\) fix \(0,2m-1\) and interchange the two consecutive interior
blocks of length \(m-1\):

\[
 \tau_m=(0,\ m,m+1,\ldots,2m-2,\ 1,2,\ldots,m-1,\ 2m-1)
                                                               \tag{5.4}
\]

in zero-based image notation. Exact forced-peeling deficiencies are

| \(m\) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| deficiency | 0 | 1 | 0 | 14 | 88 | 279 | 1512 | 4636 |

and the only physical successes in this range are \(m=2,4\). Thus the
block swap explains the isolated \(m=4\) witness but is not an all-\(m\)
rule. In the functional-digraph normal form, nothing mysterious happens:
at \(m=4\) its forced pruning has no isolated vertex and the surviving
cycle choices include a cap-two acyclic lift; from \(m=5\) onward the same
pruning itself creates isolated vertices, before the physical test is
reached.

## 6. More cyclic parents: Hall improves, physicality does not follow

Fix the canonical first parent and allow several cyclic conjugates of its
complement. Exhaustive subset enumeration gives the minimum number \(t\)
of complementary copies needed merely to obtain a perfect colour matching:

| \(m\) | minimum \(t\) | one winning set of shifts |
|---:|---:|:---|
| 3 | 1 | \(\{3\}\) |
| 4 | 2 | \(\{0,1\}\) |
| 5 | 2 | \(\{0,5\}\) |
| 6 | 3 | \(\{0,2,10\}\) |
| 7 | 5 | \(\{0,1,5,7,9\}\) |

At \(m=7\), the best deficiencies with \(t=1,2,3,4\) are respectively
\(251,33,6,1\), so at least five cyclic complementary copies are necessary.
This rules out every universal cyclic scheme using at most four such
copies.

For the displayed winning shift sets, the deterministic maximum matching
returned by the audit has maximum physical degrees \(2,4,4,5,6\) for
\(m=3,\ldots,7\), and is never a linear forest. This last statement is
about the returned matching only: the existence of a different physical
matching in those larger unions remains open.

The data suggest that adding parents rapidly repairs Hall but merely moves
the problem to the integral cap-two/forest correlation. They do not prove
that the minimum number of parents is unbounded.

## 7. Reproducibility and exact scope

Audit:

* **scratch/audit_msw_two_parent_chung_feller_20260731.py**
* **scratch/msw_two_parent_chung_feller_20260731.audit.json**

The audit performs:

1. literal reconstruction of every MSW flaw path;
2. independent Hopcroft--Karp and functional-peeling matching counts;
3. all \(S_6\) and \(S_8\) coordinate conjugates;
4. exact enumeration of every perfect matching from its forced edges and
   residual cycle bits, followed by a literal physical degree/cycle audit;
5. exhaustive cyclic-copy subsets through \(m=7\); and
6. all one-copy dihedral conjugates through \(m=9\).

Two consecutive full runs produced byte-identical JSON. No SAT/CP solver
is used by the final audit.

The exact general result is Theorems 2.1 and 3.1. The numerical exclusions
are only for the displayed finite ranges and conjugacy classes. In
particular, this note does **not** exclude:

* an arbitrary coordinate conjugate for \(m\ge5\);
* a bounded number of non-dihedral conjugates for all \(m\); or
* a physically valid matching in the larger multi-parent unions.

