# K16 ejection H1: exact all-three and two-site-plus-one radius-three no-go

Date: 2026-07-30

## Frozen source and exact scope

The source is

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
length 12873
sole hole B = 11373 = 0x2c6d.
```

Every three-substitution completion has a final literal `B` interval meeting
one, two, or all three edited positions.  This note closes the last two
classes.  It does **not** close the remaining one-site-plus-two-repair class,
and it is not an unrestricted K16 no-go.

## 1. All-three-site branch

For sites `p<q<r`, every unchanged cell of `(p,r)\{q}` must be a submask of
`B`.  The exact source census has 13,779 possible supports:

```text
span 2: 12871
span 3:   769
span 4:   121
span 5:    18.
```

For a fixed support, call a target private when every source witness meets
the three sites.  Each new affected witness belongs to one of the six
consecutive site classes

```text
p, q, r, pq, qr, pqr.
```

If the three final values are `B` submasks, a necessary relaxed condition for
a private target `T` is the existence of a fixed base `F` with

```text
F subseteq T subseteq F OR B.
```

This deliberately independent-target relaxation excludes 13,772 supports.
The same seven consecutive triples survive as in the independently audited
best-deletion basin.  An exact 8-bit OR-state DP then shares the three values
across every private-target form and empties all seven state spaces.  The DP
allows source values and is therefore stronger than the genuine-three-edit
claim.

Thus no completion exists whose final `B` witness meets all three edits.

Artifacts:

```text
scratch/audit_k16_ejection_h1_allthree_solverfree_20260730.py
  a49ff0007412d6862832898f83aa039597376bfc3f528f49d975760135a3608b
scratch/k16_ejection_h1_allthree_solverfree_20260730.audit.json
  1208e544bf386d3b8e39f85721499d0694c6eb860f34262a9d6eb6a1c6f6e209
  payload 9135ec8a134d74c66ce3f08fe48d4c1def1f5ff66bcc86993ea56883597f1a48.
```

The H100 replay took 4.43 seconds and 305 MB RSS.

## 2. Exact two-site packet

Suppose a final `B` witness uses exactly two edited sites `p<q`.  Every fixed
cell between them is a `B` submask and both new values `u,v` are nonzero
`B` submasks.  Extending through the maximal compatible collar gives the
exact condition

```text
context(p,q) OR u OR v = B.
```

The census has 13,310 positional supports and exactly 105,510,990 genuine
ordered value pairs.  For each pair, the affected-interval/private-target
criterion computes the exact intermediate hole set.  No two-edit completion
occurs; the distribution ranges from two through 28 holes.

## 3. Common-third-position lemma

Let `D` be the exact nonempty intermediate hole set.  At a prospective third
position `t`, remove its incumbent and extend left and right through the
maximal `T`-compatible fixed component.  Let its OR be `c_t(T)`.  A value `w`
supplies every member of `D` if and only if

```text
L_t(D) = OR_{T in D} (T \ c_t(T)) subseteq w
         subseteq U(D) = AND_{T in D} T.                 (3.1)
```

Hence `U(D)=0` is impossible, and otherwise every candidate value is exactly
the nonzero part of the Boolean interval `[L_t(D),U(D)]`, excluding the
incumbent when genuine substitution is required.

Recomputing (3.1) at all 12,873 positions for all 105 million pair states is
unnecessary.  Cache its feasible positions on the source word by the sorted
hole set `D`.  Changing `p,q` can alter `c_t(T)` only when the `T`-compatible
component through `t` contains `p` or `q`.  The complete exceptional set is
the union, over `T in D` and over the source and changed words, of the maximal
`T`-compatible components containing `p` or `q`, enlarged by their immediate
boundary positions.  Outside that set every scan defining `c_t(T)` is
literally unchanged.  Rechecking (3.1) on cached plus exceptional positions
is therefore exact.

An independent implementation compared this optimized position set with a
brute all-position scan on every one of the 367 distinct `(D,p,q)` rows in
the retained two-through-eight-hole bank.  The sets agreed exactly, covering
2,413 feasible positions.

## 4. Exact three-site multiplicity replay

For each candidate `(p,q,t,u,v,w)`, affected intervals split into the six
consecutive nonempty site classes

```text
p, q, t, pq, qt, pqt
```

after sorting the positions.  Each class is the product of two compressed
suffix/prefix OR chains and a fixed bridge OR.  Subtracting its old labels and
adding its new labels gives the exact multiplicity delta.  A candidate is
universal iff the source hole gains a witness and every touched covered target
retains positive multiplicity.

The implementation was independently checked on 200 deterministic random
three-site assignments: for all 65,536 labels, source count plus sparse delta
equalled a fresh complete count.

The complete run gives:

```text
joint pair assignments                    105,510,990
with nonempty common hole intersection    105,028,564
exact candidate third positions             2,308,914
exact candidate third values                9,667,813
universal candidates                                0.
```

The two-hole slice independently agrees byte-for-number with the earlier
specialized audit: 2,072,176 candidate positions and 8,423,912 values.  This
is a useful cross-check on both the cached filter and the full enumeration.

Therefore no three-substitution completion exists whose final `B` witness
uses exactly two edited sites.

Main artifacts:

```text
scratch/search_k16_ejection_h1_two_site_plus_one_complete_20260730.cpp
  d27a231c7516318acec55ffacaeafc6ef632d2be78d645dff95f96f3c18d08ab
