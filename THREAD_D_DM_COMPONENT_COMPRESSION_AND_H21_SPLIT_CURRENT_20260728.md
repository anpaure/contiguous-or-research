# DM-component compression and the recursive split-current theorem

Date: 2026-07-28

Status: exact rank-neutral compression and packet-shave theorems, exact
H22-to-H21 and H21-to-H20 compression/split instances, an exact abstract H20
two-shave commuting square, and an exact H20-to-H19 fusion/remote-current
profile route. Compression ranking is predictive but is not by itself a
splitter-existence theorem. Heavy catalogue search remains restricted to H100.

## 0. Exact conclusion

The authoritative route is

```text
H22/z6
  -- FF(1320,5339,6194) --> H22/z6 portal
  -- FR(778,2292,6368) --> H21/z6.
```

The first braid replaces one gap-one DM circuit

```text
root 449: 160 targets / 159 cells
```

by another gap-one circuit

```text
root 458: 24 targets / 23 cells.
```

Every other DM component is unchanged. Thus the canonical shore changes

```text
1006/984  ->  870/848
```

while its gap and the global matching rank remain `22` and `16361`. The
second braid removes the whole `24/23` circuit, leaving

```text
846/825, 21 components, matching rank 16362.
```

This is a **rank-neutral circuit compression followed by a unit circuit
split**. After exact full-profile cancellation, the contracted boundary
ranks are

```text
neutral compressor: 24 -> 24,
unit splitter:       17 -> 18.
```

The word “compression” has a precise scope. It reduces the number of local
targets and cells which the later splitter must control by `136`; it does
not create extra Hall slack. The portal still has deficiency `22`, and a
unit split still has to preserve every global cut down to deficiency `21`.

## 1. Transversal-matroid language

For a target-to-cell bipartite graph `G`, let `M(G)` be the transversal
matroid on the target set. Its rank on `X` is the maximum number of targets
of `X` matchable to distinct cells.

Cell occurrences, rather than distinct target profiles, carry capacity. If
`K` is a multiset of common cell columns and `B` is a collar bank, define the
augmentation capacity

```text
chi_K(B) = nu(K union B) - nu(K).
```

Here equal profiles at different physical cells remain distinct copies.

### Proposition 1.1 (common-core rank-neutral exchange)

Let two materialized endpoints be

```text
G- = K union B-,       G+ = K union B+,
```

after exact cancellation of common full-profile cell occurrences. If

```text
chi_K(B-) = chi_K(B+) = beta,
```

then `nu(G-)=nu(G+)`; the collar replacement is rank-neutral.

Moreover, form the tagged ambient graph

```text
G* = K union (tagged B-) union (tagged B+),
```

so alternative endpoint occurrences remain distinct. Choose any target basis
`I` matchable in `K`. Matroid basis
extension gives maximum target bases

```text
I union X- in M(G-),       I union X+ in M(G+),
```

with `|X-|=|X+|=beta`. In the transversal matroid `M(G*)`, contract `I` and
truncate to rank `beta`. The two extension sets are bases of this
truncation and hence are connected by ordinary one-for-one matroid basis
exchanges.

#### Proof

The rank identity is the definition of `chi`. The common target basis `I` is
independent in both endpoint matroids, so the basis-extension axiom extends
it to maximum bases of the displayed sizes. After contraction and
truncation, both extension sets are bases of one matroid; basis-exchange
connectivity applies. □

The proposition does not assert that a physical braid decomposes into those
abstract one-target exchanges. It says exactly that its before/after matching
bases differ by a rank-neutral basis replacement once the common core is
contracted.

## 2. Circuit-compression theorem

### Definition 2.1

A neutral transition is a DM-component compression `C- -> C+` relative to a
common residual shore `Z` if:

1. the old canonical shore components are `Z` together with `C-`;
2. the new canonical shore components are the same `Z` together with `C+`;
3. `C-` and `C+` are transversal-matroid circuits, with sizes `s` and `t`;
4. their component cell sets have sizes `s-1` and `t-1`; and
5. the common-core augmentation capacities before and after are equal.

It is a strict compression when `t<s`.

### Theorem 2.2 (nullity-preserving compression)

Under Definition 2.1, the global matching rank is unchanged, the canonical
DM deficiency is unchanged, and the two shore sizes both decrease by
`s-t`:

```text
left decrease  = s-t,
right decrease = (s-1)-(t-1) = s-t.
```

The transition is therefore a rank-neutral basis exchange in the sense of
Proposition 1.1 and a replacement of one unit of circuit nullity by one unit
of circuit nullity.

#### Proof

Condition 5 and Proposition 1.1 give equal global ranks. Each component is a
circuit, so each contributes exactly one to `|left|-|right|`. Replacing one
circuit by another preserves that contribution. Conditions 1 and 2 leave
all other contributions fixed, and the displayed size calculation is
immediate. □

