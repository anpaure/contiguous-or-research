# The K17 factor has a Catalan Pascal shore, but is not a copied K15/K16 lift

Date: 2026-07-31  
Status: exact solver-free structural theorem and authenticated census; no K17
word or improved numerical upper bound

## 0. Verdict

The 21-component K17 double-rainbow factor has genuine Pascal structure, but
not the literal structure suggested by either saved parent.

* Relative to either new coordinate, its marked shore projects onto all
  rank-eight sets of a sixteen-coordinate cube.  Its internal edges use every
  rank-seven colour exactly once.  Consequently it contains exactly
  \(\operatorname{Cat}_8=1430\) path components, plus seven closed cycles.
  This Catalan path count is forced in **every** lower-rainbow K17 factor.
* It is not a direct four-sector lift of any common K15 lower-rainbow factor:
  4864 of the 6435 rank-seven colour rows violate the necessary equality of
  the X and Y parent edge.
* It is not a chunked copy of the authenticated K16 carrier.  After deleting
  the new coordinate and contracting the intervening unmarked vertices, only
  367 of 12870 successor pairs are edges of the saved K16 path, and 1046
  contracted pairs are not Johnson edges at all.
* The exact K16 cap--facet bijection does give a useful K17 object: a vertical
  matching which is simultaneously rainbow on one whole lower sector and one
  whole upper sector.  But the K17 degree ledger permits only 2860 A-to-rail
  edges in total, so no lower-rainbow 2-factor can contain even one complete
  6435-edge vertical matching.  The current factor retains only 150
  prescribed X vertical edges and 163 prescribed Y vertical edges.

Thus the right recursive object is not a copied carrier.  It is a
**decorated Catalan path forest** on the marked shore, followed by a global
endpoint rethread.  The authenticated factor already supplies such a forest
at the immediate-shadow level.  Its remaining defects are exact and still
global: 5973 short coordinate runs, 1937 deeper upper holes, and 4353 lower-q2
holes.

The certified interval remains

\[
                    24313\leq \nu(17)\leq25746.
\]

## 1. Four Pascal sectors

Write the ground set as \(E\sqcup\{x,y\}\), where \(|E|=15\).  The rank-nine
owners split as

\[
\begin{array}{c|c|c}
\text{sector}&\text{owner}&\text{size}\\\hline
U&V,\ |V|=9&5005\\
X&T+x,\ |T|=8&6435\\
Y&T+y,\ |T|=8&6435\\
A&C+x+y,\ |C|=7&6435.
\end{array}                                                     \tag{1.1}
\]

The authenticated factor has edge-type census

\[
 AA^{5005},\ AX^{1430},\ AY^{1430},\ UU^{4268},\ UX^{737},
 \ UY^{737},\ XX^{5005},\ XY^{693},\ YY^{5005}.               \tag{1.2}
\]

This is exactly the Pascal count, but counts alone do not identify a parent
chronology.

## 2. The Catalan-shore theorem

The following observation is independent of the finite certificate.

### Theorem 2.1 (marked shore is a Catalan path forest plus cycles)

Let \(H\) be any spanning 2-factor of \(J(17,9)\) whose lower edge colours
are every rank-eight set exactly once.  Let \(H_y\) be the subgraph induced
by owners containing \(y\), and delete \(y\) from its vertices and edge
colours.  Then

1. \(H_y\) spans all \(\binom{[16]}8\) vertices;
2. its edges have every colour in \(\binom{[16]}7\) exactly once;
3. it has exactly \(\operatorname{Cat}_8=1430\) path components, where an
   isolated vertex counts as a path, plus an unrestricted number of cycles.

#### Proof

An edge intersection contains \(y\) exactly when both endpoints contain
\(y\).  The lower-rainbow hypothesis therefore puts precisely all
\(\binom{16}7=11440\) y-containing lower colours on the internal edges of
\(H_y\), once each.  Deleting \(y\) gives assertions 1 and 2.

The induced graph has maximum degree two.  If it has \(p\) path components
and any number of cycles, then

\[
 p=|V(H_y)|-|E(H_y)|
  ={16\choose8}-{16\choose7}=12870-11440=1430.
\]

The last number is \(\operatorname{Cat}_8\). \(\square\)

For the authenticated factor, the projected marked shore has exactly 1430
paths and seven cycles.  Its 11440 edge colours are the complete rank-seven
layer.  This is the precise recursive content of the 21-component object.

The count is dimension-free.  If a lower-rainbow spanning 2-factor of
\(J(2m+1,m+1)\) is cut according to one coordinate, its marked shore projects
onto \(\binom{[2m]}m\), its internal edge colours are
\(\binom{[2m]}{m-1}\), and therefore its number of path components is

