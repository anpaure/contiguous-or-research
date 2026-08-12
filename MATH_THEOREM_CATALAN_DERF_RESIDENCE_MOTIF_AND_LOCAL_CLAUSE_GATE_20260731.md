# The direct-edgewise minimum-three residence gate is a local cubic system

Date: 2026-07-31  
Status: exact all-parameter local characterization; independently replayed
on the strict recursive witnesses at child parameters (n=3,4,5).  The
joint motif-free common-basis/physical-side theorem and seam automaton are
open.

## 0. Result

The sealed minimum-positive-run-three condition in the direct-edgewise
recursion has no hidden global hierarchy.  Once the selected physical
support is a path forest, it is exactly a family of local three-edge
constraints.

For a trace-block path

\[
                      v_0-v_1-v_2-v_3,                 \tag{0.1}
\]

the forbidden motif is

\[
 (v_1\cap v_2)\setminus(v_0\cup v_3)\ne\varnothing.  \tag{0.2}
\]

Equivalently, orient the three Johnson edges and write
(a(e),b(e)) for their deleted and inserted coordinates.  Then (0.1) is
bad exactly when

\[
                         b(e_0)=a(e_2).                 \tag{0.3}
\]

This condition is invariant under reversing the whole path.

It yields two exact clause families.

* On the punctured central (z)-rail, every bad triple of consecutive
  child edges must meet the deleted common-basis set (Q):

  \[
                         q_i\vee q_{i+1}\vee q_{i+2}.  \tag{0.4}
  \]

* On either direct side rail, precompute every bad three-occurrence
  physical path ((A,B,C)).  Its selection clause is

  \[
                         \neg s_A\vee\neg s_B\vee\neg s_C. \tag{0.5}
  \]

Subject to role injection, maximum degree two and acyclicity, (0.4)--(0.5)
are necessary and sufficient for all new trace-block bodies to satisfy the
minimum-three condition.  Seam and path-end events remain, but those belong
to the finite protected boundary automaton rather than to block interiors.

The copied (c)-rail gives the exact preservation caveat: it is clean at
the output threshold if and only if the child paths were already clean at
that **output** threshold.  Certification only at the child's smaller
deadline depth is not a right-total recursive state.

## 1. Why the only motif is `0110`

All four trace sectors have distinct edge-intersection colours.

* In the (c)- and (z)-sectors they are inherited child lower colours.
* In the (0)-sector they are the distinct selected direct-lift lower
  colours (L_q+x).
* In the (cz)-sector they are the distinct selected projection lower
  colours (L_q-x), with (c,z) adjoined uniformly.

### Lemma 1.1 (singleton runs are impossible)

Let (v_0-v_1-v_2) be an internal two-edge trace-block path.  No coordinate
can occur only at (v_1).

#### Proof

If (y) occurred only at (v_1), Johnson adjacency would give

\[
                       v_0\cap v_1=v_1-y=v_1\cap v_2,
\]

contradicting injectivity of the edge-intersection colours. \(\square\)

### Lemma 1.2 (exact length-two motif)

For (0.1), a coordinate has pattern `0110` if and only if (0.2) holds, if
and only if (0.3) holds.  The set in (0.2) is then the singleton containing
that coordinate.

#### Proof

If (y) has pattern `0110`, the first edge inserts (y), the middle edge
does not move it, and the third edge deletes it.  This proves all three
forms.  Conversely, if the first insertion equals the third deletion, the
coordinate cannot be moved by the intervening Johnson edge: deleting it
there would make it unavailable for the final deletion, while inserting it
there would repeat an already present coordinate.  Hence its bit pattern is
`0110`. \(\square\)

Lemmas 1.1--1.2 prove that minimum-three body safety is exactly the absence
of (0.2).

An equivalent graph formulation is useful.  For each coordinate (y),
induce the selected trace forest on the vertices containing (y).  Every
component which is internal to a trace block must have at least three
vertices.  The forbidden object is an internal two-vertex component.

## 2. Exact central and side clauses

Orient one child path and number its edges (e_0,e_1,\ldots).  Removing
(Q) splits it into the (z)-trace blocks.

### Theorem 2.1 (central hitting clauses)

The (z)-blocks are minimum-three body-safe if and only if (Q) meets
every consecutive bad triple

\[
        (e_i,e_{i+1},e_{i+2})quad	ext{with}quad
        b(e_i)=a(e_{i+2}).                             \tag{2.1}
\]

#### Proof

The three edges remain consecutive inside one punctured child component
exactly when none belongs to (Q).  Apply Lemma 1.2. \(\square\)

Thus the central condition is the monotone cubic system (0.4).

For a direct side, let an occurrence remember its child edge (q) and its
lift/projection coordinate (x).  Once oriented along its selected side
path, its deletion and insertion coordinates are exactly those of (q),
possibly swapped by reversal; the added or deleted (x) is constant on the
two physical endpoints.

### Theorem 2.2 (side forbidden-path clauses)

Assume the selected side occurrences have injective roles, maximum physical
degree at most two and acyclic physical support.  The side blocks are
minimum-three body-safe if and only if no selected triple of occurrences
whose physical edges form a bad three-edge path is selected in full.