### Exact H22 instance

The independent reconstruction gives:

```text
old component roots     = {449} union R,
portal component roots  = {458} union R,
final component roots   = R,
```

where

```text
R = {960,1103,1920,2420,2575,2676,4213,5801,7504,8217,
     8218,9524,13616,13620,17683,17738,18970,19568,21641,
     24610,29776}.
```

The old and portal special components are exactly `160/159` and `24/23`.
Their size difference is `136` on each shore. For the neutral transition,
the common-profile graph has rank `16337`, and both collar banks add `24`:

```text
16337 + 24 = 16361.
```

This proves rank neutrality independently of the DM count.

For completeness, a connected positive-DM component of gap one is a circuit,
not merely a set with one-unit deficiency. Choose a maximum matching exposing
one component target. Every other component target is reached by an
alternating path; flipping that path exposes the chosen target instead.
Hence deleting any one target leaves all component right cells matchable,
while the full component has one more target than cells. This proves the
single-deletion circuit criterion used above.

## 2.1 Rooted native-basis duplicate lemma

Call a gap-one circuit `C={rho} union X` a rooted native-basis circuit if it
has distinct cells

```text
D = {d_x : x in X}
```

such that `x-d_x` is an edge and the native trace of `d_x` is `x`. This atlas
matches every target except the root.

### Lemma 2.3 (duplicate-child saturation)

Suppose an endpoint retains the native atlas and contains a second cell
`d'_u`, distinct from `d_u`, for some child `u in X`, with both

```text
rho-d'_u and u-d'_u
```

legal. A sufficient strong form is that `d'_u` duplicates the full target
profile of `d_u` and that this profile contains `rho,u`. Then the circuit is
saturated:

```text
rho -> d'_u,
u   -> d_u,
x   -> d_x for every other x in X.
```

Consequently its restricted matching rank rises from `|C|-1` to `|C|`.

#### Proof

The displayed cells are distinct and the displayed incidences are legal, so
they form a matching saturating `C`. No matching can exceed `|C|`. □

If the root edge is a nonnative physical pin, the matching lemma must be
conjoined with the literal conditions: the cell mandatory mask lies inside
`rho`, every controller letter on its interval meets `rho`, and pinning those
letters to `rho` has union exactly `rho`.

### Exact root-458 pivot

The portal circuit has 24 targets and a 23-cell native atlas. Child `462` has
one depth-one occurrence with full profile

```text
Gamma_462 = {448,450,452,454,456,458,460,462}.
```

The endpoint has two distinct occurrences of exactly this profile:

```text
cell 7216: start 778,  letters (398,206),
cell 8268: start 1830, letters (206,398).
```

Both have native trace `462`, mandatory mask `448`, and are incident with
root `458`. Pinning cell `7216` to `458` gives interval letters `(394,202)`
with union `458`; cell `8268` remains the native child occurrence.

The component-restricted profile ledger is particularly small:

```text
common occurrences: 22,
portal-only:          {462,16846},
endpoint-only:        {458,462}, {16842,16846}.
```

The 22 common occurrences have restricted rank 22. The portal-only column
adds one extension, giving local rank 23. The two endpoint-only columns add
two independent extensions, giving local rank 24. Thus the same unit appears
at three contraction levels:

```text
whole rooted circuit:       23 -> 24,
component boundary quotient: 1 -> 2,
global boundary quotient:    17 -> 18.
```

The global `17->18` statement must not be confused with the component's raw
rank. It is the common-core quotient image of the same duplicate-child pivot.

## 2.2 Pre-DM compression/split score

A search need not recompute the full alternating DM decomposition for every
candidate. Fix the current matching and cell-profile multiset. For a proposed
router and a proposed local root set, compute the following score vector.

```text
R0 = 1[chi_K(B_router)=chi_K(B_old)]                 (rank-neutral router)
R1 = 1[the proposed C is a closed gap-one circuit]   (local circuit test)
R2 = |C_old|-|C|                                     (compression amount)
D  = 1[a root-compatible child profile is duplicated]
L  = nu(new restricted C graph)-(|C|-1)              (local split gain)
G  = chi_K'(B_split)-chi_K'(B_portal)                (global boundary gain)
E  = nu(forced complement)-(n+1-|C|)                 (exterior margin).
```

Use the lexicographic score

```text
(R0,R1,R2,D,L,G,E),
```

with hard rejection unless `R0=R1=D=L=G=1` and `E>=0`. Among feasible
routers, larger `R2` means a smaller physical component for the splitter.

Every entry is computable before full DM:

* `R0` and `G` use common-profile augmentation ranks;
* `R1` uses only `G[C,N(C)]`: check `|N(C)|=|C|-1`, rank `|C|-1`, and rank
  `|C|-1` after each single target deletion;
