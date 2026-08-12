# K16 18-cell raw-splice scope ledger and single-run selection

Date: 2026-07-30; corrected 2026-07-31  
Status: **PASS scope audit; five immutable-ghost fibres and RF495 now
solver-free UNSAT; historical solver runs are theorem-redundant where noted**

## 1. Scope rule

This ledger uses `SAT`, `UNSAT`, `UNKNOWN`, and `NEVER LAUNCHED` literally.
A timeout, empty output, incomplete proof, or active process is `UNKNOWN`.

Two search objects are kept separate throughout:

1. A **raw-splice fibre** fixes 12,855 rows of a length-12,873 word and
   permits arbitrary nonzero values in 18 named cells.  A decoded SAT word
   which covers all 65,535 nonzero masks proves `nu(16)=12873` immediately.
2. A **carrier/compiler chronology** may be middle-exact and upper-complete
   without being a universal word.  It must also pass the complete
   26,332-target lower Hall/compiler gate.  The exact229 and c5960 carrier
   results are not raw-splice SAT or UNSAT results.

Item 2035's oriented-anchor theorem has exactly one raw-splice scope: the
authenticated repeat-free seed5/self `4/9/5` fibre.  It does not cover another
parent, another window allocation, a two-parent body, an optimal-trim fibre,
or the delete-p1 collar below.

## 2. Complete 18-cell raw-splice inventory

The process labels in this table are an operational snapshot, not theorem
evidence.  A live or completed-but-uncertified solver remains `UNKNOWN`.

| Parent/fibre | 18-cell geometry | Residual targets | Current exact status | Frozen evidence or CNF SHA |
|---|---|---:|---|---|
| seed5/self RF495 | `4/9/5` | 70 | **PROVED UNSAT** for the complete fixed fibre | oriented-anchor Hall theorem `d1b23b64...`; the raw solver is theorem-redundant |
| seed5/self RF594 | `5/9/4` | 70 | **UNKNOWN full fibre; survives immutable-ghost test** | `cc2a6f4e...` |
| seed5/self RF4104 | `4/10/4` | 70 | **UNKNOWN full fibre; survives immutable-ghost test** | `2eb716b1...` |
| seed5/self RF486 | `4/8/6` | 70 | **UNKNOWN full fibre; survives immutable-ghost test** | `5b7df0b7...` |
| seed5/self RF585 | `5/8/5` | 70 | **UNKNOWN full fibre; survives immutable-ghost test** | `2844efba...` |
| seed5/self RF684 | `6/8/4` | 70 | **UNKNOWN full fibre; survives immutable-ghost test** | `09879f03...` |
| seed1/self S1495 | `4/9/5` | 73 | **UNKNOWN full fibre; survives immutable-ghost test** | raw CNF `67b074bc...`; compact audit `5e0d3740...` |
| seed1/self S1594 | `5/9/4` | 73 | **UNKNOWN full fibre; survives immutable-ghost test** | `fbe7bf18...` |
| seed1/self S14104 | `4/10/4` | 73 | **UNKNOWN full fibre; survives immutable-ghost test** | `63a460c8...` |
| seed1/self S1486 | `4/8/6` | 73 | **UNKNOWN full fibre; survives immutable-ghost test** | `eaf79ae5...` |
| seed1/self S1585 | `5/8/5` | 73 | **UNKNOWN full fibre; survives immutable-ghost test** | `34d33cec...` |
| seed1/self S1684 | `6/8/4` | 73 | **UNKNOWN full fibre; survives immutable-ghost test** | `2356b3f9...` |
| seed4/self S4 | `4/9/5` | 69 | **PROVED UNSAT**, immutable ghost `0xbcc2` at deadlines `6483,7583` | item 2015 and 2026-07-31 portfolio audit |
| V/V TH495 | `4/9/5` | 60 | **PROVED UNSAT fixed fibre**, immutable `0xc279` ghost; one-hole incumbent remains valid | `e4a7ad4e...`; 2026-07-31 portfolio audit |
| V/V TH594 | `5/9/4` | 60 | **PROVED UNSAT fixed fibre**, immutable `0xc279` ghost | `074d571c...`; 2026-07-31 portfolio audit |
| optimal trim gOPT1 | trims `(3,5;8,5)`, windows `5/8/5` | 65 | **UNKNOWN full fibre; survives immutable-ghost test** | `772c7a8c...` |
| optimal trim gOPT2 | trims `(5,5;6,5)`, windows `5/8/5` | 65 | **UNKNOWN full fibre; survives immutable-ghost test** | `9026e260...` |
| optimal trim gOPT3 | trims `(6,5;5,5)`, windows `4/9/5` | 65 | **UNKNOWN full fibre; survives immutable-ghost test** | `840c8851...` |
| optimal trim gOPT4 | trims `(8,5;3,5)`, windows `5/8/5` | 65 | **UNKNOWN full fibre; survives immutable-ghost test** | `d768d77e...` |
| two-parent XV/YRF | `5/9/4` | 64 | **UNKNOWN full fibre; survives immutable-ghost test; smallest surviving residual atlas** | `778e055f...` |
| two-parent XRF/YV | `5/9/4` | 66 | **PROVED UNSAT fixed fibre**, immutable `0xc279` ghost | `b47e24bf...`; launch status irrelevant |
| two-parent XV/YS1 | `5/9/4` | 67 | **UNKNOWN full fibre; survives immutable-ghost test** | `2e989d6e...` |
| two-parent XS1/YRF | `5/9/4` | 70 | **UNKNOWN full fibre; survives immutable-ghost test** | `570f8580...`; no mixed `4/9/5` materialization found |
| marked-rail scattered puncture proposal | proposed 18-cell support | -- | **NEVER LAUNCHED** | only `punct.py` and a proposal/census exist |
| delete-p1 collar594 | `[0,5)`, `[6435,6444)`, `[12869,12873)` | 61 | **PROVED UNSAT fixed fibre**, immutable `0xc279` ghost; old solver is theorem-redundant | exact normalized CNF `cc73d7bf...` |

