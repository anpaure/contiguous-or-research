# K16 H1 joint13: 22 exact hole-action units from four-collar capacity

Date: 2026-07-30  
Status: **GO, exact and solver-independent in the frozen joint13 fibre**

## Theorem

Let `H=0x2c6d` be the sole residual hole in the authenticated thirteen-cell
H1 fibre.  Number its 29 one-block actions by their witness indices `0..28`.
Then the following 22 actions are impossible:

```text
0,1,2,3,4,5,7,8,9,10,11,12,13,14,16,17,18,19,22,23,25,26.
```

Equivalently, before using any SAT result, the only actions not excluded by
this theorem are

```text
6,15,20,21,24,27,28.
```

This is a theorem only for arbitrary nonzero substitutions on the frozen
thirteen positions.  It does not normalize arbitrary length-12873 words into
this support and is not an unrestricted K16 no-go.

## Proof

Choose a valid one-block chart for each of the 55 residual targets.  In every
one of the four disjoint collars, replace each physical cell value by the
intersection of the target labels of the selected charts which cross it,
using `0xffff` when none crosses it.  This preserves every selected chart.
Thus every cell lies in the exact 216-state meet closure of the target labels.

For interval OR `U`, target `T`, and residual need `N`, validity is exactly

```text
U subseteq T  and  N subseteq U.
```

Exhausting all `216^2`, `216^4`, `216^3`, and `216^4` cell tuples gives the
generic per-collar target capacities

```text
7, 23, 14, 12.
```

The same enumeration records, for each action of `H`, the maximum capacity
of the collar containing that selected action.  In witness-index order these
conditional capacities are

```text
5,5,5,
12,16,20,23,14,18,21,14,17,13,
9,12,14,9,12,8,
10,12,11,8,9,11,9,10,11,11.
```

Because `H` is assigned to its selected collar, it is excluded from the
capacity count in each of the other three collars.  Their sharp generic
capacities happen to remain `7,23,14,12`.  Adding the selected-collar
capacity to the other three gives

```text
54,54,54,45,49,53,56,47,51,54,47,50,46,51,54,
56,51,54,50,54,56,55,52,53,55,53,54,55,55.
```

Every target chooses exactly one collar, so its four collar assignments form
a partition.  Any total below 55 contradicts the 55-target demand.  Exactly
the 22 displayed actions have total capacity below 55, proving their units.
Totals 55 or 56 are deliberately reported as inconclusive.

As a calibration, action 2 is the former `x467` singleton state.  Its total
is `5+23+14+12=54`, exactly reproducing the independently established
`not-x467` theorem.  The new table also predicts every conditioned branch
already eliminated by a retained DRAT proof.

## Authentication

Primary all-action enumerator and run:

```text
source
  fea8ec9dd893a072d6a7e695d7d8ab38b163d8e29553bd3e06e825d3380f4552
binary
  1b14b00ec8297e2a17239ec7c1c18f1db5601c5a28ce01cadee6176bd64f65f2
result
  87731d5c50fcda00163e4e82412657359ccf5179ac011b4ce67cd0a45b6eea3d
resource record
  e9066718e5420d637504f3e5ca0e37ac529c46a3ac0cb4d380859f08b6d78643
```

It exhausted all 4,363,641,984 tuples in 41.83 seconds on one H100 CPU core,
using 9,084 KiB maximum RSS.

A second independently written enumerator, which additionally retains
maximizing tuples and covered-target sets, has source and result hashes

```text
b2a4a333ea0eea53d617319ef74a7cfee685cf368fc1e84195e52115059d3a8d
1cf38f49743dce287d3151f60b88831e9bc8cbf8d8c74802a33edb4ad5a46e54
```

Finally, a structurally different generic mixed-radix odometer reads a
separately prepared TSV ledger and recomputes interval ORs from their literal
endpoints.  It exhausted the same tuple census in 304.13 seconds and matched
every generic capacity, every conditioned capacity, every total, and every
learned unit:

```text
generic replay source
  0eab5f17fb7f0c571376a9408f39d72c2c7081471a63fba16f3429f126e6e5f8
generic replay result
  935fda6ca7d0ef5a19f87bcb6f98c851257a83fd4a918230900a13366ebe9df3
independent preflight
  2b0efe79f9265e78a8564e03201d3cfaa28f4710df85e3fe0a16c5384cfbcd92
independent audit
  6491960cdd5137972a273ff89943d83ec8cfc9c4f3590c54d8b67d291b7fa3c9
independent audit payload
  881b0ad60f53695df57771bb27f698fdf207000c866086c4f74010a969e5b14e
```

No SAT solver verdict is used in this 22-unit proof.
