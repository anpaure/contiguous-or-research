# Adjacent necklaces: the short all-quiet core reduces to unit-gap barriers

**Date:** 2026-08-05  
**Method:** a macroblock phase cube, odd-group quotient matching, and a
strict smaller-slot self-duality; no computation  
**Status:** unconditional reduction.  It matches every periodic short-run
fibre having an even-mass movable macroblock and isolates the exact mixed
barrier problem.  The latter is subsequently closed by
`MATH_THEOREM_ADJACENT_NECKLACE_EVEN_BARRIER_C4_ABSORBER_20260805.md`;
the only recursive short-core residue is then the all-unit face (0.6).

## 0. Outcome

Fix an odd cyclic coordinate length `q`.  Suppose every positive run of a
composition necklace is one of

\[
                 [a]\quad(a\geq1),
        \qquad   [2z+1,1]\quad(z\geq0),             \tag{0.1}
\]

and every two consecutive positive runs are separated by a nonempty zero
run.  This is precisely the short-run residue left by the all-quiet
phase-fibre and long-run reductions.

There is a canonical macroblock decomposition.  A macroblock begins at the
first coordinate of a positive run and ends immediately before the next
positive run.  Record its coordinate length `L>=2` and its chip mass `m`.

For every even `m` and `L>=3`, there are exactly two short all-quiet
realisations of the same macroblock data:

\[
 \begin{aligned}
 E(m,L)&=(m,0^{L-1}),\\
 D(m,L)&=(m-1,1,0^{L-2}).
 \end{aligned}                                      \tag{0.2}
\]

They are joined by one adjacent chip transfer.  After fixing the cyclic
`(m,L)` data, all such choices form an odd-group quotient of a hypercube.
Thus every fibre containing at least one movable macroblock has a perfect
matching, including every periodic fibre.

The unmatched singleton fibres have the exact form

\[
 [m_1,0^{L_1-1},m_2,0^{L_2-1},\ldots,m_p,0^{L_p-1}],
 \qquad
 \sum_iL_i=q,                                      \tag{0.3}
\]

with

\[
                       m_i\text{ odd}\quad\hbox{or}\quad L_i=2
                       \qquad(1\leq i\leq p).       \tag{0.4}
\]

In particular, at least one `m_i` is odd.  If some block has
`m_i>=3` odd and `L_i>=3`, it has an injective uniquely marked one-edge
exit.  The genuinely unresolved mixed family therefore satisfies

\[
 L_i>2\Longrightarrow m_i=1;\qquad
 m_i\ne1\Longrightarrow L_i=2.                     \tag{0.5}
\]

When every `m_i=1`, this remaining induced graph is exactly

\[
                         G_{p,q-2p}\cong G_{q-2p,p},\tag{0.6}
\]

and `q-2p` is a positive odd integer strictly smaller than `q`.  Hence the
all-unit face closes by strong induction from any protected near-perfect
theorem already known in smaller odd coordinate length.

The sole new difficulty is the mixed version of (0.5): nonunit blocks of
length two act as barriers between strings of unit blocks.  Section 6 gives
an exact local matching reduction and identifies the parity socket that a
future barrier-absorption lemma must handle.

## 1. Exact macroblock phases

Every short all-quiet positive run followed by its zero gap has one of the
forms

\[
 (a,0^g),\qquad (2z+1,1,0^g),\qquad g\geq1.         \tag{1.1}
\]

The first has macro data `(m,L)=(a,g+1)`.  The second has

\[
                 (m,L)=(2z+2,g+2),                 \tag{1.2}
\]

so its mass is even and its length is at least three.  Conversely, for
even `m>=2` and `L>=3`, the two words in (0.2) are both valid and exhaust
the possibilities in (1.1) with those data.

Moving the second coordinate of `D` into its predecessor gives

\[
                 D(m,L)\longleftrightarrow E(m,L). \tag{1.3}
\]

The reverse move is legal because `m>=2`.  It preserves the macroblock
start, the next macroblock start, the block mass, and the block length.

## 2. Periodic fibres are hypercube quotients

Fix a cyclic macroblock word

\[
                 ((m_1,L_1),\ldots,(m_p,L_p))       \tag{2.1}
\]

and let `I` be the set of indices with `m_i` even and `L_i>=3`.  Put
`t=|I|`.  At an index outside `I` there is only the singleton phase `E`.
At an index in `I` choose independently `E` or `D`.

Let `H` be the stabilizer of (2.1) under coordinate rotation.  It permutes
the `t` movable indices.  Since `H<=C_q` and `q` is odd, `|H|` is odd.
Two phase words define the same composition necklace exactly when they are
in the same `H`-orbit.  Therefore the fixed-data fibre is

\[
                            Q_t/H.                  \tag{2.2}
\]

By the odd-group hypercube quotient theorem, (2.2) has a perfect matching
whenever `t>=1`.  Every quotient edge is the literal legal transfer (1.3).
This proves the matching without choosing a root and therefore includes
all periodic macroblock skeletons.

## 3. Exact residual normal form

A fibre with `t=0` contains no index with even `m_i` and `L_i>=3`.
Consequently every positive run is a singleton and (0.4) holds.
Conversely, (0.3)--(0.4) has no movable macroblock and is a singleton
fibre.  This proves the asserted equivalence.

If every `m_i` were even, (0.4) would force every `L_i=2`, and then

\[
                             q=2p
\]

would be even.  Hence an odd coordinate length forces at least one
odd-mass block.

## 4. A marked exit from a long odd-mass singleton

Suppose (0.3) has a block with odd `m>=3` and `L>=3`.  Choose one such
block necklace-invariantly: take the first eligible block in a
lexicographically least cyclic representative.  If the least
representative occurs more than once, the choices are related by the
stabilizer and give the same receiver necklace.

