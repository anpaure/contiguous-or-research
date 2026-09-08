# The q2 marginal closes by saturating-cycle clique insertion

**Date:** 2026-08-05  
**Method:** pure mathematics; one published optimal-cycle theorem plus exact
Boolean clique insertion; no computation, search, or solver  
**Status:** unconditional marginal theorem.  There is a spanning
`Cat_r`-component path forest on the rank-`(r-1)` layer whose edge
intersections cover every rank-`(r-2)` target and have exactly the surplus
required by the MSW `q=2` ledger.  The theorem does not simultaneously make
the edge unions distinct rank-`r` owners, does not preserve the canonical
MSW punctures, and therefore does not yet lift to an owner-once upper
carrier.

## 1. The two adjacent levels

Let `Omega` have order `2r`, `r>=2`, and put

\[
 \mathcal A={\Omega\choose r-2},
 \qquad
 \mathcal B={\Omega\choose r-1}.
\tag{1.1}
\]

Write

\[
 W={2r\choose r},
 \qquad
 A=|\mathcal A|={2r\choose r-2},
 \qquad
 V=|\mathcal B|={2r\choose r-1},
\tag{1.2}
\]

and

\[
 C=\operatorname {Cat}_r={W\over r+1}.
\tag{1.3}
\]

The optimal-cycle theorem of Gregor--Mička--Mütze for any consecutive
hypercube levels, specialized to the two levels in (1.1), gives an
alternating cycle

\[
 \mathscr Z\subseteq Q_{2r}[\mathcal A\cup\mathcal B]
\tag{1.4}
\]

which contains every member of the smaller shore `mathcal A`.  It
therefore contains exactly `A` members of `mathcal B`.

## 2. Insert every unused owner without losing a lower colour

Suppress the `mathcal A` vertices of `mathscr Z`.  For each
`a in mathcal A`, its two cycle neighbours are distinct sets

\[
 X_a=a+\{x_a\},
 \qquad
 Y_a=a+\{y_a\}
 \quad\hbox{in }\mathcal B.
\tag{2.1}
\]

Thus the suppressed edge `X_aY_a` has intersection colour `a`.

Every unused owner `B in mathcal B-V(mathscr Z)` contains at least one
rank-`(r-2)` set.  Assign `B` arbitrarily to one such `a subset B`.  For
each `a`, list its assigned owners as

\[
 D^a_1,\ldots,D^a_{t_a}.
\tag{2.2}
\]

Replace the suppressed edge of colour `a` by

\[
 X_a,D^a_1,D^a_2,\ldots,D^a_{t_a},Y_a.
\tag{2.3}
\]

### Theorem 2.1 (intersection-surjective Hamilton cycle)

After all replacements (2.3), the result is a Hamilton cycle `K` on the
entire vertex set `mathcal B`.  Every edge of the block (2.3) has
intersection exactly `a`.  Consequently

\[
 \boxed{
 \{X\cap Y:XY\in E(K)\}=\mathcal A.}
\tag{2.4}
\]

Every target `a` has multiplicity `1+t_a`.

#### Proof

All sets in (2.3) are distinct rank-`(r-1)` supersets of the same
rank-`(r-2)` set `a`.  Any two of them differ only in their one element
outside `a`; they are therefore Johnson adjacent and have intersection
`a`.  The assigned-owner lists partition the owners not already on
`mathscr Z`.  Replacing pairwise distinct cycle edges by internally
vertex-disjoint paths consequently produces one cycle through every member
of `mathcal B` exactly once.  The colour statement follows block by block.
\(\square\)

This insertion is completely deterministic after the arbitrary assignment;
no matching or Hall condition is needed.

## 3. Delete only redundant occurrences

The cycle `K` has `V` edges and covers `A` intersection colours.  Its exact
repeat surplus is

\[
 R=V-A
 ={3Wr\over(r+1)(r+2)}
 ={3r\over r+2}C.
\tag{3.1}
\]

For each `a`, retain one distinguished edge from its block (2.3) and call
the other `t_a` edges redundant.  There are exactly `R` redundant edges.
Since

\[
 {R\over C}={3r\over r+2}>1,
\tag{3.2}
\]

choose any `C` distinct redundant edges and delete them.

### Theorem 3.1 (exact Catalan q2 path forest)

The remaining graph `F_2` is a spanning linear forest on `mathcal B` with
exactly `C` path components.  Every rank-`(r-2)` set still occurs as an edge
intersection, and

\[
 |E(F_2)|=V-C.
\tag{3.3}
\]

Its exact intersection multiplicity excess is

\[
 \boxed{
 |E(F_2)|-A
 ={2W(r-1)\over(r+1)(r+2)}
 ={2\over r}A.}
\tag{3.4}

#### Proof

Deleting `C` edges from one cycle produces exactly `C` path components.
Every deleted edge was redundant for its intersection colour, so all
members of `mathcal A` remain represented.  Equations (3.3)--(3.4) follow
from the binomial identities

\[
 V={Wr\over r+1},
 \qquad
 A={Wr(r-1)\over(r+1)(r+2)}.
\tag{3.5}
\]

\(\square\)

The surplus (3.4) is exactly the `q=2` count in
`MATH_THEOREM_MSW_ALL_WIDTH_COMPLEMENT_TOWER_AND_Q2_BOTTLENECK_20260805.md`.
Thus the first derivative row has an unconditional spanning Catalan path
forest with the correct literal lower palette.

## 4. The remaining correlation is explicit

For an edge `XY` of `F_2`, the two Boolean colours are

\[
 \ell(XY)=X\cap Y\in{\Omega\choose r-2},
 \qquad
 u(XY)=X\cup Y\in{\Omega\choose r}.
\tag{4.1}
\]

The construction controls `ell` exactly but does not control `u`.
Different blocks may repeat the same rank-`r` union.  In the MSW complement
tower, those rank-`r` unions are the internal owner occurrences needed to
lift the ordered `L^(1)` row back to one owner-once rank-`r` chronology.

Accordingly the `q=2` obstruction has split into two statements.

1. **Marginal q2 service:** construct a Catalan path forest on the complete
   rank-`(r-1)` layer whose intersections cover rank `r-2` with the exact
   surplus.  This is Theorem 3.1 and is closed.
2. **Correlated lift:** choose such a forest so that the rank-`r` edge unions
   required as internal owners are occurrence-compatible and nonrepeating,
   while retaining the endpoint/puncture structure needed by the MSW
   chronology.  This remains open.

Thus the vanishing `2/r` scalar reserve is not itself an obstruction.  The
live gate is the simultaneous intersection/union/endpoint correlation.

No arbitrary-width tower above `q=2`, residence, lower trace compiler, or
`B(k)+O(1)` conclusion is proved here.

## 5. Reference

P. Gregor, O. Mička, and T. Mütze, *On the central levels problem*,
arXiv:1912.01566.  The result used here is their optimal-cycle theorem for
any sequence of consecutive levels of the hypercube:
<https://arxiv.org/abs/1912.01566>.
