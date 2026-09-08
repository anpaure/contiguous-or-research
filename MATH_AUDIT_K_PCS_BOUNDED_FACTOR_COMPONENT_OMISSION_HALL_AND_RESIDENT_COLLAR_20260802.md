# Independent audit of the `PCS` bounded-factor omission-Hall theorem

**Date:** 2026-08-02  
**Lane:** K, independent proof and finite-scope audit  
**Audited theorem:**
`MATH_THEOREM_K_PCS_BOUNDED_FACTOR_COMPONENT_OMISSION_HALL_AND_RESIDENT_COLLAR_20260802.md`  
**Audited theorem SHA-256:**
`08b0f4647bf06ca21cc7b0cffcabcf560f65a2c3f2d3b752bb84c81f6a9f82ca`  
**Verdict:** **PASS.**  One load-bearing universe ambiguity found during the
audit was corrected before this freeze: all omission complements and
deletions are in the rooted turn set `mathcal T(F)=M_1`, not in the full
`2W`-edge incidence factor.

No all-`m` bounded-factor existence, global residence, deeper-shadow,
compiler, source, or word conclusion is audited here.

## 1. Basic count and factor model

For `Omega=[2m-1]`,

\[
 W={2m-1\choose m-1}={2m-1\choose m},\qquad
 U={2m-1\choose m+1},
\]

and cancellation gives

\[
 W-U={1\over m+1}{2m\choose m}=\operatorname {Cat}_m=C.
\]

Suppressing the lower roots in a factor
`F=M_0 dotcup M_1` turns the successor phase
`mathcal T(F)=M_1` into a permutation digraph on the `W` rooted vertices.
Disjointness of `M_0,M_1` excludes loops.  A subset of this turn set is
therefore a forest exactly when it omits at least one turn from every
permutation cycle.  An upper-bijective forest has `U` turns and exactly
`W-U=C` directed-path components, isolated roots included.  The theorem's
distinction between the Catalan forest and its bounded-component ambient
factor is consequently exact and necessary.

The notation repair is essential.  If one took
`Z=E(F)-Q_0` in the full incidence graph, every predecessor edge in `M_0`
would be deleted, every factor component would be hit trivially, and the
task multiplicity counts would no longer describe `Z`.  The frozen theorem
now explicitly defines `mathcal T(F)=M_1` and uses

\[
                     Z=\mathcal T(F)-Q_0.             \tag{1.1}
\]

## 2. Proposition 1.1: the `6d<=m-2` protected start

The sharp pivot owner path has `3d` Johnson turns.  Its incidence lift is
the alternating path

\[
 V_0-I_0-V_1-I_1-\cdots-I_{3d-1}-V_{3d},
\]

so it has exactly `6d` incidence edges and maximum degree two.  Under

\[
                              6d\le m-2,
\]

the small protected-factor theorem applies verbatim and extends this path
to a spanning Middle Levels two-factor.  Alternating the completed factor
phases so the protected predecessor edges lie in `M_0` leaves the successor
edges in `M_1`; hence the phase-aligned pivot is retained.

Every internal pivot incidence vertex already has degree two, so completion
cannot change the internal collar.  The literal pivot calculation therefore
retains all nonclipped internal runs of length at least `d+1`.  The two
endpoint neighbours remain chosen by the completion, so accepted exterior
residence, upper coverage, and component count do not follow.  Proposition
1.1 has exactly this scope and is correct.

## 3. Exact component-omission Hall equivalence

Let `q` be the number of ineligible turns, and for each upper task `R` put

\[
 \lambda_R=|u^{-1}(R)|,\qquad b_R=\lambda_R-1.
\]

Full-shore coverage makes every `b_R` nonnegative, and counting eligible
turns gives

\[
                     \sum_R b_R=C-q.                  \tag{3.1}
\]

The protected closure `P_*` has eligible pairwise-distinct task labels.
Thus each `R` has at most one protected occurrence.  It consequently has
at least `b_R` deletable occurrences: exactly `b_R` if one occurrence is
protected, and `b_R+1` otherwise.

### Necessity

For an allowed upper-exact forest `Q_0`, let

\[
                         Z=\mathcal T(F)-Q_0.
\]

Then `Z` contains every ineligible turn and exactly `b_R` eligible turns of
task `R`.  Since `Q_0` is a subset of a disjoint directed cycle cover, it is
acyclic exactly when `Z` meets every factor cycle.  Components containing
an ineligible turn are already hit.  On each remaining component choose one
member of `Z`; its task is represented outside `P_*`, and task `R` is chosen
at most `b_R` times.  Capacitated Hall gives

