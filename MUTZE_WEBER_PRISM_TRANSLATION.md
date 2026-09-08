# Translating the Mütze--Weber upper-layer recursion into the prism gate

## 1. Outcome

The fixed MSW outer path `O_0` is uniformly obstructed by
`MSW_SECOND_UPPER_OBSTRUCTION.md`.  The older Mütze--Weber recursion contains
the natural replacement: an exact family of dangling paths in every upper
layer of the even cube.

At the critical induction step `2m -> 2m+2`, their published recursion
splits the new central path system into exactly

\[
                         D_m+C_m+C_m=C_{m+1}         \tag{1.1}
\]

paths, where

\[
 C_m=\operatorname {Cat}_m,
 \qquad D_m=C_{m+1}-2C_m.
\]

It visits every vertex in both new middle levels exactly once.  Thus it
already solves the raw rank-rectangle packing and all upper-colour
collisions which remain open in the naive punctured-prism scaffold.

It does **not** directly solve the OR problem.  Its paths are dangling
paths of nonuniform lengths, and their endpoint pairing is not the
complement involution.  The precise positive theorem now suggested by the
literature is an `O(C_m)`-switch **equitable antipodal refinement** of this
published path system.

The primary source is Mütze and Weber,
[Construction of 2-factors in the middle layer of the discrete
cube](https://arxiv.org/abs/1111.2413), especially equations (5)--(8) and
conditions (i)--(ii) in Section 2.2.

## 2. Published dangling-path systems

Write

\[
 \mathscr P_{2m}(r,r+1)
\]

for the Mütze--Weber family of disjoint oriented dangling paths in the
layer `Q_(2m)(r,r+1)`.  A dangling path starts and ends in rank `r`.
Their recursive systems satisfy:

1. `mathscr P_(2m)(m,m+1)` visits every vertex of ranks `m,m+1`;
2. for `r>m`, `mathscr P_(2m)(r,r+1)` visits every rank-`r+1`
   vertex, and its only omitted rank-`r` vertices are the second vertices
   of the paths in `mathscr P_(2m)(r-1,r)`.

Put

\[
 \mathscr P_m=\mathscr P_{2m}(m,m+1),
 \qquad
 \mathscr U_m=\mathscr P_{2m}(m+1,m+2).             \tag{2.1}
\]

The central family has

\[
                         |\mathscr P_m|=C_m,         \tag{2.2}
\]

because the difference between the two middle ranks is `C_m`.

The upper family `mathscr U_m` covers every rank-`m+2` state and omits
exactly the `C_m` ports

\[
                         S(\mathscr P_m),            \tag{2.3}
\]

where `S(P)` denotes the second vertex of an oriented path.  Therefore

\[
\begin{aligned}
 |\mathscr U_m|
 &=\left(\binom{2m}{m+1}-C_m\right)
       -\binom{2m}{m+2}\\
 &=(m-1)C_m-{m(m-1)\over m+2}C_m\\
 &=D_m.                                             \tag{2.4}
\end{aligned}
\]

This is the first important translation: the interior Catalan count `D_m`
is exactly the number of dangling paths in the next upper layer.  It is not
merely a formal first-return convolution.

## 3. Exact three-sector induction

Mütze--Weber first make a 2-factor `mathscr C_(2m+1)` in the middle layer
on `2m+1` coordinates from two transformed copies of `mathscr P_m` and an
endpoint matching.  Delete from that 2-factor the distinguished first edge
of every path in one copy.  The result is a family of paths

\[
                         \mathscr C^-_{2m+1}.        \tag{3.1}
\]

After appending the second new bit and restoring a matching at the exposed
ports, their mixed family `mathscr P'_(2m+2)` has `C_m` paths and satisfies

\[
\begin{aligned}
 F(\mathscr P'_{2m+2})&=S(\mathscr P_m)\circ(0,0),\\
 S(\mathscr P'_{2m+2})&=S(\mathscr P_m)\circ(0,1),\\
 L(\mathscr P'_{2m+2})&=F(\mathscr P_m)\circ(0,1).
                                                               \tag{3.2}
\end{aligned}
\]

Here `F,S,L` are the first, second and last vertices and `circ` appends
bits.  Their central induction equation is

\[
\boxed{
\begin{aligned}
 \mathscr P_{2m+2}(m+1,m+2)={}&
   \mathscr U_m\circ(0,0)\\
 &\mathbin{\dot\cup}\ \mathscr P_m\circ(1,0)\\
 &\mathbin{\dot\cup}\ \mathscr P'_{2m+2}.
                                                               \tag{3.3}
\end{aligned}}
\]

The three path counts in (3.3) are respectively

\[
                              D_m,\quad C_m,\quad C_m.           \tag{3.4}
\]

By the published induction theorem, (3.3) is a disjoint dangling-path
system visiting **every** state of ranks `m+1,m+2` of the `(2m+2)`-cube.
In the union-colour formulation, this means every lower state and every
upper edge colour is owned exactly once.

The exposed-port formula (3.2) is also the structural analogue of the
canonical rank-transfer squares.  The upper-layer family deliberately
omits the ports `S(P_m)`; the mixed family begins at exactly those ports,
uses one new-coordinate matching edge, and routes through the cut old
2-factor.  Thus no surjectivity of the naive map
`x_i -> y_(i-1) union y_i` is required.

## 4. What is still missing for a wreath/OR lift

A complementary path on a `2m+2`-element core must have

\[
              m+2\text{ lower vertices},\qquad
              m+1\text{ upper vertices},            \tag{4.1}
\]

and its two lower endpoints must be set complements.  The system (3.3)
has the correct properties only on average:

\[
 {\binom{2m+2}{m+1}\over C_{m+1}}=m+2.             \tag{4.2}

\]

Individual dangling paths may have different lengths, and (3.2) does not
pair each first endpoint with its complement.  These are not two independent
obstructions.

### Lemma 4.1 (antipodality forces equitability)

Let `C_(m+1)` vertex-disjoint paths partition the rank-`m+1` vertices of
the `(2m+2)`-cube.  If every path has complementary lower endpoints, then
every path contains exactly `m+2` lower vertices.

### Proof

In `J(2m+2,m+1)`, a set and its complement are at distance `m+1`.
Every path between them therefore has at least `m+1` Johnson edges, or at
least `m+2` lower vertices.  The total lower mass is

\[
             {2m+2\choose m+1}=(m+2)C_{m+1}.       \tag{4.3}
\]

There are `C_(m+1)` paths, so their average lower-vertex count is exactly
`m+2`.  Every count is at least this average, hence every count equals it.
\(\square\)

Thus endpoint antipodality alone forces geodesicity and the exact wreath
length; no separate length-balancing theorem is needed.

The initial endpoint set is not complement-stable.  The three terms of
(3.3), together with (3.2), have endpoint counts by new-bit sector

\[
\begin{array}{c|cccc}
\text{sector}&00&10&01&11\\ \hline
\text{number of endpoints}&2D_m+C_m&2C_m&C_m&0.
\end{array}                                           \tag{4.4}
\]

An antipodal endpoint set must have equal counts in sectors `00,11` and in
sectors `10,01`.  Therefore a refinement that merely permutes the existing
terminal endpoints cannot work.  It must move endpoint status through
alternating trails, turning some currently internal lower vertices into
endpoints and vice versa.  The discrepancy is `Theta(C_m)`, so this is
consistent with, but also shows the necessity of, an `O(C_m)` switch budget.

The exact refinement target is therefore:

> **Antipodal Mütze--Weber refinement.**  Starting from (3.3),
> perform `O(C_m)` local path switches, preserving every middle vertex,
> so that every endpoint is joined to its set complement.

Lemma 4.1 then gives the size in (4.1) automatically.

Because upper states are explicit vertices of the bipartite layer graph,
a legal switch reroutes through the same upper vertices and automatically
preserves the union-colour bijection.  What must be controlled is only the
endpoint boundary and its pairing.  In particular, a fixed-endpoint tail
permutation is insufficient by (4.4).

## 5. The provenance requirement

For asymptotic OR optimality, support refinement alone is insufficient.
The switch family must also have bounded total seam complexity.

Equation (3.3) contains one literal tagged copy of the old central paths.
The mixed term is built by cutting a 2-factor made from two old path copies
at exactly one distinguished edge per old path.  Consequently the raw
recursion has only `O(C_m)` exposed ports at its top level.  This is the
right scale for halo compression, but a proof must still trace the old
central-band windows through the transformation used in the second copy.

A sufficient strengthened refinement theorem is:

1. the antipodalizing switches make `O(C_m)` cuts in total;
2. away from those cuts, every old shadow window is transported into at
   most two fixed new-coordinate sections; and
3. every exceptional window meets an `O(H)` halo of one recorded cut.

Then two tagged copies of the old repair word plus the seam halos give

\[
 R_{m+1,H}\le2R_{m,H}+O(HC_m),                     \tag{5.1}
\]

and the contractive repair theorem yields asymptotic optimality.

## 6. Precise fork in the road

The canonical fixed-outer map is now ruled out for all `m>=4`.  The
Mütze--Weber recursion proves that there is no *support-counting* obstruction
to Catalan completion: the exact `D_m+C_m+C_m` completion already exists.

What remains is one sharply stated refinement question:

\[
 \text{dangling Catalan path system}
 \quad\Longrightarrow\quad
 \text{antipodal path system with }O(C_m)\text{ switches}.
\]

Lemma 4.1 supplies equitability automatically.  Proving antipodalization,
together with the two-copy provenance audit, gives the desired contractive
lift.  Refuting it requires an endpoint-matching invariant which survives
all colour-preserving local switches.
