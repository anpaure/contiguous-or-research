# K=16: exact two-edit blocker-fortification audit

## Result

Five independent length-12874 one-hole basins were audited around the three
observed phase labels

\[
H=0x287d=10365,\qquad E=0x4e63=20067,\qquad A=0xa879=43129.
\]

No audited two-substitution configuration is universal.  In every basin the
best exact residual is two holes.

This is a scoped finite theorem, not a heuristic statement.  It has two
complementary parts.

### 1. One edit installs the blocker

For every arbitrary nonzero replacement which individually installs the input
hole, every arbitrary second replacement capable of installing all of those
debts was tested with exact interval-OR multiplicities.  The designated
finishing portal was excluded where relevant.  This includes all debt tiers;
the observed maximum was 20.

| basin | blocker | first rows | exact second-stage pairs | best residual |
|---|---:|---:|---:|---:|
| append portal phase | `A` | 27,712 | 332,488 | 2 |
| five-phase `E` | `E` | 26,788 | 66,869 | 2 |
| finished `E -> H` phase | `H` | 26,782 | 1,002,145 | 2 |
| annealed rex3 `H` | `H` | 27,243 | 1,036,894 | 2 |
| annealed rex4 `A` | `A` | 28,329 | 545,388 | 2 |

Total: **2,983,784 exact provider pairs**.  The detailed catalogs are
`scratch/twoedit_*_full.audit.json`.

The earlier one- and two-debt subtiers are separately persisted.  In
particular, the complete one-debt tier contains 1,112,624 exact pairs across
the finished-H, rex3-H, and rex4-A basins and has no completion.

### 2. The two edits create the blocker jointly

If neither edit individually creates the blocker, any new blocker witness must
contain both edited cells.  Therefore all unchanged cells strictly between the
two positions are subsets of the blocker, and both replacement values are
nonzero blocker submasks.  This gives an exact small position-pair catalogue.

For each position pair, the audit enumerates every replacement pair for which
the maximal blocker-compatible extension has OR equal to the blocker.  It then
uses the exact private-target criterion: only intervals containing one of the
two positions change, so coverage is preserved iff the new affected intervals
contain every target whose complete old witness set met those positions.

The new blocker witness is required not to cross the designated finishing
portal.

| basin | position pairs | replacement pairs | best residual |
|---|---:|---:|---:|
| append portal phase | 13,217 | 102,022,618 | 2 |
| five-phase `E` | 13,236 | 102,140,776 | 2 |
| finished `E -> H` phase | 13,235 | 102,219,492 | 2 |
| annealed rex3 `H` | 13,256 | 103,082,137 | 2 |
| annealed rex4 `A` | 13,238 | 103,060,474 | 2 |

Total: **512,525,497 exact replacement pairs**.  The detailed catalogs are
`scratch/joint2_*.audit.json`.

Independent full recomputation of the best child in every catalog reproduces
its recorded two-hole set exactly.  The recurring best residual doublets are

\[
\{43117,44141\},\quad \{10349,11373\},\quad
\{10361,10365\},\quad \{43129,43133\},\quad
\{10553,10557\}.
\]

## Exact scope: the full external radius-two theorem

Together the two audits exhaust every pair of substitutions that can produce a
new blocker witness external to the finishing portal.  Indeed, any new blocker
witness contains either:

1. both edits, which is exactly the joint audit; or
2. only one edit, in which case that edit individually installs the blocker and
   is exactly a first row of the provider audit.

Thus the two audits exhaust:

1. all pairs whose blocker witness contains both edits and avoids the finish
   portal; and
2. all pairs in which one edit individually installs the blocker and the other
   edit repairs every collateral hole, with no debt cutoff.

Therefore no pair of substitutions, away from the fixed finishing portal, can
fortify and close any of the five audited E/H/A basins.  This is an
unrestricted external radius-two impossibility theorem for those five words.

The two enumerations overlap on some pairs, so their counts should not be added
as a count of distinct configurations.  Computationally they authenticate
512,525,497 joint-witness replacement pairs and 2,983,784 common-provider
pairs.

## Implementations

- `scratch/search_k16_exact_two_edit_blocker_fortification_20260730.cpp`
- `scratch/search_k16_exact_joint_two_edit_blocker_20260730.cpp`

Both implementations use exact multiplicities.  Any zero candidate triggers a
fresh start-by-start replay over all 65,535 nonempty targets before being
written.

The frozen source-and-audit hashes are in
`scratch/k16_exact_radius2_blocker_20260730.sha256`.