* `D` is an occurrence-multiplicity/profile-containment check;
* `L` is one small matching on the proposed component; and
* `E` is one ordinary matching or min-cut after deleting the forced targets
  and cells, with no DM decomposition.

The cheap duplicate indicator `D` is only a heuristic until `L` is checked:
an extra occurrence can collide with another atlas obligation. Likewise,
local gain `L=1` is not global gain; `E>=0` is the exact exterior test.

For the audited route the score is

```text
(1,1,136,1,1,1,0).
```

The zero exterior margin means the splitter is exactly tight, not that the
exterior check is dispensable.

## 3. Exact subsequent unit-split theorem

Let a portal graph `Gp` have `N` targets, rank `n=N-h`, and a gap-one DM
circuit `C` of size `t` with an atlas `D` of `t-1` distinct cells. Assume the
atlas matches `t-1` targets of `C`, and assume a portal maximum matching uses
this internal atlas matching and an exterior matching. (This is the standard
DM-component decomposition and is audited in the present application.) Let
a materialized endpoint `G1` contain
a prescribed physical matching

```text
Q = {x-c_x : x in C}
```

of `t` distinct cells saturating the whole circuit. Reserve every target in
`C` and every cell in `Q`, and put

```text
Hp = Gp minus C minus D,
H1 = G1 minus C minus cells(Q).
```

### Theorem 3.1 (split after compression)

The portal exterior has exact rank

```text
nu(Hp) = n + 1 - t.
```

The endpoint has a matching of size at least `n+1` containing every forced
edge in `Q` if and only if

```text
nu(H1) >= n + 1 - t.
```

Equivalently, for every `S subset L minus C`,

```text
|N_H1(S)| >= |S| - (h-1).
```

#### Proof

A portal maximum matching may use the `t-1` component atlas cells and an
exterior matching of size `n+1-t`, giving the lower bound for `Hp`. A larger
exterior matching, combined with the atlas matching, would exceed portal
rank `n`, proving equality. In the endpoint, deleting the `t` forced edges
from any matching containing `Q` leaves a matching in `H1`, and conversely.
Thus the constrained endpoint rank is `t+nu(H1)`. The Hall form follows from
the bipartite deficiency formula. □

The allowed residual deficiency is `h-1`, independent of the compressed
circuit size `t`. Compression lowers physical arity; it does not relax the
global cut threshold.

## 4. Collar-current criteria

For `S subset L minus C`, define portal exterior cut slack and split current

```text
eta_p(S) = |(L minus C) minus S| + |N_Hp(S)| - (n+1-t),
j(S)     = |N_H1(S)| - |N_Hp(S)|.
```

Every `eta_p(S)` is nonnegative. Theorem 3.1 is exactly the following
necessary-and-sufficient current condition:

```text
eta_p(S) + j(S) >= 0       for every S subset L minus C.
```

Thus:

* a portal-tight exterior cut may lose no net occurrence capacity;
* a cut of slack `a` may lose at most `a`; and
* one ordinary residual min-cut separates all current rows.

After full-profile occurrence cancellation into old and new collar banks,

```text
j(S) = sum_(c in B+) 1[Gamma+(c) meets S]
     - sum_(c in B-) 1[Gamma-(c) meets S].
```

Each physical cell contributes one, regardless of the number of its arcs
into `S`. The forced cells are absent from `B+`, because their capacity is
already consumed by `Q`.

### Two-stage router/splitter ledger

The compression current and splitter current can also be kept separate. For
the pre-router graph `G-`, define

```text
sigma_-(S) = h - (|S|-|N_G-(S)|),
j_R(S)     = |N_Hp(S)|-|N_G-(S)|,
j_S(S)     = |N_H1(S)|-|N_Hp(S)|.
```

Then the complete compression-plus-split condition is exactly

```text
sigma_-(S)+j_R(S)+j_S(S) >= 1
for every S subset L minus C.
```

The currents telescope to the final forced complement. Plain global rank
neutrality of the router does not imply `j_R(S)=0`, or even nonnegative
`j_R(S)`, on each shore. What makes a compressed portal split-ready is the
stronger fact that its component deletion has the exact exterior rank in
Theorem 3.1; the splitter must then respect that portal's slack function.

### Three useful sufficient certificates

Any one of the following, together with a legal physical saturation `Q`, is
sufficient for the unit split.

1. **Fixed exterior basis.** A portal exterior matching of size `n+1-t`
   survives edge-for-edge and avoids every forced cell.
2. **Profile-dominating bank injection.** After cancellation, there is an
   injection from every lost old exterior cell occurrence `c` to a distinct
   new unreserved occurrence `phi(c)` such that
   `Gamma-(c) subset Gamma+(phi(c))` on `L minus C`. Then `j(S)>=0` for every
   `S`.
