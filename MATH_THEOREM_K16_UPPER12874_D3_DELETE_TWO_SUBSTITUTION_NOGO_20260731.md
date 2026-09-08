# K16 upper12874: exact D3 delete-plus-two-substitution no-go

Date: 2026-07-31  
Lane: D  
Status: exact scoped theorem; H100 census independently composed  
Global bracket: `12873 <= nu(16) <= 12874` (unchanged)

## 1. Theorem and exact scope

Let

```text
U = answers/k16_upper12874.word,
|U| = 12874,
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e.
```

Exactly seven deletions of `U` leave at most three uncovered targets:

```text
d=0:     {0x4879,0x6879}
d=1:     {0x2c6d}
d=3:     {0x146d,0x546d}
d=6389:  {0x4679,0x6a61,0x6b61}
d=6441:  {0x946d,0xa86d,0xd46d}
d=12871: {0x8c67,0x8ce7,0xbcef}
d=12873: {0xce61,0xce63}.
```

For each of these seven post-deletion words, changing two distinct surviving
positions to arbitrary nonzero 16-bit values never gives a universal word.
The already frozen delete-plus-one-substitution theorem also excludes a
no-op at either site.  Hence the conclusion is unchanged whether “two
substitutions” means exactly two genuine substitutions or at most two.

This is the exact `D3` radius-two theorem around the one frozen word `U`.
It says nothing about the other 12,867 deletions, reordering cells, inserting
cells, three substitutions, another length-12,874 parent, or an arbitrary
length-12,873 word.  In particular it does not improve the global lower
bound.

## 2. Exact branch dichotomy

Fix a deletion basin `W`, original hole set `H`, changed sites `p,q`, and
final word `V`.  Every final witness of an original hole meets `p` or `q`,
because a witness avoiding both would already have existed in `W`.
Therefore one of the following holds.

1. **All-joint.** Every original hole has a final witness containing both
   changed sites.
2. **Provider-first.** Some original hole has a final witness containing
   exactly one changed site.  Applying that edit alone already supplies that
   hole.

The authenticated global all-joint theorem exhausts branch 1 for all 12,874
deletions.  The new census exhausts branch 2 on `D3`.  The branches may
overlap; their union is what matters.

## 3. Complete first-provider domain

At a prospective first site `p`, let `C` range over all ORs of a suffix to
the left of `p` and a prefix to its right, including empty sides.  A value
`x` supplies a hole `h` through `p` exactly when

```text
C subset h,
h minus C subset x subset h,
x != 0.
```

The engine enumerates the union of these Boolean intervals over every
`h in H`, deduplicates values at each site, and removes the incumbent.  It
therefore includes partial providers: `x` need supply only one original
hole, and may eject any number of previously covered targets.  Across the
seven basins this is 1,495,532 ordered first-provider records.

After materializing `Z=W[p<-x]`, exact signed interval multiplicities give
its full intermediate hole set, not merely residual original holes.

## 4. Exact second-site reduction

For a target `t` represented in `Z`, intersect all its witness intervals.
At site `q`, define

```text
R_Z(q) = {intermediate holes}
         union
         {represented t whose every Z-witness contains q}.
```

The implementation reconstructs this set without a proxy.  It forms the
exact multiplicity table of intervals through `q`; a represented target is
in `R_Z(q)` precisely when that local multiplicity equals its full
intermediate multiplicity.  Targets absent from the local table have an
avoiding witness and are not demanded.

Put

```text
J_Z(q) = AND of all targets in R_Z(q).
```

For the exact suffix/prefix OR chains in the materialized word `Z`, let
`Gamma_q(y)` be the labels of intervals through `q` after writing `y` there.
Then

```text
there exists nonzero y making the word universal
iff
J_Z(q) != 0 and R_Z(q) subset Gamma_q(J_Z(q)),
```

except that if `J_Z(q)` equals the incumbent, a genuine feasible change may
lie below it.  Feasibility is upward closed within the submasks of `J`, so it
is enough to test the at most 16 nonzero coatoms of `J`.  This is the exact
maximal-value theorem, not the unsafe replacement of `J` by the intersection
of only the intermediate holes.

All chains are built after the first edit.  Consequently an interval through
the second site and first site contains the literal `x OR y` interaction;
no independent-column approximation is used.

## 5. Candidate-position reduction

