# The `K17` OPTIMAL28 compact exchange catalogue and exact chronology evaluator

Date: 2026-07-31  
Lane: AD, marked-path-preserving complement rethread  
Status: exact complete finite reduction and replayable evaluator; no feasible
repair, common compiler, or `K17` word is claimed

## 1. Result

Freeze the authenticated contiguous marked path of `4108` rank-nine owners
and its two cross-bank edges.  Release every adjacency internal to the
`20202`-owner complement, while requiring every one of the remaining `20201`
rank-eight lower colours exactly once.

There is a canonical complete catalogue of

```text
eligible complement colours                         20201
off-source exchange columns                        545721
columns including the implicit keep choices       565922
static rank-ten zero rows                              218
columns gaining one of those rows                     6419
support per static row                               10..45.
```

The full catalogue is generated from a `536`-byte authenticated sidecar and
the frozen carrier.  A C++ evaluator independently regenerates all columns,
checks degree balance and one-cycle connectivity, materializes the literal
two-bank zipper, and evaluates:

* the exact signed rank-ten provider delta;
* every rank-eleven and rank-twelve interval provider;
* strict `D2/D3` residence;
* every maximal-envelope cell and exact `D2` replay; and
* preservation of the marked path, both cross edges, and the complete lower
  rank-eight palette.

The empty-selection regression reproduces exactly

```text
D2 bad / D3 bad                        2392 / 2392
maximal-envelope empty / replay bad       0 / 3568
upper holes ranks 10/11/12              1900/911/128.
```

Thus the fixed residual-pair fibre is no longer being searched.  The exact
live finite gate is a nonempty selection from this complete exchange bank
which passes degree, path, residence, ranks `10--12`, and then the actual
common-cap recourse.

## 2. Canonical generation theorem

Rotate the authenticated owner cycle to

\[
 P_1,\ldots,P_a,Q_1,\ldots,Q_b,P_1,
 \qquad a=4108,\quad b=20202,                         \tag{2.1}
\]

where the `P` block is the frozen marked path.  The source rotation is
`21331`.  For every complement-internal source edge
`e_c={a_c,b_c}`, put

\[
 c=a_c\cap b_c,
 \qquad
 A_c=\{i\notin c:c\cup\{i\}\text{ is a complement owner}\}. \tag{2.2}
\]

For each unordered pair `{i,j}` in `A_c`, other than the pair generating
`{a_c,b_c}`, define

\[
 u=c\cup\{i\},\qquad v=c\cup\{j\}.                 \tag{2.3}
\]

The tuple `(c,a_c,b_c,u,v)` is one exchange column: remove `a_cb_c` and add
`uv`.

### Theorem 2.1 (soundness, uniqueness, and completeness)

The construction (2.2)--(2.3) gives every off-source complement Johnson
edge which preserves a source lower colour, exactly once.  Consequently it
is the complete marked-path/cross-edge-preserving lower-rainbow exchange
catalogue.

#### Proof

Both `u` and `v` are rank-nine complement owners containing the rank-eight
set `c`; because they add different coordinates, `u cap v=c`.  Thus `uv` is
a legal Johnson edge of the same lower colour as `a_cb_c`.  Omitting the old
added-coordinate pair makes it off-source.

Conversely, let `uv` be any complement Johnson edge whose colour is a source
complement colour `c`.  Then `u cap v=c`, so uniquely
`u=c union {i}` and `v=c union {j}` for distinct `i,j in A_c`.  The unordered
pair `{i,j}` therefore appears once in (2.3).  Finally an undirected Johnson
edge determines its colour as its endpoint intersection, so two different
colour groups cannot encode the same added edge.  \(\square\)

The exact complement-superset profile is

\[
 |A_c|:\quad3^{15},4^{129},5^{454},6^{1601},7^{3836},
                 8^{6748},9^{7418}.                 \tag{2.4}
\]

Hence

\[
 \sum_c\left({|A_c|\choose2}-1\right)=545721.       \tag{2.5}
\]

Ordering colours increasingly, added coordinates increasingly, and pairs
lexicographically fixes the zero-based column IDs used by the evaluator.

## 3. Exact factor and path rows

Use at most one column for a colour; a colour with no selected column keeps
its source edge.  For complement owner `w`, exact degree preservation is

\[
 \sum_e x_e\bigl(
   {\bf1}_{w\in\{u_e,v_e\}}-
   {\bf1}_{w\in\{a_e,b_e\}}\bigr)=0.                \tag{3.1}
\]

Because the two complement boundary owners have source internal degree one
and every other complement owner has degree two, (3.1) yields one path plus
zero or more disjoint cycles.  If `Q_1` is the boundary owner following
`P_a`, exact one-path connectivity is the rooted final-edge family

\[
 \sum_{f\in\delta_Q(R)} y_f(x)\ge1
 \quad(\varnothing\ne R\subseteq Q\setminus\{Q_1\}). \tag{3.2}
\]

