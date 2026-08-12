# A positive-density outer-tail matching inside one BTK SCD

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
 n=2m,\qquad N_H=\binom{2m}{m-H},
 \qquad 1\le q_0<H<m.
\]

Let \(\mathcal D_{\rm BTK}\) be the standard de
Bruijn--Tengbergen--Kruyswijk symmetric-chain decomposition of \(B_{2m}\),
and let \(\mathcal T_{q_0,H}(\mathcal D_{\rm BTK})\) be the outer-tail
overlap graph from
`MATH_THEOREM_S_PARTIAL_ANNULUS_DIAGONAL_PORT_AND_TAIL_HALL_20260726.md`.

There is an explicit vertex-disjoint directed matching in this graph with

\[
 \boxed{
 M_H=\binom{2m-2}{m-H-1}}
 \tag{0.1}
\]

edges.  Every edge is not merely a tail-overlap edge: it is an actual
genuine radius-\(H\) rotor between the two clipped BTK chains.  Therefore

\[
 \boxed{
 \lambda_H^{\rm tail}(\mathcal D_{\rm BTK})
 \ge \binom{2m-2}{m-H-1}.}
 \tag{0.2}
\]

The exact density is

\[
 {M_H\over N_H}
 ={(m-H)(m+H)\over 2m(2m-1)}.                    \tag{0.3}
\]

In the Gaussian range \(H=b\sqrt m+O(1)\),

\[
 \boxed{
 M_H=\left({1\over4}+o(1)\right)N_H
     =\left({e^{-b^2}\over4}+o(1)\right)
       \binom{2m}{m}.}                            \tag{0.4}
\]

Thus tail uniqueness and layer counting cannot prove
\(\lambda_H^{\rm tail}=o(W)\) for every SCD.  A single standard SCD
already has a positive-density tail forest.  This does not prove the
partial-annulus path-cover theorem: the narrow-annulus run cut can demand
more than the density in (0.4), and the matching constructed here does not
organize the remaining providers or choose their annular ports.

## 1. BTK signatures and clipping

Use the usual BTK bracketing convention in which a fixed block \(01\) is
matched.  A chain signature consists of fixed matched zero--one positions
and an even number of free positions, denoted by stars.  If its free
positions are

\[
                         u_1<u_2<\cdots<u_{2r},
\]

then the chain has radius \(r\).  Write \(I\) for its fixed-in
coordinates and \(O\) for its fixed-out coordinates.  Its radius-\(H\)
clipping, for \(r\ge H\), is the full state

\[
 \omega_H=
 \left(
 I\cup\{u_1,\ldots,u_{r-H}\};\
 u_{r-H+1},\ldots,u_{r+H};\
 O\cup\{u_{r+H+1},\ldots,u_{2r}\}
 \right).                                       \tag{1.1}
\]

The three parts have sizes \(m-H,2H,m-H\), respectively.  Formula
(1.1) is simply the chain at the two ranks \(m-H,m+H\), with its ordered
free coordinates displayed between them.

Let \(S\) now be an arbitrary BTK chain signature on the first
\(2m-2\) coordinates.  Suppose that \(S\) has radius \(r\ge H\), with
free positions

\[
                         u_1<\cdots<u_{2r}.
\]

Put

\[
                         a=2m-1,\qquad b=2m.
\]

There are two associated BTK chains on \([2m]\):

\[
 C_*(S):\quad S**,
 \qquad
 C_{01}(S):\quad S01.                           \tag{1.2}
\]

The first has radius \(r+1\) and free word

\[
                         u_1,ldots,u_{2r},a,b.
\]

The second has radius \(r\); coordinate \(a\) is fixed out, coordinate
\(b\) is fixed in, and its free word is

\[
                         u_1,ldots,u_{2r}.
\]

Both signatures are valid.  In \(S01\), the final \(01\) is matched
internally.  In \(S**\), the final two positions are appended to the free
positions and are flipped in the ordinary BTK order.

## 2. The suffix-pair rotor

### Theorem 2.1 (exact clipped rotor edge)

For every prefix signature \(S\) of radius \(r\ge H\), the clipped state
of \(C_*(S)\) has a genuine radius-\(H\) rotor edge to the clipped state
of \(C_{01}(S)\).

#### Proof

Let \(I,O\) be the fixed-in and fixed-out sets of \(S\).  Put

\[
                         x=u_{r+1-H},\qquad y=b.                \tag{2.1}
\]

Since \(C_*(S)\) has radius \(r+1\), formula (1.1) gives its lower part

\[
 L_*=I\cup\{u_1,\ldots,u_{r+1-H}\}.             \tag{2.2}
\]

Apply the full rotor with departure \(x\) and entry \(y\).  Its new lower
part is

\[
 L_*-x+y
   =I\cup\{b\}\cup\{u_1,\ldots,u_{r-H}\}.       \tag{2.3}
\]

