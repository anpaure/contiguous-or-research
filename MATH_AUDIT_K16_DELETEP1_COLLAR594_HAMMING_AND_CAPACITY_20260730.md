# K16 delete-p1 collar594: Hamming semantics and exact third-block capacity

Date: 2026-07-30

## Frozen fibre

The source is the authenticated length-12,873 delete-p1 word

```text
scratch/k16_upper12874_delete_p1_optimal_onehole.word
SHA-256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
```

with sole hole `0x2c6d`.  The editable positions are

```text
[0,5) union [6435,6444) union [12869,12873),
```

of widths `5,9,4`.  The complement is frozen.  The target-intersection
closure normal form has 245 nonzero values and is equisatisfiable with this
unrestricted 18-cell fibre.

## Independent encoding audit

`scratch/audit_k16_deletep1_collar594_hamming_and_hintflip_20260730.py`
reconstructs the closure-normalized source, every mapped auxiliary variable,
the full literal-polarity transform, and each raw-incumbent conditioned CNF
for bounds 3 through 11 without importing either emitter.

The audit performed

```text
1,179,630 exhaustive coordinatewise normalization checks
2,359,296 exhaustive 16-bit changed-indicator truth-table checks
exact ordered-clause reconstruction of b3,...,b11
```

and obtained

```text
expected full-hint CNF SHA-256
  a160a88600f74db7b0228ec8a3201a3bf289214cad4da6d79d874d5c8b2805ba
flipped variables 610
violated clauses under the normalized source [16649]
```

Clause 16649 is the unique coverage row for `0x2c6d`.  Thus the all-false
assignment of the transformed CNF is exactly the closure-normalized source
and violates one clause.

Audit artifact:

```text
scratch/k16_deletep1_collar594_changebound_audit_20260730/audit.json
payload d8c13e878a5a7e1601ee730cf145fe0d818c41455afb56099353c6ca6f9bf56b
```

## The one-unit Hamming distinction

Seventeen source values are already closure fixed.  The exception is

```text
flat cell 15, physical position 12870: 3 -> 3171.
```

Let `s` be the raw source, `N(s)` its coordinatewise normalization, and `y`
any closure-normalized candidate.  Then

```text
dist(y,s) = dist(y,N(s)) + 1[y_15 = 3171].
```

Moreover, exhaustive coordinatewise checking proves

```text
dist(N(x),N(s)) <= dist(x,s)
```

for every arbitrary nonzero raw candidate `x`.  Consequently:

* a conditioned bound `B` measured from the **normalized** source excludes
  arbitrary physical radius `B` when UNSAT;
* the newer conditioned bound `B` measured from the **raw** source uniformly
  excludes arbitrary physical radius `B-1` when UNSAT.

This distinction is essential when stating the result.  It does not weaken
the earlier normalized-hint physical-radius-six theorem.

## DRAT-verified conditioned faces

The independently reconstructed raw-incumbent formulas at bounds 3, 4, 5,
and 6 are UNSAT with retained DRAT proofs and `drat-trim` exit zero.  In
particular the fresh bound-six replay has

```text
CNF SHA-256   d8d952eb0b11f76bc5d2890890b8f43432d6a5db6440e1ffe91ea1001d7218be
DRAT SHA-256  a3258580ea8723d333f18dad45ece7be3ff8612dad6607f5d86e86899856b84b
proof bytes   193,595,341
resolution steps 278,959,656
drat-trim     s VERIFIED
```

By the preceding paragraph, this fresh bound-six theorem has the conservative
physical scope `radius <= 5`.  The older normalized-hint radius-six proof has
the stronger physical scope `radius <= 6` and remains valid.

The raw-incumbent bound-seven solver also returned UNSAT, but its independent
DRAT replay reached the 3,600-second resource cap (`exit 124`) without a
verdict.  It is therefore **not** promoted as a theorem in this note.

## Exact capacity of the final four-cell block

The final collar occupies flat cells 14 through 17.  The independent C++
replayer

```text
scratch/replay_k16_deletep1_collar594_block2_capacity_20260730.cpp
```

enumerated all

```text
245^4 = 3,603,000,625
```

closure-domain assignments.  For each assignment it reconstructed all ten
contiguous interval ORs and all 604 target-witness conditions directly from
the frozen map.  The exact maximum number of distinct residual targets that
this block can witness is

```text
15,
```

attained by exactly four assignments.  One lexicographic witness is

```text
[35938, 2145, 50209, 18033].
```

This agrees with, but does not rely on, the CP-SAT `OPTIMAL 15` diagnostic.
The exhaustive run used 8.7 MiB peak RSS and 6.92 seconds on one H100 CPU
core.

A second exact census found

```text
2,923,957 distinct coverage sets
414,825 inclusion-maximal coverage sets
```

and no forbidden pair, no minimal forbidden triple, and no minimal forbidden
four-set.  Thus the simple cardinality-15 inequality is the first useful
low-complexity projection cut; pairwise through four-wise compatibility is
complete.

