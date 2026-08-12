# Candidate29 `C6 x C14`: exact terminal no-go

Date: 2026-08-01  
Status: **complete exact no-go in the stated shell; independently replayed**

## 1. Scope

Fix candidate29, whose quotient successor is one `1430`-cycle of voltage
`3 mod 17`, with unique upper hole `0x0355f` and unique lower hole
`0x0062f`.  This note concerns exactly two simultaneous simple assignment
circuits with support sizes `3+7`:

```text
H3 x D7   (physical H-C6 x D-C14),
H7 x D3   (physical H-C14 x D-C6).
```

The complete unique literal terminal-map banks have sizes

```text
H3=621, D3=626, H7=303975, D7=304444.
```

Thus the exact Cartesian domain is

```text
189059724 + 190288350 = 379348074 pairs.
```

Raw atoms retain incidences equal to the opposite base matching.  Equal
histories are identified only when their complete sorted literal side patches
agree.  Triple circuits, `C30`, residence, deeper shadows, opening, and the
compiler are outside scope.

## 2. Exact evaluator

For D assignment `alpha` and H assignment `beta`, the terminal successor is

\[
                P'=\beta^{-1}P\alpha .
\]

Every Cartesian pair was evaluated, without prefilter skipping, as follows.

1. Apply both literal patches and test simultaneous D/H incidence
   disjointness.
2. Recompute the exact rank-7 current on the changed-owner union and the
   exact rank-10 current on the changed-facet union.
3. Contract the base cycle at the exact changed-tail set
   \(A\cup\alpha^{-1}P^{-1}(B)\), reconstruct every quotient component,
   and sum its literal voltage.
4. Materialize and replay on all `1430` owners/facets every one-palette-safe
   row and every running or tied connected-nonzero minimum.

The scan also audited, but never used to skip a pair, the two distinct
projected-current inequalities

\[
 \operatorname{Def}(\nu_- )\le2|A\cap B|,
 \qquad
 \operatorname{Def}(\nu_+ )\le
 2|\bar D(A)\cap\bar H(B)|.                         \tag{2.1}
\]

The isolated columns were formed before rank projection.  In particular an
opposite-base obligation contributes the deleted base colour but no isolated
new rank-7/rank-10 colour: its raw intersection/union has rank `8/9`.
No exact safe row violated (2.1), their sum inequality, or pair-rescue
containment.

## 3. Exact census

| orientation | raw pairs | terminal valid | connected/nonzero | upper safe | lower safe | both safe |
|---|---:|---:|---:|---:|---:|---:|
| `H3 x D7` | 189,059,724 | 46,275,853 | 8,081,358 | 322 | 242 | **0** |
| `H7 x D3` | 190,288,350 | 47,006,748 | 8,499,746 | 853 | 98 | **0** |

Both orientations attain minimum connected-nonzero total palette debt `2`:

```text
H3 x D7: atoms (99,53008)
H7 x D3: atoms (27091,69).
```

The one-palette replay ledgers are respectively `564=322+242` and
`951=853+98`; because `both safe=0`, there is no overlap term.  Direct full
replay agreed with every sparse palette, hole-ID, component-length, and
component-voltage computation.  All terminal quotient component counts were
odd, as forced by the even signs of both the 3- and 7-cycles.

The projected gate is already extremely selective:

| orientation | lower projected fail | upper projected fail | joint projected fail |
|---|---:|---:|---:|
| `H3 x D7` | 189,044,010 | 189,045,375 | 189,059,570 |
| `H7 x D3` | 190,274,551 | 190,269,836 | 190,288,203 |

These are diagnostic counts over the raw domain, not the basis of the
no-go.  The no-go uses the unpruned exact final currents.

## 4. Conclusion

### Theorem 4.1

No simultaneous candidate29 `C6 x C14` terminal pair in either orientation
preserves both immediate palettes.  Consequently none yields an immediate
connected nonzero-voltage quotient factor.

The stronger statement holds before topology: the exact both-palette-safe
count is zero among all `379,348,074` raw pairs.

This theorem does not exclude any larger or differently composed repair.

### Corollary 4.2 (support-ten shell closed)