Let `D` be the intermediate holes and `U_D=AND(D)`.  Any completing second
value is a submask of `U_D`.  Choose a seed hole `t in D`.  Its bits outside
`U_D` must already occur in the maximal `t`-compatible context around the
second site.  All source sites satisfying this necessary condition are
cached.

Changing the first site can alter that context only inside the old or new
`t`-compatible component incident with the first site, or at an adjacent
separator.  The engine adds exactly a superset of those affected sites in
both source and edited states.  Hence every feasible second site lies in the
cached-plus-affected list.  False positives are harmless because the exact
full target core is then tested.

This point was audited independently in
`THREAD_D_AUDIT_K16_PROVIDER_FIRST_SEEDED_POSITION_AND_MAXIMAL_VALUE_20260731.md`.
It is why the old seeded engine's position reduction may be retained while
its all-values second loop is replaced by the true target-core test.

## 6. H100 result

The seven cases ran sequentially with one CPU worker under a 512 MiB address
space limit and a 120-second CPU limit per case.  All seven returned terminal
`PASS_EXHAUSTED_NO_COMPLETION`; no timeout or resource failure occurred.

```text
deletion   first providers   candidate q sites   wall s   max RSS KiB
0                  42,491              13,581     1.69          12,800
1                  27,064             251,932     4.38          18,432
3                  41,749                 266     1.57          13,312
6389               68,555                  12     1.66          11,264
6441              103,102                 169     1.94          14,336
12871           1,133,158               6,107     7.03          13,312
12873              79,413               1,775     1.91          14,336
TOTAL            1,495,532             273,842    20.18          18,432 max
```

There were 268,879 nonzero full target cores, 248,175 maximal-value tests,
93,573 coatom considerations, and 89 literal through-chain tests after the
last deficit filter.  None covered its demanded target set, so no positive
reached full replay.  Absence of a replay is therefore a negative result at
the exact target-core condition, not an omitted verification of a positive.

The first remote deployment failed during compilation because the GCC target
pragma and default target flags disagreed; no case ran.  The retained `v2`
package compiled with `-march=native` and produced all seven terminal rows.
That compile-only failure is not counted as `UNSAT` or as a search result.

## 7. Composition and surviving scope

By the dichotomy, the new provider-first exhaustion plus the authenticated
global all-joint exhaustion proves the theorem in Section 1.  The independent
composer also verifies that every basin is literally the indicated deletion
of `U`, recomputes all seven hole sets from interval ORs, checks all seven
terminal exit codes and resource ledgers, and authenticates the all-joint
certificate.

No length-12,873 word was found.  The useful surviving direction must leave
this exact local ball: use a deletion with at least four holes, at least three
substitutions, a cell reordering/braid, or another parent chronology.

## 8. Frozen artifacts

```text
scratch/threadD_search_k16_upper12874_d3_provider_core_20260731.cpp
  SHA-256 7b1c17bbd1276a8cd4184e47f56dc4e6c66f84cc084bd155a4896ec308acd9aa

scratch/threadD_run_k16_upper12874_d3_provider_core_h100_20260731.sh
  SHA-256 40bcee9668a3e0b237667fa9089b9cfe04cf045c5f38219bbbb99bfeb559a51d

scratch/threadD_audit_k16_upper12874_d3_radius2_20260731.py
  SHA-256 b8b8109511f0b91f1e70c8607a3402e1867fb1d2e3f0e8244aa45e93ca07eb49

scratch/threadD_k16_upper12874_d3_radius2_20260731/independent.audit.json
  SHA-256 181b5c90bdfe8be692baa9f25121cf68e11787d3c987286598a7c10ce7648e0e
  payload 8d4ff5ffd4492c37da18484cbce9b0a4ca57d0fa64fa2a695e210e879785394e

THREAD_D_K16_UPPER12874_DELETE_TWO_SUBSTITUTION_TARGET_CLOSURE_MITM_20260731.md
  SHA-256 2c01d5ce6437a5d8236763426611906d980185a222134c52bd09f88ce1a8e919

THREAD_D_AUDIT_K16_PROVIDER_FIRST_SEEDED_POSITION_AND_MAXIMAL_VALUE_20260731.md
  SHA-256 1683401b58564ec5339f69425275705a37082fb90df63f8e0e179d8fa10ac4e6

scratch/k16_upper12874_delete_two_sub_alljoint_global_exact_20260730.independent.audit.json
  SHA-256 e0303b3bef80d14e9bde85863347b6c78947b212eb159bac77cac005bb29bcd0
```
