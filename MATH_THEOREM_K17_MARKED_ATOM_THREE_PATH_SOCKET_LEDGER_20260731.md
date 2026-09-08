# The frozen `K17` marked-atom bank has exact pure-`U` path number three

Date: 2026-07-31  
Status: exact finite theorem with independent literal replay; the two final
phase sockets are not physical Johnson seams

## 0. Result

Split the authenticated `1430`-edge macro forest greedily at every fixed
macro seam whose retention would create a strict internal depth-two run of
length below three.  This gives `1144` residence-clean atoms.  Exactly `106`
atoms are mandatory because together they contain all `108` forced nonflat
macros.

Join mandatory atoms by a pure old-coordinate rank-nine owner, allowing zero,
one, or two optional clean atoms between consecutive mandatory atoms.  The
literal oriented catalogue has

```text
direct candidates                         328
one-optional candidates                  2706
base total                               3034
new two-optional candidates              1706
augmented total                          4740
```

Six mandatory nodes

```text
76, 84, 92, 94, 100, 102
```

are forced path endpoints.  This remains true for an arbitrarily long chain
of optional atoms: at the blocked end, the mandatory atom has a terminal
length-two run on tag bit `15` or `16`, and the first pure-`U` owner has both
tag bits zero.  It therefore closes the bad run before any later optional
atom can act.  Reversal gives the corresponding blocked prefix.  Since one
path has at most two distinct endpoints, every such pure-`U` path cover has
at least three paths.

The frozen witness attains three paths.  Its mandatory-node and literal-owner
lengths are

```text
mandatory nodes                         19, 2, 85
literal owners                         898, 78, 4834
```

It uses `18/81/4` candidates with zero/one/two optional atoms, respectively,
`89` distinct optional atoms, and `192` distinct pure-`U` owners.  All `5810`
literal owners are distinct.  Each of the three paths is a Johnson path, and
direct replay gives zero strict internal `D2` runs below three and zero
strict internal `D3` runs below four.

Thus the exact pure-`U` path number of this marked-atom instance is

\[
                              \boxed{3}.
\]

Two additional phase joins suffice to concatenate the three traces into one
`5810`-token residence-clean row.  They are **two phase/socket obligations,
not two cells**.

## 1. The forced-endpoint proof

For each forced node, orient its mandatory atom as stored in the frozen
catalogue.  Nodes `76,84,92,100` end in exactly two consecutive owners
carrying bit `15`; nodes `94,102` end in exactly two carrying bit `16`.
The reverse orientations begin with the same length-two strings.

Every connector owner belongs to \(\binom{[15]}9\), so it carries neither
new tag bit.  Appending it to a stored orientation brackets the terminal
length-two run by zero; prepending it to the reverse orientation does the
same to the prefix.  Consequently the stored orientation has no legal
pure-`U` outgoing connector and the reverse has no legal pure-`U` incoming
connector.  Optional atoms occur only after that first connector and cannot
change this conclusion.

The six nodes must therefore be the distinct endpoints of at least three
path components.  This is solver-free and stronger than the explicit
two-optional enumeration.  The saved resource-disjoint three-path cover is
the matching upper bound.

## 2. Port-capacity replay

Distinct owner labels alone would not certify a physical partial factor, so
the independent replay restores the frozen macro-port degree ledger.  The
`192` selected pure-`U` connectors use `384` distinct rank-eight port colours,
each exactly once.  Every used colour has fixed macro degree one and residual
demand one.  Hence there is no repeated port, zero-demand use, or capacity
overrun.  The remaining ledger is exactly

```text
unused pure-U owners                     4813
unfilled occurrence-labelled halfports  9626
```

and `9626 = 2*4813`.

An independent source--owner--port--sink replay saturates this remaining
degree instance exactly: `9626/9626`.  The resulting fixed graph still has
`4813` quotient components, so this is an unconditioned Hall certificate,
not connected closure.  Any socket exchange changes endpoint incidences and
must be followed by the conditioned flow check again.

The six exposed marked-path ports are different: every one has fixed macro
degree two and residual pure-`U` demand zero.  They cannot be closed by the
ordinary residual `U`-to-port flow.  A physical completion must change or
rephase their saturated macro incidences while restoring the displaced
lower colours.

## 3. Exact geometry of the two trace joins

The best frozen trace ordering uses two arbitrary owner-owner joins.  Their
owner XOR/intersection/union ranks are

```text
(6, 6, 12),
(10, 4, 14).
```

Neither is Johnson adjacent.  The corresponding complementary-tail pairs
are