The first nontrivial compatibility constraints occur at size five.  Of the
`C(61,5)=5,949,147` five-target sets, exactly `4,253,683` are forbidden for
the final block.  A randomized search over this **exact** forbidden family
found two 23-target sets every five-subset of which is forbidden.  An
independent stream replay against all 414,825 inclusion-maximal achievable
block-coverage masks proved

```text
max |coverage intersect S| = 4
```

for both sets.  Thus each gives the compact exact inequality
`sum_{t in S} u_t <= 4`, much stronger locally than enumerating its 33,649
forbidden five-subsets.  The replay payload is

```text
97a6ee67e4c37c2e88842e98c78fcd8dd62bd8fa65a2232d7dde76124a337afc
```

This is a proof of the displayed projection inequalities, not a proof that
the full 18-cell fibre is infeasible.

The size 23 is optimal for this particular five-wise-incompatibility
construction.  There are `1,695,464` realizable five-target sets.  A CNF with
one selector for each residual target, one negative five-clause for every
realizable five-set, and a standard sequential counter requiring at least 24
selected targets is UNSAT.  The retained proof checked independently:

```text
CNF variables / clauses  2,281 / 1,699,927
CNF SHA-256              190239cb925d07ce5146f8841e7fccab5818703d75846aa5c494135c3f58ec15
DRAT bytes               16,300,261
DRAT SHA-256             06fa4f99e5b58db7df2208dffbe4860ad64194267e29a00dc8e2a03af53f440d
drat-trim                 exit 0, s VERIFIED
checked resolution steps 8,840,928
RAT lemmas                0
```

This proves only that no 24-target set has *every* five-subset forbidden.
It does not say that the final block can cover every subset of any 23-target
set, nor does it decide the full collar.

For a proof-oriented decision lane, all `4,253,683` forbidden five-target
patterns were also appended directly as five-literal clauses on the `u_t`
variables.  This exact first-incompatibility-layer formulation has

```text
6,299 variables
4,335,856 clauses
CNF SHA-256 2fa22b0a15b909d0e65303cedd6cb97cabb248e24d3ec7e7a2234d416b5ca5f8
```

An independent streaming reconstruction matched every byte; audit payload:

```text
873786f8b7a019c0db48e3f247620d22bf13a133f0a016fe1f57bd196c7cafd1
```

These clauses are redundant consequences of the exact four-cell coverage
family.  They strengthen propagation without restricting the 18-cell fibre.

## Exact capacity strengthening

For every residual target `t`, define `u_t=1` exactly when neither the 5-cell
nor the 9-cell collar witnesses `t`.  Full coverage forces every such target
to be witnessed by the final four-cell collar.  The capacity theorem gives

```text
sum_t u_t <= 15,
```

equivalently, the first two collars must jointly witness at least 46 of the
61 residual targets.

The full-hint CNF strengthened by this theorem has

```text
6,299 variables
82,173 clauses
CNF SHA-256 89cd7107c5612211a54592cc40c4deb0af9b5b18737a7efc14712c36f78e24c4
```

It uses exact `u_t` equivalences and a 1,845-clause Sinz at-most-15 counter.
An independent audit reconstructed all 5,520 added clauses byte for byte:

```text
scratch/k16_collar594_hintflip_block2cap15_cut_20260730/audit.json
payload e76f9b44f9a5d5a6f0f5834a53681650cfab43d006b97c64dd9c54f7ddcb7967
```

This is an equisatisfiable strengthening of the whole 18-cell fibre, not a
heuristic restriction.

## Current decision status

An optimization-form CP-SAT model, used only constructively, rediscovered the
other certified one-hole basin.  Applying its checkpoint to the frozen word
changes five physical collar cells, covers the original hole `0x2c6d`, and
leaves exactly `0xa86d`.  A completely independent literal replay over all
65,535 targets gives

```text
candidate word SHA-256 62db11e721ff5a4e36de6e36594dedccab10e229e5c272efc9674c0e330eef46
audit payload          8e92d8ff8bf5827f0f11bf393353d5a5b2dd4bec77e75a9bcb3598fdd7460966
```

The exact closure CNF was polarity-transformed around this second state.
Its all-false assignment violates exactly clause 44,891, corresponding to
residual target `0xa86d`:

```text
portal-centred CNF SHA-256 a44ceb12e7004c4f28e70a30da5b79a95a378f49f1e3f97395db6530c2a26ee3
manifest payload           d6d0545e583e9ca28344b3a356a10a94f0fedb421650a58b160403b0ee8528eb
```

This is a new exact phase centre, not an improvement in word length.

No SAT model has yet been returned.  One root unbounded closure run reached
its resource limit and is `UNKNOWN`; independent unbounded portfolios remain
active.  Active exact searches include phase-false unbounded formulas and
normalized-hint radius 7, raw-incumbent bounds 8--11, the capacity-15 and
23-target-clique strengthenings, the all-forbidden-five strengthening, and
an independent full CP-SAT model.
Any SAT output must still be unflipped, checked against every DIMACS clause,
decoded into the 12,873-cell word, and replayed against all 65,535 nonempty
targets before it is a certificate.