The generalized `gRF_t23`, `gRF_t28`, `gS1_t28`, and `gXV/YRF_t28` trim
relaxations are not 18-cell fibres: they have 20 or 25 free cells.  Their
solver outputs are all `UNKNOWN`; they do not classify the scattered
puncture proposal.

## 3. Strongest uncovered fibre

All rows have eighteen free cells, so “smallest” is measured here by the
fixed-body residual target count.  The numerical leaders V/V TH495 and TH594
have sixty residual targets, and delete-p1 has sixty-one, but all three are
now solver-free dead by immutable `0xc279` ghosts.  The reverse mixed row
XRF/YV is dead for the same reason.  Seed5/self RF495 survives the ghost test
but is independently dead by oriented-anchor Hall.

The smallest surviving residual atlas is therefore the **oriented**
two-parent row XV/YRF with sixty-four targets and windows `5/9/4`.  Its
reverse XRF/YV is not equivalent: only the latter places the repeating V
parent on the marked shore and transports `0x4279` to the child ghost
`0xc279`.  The next-smallest survivors are gOPT1--4 with sixty-five targets.
Survival is only a necessary-condition result; none of these rows is proved
SAT or universal.

The historical delete-p1 CNF has 5,338 variables and 76,653 clauses, but its
solver status is now irrelevant: the full fixed fibre is theorem-redundant
UNSAT.  The authenticated one-hole words `e4a7ad4e...` and `a72cc9e...`
remain valid calibration data and are nonisomorphic.

## 4. Literal-complete 19-cell SAT control

The matched control uses the V/V `5/9/5` length-12,874 geometry and 19 free
cells.  An independent audit reconstructs every expected clause in order,
checks the complete SAT assignment against all 177,958 clauses, decodes the
word, and replays all 65,535 nonzero masks.

```text
variables                 5705
cell-bit variables         304
witness variables         5401
residual targets             60
interval shapes             409
clauses                  177958
covered masks          65535/65535
```

The maximum first-attainment distances at the four fixed-body boundaries are
`20,12,19,11`, so the model's `maxext=40` catalogue is complete.  The CNF,
map, decoded word and solver-output hashes are respectively

