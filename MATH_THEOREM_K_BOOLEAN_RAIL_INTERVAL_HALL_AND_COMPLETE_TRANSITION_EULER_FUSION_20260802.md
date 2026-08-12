# Boolean rail intervals, local Hall, and complete-transition Euler fusion

**Date:** 2026-08-02  
**Status:** unconditional exact reduction, two proof-level sufficient
criteria, and a sharp obstruction to deriving chronology from Boolean
containment degrees alone.  The note starts after an owner/target-exact
static flag table has been chosen.  It does not construct that table with
the required rail properties in every dimension.

## 0. Outcome

For a fixed static marked-flag table, write the fixed head word of role `i`
as

\[
                 h_i=(A_{i,1},\ldots,A_{i,d}).          \tag{0.1}
\]

The legal leading letter is not a generic Boolean neighbour.  A head token
`j` can precede role `i` exactly when

1. the last `d-1` letters of `h_j` equal the first `d-1` letters of `h_i`;
   and
2. its first block lies in the Boolean interval which completes owner `i`.

This decomposes the balance problem into literal **rail fibres**.  Every
fibre is a bipartite interval-containment graph.  The following statements
are proved below.

1. A balanced one-copy selector exists exactly when all rail fibres satisfy
   Hall.  Their degrees have closed Boolean interval formulas.
2. In a rail fibre, minimum role degree at least maximum head-token degree
   is a simple sufficient Hall certificate.
3. If the rail multigraph is balanced and connected and every local rail
   fibre is complete bipartite, an Euler tour of the rail multigraph gives
   one literal Hamilton rotor immediately.  It uses every owner and every
   marked target once and has zero sidecar.  More generally, local
   alternating rectangles merge the circuits of any compatible transition
   system.
4. Independently, Woodall's directed Ore condition on the cloned
   predecessor digraph is a verifiable sufficient condition for the same
   Hamilton rotor, including a prescribed path after contraction.

These are genuine positive theorems, but they do not hold automatically for
a target-exact SCD selector.  The SCD flag formalism fixes middle roots and
lower targets before the trace-owner rainbow row; it is therefore a
calibration of the rail obstruction, not by itself an owner-exact instance
of the fixed-owner model in Section 1.  In a fully marked adjacent-rank
chain, every
difference block and the owner gap are singletons.  Each role then has at
most one predecessor, so Boolean shadow surplus disappears completely.  The
standard `B_7` SCD table has an explicit role with no legal successor even
though it has four Johnson-adjacent owner candidates.

Thus the all-dimensional lower-side problem is not ordinary matroid base
packing and cannot be discharged by containment degrees alone.  The exact
remaining lemma is to choose the owner/target-exact table so that its rail
multigraph is connected and its local interval graphs admit one
rectangle-interlaced transition system.  Complete local compatibility is a
strong, transparent sufficient face of that lemma.

Upper interval decks, residence, exterior chronology, and the terminal
common-cap compiler are not included unless they are encoded in the legal
leading-letter intervals before this theorem is applied.

## 1. Static marked flags and their Boolean intervals

Let `I` be the occurrence roles of an owner/target-exact static table.  Role
`i` has a distinct rank-`r` owner `T_i`, fixed nonempty suffix letters as in
(0.1), and a fixed marked payload.  Put

\[
 U_i=\bigcup_{t=1}^d A_{i,t},\qquad
 P_i=T_i\setminus U_i.                                  \tag{1.1}
\]

The admissible leading letters are exactly

\[
 \mathcal B_i={B:\varnothing\ne B,\quad
                    P_i\subseteq B\subseteq T_i\}.       \tag{1.2}
\]

Indeed, `B union U_i=T_i` is equivalent to (1.2).  Every choice in
`mathcal B_i` preserves the fixed head word, owner, and all proper-suffix
marks.

Define the two rail states and the first block

\[
 \lambda_i=(A_{i,1},\ldots,A_{i,d-1}),\qquad
 \rho_i=(A_{i,2},\ldots,A_{i,d}),\qquad
 c_i=A_{i,1}.                                           \tag{1.3}
\]

For `d=1`, both rail words are the unique empty word.

### Lemma 1.1 (literal predecessor identity)

The fixed head token `h_j` is a legal tail for role `i` if and only if

\[
             \rho_j=\lambda_i,
       \qquad P_i\subseteq c_j\subseteq T_i.             \tag{1.4}
\]