\[
 |X|\le\sum_{R:N_R\cap X\ne\varnothing}b_R
                 \qquad(X\subseteq\mathcal K_0).      \tag{3.2}
\]

### Sufficiency

Conversely, replace task `R` by `b_R` capacity copies and use (3.2) to
assign one actual deletable occurrence to every component of
`mathcal K_0`.  Different components are disjoint, so the designated actual
turns are distinct.  Extend task by task to exactly `b_R` deletions; the
preceding protected-occurrence count proves that this is always possible
without deleting `P_*`.  Add all forced ineligible turns.  The resulting
`Z` has the exact task counts and meets every factor cycle.  Its complement
is the required upper-bijective forest.

This proves all three items of Theorem 3.1 equivalent.  The complement has
`U` turns on `W` roots, hence exactly `C` path components.  The one-cycle
corollary is also exact: either a forced ineligible turn already opens the
cycle, or `q=0` and (3.1) supplies at least one deletable repeat because
`C>=1`.

The `2^s-1` interface count for an ambient factor with at most `s`
components is valid because `|mathcal K_0|<=s`.  It is a bounded number of
cuts only when `s` is bounded; the theorem does not prove such an `s`.

## 4. Theorem 4.1: exact local-residence scope

Under hypotheses 1--5, Theorem 3.1 only **marks** the chosen turns inside
the already fixed physical factor `F`.  It does not reorder `F`.  Every
load-bearing turn of the accepted collar certificate lies in `P_*` and is
retained; every nonturn boundary occurrence is frozen separately.  Thus a
collar already accepted by its two exterior capped-run states remains
resident in the ambient factor.  This implication is sound.

It is local.  Internal pivot residence alone is not enough, and neither the
omission forest nor bounded factor components proves residence elsewhere.
The theorem also does not order the `C` Catalan components as a source or
preserve upper witnesses above immediate width.

The transparent-pull alternative is correct under its stated strong
predicate: the pull supports are pairwise incidence-disjoint, form a tree
on current factor components, preserve the complete eligible/ineligible
task vector, and avoid the full collar certificate.  Leaf processing then
merges to one task-equivalent factor cycle.  Corollary 3.2 applies.  Merely
having an unlabelled component pull graph would not suffice, and the theorem
does not claim otherwise.

## 5. Proposition 7.1: forward deficiency

On the explicitly stated **edge-separable port face**, the outgoing shore
has `C` vertices and the incoming shore has `C-1`, since `K_*^in` is
deleted.  With

\[
 \delta(G_\phi)=\max_X(|X|-|N(X)|),
\]

the bipartite deficiency theorem gives

\[
                         \nu(G_\phi)=C-\delta(G_\phi).
\]

A matching of size `C-b` gives component indegree and outdegree at most one.
All its connectors increase the injective potential, so it has no directed
cycle; under these degree bounds an undirected cycle would necessarily be a
directed one.  The result is exactly `b` paths, with no edge entering
`K_*`.  Conversely, a path cover with at most `b` paths supplies a matching
of size at least `C-b`.  Therefore Proposition 7.1 is exact.

The edge-separable qualification is load-bearing.  A global common-cap,
pin-address, or shared-witness predicate need not be the conjunction of
single-connector predicates.  Such a row is outside `G_phi` unless a
separate private/product-state theorem first proves factorization.  The
frozen theorem now makes this exclusion explicit.  Also, "beginning at
`K_*`" is a component-level statement; making the literal pivot the first
turn inside `K_*` is a separate protected-opening row.

## 6. Independent K17 residence-2018 calibration

The endpoint files were checked read-only on H100.  Their hashes are

```text
c8f961413aeea43cbad5036e801c08f854f84889eaef11c281aa83bea46c057d
  checkpoint_fullq1_escape_res2018/model
885f62c5b7689ada00970688a9771a5bcaa543657e3fae3d065aed3d1f41cb9d
  checkpoint_fullq1_escape_res2018/independent.audit.json
```

The independent JSON reports

```text
status                                      PASS_INDEPENDENT_K17_H1_Q1_ZERO_MODEL
guarded clauses                             16261
augmented components                        1
opened short histogram, orientation 0       (1277,741)
opened short histogram, orientation 1       (1276,742)
opened residence                             2018
opened upper holes ranks 10..17, both        (0,1518,278,4,0,0,0,0)
```

Together with the authenticated primary model, this verifies finite
compatibility of full opened `19,448/19,448` immediate-upper coverage, the
named boundary guards, augmented connectivity, and descent from residence
`5,588` to `2,018`.