3. **Contracted boundary capacity.** If `K` is the common residual
   full-profile graph and `Bp,B1` are the residual banks, verify

   ```text
   chi_K(B1) >= chi_K(Bp).
   ```

   This is precisely `nu(H1)>=nu(Hp)` and is often much smaller than the
   full graph.

The second condition is sufficient, not necessary. The exact condition is
the slack-plus-current inequality; negative current is allowed on cuts with
enough portal slack.

## 5. The audited splitter

For the portal-to-H21 braid, exact full-profile cancellation gives common
rank `16344` and contracted boundary capacities

```text
17 -> 18.
```

Therefore

```text
16344+17 = 16361,
16344+18 = 16362.
```

The whole `24/23` root-458 circuit disappears from the positive DM shore,
and the other 21 components remain. The boundary calculation by itself is an
**unconstrained** rank certificate; it would not prove that a prescribed
physical root assignment is compatible with the exterior.

That stronger forced certificate is also exact here. Let `Q` be the 23
native atlas edges together with `458-7216`, using cell `8268` for native
child `462`. Then

```text
local rank:              23 -> 24,
|Q|:                     24,
rank(final minus C minus cells(Q)): 16338,
24 + 16338:              16362.
```

The forced complement has `16359` targets and deficiency `21`, so the split
is globally compatible and tight. This is stronger than merely checking
that the root acquired an incident cell.

The physical audit also keeps the exact scope visible. All three carriers
are Johnson paths, depth-three resident, and complete on every upper layer.
The lower-hole vectors are

```text
(4,18,6,1,0,0,0) -> (4,18,8,1,0,0,0) -> (4,18,9,1,0,0,0).
```

Thus the rank improvement is not a claim that the raw middle chronology
preserves every lower shadow. The common physical compiler/owner ledger
remains part of any coefficient-one conclusion.

The final carrier is
`scratch/k15_segment_braid_hall21_zero6.json`, SHA-256
`8a294110b530ba016b790f08f59c9d5bca3471af732867e27b0cb4a0b628b447`.
The primary route audit is
`scratch/audit_k15_segment_braid_hall22_to21.json`, SHA-256
`cc862804ea8910371283e8fdb42c1ac94ce9ed1cb5e0d3b5cdd94e8d74211e5c`.
The independent audit is
`scratch/audit_k15_h21_zero6_independent.py`, with output
`scratch/audit_k15_h21_zero6_independent.json`.
The focused local certificate, which emits no carrier and performs no
search, is `scratch/audit_threadD_root458_duplicate_child.py`, with output
`scratch/threadD_root458_duplicate_child_audit.json`.

## 6. H21 state and the next split

The H21 canonical DM shore is `846/825` and consists of exactly 21 gap-one
circuits. Its size census is

```text
169/168 x1, 161/160 x3, 160/159 x1,
5/4 x2, 3/2 x2, 2/1 x6, 1/0 x6.
```

All 825 right cells have distinct native traces, and those traces are exactly
the 846 active targets minus the 21 component roots. One maximal controller
realizes all 825 pins simultaneously.

For any H21 component `C` of size `s`, deleting `C` and its `s-1` atlas cells
leaves exact exterior rank

```text
16363-s
```

and residual deficiency `20`. A candidate H20 splitter with a physical
saturation of `C` must therefore satisfy

```text
nu(forced complement) >= 16363-s,
```

or equivalently

```text
|N(S)| >= |S|-20       for every residual target set S.
```

The six smallest nonloop candidates are the `2/1` circuits

```text
2420 -> 2932    retained cell 18663
2575 -> 2607    retained cell 16684
2676 -> 10868   retained cell 15770
9524 -> 9588    retained cell 15772
17683 -> 21779  retained cell 15761
19568 -> 27760  retained cell 16699.
```

For each, the clean graded primitive is a new depth-one native root cell plus
the retained depth-two native child cell. The `2575/2607` instance now uses
cell `16684`, start `3809`, not the historical H22 cell `17342`. Deleting its
two targets and retained cell leaves exact exterior rank `16361` and the
canonical tight shore `844/824`. A successful endpoint must reserve the new
and retained cells and keep residual rank at least `16361`.

There are also four rank-six loops, for which a depth-one native creator is
the local primitive, and two rank-seven loops, for which it is a depth-two
native creator. The five rank-four nonloops require a nonnative pin or a more
elaborate graded lift; they are not covered by the native-root shortcut.

## 7. Second prospective validation: H21 to H20

The compression ranking succeeded a second time on the frozen H21 state:

```text
H21/z6, DM 846/825
  -- RF(1510,5017,6136) --> H21/z6 portal, DM 702/681
  -- RF(885,1393,3668)  --> H20/z6, DM 677/657.
```

