# `k=17`: packet-first serial support-two basin descent from `shuffle201`

## 1. Exact scope

Start from the authenticated reverse-tie `shuffle201` factor

```text
e28a8ee5825564baf0d75720d8f3c1a53a911e9c53956aff49ed2460fd08c8dd.
```

At each serial round the computation rebuilds, relative to the current
incumbent, all `2,722,720` literal flag options and the complete unary and
opposite-difference support-two resource-circuit catalogue.  It then runs
both frozen deterministic catalogue orders.  Every accepted move is
root-disjoint from the other accepted moves of that round, preserves all
type masses and every lower flag target, and strictly improves the exact
materialized packet score

```text
(packet matching, -zero-out, -zero-in, turns, edges).
```

After each selected round, independent programs reconstruct the full static
ledger, all phase-labelled transition arcs, the packet maximum matching, the
separate owner projection, and the common-live root--owner DM relaxation.
All heavy runs used one H100 CPU per deterministic order, an 8 GiB address
space cap, and a 3,600-second CPU cap under

```text
/home/amodo/or15/work/threadA_k17_shuffle201_serial_support2_20260801.
```

## 2. Exact serial lineage

The selected lineage is:

| table | option shell `(unary, support2)` | accepted moves / roots | packet `M / z+ / z-` | common `M / def / shore` | owner `M / z-` | candidate SHA prefix |
|---|---:|---:|---:|---:|---:|---|
| `e28` | -- | -- | `954 / 234 / 445` | `718 / 712 / 770->58` | `1079 / 351` | `e28a8ee5` |
| `b01 reverse` | `2561,214610` | `303 / 570` | `1110 / 134 / 307` | `867 / 563 / 684->121` | `1148 / 282` | `44971315` |
| `b02 reverse` | `2548,214766` | `197 / 367` | `1178 / 103 / 235` | `936 / 494 / 652->158` | `1149 / 281` | `560d8d86` |
| `b03 forward` | `2545,214803` | `87 / 168` | `1207 / 95 / 213` | `961 / 469 / 657->188` | `1162 / 268` | `68d439c6` |
| `b04 forward` | `2548,215271` | `73 / 135` | `1220 / 87 / 204` | `976 / 454 / 637->183` | `1172 / 258` | `6c0ed7db` |
| `b05 reverse` | `2543,215281` | `19 / 36` | `1221 / 81 / 203` | `983 / 447 / 641->194` | `1177 / 253` | `452a332d` |
| `b06 forward` | `2545,214979` | `5 / 10` | `1223 / 84 / 201` | `981 / 449 / 637->188` | `1175 / 255` | `d32ed635` |
| `b07 forward` | `2546,215119` | `1 / 2` | `1223 / 84 / 201` | `981 / 449 / 637->188` | `1176 / 254` | `3e7af637` |

The basin-5 forward and reverse factors tie on the entire packet score but
are different tables.  Their common matchings are respectively `981` and
`983`; this fixes the reverse table as the correlation-aware tie-break.

Basin 6 is the last strict packet-matching rise, from `1221` to `1223`.
Basin 7 accepts one equal-matching move because it raises turns from `2263`
to `2265`.  Rebuilding the complete catalogue once more from the resulting
table gives

```text
literal options                    2,722,720
unary circuits                         2,546
support-two circuits                  215,115
accepted moves, forward                     0
accepted moves, reverse                     0.
```

Thus `3e7af637...` is an exact fixed point of both declared deterministic
serial orders.  The last strict packet-rise witness is `d32ed635...`, with
matching `1223`.  The best common-live table along this packet-first lineage
is instead basin 5, `452a332d...`, with common matching `983`; the fall to
`981` at basin 6 is a literal instance of the packet/common correlation.

## 3. Exact conclusion and boundary

The computation proves a materialized packet-first improvement

```text
954 -> 1110 -> 1178 -> 1207 -> 1220 -> 1221 -> 1223
```

and an exact deterministic support-at-most-two local fixed point.  At the
terminal table no single unary or support-two resource circuit is accepted
by either fixed serial order, and a complete further pass accepts no move.

This is **not** a proof that `1223` is the optimum of the disjoint circuit
master.  Several individually nonimproving circuits may improve jointly;
overlapping or iterated circuits and support at least three remain outside
the catalogue.  It is also not a common owner/root/`H` transversal: the
terminal common-live matching is only `981`, with deficiency `449`.  Upper
rows, connectedness, voltage, residence, opening, and compiler conditions
were not imposed.

The complete frozen machine-readable lineage is

```text
scratch/threadA_k17_shuffle201_serial_support2_20260801/
  packet_first_serial_lineage.audit.json
```

and that directory contains every selected and rejected-order certificate,
move list, catalogue audit, independent transition replay, owner audit, and
common-live DM audit.
