# K17 J7 higher-shadow lazy DFA/CEGAR and exact q1-forest scope

Date: 2026-08-01  
Lane: AD  
Status: exact theorem, O3 implementation, selected-assignment replay, and
independent audit.  This note does **not** construct a resident K17 carrier,
a common compiler, or a length-24313 word.

## 0. Exact outcome

The 21,778 rank-11-and-higher clauses must not be appended eagerly to the
2.2-million-variable global-q1 master.  The smallest sound integration is
nested:

1. the outer master selects cuts, sockets, provider seams, and macros;
2. its assignment is materialized into an exactly ordered **block forest**;
3. a separate chronology master chooses block orientations, literal
   connector words, and one linear/cyclic order;
4. an `O(17N+8N log 8)` fixed-word oracle replays all higher targets; and
5. a missing target contributes a certified labelled-DFA frontier clause to
   the chronology master.

A rank-11+ miss cannot in general be projected directly to a clause over the
outer q1 variables, because those variables do not choose the order of its
blocks.  This is not a technical omission: the same selected blocks can
cover or miss a target in different orders.

The available AD J7 regression was independently replayed SAT and
materialized.  Its exact selected data are

```text
71 sockets, 1793 provider seams, 1903 cuts,
macros J1 and joint-two-block J7,
6765 cut pieces, 4680 final linear blocks.
```

All 24,310 rank-nine owners occur exactly once, every within-block adjacency
is Johnson, and the complete upper-q1 support is present.  It is not an
upper rainbow: its 19,630 internal edges cover the 19,448 rank-ten targets
with excess 182.  The load histogram is

```text
load 1: 19280; load 2: 157; load 3: 9; load 4: 1; load 5: 1.
```

The exact internal higher-hole vector, at ranks 11 through 17, is

```text
1350, 777, 151, 5, 0, 0, 0.                         (0.1)
```

Thus all ranks 15--17 are already internal to blocks and only 2,283 physical
targets remain chronology-dependent.  A wholly separate naive all-interval
implementation reproduced (0.1) set-for-set.

This outer assignment is nevertheless not a resident carrier.  Exactly 245
blocks contain at least one boundary-independent short positive run; the
length-1/2/3 run counts are

```text
17, 114, 159.                                        (0.2)
```

Those 290 runs cannot be repaired merely by ordering the blocks.  The
residence master must reject or rethread them upstream.

## 1. Exact first-arrival oracle

Let

\[
                 A=A_0A_1\cdots A_{N-1}
\]

be a linear word of subsets of a `k`-set.  For a start `i` and coordinate
`c`, put

\[
 \tau_i(c)=\min\{j\ge i:c\in A_j\},                 \tag{1.1}
\]

with value infinity when no such `j` exists.

### Theorem 1.1 (first-arrival interval-OR enumeration)

For every `i<=j`,

\[
 \bigcup_{p=i}^{j}A_p
  =A_i\cup\{c\notin A_i:\tau_i(c)\le j\}.           \tag{1.2}
\]

Consequently, as `j` increases, the interval OR changes only at the grouped
finite values among the `tau_i(c)` with `c` absent from `A_i`.  Starting
from `A_i`, adjoining all coordinates having each next equal arrival time
enumerates every interval-OR value from start `i` and no other value.

If every `A_i` is a rank-nine subset of a 17-set, there are at most eight
changes per start and at most seven changes of rank at least eleven.  The
whole upper deck is therefore computed in

\[
                   O(17N+8N\log8)                   \tag{1.3}
\]

time and a `2^17` target bitset, with at most `8N` noninitial events.

For a cyclic word, duplicate the word and for start `i` retain arrivals
strictly before `i+N`.  This enumerates exactly the intervals making at most
one lap.  A cyclic scan is invalid for a linear path and is not licensed
before a cycle's opening cut has been selected.

#### Proof

A coordinate already in `A_i` belongs to every interval starting at `i`.
For `c` absent from `A_i`, it belongs to `OR(A_i,...,A_j)` exactly when its
first occurrence after `i` is at most `j`.  This proves (1.2).  Between two
successive finite first-arrival times the right-hand side is constant, and
at an arrival time exactly the grouped arriving coordinates are added.
This proves exact enumeration.

A rank-nine mask omits eight of the 17 coordinates, proving the event bound.
Reverse next-occurrence arrays cost `17N`; sorting at most eight arrivals at
each start gives (1.3).  In a cycle, every interval of at most one lap is an
interval in the doubled word with endpoint below `i+N`, and the converse is
immediate.  QED