#### Proof

The tail of role `i` with leading letter `B` is

\[
                 (B,A_{i,1},\ldots,A_{i,d-1}).          \tag{1.5}
\]

Equality of (1.5) with `h_j` gives `B=c_j` and the rail equality in
(1.4).  The owner condition for this `B` is exactly the Boolean interval
condition in (1.4).  The converse is the same calculation backwards.
\(\square\)

Form the **cloned predecessor digraph** `D_F` on the role set `I`, putting

\[
                         j\longrightarrow i             \tag{1.6}
\]

exactly when (1.4) holds.  The word "cloned" matters when two roles have
equal physical head states: their head occurrences remain separate
vertices.

## 2. Exact rail-fibre Hall factorization

For a rail state `w`, put

\[
 H_w=\{j:\rho_j=w\},\qquad R_w=\{i:\lambda_i=w\}.       \tag{2.1}
\]

Let `G_w` be the bipartite graph from `H_w` to `R_w` whose edges are (1.4).
Thus `G_w` is a literal Boolean interval-containment graph.

### Theorem 2.1 (rail Hall is exact)

The static table admits a balanced one-copy trace selector if and only if

\[
 |H_w|=|R_w|
 \quad\text{and}\quad
 |N_{G_w}(X)|\ge |X|
 \quad(X\subseteq R_w)                                  \tag{2.2}
\]

for every rail state `w`.

Choosing one perfect matching in every `G_w` gives a directed circuit
partition of all role tokens.  One transition circuit is sufficient for a
zero-sidecar rooted chronology.  If the physical heads `h_i` are distinct,
it is also necessary.  With repeated physical heads, several token circuits
may already meet at one state; the exact condition is weak connectivity of
their physical union.

#### Proof

A balanced selector uses each fixed head token once as a tail.  Lemma 1.1
forces a token in `H_w` to be assigned to a role in `R_w`, and every such
assignment is legal exactly when it is an edge of `G_w`.  Hence balance is
one perfect matching in every fibre, which is equivalent to (2.2).

After choosing these matchings, every role has one predecessor token and
every head token has one successor role.  The resulting permutation of the
role occurrences is precisely the directed token-circuit partition.  One
permutation cycle is a connected Euler chronology.  When the heads are
distinct, different permutation cycles have disjoint state sets, proving
necessity as well.  In the repeated-head case, physical weak connectivity
is the exact Euler criterion. \(\square\)

### Exact Boolean degree formulas

For a block `B`, let

\[
 \mu_w(B)=|\{j\in H_w:c_j=B\}|.                         \tag{2.3}
\]

Then

\[
 \deg_{G_w}(i)
   =\sum_{B:\,P_i\subseteq B\subseteq T_i}\mu_w(B),     \tag{2.4}
\]

and, for `j in H_w`,

\[
 \deg_{G_w}(j)
   =|\{i\in R_w:P_i\subseteq c_j\subseteq T_i\}|.       \tag{2.5}
\]

These formulas include occurrence multiplicity.  No rankwise shadow count
may replace the rail condition `rho_j=lambda_i`.

### Corollary 2.2 (degree-domination Hall certificate)

Suppose `H_w,R_w` are nonempty and equal in size, and put

\[
 \delta_w=\min_{i\in R_w}\deg(i),\qquad
 \Delta_w=\max_{j\in H_w}\deg(j).                       \tag{2.6}
\]

If

\[
                         \delta_w\ge\Delta_w>0,          \tag{2.7}
\]

then `G_w` has a perfect matching.

#### Proof

For `X subseteq R_w`, count its incident edges.  At least
`delta_w |X|` leave `X`, while at most `Delta_w |N(X)|` enter its
neighbourhood.  Equation (2.7) gives `|N(X)|>=|X|`; Hall applies.
\(\square\)

This is only a sufficient degree test.  The exact and weakest cutwise
condition remains (2.2).

## 3. A sparse complete-transition Euler theorem

Make the directed **rail multigraph** `Q_F` whose vertices are rail words
and whose occurrence-labelled edge `i` runs

\[
                         \lambda_i\longrightarrow\rho_i. \tag{3.1}
\]

It is balanced exactly when `|R_w|=|H_w|` for every `w`.

For a nonempty rail fibre define

\[
 P^*_w=\bigcup_{i\in R_w}P_i,
 \quad C^-_w=\bigcap_{j\in H_w}c_j,
 \quad C^+_w=\bigcup_{j\in H_w}c_j,
 \quad T^*_w=\bigcap_{i\in R_w}T_i.                    \tag{3.2}
\]

