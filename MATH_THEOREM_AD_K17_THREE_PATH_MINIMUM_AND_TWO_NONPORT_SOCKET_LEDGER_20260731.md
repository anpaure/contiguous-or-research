# The frozen `K17` clean-atom bank has exact path number three and two non-port socket obligations

Date: 2026-07-31  
Status: exact finite theorem in the frozen clean-atom/pure-`U` connector
catalogue, with solver-free literal and port replay; the two complementary
sockets, residual flow, palettes, deep shadows, and common cap remain open

## 0. Result

Split the frozen `1430`-macro port forest at every macro junction whose
literal concatenation creates a strict depth-two positive run shorter than
three.  This gives `1144` residence-clean atoms.  Exactly `106` atoms contain
one of the `108` forced nonflat macros and are mandatory.

Allow a directed connector from one oriented mandatory atom to another to
contain zero, one, or two optional clean atoms, with a pure rank-nine old-
coordinate owner between consecutive atoms.  All optional atoms and all
pure owners used by a path cover must be distinct.

In this exact catalogue:

```text
clean atoms                                      1144
mandatory atoms                                   106
direct/one-optional candidates                   3034
two-optional candidates added                    1706
total directed candidates                        4740
orientation-forced endpoint atoms                   6
minimum number of paths                              3
attaining mandatory path lengths                19,2,85
optional atoms used                                 89
pure-U owners used                                 192
literal owner-token path lengths              898,78,4834
```

The lower bound three is not a SAT artefact and is not confined to bridges
of optional depth at most two.  Each of the six exceptional mandatory atoms
has, in its forward orientation, a length-two suffix in one new tag
coordinate.  Every pure `U` owner has both new tag bits zero, so the first
connector immediately closes that suffix as a forbidden strict run.
Reversal turns it into the symmetric forbidden prefix.  Thus every such
atom is an endpoint in **every** path made from pure-`U` connectors and
arbitrarily many clean optional atoms.  Six forced endpoints require at
least three paths.

The saved resource-disjoint cover attains three.  Its three literal words
can be ordered `0,2,1`, without reversal, and concatenated directly into a
`5810`-token word of `5810` distinct rank-nine owners, having no strict
internal D2 run below three and no strict internal D3 run below four.  The
two direct joins are not Johnson joins and
are not pure-`U` port connectors.  Consequently the exact remaining fusion
debt of this selected bank is **two complementary non-port sockets**, not
`107` independent phase boundaries and not six external optional bridges.

This is a reduction, not a `K17` construction.  The two sockets still have
to be literalized together with the complementary facet phase, and the
remaining port flow, palettes, upper/deep shadows, and common compiler cap
must all survive.

## 1. Clean atoms and the connector language

An atom is a nonempty path of frozen macro edges.  Its literal owner word is
the concatenation of the corresponding oriented `A/X/Y` macro words.  It is
maximal subject to having no strict internal positive run shorter than
three.  The deterministic split has `1144` atoms, of which `106` meet the
forced macro set.

For an atom `P`, write `h(P),t(P)` for its two rank-eight port colours.  A
pure-`U` transition from oriented `P` to oriented `Q` is possible only when

\[
             u=t(P)\cup h(Q),\qquad |u|=9.                 \tag{1.1}
\]

The literal transition is `P,u,Q`.  A candidate is retained only if its
full literal word has no strict internal positive run below three.  The
certificate uses candidates with zero, one, or two optional atoms.  Their
selected profile is

```text
zero optional atoms per candidate                  18
one optional atom per candidate                    81
two optional atoms per candidate                    4
```

There are `103=106-3` selected candidates, `89` selected optional atoms,
and `192=103+89` selected pure owners.  Both selected resource lists are
injective.

## 2. The arbitrary-depth forced-endpoint lemma

Let `x,y` be the two new coordinates.  In the canonical orientation the six
exceptional rows are:

| mandatory node | atom | macro edges | owner length | short exit tag |
|---:|---:|---|---:|---|
| 76 | 590 | `648,1177` | 18 | `x`, suffix 2 |
| 84 | 681 | `736,1234` | 18 | `x`, suffix 2 |
| 92 | 780 | `832,1299` | 18 | `x`, suffix 2 |
| 94 | 794 | `842,1307,1308` | 25 | `y`, suffix 2 |
| 100 | 885 | `931,1375` | 18 | `x`, suffix 2 |
| 102 | 899 | `941,1383,1384` | 25 | `y`, suffix 2 |

### Lemma 2.1 (first-connector locality)

Let `P` be one of the six canonical oriented atoms and let `b` be its short
exit tag.  For every pure old-coordinate owner `u` and every continuation
word `R`, the word `P,u,R` has a strict internal positive `b`-run of length
two.  For the reversed atom, every word `R,u,reverse(P)` has such a run.

#### Proof

The positive `b`-suffix of `P` has length exactly two, so it is preceded
inside `P` by a zero.  A pure `U` owner has `b=0`.  Hence appending the first
connector closes that suffix between zeros, producing a strict run of
length two.  No token after `u` can change a run already closed by `u`.
Reversal gives the prefix assertion.  \(\square\)

The lemma is independent of the length and contents of the optional bridge.
It explains why adding all `1706` depth-two optional candidates leaves the
same six orientation-forced endpoint nodes.

