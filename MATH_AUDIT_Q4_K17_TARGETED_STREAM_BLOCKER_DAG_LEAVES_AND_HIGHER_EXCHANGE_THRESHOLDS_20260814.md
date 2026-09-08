# Audit of targeted q4 blocker-DAG leaf streams and higher-exchange thresholds

**Date:** 2026-08-14

**Verdict:** PASS on the exact symbolic and finite-replay scope stated in the
source theorem.

**Audited source:**
`MATH_REDUCTION_Q4_K17_TARGETED_STREAM_BLOCKER_DAG_LEAVES_AND_HIGHER_EXCHANGE_THRESHOLDS_20260814.md`,
H100 SHA-256
`f3bdf3d11133286fa44f2f9c04833c8a61603ea28c297563535f432bc5fc74b4`.

## 1. Hostile mathematical read

The following claims were checked independently against their definitions.

1. The directed incoming score
   `h_Q(C)=a(C)-2 sum_(j in Q)|C intersect P_j|` is the exact linear part
   of the quadratic exchange identity.  The theorem correctly retains the
   literal row mask for incoming/incoming intersections.
2. `B_C subseteq R` if and only if `C subseteq F(R)` follows in both
   directions directly from the selected supports outside `R`.
3. Inclusion-minimal blocker masks preserve blocker-DAG reachability, but
   do not preserve a leaf exact-cover menu.  The proof makes only this
   reachability claim.
4. The leaf theorem explicitly assumes incumbent row loads in `{0,1,2}`
   and a vertex cover of the load-two defect multigraph.  The outside
   family is then simple.  It has
   `680-(4|G|+10p)` occupied rows, hence
   `|F|=4|G|+10p`.  Every destroyed self group uses its full legal menu,
   including a reselectable incumbent option.  The Algorithm-X induction
   is therefore an if-and-only-if statement, including redundant removal
   masks.
5. In an interleaved row branch, completeness requires every eligible self
   option through the row and every eligible reflected-pair mask.  The
   theorem does not mistake `zero_groups=[]` for an empty destroyed-group
   set.
6. For a declared finite candidate universe, sorting by the indexed pair
   `(h_Q,index)` gives every distinct-candidate exclusion minimum from the
   first `k` entries.  The second pass emits a separate `(C,Q,h_Q(C))`
   record for every face passing the singleton cut.  The theorem explicitly
   declines any completeness claim beyond the pass-one universe.

The hostile reread found no remaining mathematical, scope, or wording
defect after these points were made explicit.

## 2. Implementation binding

The exact anchored generator and generic catalogue replay used for the five
finite batches are:

```text
861527ebce2d0f6a3aa7edbb070dd5e57ddb832f5a9786bcd12483d904d4db14
  scratch/search_q4_k17_owner_targeted_reflection_pairs_20260814.cpp

2874480130e9e27a71115f82f00c3f4b234da9a8f94b4b9922d8b9a20b57560c
  /dev/shm/search_q4_k17_owner_targeted_reflection_pairs

06ca9ee092cca5c1f540678067584eb9065fe9491bf7aa5d9169fc6559078c19
  scratch/audit_q4_k17_owner_targeted_allowed_emitall_20260814.py

b33cfea93b652967ac2efe4bffd37805060653fb18f97555de2cd6abe61486b6
  scratch/audit_q4_k17_targeted_stream_five_allowed_emitall_rebind_20260814.h100.out
```

The source's raw anchored parameterization and mask completeness were
already proved and hostile-audited in the frozen owner-targeted generator
theorem.  Here the independent Python replay does not independently
enumerate the approximately sixty-one million raw anchored parameters; it
exhaustively reconstructs and validates every row of each emitted
deduplicated catalogue and checks its absence from the stated input pool.
The final combined replay named above reran all five catalogues on H100
after the theorem's last wording repair and returned PASS on
`25+23+75+36+120=279` literal witnesses.

## 3. Five H100 structural-node batches

Every hash below was recomputed on H100.  The `catalogue` artifacts live in
`/dev/shm`; the hash, rather than workspace persistence, is the binding.

### 3.1 Root, target row 14, `|F|=162`

```text
structural artifact:
8810202b27544ae90fb7fc2a98bda2658c3ab62e114dffd50ac48af88f1f8646
  scratch/audit_q4_k17_z17_augmented255k_sampled_root_first_structural_20260814.h100.json
primary report:
ee019af8e096efab88f013e25a41c619da47a1ce669e769ff16c7f1bdea3d88b
  scratch/search_q4_k17_owner_targeted_reflection_pairs_aug255k_leaf_root0_row14_emitall_20260814.h100.out
catalogue:
aff3369ca811bfe9cb5c1ac756a44a6f90bc4e9fd5ff3f19be9e2bdec52283be
  /dev/shm/q4z17_aug255k_leaf_root0_row14_emitall.tsv
independent replay:
9829104ddc29b3925d5fe75537410b533bd5a6de6af76bef72c9427a8a5ea8bc
  scratch/audit_q4_k17_owner_targeted_allowed_emitall_aug255k_leaf_root0_row14_20260814.h100.out
```

Primary counts: 50 allowed raw rails, 25 distinct masks, 25 new.  Literal
replay: PASS on all 25.