Thus (3.1)--(3.2) are necessary and sufficient for the rethreaded complement
to be one `Q_1`--`Q_b` Hamilton path.  Adding the unchanged marked path and
the two frozen cross edges then gives one owner Hamilton cycle with every
rank-eight lower colour once.

The C++ evaluator checks the final graph directly; it does not rely on a
relaxed proxy for (3.2).

## 4. Exact rank-ten delta and the linear boundary correction

For a valid selected path define

\[
 F_0=P_a\cap Q_1,\qquad
 F_i=Q_i\cap Q_{i+1}\ (1\le i<b),\qquad
 F_b=Q_b\cap P_1,
\]

and the literal nonflat row

\[
 Z=P_1\cdots P_aF_0\cdots F_b.                     \tag{4.1}
\]

### Lemma 4.1 (rank-ten zipper reduction)

The distinct rank-ten targets represented by intervals of `Z` are exactly
the union labels of the linear owner edges

\[
 P_1P_2,\ldots,P_{a-1}P_a, P_aQ_1,
 Q_1Q_2,\ldots,Q_{b-1}Q_b.                         \tag{4.2}
\]

The cyclic closing edge `Q_bP_1` is not included.

#### Proof

Two consecutive marked owners occur literally in `Z`.  For the first cross
edge, `P_a,F_0,F_1` have union `P_a union Q_1`: the new coordinate of `Q_1`
survives in `F_1`, since otherwise `Q_2=P_a`, contradicting simplicity.

For an internal edge `Q_iQ_(i+1)`, the two facets `F_(i-1),F_i` are distinct
rank-eight facets of `Q_i`, hence have union `Q_i`.  The next facet
`F_(i+1)` contains the new coordinate of `Q_(i+1)`, since
`Q_(i+2) != Q_i`; at the right boundary take `Q_(b+1)=P_1`.  Therefore

\[
 F_{i-1}\cup F_i\cup F_{i+1}=Q_i\cup Q_{i+1}.       \tag{4.3}
\]

Conversely, two consecutive facet rows have union at most rank nine.  A
facet-only interval whose union first reaches rank ten therefore contains a
triple in (4.3); extending it without increasing rank preserves that same
edge label.  An interval meeting the marked block either contains two
consecutive marked owners or reaches rank ten at the displayed first-cross
triple.  These exhaust the linear row.  \(\square\)

Let `L_Z^0(S)` count the source edges in (4.2) with union `S`.  By Lemma 4.1,
rank-ten completeness after exchange is exactly

\[
 L_Z^0(S)+\sum_e x_e
 \left({\bf1}_{u_e\cup v_e=S}-
       {\bf1}_{a_e\cup b_e=S}\right)\ge1.           \tag{4.4}
\]

This is the exact additive provider row.  Counting the cyclic closing edge
would be unsound: its label `88314` has cyclic owner-edge multiplicity two
but only one canonical linear-zipper provider in the incumbent.

Each column has one gain label.  The `218` static holes have a disjoint union
of `6419` gaining column incidences, with `10--45` per row.  Therefore every
solution covering all `218` selects at least `218` columns.  This is only a
floor; losses in (4.4), degree balance, and connectivity can force more.

## 5. Why ranks eleven and twelve are evaluated after connectivity

Ranks eleven and twelve are not sums of independent column deltas.  Their
witness intervals concatenate facet rows along the selected complement path,
whose order is determined jointly by all chosen edges.  The exact procedure
is therefore:

1. enforce colour uniqueness, (3.1), and one-cycle connectivity;
2. orient the complement from the frozen `P_aQ_1` edge;
3. materialize `Z` by (4.1); and
4. for each start position, accumulate unions until their rank exceeds
   twelve, recording every rank-ten, eleven, and twelve mask encountered.

This scan is finite and small.  All entries of `Z` are distinct rank-eight
or rank-nine masks.  If an interval union has rank at most twelve, every row
in it is an eight- or nine-subset of one twelve-set, so its length is at most

\[
 {12\choose8}+{12\choose9}=495+220=715.             \tag{5.1}
\]

Thus the full scan takes at most `24311*715` interval extensions.  The empty
selection actually takes `136379` extensions before rank exceeds twelve.
The evaluator exports exact hole, gained, and lost mask lists separately at
each of ranks `10,11,12`.

Ranks `13--17`, currently complete, still require the same full interval
preservation check for any proposed solution; the present evaluator is
deliberately the first-three-shadow master requested here.

## 6. Residence and exact inversion

For the materialized row `Z=(Z_0,...,Z_(L-1))`, define its maximal `D2`
inverse

\[
 E_p=\bigcap_{\max(0,p-2)\le i\le\min(L-1,p)}Z_i
 \qquad(0\le p<L+2).                               \tag{6.1}
\]