This is exactly the lower part of the radius-\(H\) clipping of
\(C_{01}(S)\), because \(b\) is fixed in there and that chain has radius
\(r\).

The source collar begins with \(u_{r+2-H}\).  A rotor prepends \(x\) and
deletes the last collar entry, so the new collar is

\[
 u_{r+1-H},u_{r+2-H},\ldots,u_{r+H},             \tag{2.4}
\]

which is precisely the clipped collar of \(C_{01}(S)\).  Finally, the
new upper remainder is

\[
 O\cup\{a\}\cup\{u_{r+H+1},\ldots,u_{2r}\},     \tag{2.5}
\]

again exactly the upper remainder of \(C_{01}(S)\).  Equations
(2.3)--(2.5) identify the complete successor state, proving the genuine
rotor claim.  The endpoint case \(r=H\) is included: the ranges which
become empty are simply omitted. \(\square\)

Every genuine top-to-top rotor satisfies all outer-tail shift equations.
Hence Theorem 2.1 gives an arc

\[
 C_*(S)\longrightarrow C_{01}(S)                \tag{2.6}
\]

in \(\mathcal T_{q_0,H}(\mathcal D_{\rm BTK})\), for every
\(q_0<H\).

## 3. Vertex disjointness and the exact count

### Theorem 3.1 (positive-density tail matching)

The arcs (2.6), as \(S\) ranges over all BTK chains of \(B_{2m-2}\) with
radius at least \(H\), form a vertex-disjoint directed matching.

#### Proof

Distinct prefix signatures give distinct full signatures in both columns
of (1.2), so no two arcs share a source and no two share a target.  A
source signature ends in \(**\), whereas every target signature ends in
the fixed matched block \(01\).  Hence no source equals any target.  The
arcs are therefore vertex disjoint. \(\square\)

An SCD of \(B_{2m-2}\) has one chain of radius at least \(H\) for every
set of rank

\[
                         (m-1)-H.
\]

Indeed, each such set lies on a unique symmetric chain, and a chain meets
that rank if and only if its radius is at least \(H\).  Therefore the
number of prefix signatures used in Theorem 3.1 is exactly

\[
                         M_H=\binom{2m-2}{m-H-1},               \tag{3.1}
\]

proving (0.1)--(0.2).

For the density, put \(k=m-H\).  The elementary binomial identity

\[
 {\binom{2m-2}{k-1}\over\binom{2m}{k}}
 ={k(2m-k)\over2m(2m-1)}                       \tag{3.2}
\]

gives

\[
 {M_H\over N_H}
 ={(m-H)(m+H)\over2m(2m-1)},                   \tag{3.3}
\]

which is (0.3).  If \(H=b\sqrt m+O(1)\), then (3.3) tends to \(1/4\),
and the local central-binomial estimate gives

\[
                         N_H=(e^{-b^2}+o(1))W.
\]

This proves (0.4).

## 4. Consequence for the narrow-annulus cut

The general annular-compatible run inequality is

\[
 p\ge
 \bigl(2N_H-N_{q_0}-\lambda_H^{\rm tail}\bigr)_+.
 \tag{4.1}
\]

The matching above proves that a universal argument based only on tail
uniqueness cannot replace \(\lambda_H^{\rm tail}\) by \(o(W)\).  For the
BTK SCD, it already obeys

\[
 \lambda_H^{\rm tail}
 \ge\left({e^{-b^2}\over4}+o(1)\right)W.          \tag{4.2}
\]

Numerically, this certified sector by itself meets the positive part of
the right side of (4.1) whenever

\[
 e^{-a^2}\ge {7\over4}e^{-b^2},
 \quad\text{equivalently}\quad
 b^2-a^2\ge\log(7/4),                             \tag{4.3}
\]

although it does not construct a path cover there.  When
\(b^2-a^2<\log(7/4)\), the run cut asks for more tail edges than this one
matching supplies.  No upper bound or matching extension is proved in
that range.

## 5. Exact scope

Proved:

1. one fixed BTK SCD has a genuine top-to-top rotor matching of the exact
   size (0.1);
2. this matching lies in every outer-tail graph with \(q_0<H\);
3. its density among tag-\(H\) providers tends to \(1/4\); and
4. consequently no universal sublinear tail-forest theorem can follow
   from SCD layer uniqueness or tail-word counting alone.

Not proved:

1. that the matching extends to cover most tag-\(H\) chains;
2. that its endpoints can be integrated with the lower-tag providers in
   \(o(W/H)\) paths;
3. the annular port-transversal Hall conditions outside this sector; or
4. any coefficient-one conclusion.

The surviving positive question is now quantitative rather than
existential: enlarge the explicit \(1/4\)-density BTK tail matching, or
construct a different noncanonical SCD whose outer-tail graph meets the
full lower bound in (4.1) while also satisfying the common all-depth port
constraints.