#### Proof

Under the stated graph rows, every selected triple whose candidate physical
edges form a three-edge path occurs consecutively in one selected component.
Lemma 1.2 makes it bad precisely in the precomputed case (0.3), proving the
necessity of (0.5).  Conversely, every internal length-two run supplies its
three consecutive selected occurrences and therefore one violated clause.
\(\square\)

Equivalently, this is an ordinary path-cover problem in a second-order line
graph.  Its states are compatible ordered pairs ((e,f)), and

\[
                    (e,f)\longrightarrow(f,g)
       \quad\Longleftrightarrow\quad b(e)\ne a(g).     \tag{2.2}
\]

The residence row is therefore finite-memory and dimension-uniform.  It is
not implied by the separate matching and graphic rows.

## 3. Body-safe direct-edgewise lift theorem

### Theorem 3.1 (exact body factorization)

Fix the minimum-three threshold.  A strict direct-edgewise lift has every
maximal (0,c,z,cz) trace block body-safe if and only if:

1. the child paths are already minimum-three body-safe;
2. (Q) satisfies every central clause (0.4); and
3. the two selected direct side forests satisfy every clause (0.5).

#### Proof

The (c)-blocks are literal copies of the child paths.  The (z)-blocks
are governed by Theorem 2.1.  The (0)- and (cz)-blocks are exactly the
two side forests and are governed by Theorem 2.2.  The four sectors partition
the trace-block bodies. \(\square\)

Once Theorem 3.1 holds, every remaining residence event meets a block end or
a collar seam.  Prefix/suffix positive-run lengths capped at three are then
an exact finite boundary state, equivalently the minimum-three specialization
of the protected short-run event monoid.  This observation does not assert
that a globally accepting seam order exists.

## 4. Exact replay of the strict chain

The frozen chain gives the following complete motif census.

\[
\begin{array}{c|r|r|c|r|r}
n&\text{child bad}&\text{hit by }Q&\text{central survivors}&
 \text{upper bad}&\text{lower bad}\\ \hline
3&5&5&\varnothing&0&0\\
4&17&17&\varnothing&0&0\\
5&44&42&\{(118,119,120),(198,199,200)\}&3&8.
\end{array}                                             \tag{4.1}

At (n=3,4), neither selected side forest even contains a three-edge
window.  Thus every newly created (0,z,cz) block is body-safe; the
strict-interior defects in the outputs lie solely in the copied (c)-rail.
At (n=5), the two surviving central triples and the (3+8) bad side paths
are exactly the thirteen newly created nonchild block defects found by the
independent trace-block audit.

### Proposition 4.1 (smallest authenticated obstruction)

In the (n=3\to4) base lift, all five copied defects occur in the child
path

```text
25 23 2a 0e 16 32 38 19 0b 07 15 34 2c 29
```

in hexadecimal.  Their three-edge cut intervals are

\[
              [1,3], [2,4], [4,6], [7,9], [9,11].     \tag{4.2}
\]

The exact minimum interval-stabbing set has order three; one choice is
({3,6,9}).  Reversal or permutation of intact trace blocks cannot remove
these body motifs.

#### Proof

Directly apply (0.2) to every four-vertex window of the five authenticated
child paths.  Greedy right-endpoint stabbing of (4.2) is optimal for
intervals and yields the displayed set. \(\square\)

This is a local obstruction to the frozen base, not an impossibility theorem
for a jointly selected or internally rethreaded base.

## 5. The next-depth quantifier is load-bearing

At ground size six, the accepted deadline depth is one; at ground size
eight it is two.  Hence the first direct lift asks the copied child path to
satisfy a stronger minimum-three rule than the rule needed at its own
dimension.  Proposition 4.1 shows the failure literally.

More generally, the deadline depth is unbounded.  Every finite internal
positive run in a sealed child path is copied unchanged at every later
direct lift and eventually violates a larger threshold.  Therefore a state
which exports only current-depth safety cannot be right-total for the strict
recursion.

The exact remaining quantifier is:

> jointly choose or regenerate the child chronology at the **output-depth**
> guard, choose a strict common basis satisfying the central motif clauses,
> choose both side representative forests in the allowed second-order line
> graphs, and compose all exposed boundary events with the same private
> shadow/compiler ownership relation.

Theorems 2.1--3.1 remove sealed residence from the global mystery: it adds
only monotone cubic clauses on (Q) and negative cubic clauses on side
occurrences at the minimum-three threshold.  The unresolved part is their
simultaneous feasibility with the physical/common-basis rows and the
boundary/compiler relation.

## 6. Audit

The standard-library script

```text
scratch/audit_catalan_derf_residence_motif_gate_20260731.py
```

authenticates the strict recursive witness, reconstructs every child,
central and selected side path, verifies intersection-colour injectivity,
checks (0.2)--(0.3) window by window and writes

```text
scratch/catalan_derf_residence_motif_gate_20260731.audit.json
```

It independently reproduces (4.1)--(4.2).  No solver status or all-parameter
feasibility claim is used.