Together with the independently replayed `C10 x C10` and `C8 x C12`
no-gos, Theorem 4.1 closes every parity-legal simple two-circuit partition of
total assignment support ten for candidate29:

```text
5+5, 4+6, 3+7
```

(physical circuit lengths are twice these assignment supports).  This
corollary is confined to two simultaneous simple assignment circuits; it
does not cover overlapping sequential histories, three-circuit packets, or
larger total support.

## 5. Independent filter-first replay

A producer-independent implementation regenerated all four raw banks from
the frozen Boolean atlas.  It did not include or call the primary evaluator.
It used the following proof-safe order:

1. obligation capacity and exact support containment;
2. literal terminal collision;
3. scalar and targetwise projected-current cuts, with off-rank isolated
   traces dropped only after forming the free trace column;
4. exact final currents for every row which could still be safe on at least
   one shore; and
5. full `1430`-row palette/topology/voltage replay for every one-palette-safe
   row.

The complete pair ledger was retained.  In particular, a pair skipped after
step 3 failed the necessary projection on both shores and therefore could not
be one-palette-safe.  The independent totals exactly matched the primary:

| orientation | terminal valid | upper safe | lower safe | both safe |
|---|---:|---:|---:|---:|
| `H3 x D7` | 46,275,853 | 322 | 242 | **0** |
| `H7 x D3` | 47,006,748 | 853 | 98 | **0** |

All `564` and `951` one-palette-safe rows were materialized and replayed.
The projection reduced exact-current evaluation to respectively `577` and
`963` rows; this acceleration is not a weakening of the exact safe counts.

The primary global debt-two factors were then checked by a second,
factor-only program.  It independently regenerated the raw bank IDs from
their literal patches and obtained

```text
H3 x D7: H atom 99,    D atom 53008, one 1430-cycle, voltage 7,  holes 1+1;
H7 x D3: H atom 27091, D atom 69,    one 1430-cycle, voltage 12, holes 1+1.
```

Thus the primary minimum labels, exact palettes, connectedness, and voltage
are independently bound to the emitted factor files.  The filter-first
implementation does not claim an unpruned component histogram; the primary
scan remains authoritative for that diagnostic.

The cyclic-SCD depth-three state-Hall formulation is not evaluable from one
of these terminal rows alone: no literal equivariant rank-seven/rank-six
deletion-flag table is supplied.  Its precise diagnostic status is

```text
NOT_STATE_HALL_EVALUABLE_NO_LITERAL_EQUIVARIANT_FLAG_TABLE.
```

This is not a further rejection and gives no chronology, upper-shadow, or
compiler conclusion.

## 6. Reproducibility

Primary artifacts are in

```text
scratch/threadD_k17_candidate29_c6_c14_20260801/
```

Key hashes:

```text
source       640dc17743d21f4e561e9358e231fe517e2d07ca3972d09c696661edac2520dc
audit        e09faa7b003ebb1e6de1a99b199fac17b0d54df6c74ea155295ae233a5165f68
input factor aed64bc32992d65f77c4a0bcbcf9189f88d3d835295df517e8ca29f46595fb8a
```

The bounded one-core H100 execution exited `0` after `13:38.75`, used
`818.61` user seconds, and had maximum RSS `204,788 KiB`, with no swaps and
empty stderr.  Resource exhaustion would have been classified `UNKNOWN`; it
did not occur.

Independent artifacts are in

```text
scratch/threadD_k17_candidate29_c6_c14_independent_20260801/
```

Key hashes:

```text
independent source   f29c70e417d7f484d07e8045fe54ffaf78e0188d611df67e730611799085a731
independent audit    c9fda3defbd12f81cf99a680c0a835e2af3af35c942971ada4dbaa078c58291d
minimum checker      453a4ab31baba0b43bc87da37a3b06a37246485babaec3235b3895da70206a83
minimum audit        4c38403494c75a9948cbf9c8cc5e91a0c15bee37dfe877df3718ea656d33c05c
```

The independent scan exited `0` after `1:40.68`, used `100.50` user seconds,
and had maximum RSS `306,536 KiB`, with no swaps and empty runtime stderr.
The minimum checker exited `0` after `2.10` seconds at `34,816 KiB` RSS.