The route to the last endpoint must be described with its exact
state-relative semantics.  After a connected q1-neutral `C6` bridge, the
ordered continuation is `C8` rows `2446,12688,2243`.  Rows `12688` and
`2243` are disconnected when applied singly to the **immediate post-bridge**
state, but the preceding quench rows change that state.  The independent
promoted-chain replay checks guards, both opened q1 frames, the protected
boundary, and connectivity after every prefix of the displayed order.
Thus the four-primitive packet is strict-prefix safe even though it is not
a root-disjoint commuting batch.  This is independently frozen in
`MATH_AUDIT_R2_K17_FULLQ1_BRIDGE_QUENCH2018_CALIBRATION_20260802.md`,
SHA-256
`7388396b35fd9b88b2fae4fc63b4753f48bbede94653e8a597fbb47f9e8f0596`.

This K17 object has the exceptional `h=1` lollipop degrees (`1` at `M`, `3`
at `D`) rather than two ordinary perfect-matching phases.  It is therefore
positive calibration only: it is not an instance of Theorem 3.1 or
`PBCOH_s`, does not certify the literal pivot collar, has positive residence,
and still misses ranks 11--13 as displayed above.

## 7. K17 three-level chainization integration

The theorem's new K17 static-lower paragraph is independently covered by
`MATH_AUDIT_K_K17_THREE_LEVEL_NORMAL_CHAINIZATION_20260802.md`, SHA-256
`bd42e50191df8353b19a51ed0a3de18ee573705ea7c975003eea208e9ffff47d`.
That audit verifies the compressed-level sizes `21777,19448,24310`, both
uniform containment couplings, the conditional three-level chain
distribution, LYM, Dilworth, and the lollipop perfect matching.  Therefore
the exact K17 `d=3` **static** named-lower allocation is closed.

It also independently parses the materialized payload on the
residence-2018 lollipop phase.  The replay verifies `24,310` owner rows,
all `65,535` lower targets exactly once, chain-length histogram
`(1748,3899,18663)`, every rank-eight root and rank-nine owner exactly once,
and membership of every assigned root--owner edge in the selected
`48,620`-incidence factor.  The payload and independent audit JSON SHAs are

```text
029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1
b9a50eb60bf338e7750404a77be85fcb9aba15ef8676e53dc3d9b0ae75567e1c
```

This proves coexistence of the static chain table with the selected K17
incidence phase, not serialization of that table.

The integration preserves the required scope: no selected chain is proved
to occur as a literal suffix history, and chronology/state balance,
residence, upper shadows, pivot addresses, and common-cap/compiler remain
open.  The K19 inequality `94183>92378` also confirms that this particular
three-level compression is not an all-dimensional recurrence.

### 7.1 Canonical hinge balance is genuinely impossible

The new downstream paragraph is supported independently by
`MATH_AUDIT_K_K17_HINGE_RECTANGLE_BALANCE_INDEPENDENT_20260802.md`,
SHA-256
`c9bc857fd81be1b168f0bcbb51b54822fb2bf08a6d8f916dda4df360e61dfb69`.
Its O3 H100 replay reconstructs the literal ordered states rather than
reusing the producer's packed-state or max-flow implementation.  It obtains
the same `734904` heads and `6223360` tails and exactly one compatibility.

The stronger proof is table-independent on the old hinge face.  Every head
has rank-eight union, every short-chain tail has rank-nine union, and every
K17 three-slot chain partition has at least `3698` short chains by the slot
deficit `7395`.  Thus no such old-hinge table balances.  On the frozen table
the sole edge is not a balanced trace: it joins distinct roles and lies on
no directed cycle.  The producer's old `PASS` status and
`maximum_balanced_roles=1` label are therefore reporting errors; the numeric
maximum matching one is still a valid full-balance obstruction.

The audit also checks two genuine enlargements.  Complete right-aligned
guard/filler unsaturation remains at matching one.  A slot-preserving split
of the last layer reaches projection matching `888`, but does not close the
same-role factorization correlation.  Finally, changing arbitrary menus on
only `q` frozen roles requires `q>=12155`; a bounded correction bank cannot
repair this table.  Hence the theorem correctly leaves chronology/state
balance open and identifies positive-density split--reinsertion as the next
state class rather than claiming that static chainization serializes.

## 8. Final proof-safe boundary

The theorem correctly reduces its factor-subset face to a strictly smaller
all-`m` target:

* build a phase-aligned full-shore factor containing the protected collar;
* make its component count bounded (or supply a collar-safe transparent
  pull tree);
* accept the two exterior collar-run states; and
* satisfy the exact omission inequalities (3.2).

The strongest unconditional row is only the `6d<=m-2` protected-factor
start.  No current argument proves the remaining upper-covering,
bounded-component, boundary-state, and omission-Hall rows simultaneously
for all sufficiently large `m`.
