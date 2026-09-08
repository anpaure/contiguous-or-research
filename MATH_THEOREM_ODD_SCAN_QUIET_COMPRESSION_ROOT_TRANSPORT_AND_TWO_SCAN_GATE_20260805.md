# Odd scan matching: exact quiet compression and the two-scan blossom gate

**Date:** 2026-08-05  
**Method:** first-nonquiet scans, alternating-path components, and support
parity of the circulation blossom; no computation  
**Status:** unconditional structural reduction and no-go theorem.  The
macroscopic odd defect is exactly a smaller bounded-composition layer and
adjacent root scans transport all its monomers bijectively.  Iterating at
central mass gives a dyadic chain ending in one socket.  Transport alone
cannot reduce the monomer count.  More sharply, in the canonical
all-one circulation blossom a coordinate scan contains at most one edge
of the blossom's forced perfect matching.  Thus neither one nor two scans
can be the missing common base; a genuinely global blossom-factor or
protected-minor theorem is required.

## 1. The scan residue is a smaller capacity-two layer

On an ordered coordinate pair use

\[
 01-10,\qquad02-11,\qquad12-21,
\tag{1.1}
\]

with quiet local states

\[
                              00,20,22.
\tag{1.2}
\]

Encode these three states by `0,1,2`, respectively.

### Theorem 1.1 (even quiet compression)

Pair all coordinates of `T_(2m,R)` and use the first-nonquiet scan.  If
`R` is odd, the scan is a perfect matching.  If `R` is even, its unmatched
set is canonically

\[
                         \mathcal T_{m,R/2}.
\tag{1.3}
\]

The bijection replaces each quiet pair by its code in (1.2).

#### Proof

The scan misses exactly the states for which every coordinate pair is
quiet.  Every quiet pair has mass twice its code, proving (1.3).  If `R`
is odd there is no such state. \(\square\)

### Theorem 1.2 (odd quiet compression)

On `T_(2m+1,R)`, leave coordinate `r` unpaired and scan the other `m`
pairs in cyclic order.  If `R` is odd, the unmatched set is exactly

