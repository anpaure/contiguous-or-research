# Final cross-audit: cyclic common-history hinge ring and short-deck invariance

**Date:** 2026-08-04  
**Method:** adversarial symbolic checking of parameter sufficiency, owner and
palette identities, directed component fusion, every short exterior-interval
case, compiler transport, and residence.  Boundary cases `d=1`, `c=3`, empty
or unequal contexts, cyclic wraparound, and early linear endpoints were
checked explicitly.  No search, solver, or sampled computation was used.

**Audited theorem:**
`MATH_THEOREM_CYCLIC_COMMON_HISTORY_HINGE_RING_AND_SHORT_DECK_INVARIANCE_20260804.md`,
SHA256
`96b9f8717c138dfac7df2a4d1c439392de1a3313c9e57114d2e1cd6f145b90ba`.

## 0. Verdict

**FINAL GO at its stated local scope.**  The construction exists for every
advertised parameter triple, all `2c` owners are distinct already at `c=3`,
the lower and upper palette identities are exact, and the cyclic edge
replacement fuses the indicated directed components in the claimed
direction.  Theorem 3.1 preserves the complete occurrence deck at every
width at most `d` for arbitrary contexts.  The compiler corollary follows for
the stated occurrence-labelled strict-lower matching model.  Residence is
valid on a cyclic source word, or in a linear word with the depth-`d` endpoint
collar explicitly required in Section 4.  No arbitrary-width exterior or
planting conclusion is smuggled into the result.

The two-component fallback is also valid at its weaker stated scope: it
preserves owners and the width-at-most-`d` deck, fuses the two directed
components, and loses at most four old local immediate-palette target values,
conditional on a separate exterior upper guard for longer crossing
intervals.

The added protected-factor corollary is valid: its incidence bank has exactly
`2c` distinct edges and maximum degree two, the cited theorem applies under
`2c<=m-2`, and the cyclic edge replacement preserves degree two at every
lower and owner vertex.

The all-width strengthening is also valid.  Every interval crossing both
screens contains a rank-`r` owner and hence cannot be a strict-lower cell;
all remaining strict-lower occurrences lie in the literal left/right/context
bijection.  Every potentially lost old upper value contains a rank-`r+1`
base `U_i`, giving the stated Boolean-cone bounds for both the ring and the
two-component fallback.

## 1. Parameter sufficiency

The partition `B=C_1 dotcup ... dotcup C_d` with every part nonempty exists
exactly when

\[
                         |B|=r-2\ge d,
\]

which is the hypothesis `r>=d+2`.  After choosing `B`, the construction
needs the `c+1` distinct exterior labels `b,a_0,...,a_(c-1)`.  The total
number of required coordinates is

\[
                         (r-2)+(c+1)=r+c-1,
\]

exactly the advertised ground-set bound.  The source letters `X_i` and
`Y_i` have two distinct labels because `c>=3`, and every `C_j` is nonempty.
Thus there is no hidden size or nonemptiness requirement.

## 2. Owners and immediate palettes

The ORs of the two length-`d+1` windows are literally

\[
 L_i=B\cup\{b,a_i\},
 \qquad
 R_i=B\cup\{a_{i-1},a_i\}.
\]

Each has rank `(r-2)+2=r`.  The `L_i` are distinct because their `a_i` are
distinct.  The `R_i` correspond to the edges of the simple cycle on the
`a_i`; its unordered adjacent pairs are distinct for every `c>=3`, including
the triangle `c=3`.  Finally no `L_i` equals any `R_j`, because `b` belongs
to every former and no latter.  Hence all `2c` owners are distinct.

For the old hinges,

\[
 L_i\cap R_i=B\cup\{a_i\}=I_i,
\]

and

\[
 L_i\cup R_i=B\cup\{b,a_{i-1},a_i\}=U_i.
\]

The lower values vary by one singleton and the upper values by one distinct
cyclic adjacent pair, so both palettes are simple.

For the rethreaded hinge `L_i R_(i+1)`, direct intersection and union give

\[
 L_i\cap R_{i+1}=B\cup\{a_i\}=I_i,
\]

\[
 L_i\cup R_{i+1}=B\cup\{b,a_i,a_{i+1}\}=U_{i+1}.
\]

Thus tails fix all `L_i`, heads cyclically permute all `R_i`, the lower
palette is pointwise fixed, and the upper palette is the cyclic permutation
`U_i -> U_(i+1)`.  All identities remain valid across the modular wrap from
`c-1` to zero.

## 3. Directed component fusion

