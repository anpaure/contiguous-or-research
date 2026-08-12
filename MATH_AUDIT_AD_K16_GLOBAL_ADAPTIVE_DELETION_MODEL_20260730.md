# Exact K16 global adaptive-deletion model and novel-phase first branch

Date: 2026-07-30  
Lane: AD  
Status: **model and clause audit PASS; feasibility UNSOLVED/UNKNOWN at freeze**

## 1. Frozen inputs

The verified length-`12874` word is

```text
answers/k16_upper12874.word
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e.
```

The exact `191`-root deletion/provider census is

```text
scratch/k16_multiroot_deletion_portal_rank_20260730.tsv
SHA-256 fe51c4301cab3be93900a9f848082a8fd8a7336bf1d0f9016cb512df2f9a33d2.
```

The prioritized source is the length-`12873` novel H2 state

```text
scratch/k16_delete6440_novel_h2_20260730.word
SHA-256 a1c9ec8d4e2b22b2fa20af1d0c96a33591b273f730814e1011f7bcd159e928fe,
holes {10365,21613} = {0x287d,0x546d}.
```

Its exact topology audit selects the nonduplicate pool

```text
P = {2,3,4,528,5934,6438}.
```

Position `3` is the authenticated phase axis.  The eight values

```text
68,69,76,77,100,101,108,109
```

replace the parent hole `0x546d` by the child hole `0x766d`, while retaining
`0x287d`.  The active multiroot support `{0,3,5921,12872}` is not contained
in `P`, so this branch does not duplicate that fixed joint4 fibre.

The support authentication is

```text
scratch/ad_k16_deletion191_novel_phase_supports_20260730.audit.json
SHA-256 7dbec1f8ba999b6711c5215ff8cfc763d5fea71e7b8a36e78446e939d87fb34d
payload 6e2e7f538a60bd3f8e2ed531402ad27490b7e47d82352ec58f2b7da0bba72f77.
```

## 2. Exact arbitrary-value fixed-pool theorem

Let `A=(A_0,...,A_{n-1})` be a word and let

```text
p_0 < ... < p_{s-1}
```

be editable positions.  Every editable value may be any nonzero `k`-bit
mask; every other position retains its literal value in `A`.

Split `A` at the editable positions.  Mark every target already covered by
an interval lying wholly in one fixed run.  Call the remaining set `R`.
For `0<=a<=b<s`, an interval meeting the editable positions exactly in
`p_a,...,p_b` has a fixed OR base of the form

```text
left fixed suffix OR all internal fixed gaps OR right fixed prefix.       (2.1)
```

Let `B_ab` be the finite set of all distinct bases in (2.1).

### Theorem 2.1

For a target `T in R`, the following CNF is satisfiable by the editable-cell
bits if and only if the resulting literal word has an interval of OR `T`:

1. choose `a<=b` and `B in B_ab` with `B subseteq T`;
2. every editable cell `p_a,...,p_b` has no bit outside `T`; and
3. their joint OR contains `T \ B`.

It remains exact after, for each fixed `(T,a,b)`, deleting every need
`N=T\B` which strictly contains another attainable need `N'`.

#### Proof

Every interval meeting the editable pool has a unique first and last
editable index.  Its fixed part is exactly a suffix, the complete intervening
gaps and a prefix, hence has one of the bases (2.1).  Its OR is `T` precisely
when the editable cells contain no forbidden bit and together supply every
bit of `T\B`.  This proves both directions before minimization.

If `N' subseteq N`, every editable assignment supplying `N` also supplies
`N'`.  The base which generated `N'` is attainable and contains all bits of
`T\N'`; together with the editable cells its interval therefore has OR
exactly `T`.  Thus the larger-need term is redundant.  Conversely, any
deleted literal witness satisfies a surviving contained need and hence gives
another literal witness of the same target.  This proves exactness after
minimization.  Targets outside `R` retain their fixed-run witnesses, so one
such row for every `T in R`, plus cell-nonzero clauses, is equivalent to full
universality.  ∎

This is an occurrence theorem.  It preserves the physical chronology and
does not replace interval OR by target marginals or an outer Hall proxy.

## 3. The exact adaptive-six formula

The audited formula allows arbitrary nonzero values at every position of
`P`; any subset may retain its incumbent value.  There is no edit-budget
restriction inside these six positions.

```text
scratch/ad_k16_global12873_novelh2_adaptive6_20260730/model.cnf
SHA-256 da5261a32929063bdb40461ae77b71fab616f6e25c2f01826d847a073d75e40c

scratch/ad_k16_global12873_novelh2_adaptive6_20260730/model.map
SHA-256 a916d0425c7246f877533d29b1989f442371bc602e954f7276edbd1c700dcef6

scratch/ad_k16_global12873_novelh2_adaptive6_20260730/model.stats.json
SHA-256 a622ae31a49ace5d52868b0e69b7478b399793da6e0b07c1b3ae5dce22b1e802.
```