### Lemma 3.1 (two Boolean cap tests)

The local graph `G_w` is complete bipartite if and only if

\[
                         P^*_w\subseteq C^-_w,
             \qquad     C^+_w\subseteq T^*_w.           \tag{3.3}
\]

#### Proof

Every pair `j in H_w, i in R_w` is legal exactly when
`P_i subseteq c_j subseteq T_i`.  Requiring the left inclusions for all
pairs is equivalent to the first inclusion in (3.3), and requiring the
right inclusions is equivalent to the second. \(\square\)

### Theorem 3.2 (complete-transition Euler fusion)

Assume:

1. `Q_F` is balanced;
2. its nonisolated underlying graph is connected; and
3. the two cap tests (3.3) hold at every nonempty rail state.

Then the static table admits one balanced connected literal trace selector.
It uses every owner and every declared named target exactly once and spells
one rooted Euler chronology with zero sidecar.

#### Proof

A finite connected balanced directed multigraph has an Euler circuit.  Read
one in `Q_F`.  Whenever occurrence edge `j` is followed by occurrence edge
`i`, their common rail vertex gives `rho_j=lambda_i`.  Condition (3.3) and
Lemma 3.1 give `P_i subseteq c_j subseteq T_i`, so Lemma 1.1 turns this
transition into the literal trace of role `i` from state `h_j` to state
`h_i`.

Every occurrence edge appears once in the Euler circuit.  Hence every role,
owner, fixed marked payload, and head token appears once.  The circuit is
already the required connected trace chronology; choose any one of its
occurrences as the root. \(\square\)

The theorem can be much sparser than a global minimum-degree theorem:
degrees need only fill their own rail fibre.

### Proposition 3.3 (local rectangle absorber)

Assume only (2.2), choose one perfect matching in every `G_w`, and consider
its circuit partition.  If more than one circuit remains and some rail state
`w` contains matched pairs

\[
                         j-i,\qquad j'-i'              \tag{3.4}
\]

belonging to different circuits such that both crossed pairs

\[
                         j-i',\qquad j'-i               \tag{3.5}
\]

lie in `G_w`, switching (3.4) to (3.5) preserves every owner and marked
target and merges the two circuits.

Consequently, if such a rectangle exists after every intermediate matching
choice with more than one circuit, repeated switches prove Theorem 3.2
without requiring complete fibres.

#### Proof

The switch preserves every role and every incoming head token.  Both new
transitions are literal by membership in `G_w`, so all labelled payloads and
state degrees are unchanged.  Cutting one transition in each of two
directed circuits and crossing the successors joins them into one directed
circuit.  Iteration terminates after one switch per merger. \(\square\)

If every `G_w` is complete and `Q_F` is connected, the rectangle condition
is automatic: two distinct circuits in an edge decomposition of a connected
multigraph meet at some rail vertex.

## 4. A general directed-degree certificate

Delete loops from `D_F`, and write `W=|I|`.  The following classical
directed Ore theorem supplies a second, independent certificate.

### Theorem 4.1 (Woodall certificate)

If every ordered pair of distinct roles `j,i` for which `j->i` is absent
satisfies

\[
                 d^+_{D_F}(j)+d^-_{D_F}(i)\ge W,       \tag{4.1}
\]

then `D_F` has a directed Hamilton cycle.  The corresponding traces form a
one-copy owner/target-exact rooted Euler chronology with zero sidecar.

#### Proof

The Hamilton conclusion is Woodall's directed Ore theorem: D. R. Woodall,
"Sufficient Conditions for Circuits in Graphs", *Proceedings of the London
Mathematical Society* (3) 24 (1972), 739--755.  Apply it to the loopless
cloned predecessor digraph.  Each Hamilton arc is a literal predecessor
assignment by Lemma 1.1.  Its cycle therefore selects every role and head
token once, preserves every fixed payload, and is one connected balanced
trace circuit. \(\square\)

Equations (2.4)--(2.5) make (4.1) a literal Boolean interval-degree check.
In particular, the stronger semidegree bounds

\[
                    \delta^+(D_F),\delta^-(D_F)\ge W/2 \tag{4.2}
\]

imply (4.1).