The first arrow leaves 20 DM components unchanged and replaces only

```text
root 1920: 169/168  -->  root 1801: 25/24.
```

Both are circuits of nullity one, so the shore shrinks by `144` on each side
while the deficiency and matching rank remain `21` and `16362`. The second
arrow removes the whole `25/24` component; the other 20 components are
unchanged, and the matching rank rises to `16363`.

The exact common-profile contractions are:

| arrow | common occurrences | common rank | old boundary | new boundary | total rank |
|---|---:|---:|---:|---:|---:|
| H21 to compressed H21 | 19,282 | 16,338 | 24 | 24 | 16,362 to 16,362 |
| compressed H21 to H20 | 19,279 | 16,345 | 17 | 18 | 16,362 to 16,363 |

Thus the requested contracted common-profile ranks are exactly

```text
neutral router: K-rank 16338, quotient 24 -> 24;
unit splitter:  K-rank 16345, quotient 17 -> 18.
```

The local splitter repeats the rooted duplicate-child mechanism. On the
root-1801 circuit, restricted profile cancellation gives

```text
common occurrences: 23,
lost:   {1801,1803,1833,1835},
gained: {1801,1833}, {1803,1835}.
```

Native trace `1833` is duplicated at cells `9334` and `9599`. Hence the local
component rank rises `24->25`, while the global boundary quotient rises
`17->18`. A forced 25-cell saturation leaves complement rank `16338`, so

```text
25 + 16338 = 16363
```

with zero exterior margin. This is again an exact global lift, not merely a
local component improvement.

The final carrier is
`scratch/k15_segment_braid_hall20_zero6.json`, SHA-256
`9dd192d50e2e94dccb109fdc649fa5e13d2e4f17bac687d30547bd1bb6ddfcf1`.
The primary contraction audit is
`scratch/audit_k15_h21_h20_compression_descent.json`; the rooted-circuit
audit is `scratch/audit_k15_h21_h20_compression_theorem.py`, with certificate
`scratch/audit_k15_h21_h20_compression_theorem.json`.

## 8. Why the compression ranking is predictive

### Theorem 8.1 (single-circuit arity dominance)

Fix a neutral-candidate family with deficiency `h`. Suppose every candidate
has the same residual DM component multiset `Z` and differs only by replacing
one old circuit of size `s` by a circuit of size `t`. Then

```text
DM_left(t)  = |Z_left|  + t,
DM_right(t) = |Z_right| + t-1.
```

Consequently, among this family, minimizing either DM shore size is exactly
minimizing the arity `t` of the component which a subsequent splitter must
saturate. The compression amount is exactly `s-t` on both shores.

#### Proof

Every gap-one circuit of size `t` has `t-1` component cells. The common
residual components contribute fixed terms, giving the two identities. A
rooted native-basis saturation has one obligation for every target of the
new circuit, so its forced local matching has size `t`. □

This explains the useful part of the ranking without probability. In both
audited descents:

1. the neutral candidate preserved all other components;
2. the replacement remained a rooted native-basis circuit of nullity one;
3. the smaller circuit reduced the later forced bundle; and
4. a bounded collar refined one old four-target column into two two-target
   columns, duplicating one root-compatible child.

The same quantities can be scored before recomputing full DM, provided a
local audit certifies that the exterior components are unchanged. If the
current total left mass is `S`, its square mass is `Phi`, its focal circuit
has size `s`, and the proposed rooted circuit has size `t`, set

```text
predicted_DM_left = S-s+t,
predicted_square_mass = Phi-s^2+t^2,
predicted_largest = max(largest exterior component,t).
```

These are identities under the fixed-exterior hypothesis, not statistical
estimates. For the H21 router they give

```text
846-169+25 = 702,
132022-169^2+25^2 = 104086,
predicted largest component = 161.
```

A proof-safe prospective router score is therefore

```text
(rank-neutral, closed-circuit, rooted-native-basis,
 compression s-t, -predicted_DM_left,
 -predicted_largest, -predicted_square_mass).
```

After a splitter is proposed, append the exact acceptance coordinates

```text
(duplicate-child, local gain, boundary gain, forced-exterior margin).
```

For the new descent the audited core tuple is

```text
(1,1,1,144,1,1,1,0).
```

The last zero says the prescribed saturation is globally tight. Strictly,
raw `DM_left=702` is post-DM data; only the locally predicted value above is
a pre-DM score.

The quotient motif is literally stable across the two descents:

| descent | neutral common rank | neutral quotient | split common rank | split quotient |
|---|---:|---:|---:|---:|
| H22 to H21 | 16,337 | 24 to 24 | 16,344 | 17 to 18 |
| H21 to H20 | 16,338 | 24 to 24 | 16,345 | 17 to 18 |

