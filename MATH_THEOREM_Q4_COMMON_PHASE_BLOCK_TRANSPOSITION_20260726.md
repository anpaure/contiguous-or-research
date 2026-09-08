# A common-phase `Q_4` braid which transposes two packet colours

Date: 2026-07-26

Method: an explicit sixteen-owner calculation, followed by the standard
coloured-cycle suspension.  No search or computation is used.

## 0. Outcome

The first finite ingredient toward the ported adjacent-block transposition
gate from
`MATH_THEOREM_RECTANGLE_TERNARY_CARRY_ZERO_BLOCK_HOLONOMY_20260726.md`
has a literal solution.  The full ported gate, which also requires matching
phase-resolved collars, remains open.

There are two exact factors of the four-cube into two physical `C_8`'s
with all three of the following properties.

1. They have the same owner support, namely every vertex of `Q_4` once.
2. They admit one common colouring by `Z_8`, cyclic on every cycle on
   both shores.
3. If directions `1,2` have packet colour `A` and directions `3,4` have
   packet colour `B`, then at four common phases the packet-colour word
   changes from `A,A,B,B,A,A,B,B` to
   `A,B,B,A,A,B,B,A`.

Thus the second factor exchanges an `A`-edge and a `B`-edge at fixed
common phases.  It is not an `H`-compatible one-packet rectangle switch:
it has nontrivial block-order projection.  Appending any number of split
directions gives the same statement for physical `C_(2h)` factors.

This proves a common-support, common-phase physical braid with nonconstant
packet-phase projection.  It does **not** yet prove the previously open
ported block-transposition primitive: common phase is weaker than equality
of every phase-resolved depth-`H` collar.  The remaining issues are to close
that collar discrepancy and then pack/schedule the braids so that the
induced packet-order atlas covers the Gaussian band.

## 1. The two factors

Write the vertices of `Q_4` as bit strings in `F_2^4`.  Define two rows
of vertices, indexed by `j in Z_8`, by

\[
\begin{array}{c|cccccccc}
j&0&1&2&3&4&5&6&7\\ \hline
a_j&0000&1000&1100&1110&1111&0111&0011&0001\\
b_j&0101&1101&1001&1011&1010&0010&0110&0100.
\end{array}                                                   \tag{1.1}
\]

The sixteen displayed strings are distinct, hence exhaust `Q_4`.
The first factor is

\[
 \mathcal F^0=
 (a_0,a_1,a_2,a_3,a_4,a_5,a_6,a_7)
 \mathbin{\dot\cup}
 (b_0,b_1,b_2,b_3,b_4,b_5,b_6,b_7).                 \tag{1.2}
\]

Both cycles in (1.2) have direction word

\[
                         1,2,3,4,1,2,3,4.             \tag{1.3}
\]

The second factor is

\[
\begin{aligned}
 \mathcal F^1={}&
 (a_0,a_1,b_2,b_3,a_4,a_5,b_6,b_7)\\
 &\mathbin{\dot\cup}
 (b_0,b_1,a_2,a_3,b_4,b_5,a_6,a_7).                  \tag{1.4}
\end{aligned}
\]

Both cycles in (1.4) have direction word

\[
                         1,4,3,2,1,4,3,2.             \tag{1.5}
\]

### Theorem 1.1 (literal common-support braid)

Equations (1.2) and (1.4) are two exact `C_8`-factors of `Q_4`.

#### Proof

The rows in (1.1) partition the vertex set.  Consecutive entries in each
cycle of (1.2) differ in the coordinates listed in (1.3), including the
cyclic seam.  Hence (1.2) is an exact factor.

For (1.4), the only changed joins are

\[
 a_1\leftrightarrow b_2,qquad
 b_1\leftrightarrow a_2,qquad
 b_3\leftrightarrow a_4,qquad
 a_3\leftrightarrow b_4,qquad
 a_5\leftrightarrow b_6,qquad
 b_5\leftrightarrow a_6,qquad
 b_7\leftrightarrow a_0,qquad
 a_7\leftrightarrow b_0.                              \tag{1.6}
\]

The first, second, fifth and sixth pairs in (1.6) differ in coordinate
`4`, and the other four differ in coordinate `2`.  Every remaining edge
is inherited from (1.2).
This gives (1.5).  The two rows of (1.4) still use every vertex in (1.1)
exactly once, proving exactness.  \(\square\)

## 2. One common phase colouring

Put

\[
                         c(a_j)=c(b_j)=j\pmod8.        \tag{2.1}
\]

### Theorem 2.1 (phase compatibility)

The colouring (2.1) is cyclic on every cycle of both factors: every
successor increases `c` by one modulo eight.

