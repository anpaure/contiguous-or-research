# Audit of the adjacent-cut port-Hamilton and buffered-packet theorems

Date: 2026-07-31  
Lane: AD independent arithmetic/topology and theorem-scope audit  
Verdict: **PASS after scope corrections** for the forced-direct certificate,
exact residual ledgers, contracted port-Hamilton equivalence in its decorated
subclass, guarded grouped-SDR reduction, and conditional buffered composition
theorem.  The fixed provider checkpoint is not completable without
reselection, and no `K17` word or unconditional all-`k` bound is certified.

## 1. Forced direct layer

The shift-one seed reconstructs as `3640` disjoint Johnson edges.  The
stored exceptional table contains `572` rows.  Direct replay verifies

```text
distinct lower/q8                    572/572
distinct old endpoints                  1144
distinct boundary h9                    1144
distinct seed components touched         1144.
```

Thus the direct edges form a matching on the contracted seed components,
not merely on physical owners.  They leave `3068` path components and
`6136` exposed old ports.  This establishes literal privacy of the direct
layer.  It is only local sharpness: the later unrestricted-tail audit proves
that each of the two displayed `572`-edge banks is raw full-factor UNSAT.
Other minimum banks, or solutions with more direct edges, are not excluded.

The adjacent-length equations independently give

\[
 x_4+x_5=3067,qquad3x_4+4x_5=9631,
\]

and hence `(x4,x5)=(2637,430)`.  This is the unique minimum-maximum-length
`4/5` schedule, not a WLOG reduction for arbitrary completions.

## 2. Provider/filler arithmetic

For `p` residual provider `BU` edges and internal wedge counts `A,B,C` of
types `PP,PF,FF`, replay of incidences gives

\[
\begin{aligned}
P_{UU}&=8164-p,&F_{BU}&=6134-p,&F_{UU}&=p-1600,\\
A+B+C&=9631,&2A+B&=16328-p,&B+2C&=2934+p.
\end{aligned}
\]

Thus `p=6697-A+C`.  Nonnegativity alone gives `1600<=p<=6134`, but exact
reconstruction of the supported provider catalogue gives row classes

```text
BU-only 1001, BU+UU 3523, UU-only 3640,
```

so physically `1600<=p<=4524` and `2173<=A-C<=5097`.  The formal unfiltered
face `p=6134` has binary-string range `1037<=C<=2482`, but does not occur in
the supported shift-one catalogue.

## 3. Capacity checkpoint and the missing graphic row

The residual-cap certificate selects all `8164` unique providers with
`BU/UU=3065/5099`, respects owner/q8 capacities, and has `4209` distinct
forced boundary turns including the direct layer.  Its exact local defects
are

```text
illegal saturated wedges                       17
central duplicate h9 units                   1503
central h9 values colliding with boundary      261
total central collision units                 1764.
```

The AD topology replay adds a missing diagnosis.  Base, direct and selected
provider edges form a maximum-degree-two graph with

\[
                    (|V|,|E|,c)=(15032,12376,2660),
\]

and four cyclic components.  All four cycles are saturated.  Repeat edges
cannot open them, so the fixed provider edge set is not extendable as-is.
The wedge, turn and cycle debts may be repaired by the same exchange; they
are not additive packet lower bounds.

For disjoint `3<->3` C6 toggles only, at most six turn occurrences change
per toggle.  Therefore the `1764` collision units force support at least
`ceil(1764/6)=294` in that restricted actuator language.  This does not
apply to longer/global reselection.

## 4. Contracted repeat theorem

If provider reselection produces a clean acyclic graph with the same vertex
and edge counts, it has `2656=15032-12376` path components.  Selecting
`1879` zero-degree unused owners creates `4535` contracted nodes.  The
`4534` repeat edges have exact deficit

\[
                  BU=3069,qquad UU=1465.
\]

After degree rows, only two ports remain.  Consequently graphic independence
is equivalent to connectedness and makes the expanded owner graph one path:

\[
                4534=(2656+1879)-1.
\]

This proves the relaxed port-Hamilton equivalence inside the fixed-`K`,
fresh-q8/injective-h9, deletion-coded repeat subclass and shows why fixed
`4/5` ear lengths are no longer necessary there.  It is not an iff for
arbitrary undecorated literal completions.

## 5. Deletion-label reduction

For a repeat edge with lower facet `C`, choose `g in C` and source `C-g`.
At an owner whose **distinct** incident facets are `v-x` and `v-y`, exact
source union is equivalent to the local inequalities stated in the theorem.
Equal incident facets give an immediate empty domain even when the two
Johnson edges and rank-nine unions are distinct.

Under the prescribed no-new-to-new diamond topology, the `1879` new centres
give `1879` two-edge groups and the remaining `776` repeats are singleton
groups.  Each centre has a raw `5*4=20` domain.  The two external core
endpoints then add unary guards, reducing the full pair list before bank
filtering to `12,13,16`, or `20`; a prescribed rank-five bank can reduce it
further.  Singleton lists have size at least four only after both endpoint
facet-distinctness checks and before prescribed-bank filtering.