```text
forced nodes 94 -> 102: owners 43747 -> 44597, X shore, Johnson distance 3;
forced nodes 92 -> 100: owners 92614 -> 72813, Y shore, Johnson distance 5.
```

Therefore their natural local topologies are a shore-preserving `C6` packet
with two intermediate owners and a shore-preserving `C10` packet with four
intermediate owners.  This identifies the precise catalogue search; it does
not prove that either packet preserves the required palettes or common cap.

A subsequent exact catalogue audit closes the most literal version of this
search.  Neither pair occurs in an applicable authenticated saved packet,
and all `36` shortest `C6` geodesics and all `14400` shortest `C10`
geodesics fail after restoring the full endpoint run context.  Every direct
splice creates two `D2` length-two and two `D3` length-three runs on the
opposite tag.  Thus a viable packet must change an endpoint collar or use a
wider occurrence-labelled rethread; a bare shortest geodesic cannot realize
the two obligations.

The proved statement is only that two non-port phase transitions merge the
three residence traces.  It does **not** identify two word cells, two legal
Johnson seams, or a completed lower compiler.

## 4. Scope and current role

This theorem fixes the earlier scalar ledgers: the selected bank does not
need `107` independent phase boundaries, and within this clean-atom/pure-`U`
coordinate its exact residual component debt is two.  Still open for this
certificate are:

1. endpoint-collar-changing occurrence-labelled socket realization at the
   six saturated endpoints (the direct shortest `C6/C10` face is closed);
2. restitution of every displaced lower and upper palette occurrence;
3. socket-conditioned residual `b`-flow and quotient connectedness (the
   unconditioned residual flow already passes `9626/9626`); and
4. one common-cap lower compiler.

A subsequently found six-occurrence forest repair gives a cleaner
zero-residence-debt primary route (`106` marked components, `154` macros).
The present theorem remains an authenticated fallback and an exact local
socket normal form; it is not a `K17` word or a global obstruction.

## 5. Reproducibility

Run

```text
python3 scratch/h2_independent_audit_k17_marked_atom_three_path_frozen_20260731.py
python3 -m py_compile scratch/h2_independent_audit_k17_marked_atom_three_path_frozen_20260731.py
```

Frozen constructor and witness:

```text
scratch/search_k17_marked_atom_phase_path_frozen_20260731.py
SHA-256 5761a6168d39faeebc3e1e8eba9d2733d81b6ecebd6edf462291c82fff33256a

scratch/k17_marked_atom_phase_path_frozen_20260731.json
SHA-256 234a34703cdef66722d6df54b936361048565915f4bf9ab523e13368d828bdec
payload 3f36ddc1a6fd02d4e8b90b3cd48576c54dc8882caa94f1066dca564732e21447
```

Independent replay:

```text
scratch/h2_independent_audit_k17_marked_atom_three_path_frozen_20260731.py
SHA-256 805dee17d08d00a60b819f495f44a0b87c256fdfdc47ff6e0a30b3bebcc120ec

scratch/h2_independent_k17_marked_atom_three_path_frozen_20260731.audit.json
SHA-256 33e8e75f58e62a9a8c71ca4f1f5f970a0458f3a3da54bedf57cda9e6817287b2
payload 9895837556693099c13e1c02cf0ae0a890641e33b36c98a6bc85a73c72654f94

scratch/audit_k17_marked_atom_threepath_port_gate_20260731.py
SHA-256 8235f16aeaff3efeec3d6c659616f58e92d9262fa84300dcfb27d22faf4a9557

scratch/k17_marked_atom_threepath_port_gate_20260731.audit.json
SHA-256 4451a1f94293259578ac260a52e245f40d992e46e0503b47022fe71d7f3d1e8d
payload abb96f4b1d46c112a3e43d90befffebbdca5362a3b678e38c9a2cba919030d14

scratch/audit_k17_tailpair_c6c10_catalogue_nomatch_20260731.py
SHA-256 21ca3b3322809fc5c66ae7665ae090f13c27aa1f3b03ed2673326833e8e44674

scratch/k17_tailpair_c6c10_catalogue_nomatch_20260731.audit.json
SHA-256 8202932399108decbca30cb88c5cb6f857f028fd2337e3e2b5824b2cb211143b
payload 13d07a4c311e3cbe124bb7e44c8c8b54ba2d65a12d9386572e940532ef39dd90
```

The delegated payload `7656329c...` belonged to an earlier live-written
version.  The frozen lineage above is byte-exact and independently replayed.