The previously gained global unit moves into the common core; the local
router/splitter quotient is unchanged. That exact recurrence is the strongest
retrospective validation of the score.

There is also prospective separation in the frozen H21 census. Among the
687 nonidentity neutral descriptions, the `702/681` portal is the unique
minimum in left-shore mass; the next two left-shore masses are `814`, while
the median is `846`. Exact second-neighbourhood scans of the five best
compression-ranked portals found an H20 successor only from this minimum.
Those exhaustiveness statements belong to the companion census/search audit;
the lightweight checker attached to this note independently verifies the
winning chain and its ranks, but does not re-enumerate the 687 candidates.

### What remains heuristic

The census ranking key first fixes Hall deficiency and zero count, then
minimizes

```text
DM_left, largest component, sum(component_size squared),
```

with component-count and small-component tie-breakers. Only the `DM_left`
coordinate has the exact arity interpretation in Theorem 8.1 when the other
components are fixed. The largest-component and square-mass terms are
concentration heuristics.

Compression alone does not imply:

* that a root-compatible child profile can be duplicated;
* that the duplicated occurrence is physically pinnable;
* that the local restricted rank rises by one; or
* that the forced exterior min-cut survives.

It can also produce a false positive by merging components into higher
nullity, by creating a compact circuit with no legal root socket, or by
giving an unconstrained rank gain whose prescribed physical saturation has
negative exterior margin. Conversely, literal child duplication is only a
sufficient pattern: a longer alternating augmentation could split a circuit
without it.

Therefore the proof-safe candidate pipeline remains

```text
neutral common-core rank equality
 -> closed gap-one rooted native-basis circuit
 -> maximal compression ranking
 -> duplicate-child/local-rank test
 -> global boundary-rank test
 -> forced-complement min-cut/common-word audit.
```

The first three stages explain why the ranking points toward a small service
problem. The last three are indispensable acceptance tests. Two consecutive
successes validate the mechanism, but do not give a distribution-free theorem
that the top-ranked compression always has a splitter.

## 9. Iterated same-root packet shaves

The H20 neutral census introduces a different compression regime. The root
and the unit nullity of one DM component remain fixed; only an internal packet
is replaced.

### Theorem 9.1 (quotient packet shave)

Let `C-` and `C+` be old and new positive-DM components with the same root.
Suppose their common target set `P=C- intersect C+` is independent of rank
`p` in both component restrictions and admits the same rank-`p` occurrence
basis after restricting cell profiles to `P`. Write

```text
R- = C- minus P,       R+ = C+ minus P.
```

Assume

```text
|R-|=a,  r(C-)-p=a-1,
|R+|=b,  r(C+)-p=b-1.
```

Then contraction of `P` replaces a circuit `a/(a-1)` by a circuit
`b/(b-1)`. In particular,

```text
|C-|-r(C-) = |C+|-r(C+) = 1,
```

and the component loses `a-b` targets and `a-b` units of matching rank.
If the exterior DM components are unchanged and the full common-profile
augmentation ranks agree, the global transition is rank-neutral and both DM
shores shrink by `a-b`.

#### Proof

Contraction gives

```text
r(C-/P)=r(C-)-r(P)=a-1,
r(C+/P)=r(C+)-r(P)=b-1.
```

Thus both quotient packets have nullity one. Restoring the same independent
connector `P` preserves that nullity. Equality of the full common-profile
augmentation ranks proves global rank neutrality by Proposition 1.1. The
left shore changes by `a-b`; the component right shore changes by
`(a-1)-(b-1)=a-b`. All other components are fixed. □

### Corollary 9.2 (iterated shave ledger)

For a sequence of neutral packet shaves with component sizes

```text
s_0 > s_1 > ... > s_m,
delta_i = s_i-s_(i+1),
Delta = sum_i delta_i = s_0-s_m,
```

the focal nullity stays one, the global rank and deficiency stay fixed, and

```text
DM_left(m)  = DM_left(0)-Delta,
DM_right(m) = DM_right(0)-Delta.
```

If `Phi=sum_C |C|^2` is the left-component square-mass potential and no other
component changes, then

```text
Phi(m)-Phi(0) = s_m^2-s_0^2
              = -sum_i delta_i(s_i+s_(i+1)).
```

Let the full graph have `N` targets, rank `n=N-h`, and let the focal circuit
at step `i` have `s_i` targets and a fixed internal atlas of `s_i-1` cells.
Deleting that circuit and its atlas leaves exact residual rank

```text
nu(H_i)=n+1-s_i.
```

Therefore a shave transfers `delta_i` rank units from the focal component to
the residual graph while the residual deficiency remains exactly `h-1`:

```text
(s_i-1) -> (s_(i+1)-1)                 current -delta_i,
nu(H_i)  -> nu(H_(i+1))                current +delta_i.
```

This is a transfer ledger, not stored Hall gain. Regardless of how many
neutral shaves are composed, saturating the surviving circuit can create at
most its one surviving nullity unit.

For pairwise full-profile cancellations

```text
G_i=K_i union B_i-,       G_(i+1)=K_i union B_i+,
```

define the contracted rank current

```text
j_i = chi_(K_i)(B_i+) - chi_(K_i)(B_i-)
    = nu(G_(i+1))-nu(G_i).
```

Every neutral shave has `j_i=0`, and only these differences telescope:
the separate augmentation ranks cannot be added because `K_i` may change.

## 10. Exact H20 length-15 shaves

There are two tied frozen H20 shaves:

```text
c0161: FF(1784,1799,5170), root 960,
c0163: FF(1788,1803,3103), root 8217.
```

Each moves a half-open block of exactly 15 middle vertices and changes one
component

```text
161/160 -> 129/128,
```

with the other 19 components unchanged. The old and new target sets meet in
124 targets. Their restricted common occurrence bank has exactly 124 columns
and rank 124. After contracting it, the packet replacement is

```text
37/36 -> 5/4.
```

The removed packet has one rank-five base, all eight singleton extensions,
and all `binom(8,2)=28` pair extensions. Its rank histogram is `(1,8,28)` at
ranks `(5,6,7)`. The inserted branch has histogram `(1,1,3)`. Hence the exact
compression is

```text
37-5 = 36-4 = 32.
```

The global contracted ledger is identical for the two shaves:

| transition | common occurrences | common rank | old boundary | new boundary | current |
|---|---:|---:|---:|---:|---:|
| base to c0161 | 19,294 | 16,346 | 17 | 17 | 0 |
| base to c0163 | 19,294 | 16,346 | 17 | 17 | 0 |

Thus

```text
16346+17 = 16363
```

at both endpoints. A more refined restricted ledger shows how neutrality is
implemented:

| tested target shore | common rank | quotient before | quotient after | rank current |
|---|---:|---:|---:|---:|
| old 161-target shore | 158 | 2 | 3 | +1 |
| new 129-target shore | 127 | 2 | 1 | -1 |

The braid saturates the old circuit while creating the new smaller circuit;
the two local currents cancel globally. The canonical DM shore changes

```text
677/657 -> 645/625,
```

while matching rank `16363`, deficiency `20`, the six zero targets,
residence, and every lower/upper support set remain fixed. For H20 the whole
component residual-rank transfer is, correctly,

```text
16363+1-161 = 16203,
16363+1-129 = 16235.
```

No splitter is currently certified from either `129/128` endpoint. This is
not a no-go theorem.

## 11. The two-shave commuting square

### Theorem 11.1 (direct-sum commutation)

Let an occurrence-profile incidence vector split into an exterior block and
two disjoint transversal-matroid summands `A,B`. Suppose neutral replacements
have signed occurrence vectors `Delta_A,Delta_B`, with disjoint supports, and

```text
x_10=x_00+Delta_A >= 0,
x_01=x_00+Delta_B >= 0,
x_11=x_00+Delta_A+Delta_B >= 0.
```

Then the square commutes in the free abelian occurrence-profile category:

```text
x_00+x_11=x_10+x_01.
```

If each replacement preserves the rank and nullity of its summand, rank and
nullity are preserved at all four corners. Every additive component potential
has the sum of the two single-replacement changes. In particular, shave
amounts and DM left/right mass reductions add.

#### Proof

The vector identity is commutativity of addition. Disjoint support and
positivity ensure that every corner is an actual nonnegative occurrence
multiset. On a block-diagonal transversal direct sum, rank and nullity add;
replacing either block does not alter the contribution of the other.
Additivity of component potentials is immediate. □

For the two H20 profile deltas, all removed and added profile supports are
pairwise disjoint. The formal fourth corner is therefore an exact
occurrence-profile graph. Direct reconstruction gives

```text
base:              677/657,
either one shave:  645/625,
both shaves:       613/593.
```

The two compression potentials are exactly additive:

```text
DM mass:       -32-32 = -64 on each shore,
square mass:   -2(161^2-129^2) = -18560.
```

Its components contain `129/128` blocks at roots `960` and `8217`, the
unchanged `160/159` block at root `8218`, the unchanged `161/160` block at
root `24610`, and the 16 unchanged small components. Its matching rank is
`16363`, deficiency is `20`, and it has the same six zero targets.

Every adjacent edge of the abstract square has

```text
common occurrences 19294,
common rank        16346,
contracted rank    17 -> 17.
```

Across opposite corners, and for the grand intersection of all four states,
the exact values are

```text
common occurrences 19277,
common rank        16329,
contracted rank    34 at every corner.
```