### Literal source scope

For a depth-`h` owner row

\[
       T_i=\bigcup_{j=i}^{i+h}E_j,
\]

the identity

\[
       \bigcup_{i=a}^{b}T_i=\bigcup_{j=a}^{b+h}E_j  \tag{1.4}
\]

makes the owner oracle exact for source intervals of length at least `h+1`.
Short source intervals of length at most `h` are not represented.  A
construction certificate must either scan the actual source word or add
the short-source provider arcs explicitly.  An owner-only UNSAT result is
therefore only a long-witness no-go.

## 2. Exact outer-assignment materialization

Fix the hash-bound outer assignment and the full provider/socket catalogues.
Split every original SCD component at every selected cut.  Call the resulting
maximal intervals **cut pieces**.

For a selected provider occurrence, its declared left and right ranges and
orientations identify two seam-facing cut pieces.  The provider is the
directed edge from the oriented left piece to the oriented right piece.
The endpoint-capacity clauses give indegree and outdegree at most one.  Once
directed cycles are rejected, these edges uniquely concatenate their pieces
into directed paths.

A socket block is, literally,

```text
oriented left-state cut piece,
facet_positions in the stored order,
oriented right-state cut piece.
```

The field `child_colours` is a cut-casualty ledger, not the created edge
deck, and is not used as a delivery certificate.  The actual owner word is
replayed instead.  Each selected macro is expanded using the registry bound
to the builder hash.  Every cut piece unused by a provider, socket, or macro
remains a base block.

### Theorem 2.1 (deterministic block-forest decoder)

Suppose the following checks pass:

1. every declared provider range lies in the reconstructed seam-facing cut
   piece and replays its stored endpoints;
2. provider indegree/outdegree are at most one and no provider cycle occurs;
3. each socket and macro claims whole cut pieces in its literal order;
4. distinct blocks claim disjoint cut pieces; and
5. all unclaimed cut pieces are retained.

Then the resulting blocks partition the original owner occurrences exactly,
and every interval reported by the block oracle is a literal interval in a
selected physical block.  Reversal of an otherwise unoriented leftover
block does not alter its internal interval deck.

#### Proof

The selected cuts partition each original component.  Conditions 1 and 2
make provider composition a disjoint collection of uniquely ordered paths
of whole pieces.  Conditions 3 and 4 make the socket and macro words disjoint
unions of remaining whole pieces.  Condition 5 then assigns every piece
exactly once.  Therefore every owner occurrence appears once.  The stated
order inside each nontrivial block is literal by construction, so all of its
intervals are literal.  Reversal bijects intervals by reversing endpoints
and preserves their unions.  QED

For the selected regression the exact piece ledger is

```text
provider paths: 3071 pieces and 1793 joins, hence 1278 paths;
sockets:         350 pieces in 71 blocks;
macros:           16 pieces in 3 blocks (J1, J7-J6, J7-fusion);
base:           3328 singleton path-block entries;
total:          6765 pieces in 4680 blocks.
```

An independent audit checked every socket against its state orientations and
facet order, every provider edge against its selected target, and every cut
piece against the emitted forest.  There are no partial-piece claims.

## 3. Exact selected-forest census

Because all 4,680 blocks are linear, their number of internal Johnson edges
is exactly

\[
                24310-4680=19630.                    \tag{3.1}
\]

Literal replay gives:

| row | occurrences | distinct | holes | maximum load |
|---|---:|---:|---:|---:|
| upper q1, rank 10 | 19,630 | 19,448 | 0 | 5 |
| lower q1, rank 8 | 19,630 | 18,332 | 5,978 | 3 |

The lower holes in this table are not automatically word defects: the lower
compiler can use other source intervals.  The table is only the exact edge
deck of the owner forest.

The higher internal census is:

| rank | total targets | internal distinct | internal holes |
|---:|---:|---:|---:|
| 11 | 12,376 | 11,026 | 1,350 |
| 12 | 6,188 | 5,411 | 777 |
| 13 | 2,380 | 2,229 | 151 |
| 14 | 680 | 675 | 5 |
| 15 | 136 | 136 | 0 |
| 16 | 17 | 17 | 0 |
| 17 | 1 | 1 | 0 |

The five rank-fourteen obligations are, in decimal,

\[
        122365,125823,127998,130041,130429.           \tag{3.2}
\]

If one nevertheless expanded the missing-set DFA eagerly only on these
2,283 holes, the raw state count would be