#### Proof

Every row in (1.2) and (1.4) lists one vertex from each successive column
of (1.1).  The last vertex has colour seven and its cyclic successor has
colour zero.  \(\square\)

Consequently the exchange (1.2)--(1.4) has no phase collar: both shores
have exactly the same eight phase classes and exactly the same cyclic
phase advance.

## 3. Nontrivial packet-order projection

Give directions `1,2` colour `A` and directions `3,4` colour `B`.
By (1.3), the outgoing packet-colour word of `F^0` is

\[
                         A,A,B,B,A,A,B,B.              \tag{3.1}
\]

By (1.5), the word of `F^1` is

\[
                         A,B,B,A,A,B,B,A.              \tag{3.2}
\]

Thus the matches between phase classes `1 -> 2` and `3 -> 4` exchange
their packet colours, and the antipodal matches `5 -> 6` and `7 -> 0`
make the identical exchange.  All other common-phase matches agree in
packet colour.  In particular the block-order projection is nonconstant
on the two shores.

### Corollary 3.1 (nonconstant packet-phase projection)

On the common support `Q_2^A square Q_2^B`, the two factors (1.2) and
(1.4) are exact phase-compatible cycle factors whose packet words differ
by a balanced transposition of one `A` occurrence and one `B` occurrence.
They therefore supply the owner-successor part, but not yet the full collar
part, of the finite primitive requested in Section 7 of the
zero-block-holonomy theorem.

The balance is forced: every coordinate occurs twice in each physical
cycle.  What is new is that the two occurrences need not occupy the same
packet phases on the two shores.

Both factors are isometric.  Their direction words are respectively
`1234 1234` and `1432 1432`, so every cyclic block of at most four edges
uses distinct directions.  This antipodal repetition is why the last four
exchanges in (1.6) are necessary.  Exchanging only in the first half would
still give an exact simple cycle factor, but it would repeat direction `2`
inside a four-edge window and would not be suitable for physical strips.

The phrase “supply the finite primitive” in the preceding paragraph refers
only to owner support, physicality, and packet-phase projection.  It does
not include the full collar clause of that open lemma.  Direct shadow audit
shows that the two shores have only eight common depth-one targets out of
sixteen; their depth-two and depth-three aggregate multisets agree, but not
phase by phase.  Thus a collar closure or compensating commutator is still
necessary.

## 4. Suspension

The required coloured-cycle suspension can be written explicitly.  Let

\[
 Z=(z_0,z_1,\ldots,z_{2d-1})                         \tag{4.1}
\]

be an oriented isometric cycle with colour `c(z_j)=j mod 2d` and direction
word `sigma sigma`, where `sigma` lists its `d` directions once.  Adjoin
`s=h-d` split directions `e_1,...,e_s`.  Starting at `z_0@0`, use the
direction word

\[
             \sigma,e_1,\ldots,e_s,
             \sigma,e_1,\ldots,e_s.                  \tag{4.2}
\]

Equivalently, run the first half of `Z` at tail orientation `0`, traverse
the prefix chain from `0` to `1` above `z_d`, run the second half of `Z`
at orientation `1`, and traverse the complementary return chain above
`z_0`.

Every direction in (4.2) occurs once in each half, so the result is an
isometric `C_(2h)`.  More importantly, the set of tail orientations used
above a base vertex depends only on its colour: colours `1,...,d-1` occur
at `0`, colours `d+1,...,2d-1` at `1`, colour `d` on the forward prefix
chain, and colour `0` on the complementary return chain.  Therefore two
base factors with one common cyclic colouring lift to exactly the same
enlarged owner support.  Vertex-disjoint base cycles remain disjoint after
the lift.

Apply this with `d=4` to (1.2) and (1.4).  For every `h>=4` one obtains
two exact physical `C_(2h)`-factors on one common suspended owner support.
Their owner supports and phase classes agree, while the local block-order
words retain the exchange (3.1)--(3.2).  Their full shadow collars need not
agree.

### Theorem 4.1 (all-length common-phase braid)

For every `h>=4`, the finite `Q_4` exchange has a common-support,
common-phase physical `C_(2h)` suspension.  Hence neither exact middle
ownership, long-cycle bundling, nor phase compatibility forces zero
block holonomy.

#### Proof

Both base direction words, `1234 1234` and `1432 1432`, have the required
form `sigma sigma`, and Theorem 2.1 supplies the common cyclic colouring.
Apply (4.1)--(4.2) cycle by cycle.  The colour-fibre description proves
that the two lifted unions agree owner by owner.  \(\square\)

