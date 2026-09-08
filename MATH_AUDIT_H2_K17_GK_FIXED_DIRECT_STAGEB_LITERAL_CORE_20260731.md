# Independent audit of the K17 adjacent-cut fixed-direct Stage-B no-go

Date: 2026-07-31  
Status: **GO, with corrected scope**

## 1. Exact verdict

For the fixed `7abc` bank, the reported Stage-B round-zero infeasibility is
real, but its status label is misleading.  Round zero contains no component,
ear-shape, ear-length, cycle, or connectivity cuts.  More strongly, all
rank-nine equations and `AllDifferent` rows can be deleted, as can the three
aggregate totals, and the remaining system is still infeasible.

The surviving four families are only

\[
 d_F(D)\ge1,\qquad d_F(Q)\le1,\qquad d_F(b)\le1,
 \qquad d_F(u)\in\{0,2\}.                       \tag{1.1}
\]

Here `D` ranges over the residual required rank-six colours, `Q` over fresh
rank-eight colours, `b` over residual base vertices, and `u` over unused
rank-seven vertices.  The family-level assumption core is exactly

```text
q8_rainbow + q6_cover + base_cap + unused_degree_{0,2}.
```

It excludes the selected-edge total, base-incidence total, and selected-U
total.  Thus neither the proposed `2637/430` length split nor any other ear
schedule participates in the contradiction.

The old master does eagerly delete edges whose boundary rank-nine label
collides with the fixed direct bank.  The independent replay below also
reconstructs the larger catalogue with this deletion disabled and verifies
that the same 26 local rows and their complete incidences are unchanged.
Consequently the small proof is genuinely q9-filter-free, even though it was
first extracted from the old master.

## 2. Subset-minimal 26-row core

The literal rows, in hexadecimal, are

```text
q6:   7403 7405 7409 7411
q8:   740f 7417 741b 7427 7447 7487 7507 7607 7c07 f407 17407
base: 7415 7419
U:    740b 7423 7443 7483 7503 7603 7c03 f403 17403
```

The eight outer U vertices

```text
7423 7443 7483 7503 7603 7c03 f403 17403
```

each have exactly six catalogue edges, all under their single corresponding
upper colour

```text
7427 7447 7487 7507 7607 7c07 f407 17407.
```

Upper capacity one and degree in `{0,2}` force all eight degrees to zero.
After deleting these star options, put

```text
F=740f, G=7417, H=741b, X=740b.
```

Every edge at `X` has colour `F` or `H`, seven of each.  The last required
row `7411` has exactly two options.

* If it uses `(7413,7415)` of colour `G`, base cap `7415` forces row `7405`
  to `(7407,740d)` of colour `F`; row `7403` is then forced to
  `(740b,7413)` of colour `H`.  Vertex `X` has degree one, while both possible
  colours for a repairing X-edge are already saturated.
* If it uses `(7413,7419)` of colour `H`, base cap `7419` forces row `7409`
  to `(740b,740d)` of colour `F`; row `7403` is then forced to
  `(7407,7413)` of colour `G`.  Again `X` has degree one and both `F,H` are
  saturated.

This is a solver-free contradiction.  The audit additionally runs a tiny
exact backtracker on the complete local incidence system: the full core is
infeasible, while each of its 26 one-row deletions is feasible, with an
explicit selected-edge witness.  Hence this literal core is subset-minimal.

## 3. Relation to the independent two-bank theorem

`MATH_THEOREM_K17_GK_DIRECT_BANK_TETRAHEDRAL_PALETTE_CORE_20260731.md`
proves a stronger presentation directly in the enlarged q9-filter-free
catalogue, for both explicit direct banks.  Its `7abc` core begins at
`0x6903`, whereas this independently extracted core begins at `0x7403`.
They are different tetrahedral copies and are consistent.

The normalized `8afb` control also returns the same `0x7403` 26-row core in
the old conditioned catalogue.  Independently, the two-bank theorem supplies
a q9-filter-free `8afb` core beginning at `0x7803`.  Thus the `8afb` result is
not inferred from the `7abc` solver run.

## 4. Joint-direct gate remains open

These certificates fix all 572 direct ears.  They prove that either explicit
bank cannot be completed inside the no-further-BB residual architecture.
They do not forbid rechoosing the direct bank jointly with the residual
edges.