\[
 1350\cdot68+777\cdot300+151\cdot1094+5\cdot3474
   =507464.                                           \tag{3.3}
\]

The fixed-word oracle needs none of these state variables.

The selected AD resource named `J7` is itself two blocks.  Its eleven-owner
J6 block contributes internal higher counts `(9,8,6,5,1,0,0)` and its
three-owner fusion contributes the additional rank-eleven mask `31358`.
Thus the union of their internal decks is

\[
                         (10,8,6,5,1,0,0).            \tag{3.4}
\]

No cross term between these blocks is credited, because no literal connector
or order between them was selected.

## 4. Labelled-DFA frontier cuts

Let `G=(V,E)` be any finite transition graph for one target `U`.  Add a
supersource `s` and supersink `t`.  Multiple possible starts are arcs out of
`s`, and accepting states have arcs to `t`.  Every conditional edge `e` has
one exact positive activation atom `lambda(e)`; unconditional edges have
label `top`.  Different edges may share one label.

For assignment `a`, retain the unconditional edges and the edges whose
labels are true.  It suffices for cut soundness that every intended literal
`U`-accepting chronology projects to an `s--t` path.  Exact equality of paths
and chronologies is required only if reachability itself is used as a SAT
acceptance test.

### Theorem 4.1 (labelled reachable-frontier clause)

Let `a0` be an incumbent with no `s--t` path, and let `R` be the vertices
reachable from `s` under `a0`.  Put

\[
 C=\{\lambda(e):e\in\delta^+(R),\lambda(e)\ne\top\}, \tag{4.1}
\]

deduplicating shared labels.  Then every label in `C` is false in `a0`, and

\[
                         \bigvee_{c\in C}c            \tag{4.2}
\]

is a valid incumbent-violated clause.

More generally, if deleting every transition carrying a label in `B`
disconnects `s` from `t`, then `OR(B)` is valid.  Starting with `C`, greedily
remove `b` whenever deletion of the other current labels still disconnects
`s,t`.  The output is inclusion-minimal.  For every retained `b`, one
`s--t` path after restoring `b` certifies minimality.

#### Proof

No unconditional or incumbent-true edge leaves `R`, by reachability closure.
Thus all labels in (4.1) are incumbent-false.  Every `s--t` path must first
leave `R` and hence use an edge whose label belongs to `C`, proving (4.2).

For general `B`, an accepting path avoiding all labels in `B` would survive
their deletion, contradicting disconnection.  Hence it uses at least one
label in `B`.  The greedy deletion maintains this invariant.  At termination,
restoring any one retained label reconnects `s,t`, which proves
inclusion-minimality and supplies the claimed witness path.  QED

No multiplicity coefficient appears when one atom labels several edges.
Minimum-cardinality labelled separation is NP-hard: use one internally
disjoint `s--t` path for each set of a hitting-set instance and label its
edges by the elements of that set.  Inclusion-minimality, not cardinality
optimality, is therefore the appropriate inexpensive guarantee.

### Certificate and CNF interface

A proof-carrying semantic cut contains:

1. target `U` and mode `owner-long` or `source-exact`;
2. hashes of the transition catalogue, label map, and incumbent;
3. the sorted labels `B`;
4. a reachable-set bitset containing `s`, excluding `t`, and closed under
   every unconditional or non-`B` edge; and
5. optionally one restoring path for each retained label.

For a conjunctive transition condition `phi=AND_i ell_i`, introduce a lazy
Tseitin atom `a_phi` with

\[
 (\neg a_\phi\vee\ell_i)\quad\hbox{for every }i,
 \qquad
 (a_\phi\vee\neg\ell_1\vee\cdots\vee\neg\ell_s).    \tag{4.3}
\]

The frontier cut then uses `a_phi` once.  A final DRAT/LRAT proof certifies
UNSAT of the augmented CNF.  It does not by itself prove that the externally
added semantic cuts follow from the original q1 formula; the independent
frontier checker supplies that proof layer.

The executable regression has four vertices, four edges, and shared global
label universe `{10,20,30}`.  Under the all-false assignment it emits the
inclusion-minimal clause

```text
10 20 0
```

with closed reachable set `{0,1}` and one restoring path for each literal.

## 5. The smallest sound K17 integration

Keep the outer q1 master unchanged.  For a resident decoded forest create an
inner master containing only:

* allowed orientation variables for blocks;
* one activation atom per legal directed connector word;
* first/last or cycle-root variables;
* indegree/outdegree and path/cycle connectivity constraints; and
* literal short-source connector choices when applicable.