### Corollary 2.2 (exact path-number lower bound)

Every cover of the mandatory atoms by pure-`U`/clean-optional directed paths
has at least three paths.

#### Proof

For each exceptional atom, one orientation has no outgoing transition and
the reverse orientation has no incoming transition.  It is therefore an
endpoint of its path.  A path has at most two endpoints, so six exceptional
atoms require at least three paths.  \(\square\)

## 3. The attaining three-path certificate

The frozen cover has mandatory-node paths

```text
P0: 76,...,94                       (19 mandatory atoms)
P1: 100,84                           (2 mandatory atoms)
P2: 102,...,92                      (85 mandatory atoms)
```

The six path endpoints are exactly

\[
                 \{76,84,92,94,100,102\}.                 \tag{3.1}
\]

Literal reconstruction gives lengths `898,78,4834`.  Each path separately
passes the D2/D3 run tests.  Restoring the selected atom and pure-owner port
edges gives

```text
selected atom superedges                         195
selected pure-U edges                            192
selected port vertices                           390
selected port degree profile                 1^6, 2^384
selected port components                           3
component vertex sizes                         8,72,310
ports of degree greater than two                   0
```

Thus the certificate is not merely label-disjoint: its selected port graph
is literally a disjoint union of three paths.  This statement concerns the
selected partial graph.  Completing the unselected facet phase and its
residual demands remains open.

## 4. Exact two-socket ledger

Among all orders and reversals of the three literal paths, the saved
certificate uses order `P0,P2,P1` with no reversals.  The direct join rows
are:

| join | left/right owners | intersection rank | union rank | symmetric difference | exposed port union rank |
|---|---|---:|---:|---:|---:|
| `P0 -> P2` | `76515 -> 77365` | 6 | 12 | 6 | 11 |
| `P2 -> P1` | `59846 -> 40045` | 4 | 14 | 10 | 13 |

The exposed port pairs are respectively

\[
       (10979,11829),\qquad (27078,7277).             \tag{4.1}
\]

Their unions have ranks `11` and `13`, not nine.  Therefore neither pair
admits a pure-`U` connector.  The owner pairs are also not Johnson adjacent.
Nevertheless direct literal concatenation is run-clean:

\[
  |W|=|\{W_i\}|=5810,\qquad
  \operatorname{bad}_{D2} =0,\qquad
  \operatorname{bad}_{D3} =0.                         \tag{4.2}
\]

### Theorem 4.1 (exact non-port fusion number in the frozen catalogue)

The minimum number of joins outside the pure-`U` clean-atom connector
catalogue needed to make the certified forced bank one linear owner-phase
word is exactly two.

#### Proof

Corollary 2.2 leaves at least three pure-`U` path components.  Turning three
linear components into one linear order needs at least two cross-component
joins.  The order in (4.1) supplies two direct joins and (4.2) verifies that
they preserve the required residence rows.  Hence two is both necessary and
attained at the owner-trace level.  \(\square\)

Theorem 4.1 deliberately says *non-port obligation*, not literal socket
construction.  The two owner pairs have the wrong Johnson distance.  A
valid compiler must replace or absorb each direct join using complementary
facet tokens while preserving all lower colours, selected owner service,
upper/deep shadows, and the common cap.

## 5. Exact downstream socket condition

Let the three selected port paths be `P0,P1,P2` with their six exposed
halfports.  A complete continuation of this route must provide two
complementary socket packets `S_1,S_2` such that:

1. `S_1` replaces the `P0 -> P2` direct owner join and `S_2` replaces the
   `P2 -> P1` join in the same literal chronology;
2. after expansion, each packet has the same required endpoint owner traces
   and contributes no strict D2 run below three or D3 run below four;
3. the signed rank-eight port-colour loss/gain of `S_1+S_2` is compatible
   with a nonnegative residual demand vector;
4. the remaining unused pure owners and port half-incidences admit the exact
   pair-column residual `b`-flow and connected completion;
5. all displaced lower/upper/deep providers survive or are recreated; and
6. both packets lie in one common-cap-compatible compiler skeleton.

These six rows are necessary.  Together with an exact residual completion
and literal replay they are sufficient by direct concatenation and
expansion.  No assertion that such packets presently exist is made.

## 6. Reproducibility and scope

Primary certificate:

```text
scratch/search_k17_marked_atom_phase_path_20260731.py
scratch/k17_marked_atom_phase_path_20260731.json
payload SHA-256 b5a76f68c38824f5cc3edd3a1244c058ad44f17007c966572ecdcb85a776db52
```

AD solver-free replay and port audit:

```text
python3 scratch/audit_ad_k17_three_path_port_socket_ledger_20260731.py
```

The audit reconstructs all `4740` candidates in canonical order, decodes
the saved candidate IDs, verifies the six forced endpoints, resource
injectivity, literal D2/D3 residence, selected port degrees, the three port
components, and the two non-port interface rows.

This theorem is scoped to the frozen parent, fixed initial macro forest,
the deterministic clean-atom split, and pure old-coordinate `U` connectors.
It does not prove a complete lower-rainbow carrier after the two direct
joins, a residual `b`-flow, a common-cap compiler, deep-shadow completeness,
an optimal `K17` word, or an all-dimension recurrence.