\[
 Q_r={t:t_r=1,\text{ every other pair is quiet}\}
       \cong \mathcal T_{m,(R-1)/2}.
\tag{1.4}

Its cardinality is

\[
 |Q_r|=[u^{(R-1)/2}](1+u+u^2)^m
       =\Delta_{m,R}.
\tag{1.5}

#### Proof

An unmatched state has all paired mass even.  Since `R` is odd, the
unpaired digit must be the only odd digit in `{0,1,2}`, namely one.
Encoding the quiet pairs gives (1.4), and counting gives (1.5).
\(\square\)

At central mass these two theorems recurse without changing form:

\[
       \mathcal T_{n,n}longmapsto
       \mathcal T_{\lfloor n/2\rfloor,\lfloor n/2\rfloor}.
\tag{1.6}

Repeated quiet compression therefore terminates at `T_(1,1)`, a single
formal monomer.  This is an exact set decomposition, not yet a matching
of the residues.

## 2. Adjacent scan roots transport every monomer bijectively

Let `n=2m+1`.  For each root `r`, let `M_r` be the scan matching which
leaves `r` unpaired and pairs the remaining coordinates consecutively.
Orient every coordinate pair away from `r` and use (1.1).

### Theorem 2.1 (lossless adjacent-root transport)

For every `r`, every path component of

\[
                              M_r\cup M_{r+1}
\tag{2.1}

having endpoints joins one vertex of `Q_r` to one vertex of `Q_(r+1)`.
Consequently the alternating components define a canonical bijection

\[
                              \phi_r:Q_r\to Q_{r+1}.
\tag{2.2}

Flipping any collection of these components transports exactly the
chosen monomers from root `r` to root `r+1` and creates no additional
monomer.

#### Proof

The coordinate pairs used by the two scans together avoid only the cycle
boundary `r(r+1)`.  Hence every edge in (2.1) lies in the token graph of
the resulting coordinate path, which is bipartite by distance parity
from `r`.

Both endpoint coordinates `r` and `r+1` lie on the same shore of this
path, because their distance through the retained path is `2m`.  Every
quiet pair contributes even parity weight.  Thus every vertex of
`Q_r union Q_(r+1)` lies on that same shore.

The two quiet sets are disjoint.  Indeed `t_r=1` on `Q_r`, whereas in
the `r+1` scan the coordinate `r` is the second member of a quiet pair,
whose second digit is zero or two.

The union of two matchings is a collection of alternating cycles and
paths.  Every path endpoint lies in `Q_r union Q_(r+1)`.  Since both
endpoints lie on one bipartition shore, the path has even length.  An
even alternating path begins with the matching which misses one endpoint
and ends with the other matching; hence its endpoints belong to different
quiet sets.  Equal cardinalities then give the bijection.  Symmetric
difference along disjoint components proves the final statement.
\(\square\)

This supplies a literal one-in/one-out monomer conveyor around the odd
cycle.  It cannot by itself pay (1.5): every operation preserves the
number of monomers.

## 3. Why one circulation blossom is not a bounded-scan object

Use the notation of the odd circulation blossom.  Its odd cycle is

\[
 v_0v_1\cdots v_{n-1}v_0,
\]

and its tail is `v_(n-1)y`.  Since `y` has degree one inside the gadget,
the gadget has the unique perfect matching

\[
 \{v_{n-1}y\}
 \cup
 \{v_0v_1,v_2v_3,\ldots,v_{n-3}v_{n-2}\}.
\tag{3.1}

### Theorem 3.1 (linear scan-cover obstruction)

For the single-cut state over the all-one merged base, any
coordinate-pair scan matching
contains at most one edge of (3.1).  Consequently covering the forced
matching by scan matchings requires at least `(n+1)/2` scans.

#### Proof

For this single-cut state, `v_t` differs from the all-one word only at the
fixed defect coordinates `c,c+1` and at the current travelling-chip
coordinate.  For a forced counter edge `v_(2j)v_(2j+1)`, the latter two
travelling positions are exactly its support pair.

Fix a coordinate scan and let `p` be its first coordinate pair.  A forced
edge supported on `p` may be selected.  For any other forced counter edge
whose support belongs to the scan's coordinate matching, its two
endpoints agree on `p`.  If `p` avoids `c,c+1`, that common local state is
`11`.  If `p` meets the fixed defect, the possible common states are
`11,10`, or `01`.  Every one of these is nonquiet under both choices of
the mass-two row.  Thus the scan stops at `p` rather than at the edge's
own support.

The tail support is adjacent to the last counter support.  If it is the
first scan pair, the same local check blocks every counter edge; if a
counter support is first, either the tail is not a coordinate pair of the
scan or it is blocked at the first pair.  Hence at most the one forced
edge on `p` is contained.  Since (3.1) has `(n+1)/2` edges, the scan-cover
lower bound follows. \(\square\)

Thus the even common-row theorem cannot simply be applied to every edge
of a wrap-current blossom.  The obstruction is support-theoretic and
already occurs for one blossom, before quotient or hub collisions.

The support boundaries alone are nearly alternating, but support cover
is irrelevant: the unchanged `11` pairs force the first-nonquiet scan to
stop too early.  This is the precise failure of the proposed two-scan
shortcut.

## 4. Exact recursive sufficient statement

Let

\[
 n_0=n,qquad n_{j+1}=\lfloor n_j/2\rfloor,
\]

and use the central quiet identifications (1.6).  At level `j`, scan the
compressed central layer and regard every selected compressed edge as a
requested circulation blossom between its two level-`j` monomers.

### Dyadic global blossom-factor lemma

For every central odd sector there is a global matching construction at
every compression level such that:

1. every selected compressed edge has its literal circulation-blossom
   lift;
2. the lifted gadgets are pairwise vertex-disjoint, including across
   compression levels;
3. their forced matching (3.1) is installed by a protected-minor or
   equivalent bulk-factor operation, rather than by a bounded union of
   coordinate scans;
4. a fixed finite parallel receiver bank is avoided or retained; and
5. exactly the terminal `T_(1,1)` state is exported as the parity socket.

### Theorem 4.1 (conditional exact odd completion)

The dyadic global blossom-factor lemma implies a near-perfect matching
of the central odd capacity-two sector containing the prescribed finite
receiver bank and missing only the prescribed terminal socket.

#### Proof

At the first level, the scan matches every nonquiet state and leaves the
smaller central layer (1.6).  Apply item 3 to install the blossom lifts of
the next scan edges without changing any already closed vertex or the
protected receiver bank.  Items 1--2 allow all switches at one level to
compose.  Iterate.  Each level replaces all nonterminal quiet monomers by
perfectly matched blossom gadgets, and (1.6) identifies the remaining
monomers with the next layer.  The process ends with the unique
`T_(1,1)` monomer, which item 5 exports. \(\square\)

This statement is smaller than arbitrary Tutte because its ports and
recursive residues are explicit.  Theorem 3.1 shows, however, that it is
not a bounded-scan statement.

## 5. The remaining collision invariant

At one fixed cut level, the circulation theorem already proves that
nonhub gadget interiors are injective.  Two lifts can collide only at a
deleted-cut hub, and fixed-level hub-rainbow matching removes that
collision.  Across levels, however, a travelling chip may fill the zero
of an extra cut; the fixed-level injectivity theorem is explicitly sharp
there.

Consequently items 2--3 of the dyadic lemma reduce to the following two
concrete assertions:

1. **levelwise rainbow:** the compressed scan edges can be chosen with
   distinct deleted-cut hubs; and
2. **cross-level protected minor:** after reserving all earlier gadget
   vertices, the next bulk factor realizes (3.1) without leaving those
   vertices.

The common-row construction solves the same issue for a fixed finite
receiver bank, but not for the macroscopic number `Delta_(m,R)/2` of
blossoms.  Theorem 3.1 proves that even a bounded number of scans cannot
install one growing circulation blossom directly.  Theorem 2.1 still
shows that two adjacent scans transport the entire monomer bank
losslessly.  Transport and annihilation are therefore rigorously separate
operations.

There is also a sharp protected-size consequence.  One blossom already
has `(n+1)/2` forced matching edges.  A bank pairing
`Theta(Delta_(m,R))` monomers has `Omega(n Delta_(m,R))` literal protected
incidences if every gadget is reserved individually.  This is not
`O(log n)` or `O(d)`, so the small protected-factor theorem cannot plant
the macroscopic current gadget-by-gadget.  The missing result must be a
bulk equivariant factor theorem; only the finite receiver/socket
interface may be treated as protected support.

Nor can the fixed-bank root marker be scaled at logarithmic cost.  At
central mass, unimodality and averaging give

\[
 \Delta_{m,2m+1}
   =[u^m](1+u+u^2)^m
   \ge {3^m\over 2m+1}.
\tag{5.1}
\]

A binary marker distinguishing one private hub for each of
`Theta(Delta)` blossoms therefore needs

\[
 s\ge \log_2\Delta-O(1)
   \ge m\log_2 3-O(\log m)=\Theta(n).
\tag{5.2}
\]

The `O(log q)` fixed-bank marker theorem remains correct, but here
`q=Theta(Delta)` is exponential in `n`; its marker is linear, not
`O(log n)`.

## 6. Scope

Proved:

1. exact quiet compression of even and odd capacity-two scans;
2. the dyadic central chain ending in one formal socket;
3. lossless alternating transport between adjacent odd roots;
4. an exact linear lower bound on the number of scans needed even for one
   canonical blossom;
5. an exact lower bound excluding `O(log n)` or `O(d)` literal protected
   planting of the macroscopic current; and
6. reduction of the odd matching problem to a dyadic bulk
   rainbow/protected-minor lemma.

Not proved:

1. the dyadic global blossom-factor lemma;
2. a macroscopic hub-rainbow choice at every level;
3. cross-level circulation-interior disjointness; or
4. the resulting near-perfect odd-sector matching.