Remove the directed edge `L_i -> R_i` from component `i`.  The remaining
directed path begins at `R_i` and ends at `L_i`.  Inserting
`L_i -> R_(i+1)` therefore sends the end of path `i` to the beginning of
path `i+1`.  The induced successor permutation is

\[
                         i\longmapsto i+1\pmod c,
\]

one `c`-cycle.  Consequently all `c` components fuse into one.  Every owner
retains one predecessor and one successor, and distinctness prevents an
edge collision.  The new source fragments have the same length `d+2`, so no
source position is added.  As the theorem says, this graph argument is
conditional only on the displayed occurrences being jointly legal under
the exterior guards.

## 4. Exhaustive audit of Theorem 3.1

The positions of `X_i` and `Y_i` are separated by all `d` letters of the
common history.  Any interval containing both therefore has width at least

\[
                         1+d+1=d+2.
\]

Thus an interval of width `ell<=d` cannot meet both hinge ends.  Every such
interval meeting the displayed neighbourhood is in exactly one of these
classes:

1. a suffix of `P_i`, followed by `X_i` and possibly a prefix of `C`;
2. a suffix of `C`, followed by `Y_i` and possibly a prefix of `Q_i`;
3. wholly inside `C`;
4. wholly inside `P_i` or wholly inside `Q_i`.

The first class is fixed role by role.  The second class in old role `j` is
identical as a source word to the corresponding class in new role `j-1`,
because the complete pair `(Y_j,Q_j)` is moved together and the preceding
suffix of `C` is literal and common.  The third class is fixed.  Left-context
instances in the fourth class are fixed, and right-context instances are
cyclically permuted with `Q_j`.

This remains a bijection when contexts are empty, have unequal lengths, or
contain labels already used elsewhere: the matched source subwords are
literal copies, so their OR values and occurrence multiplicities agree.
Truncation at a context endpoint also agrees on the two matched sides.  The
four classes exhaust all intervals, since crossing from `P_i` into `C`
forces inclusion of `X_i`, and crossing from `C` into `Q_i` forces inclusion
of `Y_i`.

Therefore the occurrence-labelled OR multiset is exactly preserved for
each `1<=ell<=d`.  Taking the disjoint union of these per-width bijections
proves the joint all-width-at-most-`d` assertion.

The first possible exterior interval that can couple the unchanged left
body to the newly attached right body contains both hinge ends and has width
at least `d+2`.  It is deliberately outside Theorem 3.1.  Thus there is no
missing short exterior case, and no unsupported long-interval claim.

### All-width strict-lower corollary

For an interval of arbitrary width, the same left/right/context bijection
fails only if the interval contains both screens `X_i` and `Y_i` (or
`Y_(i+1)` after rethreading).  Such an interval contains every source letter
of `mathcal C`, hence contains

\[
                         B\cup X_i=L_i.
\]

Since `|L_i|=r`, rank monotonicity under union shows that its OR has rank at
least `r`.  Therefore every interval-OR occurrence of rank strictly below
`r` meets at most one screen.

An arbitrary-width one-sided interval extending into `P_i` is fixed as a
literal left subword.  An arbitrary-width one-sided interval extending into
`Q_i` is moved with the complete pair `(Y_i,Q_i)` and has an identical
source subword in the cyclically shifted role.  Intervals wholly inside a
context or the common history are likewise fixed or permuted.  These maps
are invertible and preserve occurrence multiplicity and OR value.

Thus the complete all-width strict-lower occurrence deck is invariant.  In
particular, transporting the selected cells of any strict-lower compiler
along this bijection preserves width, value, and injectivity, so its deletion
number remains zero without a width-normal-form assumption.

### Exact upper-damage cone

An old interval not retained by the unchanged or one-sided-permuted channel
must traverse at least one original hinge `i`.  It then contains

\[
 B\cup X_i\cup Y_i
 =B\cup\{b,a_{i-1},a_i\}=U_i.
\]

The three exterior labels are distinct and disjoint from `B`, so
`|U_i|=(r-2)+3=r+1`.  On a `k`-coordinate ground set, the number of supersets
of one `U_i` is exactly

\[
                         2^{k-(r+1)}=2^{k-r-1}.
\]

Consequently every potentially lost old target belongs to

\[
 \bigcup_{i=0}^{c-1}\{Z:U_i\subseteq Z\subseteq[k]\},
\]

whose size is at most `c*2^(k-r-1)` by the union bound.  Cone overlaps can
only decrease this number.

For the two-component fallback, the two old upper bases in (5.3) each have
rank `r+1`.  The same argument gives

\[
                         2\,2^{k-r-1}=2^{k-r}.
\]

