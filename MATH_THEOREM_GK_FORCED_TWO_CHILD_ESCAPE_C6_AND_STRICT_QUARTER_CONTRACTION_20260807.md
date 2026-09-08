# A forced two-child GK bank reduces strict `<1/4` contraction to one internal-close rethread

**Date:** 2026-08-07  
**Status:** unconditional endpoint/combinatorial theorem and exact scope
audit.  Given a standard optimal depth-two path cover, the construction
produces enough external joins to cross the strict one-quarter threshold
for all `m>=44`.  The closing-child half uses proved paired `C_6`s; the
internal-close half still requires one explicitly identified noncanonical
rethread.  Therefore unconditional physical contraction is not claimed.

## 1. A rigid positive-density primitive family

For `D in D_{m-3}`, define

\[
                         U_D=11D0100.                  \tag{1.1}
\]

In rooted-tree language, `U_D` is primitive and its outer root has exactly
two children: the first has interior `D`, and the second is a leaf.  Put

\[
                         \mathcal G_m=\{U_D:D\in D_{m-3}\}.
\]

Thus

\[
                         |\mathcal G_m|=\operatorname {Cat}_{m-3}.       \tag{1.2}
\]

The two child openers give two different depth-two sockets at `U_D`.

## 2. The later-child edge is forced in every optimal standard cover

Use the second-child opener and its adjacent closing downstep.  The
depth-two flip is

\[
                         U_D=11D0100
                         \longrightarrow
                         V_D=11D0010.                  \tag{2.1}
\]

The first primitive of `V_D` has semilength `m-1`, and the final `10` is
its only later primitive.  The exact indegree formula for the depth-two
orientation therefore gives

\[
                         d^-(V_D)=m-(m-1)=1.           \tag{2.2}
\]

Its unique predecessor is `U_D`.

## Theorem 2.1 (forced base bank)

Every matching from all nonsink roots onto all nonprimitive roots contains
every edge (2.1).

### Proof

Every nonprimitive target must be matched.  By (2.2), `V_D` has only the
one possible matching edge (2.1). \(\square\)

The sources `U_D` and targets `V_D` are all distinct.  Hence these forced
edges form a matching.  They use the later-child socket, leaving the
first-child socket unused.

## 3. Two explicit first-child escape banks

The first choice uses the downstep closing the first child.  It gives

\[
                         U_D\longrightarrow W_D^0:=10D1100.             \tag{3.1}
\]

For the second choice, assume `D` is nonempty and write its first-return
decomposition as

\[
                         D=1F0G.
\]

Change the displayed closing downstep of that first primitive upward.  Put

\[
                         D^+=1F1G.
\]

The corresponding first-child flip is

\[
                         U_D\longrightarrow W_D^1:=10D^+0100.          \tag{3.2}
\]

Both targets begin with `10`, so both are sinks of the standard
orientation.

## Lemma 3.1 (two disjoint sink banks)

As `D` varies over nonempty Dyck words of semilength `m-3`, each of the
maps `D -> W_D^0` and `D -> W_D^1` is injective, their two images are
disjoint, and neither image meets the forced target bank `{V_D}`.

### Proof

For the first map, delete the initial `10` and terminal `1100` to recover
`D`.

For the second, delete the initial `10` and terminal `0100` to recover
`D^+`.  In `D^+`, the changed step is the last upstep from height one to
height two: after it the suffix `G` stays at height at least two.  Changing
that step downward recovers `D`.  Thus the second map is injective.

The first image ends in `1100`, while the second ends in `0100`, so they
are disjoint.  Both begin in `10`, whereas every `V_D` begins in `11`.
\(\square\)

The edges in (2.1) and (3.1) are edges of the root-rotation graph `R_m`:
in both cases `x` is the downstep closing the excursion opened by `b`.
Their paired-root `C_6`s therefore combine into a literal degree-two root
path through `U_D`.

The edge (3.2) is different.  Its chosen `x` lies strictly inside the
first-child excursion.  It is a valid depth-two edge, and global
socket-colour injectivity gives it a private `a` and unused `B_y`, but it
is not an edge of `R_m`.  The proved paired-`C_6` theorem does not supply
its reverse endpoint rethread.  This distinction is the sole local gap in
the two-choice escape.

## 4. One escape is external for every rigid root