The exact census is

```text
fixed-only covered targets       65,495
repair targets                       40
consecutive editable blocks           21
distinct fixed bases                 190
maximum bases in one block            46
witness terms                         360
maximum terms for one target            9
structurally impossible targets         0
variables                             462
clauses                             6,509
literals                           14,419.
```

The independent auditor does not import the emitter.  It recomputes the
source holes, fixed-run coverage, all 190 bases, every minimized need, all
variables, the complete map and all 6,509 normalized clauses in order.  Its
result is

```text
scratch/ad_k16_global12873_novelh2_adaptive6_20260730/model.independent.audit.json
SHA-256 c254bdecde25d22491d9c5d9aa50d303aa76fe40c0393bc34fa40b7947319ed1
payload d947c8239d2b8e2daf5ed9f1a91bf01a0d571e4b7d98b27a09c813c1973143ee
status PASS_EXACT_EQUISAT_SCOPED_MODEL_UNSOLVED.
```

The emitter and decoder sources are pinned as

```text
scratch/k16_dynamic_unbounded_substitution_cnf_20260730.cpp
SHA-256 5d40fc37e1b1caea5992049887204a8224589b48f91ab7b5c6d7531efdc503a1

scratch/k16_12873_fixed_substitution_cnf_20260730.cpp
SHA-256 c660cae1f5915f23a783fc371177cbe90f0206830d2fb83be92bd0c17a964cb8

scratch/decode_verify_k16_dynamic_unbounded_substitution_20260730.py
SHA-256 37bbd13953c1f2f43531d7588925b30d1845f6cf849fdbf00c17690231908c85.
```

The decoder is fail-closed: it requires an explicit `SATISFIABLE` status, a
complete assignment of exactly the mapped variables, nonzero decoded cells,
and agreement of every change indicator.  It then ignores the claimed
witness bits and directly replays the physical word over all `65,535`
nonzero targets before writing an output.  A SAT solver transcript alone is
not a certificate.

## 4. Global 191-root branch decomposition

For each of the 191 deletion roots `D_d`, let `P_d` be its retained
provider-derived `top_support` pool, of size at most 63.  For
`b in {1,2,3,4}`, let `Phi(d,b)` be the exact formula of Theorem 2.1 with
the additional equality

```text
exactly b cells of P_d differ from their incumbents.                    (4.1)
```

The change indicators are exact bitwise equivalences, and (4.1) is encoded
by an equivalence-complete prefix counter.  Thus `Phi(d,b)` retains arbitrary
nonzero values rather than a provider menu.

### Theorem 4.1 (proof-composable portfolio)

There exists a universal length-`12873` word in one of the 191 retained
topology pools at substitution radius at most four if and only if at least
one of the `764` formulas `Phi(d,b)` is satisfiable.

#### Proof

Given a word in the stated union, its deletion root and its exact positive
change count determine one branch, and Theorem 2.1 supplies a satisfying
assignment.  Conversely a satisfying branch decodes to that literal
deletion root with exactly the mapped changes and is universal by Theorem
2.1.  The root and budget alternatives are a finite disjoint union, so no
root-selector variables are needed.  ∎

Solving the branches separately is strictly smaller in peak model size than
concatenating all guarded branch clauses into one monolithic CNF.  A SAT
branch is immediately sufficient after physical replay.  A scoped UNSAT
claim requires a checked proof for every branch; a timeout or missing proof
leaves the portfolio UNKNOWN.

The frozen manifest additionally places three phase pools on the novel H2
parent ahead of the 191 roots, giving 776 jobs total:

```text
scratch/ad_k16_global_adaptive_deletion_portfolio_20260730.manifest.json
SHA-256 86101dd39a768981269422ff9d2b4fe25b0d421ad8eb4b9f5ad8f0f00d847dfa
payload 04ba3d19750bc04dda6681b3f8166f311d42dad6f5a15306ff8b2675f135d09d.
```

The builder independently replays every one of the 191 root hole sets and
pins the hash of every virtual shortened word:

```text
scratch/build_ad_k16_global_adaptive_deletion_portfolio_20260730.py
SHA-256 715b7a59243891d9ec81463e3c9b9ddefc668f9c97e8f6db1c011d471223838f.
```

## 5. Exact boundary

The adaptive-six formula is complete only for its six physical positions.
The 191-root portfolio is complete only for change radius at most four inside
each retained `top_support` pool.  Provider topology is used to order and
choose pools; it is **not** used as an unsound claim that every successful
joint rewrite contains a one-cell provider.  In particular, the known
partial-provider-first circuits remain a warning against such a WLOG claim.

The completeness ladder is nevertheless exact: enlarge `P_d`, then raise
the change budget.  At the limiting pool of all `12873` positions, budgets
through `12873` cover every word obtainable from that deletion root; allowing
all deletion roots contains every length-`12873` word.  No finite stage short
of that limit is claimed global-WLOG.