This is only a damage-universe localization.  It neither asserts that all
cone values are actually lost nor provides protected alternative witnesses
inside the cone.

## 5. Internal fragment deck

For widths at most `d`, set the contexts empty in Theorem 3.1.  At width
`d+1`, each old fragment has exactly the two owner occurrences `L_i,R_i`,
and the head permutation preserves their full multiset.  At width `d+2`,
the only old value in role `i` is

\[
 B\cup\{b,a_{i-1},a_i\}=U_i,
\]

whereas the only new value is

\[
 B\cup\{b,a_i,a_{i+1}\}=U_{i+1}.
\]

These are cyclic permutations.  Since a fragment has exactly `d+2` source
letters, these cases prove its complete internal deck at every width.

## 6. Compiler transport

A strict-lower compiler of the type claimed uses distinct interval
occurrences as cells and matches them according to their OR values.  Apply
the all-width strict-lower occurrence bijection above to each selected cell.
It preserves the cell width and OR value, and bijectivity preserves
distinctness of the selected resources.  Carry the same target assignment
across this map.  Every compiler edge remains valid and no cell is deleted,
so the deletion number is zero.

This conclusion is exactly as strong as the strengthened theorem states: it
transports every occurrence-labelled strict-lower matching, with no width
restriction.  It does not preserve rank-`r` or upper cells, or an exterior
common-cap structure that was not part of that matching.

## 7. Residence and connector accounting

In a cyclic source word, an occurrence of coordinate `x` at source position
`p` belongs to the `d+1` consecutive owner windows whose starting positions
are

\[
                         p-d,p-d+1,\ldots,p.
\]

Hence each occurrence creates a positive owner run of length `d+1`.
Overlapping or adjacent occurrence-runs merge into a run at least as long;
disjoint runs retain their individual length.  Every coordinate of `B`
occurs in some `C_j`, while `b` and the `a_i` occur in the exterior source
letters.  This proves the positive-residence statement on the intended
cyclic factor.

For a linear word, the displayed count fails near an endpoint; for example,
an isolated fragment with empty contexts need not have `d+1` owner windows
through an exterior letter.  The theorem explicitly supplies the necessary
scope qualification: plant the fragment at least `d` source positions from
each relevant endpoint or use the clipped endpoint collar.  The residence
claim is certified with that qualification, not as an endpoint-free linear
statement.  Minimum zero-run/gap residence is also correctly left to the
exterior guard.

The old and new banks use the same multiset of `X_i`, every `C_j`, and
`Y_i`, with the `Y_i` merely permuted.  The overlap history is the identical
ordered word `(C_1,...,C_d)` at every hinge.  Thus the bare source-position
or de Bruijn connector charge is zero.

## 8. Two-component bounded-damage fallback

The fallback needs the same set `B` and four distinct exterior labels
`p,q,s,t`, hence exactly

\[
                         (r-2)+4=r+2
\]

ground coordinates.  Its old owners are

\[
 B\cup\{p,q\},\quad B\cup\{p,s\},\quad
 B\cup\{s,t\},\quad B\cup\{q,t\}.
\]

The four two-label sets are pairwise distinct, so all owners have rank `r`
and are distinct.  The old edges have lower/upper colours

\[
\begin{array}{c|cc}
1&B\cup\{p\}&B\cup\{p,q,s\}\\
2&B\cup\{t\}&B\cup\{q,s,t\}.
\end{array}
\]

After swapping heads, the first cross edge joins `B+pq` to `B+qt`; its
intersection and union are

\[
                         B\cup\{q\},\qquad B\cup\{p,q,t\}.
\]

The second joins `B+st` to `B+ps`; its intersection and union are

\[
                         B\cup\{s\},\qquad B\cup\{p,s,t\}.
\]

Thus both cross pairs are Johnson edges.  Removing one directed edge from
each old component leaves paths `R_i -> ... -> L_i`; the transposed heads
insert `L_1 -> R_2` and `L_2 -> R_1`, producing one directed cycle.  This is
the two-component specialization of the successor-permutation argument.

The proof of Theorem 3.1 uses only a common history and a permutation of the
complete right pairs `(Y_i,Q_i)`, not the cyclic adjacent-pair formula from
Sections 0--2.  It therefore applies unchanged to this transposition and
preserves every interval occurrence of width at most `d`.

The owner-width `d+1` bank is unchanged.  More generally, an exterior
interval of width `d+1` still cannot meet both hinge ends and is covered by
the same left/right source-word bijection.  At width `d+2`, the only interval
that meets both ends is the full internal fragment.  Its two old values are