Assume now that an optimal standard directed path cover has been selected.
It has one component starting at every primitive root and one component
ending at every sink root.

Fix nonempty `D`.  The two sinks `W_D^0` and `W_D^1` are distinct.  The
component starting at `U_D` has exactly one sink endpoint.  Therefore at
most one of these two sinks belongs to that component.

Choose

\[
 E_D=
 \begin{cases}
 U_DW_D^0,&W_D^0\text{ is outside the component of }U_D,\\
 U_DW_D^1,&W_D^0\text{ is inside that component}.
 \end{cases}                                           \tag{4.1}
\]

Every `E_D` joins two distinct cover components.  By Lemma 3.1, the
chosen root edges form a matching: their primitive sources and sink
targets are separately distinct.

On the component set, the edges (4.1) therefore have indegree and
outdegree at most one and no loops.  Their components are directed paths
and directed cycles of length at least two.  Delete one edge from every
cycle.  At least half remain, and the remaining component graph is a
forest.

## Theorem 4.1 (escape-join count)

Every optimal standard depth-two path cover admits at least

\[
                 J_m:=\left\lfloor{operatorname {Cat}_{m-3}-1\over2}
                       \right\rfloor                  \tag{4.2}
\]

simultaneously acyclic primitive--sink joins from the two escape banks.
Each join uses a first-child socket distinct from the forced base socket.
The joins of type (3.1) have the paired-`C_6` fusion.  Joins of type (3.2)
still require a certified internal-close rethread.

The subtraction of one only removes the exceptional empty word `D` for
which the second escape is unavailable.

## 5. The strict one-quarter inequality

Let

\[
                         N=\operatorname {Cat}_m,
 \qquad                  C=\operatorname {Cat}_{m-1}.
\]

The optimal standard cover has `C` components.  The amount that must be
removed to go strictly below `N/4` is

\[
                         C-{N\over4}={3N\over4(2m-1)}. \tag{5.1}
\]

Also

\[
 {\operatorname {Cat}_{m-3}\over\operatorname {Cat}_m}
 ={m(m-1)(m+1)\over
   8(2m-5)(2m-3)(2m-1)}.                              \tag{5.2}

The unfloored inequality

\[
 {1\over2}\operatorname {Cat}_{m-3}
 >{3N\over4(2m-1)}                                    \tag{5.3}

is equivalent to

\[
                         m(m^2-1)>12(2m-5)(2m-3),       \tag{5.4}

which holds from `m=44` onward.  Direct integer comparison including the
floor and the single excluded word gives the same threshold.

## Corollary 5.1 (conditional strict root contraction)

For every `m>=44`, any optimal standard depth-two path cover, together
with the forced/escape bank above **and a degree-two rethread for every
selected internal-close edge (3.2)**, contracts the
`Cat_m` root components to strictly fewer than

\[
                         {1\over4}\operatorname {Cat}_m               \tag{5.5}
\]

root paths.

## 6. Exact scope and remaining theorem

The proof is root-incidence exact:

* the later-child base edge is forced, not selected by an unproved
  averaging argument;
* one of two explicit first-child sinks is always external;
* the selected extra edges form a matching before cycle deletion;
* the two sockets at each `U_D` are different;
* the paired-root `C_6` theorem supplies the degree-two fusion for (3.1);
* (3.2) isolates the only additional local rethread; and
* the quantitative join count beats the strict threshold.

Two global hypotheses remain outside this theorem.

1. **Optimal standard cover existence.**  Equivalently, the standard
   nonsink-to-nonprimitive depth-two bipartite graph must have a perfect
   matching.  This is verified in finite layers but its all-`m` Hall
   theorem is not proved here.
2. **Internal-close rethread.**  The reverse of (3.2) must be embedded as
   a degree-two alternating circuit.  Ordinary paired-root `C_6` algebra
   does not cover it.
3. **Protected-ticket transport.**  The selected root path bank must
   coexist with the residence, arbitrary-upper and terminal compiler
   tickets of the Pascal child.

Thus the component count and endpoint Hall problem are closed.  The exact
new local target is the internal-close rethread for (3.2), in addition to
the ordinary base-cover Hall and downstream protected-ticket transport.
No Hamilton cycle, random permanent estimate or global endpoint sorting
is required.