```text
47f8808b0918699317ed2caa12098855fdcdab0f50173ac8a78bc14ebf78f3b8
85c6cf74494de5898957d09c89bfbe7956cf61928628ee931c99138b9bf0a764
d08b7a96dbe5ccf97a59e4557971b582f91230eded4204f0da8ca050392a6d9b
148362c970105490a27394ff0cc336e48819508ef146c72293f05bdc488427bb.
```

One metadata field is stale: the copied `model.stats.json` has direct SHA
`42864e87...`, but its internal payload claim `fc5dc3...` recomputes as
`40fc81...`.  The audit does not trust that field; the map payload, complete
clause multiset, assignment and literal replay all pass independently.

## 5. The one launched 18-cell instance

Exactly one new solver was launched from the original 2026-07-30 audit.  The
2026-07-31 immutable-ghost theorem now makes this historical run redundant;
no solver verdict is needed for the fixed-fibre classification.

```text
remote root
  /home/amodo/or15/work/
    root_k16_deletep1_collar594_cadical_cc73d7bf_20260730

solver     CaDiCaL 3.0.1, SHA 49c86c5f8447d768906dcd12d62fb4752e80a48a0d52bbc633929f32eec00b3d
seed       260730, initial/forced phase false
CPU        62, affinity checked on child PID 1848046
priority   nice 19
wall cap   21,600 seconds (+30-second termination grace)
AS cap     8,589,934,592 bytes
proof cap  6,442,450,944 bytes, binary DRAT, retained under /home
started    2026-07-30T18:52:37+00:00
```

SAT is accepted only after the frozen decoder materializes the 18 physical
values and replays all 65,535 masks.  UNSAT is accepted only after independent
proof verification.  Timeout, signal, ENOSPC, proof-cap termination, decoder
failure, or proof-verifier failure is `UNKNOWN`.

No c5960 strengthened component census was launched.  The previously queued
seed1/self watcher was stopped before it started because a live raw CaDiCaL
already covers that fibre and the complete inventory selected delete-p1.

## 6. Frozen authentication

```text
MATH_THEOREM_K_K16_RF495_ORIENTED_ANCHOR_HALL_FIBRE_NOGO_20260730.md
  d1b23b644e484829af12b1e3fcb4b22503f33e9796978e8083f15c2cda460a77

MATH_THEOREM_K16_DELETEP1_COLLAR594_TARGET_CLOSURE_NORMAL_FORM_20260730.md
  e301625c6abf2976e97623dfc4e9b1c38c3be338b9fbddb08d5e34eab590fc15
selected CNF / map / stats / audit
  cc73d7bf680d2698fd05f34bee74e1eb10427c95d2323013b4f8d5e387b948f2
  b557c13272198a2338ce1f0718c24a0a1692cd8c8e3b40b2071a125402b3c55a
  d9a456532881d51e58ce481ae0bfc8ffda23990f29490f126d6c55c06bdbd72b
  efc2096c1e8994228c096581de21f5fcf5dadc2cc0dcc4d9c42bd6c92f71988f
selected SAT decoder
  586ad17240b32a19573d04fe160ed6aab95a4efff6bfab62ce6eaf58ffcfdd8e

scratch/audit_k16_raw_splice_19cell_sat_control_independent_20260730.py
  d8d0aee5af1f6e2ef59449823e0efcfc0a69ac56c307f8600b0853036b18f504
scratch/k16_raw_splice_19cell_sat_control_20260730.independent.audit.json
  abc130b0578b5d6e9761aa75f80c97f0c9b1f8c1f377288de5107770bec67d94
  payload af2c87929919efeb8dd1f209ae0ffa12b516237f7312fc4204762c5571f88af9

scratch/run_k16_deletep1_collar594_cadical_h100_20260730.sh
  c0bbb4fe5a7399dcd9afec01fe9bfbc0f7b82b6c9e4394d889d8604f3eb01418

scratch/audit_k16_raw_splice_18cell_scope_ledger_20260730.py
  0830c68a799ee52e2a28522bc686d62d572755625542dd14c5e96d1efdf45bb5
scratch/k16_raw_splice_18cell_scope_ledger_20260730.audit.json
  f386ccb1245bdf8d44c23b15b8f3ffa19b242bdddab53ba116712da3be3f10e6
  payload 288a2c97ab2e27b7fffb9a3f855272dab28c6a9775aa471d6108e2d93fd245ab

scratch/audit_r_k16_raw_splice_immutable_ghost_portfolio_20260731.py
  18f67ffdb54bd99993abdbce4604f8c2e5727e30e8b3a3b665be25ac3146a594
scratch/r_k16_raw_splice_immutable_ghost_portfolio_20260731.audit.json
  7364bb636b0f4f98092eb0a1b1739886f50ba241974723381ee6fe887a08e660
  payload 4adfdf8bb5da08a09663a1883e5514b7581f894f49189c575484f83dc0107315
```