\[
 B\cup\{p,q,s\},\qquad B\cup\{q,s,t\},
\]

and its two new values are

\[
 B\cup\{p,q,t\},\qquad B\cup\{p,s,t\}.
\]

These are exactly the old and new upper immediate colours already displayed;
they introduce no additional target-value type beyond the upper-palette
change.  All other width-`d+2` intervals meet only one side and are transported
by the same literal subword map.

The two old lower colours and two old upper colours are pairwise distinct and
none survives among the four new colours.  Hence there are exactly four old
local immediate-palette target values potentially lost, and therefore at
most four casualties.  The theorem correctly counts lost old targets rather
than also charging the newly introduced values.

Intervals longer than `d+2` can meet a left context, both hinge ends, and the
new right context.  Their OR values need not be preserved.  The fallback
therefore makes its bounded-eviction consequence conditional on an exterior
upper guard protecting every such longer crossing interval, and explicitly
does not claim exact q1 current or unguarded arbitrary-width preservation.

## 9. Protected owner/lower-q1 planting corollary

Specialize `r=m`.  Since `|B|=m-2`, every

\[
                         I_i=B\cup\{a_i\}
\]

has rank `m-1`, while every `L_i,R_i` has rank `m`.  The containments
`I_i subset L_i,R_i` are literal, so the lifted bank

\[
                         P_c=\{I_iL_i,I_iR_i:0\le i<c\}
\]

lies in the Middle-Levels incidence graph `ML_m`.

The `I_i` are distinct, and all `L_i,R_i` are distinct by Theorem 1.1.
Consequently the displayed edges are all distinct and

\[
                         |E(P_c)|=2c.
\]

Each `I_i` has degree two in `P_c`; every displayed owner has degree one;
all other vertices have degree zero.  Hence

\[
                         \Delta(P_c)=2.
\]

The frozen small protected-factor theorem states that every subgraph of
`ML_m` with maximum degree at most two and at most `m-2` edges is contained
in a spanning two-factor.  Therefore `2c<=m-2` is exactly sufficient to
extend `P_c`.  It also guarantees enough coordinates for the construction:
the required `m+c-1` labels fit in the `2m-1` element Middle-Levels universe
because `c<m`.

Let `F` be any spanning two-factor containing `P_c`.  Define

\[
 \widehat P_c=\{I_iL_i,I_iR_{i+1}:0\le i<c\}.
\]

Every new edge is a literal incidence because
`I_i=B+a_i subset B+a_i+a_(i+1)=R_(i+1)`.  Moreover, no new edge
`I_iR_(i+1)` can already lie in `F-P_c`: the two old edges of `P_c` already
saturate `I_i` to degree two in `F`.

Thus the set-level replacement

\[
                         \widehat F=(F-P_c)\cup\widehat P_c
\]

is well defined.  At each `I_i`, one old head edge is removed and one new
head edge is inserted, while `I_iL_i` is restored.  Each `L_i` keeps its
unique protected incidence.  Each `R_j` loses `I_jR_j` and gains
`I_(j-1)R_j`.  Hence every displayed lower and owner vertex has exactly its
old degree, and every other vertex is untouched.  Therefore `widehat F` is
again a spanning two-factor.

The corollary correctly claims only an unoriented owner/lower-q1 skeleton.
The arbitrary completion need not satisfy the immediate-upper palette,
residence away from the protected bank, a component bound, or the all-width
and common-cap guards.

The direct dependency is
`MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`,
SHA256
`1deded37f83351f0750e633b8e771bc364159d7b979c21d21c5c306573b5f17f`.
Its Theorem 2.1 has exactly the maximum-degree-two and `m-2` edge hypotheses
used above.

## 10. Exact scope and dependency audit

Apart from Corollary 2.2 and its frozen protected-factor dependency recorded
in Section 9, the theorem's local literal construction is self-contained.
The completed-hinge fusion used in Section 2 is proved directly by the
path-successor argument above; the later forest-complement criterion appears
only in a conditional future statement and is not needed for any proved
conclusion.

Corollary 2.2 plants the bank in an arbitrary spanning owner/lower-q1
two-factor.  The result does not plant it in a spanning **upper-complete,
resident, common-cap guarded, or prescribed-component** carrier, prove
exterior guard legality, preserve arbitrary-width rank-`r`/upper occurrences
that traverse the full history, or provide protected alternatives inside the
localized upper-damage cones.  Its final protected-planting gate states
precisely these remaining obligations.

The audited theorem remains unchanged at SHA256
`96b9f8717c138dfac7df2a4d1c439392de1a3313c9e57114d2e1cd6f145b90ba`.
