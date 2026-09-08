# Every single-hexagon perturbation still fails the 83-target block screen

2026-09-08. Cover-selectors finite inventory, mathematical certificate,
and independent physical/certificate replay. All computation ran only
through ssh h100. No two-flip search or free row-order solver was run.
Direct-route's full note, source, and finite-certificate audit passed.
Root's full note integration audit also passed.

## 1. Complete finite inventory

Use the cyclic source S_t,U_t from
MU9_TO_BINARY10_CONSECUTIVE_BLOCK_OBSTRUCTION_20260908.md and form the
252-vertex Hamilton cycle

    S_t -- U_t -- S_(t+1),  t modulo126.

Every six-cycle is specified by a three-coordinate core K and three
outside coordinates a,b,c. Its lower vertices are K+a,K+b,K+c and its
upper vertices are K+ab,K+bc,K+ca. There are
binom(9,3)binom(6,3)=1680 such six-cycles.

The screen changes one alternating three-edge matching to the other
only if every removed edge is present and every inserted edge is absent.
It then checks all degrees and traverses the result to retain only a
single252-vertex Hamilton cycle. Every retained cycle has all126 lower
and126 upper targets exactly once, with U_t=S_t union S_(t+1).

Exact results:

| Quantity | Count |
|---|---:|
| Six-cycles inspected |1680|
| Matching flips satisfying the edge condition |162|
| Such flips producing multiple components |72|
| Distinct resulting Hamilton cycles |90|
| Hamilton cycles with82 distinct V targets |9|
| Hamilton cycles with83 distinct V targets |54|
| Hamilton cycles with84 distinct V targets |27|

Here V_t=U_t union U_(t+1), always of rank six. Intrinsically V is
attached to the lower vertex S_(t+1): it is the union of that vertex's
two upper neighbors. Thus only the three lower vertices of the flipped
hexagon change their V targets, even though the extracted cyclic indexing
may change globally. The source has all84 rank-six targets, so losing at
most three is consistent with the exact inventory.

For a small84-target Hamilton certificate, take K={0,1,3} and
{a,b,c}={5,7,8}. Remove

    (43,299), (139,171), (267,395)

and insert

    (43,171), (139,395), (267,299).

These are literal mask-labelled edges of the source Hamilton cycle.
This certificate preserves Hamiltonicity and all84 V targets; it does
not provide a viable42-row block partition.

The81 cycles with at least83 V targets form exactly nine classes under
cyclic coordinate rotation, each of size9. This quotient is exact:
rotated edge sets are compared as full sorted252-edge sets. Both
orientations of a representative were included in the boundary screen.

## 2. The bounded boundary model and its stronger certificate

The initial finite model selected42 locally realizable blocks(s,p),
1<=p<=5, whose S intervals partition all126 positions. Each selected
block retains V_(s-1),...,V_(s+p-3), and drops V_(s+p-2). It required at
least83 distinct retained V targets. All18 representative/orientation
models returned INFEASIBLE, with no UNKNOWN status.

The mathematical certificate below proves more and does not rely on
that solver result. In every such partition the dropped V positions
have consecutive cyclic gaps at most5. Equivalently,

    EVERY five-position V window contains a drop.       (1)

The certificate uses only (1); it ignores local row realizability,
the exact42-block count, and all free row orders.

### Guarded-target lemma

Call an observed rank-six target q guarded if, for EVERY occurrence x
of q in the V cycle, a specified five-position window containing x has
four other target occurrences that are globally unique in the V cycle.
Let H(q) contain q and all these unique guard targets. Then every
drop set satisfying (1) misses at least one target in H(q).

Proof. If every q occurrence is dropped, q itself is missing. Otherwise
choose a retained occurrence x. Its specified five-window must contain
a drop, and that drop is one of the four globally unique guard targets.
That target is missing. This proves the assertion. Square.

Thus two disjoint guard supports force two distinct holes. A target
absent from the entire V cycle is also a hole, and is automatically
outside every guard support made from observed targets.

## 3. Small certificate table for all nine rotation classes

For deterministic indexing, traverse each flipped cycle from the
smallest lower mask, choosing its smaller upper neighbor first. Write
the resulting alternating lists as S_0,U_0,S_1,U_1,... and define V as
above. All indices below are cyclic modulo126.

A guard entry q: x@w means that the occurrence V_x=q is guarded by
the five-position window beginning at w; the other four positions in
that window have globally unique targets. Every occurrence of q is
listed, so no unguarded occurrence is being ignored.

| Representative | Core K | Outside triple | Intrinsic hole | Guard entries |
|---:|---|---|---:|---|
|0|0,1,3|5,7,8|none|111:94@90; 365:20@20,43@43,104@104|
|1|0,1,4|2,5,8|none|366:94@94; 219:10@10,52@52,118@118|
|2|0,1,5|2,6,7|119|219:49@49,91@91,118@118|
|3|0,1,6|3,5,7|111|219:52@48,118@118|
|4|0,1,7|2,4,6|none|219:76@76,118@118; 365:20@20,62@62,104@104|
|6|0,2,4|3,5,8|437|438:12@8,49@45,91@87|
|7|0,2,5|3,6,7|429|125:18@16|
|8|0,2,6|1,3,5|359|219:40@40,82@82,118@118|
|9|0,2,6|1,4,5|359|219:49@45,89@85,118@118|