Do not add any rank-11+ row initially.  On each candidate chronology:

1. expand the exact owner and source-letter words;
2. run the first-arrival oracle on owners and the exact short-source deck;
3. accept only after literal replay of all 21,778 physical targets;
4. for a miss, add either a full incumbent chronology no-good or a certified
   labelled-frontier cut from Theorem 4.1; and
5. continue until SAT or proof-producing UNSAT.

If the selected `N-1` adjacency/connector atoms determine one literal path,
the clause saying that at least one of those incumbent-true choices changes
is always a sound, though long, fallback.  The frontier theorem can replace
it by an inclusion-minimal positive separator whenever the candidate graph
supports one.

The transition graph may overapproximate legal chronologies: failure of
reachability remains a sound no-go because every legal accepting chronology
must project to a path.  An accepting graph path is then only “no cut”; final
acceptance still requires literal replay.  To avoid CEGAR stalling, the
incumbent-active graph should be exact enough to reflect the incumbent word.

If the inner chronology problem is UNSAT for one outer forest, blocking the
entire outer assignment is automatic.  A smaller Benders cut on only some
outer socket/provider/cut variables is valid only after an independent
dependency-core proof.  A single missing target from one arbitrary ordering
does not justify such an outer cut.

## 6. Model-provenance separation

The tested SAT regression is

```text
/home/amodo/or15/work/ad_k17_j7_higher_cegar_20260801
```

with source/CNF/SAT hashes

```text
3f3bbc6cf7ef64c4458d44d7302d7f932d91d0474acd905505b5bdf42c68641c
a7e9313b08305449c343495c1f381d78c3902272933277c8bb83803b984e7d60
005551022253bfc9fa6baab3c054b31526f542f50f055c7db5f6cd34925f1964
```

and a complete 10,758,301-clause assignment replay.  This builder has no
chronology, DFA, successor, subtour, or rank-11+ variables.  Its filename
must not be used to claim otherwise.

It is also weaker than the separately corrected H2 model: the AD variable
named `J7` jointly selects the disjoint J6 and fusion blocks and does not
force the target-28926 socket.  In the corrected H2 model, `J6` and `J7` are
separate variables and `J7` means only the three-owner fusion.  Macro names
are therefore decoded only together with the source/CNF hash.  The
13-owner concatenation obtained by silently merging the two is a third
object and has a known internal residence defect; it was not used here.

## 7. Artifacts and exact remaining boundary

Canonical implementation hashes:

```text
forest materializer/oracle source
  8ce0df75aa01b1d301f414bd684e163ecfdc9f16822d93b263afa84c60b84987
O3 binary
  1cb5d7952d30fcd5288bceaf645c6d8149c3ff92b459dd9469ea7d7996dc9ac5
selected forest
  6582bd405d7fb492b812844661de01a09f502735236823461cd26b714c7b5a53
missing-target TSV
  02dd495b0ceff938f93414c546769860196083d2e4ced2dcab613133156fa98a
forest audit
  a10f6ad0aa4eb4b9571ea71c224fab6ed5688b222510a0c31dcbd2cd44e18f0b
independent replay source / binary / audit
  37305b05777e08eaad1385f7d335f50254e1cf1ec8da1fe366831177a7f672de
  d997a52627e70f9622390358d0a90eae56897e7ba3aa7b75ca4885d5f12ebd56
  6926f1e7afc3e3f4f84596571f5e56be1d7cfe9d35d7fb64e32f2361283b48f2
labelled-frontier source / binary
  b0dc8606d3111b7aa76b838c6833cd4b7bf92aad89b0e114c0c6169cab69327a
  c2615848d444887f83aad356fe042144b05797d0638bfc1d96672538864a68da
frontier cut / certificate / audit
  a5e37e2f2c8f5db0c5f46565881ba4ed6c99e5952730ac82d860efaf2bf73adc
  ebabccd6b9d4bd4c3315553bdee1f88c7fbad3d7e67b181c7a24cf0d882aa43d
  86ebe2253e6a57564ec2c8795ba0370d6cb0b50b6529a748d320d152a7d54b8b
```

Local package:

```text
scratch/ad_k17_j7_higher_shadow_cegar_20260801/
```

The proved boundary is now exact.  The higher-shadow oracle and semantic-cut
mechanism are complete.  The selected outer assignment still fails
residence by (0.2), has no inter-block chronology, leaves 2,283 internal
higher obligations to that chronology, and has not supplied the short-source
deck or common lower compiler.  No K17 equality claim follows.
