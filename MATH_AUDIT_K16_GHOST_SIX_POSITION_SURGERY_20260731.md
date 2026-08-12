# K16: exact six-position ghost surgery

## Result

The authenticated delete-p1 `collar594` length-12873 one-hole word has two
first-middle deliveries of `0xc279`, supported on

```text
[11726,11728] and [12826,12828].
```

All `6 * 65534 = 393204` nontrivial one-cell substitutions at these six
positions were replayed against the first-middle deadline system.  A single
change can collapse the duplicate deadline while preserving every other
middle label, but it cannot simultaneously install the missing label
`0x2c6d`.

The unique strongest physical position is

```text
p = 12826, old value 0xc261.
```

Exactly sixteen normalized values at this position collapse the ghost while
leaving every other middle label intact:

```text
4001 4021 4201 4221 4841 4861 4a41 4a61
c001 c021 c201 c221 c841 c861 ca41 ca61.
```

For every one of them, literal replay of all nonempty targets leaves exactly

```text
{0x2c6d, 0xc679}.
```

The sixteen p12826 substitutions and their exact residual pair were also
replayed literally in the authenticated V/V one-hole basin.  That is the
only assertion below transferred to both basins; the full six-position
ranking and common-provider census concern delete-p1 `collar594` only.

## Comparison of the six cells

| position | old | ghost-removing values preserving all other middle labels | best total literal holes |
|---:|---:|---:|---:|
| 11726 | `8010` | 32 | 5 |
| 11727 | `4001` | 0 | — |
| 11728 | `8269` | 10 | 3 |
| **12826** | **`c261`** | **16** | **2** |
| 12827 | `8231` | 0 | — |
| 12828 | `c219` | 32 | 5 |

Thus, in delete-p1 `collar594`, the middle cells of either triple cannot
remove the ghost without losing another middle label.  Among the four
endpoints, `12826` is uniquely best under the stronger literal-coverage
objective.  No complete corresponding six-position ranking is claimed for
the V/V basin.

There are ghost-free one-cell values that install `0x2c6d`, but at every one
of the six positions they lose at least two other middle labels.  At 12826
there are eight such values; none is a direct `0xc279 -> 0x2c6d` exchange.

## Closure-exact support census

For every support of size at most three contained in the six displayed
positions of delete-p1 `collar594`, the target-intersection closure domain
was enumerated exactly.  No such support produces a ghost-free complete
middle layer.

The normalization is lossless for this question.  In a hypothetical
successful assignment, each affected start first reaches a rank-eight label
`T`.  Every edited value on that witness is a subset of `T`.  Replacing it by
the intersection of all required labels containing it can only add bits
inside every relevant `T`; an earlier rank-eight prefix would then equal the
same `T`.  Therefore a successful raw assignment would have a successful
closure-normalized representative, and the finite census is exhaustive.

## One additional cell is not enough

In delete-p1 `collar594`, after any of the sixteen strongest edits at 12826
and with every original collar cell held at its incumbent value, the two
holes are `0x2c6d` and `0xc679`.  An exhaustive common-provider census over
every physical position and every value capable of witnessing both holes
finds only eight assignments.  All act at

```text
p = 6437, old 0x0879,
```

and every one creates the same six new debts:

```text
2879 287d a879 a87d c879 e879.
```

Hence no two-substitution completion passes through this fixed normalized
delete-p1 branch.  This conclusion is not asserted for the V/V analog or a
distributed 19-cell assignment.  It does not rule out a wider collar: it
identifies the exact next six-target packet that this incumbent collar must
absorb.

## Boolean-cube normal form of the surviving branch

The sixteen strongest values at `12826` are not an unstructured catalogue.
They are exactly

```text
0x4001 | a*0x0020 | b*0x0840 | c*0x0200 | d*0x8000,
```

where `a,b,c,d` range independently over `{0,1}`.  (Here `b*0x0840`
means that bits `0x0040` and `0x0800` are switched together.)  Thus the
ghost-breaking choice has four Boolean degrees of freedom while its literal
residual remains invariant:

```text
{0x2c6d, 0xc679}.
```

In the fixed delete-p1 branch, the eight common-provider values at `6437`
are exactly

```text
0x0408 | e*0x0001 | f*0x0020 | g*0x0040,
```

with independent `e,f,g in {0,1}`.  All eight create the same debt packet

```text
0x2879 0x287d 0xa879 0xa87d 0xc879 0xe879.
```

Every member of this packet contains the common core `0x0879`.  More
explicitly it is

```text
0x0879 | 0x2000,
0x0879 | 0x2000 | 0x0004,
0x0879 | 0xa000,
0x0879 | 0xa000 | 0x0004,
0x0879 | 0xc000,
0x0879 | 0xe000.
```

Consequently the selected nineteen-cell fibre has a seven-Boolean front end:
four ghost-breaking bits at `12826`, followed by three provider bits at
`6437`.  The remaining collar problem is not to discover these two roles;
it is precisely to re-host the displayed six `0x0879`-core debts while
respecting all other owners.  This factorization is exact and can be encoded
eagerly before any general collar variables.

## Consequence for the collar search

The strongest strict enlargement of the existing 18-cell collar by one
ghost cell is therefore

```text
[0,5) union [6435,6444) union {12826} union [12869,12873).
```

The fixed gaps on both sides of `12826` have OR `0xffff`, so this added cell
is a literal independent chart relative to the later collar blocks.  It
converts the inherited carrier defect into the explicit two-hole residual
`{2c6d,c679}` and is the correct 19-cell fibre to test before adding a whole
three-cell ghost collar.

Machine replay:

- `scratch/audit_k16_ghost_six_position_surgery_20260731.py`
- `scratch/k16_ghost_six_position_surgery_20260731.audit.json`