The three84-target representatives have the following visibly disjoint
support pairs:

    class0:
      {111,175,235,430,444}
      {187,189,215,222,243,343,365,366,373,411,429,474,490}

    class1:
      {366,407,411,474,490}
      {175,219,221,235,311,347,374,378,430,437,444,469,486}

    class4:
      {219,221,311,347,374,378,437,469,486}
      {187,189,215,222,243,343,365,366,373,411,429,474,490}.

Each83-target representative has its intrinsic hole plus a hole forced
inside its observed guard support. Therefore every one of the81
screen-surviving cycles loses at least TWO rank-six targets after a
consecutive-block partition. Its retained rank-six coverage is at most82.
The remaining nine Hamilton flips already have at most82 targets before
any positions are dropped.

This proves that NONE of the90 one-hexagon Hamilton perturbations can
give the requested at-least83-target block lift. Coordinate rotations
preserve the finite conditions. Reversal preserves contiguous five-window
sets, global target multiplicities, support disjointness, and (1), so
the same certificate applies in either orientation without relying on
a preferred direction for a guard.

The compact JSON certificate contains the full126-entry V sequence,
the six changed edges, the actual four unique target VALUES at every
guard, each entire support, and every represented rotation-class id:

    MU9_HEX_FLIP_GUARD_CERTIFICATE_20260908.json.

## 4. What a useful further modification must change

The exclusion is caused by explicit small protected supports, rather
than by the number of available Hamilton cycles. A modification that
preserves an intrinsic hole and its displayed guard certificate, or
preserves both disjoint displayed supports in a full84 case, cannot help.
Changing only row orders or cyclic block boundaries also cannot help.

For a guarded q, a genuinely relevant change must invalidate at least
one of the certificate's literal conditions. Possibilities include:

- creating an additional q occurrence that is not protected by one of
  the four-unique-target windows;
- changing a unique guard target's multiplicity, by creating a second
  occurrence, or changing the target at its sole occurrence;
- changing the adjacency inside a displayed five-window so that this
  protected occurrence is no longer surrounded by that guard window;
- in an83-target class, restoring the intrinsically absent target.

These are necessary ways to affect the particular certificate, not
sufficient ways to produce a cover. Other guard windows may survive.
Deleting all q occurrences leaves q itself as a hole, so that alone
does not eliminate the guarded-target charge.

The physical support for such a test is explicit. The V window
[w,w+4] uses lower vertices S_(w+1),...,S_(w+5), linked by upper
vertices U_(w+1),...,U_(w+4). A six-cycle flip changes V values only
at its three lower vertices and changes lower-to-lower adjacency only
through its three upper vertices. Therefore a prospective next move
that changes none of these links, changes no guard/q occurrence, and
creates no new duplicate of a guard or q preserves that certificate.
This yields a direct necessary-support filter before any further search.

For example, class0 requires disturbing either its unique five-window
90,...,94 or the q=365 protection at20,...,24;43,...,47;104,...,108.
Class1 requires disturbing either94,...,98 or the q=219 protection
at10,...,14;52,...,56;118,...,122. Class4 requires disturbing at least
one of the two displayed q=219 and q=365 support certificates. An
unrestricted two-flip inventory was deliberately not launched.

## 5. Provenance, caps, and independent replay

All numerical execution used ssh h100, hostname arboghast. Measured
Python runtimes were0.1912 seconds for the complete flip inventory,
0.5741 seconds for all18 boundary models,0.1628 seconds for the final
solver-independent certificate extraction, and0.0041 seconds for the
independent physical/guard replay. Including the earlier certificate
formatting correction, total computation remained well below20 seconds.
The boundary process was pinned to two CPUs and capped at1GiB; no
larger model was run.

Local durable sources:

- inventory_mu9_hamilton_hex_flips_20260908.py
- screen_mu9_hex_flip_block_partitions_20260908.py
- certify_mu9_hex_flip_drop_spacing_20260908.py
- verify_mu9_hex_guard_certificate_20260908.py

Local reports:

- MU9_HEX_FLIP_INVENTORY_20260908.json
- MU9_HEX_FLIP_BLOCK_PARTITIONS_20260908.json
- MU9_HEX_FLIP_GUARD_CERTIFICATE_20260908.json
- MU9_HEX_FLIP_DROP_CERTIFICATES_20260908.json

All paths above are in this scratch directory. The last report also
contains explicit unit-propagation refutations for every possible allowed
single missing target, using only the five-window drop clauses and
the remaining target-coverage clauses. Each inference was replayed.
Those longer traces are optional: the guard table is the shorter proof.

The independent verifier imports neither CP-SAT nor the inventory code.
Starting from the literal14-mask seed, it reconstructs all nine
representative flipped graphs, verifies each alternating matching and
252-cycle, recomputes V, and checks every guard occurrence, five-window,
unique target value, support, and intrinsic hole. All nine pass.
Its executed command was

    ssh h100 'timeout 5s python3 /tmp/mu9_hex_flip_inventory_20260908_cover_selectors/verify_mu9_hex_guard_certificate_20260908.py /tmp/mu9_hex_flip_inventory_20260908_cover_selectors/guard_certificate_compact.json'

The result is a rigorous finite exclusion for this single-flip,
consecutive-block family. It says nothing about arbitrary42-row banks,
other Hamilton cycles, nonconsecutive block assignments, or a proved
asymptotic lower bound.
