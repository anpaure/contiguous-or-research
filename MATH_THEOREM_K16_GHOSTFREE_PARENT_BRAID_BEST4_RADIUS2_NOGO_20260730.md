# K16 ghost-free parent braid: exact unrestricted radius-two no-go

Date: 2026-07-30  
Status: exact fixed-word theorem; independent witness-core replay  
Global bracket: `12873 <= nu(16) <= 12874` (unchanged)

## 1. Fixed word and conclusion

Let

```text
scratch/k16_ghostfree_parent_braid_best4_20260730.word
length 12873
SHA-256 55b029e30954391d78308412139726bdbf4ebd65b655d79a511f14e1edf24caf.
```

An independent suffix-OR replay gives exactly four holes:

```text
0xc879 = 51321
0xce61 = 52833
0xce63 = 52835
0xe879 = 59513.
```

There is no universal word obtained from this fixed word by changing at most
two distinct cells to arbitrary genuine nonzero 16-bit values.

This is a theorem about this word, not a global length-12873 no-go.

## 2. Complete two-branch partition

Every final witness of an input hole contains at least one changed cell.
Therefore every two-substitution completion is in the union of:

1. **provider-first:** some input hole has a final witness containing exactly
   one changed cell; applying that edit alone already supplies the hole;
2. **all-joint:** every final witness of every input hole contains both changed
   cells.

The branches may overlap computationally, which is harmless. Their union is
exact.

## 3. Witness-core provider theorem

For a covered target `t`, let its source witness intervals be
`[a_i,b_i]`. The positions whose alteration can destroy every old `t`
witness form the witness core

```text
[max_i a_i, min_i b_i],
```

when the left endpoint does not exceed the right endpoint. Thus a first edit
at `p` can eject `t` only when `p` lies in this core.

At such a position let `C_p(t)` be the OR of the maximal `t`-compatible
suffix before `p` and prefix after `p`. Replacing the cell by `u` supplies
`t` exactly on the Boolean interval

```text
t minus C_p(t) subseteq u subseteq t,  u != 0.
```

Consequently the exact first debt set is obtained without retaining the
injective signed column:

* an input hole remains a debt precisely when `u` is outside its provider
  interval;
* a covered target becomes a debt precisely when `p` is in its witness core
  and `u` is outside its provider interval.

For this word the exact core census is

```text
covered targets                 65,531
targets with nonempty core      51,323
target/position core incidences 167,283
maximum core length                  8.
```

This is the positional compression missing from the literal signed-column
quotient: the transition-to-holes depends only on short witness cores and
Boolean provider intervals.

## 4. Source-seeded second-position theorem

Let `D(p,u)` be the exact nonempty debt set after a first provider and put

```text
U = intersection D(p,u).
```

Any completing second value is a nonzero submask of `U`. Hence `U=0` is an
exact rejection. Choose any debt `h` and write `R=h minus U`. A second
position `q` can service `h` only if

```text
R subseteq C_q(h).
```

The positions satisfying this predicate in the source word are cached by the
pair `(h,R)`. A first edit at `p` can change the predicate only inside the
source or edited `h`-compatible component touching `p`, together with its two
boundary positions. Adding exactly those component positions to the cached
source list is complete.

At every retained `q`, the exact common second-value interval is

```text
L_q = union over d in D(p,u) of (d minus C_q(d)),
L_q subseteq v subseteq U.
```

Thus `L_q subseteq U` is necessary and sufficient to supply all current
debts. An exact two-site multiplicity delta is needed only after this test.

The complete census is

```text
genuine first provider values             151,827
first actions with nonzero debt intersection 147,887
cached source-position visits            5,591,474
affected-component additions               371,830
positions with L_q subseteq U                     0
second values                                      0
exact pair-delta checks                             0.
```

Therefore the provider-first branch is empty before any pair collateral
check. The one-thread and eight-thread signed-delta runs agree on every core
count and on the full debt histogram. A separate implementation derives the
same first debts from witness cores rather than signed columns and again finds
zero common second position.

## 5. All-joint obstruction

The common hole mask is

```text
I = 0xc861 = 51297,
```

with six set bits. In an all-joint completion both endpoint values and their
OR `z` are nonzero submasks of `I`. There are exactly `12,935` positional
supports whose strict interior is a submask of `I`.

For a support `p<q` and a hole `h`, let `C_h(p,q)` be the maximal unchanged
`h`-compatible context around the two endpoints and put

```text
M(p,q) = union_h (h minus C_h(p,q)).
```

A combined value exists only if `M(p,q) subseteq I`. Independent replay shows
that every one of the `12,935` supports forces at least two bits outside `I`:

```text
supports with M subseteq I     0
minimum forced outside bits    2
ordered replacement pairs      0.
```

Thus the all-joint branch is empty before private-target collateral checks.

## 6. Composition and scope

The provider-first/all-joint dichotomy is complete, and both branches are
empty. This proves the fixed-word radius-two theorem.

The H100 CPU runs were explicitly capped and used no GPU:

```text
provider, 8 cores: 0.82 s wall, 30,720 KiB maximum RSS
provider, 1 core : 1.71 s wall, 12,288 KiB maximum RSS
core replay, 1 core: 1.11 s wall, 8,192 KiB maximum RSS
all-joint, 1 core: 1.89 s wall, 9,216 KiB maximum RSS.
```

No result here excludes a different length-12873 word or three or more
substitutions.

## 7. Artifacts

```text
scratch/search_k16_provider_first_seeded_exact_20260730.cpp
  SHA-256 ee0623fdf3b2ba5cbb230bbef97c6809eeb128949a690472970f17b8579e2468

scratch/audit_k16_ghostfree_best4_provider_core_independent_20260730.cpp
  SHA-256 70cf6737f1cc3e5cbf0b54d8799ffe11eb634b7d29fdd9f8943692db8214dc4c

scratch/audit_k16_ghostfree_best4_radius2_exact_20260730.py

scratch/k16_ghostfree_best4_radius2_exact_20260730/audit.composed.json
  payload af57b0e6438f1e11252ac5991a0ccbd2700b90f8d1c260669f36983b866843c2
```

The composed audit authenticates both implementations, the one/eight-thread
runs, the independent all-joint lower-mask replay, and the exact branch
composition.