scratch/k16_ejection_h1_two_site_plus_one_complete_20260730.audit.json
  7973b6041da36d718e1febae6d183b5181ba41015af8391f865a7b86c21d2e8c
scratch/k16_ejection_h1_two_site_plus_one_complete_20260730.resource.txt
  787e50d613991c81728ede79123fbb057e650f067ccc6c9d6d59f7513e9a7b06
scratch/test_k16_three_site_delta_20260730.cpp
  0e235697c1f25da41ac55b34d6a7ef743d0de7aec93258ec7fb2b26429b16304
```

Independent position-filter audit:

```text
scratch/audit_k16_two_site_plus_one_position_filter_20260730.py
  69ca15e87bc218d25a57825a03157899493d624592c8e4e15db3a05752a9b7cd
scratch/k16_two_site_plus_one_position_filter_20260730.audit.json
  6b1ea38316af0996c549f49f54d04b2dc59050957207122e46365a5b88d4408c
  payload 90d265fb764c7ebe0d5f6a88aed5e97e9b8ca88ad2ea8eb3230bcf7cecbcef40.
```

The strengthened complete H100 run used eight threads, 55.12 seconds wall
time, 419.66 user CPU seconds, and 26,624 KiB maximum RSS.  Exit status one is
the program's intentional exhausted-with-no-solution return.

## 5. One-site portal plus genuinely joint repair pair

The one-site branch begins with any exact one-cell `B` portal.  Rebuilding
the atlas from maximal literal contexts gives exactly 28,805 assignments and
the debt histogram

```text
2:153, 3:8, 4:88, 5:64, 6:162, 7:377, 8:627, 9:1434,
10:2652, 11:4436, 12:4259, 13:4233, 14:4332, 15:2841,
16:1435, 17:988, 18:365, 19:350, 20:1.
```

Suppose neither remaining repair edit individually supplies any current
debt.  Then every final witness for every debt contains both repair sites:
otherwise that same interval would exist after changing its one contained
site alone.  If the exact debt set is `D`, both repair values are submasks of

```text
U = AND_{T in D} T.
```

For repair sites `p<q`, extend the fixed bridge and both flanks maximally
through `T`-submask cells and call its OR `c_{pq}(T)`.  A jointly witnessing
assignment exists only if, and its values `x,y` supply `T` exactly when,

```text
c_{pq}(T) OR x OR y = T.                                  (5.1)
```

Thus support feasibility is decided before value enumeration by
`c_{pq}(T) OR U = T` for every debt.  The complete census gives

```text
portals                         28,805
raw positional supports       372,365,874
structurally feasible supports     49,390
exact value pairs             144,191,783
universal assignments                   0.
```

Only debt sizes two, three, and six survive structurally:

```text
size 2: 49,212 supports; 143,675,934 value pairs
size 3:    176 supports;     509,896 value pairs
size 6:      2 supports;       5,953 value pairs.
```

Every final assignment is checked by the independently tested exact
three-site multiplicity delta.  This strictly contains the earlier 1,341
laminar minimum-debt supports and also includes crossed maximal collars and
provider-first overlap whenever all debts still have a joint witness.

Artifacts:

```text
scratch/search_k16_ejection_h1_one_site_plus_joint_pair_complete_20260730.cpp
  f81d7ac808e9c8f7fa7feb4887ee990e3f09ddedbd16dd0956c9d91f61240bdd
scratch/k16_ejection_h1_one_site_plus_joint_pair_complete_20260730.audit.json
  14aebcd50344894cbd423306299ac0d997571cac66a8b4dfe9ff96aa429244e4
scratch/k16_ejection_h1_one_site_plus_joint_pair_complete_20260730.resource.txt
  06297de102ae2c246f2fdcaa97b85abbb1f8f9b6feb356623f0398915a5d2ea9.
```

The H100 run used eight threads, 2:52.67 wall time, 1009.48 CPU seconds,
and 14.8 MB maximum RSS.

## 6. Exact remaining radius-three class

Only the following mixed provider-repair class remains around this rooted H1
word:

1. one edit supplies `B` through a final literal witness avoiding the other
   two edits; and
2. at least one repair edit individually supplies at least one portal debt;
   and
3. some other portal debt lacks a final witness containing both repair cells,
   so the assignment is not already covered by Section 5.

Equivalently, after a portal choose any debt `T`, any repair site whose final
value lies in the exact one-cell provider interval for `T`, compute the exact
new hole set, and apply the common-last-position Boolean interval (3.1) to
the remaining site.  Enumerating that provider-first mixed bank would give a
complete substitution-radius-three verdict for this H1 word.  No existing
hash-closed artifact covers all 28,805 portal intermediates, so no global
radius-three no-go is claimed here.