This square has an important scope restriction. It is exact in the
occurrence-profile/transversal-matroid category. No literal fourth middle
chronology or common-controller word is presently frozen. The two original
length-15 source blocks overlap, and naively composing the indexed moves in
either order does not give a legal Johnson chronology. Thus `613/593` is not
yet a physical carrier theorem.

## 12. Multi-root fusion and remote split current

The actual H20-to-H19 profile route uses neither of the two shaves. It is

```text
H20 -- RF(180,2764,4210) --> neutral H20 router
    -- FR(123,722,4710)  --> H19.
```

### Theorem 12.1 (nullity-preserving component fusion)

Let two positive-DM components `A,B` be transversal circuits of nullities
`eta_A,eta_B`. Suppose a neutral transition replaces their direct sum by one
connected component `F` on the same target union, with

```text
r(F)=r(A)+r(B).
```

Then

```text
eta(F)=eta_A+eta_B.
```

The DM component count falls by one, but total DM deficiency and global rank
are unchanged. If a later transition acts on a third component `C` and leaves
`F` rank-neutral, its rank current is remote from the fusion and can be
certified on `C` alone, subject to the global common-core check.

#### Proof

The target ground sets of `A,B` are disjoint, so

```text
eta(F)=|A|+|B|-r(F)
      =(|A|-r(A))+(|B|-r(B)).
```

Connectivity changes the DM block partition, not this arithmetic. The last
statement follows by additivity on the unchanged restrictions; global
common-core contraction is still required because physical collar columns
need not be block diagonal. □

In the exact neutral H20 router,

```text
root 8217: 161/160,
root 8218: 160/159
```

fuse into

```text
root 8216: 321/319.
```

The target union is exact. The restricted union has 317 common occurrence
columns of rank 317 and contracted rank

```text
2 -> 2,
```

so its rank stays `319` and its nullity stays two. Globally the router has

```text
common occurrences 19298,
common rank        16354,
contracted rank    9 -> 9.
```

The splitter then leaves the fused `321/319` block and all other surviving
components unchanged, but discharges the remote root-`24610` circuit
`161/160`. On that target shore its exact restricted ledger is

```text
common occurrences 159,
common rank        159,
contracted rank    1 -> 2,
restricted rank    160 -> 161.
```

The fused root-`8216` shore remains `317+(2->2)=319`. At whole-graph scale,

```text
common occurrences 19277,
common rank        16343,
contracted rank    20 -> 21,
total rank          16363 -> 16364.
```

Consequently the entire `24610` component leaves the positive DM shore:

```text
677/657 -> 516/497,
20 -> 19 deficiency.
```

This is the precise remote-current mechanism: the neutral router changes the
component topology at roots `8217/8218`, but the subsequent Hall unit is
carried by root `24610`; the fused component contributes zero splitter
current. The literal middle paths are Johnson, depth-three resident, preserve
all lower/upper support counts, and retain the same six zero targets. This is
an exact compiler-profile/Hall route, not yet a universal common-owner word.

## 13. Current proof gate

The profile-level Hall frontier is now H19. Packet shaving, direct-sum fusion,
and remote splitting must be ranked separately:

```text
shave score:  quotient arity and additive compression potential,
fusion score: preserved total nullity plus new physical collar topology,
split score:  local positive current plus exact global/forced-complement cut.
```

Only a literal chronology/controller certificate can promote the abstract
two-shave `613/593` square. Any exhaustive continuation remains an H100 CPU
task; the local work recorded here is exact reconstruction and proof audit.

## 14. Verification artifacts

The lightweight proof checker is
`scratch/audit_k15_h20_packet_shave_commuting_square.py`; its frozen output is
`scratch/audit_k15_h20_packet_shave_commuting_square.json`. It verifies both
packet quotients, every contracted rank above, the abstract fourth profile
corner, the fusion component identities, and the remote root-`24610` current.

The frozen physical carriers are:

| state | SHA-256 |
|---|---|
| canonical H20 | `9dd192d50e2e94dccb109fdc649fa5e13d2e4f17bac687d30547bd1bb6ddfcf1` |
| c0161 shave | `fdb95c316a3604f23aba75d1360230330743e443306cea5313e866a721d87563` |
| c0163 shave | `88c49a713755ba42d3577e2c80ad1c487ff7a9dd0f2f52d25e5af8da02b415c8` |
| root-8216 neutral router | `eabc8c63d5c8ae1b63e95118be620cb2e94507dafb1d11a1b10a46de41dc2e51` |
| H19 endpoint | `86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b` |

The two shave files retain the remote wrapper label `parent: state.json`, but
their middle paths materialize exactly from the frozen canonical H20 path by
their declared moves. The abstract fourth corner deliberately has no carrier
file.
