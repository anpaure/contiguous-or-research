# Colored endpoint support: exact functional-Hall reduction and the parity obstruction

**Date:** 2026-08-01  
**Status:** unconditional abstract reduction.  It identifies the exact cuts
needed after singleton support is made complete.  It does not assert those
cuts for the current `k=17` factor and does not construct a Hamilton rejoin.

## 0. Verdict

Completing every tail, head, and deleted-colour singleton row is necessary
but not sufficient for a global endpoint reassembly.

For fixed block orientations, the seam problem is a rainbow perfect matching
in a bipartite tail--head graph: every tail, every head, and every colour must
be used exactly once.  This is a three-dimensional matching problem.

There is nevertheless an exact two-stage reduction:

1. choose a perfect matching between head states and colours;
2. apply ordinary Hall between tail states and the chosen head--colour
   columns.

All second-stage inequalities are separated by one minimum cut.  With
variable block orientations, the same statement holds with selectable
left/right vertices and a weighted Hall cut.

Connectivity is not supplied by this flow theorem.  Directed subtour cuts,
or equivalently a separate graphic/path gate, remain necessary.

## 1. Fixed orientations

Let `T`, `H`, and `C` be equally sized sets of tail states, head states, and
deleted lower colours, with common size `n`.  Let

\[
                     E\subseteq T\times H\times C             \tag{1.1}
\]

be the legal seam atoms after whatever local residence predicate is being
used.

For a head--colour column `a=(h,c)`, define its predecessor list

\[
                  P_a=\{t\in T:(t,h,c)\in E\}.                \tag{1.2}
\]

Delete columns with \(P_a=\varnothing\).  Let `U` be a perfect matching between
`H` and `C` in the remaining column graph.  For \(X\subseteq T\), put

\[
                  N_U(X)=\{a\in U:P_a\cap X\ne\varnothing\}.  \tag{1.3}
\]

### Theorem 1.1 (head--colour functional Hall)

There is a perfect colored endpoint matching whose selected head--colour
columns are exactly `U` if and only if

\[
                   |N_U(X)|\ge |X|\qquad(X\subseteq T).        \tag{1.4}
\]

Consequently, the seam hypergraph has a perfect matching if and only if
there is a head--colour perfect matching `U` satisfying (1.4).

#### Proof

Once `U` is fixed, make a bipartite graph from `T` to the `n` selected
columns, joining `t` to `a` exactly when \(t\in P_a\).  A perfect matching in
this graph is literally a set of `n` triples using every tail once and,
because `U` is a head--colour perfect matching, every head and colour once.
Condition (1.4) is exactly Hall's theorem for this bipartite graph.  The
converse reads the head--colour pairs from any perfect seam matching.
\(\square\)

## 2. The exact extra Hall cuts

Use binary variables `u_a` on head--colour columns.  The first-stage rows are

\[
 \sum_{c}u_{h,c}=1\quad(h\in H),\qquad
 \sum_{h}u_{h,c}=1\quad(c\in C).                              \tag{2.1}
\]

For \(X\subseteq T\), let

\[
                  A_X=\{a:P_a\cap X\ne\varnothing\}.          \tag{2.2}
\]

The complete additional system is

\[
                        \boxed{\sum_{a\in A_X}u_a\ge |X|}
                        \qquad(X\subseteq T).                 \tag{2.3}
\]

Equations (2.1)--(2.3) are necessary and sufficient.  They are the precise
extra Hall cuts missing from singleton completeness and from separate
two-shore matching audits.

### Min-cut separation

For fixed integral or fractional `u`, build a network

```text
source -> tail t       capacity 1
tail t -> column a     capacity infinity if t in P_a
column a -> sink       capacity u_a.
```

A finite cut with source-side tail set `X` must also contain every column in
`A_X`.  Its capacity is

\[
                         n-|X|+u(A_X).                         \tag{2.4}
\]

Thus the minimum cut is below `n` exactly when some inequality (2.3) is
violated.  The entire exponential family has one polynomial-time separation
oracle.

For a fixed `u`, define

\[
             \delta(u)=\max_{X\subseteq T}(|X|-u(A_X))_+.      \tag{2.5}
\]

For integral `u`, Kőnig--Hall gives a maximum second-stage matching of size
\(n-\delta(u)\); for fractional `u`, the same formula gives the maximum
capacitated flow value.
Therefore the exact perfect-matching defect is

\[
 \boxed{\delta^*=\min_{u\text{ satisfying }(2.1)}\delta(u)},  \tag{2.6}
\]

and perfect colored endpoint matching is equivalent to \(\delta^*=0\).
This is a small master plus a min-cut Benders oracle, not plain Hall on a
single frozen projection.

## 3. Variable orientations

For every physical block `B`, let `B^+` and `B^-` be its two oriented
states and introduce

\[
                         z_{B,+}+z_{B,-}=1.                    \tag{3.1}
\]

A column now has the form \(a=(D^\tau,c)\).  Its predecessor list
`P_a` is a subset of oriented tail states.  Choose head--colour columns by

\[
 \sum_c u_{D^\tau,c}=z_{D,\tau},\qquad
 \sum_{D,\tau}u_{D^\tau,c}=1.                                \tag{3.2}
\]

### Theorem 3.1 (orientation-coupled functional Hall)

There is a colored cycle cover using one common orientation at the incoming
and outgoing occurrence of every block if and only if (3.1)--(3.2) have an
integral solution satisfying

