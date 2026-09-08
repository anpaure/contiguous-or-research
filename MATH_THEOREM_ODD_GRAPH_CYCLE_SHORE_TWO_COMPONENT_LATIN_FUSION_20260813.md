# The odd graph-absorber cycle shore fuses into two positive-resident lower-rainbow components

**Date:** 2026-08-13  
**Status:** unconditional explicit construction for every odd `q >= 3`  
**Scope:** owner row, closed trace, flat positive residence, and complete
immediate-lower row

## 1. Odd graph shore

Write

\[
 q=2h+1,\qquad
 A=\{a_i:i\in\mathbb Z_q\},\qquad
 B=\{b_j:j\in\mathbb Z_q\}.                       \tag{1.1}
\]

In the odd star--cycle absorber, after deleting the distinguished edge
`uv`, the graph is

\[
 G=K_{A,B}\cup uA\cup uB.                         \tag{1.2}
\]

There is one further vertex `v` in the ambient graph signature, but it is
isolated in `G`.  As usual,

\[
 \Omega(e)=D\cup(V\setminus e)                    \tag{1.3}
\]

maps graph edges injectively to rank-`R` owners.  Two such owners are
Johnson adjacent exactly when their graph edges meet in one vertex.

## 2. A Latin edge cycle for the bipartite part

For `i,p in Z_q`, put

\[
 e_{i,p}=a_i b_{p-i}.                              \tag{2.1}
\]

Order all `q^2` edges lexicographically in `(i,p)`:

\[
 e_{0,0},e_{0,1},\ldots,e_{0,q-1},
 e_{1,0},\ldots,e_{q-1,q-1}.                      \tag{2.2}
\]

Read (2.2) cyclically.

### Theorem 2.1 (resident Latin cycle)

The `Omega`-image of (2.2) is a simple closed Johnson owner cycle which:

1. uses every owner over `K_(A,B)` exactly once;
2. has a simple complete immediate-lower row; and
3. has every nonconstant positive run of length at least `q`.

### Proof

Inside row `i`, consecutive edges share `a_i`.  The last edge of row `i`
is

\[
 e_{i,q-1}=a_i b_{-i-1},                           \tag{2.3}
\]

while the first edge of row `i+1` is

\[
 e_{i+1,0}=a_{i+1}b_{-i-1}.                       \tag{2.4}
\]

Thus every seam, including the cyclic wrap, is a graph-edge intersection.
All edges in (2.2) are distinct, proving owner simplicity and closure.

An internal row turn has graph-vertex triple

\[
 \{a_i,b_{p-i},b_{p+1-i}\},\qquad0\le p<q-1,     \tag{2.5}
\]

whereas the seam after row `i` has triple

\[
 \{a_i,a_{i+1},b_{-i-1}\}.                       \tag{2.6}
\]

The two types have different `A/B` signatures.  Within either type the
displayed indices recover the turn.  Hence all triples, and therefore all
literal lower targets

\[
 D\cup(V\setminus\{x,y,z\}),                      \tag{2.7}
\]

are distinct.

For `a_i`, its `q` incident edges form one consecutive row block.  Its
unique positive run therefore has length `q^2-q >= q`.

Fix `b_j`.  In row `i` its edge occurs at the unique position

\[
 p_i(j)=j+i\pmod q.                                \tag{2.8}
\]

If `p_i(j)<q-1`, the cyclic distance to its occurrence in row `i+1` is
`q+1`; if `p_i(j)=q-1`, that distance is one.  Thus every nonempty
positive run between `b_j`-zero positions has length exactly `q`.
The coordinates `u,v` are constant on this component.  This proves
positive residence. \(\square\)

## 3. The `u`-star component

Choose any cyclic order

\[
 z_0,z_1,\ldots,z_{2q-1}                           \tag{3.1}
\]

of the `2q` distinct points of `A union B`, and use the graph-edge word

\[
 uz_0,uz_1,\ldots,uz_{2q-1}.                      \tag{3.2}
\]

### Lemma 3.1

The `Omega`-image of (3.2) is a simple closed Johnson owner cycle.  Its
immediate-lower targets are simple, and every nonconstant positive run has
length `2q-1 >= q`.

### Proof

Every two consecutive graph edges share `u`, and the edges are distinct.
The lower triple at a turn is

\[
 \{u,z_i,z_{i+1}\}.                               \tag{3.3}
\]

The adjacent pairs of a simple cyclic order of length `2q >= 6` are
distinct, proving lower simplicity.  The coordinate `u` is constantly
zero in the owner trace; every `z_i` is zero once and positive at the
other `2q-1` positions; and `v` is constantly positive.  This proves the
run assertion. \(\square\)

## 4. Exact two-component factor

### Theorem 4.1 (odd cycle-shore fusion)

The two cycles in Theorem 2.1 and Lemma 3.1 are owner-disjoint and together
use every owner over `E(G)` exactly once.  Their aggregate immediate-lower
row is simple, and both components admit exact cyclic flat antecedents at
depth `q-1`.

### Proof

The graph edge sets `E(K_(A,B))` and `u(A union B)` are disjoint and
partition (1.2), so injectivity of `Omega` proves the owner statement.
Every lower triple of the first component is contained in `A union B`,
whereas every lower triple of the second contains `u`.  The two lower
rows therefore cannot collide.  Each is internally simple by Theorem 2.1
and Lemma 3.1.

Finally, the cyclic flat-antecedent criterion says that a Boolean owner
trace has a depth-`(q-1)` sliding-OR antecedent precisely when every
nonconstant positive run has length at least `q`.  The two preceding
results verify this coordinatewise. \(\square\)

The only named immediate-upper targets touched by this factor are

\[
 \{D\cup(V\setminus\{z\}):z\in A\cup B\cup\{u\}\}, \tag{4.1}
\]

so there are only `2q+1` of them, although many occurrences repeat.  They
may be handled by the same external-backup convention as the original
short graph absorber.

## 5. Consequence and exact scope

The original odd decomposition used `q` separate `C_(q+2)` components and
had an unresolved run-safe port-mating problem.  Theorem 4.1 replaces that
family by exactly two closed components with no cuts and no seam matching.
Together with the previously proved one-path fusion of the star shore, the
growing cycle-shore component defect is gone in both parities:

* even `q >= 6`: one closed resident cycle by the direct Euler formula;
* odd `q >= 3`: two closed resident cycles by Theorem 4.1.

The theorem deliberately proves positive rather than dual residence.  The
`u`-star has singleton zero runs, and some `b_j` zero clusters in the Latin
cycle have length one or two.  Positive residence is exactly what flat
inversion requires.  The construction also does not make the repeated
upper occurrences injective and does not supply sockets or cap routing.
Those are later protected-host rows; they no longer include a growing
cycle-shore fusion problem.
