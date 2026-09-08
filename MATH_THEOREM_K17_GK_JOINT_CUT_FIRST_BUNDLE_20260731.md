# Joint `k=17` GK cuts and distinct first bundles close at `c=312`

Date: 2026-07-31  
Status: **GO** for the exact joint cut/assignment/first-bundle gate.  The
remaining ear completion, prefix, and upper continuation are open.  No
length-24313 word is claimed.

## 1. Why the joint model is necessary

The lexicographically optimal exposure-only certificate uses 312
pairwise vertex-disjoint GK cuts and exposes all 380 non-all-unused hard
rank-six colours.  Freezing that assignment and only then choosing first
physical neighbours fails Hall: its partner graph has matching rank 368,
with a Dulmage--Mendelsohn shore `77>65`.

That failure is not intrinsic.  It is an artifact of optimizing cuts and
hard-colour assignments before physical partners.

## 2. Exact option catalogue

For a hard colour `D`, choose:

* an original internal rank-seven port `v` containing `D`;
* one incident GK edge `e` to cut, leaving the other old neighbour `n_v`;
* a genuinely unused rank-seven partner `w` containing `D`.

The first physical edge has colours

\[
 q_8=v\cup w,
 \qquad
 h_9=n_v\cup v\cup w.                         \tag{2.1}
\]

Only options with ranks eight and nine respectively are retained.  Palette
availability is charged dynamically to the same cut set:

* if `q_8` already belongs to an old GK edge, that edge must be cut;
* if `h_9` already belongs to an old GK turn, at least one of its two old
  incident edges must be cut.

The complete catalogue contains 13,332 options on 742 unused partners and
3,273 potentially relevant seed edges.

## 3. Joint integer model

Let `x_e` select a cut and `z_o` select an option.  The constraints are:

1. exactly one option for every one of the 380 hard colours;
2. at most one option at each exposed port;
3. at most one option for each unused partner;
4. at most one option for each `q_8` colour;
5. at most one option for each `h_9` colour;
6. selected cuts are pairwise vertex-disjoint;
7. selecting an option forces its exposure cut and every required dynamic
   palette-release cut.

The primary objective minimizes the number of cuts.  Subject to that
minimum, the secondary objective minimizes endpoint--internal cuts.

## 4. Exact result

CP-SAT proves

\[
 \boxed{c_{\min}=312}.
\]

Thus the partner, `q_8`, and `h_9` SDRs cost **no additional cuts** over the
exposure-only optimum.  Subject to `c=312`, the minimum one-sided count is
again 90.  The frozen certificate has

\[
 90\text{ endpoint--internal cuts},
 \qquad
 222\text{ internal--internal cuts}.               \tag{4.1}
\]

Its 380 selected first bundles have, simultaneously,

```text
380 distinct hard colours
380 distinct exposed ports
380 distinct genuinely unused rank-seven partners
380 distinct rank-eight edge colours
380 distinct rank-nine boundary-turn colours.
```

Every selected cut is an exposure cut; no extra palette-only cut is used.
The cut occupancy is `244` single-assignment plus `68` double-assignment
cuts.

This strictly repairs the fixed-certificate Hall obstruction: the cut set,
assignment, and first physical bundles must be chosen together.

## 5. Scalar ledger

The 90 one-sided and 222 two-sided cuts destroy

\[
 90+2(222)=534
\]

old turns and create 90 isolated endpoint components.  Consequently the
previous corrected scalar ledger remains valid:

\[
 (x_1,x_2,x_3,x_4)=(4336,905,252,42),               \tag{5.1}
\]

with 5,535 joins, 1,535 new vertices, 7,070 new edges, and

\[
 12605-90=12515
\]

new turns.  Hence

\[
 9840+7070=16910,
 \qquad
 4394+12515=16909.                                  \tag{5.2}

## 6. What remains

The theorem selects only the first physical bundle incident with each of
the 380 exposed hard-colour ports.  It does not yet:

* complete and order all 5,535 ears;
* realize the 294 all-unused hard colours and all repeated rank-six slots;
* connect the resulting component forest into the final tail path;
* solve the alternating prefix-block completion;
* cover ranks 10 through 17.

It nevertheless removes the first post-cut Hall obstruction at no scalar
cost and shows that the sequential failure `368/380` was not structural.

## 7. Frozen artifacts

* optimizer: `scratch/search_k17_gk_joint_cut_bundle_20260731.py`
* immutable certificate:
  `scratch/k17_gk_joint_cut_bundle_ad6fb0631c9c336f_20260731.json`
* dependency-free replay:
  `scratch/audit_k17_gk_joint_cut_bundle_20260731.py`
* replay payload: `scratch/k17_gk_joint_cut_bundle_20260731.audit.json`
* solver transcript: `scratch/k17_gk_joint_cut_bundle_search_20260731.log`

The immutable certificate SHA-256 is

```text
ad6fb0631c9c336f229846cdb2a78a8f1a8f3a6532968310b964f5f560c0e9e4
```

and the replay canonical payload hash is

```text
479cd69d9e6bcd173607656d2148c5d1963e2c815c01f21dd910cafb1ae58ab8
```