\[
 {2m\choose m}-{2m\choose m-1}
   ={1\over m+1}{2m\choose m}=\operatorname{Cat}_m.             \tag{2.1}
\]

Thus Catalan many open paths are not a defect of the finite lift.  They are
the exact Euler characteristic of every lower-rainbow Pascal shore.  The
full 2-factor has exactly

\[
 2\left({2m\choose m}-{2m\choose m-1}\right)
   =2\operatorname{Cat}_m                                      \tag{2.2}
\]

cross-shore edge incidences: each of the forced paths contributes its two
ends and each marked cycle contributes none.  The recursive problem is to
decorate and connect precisely these forced endpoint pairs.

There is a direct connection with the saved K16 carrier.  That carrier is a
Johnson path on 12870 rank-eight vertices.  Its 12869 lower edge occurrences
have multiplicity profile

\[
                         1^{10066}2^{1319}3^{55}.                \tag{2.3}
\]

Choosing one occurrence of each of the 11440 colours deletes exactly 1429
edges and hence leaves 1430 path pieces.  The finite K17 factor has the same
Euler arithmetic, but its seven cyclic pieces show that it was globally
rethreaded rather than obtained by deletion alone.

## 3. Exact no-go for a common K15 parent

The exact K15 carrier consists of Johnson cycles of lengths 6390 and 45 and
has one edge \(e_c\) of each rank-seven colour \(c\).

More generally, any direct four-sector lift from a single lower-rainbow K15
factor obeys the following necessary local law.  For each \(c\):

* in a selected row, the projected XX and YY edges are both \(e_c\), so they
  agree with each other;
* in a leave row, the X endpoint of the AX socket and the Y endpoint of the
  AY socket are the two endpoints of \(e_c\).

The authenticated K17 factor has 5005 selected-type rows and 1430 leave-type
rows.  Direct replay gives

\[
\begin{array}{c|r|r}
\text{row type}&\text{rows}&\text{rows satisfying the common-parent law}\\\hline
\text{selected}&5005&189\\
\text{leave}&1430&1382.
\end{array}                                                     \tag{3.1}
\]

Therefore

\[
                       6435-189-1382=4864                       \tag{3.2}
\]

colour rows contradict every common-parent direct lift.  This is stronger
than comparison with the saved K15 answer.  Against that particular parent,
only 536 X rows and 518 Y rows use its prescribed edge or socket endpoint.

### Corollary 3.1

The 21-component factor is not the direct K15 four-sector construction with
a different occurrence transversal, rerooting, or component order.  Its
rail edge assignment was rebuilt globally.

This does not rule out a more general K15-to-K17 braid which changes the
parent edges themselves.

## 4. Exact no-go for a chunked copy of the K16 chronology