This is a fixed-fibre scope ledger and a historical finite-decision record. It
does not prove an unrestricted K16 no-go, and none of its raw-splice statuses
is a carrier-Hall statement.

## 7. Superseding status correction (2026-07-31)

The complete immutable-delivery scan reconstructs twenty-three tri-window
fixed complements and reads the direct delete-p1 complement literally.  It
finds five solver-free dead rows:

```text
seed4/self S4 4/9/5       ghost 0xbcc2, deadlines 6483,7583
V/V TH495 4/9/5           ghost 0xc279, deadlines 11728,12828
V/V TH594 5/9/4           ghost 0xc279, deadlines 11729,12829
two-parent XRF/YV 5/9/4   ghost 0xc279, deadlines 11729,12829
delete-p1 collar594        ghost 0xc279, deadlines 11728,12828
```

Thus every completion in each of these five fibres has a different-deadline ghost
`G>=1`.  The architecture-free K16 equality theorem forces `G=0` for every
universal length-`12873` word because

\[
 26332\le(3-G)(12873+G)
\]

fails for `G>=1`.  All five full fixed fibres are therefore solver-free
UNSAT.  Seed5/self RF495 survives this scan but is separately dead by the
oriented-anchor `21>20` theorem.

The V/V word `e4a7ad4e...` and the delete-p1 word `a72cc9e...` remain valid,
nonisomorphic one-hole calibrations with sole hole `0x2c6d`; their provider
systems and closure domains are not identified.  Of the remaining rows,
XV/YRF has the smallest fixed-body residual family, of size64; all support
cardinalities are18.  This selects a next architecture but does not certify
SAT.  The scattered-puncture proposal remains unclassified because it has no
frozen exact support.  No unrestricted K16 lower bound follows.

## 8. Canonical H2-breaking augmentation

For each immutable three-cell delivery, the portfolio JSON records every
cell's unique target-bit contribution and every proper-prefix position.  In
all five dead rows the union of those two mechanisms is the entire repeated
six-cell support.  Thus one added ghost cell is the minimum structural
augmentation capable of breaking one deadline group; removing both fixed
copies before rehosting requires one cell from each triple.

On the authenticated delete-p1 `collar594` one-hole word, literal replay
leaves only four viable one-cell ghost-breakers preserving all other middle
labels:

```text
position   best total holes
11726      5
11728      3
12826      2
12828      5
```

The canonical live row adds `p=12826` to delete-p1 `collar594`:

```text
[0,5) union [6435,6444) union {12826} union [12869,12873).
```

Exactly sixteen normalized values at that position expose the residual pair
`{0x2c6d,0xc679}`.  Literal replay of those same sixteen values in the V/V
basin exposes the same pair; no full six-position V/V ranking is claimed.
This row is **PAIR-EXPOSED**, not PAIR-CLOSED.  With the original delete-p1
collar cells kept at their incumbent values, a single further common-provider
edit has no pass: all eight candidates occur at `p=6437` and create the same
six new debts
`{2879,287d,a879,a87d,c879,e879}`.  The distributed 19-cell V/V analog has
an exact 72-target/429-value closure master with no providerless row, but its
common-core feasibility remains `UNKNOWN`.  This exact pair socket is the
constructive augmentation frontier; XV/YRF remains the smallest unaugmented
18-cell survivor.