Make the transfer

\[
 (m,0^{L-1})\longmapsto(m-1,1,0^{L-2}).             \tag{4.1}
\]

Because `m-1>=2` and `L-2>=1`, the receiver has exactly one positive run
of length two whose first entry is positive even and whose second entry is
one.  Every unchanged source run is a singleton.  Thus the changed block
is uniquely recognizable.  Replacing

\[
                         (m-1,1)\longmapsto(m,0)    \tag{4.2}
\]

recovers the source.  Hence (4.1) is injective on necklace classes.

Its receiver is in a nonquiet pair fibre.  This is an exact receiver bank,
not by itself a global matching: if those active-fibre vertices were
already used, they must be deleted and their matching deficiency routed.

After removing the source domain of (4.1), (0.5) is forced.

## 5. The all-unit face is a strictly smaller odd-slot necklace graph

Assume every `m_i=1`.  Put

\[
                         e_i=L_i-2\geq0,
 \qquad E=\sum_ie_i=q-2p.                           \tag{5.1}
\]

Because `q` is odd, `E` is positive and odd.  A rotation of the coordinate
necklace must send a positive coordinate to a positive coordinate, so it
induces, and is induced by, a cyclic rotation of `(e_1,...,e_p)`.

Sliding the `i`-th singleton one coordinate to the right, while keeping it
isolated, changes

\[
                (e_{i-1},e_i)\longmapsto
                (e_{i-1}+1,e_i-1),                 \tag{5.2}
\]

and is legal exactly when `e_i>0`.  These are precisely the adjacent unit
transfers in a weak composition of `E` into `p` cyclic parts.  Therefore
the induced graph is `G_(p,E)`.  Complement duality gives (0.6).

Finally,

\[
                       1\leq E=q-2p<q,              \tag{5.3}
\]

and `E` is odd.  Thus a strong induction on odd coordinate length applies
to the all-unit face.  Any protected socket in the smaller graph transports
back through (5.1)--(5.2); an arbitrary final monomer is also sufficient
when the adaptive radial-monomer lift is used.

## 6. Exact mixed-barrier reduction

Assume (0.5) and that at least one nonunit mass occurs.  The nonunit blocks
all have length two.  They divide the unit blocks into linear segments.
Write

\[
                         e_i=L_i-2                  \tag{6.1}
\]

on unit blocks; on barriers `e_i=0`.  The total

\[
                         \sum e_i=q-2p              \tag{6.2}
\]

is odd.

In a unit segment of even length pair its coordinates

\[
                    (1,2),(3,4),\ldots;             \tag{6.3}
\]

in a unit segment of odd length leave the first coordinate unpaired and
pair

\[
                    (2,3),(4,5),\ldots.             \tag{6.4}
\]

For one displayed pair `(u,v)`, fix `u+v` and use the two-state allocation
keys

\[
             (2z,n-2z)\longleftrightarrow
             (2z+1,n-2z-1),                        \tag{6.5}
\]

leaving the quiet singleton `(n,0)` when `n` is even.  Equation (5.2)
shows that every toggle is a literal adjacent chip transfer between two
unit blocks.

The stabilizer of the cyclic decorated barrier word has odd order and
permutes the displayed pairs.  Consequently, after fixing all pair sums
and keys, every fibre with a nonsingleton key is again `Q_t/H` and is
perfectly matched.

In a singleton key fibre, every paired contribution in (6.3)--(6.4) is
even.  Every even-length segment therefore has even extra mass.  Since the
total (6.2) is odd, some odd-length segment has an odd value in its
unpaired first coordinate.  In particular, that value is positive.

Sliding the first unit of such a segment one step right transfers one unit
of length from that unit block to the preceding nonunit barrier.  It creates
the unique macro pattern

\[
      (m,0,\,1,0^{1+e},\ldots)
        \longmapsto
      (m,0,0,\,1,0^e,\ldots),                       \tag{6.6}
\]

where the nonunit barrier has grown from length two to length three.
Choosing the first eligible odd segment in a least cyclic representative
makes (6.6) necklace-invariant.  The unique long nonunit block recovers
the source, so (6.6) is injective.

If the barrier mass `m` is odd and at least three, its receiver lies in the
marked-exit source class of Section 4 and the two stages may be ordered so
that (6.6) consumes it first.  If `m` is even, however, the length-three
barrier is one endpoint of the two-state macro phase (0.2).  Consuming it
leaves the opposite `D(m,3)` endpoint as one unmatched socket in that
two-vertex fibre.

This is the exact mixed-barrier obstruction left by the reductions in this
file.  It cannot be discarded by a cell-count argument: the three vertices
consisting of the singleton-key source and the two macro phases contain the
path

\[
             \text{source} - E(m,3) - D(m,3),       \tag{6.7}
\]

whose maximum matching leaves one endpoint.  The cited even-barrier C4
theorem closes it by adding one uniquely associated long-run state and
taking the two opposite edges of the resulting square.  Thus no barrier
socket survives after the two theorems are combined.

## 7. Scope

Proved:

1. a literal macroblock phase cube for every short all-quiet necklace;
2. perfect matching of every nontrivial macro phase fibre, including all
   periodic skeletons;
3. the exact residual normal form (0.3)--(0.5);
4. an injective uniquely marked exit from every long odd-mass singleton;
5. strict smaller-odd-slot recursion for the complete all-unit face; and
6. a second periodic phase reduction of the mixed unit-gap segments.

Not proved:

1. bounded consolidation of the sockets `D(m,3)` produced at even
   barriers;
2. deletion-stable composition with all earlier receiver banks;
3. the complete protected boundary-shell matching theorem;
4. PBBS owner/q2-halo compatibility; or
5. any universal-word upper bound.