Exact inversion is equivalent to

\[
 E_p\ne\varnothing\quad\text{for every }p,
 \qquad E_i\cup E_{i+1}\cup E_{i+2}=Z_i
 \quad(0\le i<L).                                  \tag{6.2}
\]

Equivalently, every strictly internal positive coordinate run of `Z` has
length at least three, together with envelope nonemptiness.  The evaluator
checks both (6.1)--(6.2) and the run ledger.  It also checks the derived `D3`
row; after (6.2) succeeds its residence condition is redundant, but the
separate count is retained as an audit invariant.

This is a whole-row test, including both marked/complement interfaces.  A
complement-only automaton would be insufficient.

## 7. Reproducible artifacts

Primary inputs and compact catalogue:

```text
scratch/k17_opt28_connected_owner_cycle_20260731.word
  SHA-256 a736ef9def43415ce54e6ca72abf5718e922e9d39de336b463dce7af3a1073aa

scratch/ad_k17_opt28_marked_exchange_seed536_20260731.bin
  bytes 536
  SHA-256 3a7dee9ab6c159d5b846787d504fc1c92f7946a6ce37f28cedaa3b191b713718
  embedded 436-byte static-ID SHA-256
    5a2813501aedd784a5d50d8263b9ebe591af6262d500b2b4da342980397d3125
```

The seed header authenticates the carrier SHA, dimensions, source rotation,
marked length, catalogue size, and the sorted `218` rank-ten target IDs.
The evaluator regenerates the catalogue canonically; the seed does not trust
a precomputed provider list.

Redundant direct streams and metadata:

```text
scratch/ad_k17_opt28_marked_exchange_catalogue_20260731.bin
  bytes 2684196, SHA-256 9ccf24540e96f90e210b5f3538735e29d08e3ef0a42fb3e02026a5c67791526b
scratch/ad_k17_opt28_marked_exchange_static218_20260731.bin
  bytes 27448, SHA-256 acad22726208d692d35a09ff049af72a7aa30da0468f089dc335437ec5fff5a2
scratch/ad_k17_opt28_marked_exchange_catalogue_20260731.meta.json
  SHA-256 ccc6519a0f05ec051a04d65c5da8ecbff814397ca87580a12f3b9252851dfced
  payload d4bf1843529f4df55f345c3527fa50608718c291301da50f5529f93ca8a355b6
```

Exporter, evaluator, and empty-selection regression:

```text
scratch/build_ad_k17_opt28_compact_exchange_catalogue_20260731.py
  SHA-256 142b85450187aedfa1b690212ee1846d93327300fd6bd3e1b2ecfb218b57e29d
scratch/evaluate_ad_k17_opt28_marked_exchange_20260731.cpp
  SHA-256 7848bd556e41ec3c9ad515e547f205675c895b41904c1751259d4cb859407267
scratch/ad_k17_opt28_marked_exchange_incumbent_20260731.selection
  SHA-256 87cf4d579c53eafe75751220347d2143bb21b9adffee09e609ed93b49861a001
scratch/ad_k17_opt28_marked_exchange_incumbent_20260731.eval.json
  SHA-256 f68952265e751c65934413997d7a24c980bc2fb4971d8a83a8442bf579f60cf4
```

The evaluator has no solver dependency.  A selection is a whitespace list of
zero-based column IDs.  It rejects colour conflicts and any graph which is
not degree two and connected before assigning chronology-dependent claims.
The baseline replay command is

```sh
clang++ -std=c++20 -O2 scratch/evaluate_ad_k17_opt28_marked_exchange_20260731.cpp -o /tmp/k17_exchange_eval
/tmp/k17_exchange_eval \
  scratch/k17_opt28_connected_owner_cycle_20260731.word \
  scratch/ad_k17_opt28_marked_exchange_seed536_20260731.bin \
  scratch/ad_k17_opt28_marked_exchange_incumbent_20260731.selection \
  /tmp/k17_exchange_eval.json
```

## 8. Exact remaining boundary

Proved and implemented:

* a complete, canonical `545721`-column marked-preserving exchange bank;
* an exact `6419`-incidence projection for all `218` fixed-skeleton rank-ten
  holes and the floor `|X|>=218`;
* necessary-and-sufficient degree and one-path conditions;
* the boundary-correct exact signed rank-ten row;
* exact materialized rank-eleven/twelve, residence, envelope, and replay
  evaluation; and
* a compact authenticated representation plus literal regression.

Unproved:

* existence of a nonempty integral selection passing all these rows;
* preservation/repair of ranks `13--17` in such a selection;
* feasibility of the actual rank-three common-cap clutter after `Z` is
  repaired; and
* a literal word of length `24313` or `nu(17)=24313`.

The common-cap phase must be built from the repaired row's actual maximal
envelope.  The incumbent envelope cannot be frozen because its replay already
fails in `3568` rows.