Let

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
```

be the authenticated K16 rank-eight target chronology.  It is a Johnson path
through every rank-eight set exactly once.

In every K17 factor component, retain only the y-containing owners, delete
\(y\), and join consecutive retained vertices cyclically.  This produces 20
nonempty projected cycles and 12870 contracted successor pairs.  Their
symmetric-difference histogram is

\[
 2^{11824}4^{249}6^{278}8^{310}10^{167}12^{38}14^4.             \tag{4.1}
\]

Only 367 contracted pairs are successor edges of the saved K16 path; 1046
are not Johnson edges.  Hence the marked shore is not a collection of
shifted/reversed chunks of that chronology.  Independently, the complete
one-occurrence Pascal selection domain on the saved K16 chronology is
already closed by the opposite-choice core on colour `0x0bf5`.

This is a source-relative statement.  A different or rethreaded K16 carrier
remains possible.

## 5. What the cap--facet bridge really supplies

The K16 certificate induces a bijection

\[
 \phi:\binom E8\longrightarrow\binom E7,
 \qquad \phi(C)\subset C.                                     \tag{5.1}
\]

It consists of 6386 literal cap-mode rows and the perfect matching on the 49
exceptional bridge rows.

### Theorem 5.1 (doubly-rainbow vertical matching)

The 6435 K17 Johnson edges

\[
       (y+C)\ --\ (x+y+\phi(C)),\qquad C\in\binom E8,          \tag{5.2}
\]

form a perfect matching between the Y and A sectors.  Their intersections
are every set \(y+F\), \(|F|=7\), once, and their unions are every set
\(x+y+C\), \(|C|=8\), once.  Thus (5.2) is simultaneously rainbow on one
complete lower-q1 sector and one complete upper-q1 sector.  The analogous
statement holds with X in place of Y.

#### Proof

Containment in (5.1) makes (5.2) a Johnson edge.  Its intersection is
\(y+\phi(C)\), and its union is \(x+y+C\).  Both maps are bijections. \(\square\)

This is genuine reusable supply, but it cannot simply be inserted whole.
Every lower-rainbow K17 2-factor must contain all 5005 xy-coloured edges, and
only AA edges have an xy-containing intersection.  Those 5005 edges consume
10010 of the 12870 A-degrees.  Therefore only

\[
                         12870-10010=2860                       \tag{5.3}
\]

A-to-rail edges remain in total.  In particular, no such factor can contain
even one entire 6435-edge matching (5.2), much less both X and Y copies.

The current factor uses 1430 AX and 1430 AY edges.  Only 150 AX and 163 AY
edges agree with \(\phi\).  Among the special 49 bridge facets, each shore
has 11 vertical edges, of which only two use the prescribed cap.  The
authenticated factor therefore did not inherit the finite facet exchange;
it solved its immediate palettes through another rethread.

## 6. Exact residual defect ledger

The cap--facet bridge should not be credited with gates it does not touch.
For the 21-component factor the exact cyclic residence defects are

\[
 N_1=0,\qquad N_2=3705,\qquad N_3=2268.                       \tag{6.1}
\]

Of the 5973 short runs, 4259 belong to the old fifteen coordinates, 861 to
\(x\), and 853 to \(y\).  These depend on the K17 owner order, so an envelope
matching from K16 does not change them.

All rank-ten upper colours already occur.  The 1937 deeper upper holes are

\[
\begin{array}{c|rrr|r}
\text{rank}&y\text{ only}&x\text{ only}&xy&\text{total}\\\hline
11&445&453&674&1572\\
12&107&97&154&358\\
13&0&1&6&7.
\end{array}                                                     \tag{6.2}
\]

There is no hole omitting both new coordinates.  Consequently the protected
U bank has already discharged the entire old upper cube.  A *contiguous*
copy \(y+T^{16}\) of the exact K16 target chronology would cover all 1386
currently missing y-containing upper targets.  The symmetric x copy would
cover 1385.  This is exact inherited supply, but it is conditional: Section
4 proves that the current factor contains neither block, and installing one
must preserve the lower rainbow and both shore interfaces.

At lower depth two the factor misses 4353 rank-seven targets:

\[
\begin{array}{c|rrrr}
\text{signature}&00&x&y&xy\\\hline
\text{missing}&624&1655&1667&407.
\end{array}                                                     \tag{6.3}
\]

Forty of the 49 exceptional K16 bridge facets happen to occur as q2 triple
intersections; nine remain missing.  Therefore even the finite bridge family
is not fully inherited at the next compiler row.  Since the current object
is cyclic and has no chosen opening or monotone deadline schedule, no
integral lower compiler is yet defined, let alone certified.

For comparison, the exact K16 target path itself has no internal run of
length one or two and exactly 1423 internal length-three runs.  It covers all
26333 old upper targets of ranks at least nine.  These figures explain why a
protected K16 marked block is attractive, but the 4864-row and opposite-
choice obstructions explain why copying it is insufficient.

## 7. Correct next theorem

The finite evidence points to the following recursion target.

> **Decorated Catalan-shore lift.**  Starting from a K16 middle path, select
> and rethread one occurrence of every rank-seven lower colour into exactly
> \(\operatorname{Cat}_8\) paths, while preserving enough inherited upper
> intervals and the depth-three staircase.  Pair the 2860 endpoints with the
> unmarked Pascal shore, using a controlled subset of the cap--facet vertical
> matching, and complete the global factor without creating new deep holes.

Theorem 2.1 makes the number of paths unavoidable.  Theorem 5.1 supplies a
perfectly decorated vertical-edge bank.  Equations (3.2), (4.1), and (5.3)
show why neither raw copying nor full bridge insertion can prove the result.
The remaining problem is a joint occurrence selection/rethread, not a
capacity or divisibility problem.

## 8. Audit

Run

```text
python3 scratch/audit_k17_facet_pascal_ancestry_20260731.py
```

It authenticates all three certificates, reconstructs the complete K16
cap--facet matching, checks the common-parent identities colour by colour,
projects both Pascal shores, and independently replays every residence and
upper/lower defect count.  It writes

```text
scratch/k17_facet_pascal_ancestry_20260731.audit.json
```

No solver, randomized search, network access, or unverified checkpoint is
used.
