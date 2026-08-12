# The adjacent OR-braid lemma and the K16 three-hole motif

Date: 2026-07-30

## 1. Exact local invariance

Let (A=(a_0,\ldots,a_{L-1})), fix (q<L-1), and replace the adjacent
pair ((a_q,a_{q+1})) by two nonempty masks ((x,y)) satisfying

\[
x\mathbin\lor y=a_q\mathbin\lor a_{q+1}=:u.
\]

Then every interval OR containing both edited cells is unchanged, as is every
interval containing neither.  Consequently the complete coverage delta is
supported on exactly two families:

* intervals ending at (q), and
* intervals starting at (q+1).

This gives an exact (O(L)) delta evaluation (in practice it stops when both
old and new ORs reach (2^{16}-1)).  There is no independence or additive
approximation in this statement.

## 2. Complete enumeration of braids serving a named target

Suppose an edited interval ending at (q) is to have OR (T).  If
(C=a_\ell\lor\cdots\lor a_{q-1}), the necessary and sufficient equations
are

\[
x\subseteq u,\qquad C\lor x=T.
\]

Thus (x) must contain (T\setminus C), may freely choose the bits in
(T\cap C\cap u), and cannot contain a bit outside (T).  Once (x) is
fixed, every nonempty (y) with (x\lor y=u) is obtained by taking all bits
of (u\setminus x) and an arbitrary subset of (x).  The right-prefix case
is symmetric.

Therefore `scratch/search_k16_adjacent_or_braid_blocker_20260730.cpp`
enumerates every OR-preserving adjacent braid which creates an exposed witness
of a named blocker.  Requiring that the witness interval avoid the later
portal position is also exact: such a witness necessarily survives the portal
substitution.  If the blocker was unique and the portal destroys its original
witness, every successful one-braid-plus-portal move is in this catalogue.

The implementation was independently checked in two ways:

* its delta formula agreed with full recounts in 1,000 random toy instances;
* its target-serving algebra agreed with brute force in 151,263 exhaustive
  small instances.

## 3. Frozen append-root census

For the length-12874 append root

* source SHA-256:
  `aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18`;
* sole hole (H=0x287d);
* unique blocker (A=0xa879);
* portal position (6440), with all 16 audited portal values;

the exact one-braid census found:

* 2,558 target-serving braids;
* zero fortifications that preserved every already covered mask;
* 514 fortifications with at most four pre-portal debts, hence 8,224 exact
  portal replays;
* no universal word.

The best replay has three holes.  It is

\[
q=6437,\quad (x,y)=(0xc051,0x8879),\quad
a_{6440}=0x2004,
\]

and its holes are

\[
\{0x4879,0x6879,0x8000\}.
\]

The frozen audit is
`scratch/k16_append0200_adjacent_or_braid_blocker_20260730.audit.json`, and the
materialized replay is
`scratch/k16_append0200_braid_best3_q6437_20260730.word`.

## 4. Why exactly these three holes appear

Before the braid, the relevant local cells are

\[
(a_{6437},a_{6438},a_{6439},a_{6440})
=(0x8000,0x4879,0x2879,0xa069).
\]

The following witnesses are unique:

* (0x8000) at ([6437,6437]);
* (0x4879) at ([6438,6438]);
* (0x6879) at ([6438,6439]);
* (0xa879) at ([6439,6440]).

After the braid and portal:

* (0x287d) is installed at ([6439,6440]);
* the blocker (0xa879) is moved to the external interval
  ([6438,6439]);
* the three nested unique witnesses (0x8000,0x4879,0x6879) disappear.

So the three-hole state is not generic collateral.  It is the exact local
price of relocating the unique blocker across the portal while preserving the
pair OR (0xc879).

## 5. Exact continuation from the three-hole state

From that materialized state, an exact round over every OR-preserving braid
serving at least one current hole exhausted 27,976 candidates.  Its only
one-hole improvement undoes the braid at (q=6437), returning to the sole
(0xa879) phase.  A second exact round exhausted all 3,044 braids serving that
hole and found no universal word.  The audit is
`scratch/k16_append0200_braid_best3_chain_20260730.audit.json`.

Each round is complete for a single hole-reducing adjacent OR braid.  Choosing
only the best state between rounds is a greedy chain and is **not** claimed to
be a complete arbitrary-depth braid search.

## 6. Consequence and current relevance

The lemma remains useful after the authenticated length-12874 upper-bound
word was found: deleting its position 1 gives a length-12873 word with sole
hole (0x2c6d), and its 16 exact closing portals all consume the unique mask
(0xa86d).  Thus the same invariant search applies directly to the final
one-cell gap (12873\le\nu(16)\le12874), with different labels.

## 7. Exact census in the final length-12873 deletion basin

