# K16 append-0200 collar `(4,7,3)`: target-closure normal form

## Scope

Fix `scratch/k16_append0200_12874_onehole.word` and permit arbitrary nonzero
16-bit values only at the fourteen zero-based positions

```text
[0,4) union [6437,6444) union [12871,12874).
```

All other cells remain frozen.  The fixed runs already witness 65,492 of the
65,535 nonzero masks, leaving an ordered residual set `R` of 43 repair targets.
This note gives an equisatisfiable normal form for that complete fourteen-cell
fibre.  It is not a claim about edits outside the collar and is not an
unrestricted K16 no-go.

## The normalization

For a nonzero editable value `v`, let

```text
S(v) = {t in R : v is a submask of t}.
```

Define the piecewise map

```text
N(v) = intersection S(v),  if S(v) is nonempty;
N(v) = 0x0001,             if S(v) is empty.
```

The second line is intentionally not the empty-meet convention.  Such a `v`
is *dead*: no interval witnessing a target in `R` can contain that cell.
Moreover `N(0x0001)=0x0001` for this target family.

### Theorem

If an assignment in the fourteen-cell fibre witnesses every target, then
normalizing every editable value with `N` also witnesses every target.
Consequently, feasibility of the unrestricted fibre is equivalent to
feasibility with every editable value in

```text
D = {v != 0 : S(v) != empty and v = intersection S(v)}.
```

Here `|D|=150`.

### Proof

Choose any residual target `t` and one concrete interval whose OR is `t`.
For each editable cell value `v` in that interval, necessarily `v` is a
submask of `t`; hence `t` belongs to `S(v)`.  Therefore

```text
v is a submask of N(v), and N(v) is a submask of t.
```

Replacing `v` by `N(v)` cannot introduce a bit outside `t`.  Every introduced
bit already belongs to `t`, and because the original interval OR was exactly
`t`, that bit was already supplied somewhere in the interval.  The interval
OR consequently remains exactly `t`.

A dead value belongs to no residual-target witness at all, so replacing it by
`0x0001` cannot destroy any chosen residual witness.  The argument applies
simultaneously to all 43 residual targets.  The other 65,492 targets retain
their witnesses wholly inside frozen runs.  Thus normalization preserves
universality.  Every value in `D` is fixed by `N`, proving the equivalence.

## Independent finite audit

The audit reconstructs the 43 targets without importing the emitter and then
checks the theorem kernel over all 65,535 nonzero values and all 43 targets.
There are 9,647 live values, 55,888 dead values, and 24,039 actual
value-target containments; every live containment satisfies

```text
v subset N(v) subset t.
```

Two independent domain derivations agree:

1. scanning all masks for fixed points of the container-intersection map; and
2. closing the 43 targets under pairwise bitwise intersection.

Both give 151 fixed intersections including zero, hence exactly 150 allowed
nonzero values.  An independently generated Horn/negative domain CNF has 224
clauses and 756 literals per cell; exhaustive truth-table evaluation over all
65,536 masks shows that its models are exactly `D`.

Four incumbent cells are not closed: positions `0`, `1`, `12872`, and
`12873`.  This observation is about the chosen normal form only.

## Frozen strengthened encoding

The unsolved strengthened CNF uses the 150-value domain, shared exact
interval-OR variables, and deterministic witness equivalences.  For the
frozen input it has:

```text
43 repair targets
44 active editable blocks
480 interval-OR variables
1,892 original dominated-minimal terms
1,862 retained terms
30 redundant non-singleton terms removed for target 0x8000
2,566 variables
34,801 clauses
102,628 literals
```

No SAT solver was invoked on this strengthened CNF.  It is retained as an
authenticated normal-form artifact, not as an UNSAT result.

## Exact-change caveat

`N` preserves feasibility but need not preserve whether a cell equals its
incumbent value.  Therefore the 150-value restriction is valid for the full
unbounded fibre, but must not be inserted into an exact Hamming/change-count
face without a separate count-preservation argument.

## Artifacts

```text
scratch/k16_append0200_12874_onehole.word
  SHA256 aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18
scratch/k16_append0200_phase_collar_4_7_3.positions.txt
  SHA256 f18ab34ea0f6be18c038ae4c52ba62ea931671925b2d7cd9a9513a9de5692118
scratch/k16_append0200_collar473_closure_strengthened_cnf_20260730.cpp
  SHA256 1a98c4a85145d6dd7dee3647b575cf5d6fb92dc6160c2ec71425ee1f4ddee29c
scratch/audit_k16_append0200_collar473_closure_normalform_20260730.py
  SHA256 683bdc787077c0ae8a6146d19c15a50b51d5782bc8dd7d0697dec9f0c3c1f344
scratch/k16_append0200_collar473_closure_normalform_20260730/audit.json
  SHA256 ee5a598f2ca68a5af9674adfb579b770aa63062790c0f89ca707fd457c89a381
  payload 0de897a2a06cffcf0b076947c57ffa4b9108fb242fd9b6b3821fbfad6d589bc0
scratch/k16_append0200_collar473_closure_normalform_20260730/model.cnf
  SHA256 108b2992a0e6c6796e40da43f703081c3e3b06c3c72d8561fb34a53ea60a3690
scratch/k16_append0200_collar473_closure_normalform_20260730/model.map
  SHA256 f3212c4fce5d5d2eaa2eb1e371207a552972cdb7a92eadd203e74d6d8e29593f
scratch/k16_append0200_collar473_closure_normalform_20260730/model.stats.json
  SHA256 a0fa18f12adf3def4d5c1efbb8ac709050b617b589ca290470320426e095e044
```