### 3.2 Root continuation, target row 42, `|F|=162`

```text
structural artifact:
a15e15cff4852e84a3f59ca76e2e009fd99a8ce7619258451c8601ae82bdae3c
  scratch/audit_q4_k17_z17_augmented255k_leaf25_trial0_structural_20260814.h100.json
primary report:
1988813d51a578597af761c530b232f7a1457d5741c88ad323f8a7af83e4e79c
  scratch/search_q4_k17_owner_targeted_reflection_pairs_aug255k_leaf25_row42_emitall_20260814.h100.out
catalogue:
1bd715beee5279f2353394ee412ce59b452c2eabe5240a0c3288d01967f9731d
  /dev/shm/q4z17_aug255k_leaf25_row42_emitall.tsv
independent replay:
076f207769c3b05e20e44871be31995f2d8d1a216917f3a6b0b79a48cb83f182
  scratch/audit_q4_k17_owner_targeted_allowed_emitall_aug255k_leaf25_row42_20260814.h100.out
```

Primary counts: 46 allowed raw rails, 23 distinct masks, 23 new.  Literal
replay: PASS on all 23.

### 3.3 Group-positive child, target row 228, `|F|=186`

```text
structural artifact:
4ef7ed934bcb361e5ab5aaa73c8d0f325adf04228f4b49b03e96174ccf7e542f
  scratch/audit_q4_k17_z17_augmented255k_leaf48_root0_group14_23_child0_group5_first_child_20260814.h100.json
primary report:
cbeaad6244eafe68a1bc7a7e3e83e10fd8032426beb4482040f58a5c960349b6
  scratch/search_q4_k17_owner_targeted_reflection_pairs_aug255k_leaf48_groupclosed_row228_emitall_20260814.h100.out
catalogue:
9e5dd58296c6d6ac65e50efb20fce6cb144dba2055acfb6bec503d8df2a85ac8
  /dev/shm/q4z17_aug255k_leaf48_groupclosed_row228_emitall.tsv
independent replay:
b3773966965e0cf96353614c386e2e14e203058930807659f4fd391c81be52b7
  scratch/audit_q4_k17_owner_targeted_allowed_emitall_aug255k_leaf48_groupclosed_row228_20260814.h100.out
```

Primary counts: 150 allowed raw rails, 75 distinct masks, 75 new.  Literal
replay: PASS on all 75.  There is no zero-menu self group, but the destroyed
self-group set is nonempty; this is only the pair component of an
interleaved row branch.

### 3.4 Sibling child, target row 625, `|F|=196`

```text
structural artifact:
d45e94482b375b12d68919faa9f55c260e825e69ccfc9b18417a83af18d7685b
  scratch/audit_q4_k17_z17_augmented255k_leaf123_root0_group14_23_group5_child6_structural_20260814.h100.json
primary report:
e0184b779f50594bc195dc0a3198cbe3e364373cbecf8bf11183bc25538af7c2
  scratch/search_q4_k17_owner_targeted_reflection_pairs_aug255k_leaf123_row625_emitall_20260814.h100.out
catalogue:
6db7ce0b630421adf225ddb1cbe6159fb74ad150e252c62a840eeac06cca13fa
  /dev/shm/q4z17_aug255k_leaf123_row625_emitall.tsv
independent replay:
acc1ae7d2877e6ca31e19b49e0b229612710a3af35e6983b74e5a74ce2f4d832
  scratch/audit_q4_k17_owner_targeted_allowed_emitall_aug255k_leaf123_row625_20260814.h100.out
```

Primary counts: 72 allowed raw rails, 36 distinct masks, 36 new.  Literal
replay: PASS on all 36.  Again this is a pair component, not a complete
leaf branch.

### 3.5 Sibling child, target row 89, `|F|=186`

```text
structural artifact:
c993caad8fe2273cb980e98a71d703b488401cf9ab03d3c5c6d7ed49472a7246
  scratch/audit_q4_k17_z17_augmented255k_leaf159_root0_g14c0_g23c1_g5c0_structural_20260814.h100.json
primary report:
72ee59918a4d87c889501054093ee31697669ec68fecbb734c6d964b678d9196
  scratch/search_q4_k17_owner_targeted_reflection_pairs_aug255k_leaf159_row89_emitall_20260814.h100.out
catalogue:
d21bec39a00537e087a77e8abcf39ce616037b52c58caeffe45634cf5bf67c2c
  /dev/shm/q4z17_aug255k_leaf159_row89_emitall.tsv
independent replay:
b26966d3c33a36e76c7e3e66d096b3b3269e96996b2abf4adf47123363591078
  scratch/audit_q4_k17_owner_targeted_allowed_emitall_aug255k_leaf159_row89_20260814.h100.out
```

Primary counts: 240 allowed raw rails, 120 distinct masks, 120 new.
Literal replay: PASS on all 120.  This too is only the pair component of an
interleaved row branch.

## 4. Sharp remaining gate

The exact reduction converts a structural blocker-DAG node into complete
on-demand row menus, and it converts a declared finite stream into a
lossless fixed-depth threshold bank.  It does not yet supply a feasible
full leaf patch, exhaust all blocker-DAG children, or certify the omitted
lower/upper ticket, phase, and residence resources of the emitted owner
columns.  Those are the remaining gates.