An independent implementation of the joint supported catalogue exactly
matches the authoritative implementation on all 458,934 ordered edge
records:

```text
BB 20,655; BU 147,102; UU 291,177;
packed edge-list SHA-256 fdd8ea365b967f0ee855daf41dea19d853efcf622ce534516338adb2e3cb9bce.
```

The first full joint solve aborted with `std::bad_alloc` under its address
cap after 3m41s (maximum RSS about 12.0 GiB).  Its verdict is **UNKNOWN**.
No joint-direct, unrestricted `s=1`, or K17 no-go follows.

The independent joint catalogue/model audit is frozen as

```text
scratch/h2_k17_s1_joint_raw_edge_master_20260731.py
  SHA-256 f822a7384d2d5a42eca05473eb38c75248d4a42358ff149523a5f7ccbad3e776
scratch/h2_k17_s1_joint_raw_edge_master_20260731.audit.json
  SHA-256 62a7589e2285614193b5ba80235ea3ced0b725c667458bbbffe91b1c76fbecbe
  canonical payload ff61b68e2918fb384fae50aeb826c1b4857e5ce7a3ae87490033721e64850123
```

## 5. Frozen artifacts

CP-SAT row-core extraction:

```text
scratch/h2_extract_k17_s1_stageb_literal_core_20260731.py
  SHA-256 3be5d19a708afd4371f652a4d60c4892925a81c35771b10031e08e4f24cf0aca
scratch/h2_k17_s1_stageb_7abc_literal_core_20260731.json
  SHA-256 0302e98f71a48dba0d2dc7c56688e6471df55a76f781f12dede553a205cdf102
  canonical payload ee6774500c79d41203dc4830e00fd0d89501805e5a65c98a526db7f17425fc9e
scratch/h2_k17_s1_stageb_7abc_literal_core_20260731.stdout
  SHA-256 8372a9d3d72150add26fe61e88e7bb3b894719601eb8ace9c01ebc571ccbeb84
```

The one-worker run used CP-SAT 9.15.6755, took 13.1 seconds, and returned
`INFEASIBLE` with 566 conflicts and 972,377 branches.  The full presolve and
search log is retained in the stdout artifact; this is not a DRAT/LRAT proof.

Dependency-free reconstruction and solver-free proof:

```text
scratch/audit_h2_k17_s1_stageb_7abc_literal_core_20260731.py
  SHA-256 a9a8fec573c9ef9a1b015a8979586f8131f90262af021d37758c2230b7aa4f74
scratch/h2_k17_s1_stageb_7abc_literal_core_20260731.audit.json
  SHA-256 64c879275f35e05ad319fc7eb02e4101638beab203f0f510318c5505f30a8af8
  canonical payload e48e4079afd3c53290fd6d666d6a6c6ea68d1fb0a9e1eab889883595dbf6bc8e
```

The reconstructed old catalogue has 413,268 edges and packed SHA
`644734132a0dfff929010b87b4328958e79ade80163ad706f7f008daf71d1ccf`.
With the fixed boundary-q9 filter disabled it has 423,122 edges and packed
SHA `fe8caf95c83cbe9f16e21db0b5c5cf567c751b1afe04b29991f9fd682e8746c5`.

Normalized `8afb` control:

```text
scratch/h2_k17_s1_stageb_8afb_normalized_direct_20260731.tsv
  SHA-256 fb9b119f8f51c38aa7e4c0f41ac9d461a22600f2099efff7d89b7c7d261f77ed
scratch/h2_k17_s1_stageb_8afb_literal_core_20260731.json
  SHA-256 6c3d876e4201f34e876578cd10928b66e6dab1aca5f208e013ed8a6545c77ea8
  canonical payload f19d056f82162006392d17a40dcef9e89d8a2874927b13ae6721bd6ec93c7b62
```

The authoritative q9-filter-free two-bank audit independently reruns with
canonical payload
`53354643fdba00d531468b6811affd2346e338d0296aaeb105d053801ceccc7c`.

## 6. Scope exclusions

Nothing here constructs or excludes the joint direct bank, a physical ear
factor, a connected tail, a prefix, higher-shadow coverage, residence, the
compiler, or a K17 word.  In particular, this note is not a global K17
lower bound and not an unrestricted adjacent-cut no-go.
