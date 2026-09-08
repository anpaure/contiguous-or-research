# No interior four-cycle splicing in the middle-levels incidence graph

Date: 2026-07-26

Let (J) have size (2r), and let

\[
 \mathcal X=\binom Jr,qquad
 \mathcal Y=\binom J{r+1},qquad
 M(J)=(\mathcal X,\mathcal Y;\subset).
\]

This note settles the proposed successor to the two-cut rectangle lane.
An ordinary degree-preserving two-edge switch would replace

\[
                  XY,\ X'Y'
       \quad\hbox{by}\quad XY',\ X'Y,                  \tag{0.1}
\]

where (X,X'\in\mathcal X), (Y,Y'\in\mathcal Y), and all four
incidences are present.  Such a switch is exactly an alternating
four-cycle.  There are no nondegenerate four-cycles in (M(J)).

Consequently no amount of residual degree slack, no freezing convention at
the Dyck ports, and no prescribed first-edge balance can make the proposed
move available.  The graph of spanning (b)-factors under interior
four-cycle switches is edgeless.  In particular, the nonidentity endpoint
permutation in the explicit rank-three (b)-factor of Proposition 7.2 in
`MATH_ATTACK_S_PORT_PATH_FACTOR_HALL_20260726.md` is a statewise
counterexample: four-cycle splicing cannot alter it at all.

## 1. The incidence graph is (C_4)-free

### Theorem 1.1

The bipartite graph (M(J)) contains no simple cycle of length four.

#### Proof

Suppose distinct (X,X'\in\mathcal X) had two distinct common neighbours
(Y,Y'\in\mathcal Y).  Then

\[
                         X\cup X'\subseteq Y\cap Y'.    \tag{1.1}
\]

Because (X,X') are distinct (r)-sets,

\[
                         |X\cup X'|\ge r+1.             \tag{1.2}
\]

Both (Y) and (Y') have size (r+1).  If the union in (1.2) has size
larger than (r+1), it cannot be contained in either one.  If it has size
exactly (r+1), containment forces

\[
                         Y=X\cup X'=Y',                 \tag{1.3}
\]

contrary to (Y\ne Y').  Thus two distinct lower vertices have at most one
common upper neighbour, which excludes a (K_{2,2}), equivalently a
four-cycle.  \(\square\)

The argument is hereditary: every residual support (G\subseteq M(J)) is
also (C_4)-free.

## 2. Exact obstruction to two-edge splicing

Let (F\subseteq E(M(J))) be any simple integral (b)-factor, with any
demand vector.  A nontrivial two-edge switch preserving every vertex degree
requires four distinct vertices as in (0.1).  The four old and new edges
form a (K_{2,2}).  Theorem 1.1 gives the following.

### Corollary 2.1

There is no nontrivial degree-preserving two-edge switch in a simple
(b)-factor of (M(J)).  This remains true after arbitrary edges are
forbidden or frozen.

Degenerate choices do not help.  If (X=X') or (Y=Y'), the proposed new
edge multiset equals the old one (or repeats one edge), and hence does not
produce a new simple (b)-factor.

### Corollary 2.2 (statewise monodromy obstruction)

Fix the degree vector

\[
 b(P)=b(J\setminus P)=1\quad(P\in\mathcal D_r),
 \qquad b(v)=2\quad\hbox{at every other vertex}.        \tag{2.1}
\]

Under the move system consisting only of interior alternating four-cycle
switches, every (b)-factor is an isolated state.  Its component
decomposition and its induced endpoint permutation are exact invariants.

In particular, the rank-three factor displayed in (7.8) of the Hall note
has endpoint permutation

\[
                         (124\ 134\ 135),               \tag{2.2}
\]

with the other two roots fixed.  It is degree-feasible but not
complement-paired.  Since no four-cycle switch exists even in the full
ambient graph, it cannot be repaired by the proposed splicing scheme.  This
counterexample already allows every interior incidence and imposes no
balanced first-edge restriction, so adding residual-slack hypotheses cannot
rescue a four-cycle theorem.

## 3. The genuine smallest switches

For (r\ge2), the girth is exactly six.  Given an ((r-1))-set (K) and
three distinct elements (a,b,c\notin K), one has the cycle

\[
\begin{aligned}
 K a&\subset K a b\supset K b
     \subset K b c\supset K c
     \subset K c a\supset K a .                       \tag{3.1}
\end{aligned}
\]

Together with Theorem 1.1 this proves the girth assertion.  Toggling the
three alternating edges of (3.1) is the smallest possible degree-preserving
move.

When the six cycle vertices are internal and each has one selected external
half-edge, the two alternating matchings of (3.1) pair those six half-edges
in two ways whose union is one six-cycle.  On three distinct traversing
strands the local attachment changes by a three-cycle, not by a
transposition.  Thus the direct transposition intuition attached to a
four-cycle does not transfer unchanged to the genuine minimal move.

Any viable splicing theorem must therefore use at least one of the following
larger objects:

1. alternating six-cycles, with an explicit audit of the resulting
   three-strand attachment and of the pair cuts;
2. alternating cycles of length at least eight, or composite packets of
   six-cycles, to obtain odd endpoint permutations;
3. path-menu exchanges which change more than two incidence edges at once.

Avoiding endpoint-incident edges would indeed preserve a prescribed
first-edge layer under these larger moves.  What is not automatic is the
complement monodromy: Theorem 3.1 of the Hall note still requires all
prescribed-pair cuts, and a local degree toggle alone does not certify them.

## 4. Exact conclusion

The proposed robust four-cycle splicing theorem is false for a statewise
reason:

\[
 \boxed{
 M([2r])\text{ is }C_4\text{-free, so its interior two-edge-switch graph
 is empty.}}
\]

The first meaningful successor is a six-cycle or larger-packet theorem.
No conclusion about constant one follows merely from degree feasibility or
from first-edge slack.