\[
 \boxed{
 \sum_{B^\sigma\in X}z_{B,\sigma}
 \le
 \sum_{a:\,P_a\cap X\ne\varnothing}u_a
 }
 \qquad(X\subseteq\{B^+,B^-:B\in\mathcal B\}).               \tag{3.3}
\]

#### Proof

The selected oriented tail states are those with `z=1`; the selected
head--colour columns are those with `u=1`.  Both shores have size `n`.
Inequalities (3.3) are exactly Hall on the bipartite predecessor graph
induced by these selected vertices.  A perfect matching gives one outgoing
seam from each selected tail state and one incoming seam to each selected
head state, while (3.2) uses every colour once.  The same `z` controls both
roles of a physical block, giving orientation consistency. \(\square\)

The weighted min-cut separation from Section 2 remains exact: give the
source--tail arc capacity \(z_{B,\sigma}\) and the column--sink arc capacity
`u_a`.  A cut below total selected tail mass separates (3.3).

## 4. Singleton and pairwise Hall do not promote

### 4.1 Singleton completeness has no useful matching bound

For \(n\ge2\), take triples

\[
 (t_i,h_i,c_1)\quad(1\le i\le n),\qquad
 (t_1,h_1,c_j)\quad(2\le j\le n).                             \tag{4.1}
\]

Every tail, head, and colour lies in an edge, but a matching has size at
most two.  Thus singleton completeness alone gives no positive-density
perfect-matching guarantee as `n` grows.

### 4.2 Even every two-shore projection can be perfect

Let each shore be `{0,1}` and retain the four even-parity triples

\[
                   000,\quad011,\quad101,\quad110.             \tag{4.2}
\]

Every two-shore projection is the complete bipartite graph `K_(2,2)`, and
assigning weight `1/2` to every triple is an exact fractional perfect
matching.  But there is no integral perfect matching: two disjoint triples
would have to be bitwise complements, and the complement of every
even-parity triple has odd parity and is absent.

This example is functional in the same sense as a Johnson seam: every
tail--head pair carries exactly one colour.  Hence uniqueness of the
intersection colour does not remove the obstruction.

In the functional formulation, either head--colour perfect matching selects
two columns having the same unique tail.  Its Hall cut at that tail shore
fails immediately.

Disjoint unions of this gadget give arbitrary size examples with perfect
two-shore projections, exact fractional marginals, and integral matching
number only half the required size.  Therefore the raw `k=17` projection
equalities cannot imply global colored endpoint matching by any ordinary
Hall argument.

## 5. Connectivity is a separate graphic/branching gate

A perfect colored endpoint matching gives a directed permutation of the
physical blocks, generally with several cycles.  It is one Hamilton cycle
exactly when

\[
        \sum_{e:\operatorname{tail}(e)\in S,
                     \operatorname{head}(e)\notin S}y_e\ge1
 \quad(\varnothing\ne S\subsetneq\mathcal B).                \tag{5.1}
\]

For a linear path with `n-1` seams, the equivalent undirected graphic rows
are

\[
       \sum_{e:\,c_-(e),c_+(e)\in S}y_e\le |S|-1
       \quad(\varnothing\ne S\subseteq\mathcal B),            \tag{5.2}
\]

together with endpoint capacity and exactly `n-1` edges.

These constraints cannot be absorbed into Theorems 1.1 or 3.1.  In the
oriented edge formulation, tail degree, head degree, and colour are already
three partition resources; connectivity adds a graphic/subtour resource.
A generic branching or two-matroid theorem therefore does not promote
singleton-complete support to the desired path.

Dropping either colour or one endpoint role produces familiar flow or
branching problems.  The full endpoint object keeps all of them
simultaneously and already contains the parity obstruction before topology
is considered.

## 6. Smallest exact formulation for the current route

For the joint minimum-cut route, the proof-safe hierarchy is:

1. **cut network:** one integral shortest path per old owner cycle;
2. **orientation/head--colour master:** variables `z,u` satisfying
   (3.1)--(3.2);
3. **functional-Hall oracle:** min-cut separation of (3.3);
4. **seam recovery:** a bipartite matching from selected tails to selected
   head--colour columns;
5. **connectivity:** subtour cuts (5.1) or graphic rows (5.2);
6. **upper and exact residence:** the separately required cover and
   automaton rows.

Stages 2--4 are an exact colored endpoint matching theorem.  Stage 5 is the
precise additional gate needed to turn it into one chronology.

## 7. Expansion target

The strongest natural expansion statement is not singleton degree and not
pairwise projected Hall.  It is the existence of `z,u` such that

\[
 \sum_{a:\,P_a\cap X\ne\varnothing}u_a
 \ge
 \sum_{B^\sigma\in X}z_{B,\sigma}
 \qquad\text{for every oriented tail family }X.               \tag{7.1}
\]

For a bounded-defect result, replace the right side by

\[
               \sum_{B^\sigma\in X}z_{B,\sigma}-C.           \tag{7.2}
\]

Then the min-cut theorem gives a colored endpoint matching missing at most
`C` tails.  This is the exact quantitative expansion row that an
`O(1)` construction must prove before graphic connectivity and the terminal
compiler are addressed.

No positive `C=o(n)` follows from singleton completeness or perfect
two-shore projections alone, by Section 4.
