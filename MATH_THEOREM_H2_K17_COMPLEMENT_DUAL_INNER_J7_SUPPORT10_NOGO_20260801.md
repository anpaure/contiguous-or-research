# K17 complement-dual seed: inner-J7 support-ten obstruction

Date: 2026-08-01  
Lane: H2 independent checker  
Status: **exact source-relative support-ten no-go; no run9 or global K17 claim**

## 1. Verdict

Fix the complement-dual incidence factor

```text
scratch/threadD_k17_complement_dual_splice_20260801/seed.best.tsv
SHA-256 a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3
```

Its owner permutation `A` and factor successor `A^2` both have quotient
components of lengths `1429,1`; the factor component voltages are `4,9`
modulo 17.  Both immediate turn palettes are complete.

There is no labelled successor exchange changing at most ten quotient tails
which

1. contains either literal orientation of
   `30844 -> 26750 -> 27246`;
2. retains exactly the old head-orbit set and rank-eight facet-orbit set on
   the changed tails.

The exhaustive catalogue ended normally after `728874` nodes and found zero
owner/facet-exact leaves in both orientations.  Therefore topology, voltage,
rank-ten/rank-seven turn palettes, nonduality and residence were never
reached; their zero counters are vacuous.

This computation is a deterministic exhaustive C++ census, not a SAT/DRAT
certificate.

## 2. Human completeness proof

Let `sigma` be the old successor, `lambda` its bijective rank-eight facet
label, and `S` the changed tails.  If a new arc from a tail in `S` uses head
`v`, the unique old predecessor `sigma^{-1}(v)` must also lie in `S`.
Likewise, if it uses facet `f`, the unique old tail carrying `f` must lie in
`S`.  These are necessary closure rules.

The catalogue starts with either exact J7 pair

```text
forward: 30844 -> 26750 (delta 9), 26750 -> 27246 (delta 7)
reverse: 27246 -> 26750 (delta 10), 26750 -> 30844 (delta 8)
```

whose lower labels are `26748,26734` and upper labels are
`30846,27262`.  At every unassigned forced tail it enumerates all 72
labelled quotient Johnson arcs, rejects only a repeated head/facet or a
closure larger than ten, and adds precisely the two forced old owners above.
At a leaf it requires

```text
new heads on S  = old heads on S,
new facets on S = old facets on S.
```

Any valid exchange of support at most ten therefore determines a branch
which is never pruned.  Exhausting all branches with no leaf proves the
stated no-go.

## 3. Independent residence cross-check

The earlier claim that 219 disjoint *boundary pairs* force 219 changed tails
is invalid: changing an internal tail can disrupt a short run without
changing either boundary tail.  It must not be cited.

The corrected certificate uses complete unchanged spans.  Eleven explicit
pairwise tail-disjoint spans each carry a literal `0 1 1 0` fragment.  If
at most ten tails change, one whole span remains intact (up to a uniform
deck rotation), leaving a positive run of length two.  Thus support at most
ten is independently residence-impossible for this frozen seed.  The larger
greedy packing of 151 spans is diagnostic; the eleven displayed spans are
the small theorem certificate.

The correction is frozen in

```text
MATH_AUDIT_H2_K17_COMPLEMENT_DUAL_SUPPORT10_RESIDENCE_HYPEREDGE_CORRECTION_20260801.md
SHA-256 6e9bece4243c312e959d4ea6ca4c5410e644cc4847e988376bf2b1cfc8b106ef
```

## 4. Frozen computation and independent audit

The complete H100 bundle is local at

```text
scratch/h2_k17_complement_dual_support10_connector_20260801/
```

Key hashes are

| artifact | SHA-256 |
|---|---|
| frozen C++ source | `bf1dafade59d56530c4cce736b7c400a77b4aa4fd9d11bc99e7c13cb15739692` |
| seed | `a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3` |
| H100 binary | `91ef3e85dda4cc01a3ce94c28c7bd0d851816fff5bad4c80e2f979e5529cf1a3` |
| final JSON | `0cfa7930de8fabc7b8ea1abf516529a4839344695cf305b6ebbf6e890b2e4a0d` |
| empty survivor TSV | `1295bef5b1a18a3881fb5378f9f08ffb39f8f82df501ca9375848eb3e3242f05` |

The run exited `0`, `stopped=false`, with empty compile/runtime stderr.
Independent local replay reproduced exactly `728874` nodes and zero leaves.
The fail-closed independent audit is

```text
scratch/audit_h2_k17_complement_dual_support10_final_independent_20260801.py
scratch/h2_k17_complement_dual_support10_final_independent_20260801.audit.json
```

## 5. Scope

The enumerator does **not** encode target `28926`, the full five-owner collar
`28924 -> 30844 -> 26750 -> 27246 -> 92750`, the run9 cut/socket rows,
ranks at least eleven, source/deep-shadow witnesses, opening or common cap.
Adding such rows cannot rescue this exact empty inner-J7 support-ten face,
but another seed, support at least eleven, or the uncapped run9 model remains
outside the theorem.  No unrestricted K17 conclusion follows.
