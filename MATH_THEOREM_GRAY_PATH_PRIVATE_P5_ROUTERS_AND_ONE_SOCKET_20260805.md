# One complete-transfer multiset Gray path supplies abstract private P5 routers and at most one socket

**Date:** 2026-08-05  
**Method:** deterministic decomposition of a Hamilton path into five-vertex
blocks; no computation or search  
**Status:** unconditional graph-theoretic decomposition inside the
abstract complete-transfer capacity-two graph.  It does not yet apply to
the physical adjacent-necklace sector, which has only cyclic
nearest-neighbour transfers, a rotational quotient, and a hub-colour
partition constraint.  Even in a genuine complete-transfer cap fibre,
external claim and terminal occurrence types remain separate premises.

## 0. Input

Let `G_(n,R)` be the capacity-two unit-transfer graph from
`MATH_THEOREM_CAPACITY_TWO_GRAY_PATH_ELIMINATES_ODD_BULK_BLOSSOM_20260805.md`.
The multiset-combination Gray-code theorem gives a Hamilton path

\[
                         v_0,v_1,\ldots,v_{N-1},
 \qquad N=|\mathcal T_{n,R}|.                            
\tag{0.1}
\]

Fix any integer `q` with `5q<=N`.

## 1. Five consecutive vertices are a complete private router

For task `f=0,...,q-1`, abbreviate

\[
\begin{aligned}
 t_f^0&=v_{5f},&
 p_f^0&=v_{5f+1},&
 s_f&=v_{5f+2},\\
 p_f^1&=v_{5f+3},&
 t_f^1&=v_{5f+4}.&&
\end{aligned}
\tag{1.1}
\]

Then the Gray path contains the two prefixes

\[
                         s_f-p_f^0,qquad s_f-p_f^1,
\tag{1.2}
\]

and the two suffixes

\[
                         p_f^0-t_f^0,qquad p_f^1-t_f^1.
\tag{1.3}
\]

### Theorem 1.1 (path-block private router)

The `q` systems (1.1)--(1.3) are complete private two-port routers:

1. different tasks have disjoint vertex sets;
2. the two branches of one task meet only at `s_f`;
3. all ports and sinks are distinct; and
4. every prefix and suffix is one literal unit-transfer edge.

For either choice `epsilon_f in {0,1}`, the paths

\[
                         s_f-p_f^{\epsilon_f}-t_f^{\epsilon_f}
\tag{1.4}
\]

are pairwise vertex-disjoint.

#### Proof

Every assertion is immediate from the fact that the displayed vertices
form disjoint consecutive five-vertex subpaths of the simple Hamilton path.
\(\square\)

Unlike the Boolean-cube router, this construction does not require all
suffixes to belong to an independently selected perfect matching.  The
path itself supplies both the alternatives and the bulk completion below.

## 2. The unused branch matches internally

If task `f` uses branch `epsilon_f`, match the two vertices on its unused
branch by the edge

\[
                         p_f^{1-\epsilon_f}t_f^{1-\epsilon_f}.
\tag{2.1}
\]

These `q` edges are disjoint from every selected route and from one
another.

The unreserved tail

\[
                         v_{5q},v_{5q+1},\ldots,v_{N-1}
\tag{2.2}
\]

is still a path.  Match consecutive pairs along it.

### Theorem 2.1 (routers plus one socket)

For every independent branch choice `(epsilon_f)`, the capacity-two sector
decomposes into

\[
 \boxed{
 q\text{ vertex-disjoint source-to-sink routes}
 \;\dot\cup\;
 q\text{ unused-branch matching edges}
 \;\dot\cup\;
 \text{a bulk matching}
 \;\dot\cup\;
 \text{at most one socket}.}
\tag{2.3}
\]

#### Proof

Inside each five-vertex block, the chosen route uses three vertices and
the unused edge uses the other two.  Hence all first `5q` vertices are
accounted for exactly once.  Alternating edges on the remaining path cover
all of its vertices when its order is even and all but one when its order
is odd. \(\square\)

The decomposition is literal and has no Hall, Rado, gammoid, or blossom
premise.

## 3. Central odd sector

For `R=n`, the central sector order `N` is odd.  Since `5q` is odd exactly
when `q` is odd, the tail parity may vary, but Theorem 2.1 always leaves at
most one socket.  The socket is the final unmatched vertex of (2.2), and
its physical identity is explicit after fixing the extreme Gray path.

### Corollary 3.1 (abstract complete-transfer receiver bulk)

For every fixed `q` and sufficiently large `n`, the central odd
**complete-transfer graph** simultaneously supports `q` abstract private
routes and a matching of every other vertex except at most one.

No replacement of the physical dyadic blossom-factor bank or the typed
active-port suffix-router theorem follows without the additional lifting
conditions in Section 4.

## 4. Exact remaining physical and typed interface

The theorem is deliberately co-designed: its abstract claim sources are
the middle vertices `s_f` of the selected Gray blocks.  To use it in the
OR-word induction one must still prove:

1. every Gray edge used in a block is a legal cyclic nearest-neighbour
   transfer in the physical sector, or is replaced by a literal bounded
   physical path whose interiors are mutually private;
2. the selected labelled blocks descend without collision through the
   background-stabilizer quotient and satisfy the hub-colour partition
   constraint;
3. every bounded external gain can be represented by one selected `s_f`
   occurrence in the same cap/guard state;
4. both endpoint sinks `t_f^0,t_f^1` have a terminal type legal for that
   gain, or the Gray path can be chosen inside the corresponding typed
   sector; and
5. the single residual socket is exported by the regenerative sidecar.

The first two are macroscopic physical constraints.  The last three are
the occurrence-labelled typed interface.

## 5. Scope

The theorem does not assert that an arbitrary pre-fixed receiver bank lies
on the Ruskey--Savage path.  Under a genuine complete-transfer premise it
permits the bounded receiver roles to be chosen together with the global
cap path.  It makes no assertion about cyclic nearest-neighbour lifting,
hub-rainbow descent, upper shadows, residence, or the surrounding owner
carrier.
