# The `K17` OPTIMAL28 packet path extends to one owner factor, and the remaining nonflat debt is explicit

Date: 2026-07-31  
Status: exact connected owner/lower-`q1` factor and literal nonflat-row
audit; residence, the first three upper shadows, the common cap, and a
`K17` word remain open

## 0. Result

The complete radius-one Steiner construction now passes both topology rows.

* The fixed marked bank is one path through all `106` marked macro
  components and `28` optional components.  It uses `133` distinct pure
  rank-nine owners, expands to `4108` distinct owner tokens, and has zero
  strict `D2<3` or `D3<4` run debt.
* Conditioning on that path leaves `4872` old-only rank-nine owners and
  residual rank-eight half-demand `9744`.  Exact max flow saturates all
  `9744` incidences.
* Flow attempt `86` is already connected: its quotient has one component of
  size `4872`, so no incidence rectangle is needed.
* Adding the `1430` macro objects and all `5005` pure-owner objects gives one
  connected degree-two factor.  Literal expansion is a cycle of all
  `24310=binom(17,9)` rank-nine owners exactly once.  Its consecutive
  intersections enumerate all `24310=binom(17,8)` rank-eight colours
  exactly once.

Thus middle ownership, the complete lower-`q1` palette, marked-bank
residence, and topology coexist at equality scale.  This is a genuine new
carrier theorem, but not yet an optimal word.

Cutting the cycle at its two marked/complement crossings gives a marked
owner path `P` of length `4108` and a complementary owner path `Q` of length
`20202`.  Its canonical nonflat depth-two row

\[
                 Z=P\,F(Q)
\]

has `4108` rank-nine entries and `20203` distinct rank-eight facet entries.
The facet entries together with the `4107` internal turns of `P` partition
the complete rank-eight layer.  However the exact remaining debt is

```text
strict D2 bad runs / strict D3 bad runs       2392 / 2392
maximal-inverse empty cells                              0
maximal-inverse replay mismatches                     3568
upper holes at ranks 10,11,12,13+           1900,911,128,0.
```

Consequently the construction has crossed the topology barrier.  The live
gate is now exactly a rethread of the complementary incidence factor which
preserves the fixed marked path and lower palette while repairing the
depth-two run condition and the first three upper shadows.  All upper ranks
`13` through `17` are already complete.  Only after this rethread is fixed
does the guarded common-cap matching become the final lower-compiler row.

## 1. Connected conditioned completion

Let

\[
 \mathcal T={ [15]\choose8},\qquad
 \mathcal U={ [15]\choose9}.
\]

The six-swap Pascal macro graph is a linear forest on `mathcal T` with
`1430` edges.  The OPTIMAL28 packet path adds `133` distinct labelled
`mathcal U` edges and remains a forest.  Its exact ledger is

```text
fixed forest components                         4872
unused pure-U owners                            4872
residual rank-eight half-demand                 9744
port demand profile                  0^691 1^1744 2^4000.
```

The residual incidence network has source capacity two at every unused
owner, unit owner--facet arcs, and the displayed port demands.  The saved
assignment saturates it.  Independent replay checks:

1. every unused owner selects two distinct rank-eight facets;
2. every port receives exactly its residual demand;
3. no fixed packet or macro incidence is changed; and
4. after contracting the fixed forest, all `4872` components lie in one
   connected component.

Since the completed graph has degree two at every port, connectedness makes
it one cycle.  Internal marked-path ports already have fixed degree two, so
the complement meets the marked path only at its two endpoints.  Hence the
marked bank is automatically a cyclic interval.

## 2. Literal owner-cycle expansion

Every macro edge carries its stored A/X/Y owner path.  Orient a macro block
according to the port at which the quotient cycle enters it.  Every pure-U
edge carries its singleton owner.  Traversing the connected quotient and
expanding its objects gives a cyclic word `C` with

\[
 |C|=\sum_{e\in E_{\rm macro}}|W(e)|+|\mathcal U|
     =19305+5005=24310.
\]

Literal replay proves

\[
 \{C_i\}={ [17]\choose9},\qquad
 \{C_i\cap C_{i+1}\}={ [17]\choose8},
\]

with multiplicity one in both equations.  In particular `C` is a
lower-rainbow Johnson cycle.  The raw adjacent-union palette of this cycle
is not exact: it has `17548` distinct rank-ten unions, `1900` holes, total
excess `6762`, and maximum load `6`.  This raw palette is diagnostic; the
final upper witnesses belong to the nonflat row below.

## 3. The exact nonflat zipper

Write the oriented cycle as