The resulting **guarded** grouped SDR is a genuine hypergraph matching.  The demand
inequality `|N(X)|>=2|X_pair|+|X_single|` is necessary but not sufficient;
the two-family example

\[
 \{ab,cd\},\qquad\{ac,bd\}
\]

passes the union-size inequalities and has no disjoint choice.  This is an
abstract grouped-choice counterexample; no embedding into the restricted
Boolean-diamond lists is claimed.  A valid general absorber must act on
complete guarded group options or on alternating cycles of an
occurrence--target matching that has already filtered all unary guards and
bank membership.

## 6. Buffered composition audit

Pairwise geometric nonconflict is insufficient for global composition.  The
smallest independent failures are:

1. three distinct-port connectors `12,23,31`, every pair acyclic but all
   three cyclic;
2. three packets drawing distinct cells from `{a,b}`, every pair matchable
   but the triple Hall-deficient;
3. two disjoint letter edits changing the same crossing interval; and
4. state-dependent moves `e->f` and `f->g` with no common off-state.

The corrected theorem avoids these examples by fixing a topological
skeleton (or retaining path-degree/endpoint rows in addition to a triangular
rooted-basis order), assigning every affected occurrence to one full
simultaneously evaluated halo/interface, preallocating resource/loss tickets,
and carrying an integral local cap matching in each option.  The common-cap
matching is `M_0` restricted outside replaced target/cell domains, united
with the local matchings.  Under those conditions a full independent
transversal in the complete conflict graph really does compose.  Haxell then
applies at the exact threshold

\[
                         |L_i|\ge\max\{1,2\Delta\}.
\]

This selector condition is not yet proved for the Catalan packet lists.
For all-depth shadows a constant-width buffer is insufficient unless a
separate trace identity proves longer occurrences invariant.

## 7. Additive-constant scope

A bounded exceptional list is safe only with a literal neutral bypass that
preserves topology, charges every currently missing target to the current
terminal repair, and exports only auxiliary recurrence obligations to a
regenerated bounded sidecar.  Uniformly along one covered infinite odd
spine, literal pre-repair lengths `B(k)+c_o,B(k)+c_e` and terminal repair
complexities `r_o,r_e` give

\[
             \nu(k)\le B(k)+\max\{c_o+r_o,c_e+r_e\}.
\]

All constants must be absolute in `k`.  Terminal exceptions are paid once;
carried port/ticket state must regenerate.  Dimensions outside the covered
spine need separate certificates.  Merely asserting `O(1)` exceptional cap
or topology tasks does not imply the bound.

## 8. Scope boundary

Still unproved are:

* a clean acyclic `8164`-provider selection;
* the `4534`-edge q8/h9-fresh repeat factor;
* the grouped deletion-label SDR;
* higher upper shadows, residence, prefix/common-cap completion; and
* any `K17` word or uniform fully witnessed Haxell list bound.

## 9. Frozen replay and independent theorem audits

The final guarded-SDR theorem and buffered-composition theorem were each
adversarially re-audited after correction and returned `PASS` at

```text
MATH_THEOREM_AD_K17_BOOLEAN_DIAMOND_GUARDED_GROUPED_SDR_AND_ABSORBER_20260731.md
  9a892e994959dbbc3e98676b68d92cced5e2a8ae62af7cf9f7f81f5835623681
MATH_THEOREM_AD_BUFFERED_HEX_GLOBAL_COMPOSITION_HAXELL_AND_BOUNDED_SIDECAR_20260731.md
  964c12a99f437955510eff7e55a456985f9c45c4210b24cd5187208e13b55d77
```

The dependency-free local replays are

```text
scratch/audit_ad_k17_gk_shift1_forced_direct_residual_20260731.py
  dd0694a2ce60bd499441bbbef75be5e64bafa2e5bcf6f272f858b90778d1b26a
scratch/ad_k17_gk_shift1_forced_direct_residual_20260731.audit.json
  a5dea3e738a011aff3db1fd0dbf40ef2ffbb84f91559323e2b0349fa608f77c0
  payload 802d2da895c1821e5f875595a8665c409ad749bfe4ed61b0910738c9d6019e71
scratch/audit_ad_k17_gk_shift1_residual_cap_topology_20260731.py
  c750d371b91e577364013b8bc65029bbc0c1527b9316e32aec54071a880a1679
scratch/ad_k17_gk_shift1_residual_cap_topology_20260731.audit.json
  eea2d143f4b3c0fa9476ea7c125e3486a9046792587854a4b6079cd800a7a1a2
  payload 8837b6ca82a5910646b03c9f2c2c59f075b3ed7ae13e095cbecd6a3fa0a50b66
scratch/audit_ad_k17_boolean_diamond_guarded_sdr_20260731.py
  05194aa2661fbcaafcd446e9aa4bc570aa6292f069ee2e769279f873ad6c8b2f
scratch/ad_k17_boolean_diamond_guarded_sdr_20260731.audit.json
  d68308e4618f88aceed44cd17fb339a0f418793abe78931e9b26c76bcb97ffe4
  payload 28e02bb8a1ce7c3194f518044b453d473f81634416ea5c49c24e0f7837d46616
```
