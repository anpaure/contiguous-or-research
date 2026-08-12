# Odd current: root-slide parity and the three-site phase cut

**Date:** 2026-08-06  
**Method:** exact rooted parity algebra and a six-state local token-graph
decomposition; no computation or search  
**Status:** unconditional local theorem.  It proves that a corridor of
root-value one is shore-transparent under rerooting, and that every
single adjacent three-site phase transport must pass through the central
state `111`.  In a quiet-prefix placement where that `111` state is an
endpoint of the installed boundary current, the three-site transport is
therefore forbidden.  Without that placement hypothesis the installed
scan may stop earlier, so a four-site or genuinely cross-root transport is
a sufficient next target but is not proved necessary in every global host.

## 1. Exact parity change under an adjacent root slide

Let `n` and the total mass `R` be odd.  For a state

\[
                         t\in\{0,1,2\}^{\mathbb Z_n},
 \qquad                  \sum_i t_i=R,
\]

root the coordinate cycle at `j` and put

\[
                  \chi_j(t)=\sum_{p=0}^{n-1}p\,t_{j+p}pmod2.
\tag{1.1}
\]

The corresponding cut edge is the edge immediately preceding the root in
this cyclic order.

### Theorem 1.1 (root-slide identity)

\[
                   \boxed{\chi_{j+1}(t)-\chi_j(t)
                          \equiv R-t_j\equiv1-t_j\pmod2.}
\tag{1.2}
\]

In particular, an adjacent root slide across a coordinate of value one
preserves the two cut-open shores.

#### Proof

Reindex the first sum:

\[
 \chi_{j+1}(t)
  =(n-1)t_j+\sum_{q=1}^{n-1}(q-1)t_{j+q}.
\]

Subtracting

\[
 \chi_j(t)=\sum_{q=1}^{n-1}q\,t_{j+q}
\]

gives

\[
 (n-1)t_j-\sum_{q=1}^{n-1}t_{j+q}.
\]

The first term is even because `n` is odd, while the second is congruent
to `R-t_j`.  Since `R` is odd, this is `1-t_j` modulo two.  \(\square\)

### Corollary 1.2 (one-corridor rerooting)

If a sequence of adjacent root slides crosses only coordinates whose value
is one at the instant they are crossed, then the majority/minority shore is
unchanged throughout the sequence.

This is only a parity statement.  A physical proof must still transport
the scan matching and avoid the old and new boundary-current endpoints.

## 2. The smallest phase transporter is obstructed

Consider three consecutive coordinates on a path, with total local mass
three.  The capacity-two states consist of `111` and the six permutations
of `201`.  Remove `111`.

### Proposition 2.1 (three-site separator)

The remaining local token graph has exactly two components:

\[
                 201-210-120,
       \qquad    021-012-102.
\tag{2.1}
\]

Consequently the two mass-two phase endpoints

\[
                         20\mid1,
       \qquad             02\mid1
\tag{2.2}
\]

cannot be joined by adjacent unit transfers on these three coordinates
without using `111`.

#### Proof

Every legal move transfers one unit across one of the two path edges.
Direct inspection of the six noncentral states gives precisely the four
edges displayed in (2.1).  Each of `201,120,021,102` has one additional
neighbor, namely `111`; there are no other legal moves.  Deleting `111`
therefore leaves the two stated paths.  The endpoints (2.2) are `201` and
`021`, one in each component.  \(\square\)

### Corollary 2.2 (quiet-prefix three-site phase obstruction)

At the boundary mass-two row, the central state `111` is the state with
root coordinate one and boundary pair `11`.  If the scan prefix is quiet
up to this row, its boundary `11--02` or `20--11` edge belongs to the
installed/dual scan current.  Once that state is deleted or protected,
Proposition 2.1 forbids transporting the phase endpoint `20` to `02` using
only the boundary pair and the adjacent root.

Hence a boundary-locked dual-phase basis in this quiet-prefix placement
cannot be completed by a three-coordinate detour.  A sufficient positive
replacement uses at least one further coordinate, or moves the scan root
before changing the boundary phase.

The quiet-prefix qualification is load-bearing.  If an earlier scan pair
is nonquiet, the installed scan can stop before the boundary, and the
global `111` state need not lie in the protected current.  Proposition 2.1
still says that every three-site detour passes through `111`; it does not,
by itself, forbid using that state in such a host.

## 3. Exact remaining local target

The root-slide identity says what a successful cross-root construction
should preserve: carry a value-one root corridor so all adjacent rerootings
remain on the same shore.  In a quiet-prefix placement, the three-site
separator says what it must avoid: the protected `111` bottleneck.

A sufficient next lemma is therefore:

> **Four-site root transporter.**  On a four-or-more-coordinate corridor,
> construct a pairwise-disjoint alternating gadget which moves the dual
> mass-two phase from the physical boundary to an internal scan pair,
> changes the boundary state there, and returns the root, while every root
> slide crosses a coordinate of value one and no path uses a protected
> boundary-current endpoint.

No existence claim for this transporter is made here.