\[
             P_1,\ldots,P_a,Q_1,\ldots,Q_b,P_1,
 \qquad a=4108,\quad b=20202,
\]

where `P` is the fixed marked packet path.  Define

\[
\begin{aligned}
F_0&=P_a\cap Q_1,\\
F_j&=Q_j\cap Q_{j+1} &&(1\le j<b),\\
F_b&=Q_b\cap P_1,
\end{aligned}
\]

and put

\[
             Z=(P_1,\ldots,P_a,F_0,\ldots,F_b).       \tag{3.1}
\]

Then `|Z|=24311=W+1`.  Because the owner cycle is lower-rainbow, the
`20203` facets `F_j` are distinct.  The `4107` internal colours
`P_i intersection P_(i+1)` are also distinct, disjoint from the facets, and
together the two families enumerate all rank-eight targets.

Moreover

\[
 DZ=(P_1\cup P_2,\ldots,P_{a-1}\cup P_a,
      P_a,Q_1,\ldots,Q_b).                           \tag{3.2}
\]

Thus all rank-nine owners are displayed between the direct `P` bank and
the first derivative of the facet rail.  This is the exact two-bank
rank-exchange identity; it is why connectedness of the owner factor was the
right topology target.

## 4. Exact residual gate

For a proposed depth-two row, maximal inversion is coordinatewise.  The
maximal preimage has length `W+3=24313`; every one of its cells is nonempty
for the current `Z`.  Nevertheless `3568` rows fail replay, equivalently
the coordinate traces of `Z` contain `2392` strictly internal positive runs
of length below three.  The adjacent-union row has the corresponding `2392`
strict runs below four.

By the deep-interval identity, every upper target is determined entirely by
unions of consecutive cells of `Z`.  Exhaustive changing-union replay uses
`593871` interval extensions and gives

\[
\begin{array}{c|rrrrrrrr}
\text{rank}&10&11&12&13&14&15&16&17\\ \hline
\text{holes}&1900&911&128&0&0&0&0&0.
\end{array}
\]

Therefore no downstream choice of a smaller common cap can repair these
rows: residence and ranks `10`--`12` must be fixed in the owner/facet
chronology itself.  Conversely, once they are fixed, all higher upper
shadows are already complete and are immutable under the lower cap.

The rank profile leaves positive scalar compiler room.  With `a=4108`, the
exact short-cell slack is

\[
                         7401-a=3293.
\]

This is only capacity.  A final construction must preserve one common
rank-three cap obstruction state, or satisfy the stronger permanent-host
Hall condition, while rethreading the complement.

## 5. Provenance and scope

Primary connected assignment:

```text
scratch/ad_k17_opt28_residual_connected_bflow_20260731.json
SHA-256 b3cbb0663409463cb24a2ed78db154cc88a042b633e979cba3506ba74e610ef6
payload a117a304f277a7746405814786fd3f593dffe5073443431582eb711641e7319a
```

Independent reverse/forward degree and connectivity replay:

```text
scratch/audit_ad_k17_opt28_residual_connected_bflow_20260731.py
SHA-256 a6f306a8ac9885cf6556b2746d516f831b53bb1e93e8e8dd4a996a298a0d6c01
scratch/ad_k17_opt28_residual_connected_bflow_20260731.audit.json
SHA-256 95e8b27426d9ac62ccbe490a55c2a1e256e63faa1bc561a5d5a0462380870cfd
payload 05d8685b325abc3311732f032becf2c7f158776a83c6cb36f16fca56d23056f9
```

Literal expansion and nonflat audit:

```text
scratch/materialize_k17_opt28_connected_owner_cycle_20260731.py
SHA-256 e5434ae453e8dd7a9373d2a5b50379d930554fb22560c37edf1bee04611ee89c
scratch/k17_opt28_connected_owner_cycle_20260731.word
SHA-256 a736ef9def43415ce54e6ca72abf5718e922e9d39de336b463dce7af3a1073aa
scratch/k17_opt28_connected_owner_cycle_20260731.audit.json
SHA-256 f28924a629a6e858571119538639adf3ecbd4d186c1014a475e353fe5b719280
payload 6988b37a414a516e4645f81b1dac87618c1949bc636a1190462c5f8520639d7a
```

What is proved is one connected owner/lower-`q1` factor, exact marked-bank
contiguity and residence, the complete lower palette in the nonflat row,
and the precise finite residual above.  What is not proved is a replayable
depth-two row, upper completeness at ranks `10`--`12`, a common-cap lower
matching, a length-`24313` word, or `nu(17)=24313`.