If a directed role path `P` must be protected, contract it to one vertex,
retaining arcs into its first role and arcs out of its last role.  Applying
(4.1) with the contracted order `W-|P|+1` gives a Hamilton cycle which
lifts to one containing `P`.  This is a sufficient protected-root test, not
a claim that every prescribed path satisfies it.

## 5. Why Boolean shadows alone cannot prove the lemma

The obstruction already appears on the most rigid high-chain face.

### Proposition 5.1 (singleton collapse)

Suppose every role marks a full chain of `d` adjacent ranks, so every
difference block `A_(i,t)` is a singleton, and suppose the owner gap `P_i`
is also a singleton.  If the full marked chains are globally distinct, then
every role has at most one predecessor in `D_F`.

If a balanced selector exists, its predecessor permutation is forced.  It
is connected if and only if that forced permutation is one cycle.

#### Proof

For a predecessor `j->i`, condition (1.4) requires the singleton `c_j` to
contain the singleton `P_i`; hence `c_j=P_i`.  Together with
`rho_j=lambda_i`, this fixes the complete head word `h_j`.  Global
distinctness of the full marked chains makes the head words distinct, so
there is at most one such `j`.

Hall can therefore hold only when every forced predecessor exists and they
are all distinct.  Then there is one forced cycle cover, whose components
are its permutation cycles. \(\square\)

No Kruskal--Katona or normalized-matching surplus survives this collapse:
the rail equality and singleton owner gap have already reduced the large
containment interval to one possible head word.

### Exact smallest root/target calibration

The standard recursive SCD at `(k,m,d)=(7,3,3)` is a root-exact and
named-target-exact marked table but fails before Hall.  It is not yet an
owner-exact fixed-`T_i` table in the sense of Section 1: its rank-`m+1`
turn owner is chosen only after a predecessor is attached.  It contains

\[
 p=\{0,1,6\},\qquad f_p=(p;1,0),\qquad B(f_p)=\{6\}. \tag{5.1}
\]

Its four Johnson-adjacent candidate successor roots are

\[
                 q_\beta=\{0,6,\beta\},
                 \qquad\beta\in\{2,3,4,5\}.           \tag{5.2}
\]

Their SCD flags are `f_(q_beta)=(q_beta;0,beta)`.  The rail shift requires
the new terminal deletion to lie in `B(f_p)={6}`, but it equals `beta`.
Thus `p` has no legal successor.  The corresponding rail interval graph has
an isolated occurrence, despite the four raw Boolean owner neighbours.

This is a literal counterexample to each of the following implications in
the SCD/root-flag chronology:

\[
 \text{root/target exactness}\Longrightarrow\text{rail Hall},
 \qquad
 \text{Boolean containment degree}\Longrightarrow\text{chronology}.
                                                               \tag{5.3}
\]

It does not furnish a counterexample to the stronger fixed-owner hypotheses
of Sections 1--4, and it does not rule out choosing a different SCD, target
table, or flag continuation.

The separate matched-tail Boolean construction already gives an internal
augmentation failure for the intersection of head capacity and graphic
acyclicity.  Hence the Hall-safe tree family is not a matroid in general;
ordinary matroid base packing cannot prove the desired theorem without an
additional common-potential, complete-transition, or absorber structure.

## 6. Exact remaining lower-side lemma

The stationary pull clock supplies a rational rail circulation, and the SCD
selector supplies an integral owner/target table.  Sections 2--5 show why
these projections cannot be rounded independently.

The weakest exact table-level assertion is:

> **Rectangle-interlaced rail lemma.**  Choose one owner/target-exact static
> flag table such that its rail multigraph is balanced and connected, every
> local Boolean interval graph has a perfect matching, and those local
> matchings can be joined by the rectangles of Proposition 3.3 into one
> transition circuit.

The exact replacement for "can be joined by rectangles" is that the chosen
local transition circuits have weakly connected physical union.  A single
token circuit is a stronger sufficient condition, and is equivalent when
the physical heads are distinct.  Theorem 3.2 proves the stronger condition
on the verifiable complete-local face (3.3), and Theorem 4.1 proves it on
the independent Woodall face (4.1).

What remains open is the Boolean construction of such a table from the
triangular target bank, possibly with a bounded prepared root.  A proof must
correlate the target-chain decomposition with the rail words; raw shadow
surplus controls only (1.2) after the rail has already been fixed.

Nothing in this note asserts upper-shadow coverage, residence, exterior
opening safety, or common-cap/compiler feasibility.