This proof is an owner-support statement.  It does not identify the
phase-resolved depth-`H` shadows on the two shores.  In particular it must
not be cited as a common-collar theorem.

## 5. Replication inside the Hamming-syndrome factor

The finite braid is not confined to one exceptional four-cube.  It occurs
in a positive-dimensional family of pairwise disjoint interaction
components inside every sufficiently large standard Hamming factor.

Let `h=2^t>=8`, order the directions as `1,...,h`, and choose an enumeration

\[
                         g_0,g_1,\ldots,g_{h-1}       \tag{5.1}
\]

of `F_2^t` with

\[
 g_0=0,\qquad g_1=a,\qquad g_2=b,\qquad g_3=c,
 \qquad g_4=a+b+c,                                   \tag{5.2}
\]

where `a,b,c` are independent.  Fill the remaining positions by the
unused vectors in any order.  Use the standard syndrome map

\[
 \phi(e_j)=(g_j+g_{j-1},0)\quad(1\le j<h),
 \qquad \phi(e_h)=(g_{h-1},1),                        \tag{5.3}
\]

and put `K=ker phi`.  Its translates of the standard cycle with word
`1,...,h,1,...,h` form the usual exact `C_(2h)`-factor of `Q_h`.

Equation (5.2) gives

\[
 \phi(e_2)=a+b=phi(e_4),qquad
                         v:=e_2+e_4\in K.             \tag{5.4}
\]

Translation by `v` pairs the cycles of the factor.  It has no fixed cycle:
if the standard cycle met its `v`-translate, then `v` would be the parity
vector of a cyclic interval in the word `1,...,h,1,...,h`.  Its Hamming
weight is two, so that interval would have length two, but directions `2`
and `4` are not adjacent.

For a paired pair `C+k,C+k+v`, exchange the two rows at phases

\[
                         2,3,h+2,h+3.                 \tag{5.5}
\]

The calculation in Section 1 applies with every other direction frozen.
The two new cycles have word

\[
             1,4,3,2,5,\ldots,h,
             1,4,3,2,5,\ldots,h.                     \tag{5.6}
\]

They use exactly the same combined owner set as the old pair.  Distinct
`v`-pairs of cycles are disjoint, so these exchanges may be made
independently.

### Theorem 5.1 (independent braid components)

The standard syndrome factor of `Q_h` has

\[
                         {|K|\over2}={2^h\over4h}      \tag{5.7}
\]

pairwise owner-disjoint `Q_4` braid components.  Switching an arbitrary
subfamily gives another exact isometric `C_(2h)`-factor.  Hence one cell
has at least

\[
                         2^{,2^h/(4h)}               \tag{5.8}
\]

literal factor states in which each paired component independently uses
direction order `1234 5...h` or `1432 5...h`.

All these states share the same global phase colouring: if
`x=p_j+k` in the original syndrome factor, give it colour `j mod 2h`.
The switch (5.5) only exchanges the two vertices of one phase class, so
every new successor still advances the colour by one.

#### Proof

The syndrome construction gives `|K|=2^h/(2h)` disjoint translated cycles.
Equations (5.4) and the no-fixed-cycle observation partition them into
`|K|/2` pairs.  On one pair, (5.5) is the embedded version of (1.4) with
the antipodal exchange repeated in the second half.  Thus every new row
has (5.6), is isometric, and uses the same vertices as the old two rows.
Owner-disjoint pairs commute.  The phase assertion follows directly from
the phase indices in (5.5).  \(\square\)

By relabelling the directions, the same statement holds for any four
directions grouped into two two-direction packets.  Thus the generator is
available at every edge of a packet-order sorting network, not merely at
the first four positions.

## 6. Exact remaining gate

The earlier tensor-rectangle carry failed because every permitted switch
kept the packet colour at each phase fixed.  Theorem 4.1 removes exactly
that semiconjugacy obstruction at the owner-successor level, but leaves its
collar-qualified version unresolved.

It remains to do two genuinely global things.

1. Close the phase-resolved shadow collar of the finite braid, or combine
   copies into a collar-null commutator.
2. Pack many overlapping copies of this braid while retaining one-copy
   middle ownership (disjoint braid layers tensor immediately; overlapping
   adjacent transpositions require a braid-network completion).
3. Choose the resulting packet-order states so that, simultaneously for
   all `q<=H`, the literal lower and upper shadow images miss only `o(W)`
   targets.

The present theorem is therefore a generator-and-replication theorem, not
yet the constant-one theorem.  Its significance is that the first generator
previously absent from every rectangle-carry library exists on the minimal
two-packet product `Q_4` and already has exponentially many independent
copies in a full Hamming cell.