The deletion statement was independently reproduced with a fresh C++ binary.
Among all 12,874 deletions of the authenticated length-12874 word, position 1
(value `0x2800`) is the unique minimum.  The resulting word has

* length 12,873;
* SHA-256
  `a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649`;
* sole hole (H'=0x2c6d).

An exact census of all 3,282,615 one-cell substitutions found minimum debt one
and exactly 16 minimum portals.  They all occur at position 6440 and all
consume the unique blocker (A'=0xa86d).

The complete adjacent-OR-braid blocker census on this new root found:

* 2,430 target-serving braids;
* no safe fortification;
* 8,464 exact portal replays;
* no universal word;
* best three-hole state
  (q=6436,(x,y)=(0x8070,0x8809),a_{6440}=0x046d), with holes
  \({0x2879,0x287d,0x8000}\).

The four-shard exact two-stage search then considered all 529 scoped first
braids against all 16 portals.  Across the shards it replayed 8,464 admitted
first states (4,752 with three holes and 3,712 with four) and exhausted
90,998,096 second braids.  It found no universal word.  The best
non-backtracking states have sole hole (A'=0xa86d).  Their exact one-cell
census has 16 reverse portals at the same position, each consuming (H').
Thus this neighbourhood contains an explicit two-phase cycle

\[
0x2c6d\longleftrightarrow0xa86d,
\]

not a zero-hole state.

For comparison, the exact pure-order census exhausted 4,005,097 relevant
arbitrary swaps, 141,537 contiguous reversals of span at most 12, and 849,112
adjacent block transpositions of span at most 12.  It found no zero and never
raised the blocker multiplicity above one while retaining the original sole
hole.

These are scoped finite no-go results, not a proof that length 12,873 is
impossible.  They identify the requirement on the next move class: it must
leave the adjacent-OR-braid/two-phase neighbourhood or create blocker reserve
through a genuinely larger coupled braid.

## 8. Exact recurring-doublet depth-three census

The smallest non-greedy extension was then exhausted from the best
non-backtracking (A'=0xa86d) phase.  Immediate singleton returns to (H') or
(A') were quotiented out.  At each of the first two layers only a two-hole
signature recurring at least twice in the complete corresponding layer census
was admitted.  The search allowed the full word span and at most six net
edited cells, the maximum support of three adjacent braids.

The exact layer sizes were:

* first layer: 2,916 provider braids, of which 36 give the single recurring
  doublet \({0x2c6d,0x942d}\);
* second layer: 111,360 provider braids, with 6,660 admitted paths and three
  recurring doublets:
  \({0x2c6d,0x9009}\),
  \({0x2c6d,0xa86d}\), and
  \({0x942d,0xa86d}\);
* third layer: 35,201,376 exact provider braids.

No zero-hole word occurs in this depth-three scope; the minimum is one hole.
The frozen audit is
`scratch/k16_upper12874_best_delete_phaseA_braid3_recurring_doublet_20260730.audit.json`
and the driver is
`scratch/search_k16_or_braid_recurring_doublet_depth3_20260730.cpp`.

This closes the first genuinely non-greedy OR-braid chain rather than merely
following the immediate two-phase inverse.  The conclusion remains scoped:
non-recurring intermediate signatures, more than three braids, or a move that
does not preserve each adjacent pair OR are outside the census.

## 9. The position-0 provider plus adjacent-swap family

A new compound move lies outside the recurring-doublet admission rule.  Set
position 0 to `0x0800`, which installs (H'=0x2c6d) but exposes the nested
holes `0x4879` and `0x6879`.  Swapping positions 6435 and 6436 then uses

\[
0x4071\lor0x0879=0x4879,
\qquad
0x4879\lor0x2869=0x6879
\]

to repair that pair.  Independent literal replay leaves exactly

\[
\{0x4671,0x4e71,0x4ef7,0xa879\}.
\]

This mechanism was then exhausted rather than tested only at the displayed
example.  Exactly 128 nonzero position-0 values install the original hole.
For every such value, every one of the 12,872 adjacent swaps was tested, for
1,647,616 exact states.  There is no zero-hole state and the minimum is four.
There are exactly three minimum signatures, each occurring 128 times:

\[
\begin{aligned}
&\{0x146d,0x4879,0x546d,0x6879\},\\
&\{0x4671,0x4e71,0x4ef7,0xa879\},\\
&\{0x4879,0x6879,0x8ce6,0x9ce6\}.
\end{aligned}
\]

The frozen audit is
`scratch/k16_upper12874_best_delete_p0_provider_adjacent_swap_20260730.audit.json`
and the exhaustive driver is
`scratch/search_k16_p0_provider_adjacent_swap_census_20260730.cpp`.
