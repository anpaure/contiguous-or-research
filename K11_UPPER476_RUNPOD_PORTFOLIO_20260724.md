# RunPod length-476 constructive portfolio for `k=11`

## Scope

This is a heuristic search for a genuine 476-entry universal nonzero word.
Any candidate is a rigorous upper-bound certificate only after both exact
verifiers pass.  Failure or timeout has no lower-bound meaning.

All compilation and search run on the Rose RunPod.  No search computation is
performed on the local machine.

## Program and seeds

The unrestricted simulated-annealing source is
`scratch/search_unrestricted_word_sa.cpp`.  The byte-identical RunPod copy and
its warning-free binary have hashes

```text
source  67c9d0764333268d0557a05beca2eee63963d89e6b8683da0206dc6518ed53f7
binary  54a8382b95db6555936390b94ee3a8512addc81b50a806960b89d6fa2a9faa9d
```

Four distinct verified one-hole seeds are used:

```text
canonical drop-last: e790e3b5fc0ce29898143ff16a23e1597aee54aa246c91e946854163765a0221
relocated basin:     660cb2ac66e1e357e7276be2b01b6399f9781485715cd2afb0964eeea11089ad
plateau basin:       7cda6198356e2aa5d14555ed0e65a50dc82bc7032e8c95bba627e41ff5c32cb2
unrestricted basin: e866a1fb22db8675d9e33fad6d803eaf75721fd5b6c85d4e4186d652688cd87
```

Each has length 476 and covers exactly 2,046 of the 2,047 nonzero masks.

## Launch ledger

At `2026-07-24T04:26Z`, ten one-thread searches were launched for 21,600
seconds at nice level 19 under independent 256 MiB virtual-memory caps.  The
first four used the initially idle cores; after confirming their combined RSS
was under 20 MiB, six further trajectories filled the remaining idle cores:

| name | CPU | RNG seed | seed family | wrapper / solver PID |
|---|---:|---:|---|---|
| `sa501` | 4 | 501 | canonical | `200795 / 200797` |
| `sa502` | 5 | 502 | relocated | `200796 / 200801` |
| `sa503` | 6 | 503 | plateau | `200798 / 200802` |
| `sa504` | 9 | 504 | unrestricted | `200799 / 200803` |
| `sa505` | 0 | 505 | canonical | `201131 / 201138` |
| `sa506` | 12 | 506 | relocated | `201132 / 201139` |
| `sa507` | 15 | 507 | plateau | `201133 / 201140` |
| `sa508` | 21 | 508 | unrestricted | `201134 / 201141` |
| `sa509` | 25 | 509 | plateau | `201135 / 201142` |
| `sa510` | 28 | 510 | unrestricted | `201136 / 201143` |

All ten solver processes together initially used under 40 MiB RSS.  They are
pinned away from the six exact SAT solver CPUs.  Cgroup use after the full
launch was about 27.3/32.0 GB and the OOM-kill counter remained 35.

## Automatic verification

If a search returns success, its wrapper runs both independent checkers:

```text
/root/verify_or_array 11 <candidate
/root/verify_or_suffix 11 candidate
```

Only if both exit zero is a `.VERIFIED` marker created.  A candidate must
still be copied back, hashed, and independently rechecked before changing the
certified upper bound.
